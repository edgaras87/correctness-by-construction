# Take the Kit Update

<!--
What it is: one of the Backend Kit's files, the Adapted Understanding Text of its Adapted Case for taking a Kit Update. It says why its Instruction Text is as it is, where only this Adapted Case relies on the reason.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md §3, Taking a Kit Update, kept in the Maintainer Repo. The rules this Adapted Case shares with others, and why each is so, are there (ADR-0087).
What stands on it: .claude/skills/take-the-kit-update/SKILL.md, its Instruction Text, an Agent Skill.
Its first source, input and not rules: temp/common-ground/backend-repo-change-simulation.md §8, step 1, its Chosen.
It never loads; it is read when its Instruction Text changes.
-->

This text says why an Update Take runs on a branch of its own, in the order its Agent Skill gives, and why it is an Agent Skill.

## 1. Why a branch with a gate

The Update Take runs on a branch of its own, one commit per item, its gate last, and main moves to it by fast-forward at the gate's close. So main still moves only at a gate's close, and the gate checks that the Update Take finished. Three other ways were weighed:

- **The first commit of the next Plan Step.** Main stays on the old Kit Version until that step's gate closes, so naming this repo to update in between finds the same Kit Update due again.
- **A Plan Step of its own, for the Update Take alone.** It gives the Update Take an opening, for work the Update Note already orders. The branch keeps the one thing it needs from a Plan Step: the gate.
- **One commit on main,** the rule that main moves only at a gate's close narrowed for the Update Take. The branch keeps that rule whole.

## 2. Why the Kit Update is committed first

The branch's first commit is the Kit Update as it arrived, before anything changes. It records what came, so a mismatch found at item 2 can be shown against it.

## 3. Why item 4 names item 3's commit

A commit cannot hold its own hash. Item 3's commit is the last before the Kit Version is written, and every Kit Copy stands at the new Kit Version there, so it is the *version snapshot*.

## 4. Why an Agent Skill

An Update Take is a whole piece of work between two Plan Steps, not a step inside one. Its moment shows without anything else written: a Kit Update waits in `temp/`, and the human says to take it. An Agent Skill fires on that, and loads nothing into a session that takes none. A step of the Plan Step's opening was weighed: it would wait for how this repo opens a Plan Step to be written, and the Adapted Case for taking a Kit Update must be in the Backend Kit from the first Kit Update on, since it is taken first.
