# Commit plan: the playbook takes run 3's retrospective

## Summary — the state after all commits

The CbC run playbook, `delivery/fills/cbc-run-pure-playbook.md`, is
at v8. It opens on one step form, copied at birth with the steps:
Goal, a Now line, and a Gate made of the opening items, the step's
own items asked of its goal, and the closing items. At the close a
step's gate shrinks to one line. The two stock lines every step
carried are gone. The closing items gain three checks from run 3's
RETRO D17 and D2: the records hold together, no stale "now" line,
new text reads to the writing rule.

Between the slices and Release sit two new steps, Retrospective and
Apply the retrospective, which open the ADR-0054 skills. Release
keeps its own lessons in RETRO.md and opens after the apply step.
Step 2 reads the plan against the framing. Five checks only run 5
can answer wait at the steps that judge them, as 10 gate items, each
to be removed or kept by run 5's reading.

The seed copies the playbook from the step form down.
`apply-retrospective` stops listing two items every close now
carries. ADR-0055 records the seven decisions and what was
rejected. W3 of the reading of run 3 is done.

## Commits

The decisions are marked under W3 in the reading: six in
`e2ae15f`; the seventh, and a correction to the second, in
`9b813ae`.

**1. `docs(agent): add commit plan for the playbook`**
The approved plan.

**2. `docs(adr): 0055, the playbook takes run 3's retro`**
The seven decisions, Proposed: the step form and its home, the two
steps, Release, the closing items, run 5's checks, the middle-steps
line, and a closed step in one line. Each with its rejected
options.

**3. `docs: the playbook opens on a step form`**
The form section at the top, with run 3's opening and closing
items, W3 decision 4's three added, RETRO D4's trial rule, the
struck default, and W3 decision 7's one-line closed step. Each step
loses its two stock lines and gains a Now line. Version v8. The
header comment and the seed (`pure-seed.md`: its copy command, its
check, its three v7 references) say "from the step form down" in
the same commit: the form holds a `## Step <n>` line in its code
block, so the old copy command would start inside it.

**4. `docs: apply-retrospective leaves two to the close`**
§0.2 drops "every link resolves" and "no living line says now",
which commit 3 put in every step's close. Its own commit: another
file, and reverting it alone leaves a repeat, not a break.

**4b. `docs: the Now line moves at a stage, not a commit`**
Inserted after 4. Commit 3 put the Now rule only inside the
template's placeholder, which each step overwrites, and dropped its
second half (RETRO D4, 2026-10-13). One sentence outside the
template: Now changes at a new stage, not at every commit; inside a
commit plan, the plan and the branch's log show progress.

**5. `docs: the playbook gains the two retro steps`**
Steps N-2 and N-1, the slices renumbered 5..N-3. Goals from run 3's
drafts, with run 3's name taken out. The retrospective opens when
the slice steps close. Notes point at the manual for who decides.

**6. `docs: Release keeps its own lessons`**
A Known already item for Release's lessons in RETRO.md, in the
`retrospective` skill's form; a Notes line that it opens after the
apply step. After 5, which makes the apply step exist.

**7. `docs: Step 2 reads the plan against the framing`**
The middle-steps line, as a Known already item at Step 2.

**8. `docs: run 5's checks wait at their steps`**
Five checks from RETRO D22, as 10 gate items: RETRO D28's at six
steps, and D14, D18, D20's Release and D29 at one each. Each has
its reason, its source, and a line that run 5's reading removes or
keeps it. After 5 and 6, since three of the items sit at those
steps.

**9. `docs: records carry the playbook`**
ADR-0055 Accepted. TODO: the middle-steps item ends; the item to
fold run 3's arrangement pieces into the playbook ends (F17).

**10. `docs(agent): close commit plan for the playbook`**
Deletes this file; the body says what diverged.

After the close, the reading marks W3 done:
`docs(temp): the reading closes W3`.

## Decisions taken inside this plan

- **The step form lives in the playbook, as W3 decision 1 said, though
  `b82eaf7`'s body once placed it above the STEPS markers.** That
  body predates the form's verdict. ADR-0011 rejected two masters
  meeting in a newborn: the steps would cite a form from the
  container while the form serves only them. ADR-0055 names the
  earlier view as a rejected option.
- **One version, v8, set in commit 3.** No birth happens inside the
  set, so the later commits stay within v8.
- **No CHANGELOG entry.** Its header says a change to the delivery
  is none.
- **The three checks kept on our side** (facility, absence rung,
  evidence-test measurement) already have TODO items naming the
  next birth. Rewording them for run 5 is W6's TODO pass, not this
  set.
- **The container's PLAN stub is untouched.** Its placeholders serve
  a birth without a playbook; the swap replaces them.
- **The reading's D8 comes after this set.** If it settles on a line
  for a step with no skill, that line is a commit of its own on the
  playbook, outside this plan.
