# 0002. Vendor handbook models as pinned copies

Date: 2026-08-27
Status: Accepted

## Context

Two handbook models bear directly on this repo's work: the tiers
model is the stated picture behind its whole shape (Framing reasons
against it), and the agent model is the design vocabulary for the
executions this repo exists to derive — channel choice, delivery,
and the claims that justify them. The records already point at them
(CLAUDE.md, README, ARCHITECTURE). The question is how the text gets
here.

## Options considered

1. Reference the handbook by path — free, but the tiers model itself
   rules it out: nothing downstream tracks upstream by reference;
   delivery is a pinned copy. A live reference also changes meaning
   silently whenever the handbook moves.
2. Summarize what's needed into this repo's records — agent model
   M1/M2: a hand-written summary is lossy on arrival and can drift
   while both files look current.
3. Vendor pinned copies with provenance headers — the same delivery
   the kit's skills already use; staleness is visible (the pin names
   a commit) instead of silent.

## Decision

Vendor both models under `docs/models/`, byte-identical to the
source below a provenance header naming the source path, the
handbook commit at copy time (4fe8083 — the same commit as the kit
birth pin), and the no-local-edits rule. Project-side placement, not
`.claude/`: here the models are reference material for the project's
own deliverables — executions are this repo's content — not part of
the working arrangement. Updates arrive only as a fresh pinned copy
from the handbook, never as local edits.

## Consequences

Good: Framing and execution authoring reason against the models'
actual text at a known version; records may point at the copies
without restating them.
Bad: the copies go stale as the handbook moves — accepted, because
the pin makes staleness inspectable, and nothing here tracks
upstream by reference; refreshing the pin is a deliberate act.
