# Change-plan: practice executions land (PLAN Step 4)

## Summary — the state after all commits

The executions layer is complete: infra-establish (SKILL.md + three
references), infra-serve, cbc-bootstrap (SKILL.md + two references),
and the two agent definitions (groundskeeper, system-bootstrap) live
under `executions/`, pinned per ADR-0005 — practice-born executions
are *checked against* concept v1, not derived from it, and the
header says so honestly. The bundle doc covers the whole set (all
copied at birth; every practice execution's Stage 0 gate refuses to
run early, so early install is safe). The archive's STATUS/LAYOUT
companion docs stay behind; their open/owed items live on in
TODO.md. ARCHITECTURE's forward note is gone. Step 4 is closed and
Step 5 (first harvest) is detailed. The whole cbc pipeline —
framing → establish → bootstrap → slice — is now born from this
repo.

## Commits

**1. `docs(agent): add change-plan for practice executions`**
The approved plan, committed before work.

**2. `docs(adr): pin practice-born executions as checked`**
ADR-0005, decision before the import it governs. The pin question
Step 4's gate raised: these grew from lived runs, so "derives from
concept v1" would be a false claim. Decides the pin reads *checked
against* concept v1 — same versioning function (a concept bump
triggers re-review, ADR-0003), honest lineage. Rejected: claiming
derivation anyway (false provenance); leaving them unpinned (breaks
ARCHITECTURE's pinning invariant).

**3. `docs(executions): import practice executions`**
Twelve files: `executions/infra-establish/` (SKILL.md + references/
establishment-walk.md, postgres-role-split.md,
postgres-setup-walkthrough.md), `executions/infra-serve/SKILL.md`,
`executions/cbc-bootstrap/` (SKILL.md + references/
spring-boot-walkthrough.md, spring-pom-convention.md),
`executions/agents/` (groundskeeper.md, system-bootstrap.md). Same
header discipline; pin line per ADR-0005. One fix already found and
recorded in the affected headers: the archive keeps infra-establish
at `skills/SKILL.md` with references beside it — disagreeing with
its own STATUS.md layout diagram, and unregisterable as a named
skill — normalized here to `infra-establish/SKILL.md` +
`references/` (a pure move; relative reference paths still
resolve). Close read of the remaining files at import; any further
fix named in its header.

**4. `docs(executions): extend bundle doc to practice set`**
executions/README.md's birth table gains the three skills and the
agents (`executions/agents/*` → run's `.claude/agents/`). Records
the copy-all-at-birth decision and why it is safe: each practice
execution's Stage 0 gate refuses to run before its phase.

**5. `docs: triage practice packages' open items to TODO`**
The living content of the left-behind STATUS/LAYOUT docs — their
open/owed lists — lands in TODO Later with provenance: the
establish skill unexercised as an agent (corrections expected at
first run), the second-service-family walkthrough test, trigger
descriptions unoptimized. What stays behind is install layout
(superseded by the bundle doc) and translation history (the
archive keeps it; headers point there).

**6. `docs: update architecture for practice executions`**
The Step 4 forward note removed; the executions component notes the
agent definitions; codemap row stays accurate.

**7. `docs: close Step 4 in PLAN, detail Step 5`**
Gates checked with facts; Step 5 (first harvest) detailed per
rolling wave; Decision index gains ADR-0005; TODO's Step 4 line
triaged out.

**8. `docs(agent): close change-plan for practice executions`**
Deletes this file; body is the retrospective.

## Decisions taken inside this plan

- **The agent definitions are executions too.** The packages ship
  agents (groundskeeper drives infra-establish + infra-serve;
  system-bootstrap drives cbc-bootstrap); a run installs them under
  `.claude/agents/`. Home: `executions/agents/` — flat by kind,
  consistent with ADR-0004; groundskeeper serves two skills, so
  nesting it under either would be wrong.
- **Pin phrasing: "checked against", not "derives from"** —
  ADR-0005; the honest claim that still keeps the versioning
  machinery whole.
- **Layout fix on import, recorded not silent:** infra-establish
  normalized to the named-skill layout its own STATUS diagram
  claims. First import fix of the project — the
  fixes-recorded-never-absorbed provision finally fires.
- **STATUS/LAYOUT stay behind.** Three fates considered: import
  wholesale (their layout halves would immediately lie inside this
  tree); absorb into headers (too long); leave behind, triage the
  open/owed items to TODO, let provenance headers point at the
  archive for translation history — chosen.
- **Copy-all-at-birth** for the bundle: matches the lived
  checkout-system birth; the alternative (staged install per
  pipeline phase) adds a second delivery moment for no protection
  the Stage 0 gates don't already give.
