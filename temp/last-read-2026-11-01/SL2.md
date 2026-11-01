# SL2: Stale lines, Refinement Layers 4 and 5

Reader SL2. Finding Kind: Stale lines, a line no longer true. No rule is needed: a false line is wrong. Read at `70404e1`. 31 files, each whole, but `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md` by header comment only, and `CHANGELOG.md`'s `[v1]` entry as history.

23 findings: 17 checked, 5 resting on the reader, 1 uncertain.

Three of them were first met in Refinement Round 3's read, in *Met in round 3, of other kinds* (refinement file, lines 2203 to 2310), and still stand: SL2-4, SL2-10, SL2-16. SL2-20 is near a fourth. That list was not part of step 1's leftovers check, so they are listed here.

## Refinement Layer 4

### SL2-1

- **Where:** `ARCHITECTURE.md`, §3 *What must stay true*, line 214.
- **Quote:** `| Every Agent Skill and Output Shape of the method states the concept version it derives from |`
- **The rule:** a false line is wrong. The fact's home is `docs/conventions/conventions/` §1.3, *The Foundation Line*, the cell this row cites.
- **What the text says:** every Output Shape of the method states a concept version. Conventions §1.3 says an Output Shape's line names "the convention it lives under, `practice, under the shapes convention`". All four do: `delivery/method/.claude/shapes/*.md`, line 2. No Output Shape states a concept version.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `c0eb1e6` (2026-11-01, Refinement Round 3's Writing fix) turned "Every execution" into "Every Agent Skill and Output Shape of the method". The Writing read checks how a line reads, not whether it is true.
- **Proposed:** fix: `| Every Agent Skill of the method states the concept version it derives from |`. The Output Shapes' line, the convention they live under, needs no row of its own.

### SL2-2

- **Where:** `ARCHITECTURE.md`, §2.1 *The Method Group* (lines 138 to 141), §2.2 *The Stack Group* (146 to 148), §2.3 *The Container Group* (156 to 159), the codemap (line 251) and the drawing (lines 39 to 46).
- **Quote:** `cbc-slice Agent Skills, under `.claude/skills/`, and the Output Shapes their Plan`
- **The rule:** a false line is wrong. `delivery/README.md` line 4 says what each part is, is `ARCHITECTURE.md`'s §2. `docs/conventions/exchange/` §3.2, *What goes*, lists "each group's Glossary Names, in `docs/glossary/`".
- **What the text says:** each group is listed by what it holds. None of the lists names the group's delivered Glossary Names file. These are `delivery/method/docs/glossary/method.md`, `delivery/spring-postgres/docs/glossary/stack.md` and `delivery/container/docs/glossary/container.md`. The drawing of a CBC Run's copies has no `docs/glossary/` either.
- **Stands:** resting on the reader. The three files exist, and none of the lists names them, checked. Whether a list that leaves a file out is false, or just short, is the reader's call.
- **Why it was missed:** missed at a change. `3630ed9` (2026-10-31) created the three files, and its body says "every list of what is delivered names the three files". ARCHITECTURE's group lists were not among those lists. No Foundation Line ties them to the delivery, so no Change Walk reached them.
- **Proposed:** fix:
  - in §2.1, §2.2 and §2.3, add ", and the Glossary Names it delivers, `docs/glossary/<group>.md`" to each list;
  - in the codemap, `method/ the cbc-framing and cbc-slice Agent Skills, their Output Shapes and Glossary Names (§2.1)`;
  - in the drawing, add a `docs/glossary/ copies` row.

### SL2-3

- **Where:** `README.md`, the opening list, *What it holds*, lines 9 to 11.
- **Quote:** `Skill Templates and checklists, and Output Shapes, each pinned to`
- **The rule:** a false line is wrong. The home is `docs/conventions/conventions/` §1.3, *The Foundation Line*.
- **What the text says:** the Output Shapes are each pinned to the concept version they derive from. They are not: their Foundation Line is `practice, under the shapes convention`. They stand on a convention, not on a concept version.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `5d0f5ca` (2026-11-01, Round 3's close-read fix, "README names Agent Skill Templates and Output Shapes") added the Output Shapes to the sentence. It read for Names, not for truth.
- **Proposed:** fix: "And what is made usable from it: Agent Skills with their Agent Skill Templates and checklists, each pinned to the concept version it derives from, and the Output Shapes their Plan Step Gates read."

### SL2-4

- **Where:** `PLAN.md`, *The Plan Step Form*, *The Plan Step's own items*, lines 73 to 75.
- **Quote:** `the goal. For the exchange-birth Agent Skill's goal "a project born from this repo`
- **The rule:** a false line is wrong.
- **What the text says:** the example gives a goal to the exchange-birth Agent Skill and an item about "CBC Run 5's birth entry". No exchange-birth Agent Skill exists. `TODO.md` line 62 says it is still to be written, its trigger "the CBC Run Birth after CBC Run 6's". CBC Run 5 was born by the Pure Seed on 2026-10-22.
- **Stands:** resting on the reader. That the Agent Skill does not exist, and how CBC Run 5 was born, is checked. Whether an example may name a Plan Step that never ran is the reader's call.
- **Why it was missed:** older than the events that made it false. It was written 2026-10-17 (`cc3a875`), when CBC Run 5's birth was to run the exchange-birth Agent Skill. Round 3's read met it (refinement file, line 2250), and it was not fixed.
- **Proposed:** fix: take the example from a Plan Step that ran: "For Birth CBC Run 6's goal "CBC Run 6 is born from this repo at one Delivery Pin on main", one item is "CBC Run 6's birth entry names one Delivery Pin, ours, and nothing from another repo"."

### SL2-5

- **Where:** `PLAN.md`, *Step: Take CBC Run 5's lessons for CBC Run 6*, Goal (lines 215 to 217) and Notes (lines 296 to 297).
- **Quote:** `Goal: CBC Run 6 can be born from files that carry what CBC Run 5 learned`
- **The rule:** a false line is wrong.
- **What the text says:**
  - The goal is a CBC Run 6 not yet born. CBC Run 6 was born 2026-10-29 (`337788a`), while this Plan Step was stopped, and it has run through its Release (`TODO.md` lines 38 to 40).
  - The Notes say "then Birth CBC Run 6, on full auto, opens". It opened, and is itself stopped.
- **Stands:** checked.
- **Why it was missed:** it became false at CBC Run 6's birth, after the Plan Step stopped. The devlog's Resume of 2026-10-29, later (`devlog/2026-10.md` lines 543 to 545), says "its goal names run 6, so it is rewritten on resume". That fact stands only in history.
- **Proposed:** question: rewrite the goal now, for example "CBC Run 5's CBC Run Reading has DECISION-1, DECISION-2 and DECISION-5 settled, and WORK-1 and WORK-3 to WORK-10 ended", and drop the Notes' "then Birth CBC Run 6 … opens"? Or leave it for the resume, with one line in the Plan Step saying so?

### SL2-6

- **Where:** `PLAN.md`, *Step: Take CBC Run 5's lessons for CBC Run 6*, own items, line 250.
- **Quote:** `- [ ] The playbook has no line meant for CBC Run 5 only.`
- **The rule:** a false line is wrong. The Plan Step Form says an item "is ticked when it comes true, whenever that is" (`PLAN.md` lines 76 to 77).
- **What the text says:** not yet true. It is true. `PLAN.md` lines 164 to 166, in Birth CBC Run 6, tick the same item: "taken here from the stopped Plan Step … (2026-10-29, `7f6e3a8`)". `delivery/fills/cbc-run-pure-playbook.md` names no CBC Run 5.
- **Stands:** resting on the reader. That the item is true is checked. Whether an item another Plan Step took should be ticked or struck is the reader's call.
- **Why it was missed:** it came true in the other Plan Step on 2026-10-29. Only that Plan Step's copy was ticked.
- **Proposed:** fix: `- [x] The playbook has no line meant for CBC Run 5 only: taken by Birth CBC Run 6, on full auto (2026-10-29, `7f6e3a8`).`

### SL2-7

- **Where:** `PLAN.md`, *Step: Refine this repo against its own rules*, Notes, lines 409 to 412.
- **Quote:** `made the approach-drafting Approach on Trial, and the first of the`
- **The rule:** a false line is wrong.
- **What the text says:** the refinement is the first use of the approach-evaluation Approach on Trial. It is not. `.claude/approaches-on-trial/approach-evaluation.md` *Uses*, line 129 to 130, gives its first use: "`model-placing.md`'s first evaluation, 2026-10-28 … Its first use."
- **Stands:** checked.
- **Why it was missed:** it was written 2026-10-20 (`4acf611`), when the refinement's close was to be the first evaluation. It became false on 2026-10-28. `bcf3010` (2026-11-01) reworded it for Names and kept it.
- **Proposed:** fix: "- The first use of first-time work on our Convention Seat, which ADR-0058 made the approach-drafting Approach on Trial. The approach-evaluation Approach on Trial was first used on 2026-10-28, for `model-placing.md`. This Plan Step's close judges both."

### SL2-8

- **Where:** `TODO.md`, *Next*, "Decide whether a commit plan's look-back also asks if the work could have been done better", Context, lines 87 to 88.
- **Quote:** `of them, and 2 changed the answer. CBC Run 5 tries it first, from`
- **The rule:** a false line is wrong. The item form asks for a Context "true today" (`TODO.md` header, line 13).
- **What the text says:** CBC Run 5 will try it. CBC Run 5 has run through Release and has been read. `temp/reading-run-5-2026-10-22.md` line 152 records the try: "FINDING-9. The look-back on trial: 13 lines, 0 tries". WORK-17 (line 549) gives this item that finding.
- **Stands:** checked.
- **Why it was missed:** it became false when CBC Run 5 ran, 2026-10-22. Leftover E8 names this item's trigger (line 95), not this Context line.
- **Proposed:** fix: "CBC Run 5 tried it from its CBC Run Hand-off: 13 look-back lines, 0 tries (its CBC Run Reading, FINDING-9)."

### SL2-9

- **Where:** `TODO.md`, *Next*, "Decide whether the concept, the conventions and the Approaches on Trial keep examples", Context, line 103.
- **Quote:** `The method's worked example, 271 lines in both the cbc-framing`
- **The rule:** a false line is wrong.
- **What the text says:** 271 lines. Both copies, `delivery/method/.claude/skills/*/references/worked-example.md`, hold 328 lines today.
- **Stands:** checked.
- **Why it was missed:** missed at a change. The count was right at `4620995` (2026-10-21). Round 3's rewrites of the file (`8316ce0`, `ce370e4`, 2026-11-01) grew it, and nothing re-reads a count in TODO when the counted file changes.
- **Proposed:** fix: "The method's worked example, 328 lines in both the cbc-framing".

### SL2-10

- **Where:** `TODO.md`, *Next*, "Evaluate the auto-run Approach on Trial", Context, line 192.
- **Quote:** `Context: drafted and used once, for CBC Run 5`
- **The rule:** a false line is wrong.
- **What the text says:** used once. It was used twice. `PLAN.md` line 151 says Birth CBC Run 6 used "the auto-run Approach on Trial, in its second use". The second use's note waits for that Plan Step's close (`PLAN.md` line 199).
- **Stands:** checked.
- **Why it was missed:** it became false on 2026-10-29. Round 3's read met it (refinement file, line 2244), and it was not fixed.
- **Proposed:** fix: "Context: drafted for CBC Run 5 and used twice, for CBC Runs 5 and 6 (`.claude/approaches-on-trial/auto-run.md`, its use note; CBC Run 6's note waits for its birth Plan Step's close)."

### SL2-11

- **Where:** `TODO.md`, *Next*, "Decide whether our own forms become Output Shapes", Ideas, lines 479 to 481.
- **Quote:** ``Only `.claude/decisions.md` holds one under another``
- **The rule:** a false line is wrong.
- **What the text says:** among the records, only the Decisions Log holds its form under a convention other than project-recording. `docs/glossary.md`, a record in `CLAUDE.md`'s records table, holds its form under the writing convention (line 23, `foundation: the writing convention`).
- **Stands:** checked.
- **Why it was missed:** missed at a change. The line was written 2026-10-23 (`026640d`). `8919dac` (2026-10-27) gave the glossary its own file and its Foundation Line. No Change Walk reaches TODO.
- **Proposed:** fix: "Only `.claude/decisions.md` and `docs/glossary.md` hold one under another convention: agent-arrangement and writing."

### SL2-12

- **Where:** `TODO.md`, *Next*, "Rename the manuals, Agent Skills and Agent Rules that share a name", Context line 534 and Ideas line 544.
- **Quote:** `four of the names ship, so a rename moves every CBC Run's`
- **The rule:** a false line is wrong.
- **What the text says:** four of the five shared names ship, and line 544 says "four ship". All five ship:
  - `delivery/container/.claude/skills/` holds commit-messages, commit-plan, visual-comparison and retrospective;
  - `delivery/container/.claude/rules/writing.md` is the writing Agent Rule.
- **Stands:** checked.
- **Why it was missed:** never true. The item was written 2026-10-31 (`72d76c7`, `0f91b8b8`). The shipped writing Agent Rule has existed since `83acdfe`, 2026-10-15.
- **Proposed:** fix: line 534, "all five names ship, so a rename moves every CBC Run's"; line 544, "hold-retrospective, write-plainly; all five ship, so every CBC".

### SL2-13

- **Where:** `TODO.md`, *Next*, "Read a CBC Run born before the refinement by its needs, not its diff", Context, lines 565 to 566.
- **Quote:** `item taken would land in text Refinement Round 3 rewrites.`
- **The rule:** a false line is wrong.
- **What the text says:** Refinement Round 3 is still to rewrite the text. Round 3 closed at `c6b3635` (`PLAN.md` line 306).
- **Stands:** resting on the reader. That Round 3 has closed is checked. The reason still holds for the last read, which may change text again.
- **Why it was missed:** written 2026-10-31 (`e7ee475`), before Round 3 closed on 2026-11-01. `bcf3010` reworded it and kept it.
- **Proposed:** fix: "The readings come after the refinement, not before: an item taken now could land in text the refinement's last read changes."

### SL2-14

- **Where:** `TODO.md`, *Next*, "Rewrite the method's texts plain", Context, lines 646 to 649.
- **Quote:** `Agent Skill and workflow (`2674c03`). Not yet, about 26,000 words:`
- **The rule:** a false line is wrong. The item form asks for a Context true today.
- **What the text says:** the cbc-framing Agent Skill, the stack's Agent Skills, the concept chapters and System Readiness are not plain yet. Refinement Round 3 rewrote all of them against the writing rule. Examples are `1f0c17e` (the chapters), `4884a12` and `ce370e4` (cbc-framing), and `c449de0`, `580f7dc` and `78fe685` (the stack). DECISION-16, chosen (a): "All 188 are worked in layer 6 … the item closes with them, or keeps what the work left".
- **Stands:** checked.
- **Why it was missed:** missed at a change. `e5a874b` and `bcf3010` (2026-11-01) reworded this Context for Names after the chapters were rewritten, and `bcf3010` after the method and the stack were too. Round 3 read for Writing only. The item's own trigger, "what Refinement Round 3 did leaves this item", was not acted on at Round 3's close.
- **Proposed:** question: by DECISION-16 (a), does the item close now? Or does it keep only what Round 3 left, its Context rewritten to name that?

### SL2-15

- **Where:** `TODO.md`, the same item, Ideas, lines 662 to 669.
- **Quote:** `citations of CBC Run 3's RETRO.`
- **The rule:** a false line is wrong.
- **What the text says:** Refinement Round 2's FINDING-206, "the playbook's 12 citations of CBC Run 3's RETRO", and FINDING-224, "the 'lived' markers", wait in this item. Both are gone:
  - `7f6e3a8` (2026-10-29) removed exactly 12 RETRO lines from the playbook; its 4 left are the CBC Run's own `RETRO.md`;
  - grep finds no "lived" in `delivery/method/` or `delivery/spring-postgres/`, gone in Round 3 (`a6ccf5b`, `580f7dc`, `78fe685`).

  The refinement file's *Moved to TODO* (line 2354 to 2357) says these findings "are worked in this round's layer 6, by DECISION-16: the item keeps only what the round leaves".
- **Stands:** checked for FINDING-206 and FINDING-224. FINDING-223, 227 and 228 were not checked one by one.
- **Why it was missed:** missed at a change. The item was not trimmed when Round 3 worked these findings.
- **Proposed:** fix: drop FINDING-206 and FINDING-224 from the list. Check FINDING-223, 227 and 228 the same way, and drop what Round 3 fixed.

### SL2-16

- **Where:** `TODO.md`, *Next*, "Read what CBC Run 5's first Invariant Slice's Plan Step Gate found against the Evidence Test Shape", Context, lines 733 to 734.
- **Quote:** ``Output Shapes at birth (the item on `.claude/shapes/`). The cbc-slice Agent Skill``
- **The rule:** a false line is wrong.
- **What the text says:** it points at an open TODO item on whether a Newborn CBC Run reads its Output Shapes at birth. No such item exists. ADR-0061 (2026-10-21), "A newborn reads its shapes at the gate, not at birth", settled it, and its Context says "TODO held the question since 2026-10-17". The "unless" is decided.
- **Stands:** checked.
- **Why it was missed:** it became false at ADR-0061, 2026-10-21. Round 3's read met it (refinement file, line 2247), and it was not fixed.
- **Proposed:** fix: "birth, so CBC Run 5 is the first clean one: since ADR-0061 a Newborn CBC Run reads its Output Shapes at the Plan Step Gate, not at birth. The cbc-slice Agent Skill".

### SL2-17

- **Where:** `TODO.md`, *Next*, "Decide whether a standing full read looks for missing Fact References", Context, lines 809 to 811.
- **Quote:** `close read ran with seven agents and 52 findings.`
- **The rule:** a false line is wrong.
- **What the text says:** Round 2's close read ran its Dependencies Finding Kind with seven agents and 52 findings. The refinement file's *Round 2's close read* (lines 808 to 810 and 870 to 873) says otherwise:
  - the seven readers covered all four of Round 2's Finding Kinds, Dependencies on each side being two of them;
  - the 52 are all the readers' findings;
  - Dependencies had 19.
- **Stands:** checked.
- **Why it was missed:** never true as written. It came in at `8a81a02` (2026-10-27).
- **Proposed:** fix: "repo for it today: their Dependencies Finding Kind, which two of Refinement Round 2's seven close-read agents ran, with 19 findings."

### SL2-18

- **Where:** `TODO.md`, *Later / someday*, "Decide what our CHANGELOG tracks", Context, line 934.
- **Quote:** `out. Since v1 (2026-08-28), about 1,350 commits added the`
- **The rule:** a false line is wrong. The item form asks for a Context "true today".
- **What the text says:** about 1,350 commits since v1. `git log --since=2026-08-28` counts 1,802 on main and 2,107 on this branch.
- **Stands:** checked.
- **Why it was missed:** a dated count, right at `8042a18` (2026-10-21), never refreshed.
- **Proposed:** fix: "out. Since v1 (2026-08-28), about 1,800 commits on main added the". Or drop the number: "most commits since v1 added the".

### SL2-19

- **Where:** `TODO.md`, *Later / someday*, "Watch whether the worked example anchors a CBC Run's CBC Framing", Context line 1168 and Trigger lines 1172 to 1173.
- **Quote:** `Trigger: the next CBC Framing read on a different kind of`
- **The rule:** a false line is wrong. A passed trigger is a stale line.
- **What the text says:** the trigger is still to come. CBC Run 5, `event-tickets`, framed a different kind of problem from the example's order service: two areas and a non-empty LAYER-5. Its CBC Run Reading read that framing on 2026-10-22, in *What run 5 teaches the worked example* (`temp/reading-run-5-2026-10-22.md` lines 422 to 445). The Context's "No evidence in three CBC Runs" also predates CBC Runs 4 to 6.
- **Stands:** resting on the reader. That the framing was read is checked. Whether that read is "the next CBC Framing read on a different kind of problem" is the reader's call.
- **Why it was missed:** the trigger passed at CBC Run 5's Reading, and the item was not re-read then.
- **Proposed:** question: has the trigger fired, so that the item is now due with what CBC Run 5's Reading §6.3 found? Or does it wait for CBC Run 6's?

### SL2-20

- **Where:** `TODO.md`, *Later / someday*, the Triggers of "Decide whether the Infrastructure Contract carries a paragraph on the store's facility" (line 989) and "Add a level for System Guarantees held by absence" (line 1197).
- **Quote:** `Trigger: CBC Run 5 meeting a System Guarantee held by absence.`
- **The rule:** a false line is wrong. A trigger that can no longer come, or has passed unseen, is stale.
- **What the text says:** both wait for something CBC Run 5 will do. CBC Run 5 has run through Release and has been read. Its CBC Run Reading has no line on either; grep finds no "absence", "facility" or "Infrastructure Contract" in it. So either each trigger fired and was not seen, or it can no longer fire as written. Round 3's read met line 1197 (refinement file, line 2246): "its Run Reading can answer it".
- **Stands:** uncertain. What CBC Run 5 did is in its repo, which is locked (`TODO.md` lines 45 to 60).
- **Why it was missed:** the triggers name one CBC Run, now finished. Its reading did not ask them.
- **Proposed:** question: re-aim both at "a CBC Run's CBC Run Reading finds …", or ask them at CBC Run 5's remaining work?

### SL2-21

- **Where:** `TODO-CONVERSATION-MEMORY.md`, header comment, line 21.
- **Quote:** `Last touched: 2026-10-31.`
- **The rule:** a false line is wrong. ADR-0060 decision 2 says the header holds "the date of its last touch".
- **What the text says:** last touched 2026-10-31. `a6f2a67` changed the file on 2026-11-01: its title, "TODO's Conversation Memory".
- **Stands:** checked.
- **Why it was missed:** missed at a change. `a6f2a67`, a Writing fix, changed the title and not the date.
- **Proposed:** fix: `Last touched: 2026-11-01.`

## Refinement Layer 5

### SL2-22

- **Where:** `.claude/approaches-on-trial/auto-run.md`, *Ways rejected*, lines 85 to 88.
- **Quote:** `makes any CBC Run full-auto. Rejected for now: one full-auto CBC Run has`
- **The rule:** a false line is wrong.
- **What the text says:** one full-auto CBC Run has been lived. Three have:
  - CBC Run 4 (`TODO.md` line 418, "ran on full auto through Release");
  - CBC Run 5 (this file's *Uses*);
  - CBC Run 6 (`TODO.md` lines 38 to 40).
- **Stands:** checked.
- **Why it was missed:** written 2026-10-21 (`b1efa42`), before CBC Run 5's birth. It became false on 2026-10-22 and again on 2026-10-29. `e2d66ea` (2026-10-30) reworded it for Names and kept it.
- **Proposed:** question: is a rejection's reason Living Text, to be kept true ("three full-auto CBC Runs have been lived, and a shipped Agent Rule would decide for every CBC Run what three have shown")? Or does it say when it was weighed ("when drafted, one full-auto CBC Run had been lived")?

### SL2-23

- **Where:** `.claude/rules/one-home.md`, rule 2, lines 24 to 26.
- **Quote:** `copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the`
- **The rule:** a false line is wrong. The retelling's own Fact Reference names its source, `docs/conventions/exchange/` §3.2, *What goes*. One-home rule 4: "Each retelling whose Fact Reference names it is re-read".
- **What the text says:** after CBC Run Birth, the copies that go are Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the concept. Exchange §3.2 also lists "each group's Glossary Names, in `docs/glossary/`". So does `.claude/skills/exchange-deliver/SKILL.md`, Stage 1 step 1 and Stage 2 step 2.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `3630ed9` (2026-10-31) added the Glossary Names to what goes. `2158499` (2026-11-01, a Writing fix) then rewrote line 25 and kept the old list. Rule 4's re-read of each retelling was not run.
- **Proposed:** fix: "copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial, each group's Glossary Names and the".

## Found true, so not listed

- `ARCHITECTURE.md`:
  - eleven rows in §3, as the overview says;
  - the twelve conventions in §1.2, matching `docs/conventions/`;
  - five chapters;
  - the concept at v1, with [Unreleased] making v2;
  - CBC Runs 4 and 5's states;
  - the playbook "checked against concept v1", as its header says.
- `PLAN.md`: every commit it cites exists and says what the line claims: `c6b3635`, `2e9c26b` (the provisional manual, readable at that path), `fc4efe0`, `b3b2018`, `a002002`, `657d372` (on main), `aad9053`, `7f6e3a8`, `3f20857`.
- `TODO.md`:
  - the hashes `0cdc50c`, `49d06e6`, `e6538f6`, `cb41ade`, `f097695`, `e219401`, `8d5212d`, `b7c17ae`, `fbd1c5e`, `2674c03`, `4de6ba2`, `ccce6af`, `1aa928c`, `35edd3f`, `30eb42e` exist;
  - "five names are shared" holds;
  - "11 of the 12 Agent Skills" holds: 12 distinct names;
  - "the other nine" conventions holds: the index's order holds 3;
  - the playbook still ticks "reached main by fast-forward" (line 107);
  - project-recording §9.4 still says no Agent Skill or Plan Step asks for the Plan Steps to be confirmed;
  - nothing points into a concept chapter's section;
  - three Idea Models;
  - the twelve locked entries;
  - the Container Group's `TODO.md` has `## To the deliverer`.
- `devlog/README.md`: newest entries on top, a Resume line per entry. `.claude/decisions.md`: append-only, newest last. The dates are in order.
- `README.md`, `CLAUDE.md`'s records table and `CHANGELOG.md`'s header comment still name "those who pin a concept version". This is known: `TODO.md` lines 936 to 939 name it, and leftover E3 holds `README.md`'s line.
- `.claude/skills/` (all five) and `.claude/rules/` (all six): every path, section and file they name exists. Each claim about another file matches it, but for SL2-23.
- `approach-drafting.md`, `approach-evaluation.md`, `model-placing.md` and `refinement.md`: every cited commit exists (`4fedbb3`, `a629f52`, `8c9aadf`, `19f1d7b^:temp/eval-2026-09-30.md`). The eight Finding Kinds and the four rules of 2026-10-17 count right.
- `.editorconfig`, `.gitattributes`, `.gitignore`, `CLAUDE.local.md`, `docs/adr/README.md`, `temp/README.md`: no false claim found.

## Met in passing

- Leftover E6, marked gone at `075a7ff`, still stands. `TODO.md` lines 397 to 403 still say "three Chain Links, each with its upkeep: derives …, points …, governs …". The glossary (line 220 to 222) and `docs/models/idea-to-output.md` §3.1 give four: stands on, points, governs, written from. The joined-line search likely missed it because the parentheses now break up "derives, points, governs".
- Leftover E8's line list (95, 113, 186, 199, 308, 682, 737) leaves out two passed triggers reader E named, and both still stand:
  - `TODO.md` lines 773 to 774, waiting on Refinement Round 2;
  - lines 926 to 927, "after the Plan Step that runs CBC Run 5's CBC Run Birth closes", which closed 2026-10-22 (`43aaf30`).
- Leftover E7 names line 433 only, but reader E also named lines 694 to 695 and 747 to 748. Both still stand.
- *Met in round 3, of other kinds* (refinement file, lines 2203 to 2310) was not part of step 1's leftovers check. Several of its items still stand. Three are listed above (SL2-4, SL2-10, SL2-16). Its items of other Finding Kinds may need the same check.
- `temp/run-6-handoff/` is tracked, but no TODO item or Plan Step names it. `temp/README.md` line 12 says a kept file is named by one. This is a state of the tree, not a line.
- `ARCHITECTURE.md` §2's opening (lines 130 to 132) says the Stack Group derives from the concept. §2.2 (lines 148 to 149) says it is "Not derived from the concept but checked against it". This is Agreement inside one file.
- `.claude/rules/writing.md` *Where it applies*, "What CBC Runs read" (lines 106 to 109), does not name the delivered Glossary Names files.

## Not read

None. Every assigned file was read whole, but `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md`, read by header comment as assigned. `CHANGELOG.md`'s `[v1]` entry was read as history.
