# Reader WH: Writing, the Method Group (14 files)

Read at `70404e1`. The Finding Kind is Writing: writing rules 1 to 10
(`.claude/rules/writing.md`; `docs/conventions/writing/` §2, *Why each
rule*). Every file in `lists/wh.txt` was read whole. The worked
example was read once, because its two copies are byte-identical
(checked with `cmp`). There are 12 findings: 4 checked, 7 resting on
the reader, 1 uncertain.

## Findings

### WH-1

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *Working one Invariant Slice*, line 85.
- **Quote:** `- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees, the proof,`
- **The rule:** writing rule 8 says a Name the reader may not hold is first said in plain words (`.claude/rules/writing.md`, rule 8). DECISION-39 applies it to this page: "the plain-words page writes the Names, each beside its plain words at first use". The page's own header says the same.
- **What the text says:** this is the first and only use of Invariant Slice Guarantee on the page, and no plain words stand beside it. Every other Name on the page has its plain words.
- **Stands:** checked. `git show 60398b1` turned "the guarantees" into "the Invariant Slice Guarantees" and added no plain words.
- **Why it was missed:** it was missed at a change. `60398b1` is the commit that made DECISION-39's fix on this page. The Foundation Check at that commit read only the glossary's words.
- **Proposed:** fix: `- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees (the properties the invariant needs, found by attacking it), the proof,`

### WH-2

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, the opening, lines 14 to 16.
- **Quote:** `System Never-Event, a thing that must never happen, with a Structural Wall, a structure that makes it impossible, proven by a test that`
- **The rule:** writing rule 2: write short sentences, one idea each (`.claude/rules/writing.md`, rule 2; `docs/conventions/writing/` §2, rule 2: "a chained sentence has to be held whole before any of it makes sense").
- **What the text says:** one sentence of 31 words holds three ideas. It answers each System Never-Event with a Structural Wall, glosses both Names inside the sentence, and adds the proving test. The reader has to hold all of it before the sentence makes sense.
- **Stands:** resting on the reader.
- **Why it was missed:** it was missed at a change. `60398b1` added the two glosses into one existing sentence to meet DECISION-39, and the rule 2 check at that commit did not catch it.
- **Proposed:** fix: "It answers each System Never-Event, a thing that must never happen, with a Structural Wall. A Structural Wall is a structure that makes the System Never-Event impossible. A test that creates the attack proves the Structural Wall holds."

### WH-3

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *How it fails (watch for these)*, line 107.
- **Quote:** `path, and the System Guarantee quietly becomes fiction.`
- **The rule:** writing rule 5: use plain words, not metaphor, and say what happens (`.claude/rules/writing.md`, rule 5).
- **What the text says:** "becomes fiction" is a figure for "stops being true". The method's glossary entry for Escape Hatch already says it plainly: "a System Guarantee stops being true" (`delivery/method/docs/glossary/method.md`, line 25). This is not one of the figures DECISION-26 kept.
- **Stands:** resting on the reader.
- **Why it was missed:** it was missed at a change. `8316ce0` ("cbc-framing's references meet the rule") rewrote this line and kept the figure from the old text. That commit's rule 5 check missed it.
- **Proposed:** fix: `path, and the System Guarantee quietly stops being true.`

### WH-4

- **Where:** `delivery/method/docs/glossary/method.md`, *The method's*, the CBC Framing Derivation entry, line 167.
- **Quote:** `how each stage of CBC Framing ran, kept for good`
- **The rule:** writing rule 9: write a defined thing by its Glossary Name, because a lowercase word is English and only English (`.claude/rules/writing.md`, rule 9). DECISION-25 and the call on FINDING-746 say that a stage of an Agent Skill is an Agent Skill Stage.
- **What the text says:** "stage" here is the cbc-framing Agent Skill's Agent Skill Stage, written in lowercase. It is the only lowercase "stage" left in the Method Group (checked by grep).
- **Stands:** checked.
- **Why it was missed:** it was missed at a change, twice. `c9f6b56` wrote the entry. Then `60398b1` fixed the same word in the Agent Language entry ("stage" became "Skill Stage", FINDING-1335) and left this one.
- **Proposed:** fix: `how each Agent Skill Stage of CBC Framing ran, kept for good`

### WH-5

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, *The order, and why it differs from the presentation*, line 51.
- **Quote:** `Census comes after, and makes the sketches exact.`
- **The rule:** writing rule 9: a defined thing is written by its Glossary Name, whole (`.claude/rules/writing.md`, rule 9: "Agent Skill Template, never Skill Template"; a lowercase word is English only).
- **What the text says:** "the sketches" is the Enemy Sketches of the line before, cut to one lowercase word. In English a sketch is a drawing. The meaning here is the method's.
- **Stands:** resting on the reader.
- **Why it was missed:** it was missed at a change. `3be745a` rewrote the line from "rough enemy *sketches*" and gave the Name only its first use.
- **Proposed:** fix: `Census comes after, and makes the Enemy Sketches exact.`

### WH-6

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, Stage 2, *What the exit leaves behind*, line 300.
- **Quote:** `- **The Scope Exclusions.** Every exclusion as a numbered line:`
- **The rule:** writing rule 9, as in WH-5.
- **What the text says:** "every exclusion" is every Scope Exclusion, written in lowercase in the item that opens with the Name. The next sentences say "A Scope Exclusion".
- **Stands:** resting on the reader.
- **Why it was missed:** it was missed at a change. `3be745a` rewrote "Every written-out scope exclusion" and dropped the qualifier without putting in the Name.
- **Proposed:** fix: `- **The Scope Exclusions.** Every Scope Exclusion as a numbered line:`

### WH-7

- **Where:** `delivery/method/.claude/skills/cbc-framing/templates/registry.md`, *CBC Framing Reconciliation*, lines 97 and 101 to 102.
- **Quote:** `| <…every kill, one row> | | |`
- **The rule:** writing rule 9 (`.claude/rules/writing.md`, rule 9). DECISION-19's concept table, row 2, gives "kill" the Name Enemy Collision Kill.
- **What the text says:** the guidance says "every kill". Line 101's example line, "no deferrals; no kill dropped", is text that a CBC Run copies into its own Invariant Slice Registry. Both write Enemy Collision Kill as the lowercase word "kill". The column header "Kill" and the field "Kills covered" are labels inside their owner, so they stand.
- **Stands:** resting on the reader.
- **Why it was missed:** the lines are older than the rule (`bb51b61`, the starter bundle). Then `8316ce0` and `ce370e4` worked this Agent Skill Template under the rule and missed them.
- **Proposed:** fix: line 97 becomes `| <…every Enemy Collision Kill, one row> | | |`. In line 101, "no kill dropped" becomes "no Enemy Collision Kill dropped".

### WH-8

- **Where:** both copies of the worked example, `delivery/method/.claude/skills/cbc-framing/references/worked-example.md` and `delivery/method/.claude/skills/cbc-slice/references/worked-example.md`, Stage 2, line 97.
- **Quote:** `Two Enemy Census Probes in a row found nothing new: saturated.`
- **The rule:** writing rule 9: a word given a meaning English does not have is written by its Name (`.claude/rules/writing.md`, rule 9).
- **What the text says:** "saturated" stands for Enemy Census Saturation. The line itself gives the method's meaning: two Enemy Census Probes in a row find nothing new. English "saturated" does not mean that. It is the only lowercase form of the word in `delivery/` (checked by grep).
- **Stands:** resting on the reader.
- **Why it was missed:** it was missed at a change. `8316ce0` wrote the Name "Enemy Census Saturation:" eight lines above, at line 89, and kept "saturated" from `8257301`.
- **Proposed:** fix, in both copies: `Two Enemy Census Probes in a row found nothing new: Enemy Census Saturation.`

### WH-9

- **Where:** both copies of the worked example, Stage 2, line 94.
- **Quote:** `3. Enemy Census Probe 3, quantities at huge (a key reused thousands`
- **The rule:** writing rule 6: write defined names and references exactly (`.claude/rules/writing.md`, rule 6). DECISION-19's method table, row 20, and trigger 5 make the three lenses labels: "the assumption hunt", "the timeline stretched" and "the resource lens".
- **What the text says:** Enemy Census Probes 1 and 2 name their Enemy Census Probe Lens by its label. Enemy Census Probe 3 names a move, "quantities at huge", not its lens, "the resource lens" (`cbc-framing-workflow.md` line 265). A reader who maps each probe to a lens finds no label to match. Rule 8 is touched too.
- **Stands:** resting on the reader.
- **Why it was missed:** it was missed at a change. `8316ce0` wrote the three probes with the labels and left the third without its label.
- **Proposed:** fix, in both copies: `3. Enemy Census Probe 3, the resource lens, quantities at huge (a key reused thousands`

### WH-10

- **Where:** both copies of the worked example, Stage 6, line 228. This is a script hit.
- **Quote:** `**Invariant Slice Registry:** SLICE-1 `chosen-next`. SLICE-2`
- **The rule:** writing rule 9, as ADR-0079 left it: "No Markdown mark marks a Name, but bold once, at the line that defines it. A list item's bold lead may begin with a Name" (`.claude/rules/writing.md`, rule 9).
- **What the text says:** the bold span is the Name alone, in a paragraph, not a list item. The Name's home is `docs/concept/03-cbc-framing.md`, so this is a bold Name away from its home. Lines 236, 239 and 249 are numbered list items, so their leads stand under ADR-0079. Line 223, the paragraph above, labels "CBC Framing Reconciliation:" with no bold.
- **Stands:** resting on the reader. The rule's letter was checked: the line is a paragraph, not a list item.
- **Why it was missed:** it was missed at a change. `8316ce0` wrote the line when DECISION-22 already allowed bold only at a Name's home.
- **Proposed:** fix, in both copies: drop the bold, `Invariant Slice Registry: SLICE-1 `chosen-next`. SLICE-2`, as line 223 has it.

### WH-11

- **Where:** `delivery/method/.claude/shapes/slice-record.md`, *Rules for the parts*, line 201.
- **Quote:** `- **Blocks are separated by a `---` line.**`
- **The rule:** writing rule 9: a Name built on another Name carries it whole, however long it gets (`.claude/rules/writing.md`, rule 9).
- **What the text says:** "Blocks" is Invariant Slice Guarantee Block cut to its last word. Everywhere else in the file the Name is written whole.
- **Stands:** resting on the reader.
- **Why it was missed:** the line (`d3ebdff`, 2026-10-29) is older than the Name (DECISION-19's method table, row 48, 2026-10-31). `8a4525b` and `6e1d55e` then worked this Output Shape for the Name and missed this line.
- **Proposed:** fix: `- **Invariant Slice Guarantee Blocks are separated by a `---` line.**`

### WH-12

- **Where:** `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*, the Delegated-Verdict Mode paragraph, lines 48 to 50.
- **Quote:** `derivation becomes the only review, so its legibility is part of the`
- **The rule:** writing rule 9. DECISION-19's method table, row 28, gives "derivation doc, the derivation" the Name CBC Framing Derivation.
- **What the text says:** "the written derivation" may mean the CBC Framing Derivation, the document Delegated-Verdict Mode leaves as the only review. It may also mean the reasoning as written, the English sense. The Agent Skill uses "derivation" in both senses: "Present your derivation" at line 37, and "derivation order" at line 208.
- **Stands:** uncertain.
- **Why it was missed:** the rule is unclear on a word with both an English sense and a Name. `4884a129` rewrote the line.
- **Proposed:** question: is "the written derivation" the CBC Framing Derivation? If it is, fix it to "the CBC Framing Derivation becomes the only review". The same question reaches `delivery/method/.claude/skills/cbc-framing/templates/registry.md` lines 112 and 114, "(derivation wins, recorded)" and "the derivation overrode it". There it seems to mean what CBC Framing derived.

## Found true, so not listed

- **Script hits:** 22 lines were judged. 20 are list items whose bold lead begins with a Name, which ADR-0079 decision 2 allows:
  - the plain page, lines 104 to 110;
  - the template, lines 37, 39, 66 and 67;
  - the cbc-slice workflow, lines 225, 229 and 233;
  - `evidence-test.md`, line 174;
  - `slice-record.md`, line 49;
  - the worked example, lines 236, 239 and 249, in both copies.

  The other two are WH-10's line 228, in both copies.
- **Bold Names at their home:** each sits in the file its glossary entry points at:
  - Demonstration Mode, Delegated-Verdict Mode, Falsifiable Promise Audience, System Possession Test, System Refusal Test, Enemy Sketch, CBC Framing Derivation Appendix, CBC Framing Export Filter and Agent Language, in the cbc-framing Agent Skill's `SKILL.md`;
  - the Enemy Census Probe Lens, Enemy Census Probe Stamp, Enemy Census Audit Checklist and Enemy Census Probe Log leads, in the cbc-framing workflow;
  - Correctness Specification, in the cbc-slice workflow at line 108;
  - Decision Test and Structural Wall Check, in the cbc-slice Agent Skill's `SKILL.md`.
- **Bold sentences that contain a Name:** examples are `SKILL.md` lines 130, 144, 225, 249 and 259, and the cbc-slice workflow line 102. I read the bold as marking the sentence, not the Name. The script did not flag them.
- **Rule 10:** no numbered section stands in the 14 files. The headings are unnumbered, Agent Skill Stage headings, or READINESS-n headings, which DECISION-20 puts outside the rule.
- **Labels:**
  - Exit, Hands down, Residue, theorem and contract, and the three passes' names;
  - an entry's fields, Skeleton and Illustration, and the Output Shapes' record labels ("*The wall:*", "Folds and flags", "The plan, across guarantees");
  - "Gate" inside the cbc-slice Agent Skill.

  Each is a label inside its owner (DECISION-19's method table, rows 9, 10, 39, 78 and 81, and question 4). "skeleton" and "surface" in prose are English (question 6).
- **Foundation Line values** (`concept v1`, `practice, under the shapes convention`, `the writing convention`) are written as they are, under ADR-0079 decision 3.
- **The two descriptions:** their trigger phrases, "close a slice", "slice registry" and "framing, a promise", are outside the Names (DECISION-37).
- **Agent Skill Stages outside their owner** carry the owner, as "the cbc-slice Agent Skill's Stage 1" (DECISION-25).
- **Other plain-page Names:** every Name on the plain page except WH-1's has its plain words at first use.

## Met in passing

- `delivery/method/.claude/skills/cbc-framing/SKILL.md` line 51 says the Exit is "recorded in the record the records table names for sign-offs". The container's records table (`delivery/container/.claude/CLAUDE.md`) has no row that names sign-offs. Stale lines or Agreement.
- `cbc-framing-workflow.md` Stage 6 closes with "**Hands off to:**" (line 428). Every other Agent Skill Stage there writes "**Hands down:**". This may be meant, since it leaves the Agent Skill. Layout or Agreement.

## Not read

None.
