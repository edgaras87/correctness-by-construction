# Change a Kit Copy

<!--
What it is: one of the Backend Kit's files, the Adapted Understanding Text of its Adapted Case for changing a Kit Copy. It says why its Instruction Text is as it is, where only this Adapted Case relies on the reason.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md §2, Changing a Kit Copy, kept in the Maintainer Repo. The rules this Adapted Case shares with others, and why each is so, are there (ADR-0087).
What stands on it: .claude/rules/change-a-kit-copy.md, its Instruction Text, a Paths Rule.
Its first source, input and not rules: temp/common-ground/backend-repo-change-simulation.md §3, step 1, its Chosen.
It never loads; it is read when its Instruction Text changes.
-->

This text says why the rule for changing a Kit Copy loads as it does, and what it leaves open.

## 1. Why a Paths Rule

A Kit Copy changes during work, whenever the work shows a misfit. A Paths Rule loads when a file under its paths is touched, so the rule is there each time a Kit Copy is about to change, and costs nothing in a session that touches none. An Agent Skill was weighed: it runs only when the agent sees the moment, and a Kit Copy changed in passing would miss it.

## 2. Why the header tells a Kit Copy

A Kit Copy sits in the same folders as this repo's own texts, so its path alone does not say it is one. The header of every Backend Kit file names it one. The rule loads for both, and governs only the Kit Copies.

## 3. Open

- **A check at each session's end,** comparing the Kit Copies with their Change Records. Weighed and dropped: it would run every session, needs an Adapted Case of its own, and never runs when a session stops with no warning. The commit and the gate cover what it would find. Its trigger: a gate finds a Copy Change committed in an earlier session with its Change Record missing or wrong.
- **Where the Backend Kit's Defined Terms sit in this repo,** not yet set. Their path joins the rule's `paths:` then. Its trigger: the first Kit Update that carries them.
