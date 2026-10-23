# Commit plan: this repo tracks its CLAUDE.local.md

## Summary — the state after all commits

This repo's `CLAUDE.local.md` is in git. Its settings, and why each
changed, can be read in the repo and its history. A run's stays
ignored, and the container still ships none.

agent-arrangement §3.7 and repo-hygiene's seats say so for each
side. ADR-0062 holds the decision and the option rejected. Our
`.gitignore` keeps the base section identical to the container's,
and un-ignores the file in its own "this repo" section.

## Commits

**0. `docs(agent): add commit plan for CLAUDE.local`**
Opens the set.

**1. `docs: the deliverer tracks its CLAUDE.local.md`**
ADR-0062, Proposed. agent-arrangement §3.7 gains a line for each
side: ours is tracked, a run's stays ignored. repo-hygiene's seats
say the deliverer un-ignores it in its own section. With them, what
derives: `.gitignore` gains `!CLAUDE.local.md` in the "this repo"
section, the base section untouched, and the file itself is added
as it stands today.

**2.** Merged into 1. Our `.gitignore` derives from repo-hygiene,
and the foundation check puts a derived change in the same commit
as its manual's, unless one side is the agent's own files. Apart,
commit 1 would say the file is tracked while git still ignored it.

**3. `chore(agent): log tracking CLAUDE.local.md`**
`.claude/decisions.md`: a two-line entry pointing at ADR-0062.
Its own commit: the agent's files never share one with records.

**4. `docs: accept ADR-0062`**
The final records commit: the ADR flips to Accepted.

**5. `docs(agent): close commit plan for CLAUDE.local`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **An ADR, not only a log entry.** The change is to a convention,
  agent-arrangement §3.7, with an option rejected: keep the file
  ignored and log each setting's why in `.claude/decisions.md`. The
  log entry follows from the ADR and points at it, as its header
  asks.
- **ADR-0062 goes to this decision.** The text-division item's ADR
  takes the next number when it lands.
- **Un-ignore, not delete the base line.** The base section is a
  copy of the container's master; a negation in our own section
  keeps it identical.
- **The devlog is not a commit here.** It is written at the
  session's end, as every session's is.
