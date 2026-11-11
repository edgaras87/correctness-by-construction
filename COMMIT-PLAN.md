# Commit plan: the simulation in six parts

## Summary — the state after all commits

`temp/system-repo-change-simulation.md` follows its case in the six parts of its §1 table, and no longer in two halves.

- **Its cases table is shorter.** One case covers a change to one Adapted Case, whichever of its two texts changed: when one changes alone, its entry says whether the other still matches (Failure Case 8). "A copy no longer used" is a kind of note, so it is the note row. The table goes from 15 rows to 12. Its "Half" column becomes "Kind": what changed, or how deep it goes.
- **Its steps sit in six sections,** one per part: Change, Read, Judge, Act on the verdicts, Deliver, Take. Steps are numbered inside each part, so a step added later renumbers only its own part.
- **The word "half" is gone** from both temp files, in both its meanings: a part of the case, and one text of an Adapted Case.
- **`temp/common-ground-problem.md` agrees with the simulation:** its pointers name the new sections, its rules sit under one heading per part, and "read to" moves once the verdicts are acted on.
- **The simulation's step 7 is written,** where its part is found to be.

## Commits

**1. `docs(agent): add commit plan, the six parts`**
This file.

**2. `docs: temp's simulation merges alike cases`**
§2's rows "both halves of one Adapted Case", "an Instruction Text only" and "an Adapted Understanding Text only" become one case: one Adapted Case, one text or both. The entry sits in the Adapted Understanding Text's footer either way, so the steps do not differ. What did differ goes into the steps: Change step 1's entry, and the problem file's *Recording a change*, say whether the other text still matches when one changes alone. "A copy no longer used" joins "a note with no change", since step 1 already lists an unused copy as a note. The scope paragraph and the header comment name the merged case, and the problem file's *Recording and reading* names it too.

**3. `docs: temp's simulation runs in six parts`**
§3 and §4 become six sections, one per part, steps numbered inside each. §1's table names the sections, and its moves speak of parts. §2's "Half" column becomes "Kind". The depth-a lead of the old §4 moves to the top of Judge. Every pointer to a moved step changes in this commit: inside the simulation, in the problem file (*What passes between the repos*, *Recording and reading*, *A System Repo's change*, and the step pointers), and `TODO.md`'s "step 4" in the item on resuming the simulation. The problem file's two bullets on halves become the two kinds of case.

**3b. `docs: temp's problem sorts its rules by part`**
*Recording and reading* and *Deciding and updating* become six headings, named as the simulation's sections, and each rule moves under its part unchanged: *Recording a change*, *A note* and *The gate* under Change; *Reading a change* and *The list* under Read; *Judging a change read back* under Judge; *A project-agnostic lesson* and *Narrowing, never shrinking* under Act on the verdicts. *An update* is split by bullet: what an update sends under Deliver, the other five under Take. Their wording stays, stale lines with it, until the rules are written from the steps. The line saying the rules are in two groups changes, and the simulation's header comment, which names the two old headings, changes in this commit.

**4. `docs: temp's problem moves "read to" when acted`**
The problem file's *Reading a change* and *The list* still move "read to" once the list is whole. The simulation moved it to once the verdicts are acted on (`b2f458c`). A stale fact of its own, apart from the halves.

**5. `docs: temp's simulation, step 7`** *(provisional)*
"The next reading does not find the change again." Its part is decided when it is written: likely Read, for the next reading, where it would answer *Reading a change*'s Open on how an update's changes are told from the System Repo's own. Its wording and split follow from that.

**6. `docs(agent): close commit plan, the six parts`**
Deletes this file. The body records what diverged. Before it, the sweep: "half", "halves", "first-half", "second-half", every old "§3, step" and "§4, step", and each old section title, grepped unwrapped across Living Text.

## Decisions taken inside this plan

- **Kept apart:** "a Defined Term", since it belongs to no one Adapted Case and has no footer for its entry; the two "on trial" rows, since they check different things (the reviewer, 2026-11-11).
- **The problem file's rules move by part in this plan,** commit 3b, as a move only. Rewording them from the steps is the work after this plan. The two old headings kept the halves alive in the problem file after commit 3 removed them from the simulation (the reviewer, 2026-11-11).
- **The merged case's rule goes in with the merge,** commit 2, so the problem file's *Recording a change* never lags the step it comes from.
- **Section titles** are the part names of §1's table. Each is checked against writing rule 10 when commit 3 is written.
- **Depth c** is not in this plan. It comes after step 7, as the Resume line set.
