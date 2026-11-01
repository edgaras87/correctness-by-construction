# SL1: Stale lines, Refinement Layers 1 to 3

Reader SL1. Finding Kind: Stale lines. Read at `70404e1`. All 25 files read whole.

The rule for every finding below: none is needed; a false line is wrong (`temp/refinement-2026-10-18.md`, *The last read*, *The rules' check (§2.3)*, the Stale lines row).

15 findings: 9 checked, 5 resting on the reader, 1 uncertain.

## Layer 1: the conventions manual

### SL1-1

- **Where:** `docs/conventions/conventions/README.md`, *What this is made usable as*, line 32.
- **Quote:** `- **the index, `docs/conventions/README.md`** — it points at each manual. It holds`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** the index points at each manual. It does not. `docs/conventions/README.md` names only `docs/conventions/conventions/` and `.claude/approaches-on-trial/approach-drafting.md`. It sends the reader to `ARCHITECTURE.md` §1.2 for which conventions there are. The list of manuals left the index at `722357d` (2026-09-30).
- **Stands:** checked.
- **Why it was missed:** missed at a change. `0803717` (2026-11-01, "the conventions manual meets the rule again") expanded "it points" to "it points at each manual". The Foundation Check's read of the index beside the change should have caught it.
- **Proposed:** fix: "it points at this manual and at `ARCHITECTURE.md` for the rest." Or go back to "it points."

## Layer 2: project-recording

### SL1-2

- **Where:** `docs/conventions/project-recording/README.md`, *What it is for*, line 16.
- **Quote:** `since: four CBC Runs kept their records under these Record Stubs. Every`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** four CBC Runs. The count was set on 2026-10-20 (`f1c02a7`). CBC Run 5 was born on 2026-10-21 and ran through Release. CBC Run 6 was born on 2026-10-29 (`ARCHITECTURE.md` §2.5 lists six). The count has not moved since.
- **Stands:** checked.
- **Why it was missed:** missed at a change. Neither CBC Run Birth's close checked this count. The Plan Step Form's close item on "now", "today" and "not yet" asks only about lines that mention the Plan Step's subject.
- **Proposed:** question: count the CBC Runs that kept records under the Record Stubs (five or six, depending on CBC Run 2, idle since its Step 0), or date the count, "four by 2026-10-20".

### SL1-3

- **Where:** `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 1, line 74.
- **Quote:** `   the next CBC Run Birth`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** whether a retrospective serves this repo is on trial at the close of the Plan Step that runs "the next CBC Run Birth". That trigger was the close of CBC Run 5's birth Plan Step: TODO's "Run this repo's retrospective, on trial" names it. The close came on 2026-10-22 without running the trial. The devlog says it "fired" and was left for the reviewer to place (devlog 2026-10-22). Read today, "the next CBC Run Birth" points at CBC Run 6's. That Plan Step is stopped, and nothing ties the trial to it.
- **Stands:** checked: the TODO item's trigger and devlog 2026-10-22.
- **Why it was missed:** missed at a change. The close of CBC Run 5's birth fired the trigger, but nothing re-read the two manuals that state it. `f435e8d` (2026-11-01) reworded the line and kept the claim.
- **Proposed:** question: where the reviewer places the trial. Then: "is on trial, its close placed by the reviewer (TODO's "Run this repo's retrospective, on trial")". SL1-13 is the same line in the retrospective manual.

### SL1-4

- **Where:** `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 5, line 96.
- **Quote:** `   invariants and a `src/` codemap. It keeps to about two pages, as §8`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** our `ARCHITECTURE.md` keeps to about two pages. ADR-0068 set "about two pages" at about 1,200 words. `ARCHITECTURE.md` is now 2,053 words and 269 lines.
- **Stands:** resting on the reader. The manual does not define a page; ADR-0068's word count is the measure taken.
- **Why it was missed:** missed at a change. The file grew past the measure across its Refinement Round fixes, and no check compares its size with the claim.
- **Proposed:** question: is it cut back to the measure, or does the line say "it aims at about two pages"?

### SL1-5

- **Where:** `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 6, line 119.
- **Quote:** `   decisions each, a median of 4.5, and a median of 102 lines. Their`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** the ADRs' median length is 102 lines, and the median number of decisions is 4.5. The figures were written at `eb57bcf` (2026-11-01, 08:46), when there were 78 ADRs. ADR-0079 landed after (`fc97f20`, 19:29). With 79 ADRs, the median length by `wc -l` is 103 lines. A median of an odd number of whole counts cannot be 4.5.
- **Stands:** checked for the line count. Uncertain for the decision count, since the method behind 4.5 is not given (mine gives 5, or 6 among ADRs with numbered decisions).
- **Why it was missed:** missed at a change. Nothing re-reads an undated running count when an ADR is added.
- **Proposed:** fix: date the figures, "at 2026-11-01, 78 ADRs: up to 12 numbered decisions each, a median of 4.5, and a median of 102 lines". Or drop the medians and keep "up to 12".

### SL1-6

- **Where:** `docs/conventions/project-recording/README.md`, §7.5 *When a README changes*, line 558.
- **Quote:** `already written so in Plan Step Gates in use ("ARCHITECTURE`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** Plan Step Gates in use already carry a records item such as "ARCHITECTURE current". No Plan Step Gate in this repo carries it: not the playbook's (its Gate lines are empty), not the PLAN Record Stub's, not our `PLAN.md`'s. The words came from the handbook ("lived gates") and were reworded at `f435e8d`.
- **Stands:** uncertain. CBC Runs' own plans may carry it, and they cannot be read from here.
- **Why it was missed:** older text, carried through rewordings. Each rewording kept the claim and did not check it.
- **Proposed:** question: name a gate item that exists, such as our close item "`CLAUDE.md` read top to bottom", or drop the example.

### SL1-7

- **Where:** `docs/conventions/project-recording/README.md`, §9.4 *How a playbook is written*, moment 2, line 678.
- **Quote:** `   authors them. No Agent Skill or Plan Step asks this of a CBC Run yet: the TODO`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** no Agent Skill or Plan Step asks a CBC Run to confirm its Plan Steps once the problem is framed. The playbook's Step 2 asks it under *Known already*: "the plan is read end to end against the CBC Framing Exports: each later Plan Step still stands as named, or is reworded in place, never kept silently." That line has been there since `51a792e` (2026-10-16, ADR-0055 decision 6). The manual's line came later (`90d1367`, 2026-10-26).
- **Stands:** resting on the reader. Step 2 asks for less than the manual's list: rewording, but not filling specifics, deleting, adding or renumbering.
- **Why it was missed:** missed at a change. `90d1367` wrote it without reading the playbook it describes.
- **Proposed:** fix: "The playbook's Step 2 asks part of it: each later Plan Step is read against the CBC Framing Exports and reworded where it no longer fits. The TODO item "Read CBC Run 4 against `dac4dd1`" asks whether CBC Run 4 did it."

### SL1-8

- **Where:** `docs/conventions/project-recording/README.md`, §14 *Conversation Memory*, line 856.
- **Quote:** `The trial is judged when the third item is worked with its section`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** the trial is judged at the third item worked with its section in hand. The devlog records at least three: §1 for the text-division item ("changed the work", 2026-10-24), §18 for the lesson stories and §19 with §23 for the words item (both 2026-10-29). No verdict is recorded in the devlog, TODO, PLAN or the refinement file, and the line still reads as a trigger yet to come.
- **Stands:** resting on the reader: whether those three count as items "worked with its section in hand".
- **Why it was missed:** missed at a change. The close of each of those items did not check the trial's trigger.
- **Proposed:** question: the reviewer judges the trial now, or the line names the refinement Plan Step's close as the moment, saying the item count has passed.

## Layer 3: the other manuals, the Idea Models, the concept, the glossary

### SL1-9

- **Where:** `docs/conventions/agent-arrangement/README.md`, *The CBC Run's seat*, line 52.
- **Quote:** `CBC Run receives it. Its Entry File says two things. `docs/concept/``
- **The rule:** none needed; a false line is wrong.
- **What the text says:** the shipped Entry File says two things: the copies are pinned, and before CBC Framing the only method work is the cbc-framing Agent Skill. Since `3630ed9` (2026-10-31) it also says the delivered words arrive in `docs/glossary/`, and that this project's own are `docs/glossary.md`'s. It also says where the method is. The count was written at `f07d52a` (2026-11-01), after the glossary line.
- **Stands:** resting on the reader: the count may mean only the things relevant to the seat.
- **Why it was missed:** missed at a change. `f07d52a` reworded the line without re-reading `delivery/container/.claude/CLAUDE.md`.
- **Proposed:** fix: "Its Entry File says, among other things, that..." Or add the glossary line as a third thing.

### SL1-10

- **Where:** `docs/conventions/agent-arrangement/README.md`, §2.4 *How the Entry File is written*, line 233.
- **Quote:** `heading saves one that fails. The first two are present at birth. The`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** of the five kinds of content, the first two are present at birth, and the other three, *Local rules* among them, arrive when they become true. The shipped Entry File has a `## Local rules` section at birth, with one rule: "Nothing before the CBC Run Briefing names the problem." That section has been in the Container Group since `d148ccb` (2026-09-19).
- **Stands:** checked.
- **Why it was missed:** older text: the line came with the vendored manual (`9a1637d`, 2026-09-18). It was missed at `d148ccb`, and in Refinement Round 1's Stale lines read.
- **Proposed:** fix: "The first two are present at birth, and a CBC Run's Entry File is born with one Local Rule. The others arrive when they become true..."

### SL1-11

- **Where:** `docs/conventions/facts-in-sync/README.md`, §3.1 *What a Fact Reference is*, line 179.
- **Quote:** `In a shipped file, a reference to this repo's text leads with CBC`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** a shipped file's reference to our text leads with CBC. DECISION-40 (2026-11-01) changed that form to "the Concept Deliverer's `docs/conventions/…`", and the fix landed at `8b6eec0` and `2fca3bf`. At `70404e1`, `delivery/` has 0 references that open with "CBC `docs/" and 13 that open with "the Concept Deliverer's `docs/". The manual that states the form was not changed.
- **Stands:** checked.
- **Why it was missed:** missed at a change. DECISION-40's fix changed only the shipped files. The Foundation Check, run on them, should have read facts-in-sync §3.1, the home of the form.
- **Proposed:** fix: "In a shipped file, a reference to this repo's text leads with "the Concept Deliverer's" and serves this repo's Change Walk alone." Check line 149 too, the cross-repo example, against what DECISION-40 meant for a shipped file.

### SL1-12

- **Where:** `docs/conventions/repo-hygiene/README.md`, §2 *The template layers*, lines 78 to 79.
- **Quote:** `Plan Step, Agent Skill or playbook names the append.`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** no Plan Step, Agent Skill or playbook names the append. The cbc-bootstrap Agent Skill does: "Each hygiene file, `.gitignore`, `.gitattributes` and `.editorconfig`, takes its Stack Overlay below the marked line it carries" (`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, line 205). Its walkthrough lists what each file takes (`spring-boot-walkthrough.md`, lines 50 to 56). The Agent Skill has named the append since `b6ecf85` (2026-10-21). The manual's line was written later, at `dd88bf6` (2026-10-26). "Nothing ships one" still holds: the `.part` files do not ship.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `dd88bf6` moved the line out of a dated italic without re-reading the Stack Group.
- **Proposed:** fix: "How a Stack Overlay reaches a CBC Run is open: nothing ships one. The cbc-bootstrap Agent Skill names the append, and its walkthrough lists what each file takes, written by the CBC Run itself."

### SL1-13

- **Where:** `docs/conventions/retrospective/README.md`, *The Concept Deliverer's seat*, line 89.
- **Quote:** `At the close of the Plan Step that runs the next CBC Run Birth, it`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** the same claim as SL1-3. The trial's trigger was the close of CBC Run 5's birth Plan Step (TODO's "Run this repo's retrospective, on trial"). That close came on 2026-10-22 without the trial (devlog 2026-10-22), and the reviewer has not yet placed it.
- **Stands:** checked.
- **Why it was missed:** missed at a change, as SL1-3. `7b81e55` (2026-11-01) reworded the line.
- **Proposed:** question, with SL1-3: where the reviewer places the trial. The line then names that close.

### SL1-14

- **Where:** `docs/glossary.md`, *Between them*, the Receipt Branch entry, line 74.
- **Quote:** `  named by its Delivery Pin and never merged: the Pure Seed's`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** a Receipt Branch is named by its Delivery Pin, and the Pure Seed's `birth-seed` is one. `birth-seed` is not named by a Delivery Pin. The Pure Seed puts the Delivery Pin in its commit subjects (`delivery/installs/pure-seed.md`, step 4, line 128).
- **Stands:** checked.
- **Why it was missed:** missed at a change. `873663f` (2026-10-31) took "named by the Delivery Pin" from exchange §4, step 3, and added the Pure Seed's branch beside it without checking its name.
- **Proposed:** fix: "a branch holding a delivery as it arrived, never merged: the Pure Seed's `birth-seed`, its Delivery Pin in each commit's subject, or one a CBC Run cuts at its Delivery Take, named by the Delivery Pin, so..."

### SL1-15

- **Where:** `docs/models/agent.md`, §12.7 *Claims on summaries*, claim M1, line 414.
- **Quote:** `- `evidenced` — the commit-messages manual states "≤50 chars, imperative, **no`
- **The rule:** none needed; a false line is wrong.
- **What the text says:** the commit-messages manual states "≤50 chars, imperative, no period". Our manual states neither. It says "Either mood, in the present tense" (§2.2, ADR-0049). The words now in force are the commit-messages Agent Skill's, "≤50 chars, present tense, no period". The evidence came from the handbook, vendored on 2026-08-27 (`7b049af`), where its manual said it then.
- **Stands:** resting on the reader: the line may mean the handbook's manual. Read in this repo, "the commit-messages manual" is ours, in the present tense.
- **Why it was missed:** older than the change. ADR-0049 changed the mood in our manual, and the claim's tense was not re-read. `4ee4062` (2026-11-01) reworded the line.
- **Proposed:** fix: "the handbook's commit-messages manual of the time stated "≤50 chars, imperative, **no period**"."

## Found true, so not listed

- Idea-to-Output Model §1: "8 of the 12 manuals stand on none (2026-11-01)". Four carry a Foundation Line.
- The conventions manual §1.3: every Agent Skill and Agent Rule in both Convention Seats carries a Foundation Line; every shipped Output Shape does; no Approach on Trial does. Its value forms match the tree, apart from the leftovers already listed (A3, F9).
- The conventions manual §1.4's example heading `## Stage 1 — specify-correctness` is in the cbc-slice Agent Skill. §1.5's TODO item exists. §3, step 3's birth entry is in the container's Decisions Log Record Stub: 11 conventions.
- Agent-arrangement's seats: the CBC Run holds five convention Agent Skills, one Approach on Trial and four Agent Rules. We hold three convention Agent Skills, two exchange Agent Skills, three Agent Rules with no `paths:` and three with paths. §3.9's "two qualify in a CBC Run and three here" holds. §5.3's "two comment blocks" in `CLAUDE.md` holds. The Plan Step Form's close item re-reads `CLAUDE.md`, as §2.6 says.
- Exchange §3.2 and §3.4: one Delivery Fill exists, the playbook, and one is owed. The Container Group's Entry File names the cbc-framing Agent Skill and `docs/concept/`. Every shipped Agent Skill, Agent Rule and Output Shape carries a Foundation Line (§3.5).
- Facts-in-sync §5: "The concept's meaning has changed once since v1" matches `CHANGELOG.md`'s [Unreleased].
- Project-recording: 7 of the playbook's 9 Plan Steps make nothing true the README says. The Release Plan Step's "README... verified on a clean machine" is in the playbook. The devlog stub splits at 300 lines. `## The Plan Step Form` heads our `PLAN.md`. Our `ARCHITECTURE.md` has the five parts named. We have no `RETRO.md`.
- Repo-hygiene: our root `.gitattributes` and `.editorconfig` equal the Hygiene Base. Our `.gitignore` adds the "this repo" section with `!CLAUDE.local.md`. The `.editorconfig` labels and the marked lines are as described.
- Shapes: `docs/baselines/` exists, with 5 files. `delivery/README.md` points with one sentence. Each Method Group Output Shape carries the worked example.
- The glossary's paths and named sections resolve: auto-run's and approach-drafting's *Stages*, refinement §1.1, `birth-seed`.
- The Agent Model §12.9's scorecard matches the claims' statuses. A1's "125 of 233" is a count fixed to its dated range, taken at midday on 2026-09-29.
- The concept chapters make no claim about the tree, apart from the leftover FINDING-1127.

## Met in passing

- `docs/conventions/exchange/README.md`, line 39: the delivered-copies Agent Rule loads "when a copy... is read", but its `paths:` leaves out `docs/glossary/**`, where pinned copies now land (Agreement, Refinement Layer 6).
- `docs/conventions/project-recording/README.md`, §9.3, line 660: a playbook is versioned "with a note of which project last updated it". The playbook's version line names no project (Agreement).
- `TODO.md`, lines 442 to 444: "though no Agent Skill or Plan Step asks it" has the same staleness as SL1-7 (Stale lines, Refinement Layer 4).
- `docs/conventions/conventions/README.md`, §1, lines 52 to 58: a Work Approach is "one of three" and leaves out the Approach on Trial and the Output Form. `docs/models/idea-to-output.md` §2's table includes them (Agreement).
