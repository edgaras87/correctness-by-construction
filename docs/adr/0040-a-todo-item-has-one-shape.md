# 0040. A TODO holds open work, and an item has one shape

Date: 2026-09-29
Status: Proposed (2026-09-29, under the commit plan for the TODO
pass)

## Context

`docs/conventions/project-recording/` §5 said to prune the backlog
ruthlessly and named never deleting an anti-pattern. This repo's
`TODO.md` did the opposite. On 2026-09-29 it ran to 2,120 lines:
twenty-eight closed entries kept whole with their original text,
about half the file, and open items that grew by stacking a dated
update each time something changed — about a dozen lines as a
rule, the longest 248. The story of each item lived there a second time,
after the devlog and the ADRs, and sometimes only there.

The first question was the seat: whether the deliverer, which has no
project end, should keep closed entries as its record of what
closed. The second was the item. Once the closed entries went and
the stale ones were closed or given triggers, 31 items were left,
and each was built from the same five parts: what to do, when and
by whom it was raised, why it holds, when it is due, and a stack of
dated updates. The first four are what triage needs. The fifth is
history.

Run 3's `TODO.md`, read the same day at `9869798`, keeps no closed
entries but stacks answers on open items the same way: its longest
items run to 38 and 36 lines, one of them a record of what another
repository holds.

## Options considered

- **A seat rule keeping closed entries in the deliverer's TODO.**
  Rejected: what closed is already told by the devlog, the ADRs and
  git, so the rule would keep a second copy on purpose. The seats
  differ in project end, playbooks and versioning, and none of these
  touches a backlog.
- **Title and pointer only.** Rejected: triage happens at every step
  close, and it would have to open every pointer to judge an item.
- **A context field kept in a separate document, or `TODO` as a
  directory of an index and context files.** Rejected: context files
  would hold what the devlog holds — what was noticed, when, the
  evidence — so they are a second home that drifts. Many files hide
  growth that one file shows. And the stub ships to every run, so the
  shape of one repo's problem would reach every newborn. Work in
  progress already has `temp/`.
- **A context capped at three lines.** Tried on the material:
  twenty-seven of 31 items would not fit, and trimming them cut
  meaning and lost one fact that lived nowhere else.
- **A cap of five lines.** Proposed after the trial; the reviewer
  read the result and found several items needed a little more to be
  seen clearly.
- **A shape of the run's own.** Rejected on run 3's TODO: its items
  fit the same four parts. What differs — where an item is owed, a
  playbook or the deliverer — sits in the what line, and its
  sequencing items in Now are PLAN's job, not a second shape's.
- **An Options field: the choices with their cases, the leaning one
  marked.** Proposed at step 6's boundary, from five items carrying
  choices inside their Context. Rejected by the reviewer: options
  are weighed when the item is worked, not when it is written. What
  the writer has at that moment is an idea or two, unweighed, and
  that is what the field should hold.

## Decision

1. **A TODO holds open work only.** A closed item goes; the devlog,
   the ADRs and git say what closed.
2. **An item has one shape:** what to do or decide, with the date
   and who raised it; **Context**, at most eight lines, saying why it
   holds today; **Ideas**, optional; **Trigger**, the moment it is
   due; **See**, the devlog entry, ADR or commit that tells its
   story.
3. **The story is written where it happens.** When something is
   noticed, that session's devlog entry says so and the item points
   at it. An item that is its story's only home keeps it and has no
   See.
4. **No stacked updates.** An item that changes is rewritten true
   for today; the change's story goes to the devlog.
5. **One shape for both seats.** The container's `TODO.md` stub
   states it in its comment, where a run meets it;
   project-recording §5 explains it.
6. **Ideas are parked, not weighed** (the reviewer, 2026-09-29). An
   idea for how to handle an item is noted when it comes, a line
   each. When the item is due, each is taken, extended or declined,
   and the verdict is recorded with that work.

## Consequences

- This repo's `TODO.md` went from 2,120 lines to 337 over four
  commits of the TODO pass — the prune, the stale pass, the re-sort
  and the reshape — before this rule added its comment.
- The stub changed, so the shape reaches the next birth. Records
  never travel twice, so run 3 keeps its TODO as it is; the shape
  goes to it in a note, as an offer, and whether it takes it is the
  run's call.
- Triage at a step close reads each item without opening its
  pointer, and the devlog becomes the only place an item's history
  is written.
- Reopen when an item's context fits neither a devlog entry nor
  active work in `temp/` — the case a context directory would be
  for; or when eight lines stop being enough for items that are not
  carrying text to deliver word for word.
