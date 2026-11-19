# Commit plan: the subject's limit, an aim and a line

## Summary — the state after all commits

A commit subject still aims at 50 characters, and is still counted by script when it is written. What changes is what a miss costs. A subject of 51 to 70 characters stands, with no decision and no reword. Past 70, the reviewer decides whether it is rewritten. The 70 has a reason: GitHub cuts a subject past 72, and an 8-character hash with 70 fits an 80-column terminal.

ADR-0083 records the change, and supersedes ADR-0049's decision 4 in part: the 50 stays, and so does the counting when a plan writes a subject. The commit-messages manual's §2.1 holds the rule and its why. The commit-messages Agent Skill states it, in the Master Copy and in our copy.

The Decisions Log also gains the entry this session's visual-comparison change missed: the reviewer renders, and the agent checks the syntax (`5b9f2cf`, `9b7b169`).

## Commits

**1. `docs(agent): add commit plan for subject limit`**
This plan, agreed before any work.

**2. `docs(adr): 0083, the subject's aim and its line`**
The decision first, since it was settled in talk. Opens Proposed. Context: 672 of 2,874 subjects over 50, 52 over 65, 17 over 72; ADR-0049's reason for keeping 50, that subjects fit when counted at writing, and this session's two misses, uncounted. Options: 50 as a hard limit, as today; a limit raised to 60 or 65; 50 as the aim with 70 as the line, chosen.

**3. `docs: commit-messages manual draws a line at 70`**
The manual's §2.1 holds the rule and its why: 50 the aim, 51 to 70 standing, past 70 the reviewer's decision. A Canonical Description changed, so the Change Walk runs on what stands on it: the commit-plan manual's §2.8, *Counting subjects*, and the two Agent Skill copies. What the walk finds, beyond commits 4 and 5, is said at this boundary.

**3b. `docs: commit-plan manual counts against the aim`**
Inserted at commit 3's boundary, from its Change Walk. The commit-plan manual's §2.8, *Counting subjects*, says a subject is counted against "the subject's 50-character limit"; after commit 3, 50 is the aim and 70 the line, so "limit" becomes "aim". The commit-plan Agent Skill's "its limit" reads true either way, and stays.

**4. `fix(delivery): commit-messages asks past 70 only`**
The Master Copy's subject line in *Format*: aim for 50, ask only past 70. The Foundation Check reads the manual's new §2.1 beside it.

**5. `chore(agent): commit-messages follows delivery`**
Our copy takes commit 4's change, and the Decisions Log gains its entry: the limit's line, pointing at ADR-0083. The agent's memory note on measuring subjects is changed with it, outside git: 50 the aim, 70 the line.

**6. `chore(agent): log the reviewer rendering pictures`**
The Decisions Log entry `9b7b169` lacked: the visual-comparison Agent Skill now asks the reviewer to render, and the agent to check the syntax. Why: the reviewer always looks at the render, and the renderer was refused here. Rejected: the agent rendering, with a permission rule for the renderer. Its own commit, since it is another decision.

**7. `docs(adr): 0083 accepted, 0049 superseded in part`**
The final records commit. ADR-0083 turns Accepted. ADR-0049's status names it, for decision 4.

**8. `docs(agent): close commit plan for subject limit`**
Deletes this file. Its body says what diverged.

## Decisions taken inside this plan

- **70, not 65 or 72.** 70 is your number. It sits below GitHub's cut at 72, and with a hash it fits an 80-column terminal.
- **A new ADR, not an edit to ADR-0049.** An accepted ADR's decision is never edited (`docs/adr/README.md`, its header comment).
- **Commit 6 is in this plan, though it is another change.** It is the same record, the Decisions Log, found missing while this plan walked the records table. It could instead stand alone after the close.
- **No CHANGELOG entry:** the commit-messages Agent Skill is not derived from the concept (`CHANGELOG.md`, its header comment).
- **No glossary entry:** the rule needs no new Name. "The aim" and "the line" are plain English.
- **Today's two subjects stand:** `5b9f2cf` at 59 and `9b7b169` at 55 pass the new rule. This plan's subjects all fit 50, measured by script: 46 to 49.
- **The devlog entry comes after the close,** as the session's last step, outside this plan.
