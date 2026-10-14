# 1. Finding positions

## Sources

| Source | What | How |
|---|---|---|
| **Chalmers thesis portal** (`ch`) | annonsportal.chalmers.se: thesis ads posted for Chalmers students, many not listed anywhere else | `find_jobs.py -s chalmers`; filtered to the subject areas in `config.json` (`chalmers_subjects`) |
| **LinkedIn** (`li`) | Public job search, any country. Main source for graduate jobs across the EU | `find_jobs.py -s linkedin -l <country>`; personal, low volume only (a few pages per query, pauses between requests). Full ads are often rate-limited (HTTP 429): then open the link in the user's Chrome through the browser tools and read it there |
| **Platsbanken** (`pb`) | Sweden's public employment service (JobTech API, no key) | `find_jobs.py -s platsbanken` |
| Company careers pages | Many employers (Volvo, Ericsson, Saab, Scania, RISE, AI Sweden…) post some roles only there | by hand when the user wants a broad search |
| Any other job board | e.g. EURES or a country's main board | when the user names one, add it as a new source in `find_jobs.py`: study its search URL and result page, implement search and detail, run one live query |
| Job alerts by email | e.g. Teamtailor alerts | read during “查邮件” (`03-tracking.md`) |

```
python3 scripts/find_jobs.py                       # thesis ads, all three sources, Sweden, last 21 days
python3 scripts/find_jobs.py -s linkedin -l Germany -l Netherlands -q "graduate software engineer" --any
python3 scripts/find_jobs.py --detail ch:4836      # one ad in full (ch: / li: / pb:)
python3 scripts/find_jobs.py --mark-seen ch:4834 pb:31552260   # decided against, hide next time
```

Ads already in `applications/log.md` and ids in `leads/seen.json` are left out automatically. After each triage, mark the ads the user decided against as seen, so the next search only shows new ones.

## Triage (before any writing)

1. From the list, pick the ads that plausibly fit the user's directions (see `evidence.md` and `config.json`). Read each one in full with `--detail`.
2. Apply the gates in `02-applying.md` step 0 (clearance or citizenship, language, number of students, location, deadline). For jobs outside Sweden, also look for work-permit wording: “must have the right to work in …”, “no visa sponsorship”, “EU citizens only” fail; silence means check the employer's careers page.
3. Give the user one ranked table: rank, role and employer, fit score (step 2b of `02-applying.md`, with the one main reason), gate problems, deadline (🔥 within 7 days; when two sources disagree, use the earlier date), one honest strength and one gap. Recommend which to apply for and say why the others are not worth it.
4. Check where the application link goes. The employer's own site or a known applicant system (Workday, SmartRecruiters, Teamtailor, Varbi, ReachMee, Greenhouse, Lever, Jobylon) is fine; anything else is named as unverified so the user checks it before applying.
5. After the user decides, mark the rejected ads as seen. Recommended ads not yet decided go into the user's todo list with their deadline.
6. When an ad names a contact and there is a real question (English OK? two students? location?), offer a short email draft for the user to send.

## Graduate jobs abroad

Same flow, plus:
- Search LinkedIn by country (`-l Sweden -l Netherlands -l Germany …`) with role keywords and `--any`.
- Language gate per country: the role's working language, not the language of the ad. A German ad for an English-speaking team is fine; “fließend Deutsch” is a gap to flag.
- Work-permit gate (triage step 2). Ask the user about their own permit situation before the first such application and write the answer into `evidence.md`.
- The CV Profile then names the role sought and the graduation date instead of a thesis (`02-applying.md`).
