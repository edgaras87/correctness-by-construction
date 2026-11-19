# 0083. The subject's aim, 50, and its line, 70

Date: 2026-11-19
Status: Accepted (2026-11-19, the reviewer, at the final records
commit of the commit plan for the subject limit; opened Proposed, and
revised at its commit 4, the 70 moved out of the writer's Agent Skill
into the checks)

## Context

A commit subject is limited to 50 characters (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*). ADR-0049, decision 4, kept that limit, and rejected raising it: when subjects were counted where they were first written, they fit, so the limit had been unchecked, not set wrong.

The limit is still missed, and each miss costs a decision:

- **History:** of the 2,875 subjects up to `31e3f34`, 672 are over 50 characters, 132 over 60, 52 over 65 and 17 over 72. Since 2026-11-11, 14 of 256 are over 50.
- **This session:** two subjects landed at 59 and 55, uncounted when written. Rewording them would have rewritten two commits and a hash one body names. The reviewer asked whether a small miss matters at all.
- **What a long subject breaks:** GitHub cuts a subject past 72 characters and moves the rest into the body. `git log --oneline` puts an 8-character hash before the subject, so up to 72 characters fit an 80-column terminal. Below that, nothing breaks.
- **The prefix:** the 50/72 habit was made for plain subjects. A Conventional Commits prefix takes part of the 50: `chore(agent): ` is 14 characters.
- **What counting at writing does:** from 2026-09-20 to 10-02, nobody counted, and 18 of 429 subjects passed 70. From 2026-10-08, plans counted their subjects, and from 2026-11-06 the agent counted every other one too; 1 of 1,887 passed 70. Counting costs one command per subject, at every commit.
- **A number the writer sees is a number the writer uses.** The plan's commit 4 put "ask past 70" in the commit-messages Agent Skill. The reviewer: the writer must see only 50, or 70 becomes room to spare.

## Options considered

- **50 as a hard limit, as before.** Rejected: every miss of a few characters costs a reword or a decision, though nothing breaks below 72.
- **A limit raised to 60 or 65.** Rejected: the subjects would drift to the new limit, and a short subject reads best in the log.
- **50 the aim and 70 the line, both in the writer's Agent Skill,** as the plan's commit 4 wrote it. Rejected: the writer would aim at the line.
- **Counting every subject at writing, at every commit.** Not taken for now: it costs a step at every commit, and the checks at rare points may be enough. A trial decides it.
- **50 for the writer, 70 for the checks.** Chosen.

## Decision

1. **The writer aims at 50.** The commit-messages Agent Skill states 50 only, and no other number.
2. **The checks use 70.** At a Plan Step's close and a session's end, every subject is counted by script. One up to 70 characters passes. Past 70, the reviewer decides whether it is rewritten. 70 sits below GitHub's cut at 72, and fits an 80-column terminal with its hash.
3. **A single commit's subject is not counted at writing.** A commit plan still counts its own subjects when it is written, as ADR-0049 decided. Whether single commits are counted is a trial, kept in TODO: each subject past 70 a check finds counts, fixed or kept, and at the 5th the reviewer decides to adopt counting, give it 5 more, or drop the question.

Supersedes ADR-0049, decision 4, in part: the 50 stays, and so does a plan's count; what a miss costs, and who sees which number, change.

## Consequences

- The commit-messages manual's §2.1 holds the rule, and says who uses which number. The commit-messages Agent Skill stays at `≤50 chars`, in the Master Copy and in our copy. The Plan Step Form's close item, ours and the CBC Run playbook's, checks against 70. The session-end check is in `CLAUDE.local.md`'s session-end list.
- A subject a little long no longer stops the work. One past 70 still does, but only at a check.
- Without counting at writing, more subjects may pass 70, as before 2026-10-08. The trial counts them, and its 5th find brings the question back.
