# Glossary: the stack's Names

<!-- The Names the Spring and PostgreSQL stack's Agent Skills are
     written in, each from this project's side: one plain sentence,
     with its owner where it has one. A pinned copy, like every
     delivered file: changed only as .claude/rules/delivered-copies.md
     says; a project on another stack holds that stack's file instead.
     This project's own Names are docs/glossary.md's.
     foundation: the writing convention -->

- **CBC Bootstrap** — the work between CBC Framing and the first
  Invariant Slice: the stack chosen, an empty running application on
  the Runtime Ground, and the Adversity Harness proven on one
  Adversity Class; it ends when its exit test passes
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **CBC Bootstrap Requirements** — `bootstrap-requirements.md`, the
  cbc-bootstrap Agent Skill's Stage 2 contract: the Build Coordinates, the
  capabilities, the constraints, the Runtime Ground's facts, the
  evidence owed and the CBC Bootstrap Exclusions
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **CBC Bootstrap Adversity Class** — the one Adversity Class the
  Adversity Harness is proven on at the CBC Bootstrap, read from the
  CBC Framing Exports' own words
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **CBC Bootstrap Probe** — the scaffolding endpoint and test that
  prove the Adversity Harness creates the CBC Bootstrap Adversity
  Class; both go at the first Invariant Slice
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **CBC Bootstrap Step Plan** — the cbc-bootstrap Agent Skill's Stage 3 plan: five
  steps in order, each one change with its check and its commit
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **CBC Bootstrap Exclusion** — something the CBC Bootstrap does not
  build, written with its reason
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **Build Coordinates** — the Maven project's group, artifact, base
  package, packaging and language version
  (`.claude/skills/cbc-bootstrap/SKILL.md`).
- **Migration Path Test** — the test that proves the migration path
  runs, and that it applied none at the CBC Bootstrap
  (`.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`).
- **Execution Environment** — the local runtime host for
  infrastructure
  (`.claude/skills/infra-establish/references/establishment-walk.md`).
- **Infrastructure Service** — a capability provided to the system,
  such as its database
  (`.claude/skills/infra-establish/references/establishment-walk.md`).
- **Infrastructure Service Constraint** — a requirement or limit put
  on an Infrastructure Service, each naming what enforces it
  (`.claude/skills/infra-establish/references/establishment-walk.md`).
- **Infrastructure Service Exclusion** — an Infrastructure Service not
  provided, written with its reason
  (`.claude/skills/infra-establish/SKILL.md`).
- **Infrastructure Service Re-entry** — an Infrastructure Service
  added, changed or removed on an established Runtime Ground, by the
  same evaluation from need, logged as one decision
  (`.claude/skills/infra-serve/SKILL.md`).
- **Infrastructure Establishment** — the infra-establish Agent Skill's
  work, Stage 0 to Stage 7: the Runtime Ground stood up and verified
  (`.claude/skills/infra-establish/SKILL.md`).
- **Infrastructure Establishment Log** —
  `docs/infrastructure/establishment-log.md`, kept only by a
  repository without records; one with records writes ADRs
  (`.claude/skills/infra-establish/SKILL.md`).
- **Database Role Split** — database authority enforced by grants: the
  `migrator` role owns structure, the `runtime` role writes data
  (`.claude/skills/infra-establish/references/postgres-role-split.md`).
- **Database Setup Identity** — the admin login that runs the database
  setup once and owns the database; never wired into the application
  (`.claude/skills/infra-establish/references/postgres-role-split.md`).
- **Catalog Check** — the real database state queried against what the
  model claims, each query with its expected result beside it
  (`.claude/skills/infra-establish/SKILL.md`).
- **Behavioral Check** — an Infrastructure Service Constraint
  attempted live and seen refused; with the Catalog Check, the
  infra-establish Agent Skill's Stage 5 gate
  (`.claude/skills/infra-establish/SKILL.md`).
- **Infrastructure Contract** — the manual for whoever builds on the
  Runtime Ground: its identities, how it is reached, what it refuses,
  and how schema changes are made
  (`.claude/skills/infra-establish/SKILL.md`).
- **Operator Manual** — the human's manual for standing up and using
  the Runtime Ground, written from the setup as it was done
  (`.claude/skills/infra-establish/SKILL.md`).
- **Stack Default** — the choice a stack's references make unless a
  demand or a fact about the environment defeats it: local containers
  under podman, run by compose; packages by feature
  (`.claude/skills/infra-establish/SKILL.md`).
