# Commit messages

**How a commit is written: Conventional Commits on top of the
classic 50/72 rules, with two rules of our own about who commits
and what may share a commit.**

## What it is for

So that `git log --oneline` reads as an index of a project's
history, a release tool can derive a version from the types, and
the agent's files can be filtered out of the history without
rewriting it. Adopted with the container (CBC ADR-0038, 1a, 1c,
1f). The failure it answers is measured: with the subject limit
ambient in an entry file and the rule pulled in by a skill,
fifteen of the first twenty commits of the repo it came from broke
the limit — present, correct, unfollowed (`docs/models/agent.md`
§12, A1) — which is why the rule is opened at the commit moment
and not read once. Lived here since: 480 commits under it by
2026-09-19, and run 3 held forty-four commits on the stop sentence
alone with no gate.

## What this is made usable as

- **`delivery/container/.claude/skills/commit-messages/SKILL.md` —
  the skill, shipped**, held at `.claude/skills/commit-messages/`
  and opened before writing a commit message. The format, the type
  table, the `agent` scope, the stop, with the decisions it rests
  on in its footer.
- **`.claude/skills/commit-messages/SKILL.md` — the deliverer's**,
  derived from this page like the container's and identical to it
  today, neither copied from the other (CBC ADR-0042).

This page explains; the skill states. What derives from this page
is that list. A change here walks it; a change forced in one of
them is checked back against this page.

## The seats

A run commits under the skill. The deliverer commits under the
same skill, and has one local habit — which scope carries the
signal — stated in §3 and not shipped.

## 1. What it is

A subject line that says what, a body that says why, footers that
link the trail. The subject is typed, `feat`, `fix`, `docs` and so
on, so `git log --oneline` reads as an index of the project's
history, and a release tool can derive a version bump from the
types. The body is the part `git blame` cannot reconstruct: the
reason, the rejected alternative, the constraint that makes a
strange-looking line right. A good commit body is a micro-ADR for a
change too small to deserve a real one.

## 2. Why it is shaped this way

- **Conventional Commits, not just 50/72.** The type prefix carries
  information a plain subject does not, and it is enforceable later
  by a commitlint hook (CBC ADR-0038, 1a).
- **The agent's files never share a commit with the project's.**
  A project that works with an agent has two histories in one repo:
  the work, and the arrangement that made an agent do the work a
  particular way. They stay separable, for a filtered log or a
  portfolio copy that drops the arrangement, only if no commit ever
  straddles them. Hence the `agent` scope (CBC ADR-0038, 1c); which
  paths are the arrangement's is
  `docs/conventions/agent-arrangement/` §1.
- **Commit on the word.** The commit boundary is the one place a
  wrong assumption is cheap to catch when an agent is doing the
  committing, so the agent stages, shows the diff, and waits. The
  rule is text, in the skill, and gated nowhere (CBC ADR-0038, 1f).
  *A permission rule that stopped every commit at a prompt was
  shipped once and withdrawn, 2026-09-10, after the one project
  that could have used it declined it and held forty-four commits
  on the sentence alone.*

## 3. The deliverer's habit

The deliverer's product is documents, so `docs` could swallow
everything. One answer is to make the type carry the signal —
`feat(<convention>)` for the product, `docs` for the records.
**The deliverer did not take it**, and the practice that grew
instead is worth stating rather than leaving to be inferred from
480 commits:

- `docs(<area>)` for almost everything, the scope naming the area
  touched: `adr`, `delivery`, `conventions`, `temp`, `devlog`,
  `agent`. Bare `docs` where a commit spans the records generally.
- `chore(agent)` for the deliverer's own skills and rules, each
  derived from its manual.
- `feat`/`fix` only where the delivery gained or lost something a
  run would notice — rare, and all on the delivery so far.

So the type is nearly always `docs` and the **scope** carries the
signal here, which is the mirror of the other answer, not a weaker
version of it. Either works; what does not work is following
neither and discovering the shape afterwards. *Until 2026-09-19
this section described a practice the deliverer does not have, and
its own was written nowhere.*

This section is the deliverer's and does not ship.

## Why it arrives this way

A skill, opened at the moment of writing a commit message, because
the rule held ambient in an entry file was present and unfollowed
(*What it is for*). The commit is also the moment other
conventions' discipline binds at — the `agent` scope, the stop —
which is why those sentences live in this skill and nowhere else.

## What this does not cover

- **The change set: sequencing, the boundary inside a plan, the
  close** — `docs/conventions/commit-plan/`.
- **What the agent side is, and which paths it holds** —
  `docs/conventions/agent-arrangement/`.
- **The records a commit's footer links, and what an ADR is** —
  `docs/conventions/project-recording/`.

## Where to look

- The commit boundary inside a change set:
  `docs/conventions/commit-plan/`.
- What the `agent` scope covers: `docs/conventions/agent-arrangement/`.
