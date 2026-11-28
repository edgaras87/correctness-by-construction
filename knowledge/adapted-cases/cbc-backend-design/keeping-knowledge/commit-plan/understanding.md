# Commit sets

<!--
What it is: one of the Backend Kit's files, the Adapted Understanding Text of its Adapted Case for commit sets. It says why its Instruction Text is as it is, where only this Adapted Case relies on the reason.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/commit-sets-in-cbc-backend-design.md, kept in the Maintainer Repo. The rules this Adapted Case shares with every repo, and why each is so, are there and in the Backbone Idea it adapts.
What stands on it: its Instruction Text, the commit-plan Agent Skill, delivery/container/.claude/skills/commit-plan/SKILL.md, copied to a Backend Repo's .claude/skills/commit-plan/. It moves beside this text when the exchange is rewritten, as the commit-messages Agent Skill does (devlog 2026-11-27, evening, the commit-messages manual's Plan Step, decision C).
Its first source, input and not rules: the commit-plan manual, docs/conventions/commit-plan/README.md: Why it arrives this way.
It never loads; it is read when its Instruction Text changes.
-->

This text says why commit sets reach this repo's agent as an Agent Skill, and why the stop at each commit is not in it. Each Defined Term here is defined in the Backend Kit's Defined Terms.

## 1. Why an Agent Skill

A Commit Plan is needed at one moment: work turns out to need more than one commit. The agent knows the moment by the work in front of it. An Agent Skill is read at that moment, whole, through the Pulled Channel.

Nothing else would bring it up then. Nothing in a record puts the Commit Plan in front of the agent when the work turns out larger.

## 2. Why the stop is not here

The stop at each commit must hold at every commit. An Agent Skill read only for work of more than one commit cannot carry it. So the stop is the commit-messages Agent Skill's, read at every commit.
