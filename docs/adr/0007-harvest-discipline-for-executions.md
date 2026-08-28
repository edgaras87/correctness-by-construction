# 0007. Harvest discipline for executions

Date: 2026-08-28
Status: Accepted

## Context

The repo's whole loop closes here: a run's surprise must be able to
land in an authoritative execution without breaking any standing
rule. The first lived case is exact — checkout-system hit a Boot
4.1 trap during bootstrap, recorded it in its own decision log
(2026-08-27), and updated its local walkthrough copy. Three
questions need answers before the change arrives: how a change
made *here after import* is recorded (every header currently says
"changes on import: none"), where execution-level changes are
logged given CHANGELOG is the concept-version log (ADR-0003), and
whether this discipline is a local rule or a convention (deferred
from Step 0 to the lived case).

## Options considered

For the log: 1. CHANGELOG entries for execution-only changes —
muddies ADR-0003's log with entries no concept version will ever
carry. 2. A separate execution changelog — a second log for what
git history and the file itself can already record. 3. The
execution's own provenance header carries a dated harvest line per
change — chosen; the record travels with every future copy
(self-containment, S1).

For the placement: a handbook convention now — rejected by the
garden rule's own logic: one concept repo, one lived harvest;
machinery arrives at the second instance. A local rule in the
bundle doc, promoted if a second concept repo re-derives it.

## Decision

The harvest flow, as the lived case shaped it:

1. The run's records are the source, read-only — nothing here ever
   edits a run repo (tiers model: learning moves up only through
   records).
2. The authoritative execution copy is updated to match what was
   lived, in the run's own wording — re-deriving prose from the
   decision entry would lose parts (M1).
3. The execution's header gains one dated harvest line: what
   changed, from which run and record entry. The header is the
   execution's change log; "changes on import" keeps describing
   import time and stays true.
4. The pin is untouched and no concept version bumps unless the
   mental layer itself changed — ADR-0003's versions name states
   of `concept/`, and an execution-only harvest never touches it.
5. CHANGELOG records nothing for execution-only changes; when a
   harvest does change the concept, its version entry names the
   re-derived executions as ADR-0003 already provides.
6. The archive copy stays a historical snapshot — visibly stale is
   its job.

The operative rule lives in the bundle doc's Harvest section, where
a harvester looks (P2); this ADR keeps the why and the rejected
options.

## Consequences

Good: the loop closes with zero new machinery — header lines, git
history, and one README section; every future copy of an execution
carries its own change history; the concept-version log stays
believable.
Bad: "what changed across all executions since date X" takes a git
log over `executions/`, not one document — accepted; that question
belongs to git, and a document answering it would be a third copy
of the truth.
