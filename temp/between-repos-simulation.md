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
2. **Work in a System Repo:** it changes its System Kit Copies, and marks what it changed. It chooses its stack once its problem is framed, and marks the choice for the Maintainer Repo to read.
3. **Reading a System Repo:** the Maintainer Repo reads what changed since it last read.
4. **Judging what was read:** the four questions, ending in an Understanding Lesson or none.
5. **The flow down:** a project-agnostic change, the survey, every Adapted Case it touches.
6. **Updating a System Repo:** the System Kit's changes reach a System Repo when work resumes in it.
7. **A lesson from our own work:** the Maintainer Repo finds an Understanding Lesson in its own work.
8. **New knowledge from the human:** the human learns something outside any work.

Not simulated, each for its reason:

- **Reading the Maintainer Repo:** nobody outside reads it, since a System Repo is blind. What the Maintainer Repo learns from itself is scenario 7.
- **A second System Kit:** not needed yet. Its trigger is the first problem no System Kit fits. It brings a choice and a name: several System Kits, each whole, or one System Kit whose parts birth picks from; and a name for each, once there is more than one.
- **A System Repo's own problem understanding:** the System Repo's own work, covered by the agent-work case in its System Kit.

A branch the example does not take is noted at the step where it starts, with its trigger, and not simulated. So the simulation ends.

Fixed before the simulation starts:

- **A System Repo is blind:** it has no address for the Maintainer Repo.
- **Nothing arrives by itself:** nothing crosses between the repos without the human's word. The human carries it, or the agent does on the human's word.

## 2. How a step is written

Each step has these fields. A field with nothing in it is left out.

- **Who acts:** the human, the agent, and in which repo.
- **Reads:** the texts this step needs.
- **Decides:** what is decided, and by whom.
- **Marks:** what this step must write down for a later step, or before a session ends.
- **Can go wrong:** the Failure Cases this step can hit, by number.
- **Borrowed:** what the step takes from today's exchange, and from where. The agent had read today's exchange before writing this, so each borrowing is marked.
- **Changed from today:** what the step does differently from today's exchange, and where today says it. Each goes to the Common Ground Problem's §2.2.
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
- **f. Which half of the Adapted Case it touches:** an Instruction Text copy, or a copy of its Adapted Understanding Text.

## 4. Two passes of the cycle

The scenarios run in two passes. Pass 1 starts from birth. Pass 2 starts when work resumes in the same System Repo after an update. Some needs show only on the second pass, when a step must know where the first one stopped.

## 5. The scenarios

Each scenario is written step by step, the human reading each before the next.

### 5.1 Birth of a System Repo

**Step 1. The human and the agent choose the System Kit that fits the problem.**

- **Who acts:** the human and the agent, in the Maintainer Repo.
- **Reads:** the problem the human brings, written as a problem statement: the situation, and what is hostile in it, with no promise set yet. The framing sets the promise later, inside the System Repo. Also what each System Kit is for. Today there is one, for backends.
- **Decides:** the human decides which System Kit fits, or that none does. The stack is not chosen here: CBC design chooses it once the problem is framed, inside the System Repo (scenario 2). If none fits:
  - the System Repo is not started;
  - or it is started with the project-agnostic texts, and writes its own Adapted Case as Knowledge on Trial, judged when it is read back. If that case holds, it may become a second System Kit (§1). A branch, not simulated: its trigger is the first problem no System Kit fits.
- **Marks:**
  - in the Maintainer Repo, that the System Repo exists: its name, where it lives, which System Kit it got, and why. A System Repo is blind, so the Maintainer Repo is the only side that can find it again to read it back (scenario 3);
  - the problem statement goes with the new System Repo at birth, its first text of its own. The Maintainer Repo keeps no copy.
- **Borrowed:** the problem statement is today's CBC Run Briefing, put in a new CBC Run's `temp/` (`docs/glossary.md`, *CBC Run Briefing*).
- **Can go wrong:**
  - no System Kit fits, and one is bent to fit the problem (Failure Case 24);
  - the System Repo is known only to the human, so it is never read back (Failure Case 1).

**Step 2. The Maintainer Repo gives the new System Repo its System Kit Copies.**

- **Who acts:** the human, or the agent on the human's word, in the Maintainer Repo, by the Maintainer Repo's Adapted Case for a birth.
- **Reads:** the System Kit chosen in step 1, as it stands now.
- **Decides:** nothing new. Every file of the System Kit goes, whole. Among them is the Adapted Case for taking an update, which the System Repo needs in scenario 6. Each Adapted Case goes whole, so the System Repo can judge what an update brings. The Project-Agnostic Understanding Texts stay home. Open, not decided here: the form of the birth's mechanical part, inside the Instruction Text or as a script a human can run alone. Its trigger: the intent's birth instructions are written.
- **Marks:**
  - in the System Repo, each file says whether it is a System Kit Copy or the System Repo's own from birth. A System Kit Copy may be updated later (scenario 6). A text of its own, such as the problem statement or a record it fills, never is;
  - each Instruction Text names its Adapted Understanding Text, so an Adapted Case is read, checked and updated together;
  - Knowledge on Trial keeps its mark in the copy, so the System Repo can tell it from what is proven;
  - in the System Repo, the moment of the System Kit its copies were taken. Reading back needs it to tell the System Repo's edits from the System Kit's changes (scenario 3), and an update needs it to know what is new (scenario 6). The Common Ground Problem already asks for it (§2.1, *An update*).
- **Borrowed:**
  - the Adapted Case for a birth is today's exchange manual with the Pure Seed, `delivery/installs/pure-seed.md`. The Pure Seed's shell commands sit inside the document, since the Maintainer Repo holds no code;
  - the human carries a delivery across, or the agent does on the human's word (`docs/conventions/exchange/` §1, *What cannot change*);
  - every file goes at birth (`docs/conventions/exchange/` §3.2, *What goes*);
  - the records go once, as Record Stubs, and are never updated (`docs/conventions/exchange/` §2.4, *The records' exception*);
  - each copy's *Decisions* footer is left out. It points at the Maintainer Repo's decisions, which a blind System Repo cannot read (`docs/conventions/exchange/` §3.8, *The footer at delivery*);
  - the moment is today's Delivery Pin: the Concept Deliverer's commit the copies equal, kept in the CBC Run (`docs/conventions/exchange/` §2.2, *The CBC Run*).
- **Changed from today:** the Adapted Understanding Texts go too. Today the explanation stays home (`docs/conventions/exchange/` §3.2, *What goes*).
- **Can go wrong:**
  - Knowledge on Trial in a copy is read as proven (Failure Case 18);
  - an Instruction Text goes without its Adapted Understanding Text, so the copy holds the what without the why (Failure Case 9);
  - the moment is missing or wrong, so a change of the System Kit's is read back as the System Repo's own (Failure Case 20).
