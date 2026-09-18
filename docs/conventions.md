# The conventions' manuals

`docs/conventions/` holds the seven convention manuals, their
index, and the three java-spring hygiene overlay parts — eleven
files. A manual is the *why* behind a rule, written for a
maintainer and never shipped to a run; the rules themselves are
the skill files in `starter/kit/.claude/skills/` and the shapes of
the stubs beside them.

They are this repo's, to change when a rule here changes
(ADR-0025). They began as copies of the handbook's `conventions/`
and are still identical to them.

**Provenance, recorded once.** Taken from the handbook at
`ba7eaa4`, and identical through their `8adb46f`, which is the
last state this repo was aligned with. The same coordinates
`starter/kit/` carries, because the two were taken together and a
manual explaining an artifact from a different state would
mislead. Nothing here tracks that repo.

**Keep them true to the rules they explain.** A manual's only job
is to say why its rule is shaped as it is. If a rule in
`starter/kit/` changes and its manual here does not, the manual
lies — and it is the kind of lie nothing catches, because a
manual is read rarely and by whoever is least sure. So the manual
moves with its rule, in the same commit.

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
`conventions/`. Not defects to fix today — they are correct where
they were written, and rewriting eleven files' links buys nothing
until someone follows one. They are what a relative
path does the moment a file is read from a different root, which
is every vendored copy and every shipped file. This repo's own
documents write paths from the repo root instead; a file we ship
writes them from the root of the repo that receives it.

**No compare runs on a schedule.** These are ours; nothing
upstream is owed a reading (ADR-0025). If a re-sync is ever
attempted, the coordinates above are where it starts — and
`git diff 8adb46f..<theirs> -- conventions` is the whole of what
it would have to read.

**One finding, parked rather than acted on.** Spring hygiene
overlays live here, at
`docs/conventions/repo-hygiene/templates/java-spring/`. Our
`cbc-bootstrap` never
points at them — it has a run grow its own `.gitignore` from what
the Spring skeleton produces. Two sources for one thing, and our
runs have used neither. Worth a decision when the groups are named
(PLAN Step 9), not before — and now ours to decide alone.
