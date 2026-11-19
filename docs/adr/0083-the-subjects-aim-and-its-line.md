# 0083. The subject's aim, 50, and its line, 70

Date: 2026-11-19
Status: Proposed, opened under the commit plan for the subject limit

## Context

A commit subject is limited to 50 characters (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*). ADR-0049, decision 4, kept that limit, and rejected raising it: when subjects were counted where they were first written, they fit, so the limit had been unchecked, not set wrong.

The limit is still missed, and each miss costs a decision:

- **History:** of the 2,875 subjects up to `31e3f34`, 672 are over 50 characters, 132 over 60, 52 over 65 and 17 over 72. Since 2026-11-11, 14 of 256 are over 50.
- **This session:** two subjects landed at 59 and 55, uncounted when written. Rewording them would have rewritten two commits and a hash one body names. The reviewer asked whether a small miss matters at all.
- **What a long subject breaks:** GitHub cuts a subject past 72 characters and moves the rest into the body. `git log --oneline` puts an 8-character hash before the subject, so up to 72 characters fit an 80-column terminal. Below that, nothing breaks.
- **The prefix:** the 50/72 habit was made for plain subjects. A Conventional Commits prefix takes part of the 50: `chore(agent): ` is 14 characters.

## Options considered

- **50 as a hard limit, as now.** Rejected: every miss of a few characters costs a reword or a decision, though nothing breaks below 72.
- **A limit raised to 60 or 65.** Rejected: the subjects would drift to the new limit, and a short subject reads best in the log. ADR-0049's reason still holds: counted at writing, subjects fit 50.
- **50 as the aim, 70 as the line.** Chosen.

## Decision

1. **A subject aims at 50 characters,** and is counted by script when it is written, as ADR-0049 decided.
2. **A subject of 51 to 70 characters stands,** with no decision and no reword.
3. **Past 70, the reviewer decides** whether it is rewritten. 70 sits below GitHub's cut at 72, and fits an 80-column terminal with its hash.

Supersedes ADR-0049, decision 4, in part: the 50 and the counting stay; what a miss costs changes.

## Consequences

- The commit-messages manual's §2.1 holds the rule and its why. The commit-messages Agent Skill states it, in the Master Copy and in our copy. A CBC Run takes it at its next delivery.
- A subject a little long no longer stops the work. One past 70 still does.
- The aim holds only while subjects are counted. If misses become common, the counting has stopped, and that is the defect, not the aim.
