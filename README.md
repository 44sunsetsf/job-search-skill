# job-search — a Claude Code skill for the whole job hunt

English | [中文](README.zh-CN.md)

A [Claude Code](https://claude.com/claude-code) skill that runs a student's job search from finding an ad to recording the outcome. Built for master's thesis positions and graduate jobs in Sweden and the EU, with a stage for Chinese campus recruiting (国内秋招). Written by a Chalmers master's student while applying; the rules come from real applications.

**You stay in control: Claude drafts, checks and reviews; you submit every application and send every email.**

## What it does

| Stage | What happens |
|---|---|
| 1. Find | Searches the Chalmers thesis portal, LinkedIn and Platsbanken (`scripts/find_jobs.py`), removes ads you already saw or applied to, ranks them with a fit score |
| 2. Apply | Eligibility and language gates → matches the ad to **your own evidence file** → tailored one-page CV and cover letter → ATS keyword table, PDF and layout checks → review by a fresh Claude subagent that acts as the hiring manager |
| 3. Track | Application log with git tags (each tag = exactly what was sent), inbox reading, 14-day follow-ups, thank-you notes, outcome reviews |
| 4. Interview | Interview pack per round, consistency brief against the CV you sent, mock interview, written-test prep |
| 5. 国内秋招 | Defaults for Chinese campus applications |
| 6. Writing rules | Natural, honest, “technique + outcome” bullets; Profile that reads like a person |

The central idea is `evidence.md`: every fact in a CV or letter must be recorded there first, so the model never invents a claim you cannot defend in an interview.

## Install

```
git clone https://github.com/44sunsetsf/job-search-skill
ln -s "$PWD/job-search-skill/skills/job-search" ~/.claude/skills/job-search
```

Then say “帮我初始化求职工作流” (or “set up the job-search workflow”) in Claude Code. It copies `templates/materials/` to a folder of your choice (make it a **private** repo), writes `skills/job-search/config.json` (see `config.example.json`) and interviews you to fill `evidence.md`.

Needs `python3`, and for CVs a LaTeX engine such as `tectonic` plus `pdftotext` (poppler).

## Layout

```
skills/job-search/   SKILL.md + 01…06 stage files, references/, scripts/
templates/materials/ starter folder for your own materials (evidence, log, …)
```

## Credits

Several stages and checks are adapted from [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) (MIT); its `verify_pdf.py` and `verify_layout.py` are vendored in `scripts/vendor/` with its licence. The CV and letter principles follow university career-service guidance (Chalmers Career Services).

Job-board scraping (`find_jobs.py`) is for personal, low-volume use; respect each site's terms.

MIT licensed.
