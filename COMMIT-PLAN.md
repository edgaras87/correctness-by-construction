# Commit plan: *Narrowing, never shrinking* moves to its home

## Summary — the state after all commits

*Narrowing, never shrinking* is a rule of the general layers document, `temp/common-ground/knowledge-layers-general.md`, in a **Rules** paragraph that closes its §3.2, *The arrows*. The problem file no longer holds it, and nothing points at the problem file for it. The general document points at no draft below it.

The general document keeps its own header's trial: each section's rules close it in a **Rules** paragraph. §3.2's arrows describe the arrows, and its rules stand in its **Rules** paragraph. §3.1 no longer repeats the arrow *adapt*.

Its open question 3, where a skipped part is marked, is answered by the rule and leaves the list.

What it gives us: the Change idea's move, next, points at the rule's real home from the start, and none of its new lines changes again for this.

## Commits

**1. `docs(agent): add commit plan for narrowing`**
This plan.

**2. `docs: temp's general layers holds narrowing`**
The rule moves, and everything that points at it follows, in one commit, so no pointer is ever left at a home that is gone:
- the general document's §3.2 gains a **Rules** paragraph, holding *Narrowing, never shrinking*, written for any Work Domain: no Failure Case, no Judge;
- the arrow *adapt*'s "a part left out on purpose is marked, with why" points at that rule, not at the problem file;
- open question 3 is answered by it, and leaves the list; questions 4 to 7 become 3 to 6, and the three pointers at them follow: the problem file's §3 table (6 to 5), the layers document's §4 question 2 (6 to 5), the simulation's §5, step 1, *Open* (7 to 6);
- the problem file's *Narrowing an idea* block goes;
- its one Change sentence, that Judge's question 3 tells a part lost in narrowing, with no mark, from one left out on purpose, with its mark, lands in the simulation, §5, step 1, *What each question reads*, question 3;
- the simulation's §2 row e points at the general document;
- the layers TODO item's idea on question 3 goes, since the question is answered.

**3. `docs: temp's general §3.2 gathers its rules`**
§3.2's other rules move from the arrow list into its **Rules** paragraph, so the arrows only describe. Its own commit, since it changes how §3.2 is laid out, not where a fact lives. The sentences, as read now:
- *adapt:* "When the idea above changes, each text built on it is checked, and changes if it must";
- *lesson:* "It is reworded to name no Adapted Case at layer 2, and no Work Domain at layer 1".

What the commit finds else, it lists in the diff for the reviewer; nothing more moves without the word.

**4. `docs: temp's general §3.1 drops a repeat`**
§3.1's rule "Once a higher text is written, a change to it spreads down, to each text built on it" repeats the arrow *adapt*'s rule, which commit 3 puts in §3.2's **Rules**. One goes: §3.1's, since §3.2's says more: each text is checked, and changes only if it must.

**5. `docs(agent): close commit plan for narrowing`**
Deletes this file. Before it: the rename grep for "Narrowing an idea", the problem file's old place of the rule, and the general document's question numbers 3 to 7, unwrapped; and the look back.

## Decisions taken inside this plan

- **The rule's home is §3.2, not §2.2 or §3.1.** It is a rule of the arrow *adapt*: what is marked, and where, when an idea is adapted. §3.2 is where the arrow is.
- **Failure Case 11 and Judge are left out of the general document.** Its header gives no example from one Work Domain's work, and it points at no draft below it. The Judge sentence is a fact of Change, so it goes to Change's home for now, the simulation, and moves with the rest of Change.
- **The problem file keeps no pointer for the rule.** After commit 2 nothing in it uses the rule, and its §3.5 already points at the layers model for the layers.
- **Question 3 leaves the list and the rest renumber,** as the general document's §4 says of an answered question. Three pointers follow in the same commit.
- **Commits 3 and 4 are the general document's other two faults** found on 2026-11-18, checked again today: both still stand. A third, "it leans on the problem file's Defined Terms", no longer stands; once commit 2 lands it points at the problem file nowhere.
