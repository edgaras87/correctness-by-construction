# Commit plan: the simulation judges by the layers model

## Summary — the state after all commits

The simulation, `temp/common-ground/system-repo-change-simulation.md`, judges a Change against two layers above an Adapted Case, the Work Domain Idea and the Backbone Idea, where it knew one "project-agnostic text". This is step 1 of TODO's item "Define the Change idea".

What holds after it:

- **Depths are layers.** Each depth names the highest layer it changes. Depth c is two rows, "c, at layer 2" and "c, at layer 1". Depths d and e land at layer 3, or layer 2. Depth f is left with two cases that have no home: several Adapted Cases of one Work Domain but not all, and Adapted Cases across Work Domains but not all.
- **Judge asks two layers above.** Question 4 splits: 4a, true naming no Adapted Case, for layer 2; 4b, true naming no Work Domain, for layer 1. There are 9 verdicts, named by the text that gains the lesson.
- **What follows from a rule already written is defined, by pointer to the general document. A choice of how is an Open item with its trigger,** so practice is not steered by a guess. Four Open items are new or grown: the order of 4a and 4b; how far the survey reaches at layer 1; which texts are checked for a depth-d loss; how a Backbone Idea part is known to fail a whole Work Domain.
- **The row "new text of the System Repo's own, on trial" is gone** from the cases. It is Knowledge on Trial handed back, not a Change, and is named among the sources not yet taken into account.
- **The texts the simulation points at agree with it:** the problem file's lines that the layers make wrong, inside its moving block, and the layers document's §3.2.
- **"project-agnostic" is gone from the simulation's 14 lines,** each changed once, with its meaning.

## Commits

**1. `docs: simulation drops the on-trial row`**
The simulation's §2 loses the row "new text of the System Repo's own, on trial", and a line under its table says why: it is Knowledge on Trial handed back, not a Change (`temp/common-ground/knowledge-layers.md` §2.3). The problem file's *A System Repo's change* names it among the other sources (line 223). A decision settled before this talk, apart from the layers work.

**2. `docs: simulation knows two layers above`**
The simulation's Judge and Act, its depth rows, and its "project-agnostic" lines, by decisions 2 to 8 of the talk:
- §2: the depth rows renamed to "the idea above"; c as two rows; d and e "layer 3, or layer 2"; f shrunk to its two cases with no home; each row's *Differs so far* by the decisions on the survey, depth d and depth e;
- §3, step 1: "never written to sound project-agnostic" becomes "general";
- §5: the questions read against both layers; 4a and 4b, by pointer to the general document's §3.1 and §3.2; the cap example's verdict; the 9 verdicts; step 2's "eight" becomes "nine"; the Open items for the order of 4a and 4b, and for depth d's check;
- §6: the other depths by layer; the survey's set, by pointer to the general document's §3.2 and §2.3; the rewording line, naming no Adapted Case at layer 2 and no Work Domain at layer 1, by pointer to the general document's §3.2, the arrow *lesson*, where the rule for each layer lives; the Open items for the survey at layer 1, and for depth e.

One commit, so each line changes once: the depth rows carry decisions from Judge and Act both.

**3. `docs: problem file's judging follows the layers`**
In the problem file's moving block, only the lines the layers make wrong:
- *Judging a change read back*: question 3 against both layers, its "Maintainer Repo's own" check out of the rule; question 4 as 4a and 4b; "If none holds" as a lesson for its Adapted Case (lines 185 to 192);
- *A project-agnostic lesson*: the bold lead becomes *A lesson for the idea above*; "bound to no project" and "name no project" by layer; the survey by layer (lines 196 to 201);
- *Narrowing, never shrinking*: "wrong for every repo" becomes "wrong for every text built on it" (line 205);
- *What an update sends*: the lesson's name (line 209).

The rename grep runs on the old bold lead. The one pointer at it from Living Text, the simulation's §6, moved in commit 2.

**4. `docs: layers document reads depths as layers`**
The layers document's §3.2: its lead sentence and depth table follow the simulation's rows. Its §4 question 4 is answered there, and leaves the list; questions 5 to 14 become 4 to 13, and the pointers at question 11 follow: the layers document's §2.2 tables, twice, and `TODO.md`, line 276. Question 6, renumbered 5, points at the simulation's Open item for depth d.

**5. `docs: TODO's Change idea, step 1 done`**
The item's step 1 leaves; its ideas done leave; three steps remain.

**6. `docs: Conversation Memory saves step 1's talk`**
`TODO-CONVERSATION-MEMORY.md` §35 gains today's talk, and the item's See names it. The reviewer said save.

## Decisions taken inside this plan

- **The simulation's changes are one commit, not one per part.** A depth row carries decisions from Judge and Act. Split by part, each row would change twice.
- **The problem file follows in its own commit.** Undone alone, it leaves the problem file behind the simulation, as the drafts stand today.
- **The bold lead *A project-agnostic lesson* becomes *A lesson for the idea above*,** after the verdict names of decision 8. One pointer reached it from Living Text, the simulation's §6. It moves in commit 2 to the general document's §3.2, since its line changes there anyway.
- **The cap example's verdict** (simulation §5, line 315) becomes "a lesson for its Work Domain Idea, depth c at layer 2": "any repo with scopes" is a test inside one Work Domain.
- **Removing question 4 renumbers the rest,** as the layers document's §4 rule says it leaves the list. Three pointers follow.
- **The devlog entry is not in the plan.** It comes at the session's end, as each session's does.
