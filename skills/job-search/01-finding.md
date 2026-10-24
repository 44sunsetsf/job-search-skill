# 1. Finding positions

## Sources

| Source | What | How |
|---|---|---|
| **Chalmers thesis portal** (`ch`) | annonsportal.chalmers.se: thesis ads posted for Chalmers students, many not listed anywhere else | `find_jobs.py -s chalmers`; filtered to the subject areas in `config.json` (`chalmers_subjects`) |
| **LinkedIn** (`li`) | Public job search, any country. Main source for graduate jobs across the EU | `find_jobs.py -s linkedin -l <country>`; personal, low volume only (a few pages per query, pauses between requests). Full ads are often rate-limited (HTTP 429): then open the link in the user's Chrome through the browser tools and read it there |
| **Platsbanken** (`pb`) | Sweden's public employment service (JobTech API, no key) | `find_jobs.py -s platsbanken` |
| **Company careers pages** (`cr`) | Many employers post some roles only there | `find_jobs.py -s careers` reads every company in `references/target-companies.json` (Teamtailor, Jobylon, SuccessFactors and Workday pages; fetcher from [job-scan](https://github.com/1carusalwayswa/job-scan), MIT). Edit the list to your own targets. Pages under `browser_only` render with JavaScript: open them in a browser |
| Any other job board | e.g. EURES or a country's main board | when the user names one, add it as a new source in `find_jobs.py`: study its search URL and result page, implement search and detail, run one live query |
| Job alerts by email | e.g. Teamtailor alerts | read during “查邮件” (`03-tracking.md`) |

```
python3 scripts/find_jobs.py                       # thesis ads, all three sources, Sweden, last 21 days
python3 scripts/find_jobs.py -s linkedin -l Germany -l Netherlands -q "graduate software engineer" --any
python3 scripts/find_jobs.py -s careers            # thesis ads on target companies' own careers pages (--any: all jobs)
python3 scripts/find_jobs.py --detail ch:4836      # one ad in full (ch: / li: / pb: / cr:<url>), gate check on top
python3 scripts/find_jobs.py --mark-seen ch:4834 pb:31552260   # decided against, hide next time
```

Ads already in `applications/log.md` and ids in `leads/seen.json` are left out automatically. After each triage, mark the ads the user decided against as seen, so the next search only shows new ones.

## Triage (before any writing)

1. From the list, pick the ads that plausibly fit the user's directions (see `evidence.md` and `config.json`). Read each one in full with `--detail`.
2. **Gate column first.** The list's 门槛 column and the first line of `--detail` come from `scripts/vendor/job_scan_gates.py` (from job-scan): fixed patterns for a Swedish hard requirement, citizenship or security clearance (signal words and restricted defence employers), work-permit wording and staffing agencies (bemanning). Lines marked as merit or nice-to-have are exempt. job-scan's author found prompt-only gating unreliable (the model wrote “exclude” and still scored the ad high), so quote every hit in the table. A staffing hit is a cap (step 3), not a fail. “未发现” still means read the ad: the patterns can miss things.
   Then apply the gates in `02-applying.md` step 0 (clearance or citizenship, language, number of students, location, deadline). For jobs outside Sweden, also look for work-permit wording: “must have the right to work in …”, “no visa sponsorship”, “EU citizens only” fail; silence means check the employer's careers page.
3. Give the user one ranked table: rank, role and employer, fit score (step 2b of `02-applying.md` with its caps, and the one main reason, naming a hit and a gap), gate problems, deadline (🔥 within 7 days; when two sources disagree, use the earlier date), one honest strength and one gap. Recommend which to apply for and say why the others are not worth it.
4. Check where the application link goes. The employer's own site or a known applicant system (Workday, SmartRecruiters, Teamtailor, Varbi, ReachMee, Greenhouse, Lever, Jobylon) is fine; anything else is named as unverified so the user checks it before applying.
5. After the user decides, mark the rejected ads as seen. When the user disagrees with a score, add a row to `references/fit-calibration.md` and read that file before every later scoring. Recommended ads not yet decided go into the user's todo list with their deadline.
6. When an ad names a contact and there is a real question (English OK? two students? location?), offer a short email draft for the user to send.
7. **Referral links** (adapted from ai-job-search Step 4.5). For every job (not thesis ads, which already name a supervisor) rated high or medium fit, add two LinkedIn people-search links to its row, so the user can look for a referral or a warm intro:
   - recruiters: `https://www.linkedin.com/search/results/people/?keywords=<url-encoded "<Company> recruiter">&origin=GLOBAL_SEARCH_HEADER`
   - team peers: the same URL with `"<Company> <short role keyword from the title>"`.
   These are links for the user to open; never fetch or scrape the result pages, and never name a person as found. If the user picks someone, draft a short message for the user to send.

## Graduate jobs abroad

Same flow, plus:
- Search LinkedIn by country (`-l Sweden -l Netherlands -l Germany …`) with role keywords and `--any`.
- Language gate per country: the role's working language, not the language of the ad. A German ad for an English-speaking team is fine; “fließend Deutsch” is a gap to flag.
- Work-permit gate (triage step 2). Ask the user about their own permit situation before the first such application and write the answer into `evidence.md`.
- The CV Profile then names the role sought and the graduation date instead of a thesis (`02-applying.md`).
