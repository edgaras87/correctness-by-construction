# Commit plan: the look defined, as the Look for Lessons

## Summary — the state after all commits

The Maintainer Repo's pass over one System Repo has a Name, the Look for Lessons, written in full every time, with no short form. It is defined once, in `temp/common-ground/system-repo-change-simulation.md` §1, under the parts table: it runs through Read Changes, Judge and Act; it starts when the human names a System Repo, for its lessons or to update it; it ends when Act sets the *settled snapshot* to the stop. Deliver and the Take are outside it. The problem file's Defined Terms list it, pointing there. §4, step 1 keeps the two checks and the three cases, and points at §1 for what a Look for Lessons is.

The part Read is renamed Read Changes. The Defined Term System Repo Reading means only the list Read Changes writes. In the simulation and the flow file, each sentence that says "look", "read" or "Reading" says what it means: the whole pass, the part, or the list. The TODO item "Define the look" is gone.

## Commits

**1. `docs: temp renames the Read part Read Changes`**
A rename alone, first, so commit 2 is written in the final words and the rename grep has one commit to check. The simulation's §4 title, its parts table, the *Change whole* picture and the lines that say "Read's"; the flow file's prose and the five case pictures' "Read (§4)" labels, widths kept.

**2. `docs: temp defines the Look for Lessons` (provisional)**
The Name, its home, and the meaning of each read word. The problem file's Defined Terms gain Look for Lessons, pointing at the simulation's §1, and System Repo Reading narrows to the list Read Changes writes. §1 gains its paragraph under the parts table, taken from §4, step 1's "A look is reading for lessons…" lines, which go. Two bold leads change, and every citation of them: *A look at main* becomes *Two checks at main*; *The first look after a Take* becomes *The first Look for Lessons after a Take*. Then every sentence in the simulation and the flow file that holds "look", "read", "reads", "reading" or "Reading" is read for what it claims, and rewritten where it claims the wrong thing, never only swapped. Each line changes once. At staging, each rewritten sentence is shown old beside new. Provisional: which sentences change is known only once each is read.

**3. `docs: TODO drops the item on defining the look`**
The item is done by commits 1 and 2.

## Decisions taken inside this plan

- **The home is §1, under the parts table:** the Look for Lessons groups three of the parts listed there. §4, step 1 held it inside one step of one part.
- **The problem file lists the Name, pointing at the simulation,** as it does for System Kit Update Take.
- ***A look at main* becomes *Two checks at main*:** with the definition gone to §1, it holds only the two checks and the three cases.
- **Each sentence is read for its meaning, not swapped:** a word replaced across files gets each changed sentence re-read for what it now claims (`.claude/rules/foundation-check.md`, *A moved section*).
- **Only sentences with a read word are rewritten:** a wider rewrite of the parts waits for the "Define the Change idea" item's second step, one home for each fact across the drafts, which rewrites these drafts anyway.
- **The verb stays English:** "the human has the Maintainer Repo look at it" is not the Name.
- **The case name *Change read* stays:** the reviewer's, of 2026-11-22. Its "read" is the Read Changes part's.
- **The flow file's case pictures take the new words now,** though they are redrawn next: the rename grep fixes every line that points at an old name.
- **Left as they are:** the frozen `temp/common-ground/between-repos-simulation.md`, and the old pictures file, not kept in step.
