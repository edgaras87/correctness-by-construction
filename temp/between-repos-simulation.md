# Between the Repos, Simulated

<!-- A draft for the Plan Step "Find how what we know stays true",
     stage 1. It simulates, step by step, what passes between the
     Maintainer Repo and a System Repo, and inside the Maintainer
     Repo when understanding changes. What it finds goes into
     temp/common-ground-problem.md §2.1, *What passes between the
     repos*; how it differs from today goes into that draft's §2.2,
     for stage 2. The talk behind it: TODO-CONVERSATION-MEMORY.md §31,
     its part of 2026-11-08 and 2026-11-09. It goes when the Plan
     Step closes, and git keeps every version. -->

This document simulates how understanding moves between the repos, one step at a time. It is written for the system as intended, starting fresh, not from today's exchange. Each step says what happens, and what must be marked for a later step. A later step that finds something missing adds it to the earlier step, and says why.

It uses the Common Ground Problem's Defined Terms (`temp/common-ground-problem.md`, *Defined Terms*). One more is decided and not yet written there; it goes there once the simulation is done:

- **Understanding Lesson:** knowledge that judging finds changes an Understanding Text, wherever it came from: *project-agnostic* when it changes a Project-Agnostic Understanding Text, *adapted* when it changes only one sort of repo's Adapted Understanding Text.

## 1. What is simulated

Eight scenarios, in order:

1. **Birth of a System Repo:** the Maintainer Repo starts a new System Repo from the System Kit.
2. **Work in a System Repo:** it changes its System Kit Copies, and marks what it changed.
3. **Reading a System Repo:** the Maintainer Repo reads what changed since it last read.
4. **Judging what was read:** the four questions, ending in an Understanding Lesson or none.
5. **The flow down:** a project-agnostic change, the survey, every adapted case it touches, and their instructions.
6. **Updating a System Repo:** the System Kit's changes reach a System Repo when work resumes in it.
7. **A lesson from our own work:** the Maintainer Repo finds an Understanding Lesson in its own work.
8. **New knowledge from the human:** the human learns something outside any work.

Not simulated, each for its reason:

- **Reading the Maintainer Repo:** nobody outside reads it, since a System Repo is blind. What the Maintainer Repo learns from itself is scenario 7.
- **A second kind of system:** not needed yet. Its trigger is the first System Repo that does not build a backend.
- **A System Repo's own problem understanding:** the System Repo's own work, covered by the agent-work case in its System Kit.

Fixed before the simulation starts:

- **A System Repo is blind:** it has no address for the Maintainer Repo.
- **Nothing arrives by itself:** the human carries every change across.

## 2. How a step is written

Each step has these fields. A field with nothing in it is left out.

- **Who acts:** the human, the agent, and in which repo.
- **Reads:** the texts this step needs.
- **Decides:** what is decided, and by whom.
- **Marks:** what this step must write down for a later step, or before a session ends.
- **Can go wrong:** the Failure Cases this step can hit, by number.
- **Borrowed:** what the step takes from today's exchange, and from where. The agent had read today's exchange before writing this, so each borrowing is marked.
- **Added later:** what a later step found missing here, which step found it, and why.

## 3. The example

One change is followed through every scenario:

> A System Repo writes commit messages by its System Kit Copy of the commit-message Task Instruction Text. The Task Instruction Text caps a commit subject at 50 characters. The System Repo's scope names are long, and the cap fails its work. It edits its copy to 60 characters.

It was chosen because judging it is not obvious. The edit may be specific to that System Repo, since its scope names are long. Or it may be an Understanding Lesson, if the cap is wrong for every repo.

Other kinds of change go differently. Each is written as a variant, only at the step where it parts from the example:

- **a. A delivered copy edited:** the example.
- **b. Something new added:** no copy to compare with; it has no home in the Maintainer Repo yet.
- **c. Delivered Knowledge on Trial changed:** the original is itself unjudged.
- **d. A copy no longer used, or deleted:** an absence.
- **e. A change with no why written.**
- **f. Which half of the pair it touches:** an Instruction Text copy, or a copy of its Adapted Understanding Text.

## 4. Two passes of the cycle

The scenarios run in two passes. Pass 1 starts from birth. Pass 2 starts when work resumes in the same System Repo after an update. Some needs show only on the second pass, when a step must know where the first one stopped.

## 5. The scenarios

Each scenario is written step by step, the human reading each before the next.

### 5.1 Birth of a System Repo

**Step 1. The human decides to start a System Repo.**

- **Who acts:** the human. The agent in the Maintainer Repo helps, if asked.
- **Reads:** the problem the human wants solved, as they hold it now.
- **Decides:** the human decides what system is built, and its kind: a backend, in the example. The kind decides which of the System Kit's adapted cases the System Repo gets.
- **Marks:** in the Maintainer Repo, that the System Repo exists: its name, where it lives, and its kind. A System Repo is blind, so the Maintainer Repo is the only side that can find it again to read it back (scenario 3).
- **Can go wrong:**
  - the kind has no adapted case in the System Kit yet: the trigger for a second kind of system (§1);
  - the System Repo is known only to the human, so it is never read back (Failure Case 1).
