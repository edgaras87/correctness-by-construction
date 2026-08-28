# Change-plan: templates extracted from the lived run (PLAN Step 6)

## Summary — the state after all commits

The repeating ground and harness files exist in this repo as
copy-and-fill master templates, so no run re-derives them from prose.
`executions/infra-establish/templates/` holds five files extracted
from checkout-system's lived ground (compose.yaml, .env.example,
bootstrap.sql, verify-database-model.sql, flyway.conf), identities
generalized to the walkthrough's placeholder notation;
`executions/cbc-bootstrap/templates/` holds testcontainers.properties
and the application.yaml skeleton.
Each template carries a pin + provenance header in its own comment
syntax — checked against concept v1 (ADR-0005), extracted from the
run's lived files, changes on extraction listed honestly.

Both walkthroughs are re-derived: whys and traps kept, embedded file
bodies replaced by pointers to the templates — one master, no
drifting twins — with dated harvest lines recording the change
(ADR-0007). The postgres walkthrough also gains the run's lived
lesson that .env carries a fourth key (the runtime application
password). ADR-0008 records the template home; the bundle doc says
what a run does with templates at birth; ARCHITECTURE's executions
component and the archive invariant are current. Step 6 closed.

## Commits

**1. `docs(agent): add change-plan for Step 6 templates`**
This plan, committed after agreement, before the work.

**2. `docs: decide template home in skills (ADR-0008)`**
The decision before the placement it governs (the ADR-0004 pattern):
templates live in a `templates/` directory inside the skill that uses
them — not a shared `executions/templates/` — so a skill's copy stays
self-contained and the birth table needs no new row. Also records the
master/copy relation (a run copies and fills; fills never harvest
back unless the shape itself changed) and the boundary rule this step
enacts: content an agent imitates stays an example in references/,
content a run pastes becomes a template with one master.

**3. `docs(executions): add infra-establish templates`**
The five ground files land under
`executions/infra-establish/templates/`, bodies from checkout-system's
lived files, identities generalized (`<project>`, `<project_db>`,
`<project_schema>`, `<PROJECT>_DB_PASSWORD`), run-local references
(checkout's ADR numbers, skill paths) generalized to neutral wording.
Reverting this alone restores the current prose-only state — coherent.

**4. `docs(executions): re-derive postgres walkthrough`**
postgres-setup-walkthrough.md keeps every why and trap, replaces the
embedded compose/bootstrap-SQL/flyway.conf bodies and the verify-suite
section list with pointers to the templates, and takes the .env
fourth-key lesson from the lived run. Header gains dated harvest
lines for both changes (ADR-0007).

**5. `docs(executions): add cbc-bootstrap templates`**
Two files land under `executions/cbc-bootstrap/templates/`:
testcontainers.properties (with `<uid>` placeholder) and
application.yaml — the lived config's repeatable skeleton (app name,
runtime-identity datasource with its three commented absences,
health show-components), the run's business section removed and the
removal declared. spring-boot-walkthrough.md's stage 3 and stage 4
point at them instead of restating; harvest lines record both. One
commit — the skill gains its template layer and its walkthrough
points at it; the pieces revert together coherently.

**6. `docs: record templates in bundle doc, ARCHITECTURE`**
executions/README.md gains a short Templates paragraph (skills carry
their templates at birth; establishment copies-and-fills into the run,
the testcontainers file goes to $HOME per its own rule); ARCHITECTURE's
executions component notes templates as master copies. No codemap
change — templates get no top-level directory.

**7. `docs: mark archive as retired snapshot`**
One line on ARCHITECTURE's archive invariant: the archive repo is
retired, a frozen historical snapshot — agreed this session when the
deprecation was decided; lands at the step that touches ARCHITECTURE
anyway. Own commit so reverting the templates records never touches
the retirement fact.

**8. `docs: close Step 6 in PLAN`**
Gates checked as facts, the flyway.conf and application.yaml
additions reflected in the gate text, TODO's Next item cleared and a
Later item added: the test-support Java (DatabaseIT, WebDatabaseIT,
MigrationPathIT) earns templating only when a second run re-derives
it into the same shape — today it is code, and the walkthrough's
stance is outcomes, not code to copy.

**9. `docs(agent): close change-plan for Step 6`**
Deletes this file; body is the retrospective.

## Decisions taken inside this plan

- **flyway.conf and application.yaml join the template set** beyond
  the gate's five-file list. flyway.conf is an embedded body in the
  walkthrough today; leaving the smallest ground file as prose while
  templating its four siblings would contradict the step's goal.
  application.yaml is configuration, not code — the pom-exclusion
  logic does not apply — and its absence-comments are the recall
  layer stage 3 currently forces every run to reconstruct. The gate
  text is updated at close.
- **The test-support Java stays out.** Most re-derived artifact in a
  bootstrap, but application source — templating it would reverse
  the walkthrough's declared stance ("no code to copy") on the
  strength of one lived run, and couple this repo to a moving Boot
  version. TODO Later item with a second-run trigger instead.
- **The .env fourth key is a harvest**, not just an extraction detail:
  the lived .env.example carries the runtime application password,
  which the walkthrough's §2 (three keys) predates. Second run of the
  ADR-0007 machinery, riding commit 4.
- **The pom stays out**, per the gate: its convention refuses code
  ahead of earning.
- **Provenance now names a run repo** (checkout-system) instead of the
  archive — the first non-archive provenance in the repo. Honest and
  consistent: provenance is history, not authority; the master is
  here.
- **Placeholder notation is the walkthrough's own** (`<project>`
  family), not a new syntax — one convention across prose and
  templates.
