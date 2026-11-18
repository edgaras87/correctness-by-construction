# The Common Ground Problem

<!-- A draft: the problem of the Plan Step "Find how what we know
     stays true", its stage 1, in the reviewer's words. Built from
     TODO-CONVERSATION-MEMORY.md §31, *Keeping what we know true*,
     and from what temp/model-example/idea-model-problem.md says of the problem,
     not of a model. Polished one insight at a time, each a commit,
     so the diffs show what changed. It states the problem only: an
     answer met on the way is kept as an option to consider (§8),
     not chosen. Its
     home is decided when the Plan Step closes; it goes then, and
     git keeps every version. -->

This document states the Common Ground Problem. It chooses no answer; answers met along the way are kept as options to weigh (§8). It is written about the system as intended (§2.1), and its options are weighed there; what the Maintainer Repo has today, and what was already noticed there, is set apart (§2.2). The next step sets the two against each other, and an answer is tried on the real repo only where they fit.

## Defined Terms

A Defined Term is a word or words given an exact meaning, written capitalized, so plain English stays free. Each Defined Term below is defined here, once, except those the layers model defines, whose entries point there. Its other Names, such as Backbone Idea and Work Domain Idea, are used as it defines them (`temp/common-ground/knowledge-layers-general.md` §2, *The layers*). Six plain words keep a narrow sense here, written below, and are used in no other: knowledge, text, the chat, the human, the agent, common ground. Any other lowercase word is plain English. An *italic* word is a label inside the Defined Term it belongs to. The Defined Terms below are local to the Common Ground Problem, a trial for TODO's item *Decide which names go in the glossary, and how a name one text uses alone is kept apart*, and each was checked against the repo's glossary. They are the intent's words; the repo's own names for the same things are today's, set beside them in §2.2. When this document lands, each Defined Term replaces a repo name, joins the repo's glossary, or goes. A definition names what it builds on by its Defined Term, never by where it stands in the text, such as "the same idea" or "the two".

Plain words, in a narrow sense:

- **the agent:** the AI model in a session. It knows its subjects from training, and the human and the work only from what it reads.
- **the chat:** where knowledge passes between the human and the agent; lost when a session ends, unless written down. Not text.
- **common ground:** between the human and the agent, on what the human knows: the agent's picture of the human's understanding, built from the text, matches it and its Depth of Understanding.
- **the human:** the person whose knowledge it is, who carries it from one session to the next.
- **knowledge:** what one knows, and how one understands it. It lives in a head.
- **text:** where knowledge is stored, as it stood at one moment: Understanding Text and Instruction Text, wherever kept.

Defined Terms, in alphabetical order:

- **Adapted Case:** defined by the layers model (`temp/common-ground/knowledge-layers-general.md` §2.3, *The Adapted Case layer*).
- **Adapted Understanding Text:** defined by the layers model (`temp/common-ground/knowledge-layers-general.md` §2.3, *The Adapted Case layer*).
- **Common Ground Problem:** keeping common ground between the human and the agent from one session to the next, while the text it is built from goes stale; the problem this document states.
- **Depth of Understanding:** how deep someone's understanding of an idea goes: basics for one, details for another.
- **Failure Case:** one way the human and the agent lose their common ground, numbered in §4.
- **File Instruction Text:** an Instruction Text the agent loads when a certain kind of file is opened.
- **Instruction Text:** defined by the layers model (`temp/common-ground/knowledge-layers-general.md` §2, *The layers*). So far it comes in three sorts, by when the agent loads it: Task Instruction Text, Session Instruction Text and File Instruction Text.
- **Knowledge Axis:** one way of sorting text. There are five: *who uses it*, *time*, *kind*, *where*, *layer* (§3).
- **Knowledge Drift:** text and knowledge moving apart. The text holds less than the knowledge, or is older than it.
- **Knowledge Drift Repair:** bringing text back in line with the knowledge, so common ground can be built from it again: finding where it drifted, judging each place, deciding with the human what changes, and fixing it. Today the finding is a sweep: one or more agents read the whole repo.
- **Knowledge on Trial:** defined by the layers model (`temp/common-ground/knowledge-layers-general.md` §3.1, *How the layers fill*).
- **Knowledge Time Shift:** knowledge changing *time*: *later* to *now* when learned or checked, *now* to *before* when replaced.
- **Maintainer Repo:** the repo that keeps the understanding and the System Kit, and reads back what each System Repo learns.
- **Maintainer Repo Register:** the Maintainer Repo's list of its System Repos: where each lives, and its *settled snapshot*.
- **Mistaken Knowledge:** knowledge that is itself wrong, carried faithfully into text. It is not Knowledge Drift.
- **One Home per Fact:** the Maintainer Repo's practice: each fact in one text, its home, with every other text pointing there.
- **Repo Responsibility:** what each repo is meant to keep: the Maintainer Repo, and each System Repo (§2). Its *time* is *later*: as meant, not as done today.
- **Repo Responsibility Gap:** where a repo does not keep its Repo Responsibility. It is fixed in the repo, or in the Repo Responsibility.
- **Session Instruction Text:** an Instruction Text the agent loads in every session.
- **System Kit:** what the Maintainer Repo keeps for System Repos to work from, shared by the System Repos it serves, and listed in §2.1, *What the System Kit holds*. Its originals stay in the Maintainer Repo, beside the project-agnostic understanding they are adapted from; each System Repo works from copies, and takes the System Kit's changes by a System Kit Update.
- **System Kit Attention Note:** what a System Repo writes for the Maintainer Repo to look at in the System Kit, when no System Kit Copy Change carries it.
- **System Kit Copy:** a copy of a System Kit file, as it lives in a System Repo.
- **System Kit Copy Change:** a System Repo's change to a System Kit Copy, made against the System Kit Version that copy came from.
- **System Kit Copy Change Record:** what a System Repo writes with each System Kit Copy Change: what changed, what happened, which work found it, and the System Repo's proposal. It sits in the footer of the Adapted Understanding Text of the Adapted Case the copy belongs to. For a System Kit Copy outside any Adapted Case, where it sits is open.
- **System Kit Update:** what the Maintainer Repo sends a System Repo: a copy of every System Kit file at one System Kit Version, with its System Kit Update Note.
- **System Kit Update Note:** what the Maintainer Repo writes with a System Kit Update, for the System Repo that takes it.
- **System Kit Version:** the System Kit as it stood at one Maintainer Repo commit. Each System Repo records the one its System Kit Copies came from.
- **System Repo:** a repo where a real system is built by the concept, working from copies of the System Kit.
- **System Repo Reading:** the Maintainer Repo reading one System Repo since it last read it, and the draft that lists what it found.
- **Task Instruction Text:** an Instruction Text the agent loads for one kind of task.
- **Text Life Phase:** where in a text's life a Failure Case shows: *writing*, *aging*, *reading*.
- **Understanding Text:** defined by the layers model (`temp/common-ground/knowledge-layers-general.md` §2, *The layers*).

Labels:

- *who uses it*: *the human*, *the agent*, *both*
- *time*: *before*, *now*, *later*
- *kind*: Understanding Text, Instruction Text
- *where*: *the Maintainer Repo*, *a System Repo*; a Failure Case is *either* or *between*
- *layer*: *layer 1* to *layer 4*
- Text Life Phase: *writing*, *aging*, *reading*
- Maintainer Repo Register: *settled snapshot*, the System Repo's snapshot up to which the Maintainer Repo has read, judged and acted on. It holds the System Kit Version the System Repo had then, which may be behind the newest.

## 1. The purpose

Knowledge is what one knows, and how one understands it. It lives in a head. Text is where it is stored, as it stood at one moment.

Text here is understanding and instruction (§3.3), wherever it is kept. So far it is kept in the repo's files, in commit messages, in the human's private working rules, and in the agent's memory.

The chat is not text. It is where knowledge passes between the human and the agent, and it is lost when the session ends unless something is written down.

Two sides work with the knowledge:

- **The human:** the person whose knowledge it is. They learn, decide, and carry the knowledge from one session to the next.
- **The agent:** the AI model working in a session. It knows its subjects from its training, but starts each session knowing the human and the work only from what it reads.

The purpose is common ground between the human and the agent on what the human knows, and how deeply, from one session to the next. Both learn, and write down what they learn. A new session reads it, and the human doesn't have to retell it. Both continue improving from there.

The problem holds wherever a human works with an agent across sessions. The Maintainer Repo is where it is seen first, and where it is tested.

## 2. The Maintainer Repo

The Maintainer Repo is pictured twice. §2.1 is the intent: what it should be and keep, in the Common Ground Problem's own Defined Terms. §2.2 is what it has today, not yet checked, and what to check, in the repo's own names. They are kept apart because the repo may have drifted from the intent, and a problem written only from today would take that drift as given. Each difference between them is a Repo Responsibility Gap, or a sign the intent should change.

### 2.1 As intended

Each project is meant to live in a repo, a git repository, of one of two sorts, so far:

- the Maintainer Repo, which holds the concept;
- each System Repo, which builds a real system by the concept.

The Maintainer Repo holds more than its own work. It also holds the understanding of agent work. No single project owns it, and every System Repo receives it adapted, in the System Kit.

Its understanding falls in two groups. Each is adapted for two places, the Maintainer Repo and each System Repo:

| Understanding | Adapted for the Maintainer Repo | System Kit |
|---|---|---|
| How work is done with an agent: a change, a commit, a plan | its own Adapted Case of agent work | agent work, adapted for System Repos (below, *What the System Kit holds*) |
| How a CBC system is designed: the concept and its methods | none | CBC system design, adapted for one kind of system (below, *What the System Kit holds*) |

The Maintainer Repo means to keep both groups in the layers of knowledge (§3.5). Whether the layers are kept apart as meant is checked in the next step.

The understanding of CBC system design is project-agnostic: it fits any system, not only software. The System Kit holds it adapted for one kind of system so far (below, *What the System Kit holds*).

So knowledge written in the Maintainer Repo becomes instructions that agents act on: in the Maintainer Repo itself, for its own work, and in every System Repo. The agent in a System Repo starts with none of the Maintainer Repo's context, only its System Kit Copies, and they can drift, or change on their own.

The Repo Responsibility follows. It may change itself, and whether the repo does all of it is not yet checked.

The Maintainer Repo keeps:

1. understanding of agent work;
2. understanding of the concept, CBC system design;
3. the System Kit, for every System Repo to work from (below, *What the System Kit holds*);
4. its own Adapted Case of agent work, updated as the project-agnostic understanding changes;
5. findings from System Repos. A System Repo uses its Adapted Cases in practice, and changes them as its problems demand. It can judge a change against its own Adapted Cases, but not against the project-agnostic understanding or other System Repos. The Maintainer Repo reads the System Kit Copy Changes back and judges each, by its own Adapted Case of taking a change from another repo (below, *Judging a change read back*);
6. System Kit Updates for System Repos, taken when work resumes in one (below, *An update*): a System Repo born earlier gets the System Kit's changes, and judges each against its own System Kit Copy;
7. its own records: the history and the backlog of this work.
8. its Knowledge on Trial, from System Repos and its own, judged here. Each stays on trial for more uses, lands as new understanding, or lands in pieces, added to understanding texts that already exist, or is dropped. A landing is a moment for a Knowledge Drift Repair of what it touches, here and in the System Repos' System Kit Copies. The Maintainer Repo also judges its own Knowledge on Trial, with no outside judge. A System Repo's, once judged here, reaches that System Repo by a System Kit Update, judged there like any other change.

Each System Repo:

1. keeps its System Kit Copies of the Adapted Cases (below, *What the System Kit holds*). It uses them, and may change any part of them. The project-agnostic understanding stays in the Maintainer Repo;
2. keeps understanding of its own problem: one specific system's design;
3. keeps its own records, started from the record forms in its System Kit;
4. has its own Knowledge on Trial: it uses each until the Maintainer Repo judges it, and offers it back;
5. takes System Kit Updates by its copy of the Adapted Case for taking them, and may change any part of it (below, *An update*).

#### What the System Kit holds

Other parts of this document point here, and list none of it.

Agent work and CBC system design are each held as Adapted Cases. How each splits into Adapted Cases, one or several, is open.

1. agent work, written from its project-agnostic understanding for System Repos, among it how a System Repo takes a System Kit Update;
2. CBC system design, written from its project-agnostic understanding for one kind of system: backends, so far;
3. the Defined Terms the Adapted Cases use;
4. the forms a System Repo's records start from. They go once, at birth, and are the System Repo's own after it;
5. a description of CBC system design for the System Repo's readers, as adapted to its kind of system. Its form is open, and is decided when the concept is split, and so is whether a System Repo may change it.

#### What passes between the repos

So far, three movements:

| Movement | From, to | What passes |
|---|---|---|
| birth | the Maintainer Repo to a new System Repo | System Kit Copies, taken at one System Kit Version |
| reading back | a System Repo to the Maintainer Repo | what the System Repo changed in its System Kit Copies, and why |
| update | the Maintainer Repo to a System Repo, when work resumes in it | the System Kit's changes since its copies were taken |

Each sort of repo takes a change from the other by its own Adapted Case of one idea, how a repo takes a change from another. The Maintainer Repo's is the judging below. The System Repos' is part of the System Kit: each System Repo uses its copy and may change it, and the Maintainer Repo judges those System Kit Copy Changes like any other.

A System Kit Copy Change read back is followed in six parts, from the System Kit Copy Change to the System Kit Update's take, each with its rules below. Their cases are simulated one at a time (below, *A System Repo's change*).

The rules of Change and Read come from one case, one Adapted Case changed in any of its texts, simulated step by step. Each rule's options, and why the others were not taken, are there (`temp/common-ground/system-repo-change-simulation.md` §3, *Change*; §4, *Read*). The other cases are checked against them next.

##### Change

**Recording a change.** A System Repo changes its copy when its work shows the copy does not fit, never ahead of that, the human deciding. The System Kit Copy Change carries a System Kit Copy Change Record, written and committed with it, in a footer of the copy's Adapted Understanding Text, which is not loaded for work. A commit that changes a copy and not its System Kit Copy Change Record is stopped. The take of a System Kit Update is not a System Kit Copy Change, and passes (below, *An update*). The System Kit Copy Change Record says what changed, by meaning, and whether the texts it left as they were still match it; what happened, concretely, in the System Repo's own words; which work found it; and whether the System Repo thinks the System Kit Copy Change answers its own problem or one any repo would meet. That last is a proposal, never a verdict. The System Kit Copy Change Record says the System Kit Copy Change as it stands: a later edit or reversal rewrites it. The copy keeps the System Kit Copy Change (below, *An update*).

**A System Kit Attention Note.** What has no System Kit Copy Change to carry it goes in a System Kit Attention Note, in one known place in the System Repo's records: a misfit with none made, a doubt about a line, something the System Kit lacked, a copy no longer used, or anything the human wants the Maintainer Repo to check. It never lists a System Kit Copy Change. One about a System Kit Copy Change points at its System Kit Copy Change Record.

**The gate.** At each Plan Step's close, the step's System Kit Copy Changes are compared with their System Kit Copy Change Records and seen together. The human decides each: kept, edited or reversed. System Kit Copy Changes with one reason are linked, the reason written once. The gate asks once whether an Adapted Case did not fit with no System Kit Copy Change made, and each one named becomes a System Kit Attention Note. Main moves only at the close.

##### Read

**Reading a change.** The Maintainer Repo Register keeps, for each System Repo, where it lives and its *settled snapshot*, the snapshot at the commit its last System Repo Reading stopped at. The *settled snapshot* moves to a System Repo Reading's stop once its verdicts are acted on, right after judging when they ask for no change, never before. Birth sets the *settled snapshot* at the commit holding the copies as they arrived, so it is never empty. A System Repo has work to read when its main has moved past the *settled snapshot*. It is checked when the human names it, and every System Repo is when the human asks what to read. A System Repo Reading runs from the *settled snapshot* to main, so it reads only closed Plan Steps, and it writes main down before reading anything. It compares the System Kit's folders and the System Kit Attention Notes' place across that span, in the System Repo's own history, and pairs each System Kit Copy Change with its System Kit Copy Change Record in the same diff. So a System Kit Copy Change with no System Kit Copy Change Record is still found (Failure Case 22), and one already read is not found again. A look past main may be asked for; it moves nothing, and gives only System Kit Attention Notes. Open: a System Kit Update lands inside the next span, and how its changes are told from the System Repo's own. Its trigger: the first System Kit Update to reach a System Repo whose copies have System Kit Copy Change Records.

**The list.** A System Repo Reading is one line per System Kit Copy Change and per System Kit Attention Note, nothing judged: the System Repo's proposal stays a proposal. System Kit Copy Changes with one reason are listed together. The human checks that the list is whole. The System Repo Reading is a draft, and goes once its work is done.

##### Judge

**Judging a change read back.** Four questions, in order, the cheapest first:

1. Did the System Kit Copy already say this? Then it is a misreading (Failure Case 7). Nothing changes but, perhaps, the copy's wording.
2. Is it specific to that System Repo's problem? Then nothing changes here; it stays in that System Repo.
3. Does the project-agnostic understanding already hold it? Then the Adapted Case it came from lost it in narrowing, and is fixed from the project-agnostic understanding. The Maintainer Repo's own Adapted Case of the same idea is checked for the same loss.
4. Is it true for every repo? Then it is a project-agnostic lesson, below.

If none holds, it is a lesson for System Repos only: the Adapted Case it came from gains it, and the project-agnostic understanding stays as it is. A lesson found in the Maintainer Repo's own work takes questions 3 and 4 the same way.

##### Act on the verdicts

**A project-agnostic lesson.** The text above an Adapted Case, a Work Domain Idea or a Backbone Idea, is bound to no project, so a lesson enters it if it holds for any project, whatever an Adapted Case says.

- It is reworded to name no project, the agent drafting and the human deciding. Its first wording is kept beside it, since the rewording is the agent's reading.
- Every other Adapted Case built on that idea is surveyed; the one the lesson came from is not. Each answers "holds as it is", "must change", with what and why, or "conflicts", with why. A conflict is input to the human's decision, never a veto. If every answer conflicts, the lesson may not be project-agnostic.
- The survey is always run when the lesson changes or contradicts project-agnostic text that already exists, and at the human's choice when the lesson is new.
- The project-agnostic understanding then gains the lesson, or is fixed where it was wrong (Failure Case 11), and what the survey found must change, changes.

How each question is answered, and by whom, is open. So is a System Kit Copy Change that arrives without its why (Failure Case 22).

**Narrowing, never shrinking.** The text above an Adapted Case changes only where it is wrong for every repo (Failure Case 11). A part that does not fit one sort of repo stays in it: the Adapted Case leaves the part out, and marks that it did, with why. The mark is written when the exclusion is decided, never listed ahead. So question 3 can tell a part lost in narrowing, with no mark, from one left out on purpose, with its mark. A change to a marked part reopens its why.

##### Deliver

**What an update sends.** A System Kit Update sends the System Kit's changes, each with its why. The project-agnostic understanding stays home, as at birth. A change that comes from a project-agnostic lesson quotes the lesson as its why.

##### Take

**An update.** How a System Repo takes one is open. Seen so far:

- a System Kit Copy may differ from its original, and keeps the System Repo's specific System Kit Copy Changes. This holds for an Instruction Text and its Adapted Understanding Text alike, and still holds after reading back and a System Kit Update. A System Kit Update never overwrites it: the System Repo judges what is new, as the Maintainer Repo judges a lesson;
- work resuming in a System Repo goes in a fixed order: reading back, judging, then the System Kit Update;
- each System Repo says which System Kit Version its copies come from;
- a declined System Kit Update is recorded with its why, so a later reading back does not take it for a new System Kit Copy Change;
- the instructions for taking a System Kit Update are taken first, on their own, and the rest under them. Otherwise a System Kit Update is taken by instructions older than it (Failure Case 10).

#### A System Repo's change

This section follows one source of the Common Ground Problem: a System Repo changes its System Kit Copies, and the System Kit Copy Change has to reach the Maintainer Repo and be judged there. What the System Repo needs then comes back to it in a System Kit Update. Other sources exist, such as a birth, a lesson found in the Maintainer Repo's own work, or new knowledge from the human. They are left on purpose until this problem is finished (`TODO.md`, the item on resuming the simulation).

A System Kit Copy Change is followed in six parts: change, read, judge, act on the verdicts, deliver, and take. Its cases are of two kinds:

- **What was changed:** these vary how the System Repo records its System Kit Copy Change, and how the Maintainer Repo finds it. They are the same however deep the System Kit Copy Change turns out to go, since that is known only once it is judged.
- **How deep it goes:** these vary how the Maintainer Repo decides, and how the System Kit Update is written.

The cases are simulated in `temp/common-ground/system-repo-change-simulation.md`, and the rules above are written from it.

**Taken into account:** the cases the rules have been checked against. None is finished yet.

**Not taken into account:** the other sources named above, and each case sent to TODO, with its why. None is sent yet.

### 2.2 Today and what to check

Today the Maintainer Repo is `correctness-by-construction`. Its concept is correctness by construction, written in plain words. It holds documents only, no code.

Its two groups of understanding, agent work and the concept, are split today. They may turn out to be one understanding, sorted into two groups.

It describes the three levels of understanding itself, in its Idea-to-Output Model (`docs/models/idea-to-output.md`, §2).

For Knowledge on Trial it has the Approach on Trial: one text for work done for the first time, written in a System Repo or here, and for ways of working only. Whether that meets the Repo Responsibility, and what other Knowledge on Trial needs, is a check for the next step.

Seen already, three Repo Responsibility Gaps:

- one convention manual, the middle level for one way of working, is written for both repos at once, the Maintainer Repo and every System Repo, though the two need different things from it: one middle serving two repos (Failure Case 15);
- two of the repo's texts give one name two scopes. "Canonical Description" is the middle level only in the Idea-to-Output Model, §2, but in the glossary it covers the Idea Models too (Failure Case 8);
- the concept, `concept/`, holds the project-agnostic understanding of CBC system design and its backend case in one text, not split. Its examples and words lean toward software. Which parts are project-agnostic and which are the backend case is sorted in the next step.

What the Maintainer Repo has today, for each Defined Term of the intent:

| Defined Term | In the Maintainer Repo today |
|---|---|
| Maintainer Repo | the Concept Deliverer, a Concept Repo by its Tiers Model: `correctness-by-construction` |
| Maintainer Repo Register | the list of CBC Runs (`ARCHITECTURE.md` §2.5, *The CBC Runs*). Its *settled snapshot* is today's Read-Through Commit, kept in the CBC Run instead |
| System Repo | a CBC Run |
| System Kit | the delivery, `delivery/`: the Container Group, the Method Group and a Stack Group, with the concept and each group's Glossary Names |
| System Kit Copy | a CBC Run's copy of a Master Copy |
| System Kit Copy Change | a CBC Run's edit to a copy (`docs/conventions/exchange/` §5.1, *When a copy may be edited*) |
| System Kit Copy Change Record | the edit's line in the CBC Run's Decisions Log (`docs/conventions/exchange/` §5.1, *When a copy may be edited*) |
| System Kit Attention Note | a CBC Run Ask with no edit behind it, such as a question (`docs/conventions/exchange/` §5.1, *When a copy may be edited*) |
| System Kit Update | a delivery |
| System Kit Update Note | the Delivery Note |
| System Kit Version | the Delivery Pin: the Concept Deliverer's commit a CBC Run's copies equal |
| Instruction Text | a Work Approach: an Agent Skill, an Agent Rule, an Approach on Trial or an Output Form. Which of the three sorts an Output Form is, is open |
| Task Instruction Text | an Agent Skill |
| Session Instruction Text | the Entry File, `CLAUDE.md`; an Agent Rule loaded in every session; the human's private working rules |
| File Instruction Text | an Agent Rule loaded by path, when a file it names is opened |
| Knowledge on Trial | the Approach on Trial, for ways of working only |
| Backbone Idea and Work Domain Idea, the layers model's Names | an Idea Model, `docs/models/`; the concept, `concept/`, with its backend case inside it |
| Adapted Case | no one thing: a convention manual, with the Work Approaches made from it |
| Adapted Understanding Text | a convention manual, `docs/conventions/` |
| Defined Term | a Glossary Name, in `docs/glossary.md` |
| One Home per Fact | the facts-in-sync convention, and the one-home Agent Rule |
| Knowledge Drift Repair | the Foundation Check and its Change Walk at each commit; the refinement's reads of the whole repo |
| System Repo Reading | a CBC Run Reading |
| birth of a System Repo | a CBC Run Birth |

## 3. The Knowledge Axes

Where text is kept today, in the Maintainer Repo, on each of the five Knowledge Axes, which §3.1 to §3.5 explain. Every text should have a place on each Knowledge Axis; one that doesn't is a finding. A text not yet sorted by layer waits for today's Maintainer Repo to be brought into the layers model (`TODO.md`, the item on the layers of knowledge).

| Where it's kept | Kind | Time | Who uses it | Where | Layer |
|---|---|---|---|---|---|
| Understanding files in the repo, such as the concept's chapters and the convention manuals | understanding | now | both | the Maintainer Repo | not yet sorted: the concept holds layers 1 and 2 in one text |
| Instruction Texts, of all three sorts; today, Agent Skills and Agent Rules | instruction | now | the agent acts on it; the human checks what they told it | the Maintainer Repo; as System Kit Copies in each System Repo, for those in the System Kit | 3 |
| Devlog, the journal of the work, and commit messages | understanding | before | both, seldom | the Maintainer Repo; each System Repo keeps its own | open (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 6) |
| TODO, the backlog | understanding | later | both | the Maintainer Repo; each System Repo keeps its own | open, as the devlog's |
| The human's private working rules | instruction | now | the agent acts on it; the human wrote it | the Maintainer Repo | not yet sorted |
| The agent's memory | both | now | the agent; the human rarely | the Maintainer Repo's work, outside its files | not yet sorted |
| Knowledge on Trial; today, in the Maintainer Repo, the Approach on Trial, for ways of working only | both | now, unchecked | the agent works by it; the human judges it | the Maintainer Repo, or a System Repo | 3 |
| System Kit Copy | mostly instruction; the concept and the Defined Terms are understanding | now | the agent in the System Repo | each System Repo | 3, used in 4 |
| The Repo Responsibility, §2's lists | understanding | later | both | the Maintainer Repo | not yet sorted |

### 3.1 Who uses the text

The text is the interface between the human's mind and the agent, the means by which they reach common ground (§1). Each uses it differently.

For the human, the text is, so far:

- how they see something, and how they understand it;
- where they are with it, at the Depth of Understanding each idea needs;
- not always correct;
- what they recall from.

For the agent, the text is, so far:

- what the human knows, and at what Depth of Understanding: the agent's side of common ground;
- where to start helping: applying the idea, learning more of it, keeping it up, going deeper, and anything else done with it.

The agent usually knows more about the subject than the text says.

Each list holds what has been found so far; more may come.

The text is also the agent's interface with itself, from one session to the next. What the agent learns in a session reaches the next only if it is written down.

Some of that text is kept outside the repo: the agent's own memory, notes it writes for itself about working with the human, such as "never push" or "explain simpler first". The human rarely reads them. They overlap the human's own working rules and the repo's Session Instruction Texts, and they can go stale like any other text.

### 3.2 The time of knowledge

Knowledge has a time too:

- before: what was known or thought in the past;
- now: what is known or thought now, not always checked;
- later: what is meant to be learned, or checked, afterwards.

A Knowledge Time Shift is where knowledge gets lost. If a Knowledge Time Shift isn't written down, the old text keeps claiming now.

New knowledge enters in several ways, so far: the human learns, a talk ends in a decision, the agent finds something in the work, a System Repo shows something the Maintainer Repo reads back, or knowledge is used as Knowledge on Trial (§3.3).

Before keeps why it changed, not only what was thought. Without that why, a reader afterwards sees what changed but not the reason: the why goes missing (§4), this time between before and now.

Now has degrees of certainty: what is thought now isn't always what is known. Some of now is unchecked, and later holds what should be checked.

What before is for, so far:

- not repeating a mistake: a dead end marked as one isn't tried again;
- knowing why now is as it is: when a past decision is questioned, its reasons and what was rejected are there;
- seeing where the human has been: the path of their understanding, which helps the agent judge their Depth of Understanding now;
- resuming work: where it stopped, and what was tried;
- going back: undoing to an earlier state;
- evidence: what things cost, so a choice can be judged.

### 3.3 The kind of text

Text comes in two kinds, so far:

- understanding: what is known, and how it is understood;
- instruction: text built on understanding, to apply it.

How close a text is to an idea's backbone is a Knowledge Axis of its own, the layer (§3.5).

An instruction has two readers too. The agent acts on it. The human reads it to know what they told the agent.

Some instructions are followed by the human alone, such as the steps of a birth that a human can run without the agent. Instruction Text, what the agent acts on, does not cover them. Whether they need a Defined Term of their own is open.

The two kinds go wrong differently. Understanding may be not always correct and still do its job. An instruction must be faithful to its understanding, since the agent acts on it as it stands. It is only as right as that understanding: Mistaken Knowledge passes into a faithful instruction unseen.

While knowledge is on trial, a text can be both kinds: a way of working tried for the first time is written as one text, an instruction with its understanding inside it. It is split only when it is judged, since what is not yet understood cannot be split.

Some understanding is about the agent itself: how a change works, in four steps, `decide ──▶ make ──▶ check ──▶ record`; how a session starts empty; what loads when. Here the agent teaches the human. From what the human then understands, the two write instructions together, such as how a change is recorded.

An instruction stands on its understanding. When the understanding moves on, the instruction can go stale without anyone seeing it. An instruction that carries the whole why grows long.

One understanding can give several instructions. When each instruction retells the understanding, the same knowledge is written several times, and they can disagree.

An instruction can be copied to other repos, for the agents working there, with the adapted understanding it stands on. Each copy can drift from the understanding it came from, and can change on its own.

### 3.4 Where the text is

A text is kept in the Maintainer Repo, or in a System Repo. Some is in both: what the Maintainer Repo ships becomes a System Kit Copy in each System Repo, and System Kit Copy Changes come back only when the Maintainer Repo reads them.

Some failures can happen in either repo. Others happen only between the two: a System Kit Copy drifts from its original; the Maintainer Repo judges a System Kit Copy Change wrongly, as a lesson when it was specific to the System Repo, or the other way round; work resumes in a System Repo without a System Kit Update.

The two repos are not the two sides of §1. The human and the agent work in both.

### 3.5 The layer of text

A text also sits in a layer of knowledge, by how close it is to an idea's backbone: from layer 1, bound to no Work Domain, to layer 4, the work done by a text. What each layer holds, and where each is kept, is the layers model's (`temp/common-ground/knowledge-layers.md` §2, *The layers*).

## 4. What goes wrong

Most of what goes wrong is Knowledge Drift, but not every failure here is. In Failure Case 11 the text matches the knowledge, but the knowledge is wrong: Mistaken Knowledge. Knowledge Drift is fixed by bringing the text up to the knowledge; Mistaken Knowledge is fixed in the knowledge first.

A third failure sits outside the text: a Repo Responsibility Gap (§2). It is fixed in the repo, or in the Repo Responsibility, and it can cause Knowledge Drift. The next step of this work checks it first (§6).

- **When the text holds less than the knowledge, the why goes missing.** An Instruction Text is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **When the text is older than the knowledge, it goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. The agent then reads it as true and acts on it. This is felt as the bigger problem; §6 tests it. A text goes stale when its time is wrong: it still reads as now after the knowledge has moved on.

Wrong understanding is not, by that alone, the problem. Understanding that is incomplete or not correct, but honestly shows where the human is, does its job. An instruction is different: the agent acts on it as it stands (§3.3). The problem is text that no longer matches where the human is, or that the agent treats as settled fact.

A failure shows in one of three Text Life Phases: two moments, *writing* and *reading*, and the stretch between them, *aging*.

- *Writing:* knowledge goes into text, and part of it is lost, such as the why.
- *Aging:* the knowledge moves on, and the text grows older than it.
- *Reading:* the agent reads the text and builds a different understanding from it than the human holds.

The interface between the human's mind and the agent breaks in these Failure Cases, found by thinking it through, each to be tested against real sessions (§6). Each is tagged with the Text Life Phase it breaks in, the Knowledge Axis it lives on (§3), and where: in either repo, or between the Maintainer Repo and a System Repo (§3.4):

| Failure Case | Text Life Phase | Knowledge Axis | Where |
|---|---|---|---|
| 1. The human knows something the text doesn't hold. | writing | who uses it | either |
| 2. The text is older than the human's understanding: they have moved on. | aging | time | either |
| 3. The agent's context is older than the text: it read the text earlier in the session, or from a summary, and the text has changed since. | aging | who uses it | either |
| 4. The text is ahead of the human: the agent wrote it, and it holds the agent's understanding, not the human's. | writing | who uses it | either |
| 5. The text misses the human's Depth of Understanding: too thin to recall from, or too dense to read. | writing | who uses it | either |
| 6. The text is wrong, and the agent treats it as true instead of suggesting a fix. | reading | who uses it | either |
| 7. The agent reads the text and builds a different understanding from it than the human meant. | reading | who uses it | either |
| 8. Two texts disagree, and neither says which one is where the human is now. | aging | time | either |
| 9. The text holds the what, not the why. | writing | kind | either |
| 10. An instruction still applies understanding that has moved on. | aging | kind | either |
| 11. An instruction is faithful to Mistaken Knowledge, and neither side sees it until the work shows it. | writing | kind | either |
| 12. A Knowledge Time Shift isn't written down: what was learned still sits in later, or replaced understanding isn't kept as before. | writing | time | either |
| 13. The agent reads a before text as now, such as an old journal entry taken as current. | reading | time | either |
| 14. The agent reads understanding as an instruction, such as the human thinking aloud, in chat or in text, taken as an order, or applies an instruction where it wasn't meant to. | reading | kind | either |
| 15. One understanding text serves repos whose needs differ, and a change made for one changes the other. | writing | where | between |
| 16. One instruction covers several tasks, and a change made for one task changes the others. | writing | kind | either |
| 17. A later text is read as now: what is meant to be is taken for what is. | reading | time | either |
| 18. Unchecked knowledge is read as checked, such as Knowledge on Trial taken as proven. | reading | time | either |
| 19. A System Kit Copy drifts from its original. | aging | where | between |
| 20. The Maintainer Repo judges a System Kit Copy Change wrongly: a lesson taken as specific to the System Repo, or something specific taken as a lesson. | reading | where | between |
| 21. Work resumes in a System Repo without reading back and updating first, and goes on from its old System Kit Copy. | aging | where | between |
| 22. A System Kit Copy Change reaches the Maintainer Repo without its why: the System Repo wrote down what it changed, not why. | writing | where | between |
| 23. An adapted understanding lags behind its project-agnostic idea, which has moved on. | aging | layer | either |
| 24. A project-agnostic idea is bent to one project's needs, and no longer fits the others. | writing | layer | between |
| 25. The agent reads a text at the wrong layer, such as a line of an Adapted Case taken as true for the whole idea it was adapted from, or the other way round. | reading | layer | either |

The same Failure Cases by Text Life Phase and Knowledge Axis. Every cell has a Failure Case; an empty one would point at a missing Failure Case:

| | who uses it | time | kind | where | layer |
|---|---|---|---|---|---|
| **writing** | 1, 4, 5 | 12 | 9, 11, 16 | 15, 22 | 24 |
| **aging** | 3 | 2, 8 | 10 | 19, 21 | 23 |
| **reading** | 6, 7 | 13, 17, 18 | 14 | 20 | 25 |

Seen on 2026-11-05: Failure Case 1, the purpose of an earlier attempt to rebuild the Maintainer Repo's way of working, written nowhere for 3 days; Failure Cases 4 and 5, the agent's dense answers, until the human said they had lost common ground.

## 5. What was tried

The Maintainer Repo keeps One Home per Fact, with a reference wherever another text needs the fact. It was built without full consideration, and it is felt to have cost too much to keep here; §6 tests where that cost comes from:

- **Finding is cheap, judging is not.** A search lists every place that points at a fact. Whether each place still holds needs reading. The Maintainer Repo has 398 section references pointing at 129 sections. The most pointed-at section has 22.
- **The fix becomes a loop.** A change in one referring place can force the home to change. Then every other reference has to be checked again. If they disagree, it's back to the home, and so on. A decision has to be weighed across many places, not taken in one pass.
- **It multiplies.** When references start disagreeing with each other, each disagreement starts its own loop.
- **A Knowledge Drift Repair starts with a sweep.** Every finding it makes can start a loop.

## 6. Where it may be wrong

The next step of this work tests these against the Maintainer Repo's history: the devlog's notes of what each session lacked, and the findings of past reviews of the Maintainer Repo:

- how often stale text actually hurt a session, and how;
- where staleness comes from: a retelling that drifted, a home that was wrong, or something never written down;
- whether every text must stay true, or only what the agent acts on;
- whether the cost lies in One Home per Fact itself, or in how it's kept, such as the sweep;
- whether only now decides that a change is needed, with before as input and not authority;
- when checking before costs more than it gives, and whether it can harm: by what reading it costs, by anchoring new thinking to old framing, or by being read as now;
- which parts of before pay, and which aren't worth keeping. The Maintainer Repo's devlog alone is 8,773 lines, after 4 months;
- whether the middle level is needed for every idea, or only for an idea that serves projects with different needs;
- whether a System Kit Update taken only when work resumes in a System Repo still holds when more than one project runs at once, or someone other than the human works in a System Repo;
- whether part of the cost of One Home per Fact comes from levels missing or merged: an instruction written straight from a project-agnostic idea is reread whenever the idea changes.

## 7. What would show it's solved

First checks only. They are refined once the next step shows which Failure Cases really happen. Each line can be checked:

- A new session continues without the human retelling. Count the retellings and corrections in each session.
- Behind each Instruction Text, its why can be found.
- The cost of one change stays about the same as the repo grows.

## 8. Options to consider

Answers met while stating the problem, kept to be weighed, not chosen:

- write an instruction only when work needs one, and keep it short;
- keep the why in the understanding, not in the instruction;
- let an instruction point up to its understanding instead of retelling it. How this differs from One Home per Fact (§5) is open.
- keep a middle level for an idea that serves projects with different needs, and none for an idea only one project uses. Weighed so far:

  | | With a middle level | Without one |
  |---|---|---|
  | The project-agnostic idea | written once, fits any project | bent to fit each project, or repeated in each |
  | One idea, two projects with different needs | each gets its own adapted text | one text serves both (Failure Case 15) |
  | A change to the project-agnostic idea | reread the adapted texts, a few | reread every instruction |
  | Its cost | one more level to keep, and drift between levels (Failure Cases 23 and 24) | the project-agnostic idea retold everywhere |
