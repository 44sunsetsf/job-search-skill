# 4. Interviews and written tests

Adapted from ai-job-search's interview guide. The core rule: **the interviewer has read the CV and letter that were sent, so nothing said in the room may contradict them, and every claim on paper must hold up when probed in depth.**

## When an interview is booked

1. **Load what was sent:** the tag of that application (`JD.md`, CV, letter), plus notes and feedback from earlier rounds in the interview folder. Feedback from round N is the most valuable input for round N+1.
2. **Ask only what is not recorded:** the stage (screening / technical / case / final / thesis supervisor meeting), date and time (in the user's local time), format, and who interviews.
3. **Research, verified.** Use `companies/<company>.md` if under 30 days old; otherwise check the company's own pages and update it with URLs and the date. For each interviewer, only public professional information. Their role tells the likely angle: **HR** checks the timeline, motivation and logistics; **a hiring manager or supervisor** checks motivation, team fit and how the user works; **an engineer or researcher** checks technical depth. Two or three verified, recent facts become “why this company” hooks.
4. **Build the pack** in `interviews/<company>-<id>/round-N.md`. One file per round; earlier rounds stay as history.

## The pack, in this order

1. **Header:** date and time, format, interviewers and their likely angle.
2. **Consistency brief:** the claims in the sent CV and letter most likely to be probed (numbers, “I built…”, stretches), each with where the user's own notes answer it. Team-project scope stated plainly.
3. **Self-introduction** (“tell me about yourself”), tailored to this ad: see the next section.
4. **Likely questions, by priority:** (1) anything doubted or left open in an earlier round; (2) **the gaps** from the requirement table, each with an honest bridge answer: acknowledge → closest real experience → how the user would learn it, never an invented answer; (3) each requirement in the ad; (4) the stage type: screening = motivation, availability, timeline; technical = the ad's stack and the user's projects in depth; final = values, “any concerns”, salary or start date; thesis supervisor = research question, method, how the user works with a supervisor.
5. **Story mapping:** for each behavioural question pick a story from the user's story library (`handbook/`). If none fits, draft one strictly from recorded facts (situation, task, action, result, lesson) and add it to the library only if the user approves.
6. **Why this company / why this thesis:** from the verified hooks, never generic.
7. **Questions to ask (4–6)**, matched to the stage; drop any the public material already answers.
8. **Practical:** test the call link and camera, notes allowed or not, key English phrases and hard words for the topic with pronunciation.

## “Tell me about yourself”

It is almost always the first question, at every stage, and it sets the tone. Every pack has one tailored to the ad (user decision 2026-10-19). The approach is the one common in US big-tech interview prep (Tech Interview Handbook, GreatFrontEnd behavioural guide):

- **Present → past → future.** *Present:* who the user is now and their direction, in one or two sentences. *Past:* **only the 2–3 experiences that best match this ad**, never the CV read top to bottom; each one gets one concrete detail, such as what was built or a number. *Future:* why this role or thesis is the natural next step. Close on the ad's own words so it leads into “why us”.
- **45–60 seconds** (about 120–150 words), never over 2 minutes. Use the short end for screening calls and thesis supervisor meetings, which are more conversation than test.
- **It agrees with what was sent.** Pick from the sent CV and letter. If the intro mentions something they don't contain, flag it in the pack. Team projects are said as team work (“in a team”), and the user claims only their own part.
- **Short, plain sentences** the user can say naturally (at the user's level of English), with hard words and their pronunciation.
- **Teach the structure, not the script.** The pack has the script plus a one-line cue, for example “now → two matching experiences → so this role”. The user says it aloud without the script, then types their own version. Claude polishes that version toward how the user naturally speaks, rather than making them memorise Claude's wording.

## Mock interview (when the user wants one)

In chat: warm-up (“tell me about yourself”), the role's technical questions, one or two behavioural questions tied to the ad's competencies, then one hard or unexpected question. After each answer: what worked, what to sharpen, which story would have fit better. Coach toward how the user naturally speaks. English interviews in English, with corrections in the user's own language.

## After the interview

- Same day: record the questions asked, the user's impression and any feedback, verbatim, at the bottom of that round's file; update the log; offer the thank-you note.
- New facts the user remembers while preparing go into `evidence.md` in the same turn.

## Written tests and online assessments

A folder `tests/<company>/prep.md` with the time in the user's local time, the deadline for any practice run, the device and room rules from the notice, what the test covers (marked “to verify” until confirmed from the official notice), and a day-by-day plan up to the test. Never copy access codes into the file. After the test: format and impressions only; never write down or share the questions, which test rules usually forbid.
