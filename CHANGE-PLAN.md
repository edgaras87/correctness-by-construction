# Change-plan: adopt the spring harness reference

## Summary — the state after all commits

cbc-bootstrap's references gain `spring-harness-reference.md`: the
evidence harness's recurring artifacts as code — the two test bases,
the migration-path test, and the probe pair — adapted from the
workbench-era doc the user handed over (`temp/`, uncommitted) and
confirmed against the third lived pass, checkout-system's bootstrap,
read read-only. The walkthrough's stages 4–5 point at it; the TODO
Later item parked on the second-run trigger is resolved. The handed
pom-convention doc is discarded as superseded (our Step 4 import is
its cleaned descendant); `temp/` is deleted, never committed.

## Commits

**1. `docs(executions): import spring harness reference`**
The adapted, confirmed doc lands beside the walkthrough. Old
maintenance language stripped; cross-references renamed to this
skill's files; identities generalized to the walkthroughs' notation;
provenance header lists the third pass's corrections.

**2. `docs(executions): point walkthrough at harness ref`**
Stages 4–5 gain pointer lines; the walkthrough's header records the
re-derivation. Separate from commit 1 so the reference's arrival and
the walkthrough's routing each revert whole.

**3. `docs: resolve test-support item in TODO`**
The Later item parked on "a second run re-derives the same shape" is
deleted — the trigger fired and the adoption is its resolution.

## Decisions taken inside this plan

- **Reference, not template** (ADR-0008 rule 4): the artifacts vary
  at named points per run — imitated code with one master, never
  copy-and-fill. The user's instinct ("reusable pattern in the
  bootstrap skill") lands on the references side of the boundary.
- **The trigger is judged fired.** ADR-0008 keeps code out "until a
  second run re-derives the same shape": the handed doc proves two
  pre-repo passes, and checkout-system re-derived the shape a third
  time. Adoption applies the rule; no ADR changes.
- **The third pass wins where passes disagree.** The authority-split
  miniature (ground's own bootstrap.sql in the container; migrate as
  migrator; context as runtime, identity asserted), the two-base
  layering, the identity-asserting probe, the count-sized pool. The
  old doc's virtual-threads claim and its `failOnMissingLocations`
  guard demote to variation points, each honestly attributed.
- **MigrationPathIT joins the set** at its bootstrap-time shape
  (zero applied) — the walkthrough's stage-4 outcome the old doc
  lacked; its slice-era evolution is noted, slice-era base growth
  (clock config) excluded — this is the bootstrap shape only.
- **No ARCHITECTURE change**: a new file inside an existing
  `references/` directory changes no shape — same call as Step 6's
  templates.
- **The pom-convention doc takes nothing with it.** Diffed section
  by section against our copy; the one absent nugget (the handoff
  names capabilities, never dependencies) already lives split across
  our copy's scope line and the walkthrough's requirements-win rule.
