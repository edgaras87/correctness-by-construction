# Judge Copy Changes, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Judge Copy Changes and Act on the verdicts, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md §3.3, Judge Copy Changes, and §3.4, Act on the verdicts, the parts it is written from. It adapts that text, and never retells it.
What stands on it: .claude/skills/judge-copy-changes/SKILL.md, its Instruction Text, an Agent Skill.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Why it carries no Foundation Line: docs/conventions/conventions/ §1.3, The Foundation Line.
Its first source, input and not rules: temp/common-ground/backend-repo-change-simulation.md §5, Judge Copy Changes, and §6, Act on the verdicts, each step's Chosen.
-->

This text says why the Maintainer Repo judges a Repo Reading, and acts on its verdicts, the way its Agent Skill does. Who judges, what a verdict holds, what each depth asks, and why, are in Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.3, *Judge Copy Changes*; §3.4, *Act on the verdicts*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Failure Case | `temp/common-ground/common-ground-problem.md`, *Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `docs/conventions/project-recording/` §2.1, *What a plan is* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Repo Reading | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## 2. Judge and Act in one Adapted Case

Act on the verdicts runs right after the human decides the verdicts, in the same pass over one Backend Repo. What each depth asks, the survey, the rewording and the stop moving are layer 2's, since other parts rely on them. Act's own steps are few. So one Adapted Case holds both, and one Agent Skill runs them in order.

## 3. Question 0 first

A Copy Change that does not fix what happened, or breaks something its Kit Copy did, goes nowhere. Asking how deep it goes before asking whether it is sound would weigh a change that is then dropped. So soundness is asked first, and an unsound line is asked nothing more.

## 4. The four questions, in order

They run from the cheapest check to the dearest, and stop at the first that holds:

1. **Did the Kit Copy already say this?** It needs only the original part beside the Copy Change. When it holds, the Backend Repo misread its Kit Copy (Failure Case 7), and nothing new is made. The Backend Kit as it is now is read too, so a lesson it has since made the same way is not made twice.
2. **Is it specific to that Backend Repo's problem?** It needs what happened, and the Backend Repo's own framing. When it holds, nothing leaves the Backend Repo.
3. **Does the idea above already hold it?** Then the Adapted Case lost the part in narrowing, and the fix comes from the idea above, not from a new lesson. A part lost has no mark, and one left out on purpose has its mark (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**, *Narrowing, never shrinking*), so the two are told apart.
4. **How high is it true?** It reads across texts, the dearest check, so it comes last. A lesson goes as high as it is true (`knowledge/backbone-ideas/change.md` §3, *How the layers fill*). How it is answered is open (§8).

## 5. From the reason, never the wording

The depth comes from the reason, never the edit. A cap raised from 50 to 60 is the Backend Repo's own, depth a, when its reason is "our scope names are long". The same edit is a lesson for its Problem Domain Idea, depth c at layer 2, when its reason is "the cap counts the scope, which any repo with scopes meets". A Copy Change worded for one project may still be a lesson for every repo: the Backend Repo writes in its own words on purpose (Change, in keeping knowledge, §3.1, *Change a Kit Copy*), and making a lesson general is rewording, after judging (Change, in keeping knowledge, §3.4).

## 6. A line with no Change Record

Its why is looked for in the Backend Repo first, in the commit that made the Copy Change and in the Backend Repo's records, then asked of the human. Two other ways were weighed:

- **Judged from the comparison alone.** It judges on a guess at the why (Failure Case 22).
- **Held until the human brings its why.** It asks the human for what the Backend Repo may already have written.

## 7. Lines together, lines split

Lines under one reason are judged together, and the reason once: judged apart, one reason could get two verdicts. A line whose parts answer differently is split, since one verdict holds one answer. The parts keep their one Change Record.

## 8. Open

- How question 4 is answered, and by whom. A first guess, not a rule: 4a first, and 4b only if 4a holds. 4a is the cheaper check, inside one Problem Domain, and a lesson still true naming no Problem Domain is true across its own. Its trigger: depth c checked against these rules (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it"), or the first lesson judged at layer 1.
- Whether an unsound verdict offers a fix. Its trigger: the first unsound verdict.
- Whether a Look for Lessons is one of the Maintainer Repo's Plan Steps. It is a question of how the Maintainer Repo's agent shapes its work, and that idea is not yet written. Its trigger: How an agent works, in keeping knowledge, written (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.1, *Keeping knowledge*).
