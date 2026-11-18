# Commit plan: the problem file's manual run

## Summary — the state after all commits

`temp/common-ground/common-ground-problem.md` states the problem in its own words, and keeps no picture of the levels of its own. Where it needs the layers, it points at the layers model (`temp/common-ground/knowledge-layers.md`), the reviewer's option a.

- **Gone:** the old three levels: §2.1's levels table, the "middle level", and the word "project-agnostic", replaced on the reviewer's word of 2026-11-14 by domain-agnostic, the model's Backbone Idea.
- **Moved:** 11 Defined Terms live in the layers documents, and the problem file points at them: 4 in the general document, the kinds of text and Knowledge on Trial; 7 in the Maintainer document, the repos and what travels between them. Project-Agnostic Understanding Text goes.
- **Marked:** §8's middle-level option is marked as taken up by the model, on trial, and §6's doubts are in the model's words.
- **Gained:** the layer axis gets its reading case, the Judge rules reach layer 2, and Failure Case 15 names Work Domains, or each goes to TODO with its why.

What it gives: one home for the layers, and a problem file whose words match the model it points at. Before this plan, commit `aa9e62c` added the fifth Knowledge Axis, the run's first commit.

## Commits

**1. `docs: temp's problem names a layer reading case`** (provisional)
§4: the grid's empty cell, reading × layer, gets its Failure Case, numbered 25, and the cell names it. The wording is the reviewer's, drafted at this boundary. It comes first because `aa9e62c` left the cell empty, and §4's rule calls that a missing Failure Case.

**2. `docs: temp's problem points at the layers model`**
§2.1: the levels table and its two sentences around it, "Between understanding and instruction…" to "…checked in the next step", go. One sentence points at the layers model's §2. §3.5 is already the pointer, so §2.1 may point there instead. This is the second old copy of the levels after §3.3's, and it goes before the words change, so nothing is swept twice.

**3a. `docs: temp's general layers define text kinds`**
Four Defined Terms move from the problem file into `temp/common-ground/knowledge-layers-general.md`, each bold at its home there: Understanding Text and Instruction Text (§2), Adapted Understanding Text (§2.3, the understanding text of an Adapted Case: why its Instruction Texts are as they are), and Knowledge on Trial (§3). The general document's line "The model uses the Common Ground Problem's Defined Terms" goes, so it no longer leans down on the problem file (found item 2's last fault).

In the problem file:
- the four entries, and Adapted Case's, become pointers to the general document;
- Project-Agnostic Understanding Text goes, its two uses becoming "the text above an Adapted Case, a Work Domain Idea or a Backbone Idea";
- *Defined Terms*' lead says the layers model's Names are defined there;
- §2.2's table follows: its Project-Agnostic row names the Backbone Idea and Work Domain Idea, and its Adapted Understanding Text row keeps only "a convention manual".

`temp/common-ground/system-repo-change-simulation.md` line 342 follows. Every other file that points at the problem file's Defined Terms for one of these terms is found by grep, and follows in this commit.

**3b. `docs: temp's Maintainer layers define the repos`**
Seven Defined Terms move from the problem file into `temp/common-ground/knowledge-layers.md`, each bold at its home there: Maintainer Repo, System Repo, System Kit, System Kit Copy, System Kit Copy Change, System Kit Update and System Kit Version. Its line "The model uses the Common Ground Problem's Defined Terms" names only the terms still borrowed. The problem file's seven entries become pointers. Every other file that points at the problem file's Defined Terms for one of these follows, by grep.

Both commits come before the sweep, because the sweep uses their words. The general document's commit comes first, since the Maintainer document points up at it.

**4. `docs: temp's problem drops project-agnostic`** (provisional)
Every remaining "project-agnostic", about 20, takes commits 3a and 3b's words, and so does §2.2's "the middle level for one way of working", line 246:
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

- **Scope is the problem file, and the Defined Terms the two layers documents own.** Revised at commit 3: the 11 terms that describe the layers, or how knowledge travels between the repos, move into the layers documents, which ends the models' pointers down into the problem file (finding 10). The general document's other faults (found item 2) are the next plan. The 21 terms that stay are the problem's own words, the change work's detail, which has no home yet, and the three sorts of Instruction Text, which wait for the Agent Model's rewrite.
- **"Step by step"** (§2.1) stays. Its fix waits on a name for the movement, the Maintainer document's §4 question 3.
- **No records commit.** The devlog entry comes at the session's end. The TODO gains a line only if commit 6 sends the Judge rule there, and that line is commit 6.
- **Commits 1, 4, 6 and 7 are provisional:** each one's wording or outcome is the reviewer's, at its boundary.
