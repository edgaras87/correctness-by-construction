# Visual comparison, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/visual-comparison.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Case for visual comparison.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first sources, input and not rules: the visual-comparison manual, docs/conventions/visual-comparison/README.md: What it is for, its case; The seats; What this does not cover, its first item, the Mermaid trial (PLAN.md, the visual-comparison manual's Plan Step, decisions A to C). The decisions behind them: ADR-0027; ADR-0028.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is visual comparison in the Maintainer Repo's Problem Domain, keeping knowledge: the constraint its pictures hold to, its Mermaid trial, and the case the comparison came from. How the way a structure is shown is chosen is visual comparison's (`knowledge/backbone-ideas/visual-comparison.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Plain text, no build step

The Maintainer Repo is reviewed in the diff. A picture is read on GitHub and in the IDE, beside the text around it, and reviewed in the same diff (ADR-0027). So the Maintainer Repo holds to plain text that renders with no build step, and its notations are Mermaid and Unicode box drawing (`knowledge/backbone-ideas/visual-comparison.md` §6, *The buildable notations*).

**Rules:**

- A picture here is Mermaid or Unicode box drawing, written in the Markdown file it belongs to.

## 3. The Mermaid trial

The Maintainer Repo draws in Mermaid, on trial. Two things end the trial: a picture whose layout must be fought, and a place the repo is read in that shows the source instead of the picture. On either, the repo goes back to box drawing, authored in AsciiFlow (ADR-0027, decision 2).

The trial is this repo's, and is not delivered (ADR-0027, decision 3).

**Rules:**

- Mermaid here is a trial, and ADR-0027 says what ends it.
- The trial is not delivered to a Backend Repo.

## 4. The case of 2026-09-18

On 2026-09-18, two Mermaid dialects failed only when rendered. Each had been chosen as built for the job in hand (ADR-0027, ADR-0028):

- **`block-beta`** lost its arrow labels;
- **`sequenceDiagram`** had to draw the Maintainer Repo's reading of a Backend Repo as an arrow into it. The arrow said the opposite of the rule it was drawn to show: the reading sends the Backend Repo nothing.

The answer that won one requirement that day was a table. A method named for diagrams would have left the table out of the candidates. So the comparison's subject is a question (`knowledge/backbone-ideas/visual-comparison.md` §2, *What a comparison is*). It was written the same day.

## 5. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.
