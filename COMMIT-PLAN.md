# Commit plan: writing rules

## Summary — the state after all commits

Two rules load in every session of every run, and here: how a text
reads (`writing.md`) and where a fact lives (`one-home.md`). Run 3
wrote both at its retrospective (its RETRO.md, D1 and D2) because
the same lessons, kept in a manual and in the agent's memory, never
changed its records; loaded, they did.

`writing` is a new convention, the tenth, its manual the why of each
rule. One home per fact is not new: it is project-recording's §11,
rule 1, which now ships as a loaded rule as well. Agent-arrangement
gains the slot neither fitted: a convention whose moment is every
task ships as a rule with no `paths:`, paid for in every session.
Both rules reach a run in the container, their examples from the
worked example's order service and its full-word tags; and this
repo holds its own, so its new text follows them from now. Its old
text is the reading's W8. ADR-0053 records it.

## Commits

**1. `docs(agent): add commit plan for writing rules`**
This plan, agreed.

**2. `docs(adr): 0053, how text reads, where facts live`**
The decision, opened Proposed: a writing convention; one home per
fact loaded from project-recording; ambient rules for a convention
whose moment is every task. Rejected: the voice kept in memory or in
`CLAUDE.local.md`; one rule for both questions; rules loaded only on
Markdown paths, which miss chat; the lessons left in manuals.

**3. `docs: ambient rules may carry a convention`**
Agent-arrangement's §2.4 and §3.2: a rule with no `paths:` passes
the entry file's tests when it is a convention's artifact whose
moment is every task and nothing else delivers it; it is paid for
in every session, so few qualify.

**4. `docs: a writing convention, and its rule`**
The manual, `docs/conventions/writing/README.md`; the shipped
`delivery/container/.claude/rules/writing.md`; the container's
decisions-log birth entry names the convention; `ARCHITECTURE.md`'s
counts and what the manuals cover.

**5. `docs: one home per fact, loaded`**
Project-recording: §11's rule 1 gains what run 3's rule found it
lacked, as a dated lesson: a summary says it is one and names its
owner; a fact changes at its home; two copies that cannot be
avoided are an owner and a follower, with a check; history is not a
second home; comments and config count too. It gains its loaded
rule, and its *What this is made usable as* and *Why it arrives
this way* say so. The shipped
`delivery/container/.claude/rules/one-home.md`; `ARCHITECTURE.md`'s
list of the container's files.

**6. `chore(agent): this repo loads the writing rules`**
`.claude/rules/writing.md` and `.claude/rules/one-home.md`, derived
from the manuals like the container's; an entry in
`.claude/decisions.md`, since it changes how this repo's agent
works.

**7. `docs: records carry the writing rules`**
ADR-0053 Accepted.

**8. `docs(agent): close commit plan for writing rules`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **Writing is its own convention; one home is project-recording's.**
  How a text reads is no record's business. Where a fact lives is
  exactly the records': §11 already says it, and the records table
  already says which record owns which fact.
- **The rule is checked back against its manual**
  (`docs/conventions/conventions/` §3.5, rule 4). Run 3's one-home
  rule says five things §11 does not, so §11 takes them; the rule
  takes nothing back, since its why is the manual's. Writing's
  manual is new and written from its rule, so nothing to calibrate.
- **Both always loaded.** Run 3's first draft loaded writing on
  Markdown paths only, and dropped it: chat has no path. A `paths:`
  list loads on reading a file, not on writing one, so one home on
  record paths would miss the moment of writing too.
- **The examples are the order service's,** in full-word tags; the
  glossary is "the project's, where it keeps one", since no
  container record is a glossary yet (group E's).
- **This repo adopts both now** (commit 6). New text follows them
  from the commit; the old is W8's, after the reading.
- **Neither rule names CbC.** They are the container's, and the
  container is what any project would want.
