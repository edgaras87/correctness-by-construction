# Change-plan: framing record shape + safe-reservations harvest

## Summary — the state after all commits

The cbc-framing skill carries the record-shape decision and the
safe-reservations harvest (TODO Framing check run 2; node read
read-only, its custom language never adopted — only the framing
logic travels, reworded):

- **The derivation doc**: framing's working record is one file,
  `framing.derivation.md`, in the run's repo — one section per
  step, each split "what this step earned" (clean) / "how it ran"
  (reasoning, probes, dead ends); a section freezes at its verdict
  (later changes only as logged return trips); a bulky mechanical
  sweep may live as a referenced appendix file carrying no
  decisions. Framing verdicts live inline in this doc; delegation
  (if any) in the run's .claude/decisions.md; adoption as one ADR.
- **The export**: at close the three exports are composed from the
  earned blocks under a residue filter (exports never reference the
  derivation doc's machinery), committed in derivation order —
  intent, then the definition growing L2 → L1 → L4 → L3 → L5, then
  the registry, then the adoption record — so the run repo's git
  history tells the derivation story. The derivation doc is kept as
  the archive, never deleted. "All paper, no repo" is corrected:
  the stub-born repo is the paper's home.
- **Census machinery** (workflow step 2): the three probe lenses as
  runnable procedure (assumption hunt, stretched timeline, resource
  grid), the three-stamp rule, the audit checklist; the exit records
  its ledgers — numbered fences (W-list) in ink, the not-probed
  ledger, scope verdicts each with recommendation and reason.
- **Intent outcomes** (step 0): audience is who the claim is sold
  to (consumers belong in the census); worth-proving; what done
  demonstrably means (adversity genuinely created, witness never
  fires, legibly).
- **Step 6 named as three passes**: theorem/definition sort with a
  written because per stamp → pairwise dedupe (must the evidence
  create different adversity?) → folds.
- **Registry template refined**: adversity-class grouping as
  headings-never-boundaries, riders (silent violation voids the
  slice's evidence), evidence-shape flags, the written zero.
- **TODO updated**: the framing-check and record-shape items
  resolved; two Later items added (two-tier harvest idea beside
  ADR-0007; a define phase — name, repo name, repo description —
  for cbc-bootstrap's territory).

Every edited file gains dated harvest lines naming safe-reservations
as the source, in this repo's own wording.

## Commits

**1. `docs(agent): add change-plan for framing shape`**
The agreed plan, timestamped before the work.

**2. `docs(executions): adopt derivation-doc export`**
SKILL.md's export section rebuilt around the shape decision: the
derivation doc with its three rules, the residue filter, the
derivation-order commit sequence, where each record kind lives, the
"no repo" correction. The shape is one decision — it lands whole.

**3. `docs(executions): enrich intent outcomes`**
Workflow step 0 and the skill's step-0 gate gain the audience
distinction, worth-proving, and done-demonstrably-means.

**4. `docs(executions): teach the census probes`**
Workflow step 2 gains the probe machinery as procedure: the three
lenses, the three-stamp rule, counted saturation restated against
the stamps, the audit checklist.

**5. `docs(executions): record census exit ledgers`**
Workflow step 2's exit gains the numbered fence list, the
not-probed ledger, and scope verdicts as a named output — distinct
from commit 4: that one is how to probe, this one is what the exit
must leave behind.

**6. `docs(executions): name step 6's three passes`**
Workflow step 6 restructured as sort → dedupe → folds, each pass
with its test and its record.

**7. `docs(executions): refine registry template`**
The template and the skill's outcome list gain headings-never-
boundaries grouping, riders, evidence-shape flags, the written zero.

**8. `docs: update TODO after framing checks`**
Both resolved Next items deleted; the two parked Later items added.

**9. `docs(agent): close change-plan for framing shape`**
Deletes this file; body records what diverged.

## Decisions taken inside this plan

- **The derivation doc is named `framing.derivation.md` at the run
  repo's root** — a visible sibling of the three exports the skill
  already places at root; appendix files (if any) sit beside it as
  `framing.<name>.md`.
- **The probe machinery lands inside the workflow, compressed**, not
  as a separate reference: it is method core every census needs, not
  imitated optional material — references are for the latter
  (ADR-0008's spirit).
- **The derivation-order commit sequence is the default practice**,
  not optional ceremony — the user adopted it; a run that skips it
  is off-default and logs why.
- **Two finds parked, not landed**: the two-tier harvest idea
  (sure adoptions vs held insights) touches ADR-0007, this repo's
  own discipline — a meta change deserving its own decision; the
  define phase (project naming with verdicts) is cbc-bootstrap
  territory. Both go to TODO Later, not into this change set.
- **Checkout's thinner shape is not marked wrong**: the skill
  describes the decided shape; checkout's run predates it and
  stands as lived history.
- Census work split across two commits (4, 5) by what they change:
  procedure vs exit obligations — each reverts coherently.
