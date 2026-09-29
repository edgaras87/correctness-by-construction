# 0042. Two derivations of one set of conventions

Date: 2026-09-29
Status: Proposed (2026-09-29, under the commit plan for the split)

## Context

The convention manuals in `docs/conventions/` describe how a project
is kept, from two seats: a run's, a builder's, and the deliverer's,
a maintainer's. `delivery/container/` is those conventions made
usable, and ADR-0038 settled whom for: "what CbC runs need", since
keeping it close to a universal kit "had no reader".

This repo has gone on treating the container as the source of its
own setup as well:

- **Its skills are renewed from the container at a pin.** The
  decisions log, 2026-09-19: "the four pinned copies are updated to
  this repo's container @ 478ecdc … First update taken from our own
  container". And on 2026-09-27: "Copies renewed … copied whole
  from `delivery/container/` at 76f077c".
- **Its records are kept "under the same stubs"**, in
  project-recording's "made usable as" list and in both of its
  seats. commit-messages names "the deliverer's own skill copies
  renewed from the container". `docs/master.md` §4 calls the two
  arrangements "tied to each other".

The same entry of 2026-09-19 saw the circularity and left it open:
"we are the deliverer and a receiver of the same artifacts … the
convention's language assumes two repos, and a second instance
should say whether that assumption needs writing down or is
harmless."

It is not harmless. PLAN no longer matches the container's stub:
ADR-0041 made the deliverer's plan milestones only, with no STEPS
markers and no "Steps from" line. The entry files were never the
same. A run's opens on a builder's work; ours sits at the root and
opens on a maintainer's. And agent-arrangement records the failure
this invites: "Reading a shared file and assuming a shared job is
how a rule ends up held in the repo that cannot apply it", as
`convention-lifecycle` was held here from 2026-09-03 to 09-26 and
never once run.

At the level of each file, the right relation is already declared.
Every skill and rule this repo holds names its convention as its
`foundation` — "the commit-plan convention", not the container.

## Options considered

- **One container for both seats**, the deliverer receiving from its
  own shipped files. This was the practice, and it is rejected on
  the evidence above: the jobs differ, and they have already made
  the files differ.
- **A maintainer's container now**, beside the run's. Rejected as
  built ahead: it would have one user. When a second maintainer
  repo is needed, one is filtered out of this repo — the
  functionality and layout kept, this concept's own content dropped
  (the reviewer's idea).
- **Diverging the identical files to make the separation visible.**
  Rejected: three skills are byte-identical today because their
  manuals ask the same of both seats. Changing them would be a
  change nobody needs.

## Decision

1. **The manuals are the one source.** Two things derive from them:
   `delivery/container/`, the run's, and this repo's own records
   and `.claude/`, the deliverer's.
2. **Neither is copied from the other.** When a convention changes,
   each derivation is updated from its manual. A file identical in
   both is an outcome, not a dependency.
3. **The deliverer's own files carry no pin.** The decisions log
   stops recording copies of our own skills taken at a commit of
   this repo.
4. **No maintainer's container until a second maintainer repo
   needs one.** It is then filtered out of this repo.
5. **The run's side does not change.** The container, its stubs and
   what it ships stay as they are.

## Consequences

- project-recording, agent-arrangement, commit-messages,
  `docs/master.md` §4, `delivery/README.md` and ARCHITECTURE stop
  saying the deliverer's setup comes from the container.
- A change to a convention that both seats hold is two edits, one
  per derivation, each checked against the manual. That was already
  true in practice; the renewals were the second edit made by
  copying.
- The decisions log's 2026-09-19 question is answered: the
  assumption did need writing down, and the answer is that there are
  two derivations, not a deliverer that receives from itself.
- Nothing reaches run 3: its container is what it was.
