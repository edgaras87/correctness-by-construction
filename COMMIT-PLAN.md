# Commit plan: the look defined, as the Look for Lessons

## Summary — the state after all commits

The Maintainer Repo's pass over one System Repo has a Name, the Look for Lessons, written in full every time, with no short form. It is defined once, in `temp/common-ground/system-repo-change-simulation.md` §1, under the parts table: it runs through Read Changes, Judge and Act; it starts when the human names the System Repo to read or to update; it ends when Act sets the *settled snapshot* to the stop. Deliver and the Take are outside it. The problem file's Defined Terms list it, pointing there. §4, step 1 keeps the two checks and the three cases, and points at §1 for what a Look for Lessons is.

The part Read is renamed Read Changes. The Defined Term System Repo Reading means only the list Read Changes writes. In the simulation and the flow file, "read" and "Reading" mean Read Changes or its list; where they meant the whole pass, they say Look for Lessons. The TODO item "Define the look" is gone.

## Commits

**1. `docs: temp defines the Look for Lessons`**
The Name and its home. The problem file's Defined Terms gain Look for Lessons, pointing at the simulation's §1. §1 gains its paragraph under the parts table, taken from §4, step 1's "A look is reading for lessons…" lines, which go. Every "look" that names the pass becomes "Look for Lessons": in the simulation, and in the flow file's prose, flowchart and pictures, the pictures' column widths kept. Two bold leads change, and every citation of them: *A look at main* becomes *Two checks at main*; *The first look after a Take* becomes *The first Look for Lessons after a Take*.

**2. `docs: temp renames the Read part Read Changes`**
A rename of its own, so the rename grep has one commit to check. The simulation's §4 title, its parts table, the *Change whole* picture and the lines that say "Read's"; the flow file's prose and the five case pictures' "Read (§4)" labels, widths kept.

**3. `docs: temp's read words mean Read Changes` (provisional)**
The Defined Term System Repo Reading narrows to the list Read Changes writes. Every "Reading", "read", "reads" and "reading" in the simulation and the flow file is read in its sentence: 80 and 113 uses, counted by script. Where one means the whole pass, it becomes Look for Lessons, or the sentence is rewritten. Provisional: which lines change is known only once each is read.

**4. `docs: TODO drops the item on defining the look`**
The item is done by commits 1 to 3.

## Decisions taken inside this plan

- **The home is §1, under the parts table:** the Look for Lessons groups three of the parts listed there. §4, step 1 held it inside one step of one part.
- **The problem file lists the Name, pointing at the simulation,** as it does for System Kit Update Take.
- ***A look at main* becomes *Two checks at main*:** with the definition gone to §1, it holds only the two checks and the three cases.
- **The verb stays English:** "the human has the Maintainer Repo look at it" is not the Name.
- **The case name *Change read* stays:** the reviewer's, of 2026-11-22. Its "read" is the Read Changes part's.
- **The flow file's case pictures take the new words now,** though they are redrawn next: the rename grep fixes every line that points at an old name.
- **Left as they are:** the frozen `temp/common-ground/between-repos-simulation.md`, and the old pictures file, not kept in step.
