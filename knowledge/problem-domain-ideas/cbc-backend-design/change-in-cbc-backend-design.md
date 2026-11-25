# Change, in CBC backend design

<!--
What it is: a Problem Domain Idea of the Backend Repos' Problem Domain, CBC backend design, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/change.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it. Where each layer is kept, and what the Backend Kit holds, are knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md's.
What stands on it: the Backend Kit's Adapted Cases for keeping knowledge, under knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/: knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/understanding.md, from §2; knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/understanding.md, from §3.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Where it started: the Backend Repo's parts of how a change travels, knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md §3.1, Change a Kit Copy, and §3.6, Take the Kit Update (ADR-0087). Drafted as the layers of knowledge, in CBC backend design, it held only change, and was renamed (ADR-0088).
Its first source, input and not rules: temp/common-ground/backend-repo-change-simulation.md §3 and §8, each step's Chosen.
-->

This document is Change in the Backend Repos' Problem Domain: how a Backend Repo changes a Kit Copy, and how it takes a Kit Update. What a change is, and the rules every change keeps, are Change's (`knowledge/backbone-ideas/change.md`). Changing a Kit Copy is Change's arrow *fit*, in a Backend Repo (`knowledge/backbone-ideas/change.md` §4, *The arrows*). Where each layer is kept, and what the Backend Kit holds, are the layers of knowledge, in keeping knowledge's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`). The Backend Kit's Adapted Cases for keeping knowledge are written from this document. How a change travels between the repos, both sides, is the Maintainer Repo's own Problem Domain Idea (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3, *How a change travels*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Failure Case | `temp/common-ground/common-ground-problem.md`, *Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `docs/conventions/project-recording/` §2.1, *What a plan is* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Update Note | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Update Take | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## 2. Changing a Kit Copy

**When a Kit Copy changes.** A Kit Copy changes only when the Backend Repo's work shows it does not fit what happened, never ahead. The human decides the Copy Change, the agent proposing. It is made then, with its Change Record. A Copy Change may be edited or reversed later, its Change Record with it. Three other ways were weighed:
- **Changed ahead, for what the agent foresees.** It is a speculation, with nothing that happened behind it.
- **The misfit noted, and the Kit Copy changed at the gate.** It gains nothing by waiting, since a Change Record lets any Copy Change be edited or reversed later. Until the gate, the Kit Copy would say what the Backend Repo no longer does.
- **The Kit Copy left as it is, what the Backend Repo does instead written in its own records.** The Kit Copy then says it for good, and the next agent reads the Kit Copy, not the records.

**Where the Change Record sits.** In a footer of the Kit Copy's Adapted Understanding Text, which is not loaded for work. So the Copy Change and its why land in one diff, and the why cannot lose its Kit Copy. When only an Instruction Text changes, its Change Record goes there too. An Instruction Text with no Adapted Understanding Text, such as the Backend Kit's Defined Terms, carries its Change Record in its own footer.

**What the Change Record holds:**
- what changed, by meaning: the part, and what it says now. When some of the Adapted Case's texts were left as they were, it also says whether they still match the Copy Change (`temp/common-ground/common-ground-problem.md` §4, Failure Case 8);
- what happened, concretely, in the Backend Repo's own words. It is never written to sound general: rewording it is the Maintainer Repo's, after judging;
- which work found it;
- the Backend Repo's proposal, marked as one: its own problem, or one any repo would meet.

**When it is rewritten.** The Change Record says the Copy Change as it stands. A later edit rewrites it, and git keeps the old one.

**The commit.** A Copy Change and its Change Record go in the same commit. A commit that changes a Kit Copy and not its Change Record is stopped there. An Update Take is not a Copy Change, so its commits pass. Work never committed is lost, the Copy Change and its Change Record together.

**At the gate.** The gate of the Backend Repo's Plan Step decides each Copy Change made in the step, now that the whole step is seen: kept, edited or reversed, its Change Record with it. So what reaches main has passed a gate.

## 3. Taking a Kit Update

**When it is taken.** A Kit Update is taken between two of the Backend Repo's Plan Steps, when the next is about to open, never in the middle of one, the agent proposing and the human deciding. Before that step opens, in a fixed order: a Look for Lessons runs to main, and the Backend Repo's Kit Update, when one is due, is made, delivered and taken. Then the step opens on the new Kit Copies, or on the same ones when no Kit Update was due. The human works on one project at a time, so the Backend Repo waits at little cost. A Backend Repo's Plan Step open when the human returns finishes on the old Kit Copies first. Two other ways were weighed:
- **Taken whenever it arrives.** It lands in the middle of a step, which then runs on two sets of rules.
- **Taken at the opening, whatever the Look for Lessons reached.** It takes the Kit Update over Copy Changes not yet judged. The Kit Update answered none of them, and clearing their Change Records loses them before they are judged.

**The check first.** The Update Take checks first, from the Update Note, what the Backend Repo itself can see:
- case 1, its main is still the *settled snapshot* the Update Note names: the Kit Update is taken;
- case 2, anything else: there is no Update Take, and the Backend Repo says so. The human names it to update again, and a new Kit Update replaces the waiting one.

**When the Backend Kit moves on.** The Backend Kit may move after the Kit Update is made. That is no reason to refuse the Kit Update: it is correct, if not the latest, and the next brings the rest.

**What is taken.** The Adapted Case for taking a Kit Update is taken first, on its own, so the rest is taken by the new one (`temp/common-ground/common-ground-problem.md` §4, Failure Case 10). Every Kit Copy is then taken whole, at the new Kit Version. A part the Backend Repo never changed is taken, and work shows whether it fits. A Kit Copy taken whole takes its Change Records away with it. Nothing is lost: main is the *settled snapshot*, so each was read and judged. Kept, a Change Record would say how its Kit Copy differed from the old Backend Kit: after the Update Take some would describe nothing, and none would say how the Kit Copy differs from the new one. The new Kit Version is recorded, with its *version snapshot*: the commit where every Kit Copy stands at it. Both are written in `.claude/kit-version.md`, a file of its own, rewritten at each Update Take, so the Maintainer Repo finds them at one fixed path.

**What a Change Record stands against.** Every Change Record stands against the last Kit Version taken, or birth's, and every Change Record goes at an Update Take. This is confirmed at the first Kit Update to reach a Backend Repo whose Kit Copies have Change Records.

## 4. Its Adapted Cases

The Backend Kit's, in its group for keeping knowledge, each written from this document:
- for changing a Kit Copy, `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/`. It loads when a Kit Copy is touched;
- the gate's part of closing one of the Backend Repo's Plan Steps, *At the gate*, written with how a Backend Repo closes a Plan Step (`TODO.md`, the item that rewrites the Agent Model);
- for taking a Kit Update, `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/`, itself in the Kit Update and taken first.

## 5. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **Finished work under a changed rule:** finished work done under a rule the Kit Update changed may now be wrong. New work follows the new Kit Copy; the Backend Repo lists which Backend Kit changes touch rules its finished work followed, and the human decides. Its trigger: the first Kit Update that changes a rule one of the Backend Repo's finished Plan Steps followed.
2. **Dropping an open step for a Kit Update:** dropping or restarting the Backend Repo's open Plan Step so the Kit Update is taken sooner, when the Kit Update changes a rule the step rests on. Its trigger: the first Kit Update the human wants taken before an open step finishes.
3. **Asking at each opening:** whether each opening of the Backend Repo's Plan Steps asks: was this Backend Repo named to update? Without that question, a Backend Repo nobody names opens each step on the old Kit Copies, and falls further behind each time. Its trigger: the first time one of the Backend Repo's Plan Steps opens on old Kit Copies because nobody named the Backend Repo to update.
