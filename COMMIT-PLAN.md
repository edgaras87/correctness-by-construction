# Commit plan: every part runs, with its output

## Summary — the state after all commits

The Maintainer Repo's four parts of Change form a chain, and each runs at every look, even with nothing to do. Read always gives the stop, main's commit written first, and a list of what changed since the settled snapshot, possibly empty. Judge always gives a verdict per line, possibly none. Act on the verdicts does what each verdict asks, then always sets the settled snapshot to the stop. Deliver gives an Update when one is due. So the settled snapshot moves in one place only, Act, and case C is Read finding an empty list, not the look moving the settled snapshot itself. Each case picture in the flow file shows every part's output, empty or not.

## Commits

**1. `docs(agent): add commit plan for part outputs`**
This plan, agreed before any of the work.

**2. `docs: temp's parts always run, Act sets snapshot`**
The simulation, as one change, since a part changed alone leaves the others contradicting it:
- §4, step 1: the case table's *What follows* for C1 and C2 says Read's list is empty and Act moves the settled snapshot to main, not the look;
- §4, step 2: *Where it stops* writes the stop at every look, not only as an open Reading's first line; *When the stop moves* says Act always sets the settled snapshot to the stop, whether or not anything was read; its Adapted Case follows;
- §4, step 4: the list may be empty, and an empty list needs no draft;
- §5, step 1: Judge runs on any list; an empty one gives no verdicts;
- §6, step 1: Act always ends by setting the settled snapshot to the stop; with no verdicts, that is all it does. Its Adapted Case follows.

**3. `docs: temp's cases show each part's output`**
The flow file follows the simulation: each case's now part gives Read's stop and list, Judge's verdicts and Act's setting of the settled snapshot, empty or not. C1 and C2's line "the settled snapshot moves up to c3, with no Reading" moves from Read to Act. The look chart's case C box says the same.

**4. `docs(agent): close commit plan for part outputs`**
Deletes this file. Before it, a grep for every phrase that has the look, or anything but Act, move the settled snapshot, across `temp/common-ground/` and TODO, unwrapped. The body records what diverged.

## Decisions taken inside this plan

- **The simulation first, the pictures after,** as for every finding today: the flow file draws the simulation.
- **One commit for the simulation.** Read, Judge and Act each change a little; any one alone contradicts the rest.
- **An empty list needs no draft.** The Defined Term System Repo Reading, "and the draft that lists what it found", stands: with nothing found, there is nothing to list.
- **In case A, Act sets the settled snapshot to the stop it already is.** It changes nothing, and keeps one rule.
- **Not in this plan:** moving check 3, "is an Update due?", from the look into Deliver for every case. It is the next question, decided after this plan closes.
