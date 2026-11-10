# A System Repo's Change, Simulated

<!-- A draft for the Plan Step "Find how what we know stays true",
     stage 1. It simulates one case of temp/common-ground-problem.md,
     *A System Repo's change*, step by step, until that draft's rules
     can be written from it: *Recording and reading* first, then
     *Deciding and updating*. The rules live there, never here. Its
     input: the frozen temp/between-repos-simulation.md, scenarios 2
     and 3. It goes when the Plan Step closes, and git keeps every
     version. -->

This document simulates one case: a System Repo changes both halves of one Adapted Case in its System Kit Copies, and the Maintainer Repo reads the change back. It uses the Common Ground Problem's Defined Terms (`temp/common-ground-problem.md`, *Defined Terms*).

The scope: the two halves are the Instruction Text and its Adapted Understanding Text. The change may have any reason, its own or one any repo would meet. Either half may change first. One stretch of work may hold several such changes. Each step's choice must hold for all of it, so no fixed example is used: a step is tried against the scope's edges.

## 1. How it is worked

Three moves, in order:

1. **Simulate:** each step below says what must happen, what could be done, and what is chosen.
2. **Write the rules:** once all of a half's steps are seen together, its rules are written in `temp/common-ground-problem.md` §2.1, *What passes between the repos*.
3. **Check them:** each step is walked again against the rules. A step a rule does not hold for changes the rule or the step.

Each step has these fields. A field with nothing in it is left out.

- **What must happen:** the outcome, and who acts.
- **Options:** what could be done here, today's way among them.
- **Chosen:** the option taken, and why the others were not.
- **Open:** what the step leaves undecided, each with the trigger that decides it.
- **Today:** what is borrowed from today, and what changes, each with its source.

## 2. The first half, recorded and read

Seven steps:

1. The work meets a copy that does not fit.
2. The System Repo edits both halves of the Adapted Case.
3. It records why.
4. The stretch of work ends, and the Maintainer Repo is told.
5. The Maintainer Repo finds where to start reading.
6. It compares the copies, and reads each why.
7. It lists what changed, nothing judged.

**Step 1. The work meets a copy that does not fit.**

- **What must happen:** during its own work, the System Repo finds that a System Kit Copy does not fit what happened, and the human decides what is done about it, the agent proposing.
- **Options:**
  - a. the copy is changed now, because the work showed it does not fit;
  - b. the copy is changed ahead, for what the agent foresees;
  - c. the misfit is noted, and the copy changed later, at the end of the stretch of work;
  - d. the copy stays as it is, and the System Repo writes what it does instead in its own records.
- **Chosen:** a. The others:
  - b is a speculation, with nothing that happened behind it;
  - c leaves the copy saying what the System Repo no longer does, until someone remembers the note;
  - d leaves the copy saying it for good, and the next agent reads the copy, not the records.
- **Today:**
  - borrowed: an edit comes from something that happened, never a speculation (`delivery/container/.claude/rules/delivered-copies.md`, rule 2; `docs/conventions/exchange/` §5.1, *When a copy may be edited*);
  - changed: today d is required when the need is the CBC Run's own: "never this CBC Run's own answer", and what only it needs goes in its records (`docs/conventions/exchange/` §5.1). So today forbids an edit for the System Repo's own reason. Here the copy keeps it (`temp/common-ground-problem.md` §2.1, *An update*).
