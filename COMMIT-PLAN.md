# Commit plan: the problem file's manual run

## Summary — the state after all commits

`temp/common-ground/common-ground-problem.md` states the problem in its own words, and keeps no picture of the levels of its own. Where it needs the layers, it points at the layers model (`temp/common-ground/knowledge-layers.md`), the reviewer's option a.

- **Gone:** the old three levels: §2.1's levels table, the "middle level", and the word "project-agnostic", replaced on the reviewer's word of 2026-11-14 by domain-agnostic, the model's Backbone Idea.
- **Changed:** the three Defined Terms that carried the old levels point at the model's Names, or go.
- **Marked:** §8's middle-level option is marked as taken up by the model, on trial, and §6's doubts are in the model's words.
- **Gained:** the layer axis gets its reading case, the Judge rules reach layer 2, and Failure Case 15 names Work Domains, or each goes to TODO with its why.

What it gives: one home for the layers, and a problem file whose words match the model it points at. Before this plan, commit `aa9e62c` added the fifth Knowledge Axis, the run's first commit.

## Commits

**1. `docs: temp's problem names a layer reading case`** (provisional)
§4: the grid's empty cell, reading × layer, gets its Failure Case, numbered 25, and the cell names it. The wording is the reviewer's, drafted at this boundary. It comes first because `aa9e62c` left the cell empty, and §4's rule calls that a missing Failure Case.

**2. `docs: temp's problem points at the layers model`**
§2.1: the levels table and its two sentences around it, "Between understanding and instruction…" to "…checked in the next step", go. One sentence points at the layers model's §2. §3.5 is already the pointer, so §2.1 may point there instead. This is the second old copy of the levels after §3.3's, and it goes before the words change, so nothing is swept twice.

**3. `docs: temp's problem Defined Terms follow layers`** (provisional)
*Defined Terms*: Project-Agnostic Understanding Text, Adapted Understanding Text and Adapted Case each point at the model's Name, or go. §2.2's table rows for them follow. Which point and which go is decided at this boundary, one term at a time. It comes before the sweep, because the sweep uses the words chosen here.

**4. `docs: temp's problem drops project-agnostic`** (provisional)
Every remaining "project-agnostic", about 20, takes commit 3's words:
- the Repo Responsibility's items 1, 2 and 4, with item 7's stray full stop;
- the Judge questions 3 and 4;
- *A project-agnostic lesson* and *Narrowing, never shrinking*;
- Failure Cases 23 and 24;
- §2.1's opening and *What the System Kit holds*.

§6 and §8 are left to commit 5. Counted by grep before and after. If it runs past about 30 changed lines, it splits by section, and the plan is revised.

**5. `docs: temp's problem options meet the model`**
- **§8:** the option "keep a middle level…" and its table are marked as taken up by the layers model, on trial, and stay listed. The header says the file chooses no answer.
- **§6:** the two "middle level" doubts are reworded in the model's words. They stay doubts.

**6. `docs: temp's Judge rules reach layer 2`** (provisional)
§2.1, *Judging a change read back*: a lesson shared by the Adapted Cases of one Work Domain goes to its Work Domain Idea, the model's depth f. It may instead go to TODO, for the change work, as the simulation's rules come from it. Decided at this boundary. If so, the commit is a TODO line.

**7. `docs: temp's Failure Case 15 names Work Domains`** (provisional)
§4: Failure Case 15, "one understanding text serves repos whose needs differ", is sharpened to one text serving two Work Domains, and §2.2's example points at it. It may stand as it is, decided at this boundary.

## Decisions taken inside this plan

- **Scope is the problem file only.** The models' pointers down into its Defined Terms, and the general document's own faults (found item 2), are the next plan, though the run's order put found item 2 "with it". They touch other files, and finding 10 needs the Defined Terms settled first, by commit 3.
- **"Step by step"** (§2.1) stays. Its fix waits on a name for the movement, the Maintainer document's §4 question 3.
- **No records commit.** The devlog entry comes at the session's end. The TODO gains a line only if commit 6 sends the Judge rule there, and that line is commit 6.
- **Commits 1, 3, 4, 6 and 7 are provisional:** each one's wording or outcome is the reviewer's, at its boundary.
