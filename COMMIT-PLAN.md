# Commit plan: set aside a project's own Changes and Attention Notes

## Summary — the state after all commits

The change simulation, `temp/common-ground/system-repo-change-simulation.md`, follows one pure case: a Change the System Kit takes, depth b. Its rules hold no Attention Note and no putting back. Both stay known: §2 gains a short list, *Known, not ruled*, each entry with what can happen and its trigger. The first is Attention Notes. The second is a Change the System Kit does not take: judged its own, unsound, misread or held. Case D1 goes with it. A Reading reads only main: the look past main is gone, with no entry. The Take keeps its branch and its gate, and the gate checks that the Take finished. Whether the Take still needs a branch at all is an open point in §8. The flow file draws the same, and pictures 1 and 2 are gone. The next step, finishing the flow from Change to Take, then checks rules that hold no guesses.

## Commits

**1. `docs: Conversation Memory §36, set-aside calls`**
Today's talk shaped the item: the four decisions on a Change not taken, the look past main, the Take's gate, and pictures 1 and 2. They are recorded before the work, which follows them.

**2. `docs: temp's flow file drops pictures 1 and 2`**
Closes that TODO item in the same commit. Done first, so no later commit fixes pictures that are going.

**3. `docs: temp's Reading has no look past main`**
§4, step 1's paragraph and its Adapted Case line. Its own decision, removed outright, not set aside. Before commit 4, so commit 4 does not edit it.

**4. `docs: temp sets Attention Notes aside`**
§2's list opens, with the Attention Note as its first entry; the table's Attention Note row leaves. The Attention Note lines leave §3 (the paragraph, the gate's misfit question), §4 (check 2, the case table's column, steps 3 and 4), §7 (a held line's answer comes back as a Record) and §8 (items 5 and 8).

**5. `docs: temp's simulated case becomes depth b`**
The intro, §2's table (row a goes to the list as the second entry, with case D1) and *Change whole*'s depth-a column. §3, step 1's *Today* line on the Copy keeping it. §4's case table loses D1, and case A loses its kept Changes. The flow file's look loses D1.

**6. `docs: temp's Judge runs for depth b`** — provisional
§5's intro and steps 1 and 2 follow depth b. Wording and split are set at its boundary.

**7. `docs: temp's Act runs for depth b`** — provisional
§6, step 1 simulated anew for depth b: what must happen, options, chosen, from case D2's path. Wording and split are set at its boundary.

**8. `docs: temp's Deliver runs for depth b`** — provisional
§7, step 1's depth-a lines follow depth b. Wording and split are set at its boundary.

**9. `docs: temp's Take puts nothing back`** — provisional
§8: no putting back (decision 1), the gate checks the Take finished (decision 3), the branch question in *Open*. Items renumbered, and every reference to them fixed: §4's "item 6", the flow file's item notes. The flow file's *The Take*, D2 and the other cases' gate notes follow. Wording and split are set at its boundary.

**10. `docs: TODO closes setting guesses aside`**
The set-aside item leaves, and its Conversation Memory §36 with it, since a section goes in the commit that works its item (`TODO-CONVERSATION-MEMORY.md`, its header comment). The triggers of the check-3 item and of the "Version it was built from" item named it; both become due now.

## Decisions taken inside this plan

- **The flow file follows in the commit** that changes what it draws, never later, so each commit reverts whole.
- **The problem file is untouched.** The TODO item names only the simulation. "System Kit Attention Note" stays a Defined Term there, and the short-form row stays, since §2's list uses it.
- **The Take's items are renumbered,** not left with a hole at item 4. Commit 9 greps every old item number.
- **The branch question goes into §8's *Open*,** with its trigger, not only into this plan, which goes at the close.
- **§5 to §8 are provisional:** their new text is simulation work, shaped as it is written.
