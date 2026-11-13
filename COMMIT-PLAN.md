# Commit plan: carry out the take's branch and a look's cases

## Summary — the state after all commits

The simulation (`temp/system-repo-change-simulation.md`) holds both
decisions taken in the flow file (`temp/system-repo-change-flow.md`).
The take runs on a branch of its own: the System Kit Update committed as it
arrived, one commit per part, and a gate last, which decides the
Changes put back and the verdicts acted on as a Plan Step's gate
does. Main moves by fast-forward at that gate's close, so "main
moves only at a gate's close" is true again, and found item 1 is
solved. A look at a System Repo makes three checks, main moved,
Changes and Update due, and ends in one of cases A to D. After a
take, the older snapshot a Reading compares is the clean copy,
checked against its Version.

The flow file's Now pictures the simulation as it then stands. Its
two After sections, item 1a and item 2, are gone. How cases A to D
are shown is work of its own, a TODO item. A Change put back at a take is judged
like any other; a Change that comes back and is never settled is
left to practice, as an Open.

## Commits

**1. `docs: temp's take runs on a branch with a gate`**
The simulation's Take part (§8, step 1): the branch, the System Kit Update
committed as it arrived, one commit per part, the gate last, main
moving at the gate's close. The commit "that holds the Version" is
the clean-copy commit. The Change part's commit check (§3, step 1)
says "its commits", since a take now makes several. Its own commit,
since Read (commit 2) stands on it.

**1b. `docs: temp's take sits between two Plan Steps`** (inserted)
§8, step 1's *What must happen* opens: the Update is taken between
two Plan Steps, when the next is about to open, never in the middle
of one. It said "when the next Plan Step opens", then "before that
step opens". With its own branch and gate, the take sits outside
both steps.

**2. `docs: temp's look ends in one of four cases`**
The simulation's Read part (§4): a look's three checks and cases A to
D, and after a take, the clean copy as the older snapshot, checked
against its Version. The Opens these answer go, the one on judging
a Change put back again among them: it is judged like any other,
and the cost is accepted. A new Open names the rare case, a Change
that comes back and is never settled; its trigger, the first Change
judged twice with no settling. §4 is written in snapshot words:
*read to* is the snapshot already taken into account, main's latest
snapshot is the one checked, the commits between are history,
opened only to understand something deeper, and the clean copy is
the one special point, used only after a take. Provisional: where
in §4 the look sits is found when the text is written.

**3. `docs: temp's Now picture 1 takes the new take`**
The flow file's picture 1 and its table, redrawn on the take of
commit 1: its parts on a branch, the gate, main moving at c14. c2
loses its "main moves here?" mark. The next Reading compares from
the clean copy. The Key no longer says a bracket marks the commits
a Reading covers: it shows the two snapshots compared, and the
commits between them are history. The take's case 1, the take that
passes its check, is checked against the redraw, as §8, step 1,
*Before the take* writes it.

**3b. `docs: temp's take's gate compares the clean copy`** (inserted)
§8, step 1, item 8: the take's gate compares the Copies against the
clean copy, item 3's commit, not the Reading's stop. Against the
stop it would see every change the new Version brought; against the
clean copy, only the Changes put back and the verdicts acted on.
Item 1a's option a had it so; commit 1 wrote the stop.

**4. `docs: temp's Now picture 2 takes the new take`**
Picture 2 and its table, the same way. Its own commit: picture 2's
round, the postponed take and the refused take, has more to check.
The take's case 2, the refused take, is checked against the redraw,
as §8, step 1, *Before the take* writes it: whether it still holds,
and how it is worded. A case that does not hold is a revision of
this plan.

**4b. `docs: temp's refused take goes through a look`** (inserted)
The simulation's case 2 (§8, step 1, *Before the take*) is reworded:
there is no take, and the System Repo says so; the human has it
looked at, the look finds case C or D (§4, step 1, *A look at
main*), and a new Update replaces the waiting one. *Old Records*
loses "span" for snapshot words. Case C's *What follows* gains "then
check 3 again": after a refused take with no Copy changed, the
waiting Update still names the old stop, and without a new one
every take is refused. Found by commit 4's check of case 2.

**5. `docs: temp's flow drops its decided After items`**
The found-item-1 line in Now's intro, the 1a section and item 2 go.
Their facts now live in the simulation.

**6a. `docs: temp's R5 asks for the two snapshots`** (replaces 6a to 6d)
The flow file's R5 asks which two snapshots each Reading compares,
not where it starts and stops.

**6b. `docs: temp's opening order has an Update when due`**
§8, step 1: the order before a step opens has the Update made,
delivered and taken when one is due, and the gate-list question at
an opening asks the same. Both read as if an Update always comes,
though §7, step 1 sends one only when it carries something. Found
by case A's drawing.

## Decisions taken inside this plan

- **The simulation first, the flow file after.** The flow file says
  its facts live in the simulation, so the simulation changes before
  the pictures follow it.
- **Items 1a and 2 are carried out together.** Both change the
  simulation's take and Read, and Now's pictures; apart, Now would be
  redrawn twice.
- **A Change put back is judged again.** The reviewer decided it:
  every Change is judged, the take's among them. A personal one is
  confirmed and nothing is sent; one judged otherwise gets its
  System Kit change or its verdict, as any Change does.
- **The TODO item on the delivery window is untouched.** Item 2 states
  today's rule: an Update waits for the step's gate, or the human's
  word. Whether a check of the window is a must stays that item's.
- **No records commit inside the plan.** No ADR, glossary entry or
  CHANGELOG line is due, since the drafts in `temp/` are not the concept.
  The devlog entry is written at the session's end.
- **The case pictures leave the plan.** Case A's commit picture
  repeated picture 1, and showed its case in three lines. A look is
  a choice between four outcomes, so its form, a picture of commits,
  a diagram or the table, is chosen first, as work of its own with
  the visual-comparison Agent Skill.
