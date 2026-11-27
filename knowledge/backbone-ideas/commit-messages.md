# Commit messages

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules: the commit-messages manual, docs/conventions/commit-messages/README.md, deleted on 2026-11-27, its last state in git at 47007e1b: its opening; What it is for; §1; §2; and from the commit-messages Agent Skill, .claude/skills/commit-messages/SKILL.md, its Rules: one logical change per commit, no placeholder subjects on a shared branch. The decisions behind them: ADR-0038, 1a, 1c and 1f; ADR-0049, 5; ADR-0083.
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- It names no file that carries its rules to the agent: that is each Adapted Case's.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says how a commit is written: its message, what may share one, and who commits it. It names no Problem Domain: each Problem Domain Idea adapted from it says what its own repos' commits carry.

Its neighbours: which files are agent files is agent files' (`knowledge/backbone-ideas/agent-files.md` §3, *The agent files*); what a decision record is, and the other records a footer links, are records' (`knowledge/backbone-ideas/records.md` §3, *The records*); work of more than one commit is the commit-plan manual's (`docs/conventions/commit-plan/`).

## 1. Its Defined Terms

None of its own.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Enforcement Gate | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. What a commit message is

A commit message has three parts:

- the subject, one line: what the commit changes;
- the body: why;
- the footers: links to the trail, such as the decision or the backlog item behind it.

The body is the part history cannot rebuild. The diff shows what changed. It does not show the reason, the alternative rejected, or the constraint that makes a strange line right. A good body does for a small change what a decision record does for a large one.

**Rules:**

- The subject makes sense alone, in a log of one line per commit.
- The body says why, and what the diff cannot: alternatives rejected, constraints not obvious.
- A reason too small for a decision record, but worth keeping, is written in the body.
- A body line is wrapped at 72 characters.
- A commit that carries out a decision links it in a footer. One that resolves a backlog item names it.

## 3. The subject

A subject is typed, in the Conventional Commits format: `<type>(<scope>): <description>`. The type, such as `feat`, `fix` or `docs`, says what kind of change it is. So a log of one line per commit reads as an index of the history, and a release tool can derive the next version from the types. The scope, where one is given, names the area the commit touches.

The subject says what the commit changes, in the present tense. Either mood will do. A change to the work reads as a command: "rename the config file". A record reads as what became true: "the backlog holds the question". "Renamed the file" fails: it reports the author, not the repo.

The subject is short, and two numbers serve two readers:

- **50 characters, the writer's aim.** The writer is shown only this number. A larger number, once seen, becomes room to spare.
- **70 characters, a check's line.** A check that counts subjects passes one up to 70. Past 70, the human decides whether it is rewritten. Nothing breaks below 72: GitHub cuts a subject past 72, and 70 characters with the hash fit an 80-column terminal. So a miss of a few characters is not worth a reword.

Where a repo runs that check is its own, and each Problem Domain Idea says.

**Rules:**

- A subject is typed, `<type>(<scope>): <description>`, in the present tense, with no period.
- A breaking change is marked `!` after the type, and explained in a footer.
- The writer aims at 50 characters, and is shown no other number.
- A check that counts subjects passes one up to 70. One past 70 is the human's to keep or rewrite.

## 4. What shares a commit

One commit is one logical change. "Fix X, update the dependencies and rename a file" is three commits.

A repo worked by an agent has two histories in one: the work, and the agent files that made the agent do it a particular way. They stay separable only if no commit straddles them. Then a log can be filtered of the agent files, and a copy of the repo can drop them, without rewriting history. So a commit that touches agent files touches nothing else, and its scope says so.

**Rules:**

- One logical change per commit.
- A commit that touches agent files touches nothing else, and is scoped `agent`.
- A shared branch holds no placeholder subjects, such as `wip`: they are squashed first. A private branch may hold them.

## 5. Commit on the word

When an agent commits, the commit is the one place where a wrong assumption is cheap to catch. So the agent stages the commit, shows the human the diff, and waits for the word. No Enforcement Gate holds this: the rule is text, read at the commit.

**Rules:**

- The agent commits only on the human's word, one commit at a time.
- It pushes only on the same word.

## 6. Open questions

A question joins this list when work meets one, and leaves it once its answer is in the text above.

1. **Whether a single commit's subject is counted when it is written.** A check counts subjects after they are written, so a subject past 70 is found late. Its trigger: the 5th subject past 70 a check finds (`TODO.md`, the item "Decide whether a single commit's subject is counted by script when it is written").
2. **How the stop at each commit sits with the operator's settings.** Agent files counts how often the agent stops for review as a setting (`knowledge/backbone-ideas/agent-files.md` §10, *The operator's file*); §5 makes the stop a rule. Its trigger: the rewrite done (`TODO.md`, the item "Decide how work is run by agents").
