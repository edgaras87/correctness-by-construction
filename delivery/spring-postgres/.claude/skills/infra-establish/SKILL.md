---
name: infra-establish
description: Run the Infrastructure Establishment of a framed backend project, its Runtime Ground. Decide the Execution Environment against the Stack Default (podman local containers, compose-driven). Choose the Infrastructure Services strictly from the adversity needs of the Invariant Slice Registry, and state each Infrastructure Service Exclusion with its why. Name each Infrastructure Service Constraint with database-level enforcement. Stand the services up, verify both ways (a Catalog Check and a Behavioral Check), and write the two manuals: the Infrastructure Contract for the builder, the Operator Manual for the operator. Use whenever a framed project needs its infrastructure stood up: containers, PostgreSQL, compose files, Flyway or migrations tooling, "set up the database", "stand up the ground", "infrastructure establishment", even if the user just says "the framing is done, let's get it running". It requires the completed CBC Framing Exports (the CBC Framing Intent, the System Definition and the Invariant Slice Registry). Stage 0 checks them, and refuses to go on without them. Do NOT use for CBC Framing (the cbc-framing Agent Skill), for implementing Invariant Slices (the cbc-slice Agent Skill), or for adding a service to an already-established Runtime Ground (the infra-serve Agent Skill).
foundation: practice, checked against concept v1
---

# Infrastructure Establishment — from no infrastructure to a governed, verified Runtime Ground

Take one framed project to its Runtime Ground:

1. the Execution Environment chosen and running;
2. the Infrastructure Services the problem's reasoning requires,
   stood up;
3. each constrained to need;
4. each verified both ways;
5. the manuals that make the Runtime Ground usable and reproducible.

The exit is Infrastructure Establishment's Stage 7: **the Runtime Ground runs,
constrained to need, and both manuals stand.**

The full procedure is
`.claude/skills/infra-establish/references/establishment-walk.md`.
Read it before Stage 1. When PostgreSQL is the decided datastore, two
more references apply at their Agent Skill Stages:

- `.claude/skills/infra-establish/references/postgres-role-split.md`,
  the Database Role Split, which makes the Infrastructure Service Constraint real;
- `.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`,
  the sequence end to end, as two CBC Runs confirmed it.

## Stage 0 — readiness (before anything else)

The service decision lives in *this* work, but the **need** is handed
in. Check against the actual repo:

1. **The CBC Framing Exports exist and are settled:**
   - the CBC Framing Intent;
   - the System Definition: its environment facts are binding;
   - the Invariant Slice Registry: its Invariant Slices' adversity
     requirements are the deciding constraints.

   With the cbc-framing Agent Skill, these live under `docs/system/`:
   `intent.md`, `definition.md`, `registry.md`.
2. **The environment facts are readable.** The System Definition
   states what Runtime Ground the system assumes: the lines of "The
   Runtime Ground" in
   `.claude/skills/cbc-framing/references/cbc-framing-workflow.md`.

   If the System Definition has no Runtime Ground facts, this is not
   "stop". It is the later trigger the System Definition's own
   revision rule names. The facts are added by a CBC Framing Export Revision
   in LAYER-1-ENVIRONMENT: what changed, why, and that this check set
   it off. It is one commit, and touches no System Possession, System
   Refusal or verdict. Then the check passes. Two CBC Runs met this,
   the same way both times. A fact CBC Framing left unstated is
   written where it belongs.
3. **The repo exists, and is a git repo** with its hygiene files
   present or creatable: `.gitignore` at least, since secrets
   handling depends on it.

**Check 1 or 3 fails: stop.** Report exactly what is missing. CBC
Framing work is never done here. An Infrastructure Establishment
started on a project not framed provisions from habit, and habit is
exactly what the method exists to refuse.

## The Agent Skill Stages and their Gates

In the drawing, environment is the Execution Environment, services the
Infrastructure Services, constraints the Infrastructure Service
Constraints, and contract the Infrastructure Contract and the Operator
Manual.

```
0: ready? → 1: environment → 2: services   → 3: constraints → 4: the reference
                (decided,       (from need,     (named, with     (applied or
                 stood up)       exclusions)     enforcement)     recorded)
          → 5: stand up + verify BOTH ways → 6: contract → 7: exit test
```

The full detail of each Agent Skill Stage:
`.claude/skills/infra-establish/references/establishment-walk.md`.
What cannot be bargained away:

- **Stage 1 Gate:** the Execution Environment decision is logged with
  its why *before* any file of the Runtime Ground exists. **No compose
  file is created at Stage 1:** its content is the outcome of Stages
  2 to 5. The adversities' demands choose the Execution Environment.
  **What the evidence must be able to do to the Runtime Ground is
  proven by the Adversity Harness that does it,** not here. The
  Operator Manual's environment section is written from the stand-up
  as it is done.
- **Stage 2 Gate:** one logged evaluation, Invariant Slice by
  Invariant Slice: what capability does each invariant's evidence
  actually require? The set of Infrastructure Services is what
  survives that question. **Each Infrastructure Service Exclusion is
  stated with its why:** a cache refused, a queue refused, and for
  what reason. No list of Infrastructure Service Exclusions, no Stage 2.
- **Stage 3 Gate:** every Infrastructure Service Constraint names its
  **enforcement mechanism:** the database's own grant system, a
  config, a Structural Wall. Never convention, code review, or trust.
  An Infrastructure Service Constraint without enforcement is a wish.
- **Stage 5 Gate:** verification runs **both ways, always:**
  - the **Catalog Check:** real state queried against the Database Role Split's
    claims, the expected result stated beside each query;
  - the **Behavioral Check:** the Infrastructure Service Constraint
    attempted, and watched being refused, live.

  A Runtime Ground verified one way is not verified.
- **Stage 6 Gate:** both manuals stand:
  - the **Infrastructure Contract**, for the builder: identities,
    reachability, refusals, how schema changes are made;
  - the **Operator Manual**, for standing up and use, written from
    the work as done.

  No manuals, no exit.

## The rule for results (every Agent Skill Stage that runs commands)

1. State the command, and its expected result.
2. Run it.
3. Read the actual output.
4. The outcome is what actually happened.

Record it in the Runtime Ground's record (*Records and outputs*,
below). Destructive acts, such as dropping volumes or resets, need
the reviewer's explicit yes. Installs on the host are the reviewer's
own acts.

## Deviations — legal, never silent

A different Runtime Ground, with no containers, several services, or
another family of constraints, may force departures from `establishment-walk.md` or
the references. Depart when the Runtime Ground demands it. Log where,
what was done instead, and why. The references are written from what
CBC Runs did, not rules. But a deviation not logged makes the record
wrong.

## Records and outputs

The repo's own records win. Where the Runtime Ground's record
lives depends on what the repo keeps. Two CBC Runs worked it, and the
shape below is theirs.

- **A repo with records** (a plan, ADRs, a devlog: every
  CBC Run): **no Infrastructure Establishment Log.**
  - Decisions are ADRs:
    1. the Execution Environment;
    2. the set of Infrastructure Services, with the Infrastructure
       Service Exclusions;
    3. the Infrastructure Service Constraints, each with its
       enforcement.
  - The Infrastructure Establishment as done is the devlog's entry for the Plan Step, growing
    as it runs. For each Agent Skill Stage that runs commands,
    it holds the command, what was expected, and what actually
    happened.
  - The expected results sit in `infrastructure/postgres/verify-database-model.sql` and the Operator
    Manual.
  - The Execution Environment ADR maps this Agent Skill's default
    records to the repo's own: the sentence the Infrastructure Establishment Log's first entry
    would have held. One CBC Run kept an Infrastructure Establishment Log beside such records, and
    it held nothing they did not.
- **A repo without records:** the Infrastructure Establishment Log,
  `docs/infrastructure/establishment-log.md`, beside the manuals. It
  is the decision record and the Infrastructure Establishment's outputs as done. Its first
  entry maps this Agent Skill's defaults to whatever the repo does
  keep. Prose about the Runtime Ground lives with the manuals.
  `infrastructure/` holds only what runs.

The layout, in both cases:

- `compose.yaml` and `.env.example` at the root, `.env` ignored: the
  first command of someone new to the repo finds them there.
- `infrastructure/`: the rest of the runnable Runtime Ground
  (`bootstrap.sql`, `verify-database-model.sql`, the migration tool's config),
  landed as the Infrastructure Establishment produces them.
- The two manuals, under the repo's docs directory
  (`docs/infrastructure/`), beside what else is written about the
  system:
  - `infrastructure-contract.md`, the Infrastructure Contract: the
    **living** manual for the builder. It has one section per
    Infrastructure Service, saying:
    - which identity to connect as, and which never to use;
    - reachability inside and outside the Execution Environment's
      network;
    - what the Infrastructure Service Constraints refuse;
    - how schema changes are made.

    It grows at every Infrastructure Service Re-entry, and is never
    rewritten from scratch.
  - `operator-manual.md`, the Operator Manual: everything the
    operator needs to stand the Runtime Ground up and use it,
    written **from the setup as it is done, at the time,** never
    reconstructed later.
- The README's `Prerequisites` section, derived from the Operator
  Manual at the exit, when the Runtime Ground stands. It carries the
  environment lines only, merged and filled from
  `.claude/skills/infra-establish/templates/readme-prerequisites.md`.
  The stack's line arrives at the CBC Bootstrap, not here. `establishment-walk.md`'s
  Stage 7 says how.
- Optional, only if the project keeps public docs: a setup guide,
  derived from the Operator Manual. It is never a second home, and is
  derived again when the manual changes.

---

## Decisions

- ADR-0008 — `references/postgres-setup-walkthrough.md`: the Runtime
  Ground's files are Agent Skill Templates beside the references
- ADR-0013 — *Records and outputs* and `references/establishment-walk.md`
  Stage 7: the README's Prerequisites section arrives when the Runtime
  Ground stands
