---
paths:
  - ".claude/rules/**"
  - ".claude/skills/**"
  - ".claude/understanding/**"
---

<!-- One of the Backend Kit's files: the Instruction Text of its Adapted Case for changing a Kit Copy, a Paths Rule. Why it is as it is: .claude/understanding/change-a-kit-copy.md. -->

# Change a Kit Copy

This rule governs every change to a Kit Copy. A file under these paths is a Kit Copy when its header names it one of the Backend Kit's files. This repo's own texts are not, and this rule does not govern them. Each Defined Term here is defined in the Backend Kit's Defined Terms.

## The rules

1. **Change a Kit Copy only when the work shows it does not fit what happened.** Never ahead, for what you foresee.
2. **Propose it; the human decides.** Make the Copy Change only on the human's word.
3. **Write its Change Record with it,** in a footer of the Kit Copy's Adapted Understanding Text. When only an Instruction Text changes, its Change Record goes there too. An Instruction Text with no Adapted Understanding Text carries its Change Record in its own footer.
4. **The Change Record holds:**
   - what changed, by meaning: the part, and what it says now. When some of the Adapted Case's texts were left as they were, whether they still match the Copy Change;
   - what happened, concretely, in this repo's own words, never written to sound general;
   - which work found it;
   - your proposal, marked as one: this repo's own problem, or one any repo would meet.
5. **Commit the Copy Change and its Change Record together.** Never commit a change to a Kit Copy without its Change Record. An Update Take is not a Copy Change, so its commits pass.
6. **Edit or reverse a Copy Change the same way.** Rewrite its Change Record to say the Copy Change as it stands; git keeps the old one.
7. **The gate of the Plan Step decides each Copy Change made in it:** kept, edited or reversed, its Change Record with it.
