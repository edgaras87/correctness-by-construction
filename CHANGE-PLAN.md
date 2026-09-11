# Change-plan: harvest run 3's ground into infra-establish and cbc-framing

## Summary — the state after all commits

Six findings from run 3's Step 3 (read 2026-09-11, TODO Now) land in
the bundle masters, in the run's own wording, one dated harvest line
per file touched (CBC ADR-0007), the pins untouched — runs re-pin on
their own act. After the set: infra-establish's records section
states the record-keeping-repo shape as the default (no
establishment log; decisions as ADRs, the walk as lived in the
devlog, expected results in the verify suite and the operator
manual; compose.yaml and the env files at the root, the runnable
ground under `infrastructure/`, the manuals under `docs/`) and
says where the mapping note goes; infra-serve reads the ground's
record wherever the repo keeps it; Stage 0's check 2 names the
return trip instead of "stop"; cbc-framing's census asks for the
runtime ground at framing, so the return trip stops being needed;
the PostgreSQL walkthrough carries the two lived traps; the verify
template checks the CONNECT revoke; the templates say which naming
case they ship. Nothing in `concept/` moves: no CHANGELOG entry, no
concept version.

## Commits

**1. `docs(agent): add change-plan for the run 3 ground harvest`**
This plan.

**2. `docs(starter): infra-establish records the log-less shape`**
SKILL.md's Records-and-outputs section rewritten around the shape
both lived runs used: the layout, and — for a repo with records —
no establishment log, the decisions as ADRs, the walk as lived in
the devlog with its expected-and-actual tables, expected results in
the verify suite and the operator manual, the mapping note in the
environment ADR. The log stays as the shape for a repo without
records. The lived-result discipline's "record it in the
establishment log" becomes "in the ground's record — the log, or
the repo's work record"; the verify template's header phrase the
same; infra-serve's Stage 0 and step 2 read the ground's record
wherever the repo keeps it. Harvest lines in infra-establish
SKILL.md, the verify template, infra-serve SKILL.md.

**3. `docs(starter): Stage 0 names the return trip`**
SKILL.md check 2 and the walk's Inputs paragraph: a definition with
no runtime-ground facts is not "framing unfinished — stop" but the
downstream trigger the definition's own revision rule names — a
dated revision entry in L1, one commit, lived twice (checkout-system
d25ff48, run 3 44f256d). The stop stays for checks 1 and 3. Harvest
lines in SKILL.md (second, same set) and establishment-walk.md.

**4. `docs(starter): cbc-framing's census asks for the runtime ground`**
The workflow's step 2 gains a short labeled block beside the trust
list — "The runtime ground" — what the system assumes about where it
runs: the machine, a stranger's clean machine, plural instances, the
store as a service outliving them, the clock; in run 3's words, with
its why (the ground is derived from need, not habit). The mismatch
between two skills of this bundle closes here. Harvest line in
cbc-framing-workflow.md.

**5. `docs(starter): the walkthrough carries two lived traps`**
postgres-setup-walkthrough step 6: the image runs the bootstrap
against a temporary server and restarts, so the health check can
report healthy in that window and the first query fails with "the
database system is shutting down" — `pg_isready` plus one real
query is the honest up. Step 9: a host without a `psql` client
reads from outside through a client container on the host network,
the command as run 3 ran it. Harvest line.

**6. `docs(starter): the verify suite checks the CONNECT revoke`**
Template query 6 — `has_database_privilege` for both roles and
PUBLIC as `0::oid`, expected t, t, f — because the bootstrap's
REVOKE is a claim the suite never checked. The walkthrough's step
7 gains the behavioral half: a probe role created, refused, dropped.
Harvest lines in the template (second, same set) and the
walkthrough (second, same set).

**7. `docs(starter): the templates name the naming case they ship`**
A comment at the bootstrap template's role names: prefixed roles
are the shared-cluster case the role-split reference describes; a
dedicated cluster takes bare names, and the verify template's LIKE
filter then becomes an explicit IN list — the trade the verify
header once named. Harvest lines in bootstrap.sql and the verify
template (third, same set).

**8. `docs: records for the run 3 ground harvest`**
TODO's harvest item DONE, with what each fix became; devlog entry
and resume line. No ADR: every change is a harvest under CBC
ADR-0007's flow, the skill's rule text moving to what two runs
lived.

**9. `docs(agent): close change-plan for the run 3 ground harvest`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The records shape is a harvest, not a new decision.** The
  skill's defaults came from the archive and were lived by neither
  run as written; the default moves to what both runs did, the log
  kept for the case it was written for. If the user reads it as a
  decision of this repo, an ADR joins commit 8.
- **infra-serve is in scope.** Its Stage 0 requires the log to
  exist; left alone, the log-less shape would fail every re-entry.
- **The verify template takes three harvest lines from one set**,
  one per change, rather than one line naming three — ADR-0007's
  line is per change, and the three revert independently.
- **cbc-framing's block sits in the workflow, not the plain page.**
  The plain page maps the layers; the workflow's step 2 is where
  the census is run and where the trust list already sits beside
  the facts.
- **Wording is the run's.** Each fix quotes or closely follows run
  3's manual, ADRs and devlog; nothing is re-derived from the
  finding alone.
