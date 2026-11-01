# Commit messages

**How a commit is written: its message, who commits it, and what
may share one.**

## What it is for

So that `git log --oneline` reads as an index of a project's
history, a release tool can derive a version from the types, and
the agent's files can be filtered out of the history without
rewriting it. Adopted with the Container Group (ADR-0038, 1a, 1c,
1f). The failure it answers is measured. The subject limit sat in an
Entry File, through the Ambient Channel, and an Agent Skill pulled
the rule in. 15 of the first 20 commits of the repo it came from
broke it: present, correct, unfollowed (`docs/models/agent.md`
§12, *Claims*, A1). So the rule is opened at the commit, not read
once. Lived here since: 480 commits under it by
2026-09-19, and CBC Run 3 held forty-four commits on the stop
sentence, the rule that the agent waits at each commit, alone with
no Enforcement Gate.

## What this is made usable as

- **`delivery/container/.claude/skills/commit-messages/SKILL.md` —
  the Agent Skill, shipped**, held at `.claude/skills/commit-messages/`
  and opened before writing a commit message. The format, the type
  table, the `agent` scope, the stop, with the decisions it rests
  on in its footer.
- **`.claude/skills/commit-messages/SKILL.md` — the Concept Deliverer's**,
  derived from this page like the Container Group's, neither copied from
  the other, and written for this Convention Seat (ADR-0042, ADR-0069).

This page explains; the Agent Skill states. What derives from this page
is that list. A change here runs the Change Walk on it; a change forced in one of
them is checked back against this page.

## The seats

A CBC Run commits under the Agent Skill. The Concept Deliverer commits under the
same Agent Skill. It has one local habit: the scope, not the type,
carries the signal. It is stated in its own section, and not shipped
(§3, *The Concept Deliverer's habit*).

## 1. What a commit message is

A subject line that says what, a body that says why, footers that
link the trail. The subject is typed, `feat`, `fix`, `docs` and so
on, so `git log --oneline` reads as an index of the project's
history, and a release tool can derive a version bump from the
types. The body is the part `git blame` cannot reconstruct: the
reason, the rejected alternative, the constraint that makes a
strange-looking line right. A good commit body does for a small
change what an ADR does for a large one.

## 2. Why it is shaped this way

### 2.1 Conventional Commits

Conventional Commits, not just the 50/72 limits, 50 characters for
the subject and 72 for a body line. The type prefix carries
information a plain subject does not, and it is enforceable later
by a commitlint hook (ADR-0038, 1a).

### 2.2 Mood and tense

Either mood, in the present tense. A subject says what the
commit changes. A change to the work reads naturally as a command,
a record as what became true. Both read well in the log. *Its story: ADR-0049.*

### 2.3 The `agent` scope

The agent's files never share a commit with the project's. A project that works with an agent has two histories in one repo:
the work, and the arrangement that made an agent do the work a
particular way. They stay separable, for a filtered log or a
portfolio copy that drops the arrangement, only if no commit ever
straddles them. Hence the `agent` scope (ADR-0038, 1c); which
paths are the arrangement's is the agent-arrangement manual's
(`docs/conventions/agent-arrangement/` §1.1, *A closed list of paths*).

### 2.4 Commit on the word

The commit boundary is the one place a
wrong assumption is cheap to catch when an agent is doing the
committing. So the agent stages the commit, shows the diff, and
waits for the word: the stop. The
rule is text, in the Agent Skill, and gated nowhere (ADR-0038, 1f).
*Its story: devlog 2026-09-10, later; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 3. The Concept Deliverer's habit

Here the type is nearly always `docs`, and the **scope**, where one
is given, carries the signal. The Concept Deliverer's product is
documents, so `docs` could be every commit's type. One answer is to
make the type carry the signal —
`feat(<convention>)` for the product, `docs` for the records.
**The Concept Deliverer did not take it**, and the practice that grew
instead is worth stating rather than leaving to be inferred from
the log:

- Bare `docs` for most: the manuals, the records, `ARCHITECTURE.md`.
- `docs(<area>)` where one area is the whole commit: `temp` for a
  draft or the refinement's file, `agent` for the agent's records
  such as a commit plan, `adr` for an ADR.
- `chore(agent)` for the Concept Deliverer's own Agent Skills, Agent Rules and
  Approaches on Trial.
- `feat`/`fix` where something a CBC Run would notice was gained or
  lost: `fix(delivery)` most often, `fix(concept)` and
  `fix(agent)` rarely.

So the scope carries the signal here. It is the other answer done
with the scope instead of the type, and not a weaker version of it. Either works; what does not work
is following neither and discovering the shape afterwards. *Its story: devlog 2026-09-19, after the close; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## Why it arrives this way

An Agent Skill, opened at the moment of writing a commit message
(`docs/models/agent.md` §4.2, *Pulled Channel*), because the rule held in an
Entry File, through the Ambient Channel, was present and unfollowed (*What it is for*;
`docs/models/agent.md` §12.1, *Claims on the Ambient Channel*). The commit is also the moment two other
rules bind at, the `agent` scope and the stop. That is why those
sentences live in this Agent Skill and nowhere else.

## What this does not cover

- **The Change Set: sequencing, the boundary inside a plan, the
  close** — `docs/conventions/commit-plan/`.
- **What the agent side is, and which paths it holds** —
  `docs/conventions/agent-arrangement/`.
- **The records a commit's footer links, and what an ADR is** —
  `docs/conventions/project-recording/`.

## Where to look

- The commit boundary inside a Change Set:
  `docs/conventions/commit-plan/`.
- What the `agent` scope covers: `docs/conventions/agent-arrangement/`.
