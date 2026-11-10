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

Nine scenarios, in order:

0. **An idea's repo:** the Maintainer Repo makes a repo for a new idea. Its brief is worked there on a branch of its own, and main is made from the brief's cleaned history.
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

The scenarios run in two passes. Pass 1 starts from an idea (scenario 0). Scenario 0 runs once per idea, so pass 2 does not repeat it. Pass 2 starts when work resumes in the same System Repo after an update. Some needs show only on the second pass, when a step must know where the first one stopped.

## 5. The scenarios

Each scenario is written step by step, the human reading each before the next.

### 5.0 An idea's repo

It runs once per idea, before birth. The example starts at birth (§3), so it has no part here.

**Step 1. The Maintainer Repo makes a repo for a new idea.**

- **Who acts:** the human, or the agent on the human's word, by the Maintainer Repo's Adapted Case for a new idea. It works from the Maintainer Repo, and writes only into the new repo.
- **Reads:** the idea, as the human tells it.
- **Decides:** the human decides the idea is worth a repo. Open, not decided here: which texts the idea's repo gets when it is made, so a session there knows what a brief holds, how the briefing is worked, and where its lessons are written. Its trigger: the intent's instructions for a new idea are written.
- **Marks:**
  - in the Maintainer Repo, a register entry: the idea's repo, where it lives, and its state, *briefing*. The register is the only place the Maintainer Repo can find it again. A dropped idea stays in the register, marked *dropped*;
  - in the idea's repo, a briefing branch that holds its first commit. Main does not exist until the brief is finished (step 3).
- **Borrowed:**
  - the register is today's table of CBC Runs, each with where it lives and its state (`ARCHITECTURE.md` §2.5, *The CBC Runs*);
  - the brief is today's CBC Run Briefing (`docs/glossary.md`, *CBC Run Briefing*).
- **Changed from today:** a brief is drafted in a repo of its own. Today it is drafted in the Concept Deliverer's `temp/`, such as `temp/run-6-briefing.md`, and its drafting history stays in the Concept Deliverer's. The Maintainer Repo now keeps only the register entry.
- **Can go wrong:**
  - the idea's repo is known only to the human, so it is never found again (Failure Case 1);
  - the register is not updated, so it is older than the human's understanding (Failure Case 2).

**Step 2. The brief is worked on the briefing branch.**

- **Who acts:** the human, with an agent: from the Maintainer Repo, or in a session of the idea's repo's own.
- **Reads:** the brief so far. Context from the Maintainer Repo, such as project-agnostic understanding or what other System Repos found, comes in only on the human's word.
- **Decides:** the human decides what the brief includes and excludes, and when the work pauses, stops, or is finished. The agent may draft on the human's word.
- **Marks:**
  - commits on the briefing branch, as the work needs. This branch is never rewritten;
  - each include and exclude, with its why, written where step 3's cleanup keeps it;
  - in the register, the state, on the human's word: *briefing*, *paused* or *dropped*.

  Open, not decided here: whether the briefing branch stays in the idea's repo, where a later agent can read it, or moves out of it. Until then it stays. Its trigger: the first briefing that brought in context from the Maintainer Repo.
- **Borrowed:** the brief is the human's; the agent drafts it when asked, and the human's version is what goes (`.claude/approaches-on-trial/auto-run.md`, *Stages*, stage 2).
- **Can go wrong:**
  - context from the Maintainer Repo is written into the brief, so the System Repo inherits what it is meant never to see. No Failure Case covers it yet, as in scenario 1, step 3;
  - the register says *briefing* for an idea the human has let go (Failure Case 2).

**Step 3. The brief is finished, its history cleaned, and main is made.**

- **Who acts:** the agent, on the human's word, in the idea's repo.
- **Reads:** the briefing branch, whole.
- **Decides:** the human decides the brief is finished, and approves the clean history before main is made.
- **Marks,** in this order:
  - what was learned, first: each dead end and each rejected option, with its why, where the clean history keeps it. The cleanup drops commits, never lessons;
  - a clean branch holding the brief in clean commits. The briefing branch is never rewritten. How the clean branch is built, a copy cleaned or the work brought onto a new branch, is the Adapted Case's;
  - main, made once at the clean branch's tip, after the human approves. The clean branch is then deleted;
  - the briefing branch, kept local and never pushed;
  - in the register, the state *brief done*.

  Open, not decided here:
  - a record that cites a commit on the briefing branch points at nothing on main. Either the cleanup fixes each citation, or a record on the briefing branch cites no commit. Its trigger: the first cleanup;
  - "never pushed" is only told: a push of every branch takes it too. Its trigger: the idea's repo gets its first remote;
  - whether every Plan Step in a System Repo ends the same way, its branch cleaned before main moves. Its trigger: the first birth that ends this way.
- **Borrowed:** a Plan Step's branch reaches main by fast-forward, on the reviewer's word (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*).
- **Changed from today:** today a branch reaches main as it is, with no cleanup. Main's history is still never rewritten (`TODO.md`, the item on landing two facts in the exchange convention): only the briefing branch is cleaned, and main is made from the result.
- **Can go wrong:**
  - the cleanup drops a why, so the clean history holds the what without the why (Failure Case 9);
  - the briefing branch is pushed, and what was meant to stay local is out.

### 5.1 Birth of a System Repo

**Step 1. The human and the agent choose the System Kit that fits the problem.**

- **Who acts:** the human and the agent, in the Maintainer Repo.
- **Reads:** the problem the human brings, written as a problem statement: the situation, and what is hostile in it, with no promise set yet. The framing sets the promise later, inside the System Repo. Also what each System Kit is for. Today there is one, for backends.
- **Decides:** the human decides which System Kit fits, or that none does. The stack is not chosen here: CBC design chooses it once the problem is framed, inside the System Repo (scenario 2). If none fits:
  - the System Repo is not started;
  - or the Maintainer Repo first writes an Adapted Case for the new kind of system, from the project-agnostic understanding, as Knowledge on Trial, and the System Repo is started with it. The project-agnostic texts stay home, as at every birth. The System Repo adapts the case further, and reading back judges it like any other. If it holds, it may become a second System Kit (§1). A branch, not simulated: its trigger is the first problem no System Kit fits.
- **Marks:**
  - in the Maintainer Repo, that the System Repo exists: its name, where it lives, which System Kit it got, and why. A System Repo is blind, so the Maintainer Repo is the only side that can find it again to read it back (scenario 3);
  - the problem statement goes with the new System Repo at birth, its first text of its own. The Maintainer Repo keeps no copy.
- **Borrowed:** the problem statement is today's CBC Run Briefing, put in a new CBC Run's `temp/` (`docs/glossary.md`, *CBC Run Briefing*).
- **Can go wrong:**
  - no System Kit fits, and one is bent to fit the problem (Failure Case 24);
  - the System Repo is known only to the human, so it is never read back (Failure Case 1).

**Step 2. The Maintainer Repo gives the new System Repo its System Kit Copies.**

- **Who acts:** the human, or the agent on the human's word, by the Maintainer Repo's Adapted Case for a birth. It works from the Maintainer Repo, and writes only into the new System Repo.
- **Reads:** the System Kit chosen in step 1, as it stands now.
- **Decides:** nothing new. The birth delivers everything and decides nothing. Every file of the System Kit goes, whole. Among them are the two Adapted Cases the System Repo needs before its work: the one for finishing its birth (step 3), and the one for taking an update (scenario 6). Each Adapted Case goes whole, so the System Repo can judge what an update brings. The Project-Agnostic Understanding Texts stay home. Before step 3, the human checks that every file arrived whole and the moment is written. Open, not decided here: the form of the birth's mechanical part, inside the Instruction Text or as a script a human can run alone. Its trigger: the intent's birth instructions are written.
- **Marks,** in this order:
  - the new System Repo, with a first commit that holds nothing from the System Kit, so the next commit holds the copies and nothing else;
  - the start: the System Kit Copies, committed as they arrived, on a branch of their own that is never merged or changed. It is made before the agent acts, so no edit of the System Repo's can be in it. Every change after it is the System Repo's own, and the first reading back starts there (scenario 3);
  - the moment of the System Kit the copies were taken at, in each commit of the start and in the System Repo's first record entry. The moment says what the copies came from, in the Maintainer Repo's history. The start says where the System Repo's changes begin, in its own. Reading back needs both, and both are kept in the System Repo, since the Maintainer Repo can look only there. An update needs the moment to know what is new (scenario 6). The Common Ground Problem already asks for it (§2.1, *An update*);
  - the problem statement from step 1, put beside the copies and not committed. It is the System Repo's own text;
  - in each file, whether it is a System Kit Copy or the System Repo's own from birth. A System Kit Copy may be updated later (scenario 6). A text of its own, such as the problem statement or a record it fills, never is;
  - in each Instruction Text, the Adapted Understanding Text it stands on, so an Adapted Case is read, checked and updated together;
  - in a copy of Knowledge on Trial, its mark, so the System Repo can tell it from what is proven.
- **Borrowed:**
  - the Adapted Case for a birth is today's exchange manual with the Pure Seed, `delivery/installs/pure-seed.md`. The Pure Seed's shell commands sit inside the document, since the Maintainer Repo holds no code. It "delivers everything and decides nothing" (its opening);
  - the human carries a delivery across, or the agent does on the human's word (`docs/conventions/exchange/` §1, *What cannot change*);
  - every file goes at birth (`docs/conventions/exchange/` §3.2, *What goes*);
  - the first commit is today's hygiene commit, and main stays there, the delivered files beside it untracked (`delivery/installs/pure-seed.md`, steps 3 and 5);
  - the start is today's Receipt Branch, `birth-seed`, never merged (`delivery/installs/pure-seed.md`, step 4; `docs/glossary.md`, *Receipt Branch*);
  - the moment is today's Delivery Pin, the Concept Deliverer's commit the copies equal. The Pure Seed writes it in each commit's subject on `birth-seed`, and in the birth entry of the Decisions Log (`delivery/installs/pure-seed.md`, steps 2 and 4);
  - the check is today's *Check the seed* (`delivery/installs/pure-seed.md`, step 6);
  - the problem statement waits in `temp/`, and the System Repo commits it unchanged when its work starts. Today a full-auto birth puts it there (`.claude/approaches-on-trial/auto-run.md`, *Stages*, stage 6), and CBC Framing commits it unchanged (`delivery/fills/cbc-run-pure-playbook.md`, Step 1);
  - the records go once, as Record Stubs, and are never updated (`docs/conventions/exchange/` §2.4, *The records' exception*);
  - each copy's *Decisions* footer is left out. It points at the Maintainer Repo's decisions, which a blind System Repo cannot read (`docs/conventions/exchange/` §3.8, *The footer at delivery*).
- **Changed from today:**
  - the Adapted Understanding Texts go too. Today the explanation stays home (`docs/conventions/exchange/` §3.2, *What goes*);
  - today two texts disagree on the start. The Pure Seed writes the Read-Through Commit as *none* at birth, and keeps the delivery as it arrived on the Receipt Branch (`delivery/installs/pure-seed.md`, steps 2 and 4). The exchange's cycle has the CBC Run write its birth commit b as its Read-Through Commit (`docs/conventions/exchange/` §2.5, *One cycle*). The start here is the Pure Seed's;
  - today a pure birth keeps the problem statement out: it arrives later, and opens CBC Framing (`delivery/installs/pure-seed.md`, step 7).
- **Can go wrong:**
  - Knowledge on Trial in a copy is read as proven (Failure Case 18);
  - an Instruction Text goes without its Adapted Understanding Text, so the copy holds the what without the why (Failure Case 9);
  - the moment is missing or wrong, so a change of the System Kit's is read back as the System Repo's own (Failure Case 20);
  - the start holds an edit, or is changed later, so reading back takes the edit for the System Kit's text, and it is never judged (Failure Case 19).

**Step 3. The human starts the agent, and the agent finishes the birth.**

- **Who acts:** the human, then the agent in the new System Repo, in its first session.
- **Reads:**
  - the prompt: one fixed text, the same for every birth. It holds only what is true of this session: what arrived and where, that the birth is finished by the System Repo's Adapted Case for it, and that a reviewer is present. It names no moment: that is in the files (step 2);
  - every file that arrived in step 2, before any change.
- **Decides:** the agent decides how the System Repo is arranged, each choice with its why in its plan. Its Adapted Case for a birth gives the outcomes and the order, never the arrangement:
  1. read everything that arrived, before any change;
  2. cut a branch for the birth's work from main;
  3. plan the arrangement, each choice with its why;
  4. commit one at a time, on the reviewer's word;
  5. end when the outcomes hold: the records exist and the agent's arrangement stands, before any work on the problem.

  Open, not decided here: whether the problem statement is read at birth, or only when the work starts (scenario 2). Its trigger: scenario 2's first step is written.
- **Marks:**
  - in the System Repo's records, the end of the birth. Scenario 2 starts after it, so reading back can tell the birth's arrangement from the work's changes;
  - in the plan, each arrangement choice and its why, so reading back reads the why with the change.
- **Borrowed:**
  - the prompt is today's Pure Seed prompt, the same for every birth so births can be compared, holding what is true of this session only (`delivery/installs/pure-seed.md`, step 7);
  - the agent finishing the birth is today's Newborn CBC Run's agent, which finishes the CBC Run Birth (`delivery/installs/pure-seed.md`, its opening and step 7);
  - the order is today's prompt: read the whole repository, plan the agent's own commit sequence, commit on the reviewer's word (`delivery/installs/pure-seed.md`, step 7);
  - the branch is the branch every Plan Step cuts from main (`delivery/fills/cbc-run-pure-playbook.md`, *At the opening*);
  - the outcomes and the end are today's Step 0, Bootstrap, closed on its Plan Step Gate: "the repo, the records and the agent's arrangement exist before any content" (`delivery/fills/cbc-run-pure-playbook.md`, Step 0).
- **Changed from today:** the order and the outcomes live in an Adapted Case in the System Kit, not in the prompt. Today the prompt holds the order, and Step 0's gate is left for the agent to write. A prompt lives only in its session, and the System Repo can neither change it nor offer a change back.
- **Can go wrong:**
  - the agent reads the Maintainer Repo, which a System Repo is meant never to see. Today blindness is only told: the other repo sits on the same disk. Run 3's agent read a checkout on disk of the repo it took copies from (devlog 2026-09-09, later). No Failure Case covers it yet; noted for the Common Ground Problem's §4;
  - an arrangement choice is committed without its why, so reading back has the change and not the reason (Failure Case 22).
