# The conventions' manuals

`docs/conventions/` holds the seven convention manuals, their
index, and the three java-spring hygiene overlay parts — eleven
files. A manual is the *why* behind a rule, written for a
maintainer and never shipped to a run; the rules themselves are
the skill files in `delivery/container/.claude/skills/` and the shapes of
the stubs beside them.

They are this repo's, to change when a rule here changes
(ADR-0025). They began as copies of the handbook's `conventions/`
and were identical to them until 2026-09-19, when 66 citations and
nine paths were corrected to be true in this repo — see below. The
bodies are otherwise untouched, so a re-sync still diffs cleanly
against the handbook once those two classes are set aside.

**Provenance, recorded once.** Taken from the handbook at
`ba7eaa4`, and identical through their `8adb46f`, which is the
last state this repo was aligned with. The same coordinates
`delivery/container/` carries, because the two were taken together and a
manual explaining an artifact from a different state would
mislead. Nothing here tracks that repo.

**Keep them true to the rules they explain.** A manual's only job
is to say why its rule is shaped as it is. If a rule in
`delivery/container/` changes and its manual here does not, the manual
lies — and it is the kind of lie nothing catches, because a
manual is read rarely and by whoever is least sure. So the manual
moves with its rule, in the same commit.

**What did not come, and why.** Sixteen of the handbook's entries
under `conventions/` are symlinks into `delivery/container/`, not files:
each convention's `SKILL.md`, the record stubs, and the base
hygiene templates. The kit is the master of everything that ships
(HANDBOOK ADR-0040), and we hold that kit at `delivery/container/`, so
reproducing the links would duplicate what we already have. A
manual's pointer to "its artifact" resolves here into
`delivery/container/` instead.

One of those pointers does not resolve, and the mismatch is our
delta rather than a defect:
`docs/conventions/agent-arrangement/stubs/CLAUDE.md` names
`delivery/container/CLAUDE.md`, which our kit does not have — it
ships the entry file at `.claude/CLAUDE.md` (delta row 1).

**What was corrected, and why it could not wait.** Two classes,
both of which made a manual say something false *here* while being
correct where it was written.

The citations, and these were the serious ones. A shipped rule
writes `HANDBOOK ADR-nnnn` precisely because, as
`docs/conventions/README.md` states, a bare number names the
reading repo's own decision. The manuals wrote bare numbers — 66 of
them across all eight files — so every one read as ours, and about
22 of the numbers exist here and point at an unrelated decision. A
manual saying `ADR-0005` meant Conventional Commits and read as
*practice-born executions pin as checked-against*. Nothing errors;
a reader lands somewhere plausible and wrong. The shipped half had
been prefixed and the kept half had not, which is what makes this
an oversight rather than a choice: whoever prefixed the rules did
not walk the manuals.

The paths, nine lines in five files, plus the pointers that reach
out of the vendored tree into this repo. Four of those: two did
not resolve at all — their `starter/` sits one level up from
`conventions/` while ours is at the root and, since ADR-0029, is
not called that either — and two resolved *by accident*,
`../../models/tiers.md` and `../../models/agent.md` landing on
`docs/models/` because that is where we happen to keep them. All
four are now written from the repo root, as `docs/models/agent.md`
and `delivery/README.md` rather than as relative links, because
that is this file's own rule and a pointer that works by accident
is the one that breaks silently. The `stubs/` links went the same
way: those directories were never reproduced here, so the lines
name `delivery/container/` instead of linking into nothing.

**The line that decides which pointers get rewritten** is whether
they leave the tree. The ten remaining relative links go
manual-to-manual — `../commit-messages/` and its kin — and are
left alone: they resolve, they are the handbook's own internal
cross-references, and rewriting them would be a change of voice
rather than a correction.

**The local rule this is evidence for** is unchanged, and is why
the bodies could be left alone otherwise: a relative path means a
different thing the moment a file is read from a different root,
which is every vendored copy and every shipped file. This repo's
own documents write paths from the repo root instead; a file we
ship writes them from the root of the repo that receives it.

**What is still not ours** is the voice. `docs/conventions/README.md`
is written *as the handbook*, end to end — "the kit is the master",
"this repo's own `.claude/skills/` holds copies at a pin, like any
project's". Correcting its citations and paths does not touch that,
and rewriting it is ADR-0025's question rather than a fix. It is in
TODO.

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
