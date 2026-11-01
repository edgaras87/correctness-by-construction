# LES: Lessons, what ships (layer 6, 62 files), at 70404e1

Reader LES. Finding Kind: Lessons, a case written as the rule.
All 62 files read whole; the worked example once (the two copies are byte-identical).

The rule, for every finding below: `docs/conventions/conventions/` §2.6, *A lesson taken*. "A finding taken into a manual is written as what it teaches, not as the case that taught it. The body states the lesson in general ... Another convention, or one project's detail, may appear as an example. The statement never stands on it." DECISION-7 (c) reaches the files derived from a convention in both seats, and sent the method's and the stack's texts to the plain rewrite; DECISION-16 made Refinement Round 3 that rewrite. ADR-0073: "A run never reads our origins." A shipped file cannot point at our devlog or ADRs, so it needs no story line.

All 18 findings are in the Stack Group. One cause covers them all (*Why it was missed*, the same in each):
- FINDING-223 (the harness reference's "passes", variation point 9's own history) and FINDING-224 (the "lived" markers) were sent to the plain rewrite by DECISION-7. Then DECISION-16 sent them to Round 3's layer 6. The refinement file's Round 3 *Endings* says they "are worked in this round's layer 6".
- No commit in *The work* cites either of them.
- The rewrite commits turned "the third pass", "lived once" and "lived twice" into "the latest CBC Run", "One CBC Run" and "Two CBC Runs". They kept the cases. The Round 3 commits were `a6ccf5b`, `c449de0` and `580f7dc`. The close read's commits were `63bb1db` and `1f13fee`.
- Round 3 read only the Writing Finding Kind, so nothing read these lines for Lessons after DECISION-16.

Each finding names the commit that last wrote its line.

## The Stack Group: cbc-bootstrap

**LES-1.**
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *The boundary you must keep — WHAT before HOW*, lines 36–39.
- **Quote:** `This rule was written from a practice with two roles: one decided`
- **The rule:** §2.6 above. The case goes to history and the body states the lesson.
- **What the text says:** the paragraph tells where the rule came from: a practice with two roles. That is an origin story, which a CBC Run never reads (ADR-0073). The lesson in it is general: one agent does both jobs, and the boundary between Agent Skill Stages keeps them apart. It is FINDING-224's "distilled from a two-seat discipline", reworded.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change, `c449de0` (the common cause above).
- **Proposed:** fix: "One agent decides both **what** is built, under which constraints, and **how** it is realized in code. The boundary between the Agent Skill Stages keeps the two apart."

**LES-2.**
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 2 — write the CBC Bootstrap Requirements*, lines 146–149. Also *Stage 3 — the CBC Bootstrap Step Plan*, line 178.
- **Quote:** `other manuals. Both CBC Runs that ran this Agent Skill put it at`
- **The rule:** §2.6 above.
- **What the text says:**
  - The default path is given through a count of past CBC Runs. The count goes stale when the next CBC Run runs this Agent Skill.
  - Line 178, "The shape CBC Runs have used is five steps", states the plan's shape the same way.
  - DECISION-40 kept counts like this in the cbc-framing workflow, "since the CBC Run reads it as why the line is required". It is not clear whether its reason reaches a default path or a plan's shape.
- **Stands:** uncertain.
- **Why it was missed:** missed at a change, `c449de0` (line 148) and `a6ccf5b` (line 178).
- **Proposed:** question: does DECISION-40's reason reach this? If not, fix: "The usual place is `docs/construction/`." and "The usual shape is five steps (see the walkthrough's steps):".

**LES-3.**
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, opening, *Why code exists here at all*, lines 23–30.
- **Quote:** `Harness's outcomes, not by the problem. Three CBC Runs produced them`
- **The rule:** §2.6 above.
- **What the text says:**
  - The reason the five files carry code rests on what happened: "Three CBC Runs produced them almost identically, and each one's only route was reading the earlier CBC Run's source."
  - The lesson is already stated in general just before: these five are shaped by the stack and the Adversity Harness's outcomes, not by the problem.
  - "The last CBC Run's source" is a CBC Run the reader cannot place.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change, `63bb1db` (the common cause above).
- **Proposed:** fix: "This file carries code so that no CBC Run has to derive these five from another's source. ... It does not hold for these five, which are shaped by the stack and the Adversity Harness's outcomes, not by the problem, so they come out the same in every CBC Run on this stack." Drop the "Three CBC Runs produced them" sentence.

**LES-4.**
- **Where:** `spring-harness-reference.md`, §1 *The database base*, *Outcomes it realizes*, item 3, line 61.
- **Quote:** `3. the latest CBC Run's correction: **the Database Role Split holds`
- **The rule:** §2.6 above.
- **What the text says:** the outcome is labelled by the CBC Run whose correction it was. The outcome stands without the label. The label is a story line.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `63bb1db` (it was "the third pass's" before `a6ccf5b`). This is FINDING-223's residue.
- **Proposed:** fix: "3. **the Database Role Split holds in evidence runs.** The container is set up by ..."

**LES-5.**
- **Where:** `spring-harness-reference.md`, §1, *Bound facts*, the Database Role Split bullet, lines 144–149.
- **Quote:** `  Harness run as the container's superuser, an earlier CBC Run's`
- **The rule:** §2.6 above.
- **What the text says:** "an earlier CBC Run's shape" says who once did it this way. The lesson ("proves the round-trip but not the authority") stands without it.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `63bb1db` ("the second pass's shape" before).
- **Proposed:** fix: "An Adversity Harness run as the container's superuser proves the round-trip but not the authority."

**LES-6.**
- **Where:** `spring-harness-reference.md`, §3 *The Migration Path Test*, *Bound facts*, first bullet, lines 287–292.
- **Quote:** `  the first Invariant Slice needs V1, the latest CBC Run changed this`
- **The rule:** §2.6 above.
- **What the text says:** what happens to the assertion when the first migration lands is told as what one CBC Run did. It is FINDING-223's "the third pass evolved this to…", reworded.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `63bb1db`.
- **Proposed:** fix: "When the first Invariant Slice needs V1, the assertion becomes "count ≥ 1 and none failed": the count changes, the proof does not."

**LES-7.**
- **Where:** `spring-harness-reference.md`, §3, *Bound facts*, the refused DDL bullet, lines 298–302.
- **Quote:** `  CBC Run met this: a copy wired as the right name but without the`
- **The rule:** §2.6 above.
- **What the text says:** the reason for the refused DDL check comes as a case one CBC Run met. The fact that follows is general, so the case clause adds only a story. It was "(lived once)" before `a6ccf5b` (FINDING-224).
- **Stands:** checked.
- **Why it was missed:** missed at a change, `a6ccf5b`.
- **Proposed:** fix: "**The refused DDL shows the authority, not only the identity.** A copy wired as the right name but without the Database Role Split, the grants missing and `bootstrap.sql` not mounted, passes the identity assertion and fails here, with the Runtime Ground's own message."

**LES-8.**
- **Where:** `spring-harness-reference.md`, §6 *The variation points*, item 4, lines 482–489.
- **Quote:** `   missing location with a warning. An earlier CBC Run caught it in`
- **The rule:** §2.6 above.
- **What the text says:** the two ways to catch a missing migrations directory are told as which CBC Run did which: "An earlier CBC Run caught it in Flyway config ... The latest relied on the Migration Path Test". It was "The second pass closed it", FINDING-223's text.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `63bb1db`.
- **Proposed:** fix: "Two ways work: Flyway config (`failOnMissingLocations(true)`), or the Migration Path Test plus a tracked directory. Catching it nowhere leaves the suite green on a clone that cannot migrate."

**LES-9.**
- **Where:** `spring-harness-reference.md`, §6, item 9, lines 526–530.
- **Quote:** `   once left the rule unsaid, so each CBC Run decided by habit.`
- **The rule:** §2.6 above.
- **What the text says:**
  - The variation point tells its own history: "This file once left the rule unsaid ... One CBC Run met why".
  - FINDING-223 named this: "Variation point 9 tells its own history." It still does.
  - The lesson, why a substring fails, is general and stands without the history.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `63bb1db` and `a6ccf5b` ("Lived once" before).
- **Proposed:** fix: "9. **A body is asserted by path, never by substring.** A substring cannot tell `3` from `30`, cannot say a field exists, and cannot say one is absent. The rule, decided before the first Invariant Slice and held after:"

**LES-10.**
- **Where:** `spring-harness-reference.md`, §6, item 1, lines 467–470, and item 6, lines 493–495. Also `spring-boot-walkthrough.md` §5, line 240.
- **Quote:** `   version.** `postgres:17` here, because the Runtime Grounds CBC Runs`
- **The rule:** §2.6 above.
- **What the text says:**
  - Two values in the file are justified by what past CBC Runs did. Item 1: "because the Runtime Grounds CBC Runs built were 17". Item 6: "A hundred is what the CBC Runs used".
  - The walkthrough adds "(one CBC Run used a hundred)".
  - The lesson is general in each place: the image follows the Runtime Ground's major version, and the request count is free as long as the requests are released together.
  - DECISION-40's reason, a count read as why a line is required, may or may not reach a value's provenance.
- **Stands:** uncertain.
- **Why it was missed:** missed at a change, `a6ccf5b` (item 1) and `63bb1db` (item 6).
- **Proposed:** question: does DECISION-40 reach these? If not, fix: "`postgres:17` here, the illustration's version." "A hundred is this file's number." "(a hundred, say)".

**LES-11.**
- **Where:** `spring-harness-reference.md` §1, line 162; §2, lines 213–215; §4, lines 430–434. Also `app-structure.md` *The Stack Default*, lines 53–54.
- **Quote:** `  image. The latest CBC Run ran 12 against the Runtime Ground's 11.`
- **The rule:** §2.6 above. One project's detail may be an example, and the statement never stands on it.
- **What the text says:**
  - Each line is an example under a rule stated in general: Flyway's majors may differ; the bases grow only what every test needs; any pool sized to the count satisfies the barrier; a feature starts with as few classes as it needs.
  - So each meets §2.6 as an example.
  - But each names the case by a CBC Run the reader cannot place: "The latest CBC Run", "(the latest CBC Run) and virtual threads (an earlier one)", "One feature a CBC Run built".
  - The brief names a named CBC Run's incident in shipped prose as the candidate.
- **Stands:** uncertain.
- **Why it was missed:** missed at a change, `63bb1db` (§1, §2, §4) and `c449de0` (`app-structure.md`).
- **Proposed:** question: keep them as examples, or drop the CBC Run tags and keep the numbers. For example: "Flyway 12 against the Runtime Ground's 11 is fine." "A fixed pool of that size and virtual threads both satisfy it."

**LES-12.**
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, §3 *Wire the runtime datasource*, lines 127–130.
- **Quote:** `CBC Run decided it at release, not at the CBC Bootstrap. It is never`
- **The rule:** §2.6 above.
- **What the text says:** when fail-fast on a missing secret is decided is told as what one CBC Run did. The general rule is already in the cbc-bootstrap Agent Skill's CBC Bootstrap Exclusion 6: "The question comes back at release ... It is decided there, unless this CBC Run decides otherwise by name."
- **Stands:** checked.
- **Why it was missed:** missed at a change, `a6ccf5b`.
- **Proposed:** fix: "It is decided at the cbc-bootstrap Agent Skill's Stage 1 by name, and may be put off to release there (CBC Bootstrap Exclusion 6). It is never absorbed here."

**LES-13.**
- **Where:** `spring-boot-walkthrough.md`, §4 *The Adversity Harness*, *The test runtime*, *Traps, exact*, item 1, lines 141–144.
- **Quote:** `   from the project root. A CBC Run searched long for the cause of the "no`
- **The rule:** §2.6 above.
- **What the text says:** "A CBC Run searched long for the cause" is a story. The fact the reader needs is general: the file is ignored in the project root, and the error it gives names something else.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `63bb1db`.
- **Proposed:** fix: "`~/.testcontainers.properties` binds **only from `$HOME`,** never from the project root. In the project root it is ignored, and the error, "no valid Docker environment", does not say why."

**LES-14.**
- **Where:** `spring-boot-walkthrough.md`, §5 *The adversity created*, lines 267–292.
- **Quote:** `- **Traps met:** none. Three instances, 120 requests at one instant,`
- **The rule:** §2.6 above.
- **What the text says:**
  - The proof across instances is introduced as "**As one CBC Run built it:**".
  - It ends with one run's results: "Three instances, 120 requests at one instant, no port collision across runs". That is a count from one event.
  - Its trial status is already said, once, in the harness reference's variation point 8: "carried here as prose until a second CBC Run builds it". A trial status may stand (ADR-0073 kept one).
  - The bullets between are practice stated in general.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change, `a6ccf5b`.
- **Proposed:** fix: the lead becomes "**How it is built, built once so far:**". The last bullet becomes "**Traps known:** none yet."

## The Stack Group: infra-establish

**LES-15.**
- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Stage 0 — readiness*, check 2, lines 49–56.
- **Quote:** `   Refusal or verdict. Then the check passes. Two CBC Runs met this,`
- **The rule:** §2.6 above.
- **What the text says:**
  - "Two CBC Runs met this, the same way both times" is a count. The lesson follows it in general: "A fact CBC Framing left unstated is written where it belongs."
  - It is the same fact as the cbc-framing workflow's "Two CBC Runs left it out and wrote it later", which DECISION-40 kept as why the line is required.
  - It was "Lived twice" before `580f7dc` (FINDING-224).
- **Stands:** uncertain.
- **Why it was missed:** missed at a change, `580f7dc`.
- **Proposed:** question: does DECISION-40 reach a second telling of the same count? If not, fix: drop "Two CBC Runs met this, the same way both times."

**LES-16.**
- **Where:** `infra-establish/SKILL.md`, *Records and outputs*, the first bullet's last item, lines 158–161.
- **Quote:** `    would have held. One CBC Run kept an Infrastructure Establishment Log beside such records, and`
- **The rule:** §2.6 above.
- **What the text says:** the only reason given for "no Infrastructure Establishment Log" in a repo with records is one CBC Run's case. It was "Lived once: a log beside" before `580f7dc` (FINDING-224).
- **Stands:** checked.
- **Why it was missed:** missed at a change, `580f7dc` and `1f13fee`.
- **Proposed:** fix: "An Infrastructure Establishment Log beside such records holds nothing they do not."

**LES-17.**
- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, §1 *Declare the service*, *Podman notes*, lines 54–56.
- **Quote:** `- the `name:` pin is a correction a CBC Run made. Without it, the`
- **The rule:** §2.6 above.
- **What the text says:** the pin is introduced as "a correction a CBC Run made". The reason after it is general.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `580f7dc`.
- **Proposed:** fix: "- the `name:` pin is required. Without it, the volume's identity depends on the directory the file happens to run from."

**LES-18.**
- **Where:** provenance counts that open or frame a reference:
  - `spring-harness-reference.md` line 7;
  - `cbc-bootstrap/references/app-structure.md` lines 27–28, "One CBC Run used it across nine Invariant Slices";
  - `cbc-bootstrap/templates/readme-run-test.md` line 8, "the Spring and Maven shape CBC Runs used";
  - `infra-establish/SKILL.md` line 29, "as two CBC Runs confirmed it", and lines 140–142, "Two CBC Runs worked it, and the shape below is theirs";
  - `infra-establish/references/establishment-walk.md` lines 4–5, "Two CBC Runs have done it", and line 151, "as CBC Runs did it";
  - `infra-establish/references/postgres-setup-walkthrough.md` lines 3–4, "as two CBC Runs did it".
- **Quote:** `PostgreSQL. Three CBC Runs built them. The shape below is the latest`
- **The rule:** §2.6 above. ADR-0073: a run never reads our origins.
- **What the text says:**
  - Each line says how many CBC Runs a reference or a default came from. None states a rule through a case.
  - `infra-establish/SKILL.md` lines 134–135 already state the status in general: "The references are written from what CBC Runs did, not rules."
  - The counts go stale at the next CBC Run that runs the Agent Skill.
  - Whether a provenance count is a story line, or a trust signal DECISION-40's reason keeps, no decision says.
- **Stands:** uncertain.
- **Why it was missed:** missed at a change, `63bb1db`, `c449de0`, `a6ccf5b`, `580f7dc` and `1f13fee`. Most were "lived" markers (FINDING-224).
- **Proposed:** question: keep the counts as the reader's measure of how proven a reference is, or let the one general line in `infra-establish/SKILL.md` stand for all and drop the counts. For example, "the sequence end to end", "What to do, end to end, for one Infrastructure Service.", "The shape below is the most corrected one."

## Found true, so not listed

- **The container, 25 files:** no body states a rule through a case.
  - approach-drafting's *Uses* notes stand by DECISION-18.
  - visual-comparison §4 is a list of cases by design, as FINDING-222 read it. Its §1 and §2 hold no case since `89b8b35`.
  - The *Decisions* footers that name CBC Run 3 (delivered-copies, shapes-lifecycle, both retrospective Agent Skills) are stripped at delivery by the Pure Seed's step 2.
- **`delivery/README.md` §4 and the Pure Seed's opening** give the composed files' reason in general (FINDING-266 holds). The Pure Seed's one story pointer, "(devlog 2026-09-06, ...)", sits beside a lesson stated in general. The Pure Seed is ours, never copied into a CBC Run.
- **The playbook** cites no CBC Run 3's RETRO any more (FINDING-206 holds). Its dated lines are examples.
- **The Method Group:**
  - the cbc-framing workflow's counts stand by DECISION-40: lines 46–47 "all six CBC Framings so far", line 241, and the *Open* section, lines 444–454;
  - the worked example, both copies, and the four Output Shapes' illustrations are examples;
  - no "lived" or "pass" marker is left.
- **The Stack Group, lines that meet the rule:**
  - The tested versions in the walkthrough (lines 147–149, podman 5.8 and Testcontainers 2.0.5; lines 219–220, Boot 4.1.1) carry a fact the reader acts on, as FINDING-224 allowed.
  - Trial-status lines state status, not a lesson, as ADR-0073 kept one: the harness reference's variation point 8 (lines 505–506), `app-structure.md` lines 67–68, and the alternatives' "(no CBC Run has used it)".
  - The "traps met" labels (walkthrough lines 113–114, `postgres-setup-walkthrough.md` line 130) frame a fact stated in general. That is the walkthrough's design.
  - `establishment-walk.md` line 127, "so no later project derives it again", is leftover I1, already listed.

## Met in passing

- `TODO.md` lines 642–675, "Rewrite the method's texts plain", still lists FINDING-223, 224, 227, 228 and 206 among its *Ideas*, as "left here by the refinement's DECISION-7 and DECISION-8". The refinement file's Round 3 *Endings* says Round 3's layer 6 worked them. *The work* names no commit for any of them. One of the two is stale, and LES-1 to LES-18 show 223 and 224 were not worked.
- `delivery/container/.claude/skills/visual-comparison/SKILL.md` line 126: "(§1, *When this fires*) covers this" starts at column 0 inside an indented list item. It is a lazy continuation (Layout).

## Not read

None. All 62 files were read whole. The worked example was read once, its two copies byte-identical (`cmp`).
