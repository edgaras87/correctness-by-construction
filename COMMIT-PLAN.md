# Commit plan: a skill's phases are stages

## Summary — the state after all commits

No shipped skill calls its phases steps; "step" is PLAN's (the
reading's D6, W17). `cbc-framing`'s parts are Stage 0 to Stage 6,
and `infra-establish`'s walk, after its Stage 0, is Stage 1 to
Stage 7, as `cbc-slice`, `cbc-bootstrap` and `infra-serve` already
say. Every text citing them follows, both worked examples alike. A
numbered instruction inside a stage keeps "step".

## Commits

**1. `docs: framing's parts are stages`**
`cbc-framing`'s skill, workflow and plain page, and both worked
examples, kept identical; `cbc-slice`'s workflow, which cites
framing's stage 3. Framing's family reverts as one.

**2. `docs: infra-establish walks in stages`**
The skill's gates and the walk's references to its own parts.
Apart from commit 1, since nothing in framing cites the walk.

**3. `docs(temp): the reading closes W17`**
W17 marked done, D6's finding F14 ended, and the pass over every
open item.

## Decisions taken inside this plan

- **Chapter 03 stays.** It calls choosing the promise "the hardest
  step" in plain English and numbers no part, so no Now line can
  meet it.
- **No CHANGELOG line.** Only skills change, as in F1 and F2.
- **Walkthrough sections stay steps,** as D6 says: the PostgreSQL
  walkthrough's "re-run step 7" is its own section 7, not the walk's.
