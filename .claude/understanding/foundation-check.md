# The Foundation Check, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for the check at the commit, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is, where only this repo relies on the reason.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md, the Problem Domain Idea it is written from: §4, The Change Walk, and §5, Where a disagreement is raised. It adapts that text, and never retells it.
What stands on it: its Instruction Text, the Foundation Check Agent Rule, .claude/rules/foundation-check.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: the facts-in-sync manual, docs/conventions/facts-in-sync/README.md, deleted on 2026-11-27, its last state in git at 0f525a7d: §4's last paragraph, what the check makes this repo do; Why it arrives this way, its half for the check; the check's header comment, at 643c2bd6; and PLAN.md, the facts-in-sync manual's Plan Step, decision B.
-->

This text says why the Foundation Check acts at the commit, why it loads in every session, and what it stands for while the layers model has no form of its own for it.

## 1. Its Defined Terms

- **Foundation Check:** this repo's check before a commit is staged: on a changed text others stand on, it runs the Change Walk, and lists each disagreement it finds for the human to decide.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Agent Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Ambient Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Change Walk | `knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Foundation Line | `docs/conventions/conventions/` §1.3, *The Foundation Line* |
| Paths Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |

## 2. Why at the commit

The Change Walk and the settling of a disagreement were once only written down, and had to be remembered. The commit is where a change to a text others stand on is whole and not yet kept: a disagreement found there is settled in the same commit, or in the next. The searches can be checked by their tokens, a path or a Foundation Line's value. The re-reads and the decisions cannot. So the check makes the agent do them before every such commit.

## 3. Why every session

Its moment is every commit that touches a text others stand on, and any task may make one. A Paths Rule loads only when a file under its paths is touched with the agent's tools, and an edit made by script loads nothing (`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md` §6, *Paths Rules*). So it is an Agent Rule with no `paths:` list, through the Ambient Channel (`knowledge/backbone-ideas/how-an-agent-works.md` §7, *Choosing a channel*).

## 4. What it stands for

The check finds the texts others stand on by today's marks: the folders it lists, and the Foundation Line. A text of the layers carries no Foundation Line, and lists what stands on it in its header instead (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §4, *The Change Walk*).

Its step 3 is, for this repo's own change, what Change asks before an idea above changes: that every text built on it is asked whether it still fits (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.4, *Act on the verdicts*). That change, depth c, has never been walked through. So the check stands as it works, its steps unchanged but for their pointers (PLAN.md, the facts-in-sync manual's Plan Step, decision B).

## 5. Open questions

1. **What replaces it in the layers model.** Its trigger is that of `TODO.md`'s item "Simulate depth c, then bring the Change idea to it".
