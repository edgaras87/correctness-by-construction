# Reader WF: Writing, Refinement Layer 5 and the container's copies

Read at `70404e1`. Finding Kind: Writing, writing rules 1 to 10
(`.claude/rules/writing.md`; why: `docs/conventions/writing/README.md` §2).
Read whole: the 18 files of `lists/wf.txt` but `.claude/decisions.md`, read by
its header comment (lines 3 to 18). Then the 6 container copies diffed against
ours, the differing lines read.

15 findings: 11 checked, 2 resting on the reader, 2 uncertain.

## Findings

### WF-1. Our Entry File's three tests

- **Where:** `CLAUDE.md`, the second header comment (under *Records*), lines 38 to 44.
- **Quote:** `1. True of this project and nowhere else — else it is a`
- **The rule:** writing rule 2, one idea each, and rule 3, parts not chained with dashes (`.claude/rules/writing.md`, *The rules*).
- **What the text says:** "else it is a convention, stated once, there": "there" points at nothing. Line 43 to 44, "a fact whose failure is not noticing it", cannot be read once. Each test chains its reason on with a dash. The container's copy of the same comment was fixed by FINDING-1278 and 1279 (`delivery/container/.claude/CLAUDE.md` lines 60 to 66); ours was not.
- **Stands:** checked. The container's fixed text is in the tree; ours is unchanged since `8d08cfd`.
- **Why it was missed:** missed at a change. `fab7214` ("our Entry File and Agent Rules meet the rule again") edited line 42 of this comment and did not carry FINDING-1278's fix. The leftover agent-arrangement §2.4 line ("a fact whose failure is not noticing it", 220) is the source this comment retells; this is its follower in our Entry File, not the same line.
- **Proposed:** fix, as the container's: "1. True of this project and nowhere else. Otherwise it belongs in a manual, stated once." / "2. No moment. Otherwise it goes where the moment is: …" / "3. Nothing else would deliver it: a stance, or a fact nobody would notice was missing." Settle it with the agent-arrangement leftover, so the source and this retelling say the same.

### WF-2. "An Agent Rule with paths:" for Paths Rule

- **Where:** `CLAUDE.md`, the same comment, lines 41 to 42; `.claude/rules/foundation-check.md`, header comment, lines 8 to 9, and *Decisions*, line 80.
- **Quote:** `paths: list for an Agent Rule about one directory.`
- **The rule:** writing rule 9: write a defined thing by its Glossary Name. `docs/glossary.md` line 175: "**Paths Rule** — an Agent Rule with a `paths:` list".
- **What the text says:** three lines spell out the Name's definition instead of writing it: "`.claude/rules/` with a paths: list for an Agent Rule about one directory"; "an Agent Rule with paths: loads only when a file is touched"; "why not an Agent Rule with paths:".
- **Stands:** checked. Paths Rule entered the glossary at `b379c2d` (2026-11-01 13:34).
- **Why it was missed:** `CLAUDE.md` line 42 was missed at a change: `fab7214` (18:03 the same day) rewrote it from "a rule" to "an Agent Rule" after the Name existed. The two foundation-check lines are older than the Name (`ecda44f`, `2158499`); `b379c2d` added the Name without a grep for its definition's wording.
- **Proposed:** fix: "or a Paths Rule in `.claude/rules/` for one directory"; "a Paths Rule loads only when a file is touched with the agent's tools"; "why not a Paths Rule, a `CLAUDE.md` line, or a hook now". The container's `delivery/container/.claude/CLAUDE.md` lines 64 to 65 carry the same wording (reader G's file).

### WF-3. "A change here walks it" in the refinement Approach on Trial

- **Where:** `.claude/approaches-on-trial/refinement.md`, *What this is made usable as*, line 47.
- **Quote:** `What derives from this page is that list. A change here walks it.`
- **The rule:** writing rule 9, the Name Change Walk. DECISION-39 (a): the form's sentence becomes "A change here runs the Change Walk on it", in the conventions manual and every manual.
- **What the text says:** the manual form's sentence in its old wording; "walks" names the Change Walk in lowercase. This page keeps the manual form's sections.
- **Stands:** checked. It is the last "walks it" in Living Text.
- **Why it was missed:** missed at a change: DECISION-39's work (`103a301`, `0cdd102`, `efb8cef`) swept the manuals; this page is an Approach on Trial with the manual form.
- **Proposed:** fix: "What derives from this page is that list. A change here runs the Change Walk on it."

### WF-4. "Grep, then walk" in model-placing

- **Where:** `.claude/approaches-on-trial/model-placing.md`, *Stages*, step 7, lines 41 to 42.
- **Quote:** `7. **Grep, then walk.** Grep every reference in Living Text to the facts' old`
- **The rule:** writing rule 9, the Name Change Walk, as DECISION-39 and `.claude/rules/foundation-check.md` step 3 now write it.
- **What the text says:** "then walk what stands on the Idea Model and on the lower text", with a Fact Reference to facts-in-sync §4, the Change Walk's home. The Change Walk is meant and written as a lowercase verb.
- **Stands:** checked.
- **Why it was missed:** missed at a change: `448a16c` wrote the bold lead "Grep, then walk." on 2026-11-01, after DECISION-39.
- **Proposed:** fix: "7. **Grep, then run the Change Walk.** Grep every reference … (…); then run the Change Walk on what stands on the Idea Model and on the lower text (…)."

### WF-5. "Real question" in auto-run

- **Where:** `.claude/approaches-on-trial/auto-run.md`, *Stages*, step 4, line 48.
- **Quote:** `is a Real question, one the CBC Run must not decide alone;`
- **The rule:** writing rule 9: a word given a meaning English does not has a Glossary Name, two or more words, each capitalized, entered in the glossary; a lowercase word is English.
- **What the text says:** "Real question" is capitalized like a Name and given a meaning of its own, but it is in no glossary, and its second word is lowercase. `TODO.md` line 85 cites this file as its home: "a Real question being what the auto-run Approach on Trial calls one".
- **Stands:** checked. No glossary lists it.
- **Why it was missed:** missed at a change: `448a16c` (2026-11-01) wrote the line.
- **Proposed:** question: plain words, "past which is a question the CBC Run must not decide alone", with `TODO.md` 85 following; or a Name with a glossary entry pointing here. Recommended: plain words, since the line already defines it in place.

### WF-6. The convention-manual item 3's dash

- **Where:** `.claude/rules/convention-manual.md`, *The sections, in this order*, item 3, lines 42 to 46.
- **Quote:** `shipped or the Concept Deliverer's, with the moment it opens at — or`
- **The rule:** writing rule 3: parts are not chained with dashes; rule 2, one idea each.
- **What the text says:** one sentence carries the list's content, its marks, its moment, and, after a dash, the other case, "nothing shipped", and what a repo then holds.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `ecda44f` (2026-10-30) rewrote the line and kept the dash.
- **Proposed:** fix: "everything derived from the manual, each by path from the repo root, marked shipped or the Concept Deliverer's, with the moment it opens at. When nothing ships: "nothing shipped", and then what a repo holds."

### WF-7. Two Fact References side by side

- **Where:** `.claude/rules/convention-manual.md`, item 7, lines 80 to 82.
- **Quote:** `Where the reasoning rests on the Agent Model, a Fact Reference to the part it rests on, such as`
- **The rule:** writing rule 3, label the parts; rule 2.
- **What the text says:** "…such as (`docs/models/agent.md` §8, …) (`docs/conventions/conventions/` §2.7, …)." Two parentheses stand together. Nothing tells the example from the item's own source, and the sentence has no verb.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `839f785` (2026-11-01) added the second parenthesis beside the first.
- **Proposed:** fix: "Where the reasoning rests on the Agent Model, it carries a Fact Reference to that part, such as (`docs/models/agent.md` §8, *Choosing a channel*). Why: (`docs/conventions/conventions/` §2.7, *The channel*)."

### WF-8. `exchange-read` as rule 6's example

- **Where:** `.claude/rules/writing.md`, *The rules*, rule 6, line 30.
- **Quote:** ``exactly: ADR-0052, FINDING-7, WORK-9, `exchange-read`. Define each``
- **The rule:** writing rule 9 as DECISION-27 reads it: an agent part is written with its kind word, always, "the cbc-slice Agent Skill"; the 166 skill names in backticks were fixed so.
- **What the text says:** the rule's own example of a name written exactly is a bare Agent Skill name in backticks, the form DECISION-27 retired. It is the last backticked Agent Skill name in our agent files.
- **Stands:** uncertain. As a label in a list of labels it may be meant as the folder's name, not prose.
- **Why it was missed:** older than the rule (`5c5ac7d`, 2026-10-18); DECISION-27's sweep left it.
- **Proposed:** question: keep it as a label, or replace it: "ADR-0052, FINDING-7, WORK-9, the exchange-read Agent Skill".

### WF-9. "living text" in the container's one-home Agent Rule

- **Where:** `delivery/container/.claude/rules/one-home.md`, *Not a second home*, line 46. Script hit.
- **Quote:** `comment is living text.`
- **The rule:** writing rule 9. Living Text is a shared Name, `delivery/container/docs/glossary/container.md` line 50; DECISION-19's Agent Model table, row 16, names this file as the one that uses it.
- **What the text says:** "The Decisions Log's header comment is living text." The Name is written in lowercase. Our copy writes "Living Text".
- **Stands:** checked.
- **Why it was missed:** older than the Name (`1c531b4`, 2026-10-27); then missed at two changes to the same paragraph: `ddd6057` (DECISION-33's work) and `ae8eb31` (ADR-0079), which edited line 44.
- **Proposed:** fix: "comment is Living Text."

### WF-10. "the one-home rule" in the container's footer

- **Where:** `delivery/container/.claude/rules/one-home.md`, *Decisions*, line 52.
- **Quote:** `- ADR-0053 — the one-home rule loads in every session`
- **The rule:** writing rule 9 as DECISION-27 reads it: "the one-home Agent Rule", the kind word always.
- **What the text says:** "the one-home rule". Our copy's footer, line 68, says "the one-home Agent Rule".
- **Stands:** checked.
- **Why it was missed:** missed at a change: `ac34e28` (2026-10-31) wrote it, after DECISION-27; `ddd6057` did not catch it.
- **Proposed:** fix: "- ADR-0053 — the one-home Agent Rule loads in every session".

### WF-11. "(CBC docs/…" in the container's one-home comment

- **Where:** `delivery/container/.claude/rules/one-home.md`, header comment, lines 12 to 13.
- **Quote:** `Concept Deliverer's facts-in-sync manual (CBC`
- **The rule:** writing rule 8, as FINDING-1277 read it; DECISION-40 (a): "CBC docs/…" becomes "the Concept Deliverer's docs/conventions/…" at each.
- **What the text says:** "(CBC docs/conventions/facts-in-sync/ §1, One home; The CBC Run's seat)". A CBC Run does not know "CBC" is our Repo Tag. It is the last "CBC docs/" under `delivery/`.
- **Stands:** checked.
- **Why it was missed:** the phrase breaks across lines 12 and 13, so FINDING-1277's list of 11 lines, found line by line, did not hold it; `ddd6057` edited line 12 and kept it.
- **Proposed:** fix: drop "CBC": "(docs/conventions/facts-in-sync/ §1, One home; The CBC Run's seat)". The sentence already says "the Concept Deliverer's facts-in-sync manual".

### WF-12. "An Invariant Slice Registry entry"

- **Where:** `delivery/container/.claude/rules/one-home.md`, *The rules*, rule 3, lines 27 to 28.
- **Quote:** `reads it in the owner's place. An Invariant Slice Registry entry`
- **The rule:** writing rule 9. The Name is Invariant Slice Entry, `delivery/method/docs/glossary/method.md` line 247 (DECISION-19's method table, row 75).
- **What the text says:** the thing is written as the registry's Name plus the lowercase word "entry".
- **Stands:** checked.
- **Why it was missed:** missed at a change: `ddd6057` wrote it, after the Name was given.
- **Proposed:** fix: "reads it in the owner's place. An Invariant Slice Entry does this: it links the Invariant Slice Record it sums up."

### WF-13. "the build stage" in the container's writing example

- **Where:** `delivery/container/.claude/rules/writing.md`, *Before and after*, the After text, line 94. This line is the container's alone.
- **Quote:** `> red. That Red Run is owed in the build stage.`
- **The rule:** writing rule 9: an Agent Skill Stage is written "Stage 3" inside its owner, and with its owner outside it (DECISION-19's method table, row 1; DECISION-25).
- **What the text says:** the example meant to show the rule writes the cbc-slice Agent Skill's Stage 3 as "the build stage", in lowercase.
- **Stands:** checked. Stage 3 of `delivery/method/.claude/skills/cbc-slice/SKILL.md` is "build" (line 147).
- **Why it was missed:** missed at a change: `ddd6057` edited this line ("red run" to "Red Run") and kept "the build stage".
- **Proposed:** fix: "That Red Run must happen in Stage 3, build." This also drops "owed", which FINDING-1344's call says is not a dead figure.

### WF-14. `` `cbc-slice`'s Stage 3 `` in the container's rule 9

`delivery/container/.claude/rules/writing.md`, rule 9, line 55. Quote: ``"delivered-copies rule 4", "`cbc-slice`'s Stage 3";``. Rule 9 as DECISION-27 reads it: an Agent Skill is written with its kind word, not in backticks. The example follows the container glossary's Agent Skill Stage entry (line 86), which is leftover E13's form. Checked. Written at `ddd6057`. Proposed: question: settle it with E13, and this example follows.

### WF-15. The bold Change Set in the container's commit-plan

`delivery/container/.claude/skills/commit-plan/SKILL.md`, line 9. Script hit. Quote: ``A **Change Set** is a body of work that needs more than one commit.``. Rule 9 as ADR-0079 reads it: bold once, at the home the glossary entry names. Ours dropped this bold at FINDING-626, by DECISION-22, and DECISION-33 says the container's copy takes our fixes. But the container glossary's Change Set entry (line 93) names the commit-plan Agent Skill as where a CBC Run finds it, so from the CBC Run's side this may be the home. Uncertain. The hunk also goes to the Agreement reader of the CBC Run's side. Proposed: question: drop the bold, as DECISION-22 named 626; or keep it as the CBC Run's home of the Name, a seat difference ADR-0069 allows. Recommended: drop it, since our glossary's home is the manual.

## The copies

- `approach-drafting.md`, `commit-messages/SKILL.md`: byte-identical. Every line read holds for both; no finding.
- `visual-comparison/SKILL.md`: one hunk, §5, the seat's. No finding in it or in the shared lines.
- `commit-plan/SKILL.md`: three hunks. Lines 95 and 149 are the seat's. Line 9 is WF-15. No finding in the shared lines.
- `one-home.md`: every difference is the seat's. WF-9 to WF-12 are in the container's lines only.
- `writing.md`: every difference is the seat's. WF-13 and WF-14 are in the container's lines only. WF-8 is in our line only. The *Decisions* line on ADR-0079 is shared (see Met in passing).

## Found true, so not listed

- No numbered title in the 24 files passes 30 characters or carries a dash, colon, comma or parenthesis (script, then by eye).
- No Glossary Name is spelled in lowercase in the 24 files, lines joined, except WF-9. "made usable" and the Foundation Line values are allowed.
- Bold: the only bold Name away from its home is WF-15. `refinement.md` §1.1 bolds its three Names at their home. The bold opening statement (`refinement.md` 3 to 7) and the bold question (`approach-drafting.md` 24) mark a statement, not a Name.
- Local numbers carry their owners: "CBC Run 3's RETRO D2", "Refinement Round 1's DECISION-1".
- The Agent Skill Stage headings with a dash in `exchange-read` and `exchange-deliver` are leftover F11; step 6 with no bold lead is F13; "the fourth writes a document" is F12; working-a-reading's Foundation Line is F9; "The refinement is open." is F15. Not listed again.
- "birth" in auto-run 9 and exchange-deliver 153 is the idiom DECISION-36 keeps English. "Release" is the playbook's Plan Step label, written with its owner ("its Release").
- `CLAUDE.local.md` and the `.claude/decisions.md` header comment meet rules 1 to 10.

## Met in passing

- Both `writing.md` copies' *Decisions* line on ADR-0079 says "rule 10: a comma or a parenthesis is a gloss". ADR-0079 decision 4, narrowed, says a comma that joins a gloss; a comma in a list is not. Stale lines, both copies.
- `delivery/container/.claude/CLAUDE.md` lines 64 to 65 say "with a paths: list for an Agent Rule about one directory": WF-2's wording, reader G's file.
- `TODO.md` line 85 retells "Real question" from auto-run: it follows WF-5.
- `.claude/skills/visual-comparison/SKILL.md` line 126, "(§1, *When this fires*) covers this", starts at column 0 inside a list item, a lazy continuation (Layout), in both copies.
- Leftover F6, as written ("commit-plan 24 hunks (3 now: 2 seat, 1 bold Change Set)") is correct at `70404e1`: 3 hunks.

## Not read

None.
