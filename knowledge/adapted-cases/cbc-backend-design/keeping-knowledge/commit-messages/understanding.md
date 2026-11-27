# Commit messages

<!--
What it is: one of the Backend Kit's files, the Adapted Understanding Text of its Adapted Case for commit messages. It says why its Instruction Text is as it is, where only this Adapted Case relies on the reason.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/commit-messages-in-cbc-backend-design.md, kept in the Maintainer Repo. The rules this Adapted Case shares with every repo, and why each is so, are there and in the Backbone Idea it adapts.
What stands on it: its Instruction Text, the commit-messages Agent Skill, delivery/container/.claude/skills/commit-messages/SKILL.md, copied to a Backend Repo's .claude/skills/commit-messages/. It moves beside this text when the exchange is rewritten (PLAN.md, the commit-messages manual's Plan Step, decision C).
Its first source, input and not rules: the commit-messages manual, docs/conventions/commit-messages/README.md, deleted on 2026-11-27, its last state in git at 47007e1b: Why it arrives this way; from What it is for, why the rule is opened at the commit.
It never loads; it is read when its Instruction Text changes.
-->

This text says why commit messages reach this repo's agent as an Agent Skill, and why two other rules sit in it. Each Defined Term here is defined in the Backend Kit's Defined Terms.

## 1. Why an Agent Skill

A rule for writing a commit message binds at one moment: the commit. An Agent Skill is read at that moment, whole, through the Pulled Channel. A rule held in the Entry File reaches the agent through the Ambient Channel, at every task, and binds at none of them. In the repo the rule came from, the subject's limit sat in the Entry File, and 15 of the first 20 commits broke it: present, correct, unfollowed. So the rule is opened at the commit, not read once.

## 2. Why the stop and the `agent` scope sit here

The commit is also the moment two other rules bind at:

- **the `agent` scope:** a commit that touches the agent files touches nothing else;
- **the stop:** the agent stages the commit, shows the diff, and waits for the human's word.

So those sentences live in this Agent Skill, and nowhere else. No Enforcement Gate holds the stop: it is this Agent Skill's sentence, read at the commit.
