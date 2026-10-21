# How I work with Claude (full auto)

## Commits
- Commit freely: small commits on each step's branch.
- At a step's close: fast-forward main to the branch as it is, and
  tag `run5/step-<n>`. Agent files apart from project files.
- Never create a remote. Never push. Never delete a branch.

## Explaining
- Write so I can read it once, in chat and in records:
  `.claude/rules/writing.md`.

## Decisions
- Do not wait for me. Decide by `docs/run.md`, and log each
  decision in `docs/decision-log.md` with what was rejected and
  why. I read the log after the run.

## New kinds of work
- Work that no skill, rule or approach on trial covers gets an
  approach on trial: `.claude/approaches-on-trial/approach-drafting.md`.

## Where you work
- Only inside this directory, and the containers and volumes you
  create. Never read or change another repository, or another
  project's containers.
