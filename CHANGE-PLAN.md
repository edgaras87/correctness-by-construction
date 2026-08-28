# Change-plan: practice executions land (PLAN Step 4)

Revised at the commit-3 boundary. The original plan imported the
archive's skill+agent packaging as-is; review questioned the whole
form, weighed guides + plan-step pointers, and settled on **skills
without agents**: the phases stay skills (uniform delivery with
framing/slice; re-entry auto-fires on "we need Redis now" moments
no plan step waits for — agent model P1/P2), while the agent seat
layer — never lived, mostly restating the skill bodies — stays
behind.

## Summary — the state after all commits

The executions layer is complete, one mechanism throughout:
cbc-framing, cbc-slice (Step 3), and now infra-establish (SKILL.md
+ three references), infra-serve, and cbc-bootstrap (SKILL.md + two
references) — all skills under `executions/`, pinned per ADR-0005.
The agent definitions stay behind (ADR-0006), their one unique
piece — the record-path defaults — absorbed into the infra-establish
skill as a recorded change. The bundle doc covers the whole set,
copy-all-at-birth. The STATUS/LAYOUT open/owed items live on in
TODO.md. Step 4 closed, Step 5 detailed. The whole pipeline —
framing → establish → bootstrap → slice — is born from this repo.

## Commits

**1. `docs(agent): add change-plan for practice executions`** — done.

**2. `docs(adr): pin practice-born executions as checked`** — done
(ADR-0005; unaffected by the revision).

**3. `docs(agent): revise change-plan — skills minus agents`**
This revision, on its own commit; body records what forced it.

**4. `docs(adr): keep practice executions as skills, drop agents`**
ADR-0006. Decides: skill form kept — uniform delivery (one
mechanism for every execution a run installs), and re-entry
(infra-serve) auto-fires at unplanned moments no plan step covers;
the agent seat layer left behind — never lived (the archive's own
STATUS owes it a first run), ~80% restated from the skill bodies.
Rejected: guides + plan-step pointers (right for the planned
phases, but re-entry would depend on human memory — P1); the
packaging as-is (untested seat layer); import-then-reshape (churn).

**5. `docs(executions): import practice executions as skills`**
Eight files. `executions/infra-establish/` — SKILL.md (moved fix
recorded: the archive keeps it at `skills/SKILL.md`, against its
own STATUS diagram and unregisterable as a named skill; plus one
addition, the record-path defaults absorbed from the groundskeeper
agent file, named in the header) and `references/`
(establishment-walk.md, postgres-role-split.md,
postgres-setup-walkthrough.md — verbatim, moved note).
`executions/infra-serve/SKILL.md` — verbatim.
`executions/cbc-bootstrap/` — SKILL.md + references/
(spring-boot-walkthrough.md, spring-pom-convention.md) — verbatim.
Pin lines per ADR-0005; headers below frontmatter as in Step 3.

**6. `docs(executions): extend bundle doc to practice set`**
executions/README.md: the birth table gains the three skills
(each → run's `.claude/skills/`). Records copy-all-at-birth and
why it is safe (every practice skill's Stage 0 gate refuses to run
before its phase), plus the working advice: the run's PLAN authors
an infra step and a bootstrap step that invoke the skills; only
re-entry arrives unplanned, and the trigger covers it.

**7. `docs: triage practice packages' open items to TODO`**
The left-behind STATUS/LAYOUT docs' living content lands in TODO
Later with provenance: first lived use owed (corrections expected),
the second-service-family walkthrough test, trigger descriptions
unoptimized (still live — the skills keep their triggers). Install
layout is superseded by the bundle doc; translation history stays
in the archive, reachable via the headers.

**8. `docs: update architecture for practice executions`**
Forward note removed; the executions component stays one-form
(skills), noting the agents were left behind (ADR-0006); codemap
stays accurate.

**9. `docs: close Step 4 in PLAN, detail Step 5`**
Gates checked with facts; Step 5 detailed per rolling wave;
Decision index gains ADR-0006; TODO's Step 4 line triaged out.

**10. `docs(agent): close change-plan for practice executions`**
Deletes this file; body is the retrospective — including the
two-stage revision (guides weighed, skills minus agents chosen)
and the original plan's ten-vs-"twelve" counting slip.

## Decisions taken inside this plan

- **Skills, no agents** (ADR-0006) — the revision's core. One
  mechanism for everything a run installs; re-entry protected by
  its trigger; the untested seat layer stays behind.
- **Record-path defaults absorbed** into the infra-establish skill
  from the groundskeeper file — the agents' only content the skills
  lack; an addition recorded in the header, never silent.
- **infra-serve stays its own skill** — its trigger is its value:
  it fires on the unplanned utterances ("add a queue", "bump the
  version") that make re-entry the moment the method is most
  needed and least remembered.
- **Pin phrasing: "checked against"** (ADR-0005, landed).
- **STATUS/LAYOUT stay behind**; open/owed items to TODO, layout
  superseded, history archived.
- **Copy-all-at-birth** for the bundle: one delivery moment; Stage
  0 gates make early copy safe.
