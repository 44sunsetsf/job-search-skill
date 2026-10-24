# Vendored from MadsLorentzen/ai-job-search (MIT, see LICENSE-ai-job-search)

Copied 2026-10-14 from https://github.com/MadsLorentzen/ai-job-search `tools/`.

- `verify_pdf.py` — page count, clean text layer, `--ascii-dates` (en-dash in dates breaks some ATS imports), `--contains`.
- `verify_layout.py` — holes, pages ending early, stranded headings. Local change: `--footer-band` (default 90 pt, theirs); our CVs and letters have no footer, so we call it with `--footer-band 0`.
- `posting_guard.py` + `page_decode.py` (added 2026-10-24) — cleans a job ad before the model reads it: removes hidden HTML and invisible / Unicode tag characters, quotes instruction-like lines. Advises, never blocks.

Updated 2026-10-24 to upstream `e16acee3abda` (`verify_pdf.py` `--ascii-dates` fixes). `verify_layout.py` kept at the 2026-10-14 copy.
