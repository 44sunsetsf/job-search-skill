# 6. Writing rules for every CV

These rules apply to the general (master) CVs and to every tailored copy. The user's own taste overrides them: when the user sets a new rule, add it here.

**Ask before changing a general CV.** Show the user the old and the new text and wait for a yes; the report names every file changed. Tailored copies are exempt.

**Exactly one full page.** After any change, every CV is exactly one page: no spill onto a second page, and not so short that the layout stretches the gaps. Render the PDF to an image and look at it: spacing even, no single-word lines, nothing cramped or empty.

## Rule zero: every sentence must read naturally

Everything must be natural, coherent and sincere: CVs, letters and application answers. When the user points out a weakness, fix it the way a person would actually say it; don't add a sentence engineered to defend against the criticism. Before reporting, read the whole paragraph, not just the changed sentence, and ask: would a real person say this to a recruiter?

- Write sentences a native speaker would write. No telegraphic fragments made by squeezing a line: no noun piles as a subject (“injected parameters and an evidence gate on every conclusion curb hallucination”), no clauses with the verb dropped (“; 9 transitions tested.”, “; answers 32% faster.”).
- Fixes that read well: a purpose or result clause (“Designed the skill engine to reduce hallucination: the framework fills in tool parameters and checks each conclusion against the raw data”), a coordinated verb sharing the CV's implied subject (“…, and tested all 9 transitions”), or a full clause (“it grew from 20 to 130+ internal users”).
- **Cut stock phrases and apologetic wording** (from ai-job-search): “I am passionate about”, “I believe I would be a great fit”, “leverage my skills”, “hit the ground running”, “drive results”, “synergies”. Not “I think I could contribute” but “I bring X, shown by Y”. Every buzzword needs a concrete example or goes. Long em-dashes in letter prose read as machine-written; use a comma or a full stop.
- **Every bullet starts with a strong past-tense verb**: Built, Designed, Implemented, Orchestrated, Engineered, Hardened, Offloaded, Enforced, Automated, Optimised, Cut, Reduced. Never a weak opener: Made, Used, Did, Set up, Worked on, Helped, Handled, Was responsible for, Participated in. For team work, name your own part in the sentence instead of opening with “Helped”. No bold labels such as “**Agentic RAG:**”; keep the ad's keywords inside the sentence, bolding one or two where useful. Chinese CVs follow the same idea (open with 设计、实现、构建…, never 负责、参与、协助 or 基于、采用), without bold in the bullets.
- When a fluent sentence no longer fits, cut a less important detail or let the bullet run to two full lines. Never compress grammar to save space.

## How a bullet reads

Write **technique + outcome** and leave hooks for the interviewer to ask about; method and process belong in the interview, not on the page.

- Each bullet is a coherent sentence, not a chain of noun phrases. Use verbs that link mechanism to outcome. Aim for one line; if the content needs more, split it or let it run to **two full lines**. Never leave a 1–3 word tail on a line of its own. Only the richest one or two bullets per section get two lines.
- Each bullet reads technique → the pain point it solved or the gain it brought, with a number where a real one exists.
- Professional terms are expected; drop jargon only you use.
- Write the current design as if it had always been that way: no “rewrote / upgraded / from X to Y” framing.
- Add a metric only when it is natural and solid. Never force one; a weak-looking absolute number is better left for the interview.
- Keep every hook word your interview notes have an answer for; cut connecting words first, then modifiers, then lower-value detail. Removed detail must still exist in the notes as a follow-up answer.
- Team projects: say so (“team project … my parts”), and claim only the user's own parts.

## English CV layout rules

- One page. Single column, simple bullets, standard section names, no icons or text in images (ATS reads text only).
- **Section order: Profile → Experience → Education → Projects → Skills and Languages.** Work experience before education.
- Contact: name, phone, professional email, LinkedIn, city. No address, age, gender, nationality or personal ID number. Photo optional.
- Experience and Education use a one-line heading, “**Role** — Company” with the dates on the right, then a small detail line.
- Projects: title row “Name | stack”, then one short positioning line, with a demo link and a GitHub link when the project is live. No trailing “Skills:” bullet.
- **Date ranges use a plain ASCII hyphen** (`Jun 2026 - Sep 2026`), never `--` (it becomes an en-dash in the text layer and some applicant systems drop the dates). Keep `--` in prose ranges.
- Name the file `Firstname_Lastname_CV.pdf`, never `CV_final_v7`.

## English Profile

About three rendered lines, written like a person introducing themselves, not a formula: one short sentence for the thesis or role, one real fact, one sentence of personality.
1. **Who and what:** “I am an MSc student at <university> looking for a spring 20XX thesis on …”. Don't repeat the programme name; Education shows it.
2. **One or two real facts** that fit the role, said plainly.
3. **Personality, with real weight, from the angle of what I bring to a team** (“I am curious, patient and a good listener, and I get along well with people from different backgrounds”). Use plain traits a person says when introducing themselves, not working habits or professional ideals (“ask questions early”, “would rather say ‘I'm not sure’ than guess”). Pick traits that fit the team's vibe as the ad describes it. They need no professional evidence, but they must be true and not exaggerated.

   **When the field is new to the user** (for example vehicles or heavy machinery for a software student), the first or second sentence names the transferable link between their background and the ad's problem; it is the strongest card a newcomer has, so don't leave it to the letter.

What goes wrong, so don't repeat it:
- Personality written as work habits or a slogan.
- Too much technology and too little personality: don't pile the ad's terms into the thesis sentence or turn the fact into a feature list.
- Three disconnected claims.
- Forced connectors (“led me to”, “Curious by nature, …”).
- **Choosing the team instead of fitting it** (“I enjoy teams that share ideas freely…”). The angle is that the user's personality suits the team.
- Backing each trait with a project, or repeating the degree name.
- Sounding dependent (“learning a new domain from experts”), and then over-correcting with a crafted defence. Say it simply: “Vehicles are new to me, but I enjoy digging into a new field and would start reading right away.”

## Build and check (general CVs)

1. Compile every CV PDF; each must be **exactly 1 page**. If one overflows, shorten bullets rather than drop links.
2. Check wrapping with `pdftotext -layout`.
3. Check links are clickable: `pdfinfo -url <pdf>`.
4. Run `scripts/check_bullets.py` and the two checkers in `scripts/vendor/`.

## After changing a general CV

Update everything that quotes it: the website or portfolio copy, any tracker or autofill tool that reads it, and the user's interview notes (the quote and the hook-word table), then commit them together.

## Review pass for the general CVs (optional, after a big rewrite)

Read only the PDF text as a recruiter would for 30 seconds and write down (1) who the candidate is, what they built and with what result, (2) which lines are filler or hide the strongest evidence, (3) what would stop an interview. Fix only with true material. Tailoring to a specific ad belongs to `02-applying.md`.
