# 0026. The models are ours; ADR-0002's clause goes

Date: 2026-09-18
Status: Proposed (opened inside the change-plan for taking the
models, per change-plans §4; flips at that set's final records
commit)

## Context

ADR-0025 took the kit and the conventions' manuals and made the
handbook provenance rather than an upstream. It did not mention
`docs/models/`, and the two files there — `tiers.md` and `agent.md`,
vendored under ADR-0002 — still carry this in their headers:

```
Pinned: do not edit here — changes happen in the handbook and
arrive as a fresh pinned copy. See ADR-0002.
```

So after this morning the repo has exactly one live upstream
dependency left, covering two files, and nobody decided to keep it.
It survived because the decision was written about the kit and the
models were not in view.

Two things make that residue worse than an oversight.

**The channel it depends on closed today.** The exchange with the
handbook ran to its end this afternoon and both sides recorded the
fork. The handbook is about to be parked. "Changes happen in the
handbook and arrive as a fresh pinned copy" now describes a delivery
from a repo nobody is working in — a rule that cannot fire, sitting
in shipped-adjacent text, which is the same defect the handbook
removed from its own ADR-0038 this afternoon: *an unresolvable
provisional mark tells every later reader to wait for something that
will not come.*

**It contradicts what the same records now say.** `ARCHITECTURE.md`
carries "Vendored models are never edited locally — changes arrive
only as a fresh pinned copy" as a standing invariant, two entries
below one that says the container's provenance is kept precisely
*because* nothing tracks that repo any more. Both are true as
written and they describe different worlds.

## Options considered

1. **Leave them vendored — one thin channel, models only.** The
   honest argument, and the one this repo leaned toward before the
   decision: the tiers model describes three tiers, and the tier
   that can see all three is the right owner of that picture. We can
   see two. Rejected: the cost is not the reading, it is the
   standing obligation and the live coupling — the thing ADR-0025
   dismantled for being paid weekly against a need that does not
   exist. Two files do not justify keeping a channel open to a
   parked repo, and a copy we may not edit is a constraint whether
   or not anyone exercises it.

2. **Drop the copies; summarize what we need into our own records.**
   Rejected, and already rejected once: ADR-0002 weighed it and
   found a hand-written summary lossy on arrival and free to drift
   while both files look current. Nothing about the fork improves
   that argument.

3. **Take them, as the kit was taken.** Chosen. The material is
   ours; where it came from is a fact written down; the obligation
   goes.

## Decision

1. **Both models are this repo's.** `docs/models/tiers.md` and
   `docs/models/agent.md` are ours to hold, to edit, and to let
   drift from what the handbook holds. No re-derivation is owed and
   no delta is tracked.

2. **The provenance is recorded in each header, as two hashes**, the
   shape ADR-0025 set. The bytes came from `ba7eaa4`; both files are
   verifiably identical through the handbook's `8adb46f`, so that is
   the last aligned state and divergence starts after it. The
   coordinates are what a re-sync would begin from, and nothing
   more.

3. **ADR-0002 is superseded in part.** Its decision that updates
   "arrive only as a fresh pinned copy from the handbook, never as
   local edits" no longer holds for these files. Everything else in
   it stands, and is why this ADR is not a replacement: its reading
   of why a pinned copy beats a live reference, and why a summary is
   worse than either, still governs every file this repo ships to a
   run. That reasoning was never about who owned the source.

4. **The bodies are taken verbatim, and editing is permitted, not
   owed.** Taking a document is not rewriting it. Both are the
   handbook's drafts, carrying their own drafting notes and, in
   `agent.md`, refutation conditions; those stay as written until
   something lived here contradicts them. A rewrite on the day of
   taking would spend the only thing that keeps a re-sync cheap and
   would claim authority over text no instance here has tested.

5. **The trigger for reopening: the handbook is revived and its
   models move materially.** Then the question is a compare, at the
   coordinates in decision 2 — not a resumed subscription. Until
   then there is nothing to reopen, because there is nobody moving
   the source.

## Consequences

Good: nothing in this repo tracks the handbook by reference or by
pin. The handbook appears only as recorded provenance, in four
places that name a hash. A contradiction between two standing
invariants is removed rather than lived with, and the `ARCHITECTURE`
diagram loses its last upstream arrow — the kit's went with
ADR-0025, the findings arrow closed with today's exchange, and the
models were the last standing reason to draw the box.

Bad, and named rather than discovered: **we now maintain a picture
of a tier we cannot see.** The tiers model's §3 was revised on this
repo's own report of five lived runs, so we have fed it before — but
feeding a model from below is not the same as owning its account of
what sits above. If that account goes wrong, nothing here will
notice. Accepted because the alternative was a live coupling to a
parked repo, which fails in the same direction and costs more.

Also bad: `agent.md` is a draft with refutation conditions attached
to its behavioural statements. Owning a draft means owning its
unfinished parts, and no procedure here says who refutes them or
when. Not solved by this decision; noted as the first thing
ownership makes ours that was previously somebody else's problem.
