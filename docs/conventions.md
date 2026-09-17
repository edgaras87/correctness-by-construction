# The conventions' manuals — vendored, read-only

`docs/conventions/` holds the handbook's `conventions/` directory:
the seven manuals, their index, and the three java-spring hygiene
overlay parts. Eleven files, byte-identical to the handbook at the
pin below (ADR-0002's rule, ADR-0024 decision 5). This file sits
beside them rather than inside, so nothing about the set travels
with the set.

Conventions pin: `ba7eaa4` — taken 2026-09-18, the same pin
`starter/kit/` is held at. The two move together: a manual
explaining an artifact at a different hash than the artifact is a
manual that lies.

**Read-only, and why.** A manual is the *why* behind a rule,
written for a maintainer. We hold four of the rule artifacts
verbatim, so their manuals explain ours exactly, and an edit here
would fork the explanation while the rule stayed shared —
anchoring neither copy. Friction with a manual goes up as a
finding, never into the copy (ADR-0022 decision 7).

**What is ours to write, and where it lives.** Anything this repo
flavours needs an explanation these manuals cannot give, because
they do not know it happened. Today that explanation is the delta
list in `starter/README.md` — four departures, one reason each.
When it outgrows a table it graduates into manuals here, ours,
beside theirs.

**What did not come, and why.** Sixteen of the handbook's entries
under `conventions/` are symlinks into `starter/kit/`, not files:
each convention's `SKILL.md`, the record stubs, and the base
hygiene templates. The kit is the master of everything that ships
(HANDBOOK ADR-0040), and we hold that kit at `starter/kit/`, so
reproducing the links would duplicate what we already have. A
manual's pointer to "its artifact" resolves here into
`starter/kit/` instead.

One of those pointers does not resolve, and the mismatch is our
delta rather than a defect:
`docs/conventions/agent-arrangement/stubs/CLAUDE.md` names
`starter/kit/CLAUDE.md`, which our kit does not have — it
ships the entry file at `.claude/CLAUDE.md` (delta row 1).

**Two links dangle, and they are the evidence for a local rule.**
The manuals cite each other and the repo around them with relative
paths. Inside the vendored tree those still resolve, and two that
reach outside it resolve here by accident —
`../../models/tiers.md` and `../../models/agent.md` land on
`docs/models/`, which is where we happen to keep them. Two do not:
`../../starter/README.md` and `../../starter/playbooks/` resolve
to `docs/starter/...`, which does not exist, because our
`starter/` is at the root and theirs sits one level up from
`conventions/`. Not defects to fix — the manuals are read-only and
they are correct where they were written. They are what a relative
path does the moment a file is read from a different root, which
is every vendored copy and every shipped file. This repo's own
documents write paths from the repo root instead; a file we ship
writes them from the root of the repo that receives it.

**The compare.** Byte-identity against the handbook at the pin,
for all eleven; then the reading, which asks what either side has
learned (ADR-0023). Run it when the kit pin moves, since the two
pins move together.

**One finding, parked rather than acted on.** The handbook keeps
Spring hygiene overlays here, at
`docs/conventions/repo-hygiene/templates/java-spring/`. Our
`cbc-bootstrap` never
points at them — it has a run grow its own `.gitignore` from what
the Spring skeleton produces. Two sources for one thing, and our
runs have used neither. Worth a decision when the groups are named
(PLAN Step 9), not before.
