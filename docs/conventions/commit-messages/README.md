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
  by a commitlint hook (ADR-0005).
- **The agent's files never share a commit with the project's.**
  A project that works with an agent has two histories in one repo:
  the work, and the arrangement that made an agent do the work a
  particular way. They stay separable, for a filtered log or a
  portfolio copy that drops the arrangement, only if no commit ever
  straddles them. Hence the `agent` scope (ADR-0019).
- **Commit on the word.** The commit boundary is the one place a
  wrong assumption is cheap to catch when an agent is doing the
  committing, so the agent stages, shows the diff, and waits. The
  rule is text, in the skill, and gated nowhere: a permission rule
  that stopped every commit at a prompt was shipped once and
  withdrawn, after the one project that could have used it declined
  it and held forty-four commits on the sentence alone (ADR-0035).

## In the handbook itself

A repo whose product is documents would file every commit under
`docs`, and the type would carry nothing. So here:

- `feat(<convention>)` or `fix(<convention>)` for the product, the
  scope being the unit that ships — a convention's name, `starter`
  for the kit, `agent-model` or `tiers-model` for a model.
- `docs(handbook)` for the records catching up: PLAN, ADRs, devlog,
  TODO, changelog.
- `chore` for hygiene and tooling; `chore(agent)`, `feat(agent)`,
  `docs(agent)` for this repo's own arrangement, as anywhere.

This note is the handbook's and does not ship.

## Where to look

- The rules: [`SKILL.md`](SKILL.md).
- The commit boundary inside a change set:
  [`../change-plans/`](../change-plans/).
- What the `agent` scope covers:
  [`../agent-arrangement/`](../agent-arrangement/).
