# 0008. Templates live inside their skill

Date: 2026-08-28
Status: Accepted

## Context

Step 6 extracts the repeating ground and harness files from
checkout-system's lived run — compose.yaml, .env.example, the
bootstrap SQL, the verification suite, flyway.conf, the
testcontainers properties, the application.yaml skeleton — so no run
re-derives them from walkthrough prose. Two questions need answers
before the first template lands: where templates live, and what
relation a run's filled copy has to the master here. The standing
decisions that bound the answer: executions are content under
`executions/` (ADR-0004), a run copies the whole bundle at birth,
and each skill's copy must work without reaching back to this repo.

## Options considered

For the home: 1. A shared `executions/templates/` directory — breaks
skill self-containment: the walkthrough pointers would cross the
skill boundary, a run copying `.claude/skills/infra-establish/`
would not get the files its own walkthrough points at, and the birth
table would need a new row with its own destination rule.
2. Stay in the walkthroughs as embedded bodies (status quo) — every
run's paste is a copy of prose with no single master; the lived
correction cycle showed those bodies drifting from the lived files.
3. A `templates/` directory inside the skill that uses them, beside
`references/` — chosen; the skill's copy stays self-contained and
the birth table is unchanged.

## Decision

Templates live in `templates/` inside the skill whose walkthrough
points at them. The relations that make them templates:

1. **This repo's copy is the master.** Each carries a pin +
   provenance header in the file's own comment syntax: checked
   against concept v1 (ADR-0005 — practice-born), extracted from the
   named run's lived file, changes on extraction listed honestly.
   Placeholders use the walkthroughs' existing notation
   (`<project>`, `<project_db>`, `<project_schema>`).
2. **A run copies and fills.** The filled file becomes the run's own
   file — unlike a skill copy, it does not stay pinned verbatim, and
   it may replace the template's header with its own. The bundle's
   birth pin is the provenance of everything filled from it.
3. **Fills never harvest back.** A run's filled values are that
   run's decisions. What harvests is a change to the *shape* — a new
   line every run turns out to need, a comment that was wrong — via
   the ADR-0007 machinery, as with any execution.
4. **The boundary rule** this step enacts: content an agent
   *imitates* stays an example under `references/`; content a run
   *pastes and fills* becomes a template under `templates/` with one
   master. Application source code is neither — it stays outcomes in
   the walkthroughs until a second run re-derives the same shape.

## Consequences

Good: one master per repeating file; a skill directory is the whole
skill — copy it and the walkthrough's pointers resolve; the birth
table needs no new row; walkthroughs shrink to whys and traps, which
is the part templates cannot carry.
Bad: templates ride into every run whether used or not — accepted,
same trade as copy-all-at-birth; and a template can go stale against
the stack it encodes, caught only by the next lived run — accepted,
that is what harvests are for.
