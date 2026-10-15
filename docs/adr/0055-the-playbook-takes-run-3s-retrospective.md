# 0055. The playbook takes run 3's retrospective

Date: 2026-10-16
Status: Proposed (under the commit plan for the playbook)

## Context

Run 3, never-oversold, closed its retrospective on 2026-10-12. Ten
of its decisions name the run playbook as a place they land (its
`RETRO.md`). Seven are taken here:

- **D1 and D4:** a gate says what, not how. A step's own items are
  asked of its goal, and the skill's stages are not copied in. A
  closed step shrinks to one line. Run 3's Step 8 gate ran to about
  150 lines, most of it `cbc-slice` retold, and its PLAN to 1,216
  lines.
- **D17 and D2:** each close checks what run 3's clean-up pass later
  swept for. That pass took 8 agents and found 20 fixes, most of
  them left by a step whose own close could have caught them.
- **D22:** eight checks only the next run can answer, each to sit at
  the step that judges it. A list in `RETRO.md` is never read by the
  run that must answer it.
- **D23 and D24:** a retrospective step and an apply step, before
  Release. ADR-0054 shipped their skills and left the steps to the
  playbook.

The other three go elsewhere. D8, the briefing committed at
framing, is the reading's group E. D25, new work started from a
provisional manual, is the reading's D8. D26's half is in
`cbc-bootstrap`'s close already.

Run 3 also reshaped its Release step at birth, and asked us to fold
it back (its TODO, held since 2026-09-23). Two of our own TODO items
wait on the same file. One folds run 3's arrangement pieces into the
playbook once its retrospective judged them; D4 kept all three. The
other, open since 2026-09-10, tells a run at Step 2 to read its plan
against its framing; no text of ours tells it today.

Playbook v7 repeats two stock lines on each of its seven steps, has
no step for either skill, and gives Release no item for its own
lessons.

## Options considered

- **The step form in the container's PLAN stub, above the STEPS
  markers.** Run 3 placed it there, and `b82eaf7`'s body said the
  same before the form had a verdict. Rejected: the steps would use
  a form from another file, and ADR-0011 rejected two masters
  meeting in a newborn. A re-run of the swap would also leave the
  form behind.
- **The form's instruction as a rule.** Rejected, as run 3's D4 did:
  it is used once per step, when the gate is written, and a rule
  reaches only the agent, not the reviewer reading PLAN.
- **A closed step keeps its ticked gate in PLAN.** Rejected: nobody
  reads a closed gate again in PLAN, and the commit that closed the
  step holds it whole.
- **Gate items written ahead for the two new steps,** as run 3's
  drafts have them. Rejected: most retell the skills' close, which
  D4 rules out, and no other step has them.
- **Release's Known already list dropped with the stock lines.**
  Rejected: every Release needs those items, whatever its goal says.
- **Run 3's `records.py` as the tool of the records check.**
  Rejected at the reading (its F8): this repo holds no code, and
  half the script is run 3's own. The item states the outcome.
- **All of D22's checks as gate items.** Rejected: a run reads a
  gate before its work starts. A check of whether it does something
  unasked is spoiled once it is asked.
- **The checks left in a note or in our TODO.** Rejected, as D22
  did: the run never reads them.

## Decision

1. **The playbook opens on one step form, copied at birth with the
   steps.** A step has a Goal, a Now line, and a Gate. The gate is
   the opening items, the step's own items asked of its goal, and
   the closing items. A trial names the close that judges it, and
   its verdict is one line: kept, changed or dropped. A default that
   does not fit a step is struck there, with its reason. The seed
   copies from the form down.
2. **Two steps come between the slices and Release:**
   Retrospective and Apply the retrospective, each opening its
   skill. The first opens when the slice steps close. Each has a
   goal and the form's gate, and no items written ahead.
3. **Release keeps its Known already list,** the one step that does.
   It gains Release's own lessons in `RETRO.md`, and opens after the
   apply step.
4. **Every step's close gains three checks.** The records hold
   together: links, paths, cited numbers, and each pair of copies.
   No living line says "now" about what the step changed. New text
   reads to the writing rule. A run may write its own script for the
   first.
5. **Five of D22's checks wait at their steps,** as 10 gate items,
   each with its reason and source. Run 5's reading removes or keeps
   each. Three checks stay with us, never told to the run: the
   store's facility, the absence rung, and the evidence-test
   measurement.
6. **Step 2 reads the plan against the framing,** as a Known already
   item for every run.
7. **At the close, a step's gate becomes one line:** the date, what
   the step delivered, and the commit that holds the ticked gate.
   This is part of the close, not a later edit, so a closed gate
   still keeps its words.

## Consequences

- The playbook is v8, and `pure-seed.md` names it.
- `apply-retrospective` stops listing the two checks every close
  now carries.
- The two TODO items end.
- Run 5 is the first run born under v8. Decisions 1 and 7 are first
  used there, and its reading judges the five checks.
- The reading's D8 may add a line to the form, for a step with no
  skill.
