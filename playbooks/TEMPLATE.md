# Playbook: <project type, e.g. "Backend service">

<!--
HOW TO USE THIS FILE
1. Keep this file in playbooks/<type>.md — it is the REUSABLE template.
2. New project: copy it to the project repo as PLAN.md, fill in specifics,
   delete steps that don't apply, add ones that do.
3. During the project: update statuses and notes in PLAN.md (not here).
4. After the project: run the Retrospective at the bottom of PLAN.md,
   then fold the lessons back INTO this playbook and bump its version.
-->

Playbook version: v1 (created YYYY-MM-DD)
Last updated from project: <project name, date>

## Legend

- `[ ]` planned   `[~]` in progress   `[x]` done   `[!]` blocked   `[-]` skipped (say why)
- **Gate** = exit criteria. A step is not done until every gate item is true.
- Detail only the next 1–2 steps finely (rolling wave); keep later steps coarse.

---

## Step 0: Framing

Status: [ ]
Goal: know what we're building and why, before touching code.
Gate:
- One-paragraph problem statement written and agreed.
- Success criteria defined (how we'll know it worked).
- Out-of-scope list written (what we are deliberately NOT doing).
- Rough full-plan sketch below reviewed once end-to-end.
Records: create README.md stub, decisions folder (docs/adr/), this PLAN.md.
Warnings from past runs:
- <e.g. "Skipping the out-of-scope list led to scope creep in project X.">

## Step 1: Skeleton & CI

Status: [ ]
Goal: an empty but deployable, testable project.
Gate:
- Repo builds from a clean clone with one documented command.
- One trivial test exists and passes in CI.
- Lint/format checks run in CI.
- (If applicable) deploys to a staging environment.
Records: README run instructions; ADR if toolchain choice was non-obvious.
Warnings from past runs:
- <e.g. "Set up CI caching now; retrofitting it mid-project wasted a day.">

## Step 2: Data model / core domain

Status: [ ]
Goal: the central entities exist and are trustworthy.
Gate:
- Schema/migrations run cleanly up AND down on a fresh database.
- Core entities have create/read/update paths with tests.
- Invariants written down (what must never happen to this data).
Records: ADR for storage choice; note invariants in ARCHITECTURE.md.
Warnings from past runs:
- <...>

## Step 3: <next major capability, e.g. Auth>

Status: [ ]
Goal: <one sentence>.
Gate:
- <criterion>
- <criterion>
- Tests cover the failure paths, not just the happy path.
Records: <ADRs expected here, if any>.
Warnings from past runs:
- <...>

## Step 4: <coarse placeholder — detail after Step 2/3>

Status: [ ]
Goal: <one line>.
Gate: TBD — depends on <decision that unlocks it>.

## Step N: Release & handoff

Status: [ ]
Gate:
- CHANGELOG entry written for the release.
- README verified by someone (or a clean machine) other than the author.
- Known issues filed, not just remembered.
- Monitoring/alerts in place (if a running service).
Warnings from past runs:
- <...>

---

## Discovered along the way

<!-- Things found mid-step that don't block the current gate.
     Triage each: assign to a future step, file as issue, or drop. -->
- <YYYY-MM-DD> <finding> → <where it went>

## Decision index

<!-- One line per ADR so the plan stays the map. -->
- ADR-0001: <title> (Step 1)
- ADR-0002: <title> (Step 2)

---

## Retrospective  (fill at project end — this feeds the playbook)

Ran: <start date> → <end date>

For each step, answer briefly:
1. **Estimate vs reality** — which steps took much longer/shorter, and why?
2. **Wrong order?** — did anything need to happen earlier? (e.g. "rate
   limiting belonged in Step 3, not Step 5")
3. **Dead ends** — approaches tried and abandoned; write each as a warning
   so the next run doesn't repeat it.
4. **Missing steps** — work that had no home in the plan; add it as a step
   or gate item in the playbook.
5. **Useless gates** — criteria that added ceremony without catching
   anything; remove or loosen them.

Then: copy the surviving lessons into playbooks/<type>.md as new
"Warnings from past runs" lines or changed gates, bump the playbook
version, and note this project under "Last updated from project".
