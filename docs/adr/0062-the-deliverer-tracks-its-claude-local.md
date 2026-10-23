# 0062. The deliverer tracks its CLAUDE.local.md

Date: 2026-10-23
Status: Proposed (2026-10-23, under the commit plan for
CLAUDE.local.md).

## Context

`CLAUDE.local.md` holds the operator's settings, never rules: how
often the agent stops for review, how far it decides alone
(`docs/conventions/agent-arrangement/` §3.7). The hygiene base
ignores it, since it is one person's, in one checkout. This repo
has ignored it since 2026-09-09.

On 2026-10-23 a setting moved into it from the agent's private
memory: a TODO line decided while talking is staged at once. The
talk that moved it found that the settings shaping how the agent
works here are seen by no reader of the repo, and have no history.
The talk on a session's end had already counted habits the repo
cannot show as a problem (`TODO-CONVERSATION-MEMORY.md` §12). This
repo has one operator.

## Options considered

- **Keep it ignored, and log each setting's why in
  `.claude/decisions.md`.** Rejected: the log would retell the
  file, a second home, and the file itself would stay unseen.
- **Track it on both sides, and ship one to runs.** Rejected: a
  run's operator may set it differently, and the reading of run 3
  declined to ship it (§3.7's lesson).
- **Track the deliverer's only.** Taken.

## Decision

The deliverer's `CLAUDE.local.md` is tracked. Its `.gitignore`
un-ignores the file in its own "this repo" section. The base keeps
ignoring it, so a run's stays ignored.

## Consequences

- agent-arrangement §3.7 and repo-hygiene's seats say so.
- The file still holds settings only, and its words still never
  enter a record.
- A second operator of this repo would make it one person's file
  again. That is when this decision is revisited.
