# Commit messages

How a commit is written: Conventional Commits on top of the classic
50/72 rules, with two rules of our own about who commits and what
may share a commit.

**What ships:** [`SKILL.md`](SKILL.md), which a project holds at
`.claude/skills/commit-messages/` and an agent opens before writing
a commit message. This page explains it; the skill states it.

## What it is

A subject line that says what, a body that says why, footers that
link the trail. The subject is typed, `feat`, `fix`, `docs` and so
on, so `git log --oneline` reads as an index of the project's
history, and a release tool can derive a version bump from the
types. The body is the part `git blame` cannot reconstruct: the
reason, the rejected alternative, the constraint that makes a
strange-looking line right. A good commit body is a micro-ADR for a
change too small to deserve a real one.

## Why it is shaped this way

- **Conventional Commits, not just 50/72.** The type prefix carries
  information a plain subject does not, and it is enforceable later
  by a commitlint hook (HANDBOOK ADR-0005).
- **The agent's files never share a commit with the project's.**
  A project that works with an agent has two histories in one repo:
  the work, and the arrangement that made an agent do the work a
  particular way. They stay separable, for a filtered log or a
  portfolio copy that drops the arrangement, only if no commit ever
  straddles them. Hence the `agent` scope (HANDBOOK ADR-0019).
- **Commit on the word.** The commit boundary is the one place a
  wrong assumption is cheap to catch when an agent is doing the
  committing, so the agent stages, shows the diff, and waits. The
  rule is text, in the skill, and gated nowhere: a permission rule
  that stopped every commit at a prompt was shipped once and
  withdrawn, after the one project that could have used it declined
  it and held forty-four commits on the sentence alone (HANDBOOK ADR-0035).

## In this repo itself

This repo's product is documents too, and the handbook's answer to
that was to make the type carry the signal — `feat(<convention>)`
for the product, `docs(handbook)` for the records — so that `docs`
did not swallow everything. **We did not adopt it**, and the
practice that grew instead is worth stating rather than leaving to
be inferred from 480 commits:

- `docs(<area>)` for almost everything, the scope naming the area
  touched: `adr`, `delivery`, `conventions`, `temp`, `devlog`,
  `agent`. Bare `docs` where a commit spans the records generally.
- `chore(agent)` for pinned copies updated to a new upstream state.
- `feat`/`fix` only where the delivery gained or lost something a
  run would notice — rare, and all on the delivery so far.

So the type is nearly always `docs` and the **scope** carries the
signal here, which is the mirror of their answer, not a weaker
version of it. Either works; what does not work is following
neither and discovering the shape afterwards, which is what
happened — this section was theirs, describing a practice we do not
have, while ours was written nowhere until 2026-09-19.

This note is local and does not ship.

## Where to look

- The rules: [`SKILL.md`](SKILL.md).
- The commit boundary inside a change set:
  [`../commit-plan/`](../commit-plan/).
- What the `agent` scope covers:
  [`../agent-arrangement/`](../agent-arrangement/).
