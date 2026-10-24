#!/usr/bin/env python3
"""Deterministic gates for job ads: Swedish language, citizenship / security clearance, staffing agencies.

Adapted from 1carusalwayswa/job-scan (MIT, see LICENSE-job-scan), commit 8284984 (2026-09-12):
lang_gate.py, citizenship_gate.py and the staffing half of pre_gate.py, merged into one module with the
JSONL plumbing and scores removed. Their reason for doing this with regexes instead of a prompt: prompt-only
gating failed three times in a row (the model wrote "exclude" in its reason but scored 76-82).
Local additions: the work-permit patterns (EU graduate jobs), "bae systems" in the restricted list, Platsbanken's
structured must-have languages and occupation fields (as in their lang_gate.py and pre_gate.py), and the profile-gap
groups of their profile_gap_gate.py read from job_scan_data/profile_gaps.json.

Prefers false negatives (left to the model's own reading) over false positives: a phrase inside a
merit / nice-to-have line or section is exempt.

    python3 job_scan_gates.py --employer "Saab AB" < ad.txt     # prints one line per gate hit
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "job_scan_data"

# ---------- Swedish language (lang_gate.py) ----------

LANG_PATTERNS = [
    r"flytande\s+(i\s+|på\s+)?svenska",
    r"svenska\s+(flytande|i\s+tal\s+och\s+skrift|i\s+både\s+tal\s+och\s+skrift)",
    r"god\s+kommunikativ\s+förmåga\s+på\s+svenska",
    r"goda\s+kunskaper\s+i\s+svenska\s+(i\s+)?(tal\s+och\s+skrift|både)",
    r"\bsvenska\b[^.\n]{0,35}\btal\s+och\s+skrift\b",
    r"obehindrat\s+på\s+svenska",
    r"(fluent|fluency)\s+in\s+swedish",
    r"(professional|native|excellent)\s+(level\s+of\s+)?swedish",
    r"swedish[^.]{0,45}(in\s+speech\s+and\s+writing|verbally\s+and\s+in\s+writing|"
    r"in\s+writing\s+and\s+speech|spoken\s+and\s+written|both\s+spoken\s+and\s+written)",
    r"(speak|write|communicate)[^.]{0,30}fluently\s+in\s+swedish",
    r"\b(converse|communicate|conversational|proficiency)\s+(in\s+)?swedish\b",
    r"ability\s+to\s+converse[^.]{0,20}swedish",
]
LANG_EXEMPT_NEAR = re.compile(
    r"meriterande|är\s+ett\s+plus|is\s+a\s+plus|önskvärt|fördel|nice\s+to\s+have|"
    r"collective\s+agreement|kollektivavtal|or\s+english|eller\s+engelska|swedish\s+(university|company|market)|"
    r"(additional\s+)?merits?\b",
    re.IGNORECASE,
)

# ---------- citizenship / clearance (citizenship_gate.py) ----------

CLEARANCE_PATTERNS = [
    r"säkerhetspröv",
    r"säkerhetsskydd",
    r"säkerhetsklass",
    r"svenskt\s+medborgar(skap|e)",
    r"krav\s+på\s+(svenskt\s+)?medborgarskap",
    r"swedish\s+citizen(ship)?",
    r"security\s+(clearance|vetting)",
]
SAME_LINE_EXEMPT = re.compile(
    r"meriterande|is\s+a\s+plus|är\s+ett\s+plus|önskvärt|nice\s+to\s+have|(additional\s+)?merits?\b",
    re.IGNORECASE,
)

# ---------- work permit (local addition, for EU graduate jobs) ----------

PERMIT_PATTERNS = [
    r"(no|not\s+able\s+to\s+(offer|provide)|unable\s+to\s+(offer|provide)|cannot\s+(offer|provide))\s+"
    r"(visa\s+)?sponsorship",
    r"\bEU\s+citizens?\s+only\b",
    r"must\s+(already\s+)?(have|hold)\s+(the\s+)?(right|permit|authori[sz]ation)\s+to\s+work",
    r"(valid|existing)\s+(EU\s+)?work\s+permit\s+(is\s+)?required",
]

# ---------- shared section logic ----------

MERIT_LINE_START = re.compile(
    r"^\s*(?:meriterande|(?:additional\s+)?merits?|nice\s+to\s+have|"
    r"preferred\s+(?:qualif|skill)|desired\s+(?:qualif|skill)|"
    r"bonus\s+(?:if|qualif)|plus\s+if\s+you|önskvärd)",
    re.IGNORECASE,
)
REQ_HEADER = re.compile(
    r"\b(krav|requirements?|qualifications?|your\s+background|what\s+we\s+(expect|need)|"
    r"vad\s+vi\s+söker|vi\s+söker\s+dig|befattningen\s+kräver|annat\b|"
    r"what\s+you\s+bring|who\s+you\s+are|övrigt|vi\s+erbjuder|what\s+we\s+offer|"
    r"ansökan|om\s+(tjänsten|rollen|uppdraget)|about\s+the\s+(role|position)|"
    r"uppdragsinformation|startdatum)\b",
    re.IGNORECASE,
)


def _line_around(text: str, start: int, end: int, reach: int) -> str:
    a = text.rfind("\n", max(0, start - reach), start)
    a = a + 1 if a != -1 else max(0, start - reach)
    b = text.find("\n", end, min(len(text), end + reach))
    b = b if b != -1 else min(len(text), end + reach)
    return text[a:b]


def _in_merit_section(text: str, pos: int) -> bool:
    """A short merit header in the 400 characters before pos, with no requirement header after it."""
    start = max(0, pos - 400)
    merit = req = -1
    offset = start
    for line in text[start:pos].split("\n"):
        s = line.strip()
        if s and len(s) < 60 and MERIT_LINE_START.match(s):
            merit = offset
        if REQ_HEADER.search(line):
            req = offset
        offset += len(line) + 1
    return merit != -1 and merit > req


def _first_hit(text: str, patterns: list[str], exempt: re.Pattern, reach: int) -> str:
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            if exempt.search(_line_around(text, m.start(), m.end(), reach)):
                continue
            if _in_merit_section(text, m.start()):
                continue
            return text[m.start():m.end()]
    return ""


def _company_re(name: str, key: str) -> re.Pattern:
    pats = json.loads((DATA / name).read_text(encoding="utf-8"))[key]
    return re.compile(r"\b(" + "|".join(re.escape(p) for p in pats) + r")\b", re.IGNORECASE)


RESTRICTED = _company_re("restricted_employers.json", "company_patterns")
GAPS = json.loads((DATA / "profile_gaps.json").read_text(encoding="utf-8"))

# Platsbanken occupation groups that are IT operations / support rather than development (pre_gate.py's default list)
EXCLUDED_GROUPS = ["drifttekniker", "supporttekniker", "nätverks- och systemtekniker", "chefer inom it", "it-chefer"]
IT_FIELD = "data/it"


def profile_gaps(text: str) -> list[str]:
    """Groups of tool stacks the user lacks that the ad asks for (at least min_hits patterns matched)."""
    if not GAPS.get("enabled"):
        return []
    out = []
    for g in GAPS["groups"]:
        found = sorted({m.group(0) for p in g["patterns"] for m in re.finditer(p, text or "", re.IGNORECASE)},
                       key=str.lower)
        if len(found) >= GAPS.get("min_hits", 2):
            out.append(f"缺技术栈 {g['name']}（{'、'.join(found[:4])}）→ 对口分封顶 {g['cap']}")
    return out
STAFFING = _company_re("staffing_companies.json", "patterns")


def check(employer: str, text: str, must_languages: list[str] | None = None,
          occupation_group: str = "", occupation_field: str = "") -> list[str]:
    """Return one short Chinese label per gate hit, quoting what matched.

    must_languages / occupation_*: Platsbanken's structured fields, when the ad has them."""
    hits = []
    if m := RESTRICTED.search(employer or ""):
        hits.append(f"国籍/安全审查：受限雇主「{m.group(0)}」")
    elif frag := _first_hit(text or "", CLEARANCE_PATTERNS, SAME_LINE_EXEMPT, 80):
        hits.append(f"国籍/安全审查：「{frag}」")
    svensk = [l for l in must_languages or [] if "svensk" in l.lower() or "swedish" in l.lower()]
    if svensk:
        hits.append(f"瑞典语硬性要求：雇主勾选必须语言「{svensk[0]}」")
    elif frag := _first_hit(text or "", LANG_PATTERNS, LANG_EXEMPT_NEAR, 60):
        hits.append(f"瑞典语硬性要求：「{frag}」")
    if frag := _first_hit(text or "", PERMIT_PATTERNS, SAME_LINE_EXEMPT, 80):
        hits.append(f"工作许可：「{frag}」")
    if m := STAFFING.search(employer or ""):
        hits.append(f"中介（bemanning）：「{m.group(0)}」")
    group = (occupation_group or "").lower()
    if group and any(g in group for g in EXCLUDED_GROUPS):
        hits.append(f"职业类别是运维/支持：「{occupation_group}」")
    elif occupation_field and occupation_field.lower() != IT_FIELD:
        hits.append(f"职业类别不是 IT：「{occupation_field}」")
    hits += profile_gaps(text)
    return hits


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--employer", default="")
    a = p.parse_args()
    hits = check(a.employer, sys.stdin.read())
    print("\n".join(hits) if hits else "门槛：未发现")


if __name__ == "__main__":
    main()
