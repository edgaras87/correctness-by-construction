# Change-plan: first harvest (PLAN Step 5)

## Summary — the state after all commits

The harvest loop has run end-to-end once, on a real item: the Boot
4.1 TestRestTemplate trap, lived during checkout-system's bootstrap
and recorded in that run's decision log, now lives in this repo's
authoritative `spring-boot-walkthrough.md` — the same two-hunk
change the run's own copy carries, with run provenance in the
header. ADR-0007 records the harvest discipline the lived case
produced: how execution changes arrive, where they are logged, and
that an execution-only harvest bumps no concept version. The bundle
doc carries the operative harvest rule where a harvester looks.
Step 5 is closed; the plan's last open step is Release.

## Commits

**1. `docs(agent): add change-plan for first harvest`**
The approved plan, committed before work.

**2. `docs(adr): adopt harvest discipline for executions`**
ADR-0007, decision before the harvest it governs. The flow the
lived case produced: the run's record is read, never edited; the
authoritative execution copy is updated to match what was lived;
the change is logged as a dated harvest line in that execution's
own provenance header (which travels with every future copy); the
pin is untouched and no concept version bumps when the mental
layer is untouched; CHANGELOG stays the pure concept-version log;
the archive copy stays a snapshot, visibly stale. Placement:
local rule in the bundle doc, not a handbook convention — one
concept repo, one lived harvest; the garden rule's logic applies
(machinery at the second instance, not the first). Rejected:
CHANGELOG entries for execution-only changes (muddies ADR-0003's
log with entries no version will ever carry); a separate
execution changelog (a second log for what headers + git history
already record); authoring a convention now (ahead of need).

**3. `docs(executions): harvest Boot 4.1 trap from checkout-system`**
The two-hunk change applied to
`executions/cbc-bootstrap/references/spring-boot-walkthrough.md`,
matching the run's lived wording: stage 4's exact-traps list gains
the RANDOM_PORT / @AutoConfigureTestRestTemplate trap (lived on
Boot 4.1.1), and the recall list gains its compressed line. The
header gains the harvest line: date, what, from which run record.
"Changes on import: none" stays true — it describes import time.

**4. `docs(executions): add harvest section to bundle doc`**
executions/README.md gains a short Harvest section — the operative
rule at the place a harvester looks (P2): where improvements come
from (a run's records, read-only), where they land (the
authoritative copy + a header line), what never happens (editing
the run, editing the archive, bumping the concept for an
execution-only change). Points at ADR-0007 for the why.

**5. `docs: close Step 5 in PLAN, author Step 6`**
Gates checked with facts, including the archive-staleness confirm
(snapshot, no action). A new Step 6 — Templates extracted from the
lived run — is authored between harvest and Release (rolling wave:
checkout-system's lived ground files put the extraction past the
don't-author-speculatively bar, and the just-decided ADR-0007
gives it its discipline). Its gate: sources read read-only from
checkout-system; templates (compose, bootstrap SQL, verify suite,
env and testcontainers files — not the pom) landed as the master
copies with pin+provenance headers; the walkthrough re-derived to
keep the whys and point at them (one master, no drifting twins);
own change-plan. TODO's templates item moves from Later into Next
assigned to Step 6; TODO's Step 5 line triaged out. Step N
(Release) note records that the success criterion "harvest loop
run once end-to-end" is now met. Decision index gains ADR-0007.

**6. `docs(agent): close change-plan for first harvest`**
Deletes this file; body is the retrospective.

## Decisions taken inside this plan

- **The execution's header is its change log.** A dated harvest
  line per change, riding the file into every future copy
  (self-containment, S1); "what changed since my run was born" is
  answerable from the header and git history. No second log.
- **No concept bump for execution-only harvests.** ADR-0003's
  versions name states of the mental layer; this harvest never
  touched `concept/`. The pin stays "checked against concept v1".
- **Harvest discipline is a local rule, not a convention** — the
  garden rule's logic: the handbook gets it when a second concept
  repo writes it twice. Queued nowhere yet; the retrospective's
  promotion pass will see ADR-0007.
- **The harvested wording is the run's wording.** The run lived
  it and phrased it; the authoritative copy takes the lived text
  rather than re-deriving prose from the decision entry — the same
  fidelity rule as every import (M1).
- **Templates get their own step, after this one.** checkout-system
  makes the extraction lived, not speculative, so it graduates from
  Later — but it is a change set of its own (the walkthrough
  re-derivation is the load-bearing half) and it wants ADR-0007
  decided first. Step 6, authored at this plan's commit 5.
