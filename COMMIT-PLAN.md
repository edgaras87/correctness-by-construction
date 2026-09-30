# Commit plan: the eval, held

## Summary — the state after all commits

The whole repo was read on 2026-09-30 by six readers, one area each,
and their findings checked against the tree. About sixty findings in
six groups: what reaches a run, the method's contradictions, our own
seat against its manuals, manuals wrong now, the front door and
records, the ADRs.

They are held, not fixed, in `temp/eval-2026-09-30.md`: one line per
finding, numbered, where it is and what is wrong, nothing decided —
the form a reading of a run takes, because this is a reading of
ourselves. Each later set opens on one group, makes its own plan
then, and strikes its lines at its close. The file is deleted when
it is empty.

TODO holds only what waits on something:
- the reviewer's decision on the commit type for a new agent skill
  here, `feat(agent)` or `chore(agent)`;
- whether the three ADRs partly reversed on 2026-09-24 (0030, 0031,
  0035) need an ADR of their own;
- "Read run 3 and deliver" loses "first": the eval's group 1 comes
  before it, since a delivery now would carry those defects.

`temp/README.md` names the eval among what `temp/` holds.

## Commits

**1. `docs(agent): add commit plan for the eval`**
This plan.

**2. `docs(temp): the eval's findings, held`**
`temp/eval-2026-09-30.md`, and the one line in `temp/README.md`.
Each finding says whether it was checked against the tree or rests
on its reader's evidence, and the uncertain ones say so.

**3. `docs: TODO holds what the eval defers`**
The two decision items, and the run 3 item's trigger.

**4. `docs: devlog carries the eval`**
The session's entry: the readers, the groups, where the list lives,
the order.

**5. `docs(agent): close commit plan for the eval`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Held in `temp/`, not filed in TODO.** Most findings are wrong
  now, not waiting, and sixty items would drown the backlog. TODO
  takes only what waits on a decision or a trigger.
- **No plans ahead.** A set's plan is made when it opens, from what
  is true then; group 1's fixes change what groups 2 and 4 need.
- **Not named `reading-*`.** That name loads the reading rule, which
  is the shape of a reading of a run; this list borrows its form but
  is not one.
