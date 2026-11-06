# The problem: keeping what we know true

<!-- A draft: the problem of the Plan Step "Find how what we know
     stays true", its stage 1, in the reviewer's words. Built from
     TODO-CONVERSATION-MEMORY.md §31, *Keeping what we know true*,
     and from what temp/idea-model-problem.md says of the problem,
     not of a model. Polished one insight at a time, each a commit,
     so the diffs show what changed. It states the problem only: an
     answer met on the way is kept as an option to consider (§8),
     not chosen. Its
     home is decided when the Plan Step closes; it goes then, and
     git keeps every version. -->

This text states one problem: how what a human and an agent know stays true, and shared, from one session to the next. It proposes no answer.

## Names

A capitalized Name is defined here, once; a lowercase word is plain English; an *italic* word is a label inside the Name it belongs to. The Names are local to this text, a trial for TODO's item *Decide which names go in the glossary, and how a name one text uses alone is kept apart*, and each was checked against the repo's glossary. A definition names what it builds on by its Name, never by where it stands in the text, such as "the same idea" or "the two".

Plain words, in a narrow sense:

- **knowledge:** what one knows, and how one understands it. It lives in a head.
- **text:** where knowledge is stored, as it stood at one moment: Understanding Text and Instruction Text, wherever kept.
- **the chat:** where knowledge passes between the human and the agent; lost when a session ends, unless written down. Not text.
- **the human:** the person whose knowledge it is, who carries it from one session to the next.
- **the agent:** the AI model in a session. It knows its subjects from training, and the human and the work only from what it reads.
- **common ground:** between the human and the agent, on what the human knows: the agent's picture of the human's understanding, built from the text, matches it and its Depth of Understanding.

Names, in order of first use:

- **Depth of Understanding:** how deep someone's understanding of an idea goes: basics for one, details for another.
- **CBC Run:** a repo that builds a real system by the concept, starting from what this repo ships. This repo's glossary Name.
- **Understanding Text:** text that holds what is known, and how it is understood.
- **Instruction Text:** text built on an Understanding Text, to apply it; what the agent acts on. Agent Skills and rules are Instruction Texts.
- **General Understanding Text:** an Understanding Text bound to no project.
- **Adapted Understanding Text:** a General Understanding Text narrowed to one project's needs; the middle level between General Understanding Text and Instruction Text.
- **Shipped Copy:** an Instruction Text this repo ships, as it lives in a CBC Run.
- **Repo Intent:** what this repo and each CBC Run are meant to keep (§2). Its *time* is *later*, not the repo today.
- **Failure Case:** one way the human and the agent lose their common ground, numbered in §4.
- **Knowledge on Trial:** new knowledge used before it is judged: a way of working, an Understanding Text, or a text's form.
- **Knowledge Axis:** one way of sorting text. There are four: *who uses it*, *time*, *kind*, *where* (§3).
- **Knowledge Move:** knowledge changing *time*: *later* to *now* when learned or checked, *now* to *before* when replaced.
- **Knowledge Drift:** text and knowledge moving apart. The text holds less than the knowledge, or is older than it.
- **Knowledge Drift Repair:** bringing text back in line with the knowledge, so common ground can be built from it again: finding where it drifted, judging each place, deciding with the human what changes, and fixing it. Today the finding is a sweep: one or more agents read the whole repo.
- **Knowledge Drift Phase:** where Knowledge Drift happens: *writing*, *aging*, *reading*.
- **Mistaken Knowledge:** knowledge that is itself wrong, carried faithfully into text. It is not Knowledge Drift.
- **Repo Intent Drift:** the repo not being what Repo Intent says. It is fixed in the repo, or in the Repo Intent.
- **One Home per Fact:** this repo's practice: each fact in one text, its home, with every other text pointing there.

Labels:

- *who uses it*: *the human*, *the agent*, *both*
- *time*: *before*, *now*, *later*
- *kind*: Understanding Text, Instruction Text
- *where*: *this repo*, *a CBC Run*; a Failure Case is *either* or *between*
- Knowledge Drift Phase: *writing*, *aging*, *reading*

## 1. The purpose

Knowledge is what one knows, and how one understands it. It lives in a head. Text is where it is stored, as it stood at one moment.

Text here is understanding and instruction (§3.3), wherever it is kept. So far it is kept in the repo's files, in commit messages, in the human's private working rules, and in the agent's memory.

The chat is not text. It is where knowledge passes between the human and the agent, and it is lost when the session ends unless something is written down.

Two sides work with the knowledge:

- **The human:** the person whose knowledge it is. They learn, decide, and carry the knowledge from one session to the next.
- **The agent:** the AI model working in a session. It knows its subjects from its training, but starts each session knowing the human and the work only from what it reads.

The purpose is common ground between the human and the agent on what the human knows, and how deeply, from one session to the next. Both learn, and write down what they learn. A new session reads it, and the human doesn't have to retell it. Both continue improving from there.

The problem holds wherever a human works with an agent across sessions. This repo is where it is seen first, and where it is tested.

## 2. This repo as intended

This repo, `correctness-by-construction`, holds one concept, correctness by construction, written in plain words, and what is made from it. It holds documents only, no code. Other repos, each a CBC Run, or run for short, build real systems by the concept. Each starts from what this repo ships, and what it learns is read back here.

Among its instructions are Agent Skills and rules. An Agent Skill is an instruction the agent loads for a task; a rule is one it loads in every session.

Its understanding falls in two groups. Each gives instructions in two places, this repo and each CBC Run:

| Understanding | Instructions for this repo | Instructions shipped to each CBC Run |
|---|---|---|
| How work is done with an agent: a change, a commit, a plan | this repo's own Agent Skills and rules | the Container Group: the setup for the agent in a run, its Agent Skills, rules and records |
| How a CBC system is designed: the concept and its methods | none | the methods, such as the cbc-framing and cbc-slice Agent Skills |

The two groups are split today. They may turn out to be one understanding, sorted into two groups.

Between understanding and instruction, this repo means to keep a middle level, for both groups. It describes the three levels itself, in its Idea-to-Output Model (`docs/models/idea-to-output.md`, §2):

| Level | What it holds | In this repo |
|---|---|---|
| understanding, general | an idea any repo can adapt (§3.3) | the Idea Models, `docs/models/` |
| the middle | understanding adapted to one repo's needs (§3.3) | the convention manuals, `docs/conventions/`; the concept, `concept/` |
| instruction | how a piece of work is done, for the agent | Agent Skills, rules, the Approach on Trial |

Each idea can then live in three texts, not two. Whether the levels are kept apart as meant is checked in the next step.

So knowledge written here becomes instructions that agents act on in other repos. The agent in a CBC Run starts with none of this repo's context, only what was shipped, and the copies there can drift, or change on their own.

What each repo is meant to keep: the system as we mean it to be. This is later knowledge (§3.2), what should be, not a description of the repo today, and the intent itself may change. Whether the repo does all of it is not yet checked.

This repo keeps:

1. understanding of agent work;
2. understanding of the concept, CBC system design;
3. delivery: instructions made from both, general enough to reuse in any project built by the concept;
4. its own instructions, from the understanding of agent work, updated as that understanding changes;
5. findings from runs. A run uses the instructions in practice, and changes them as its problems demand, without the understanding to judge whether a change is right. This repo reads the changes and concludes one of two things:
   - a lesson: the understanding is updated, then the delivered instructions, so future runs don't repeat a mistake or miss the same thing;
   - specific to that run's problem: the change is rejected, and the understanding and the delivery stay as they are;
6. updates for runs already running: when delivery changes, a run born earlier gets the change, or keeps working from its old copy;
7. its own records: the history and the backlog of this work.
8. its knowledge on trial, from runs and its own, judged here. Its form for work done for the first time is the Approach on Trial: one text, written in a run or here. That is what the repo has today; whether it meets this intent, and what other knowledge on trial needs, is checked in the next step. Each stays on trial for more uses, lands as new understanding, or lands in pieces, added to understanding texts that already exist, or is dropped. A landing is a moment for a Knowledge Drift Repair of what it touches, here and in the runs' copies. This repo also judges its own knowledge on trial, with no outside judge. A run's, once judged here, reaches back to that run by an update, or the run keeps working from its own version.

Each CBC Run:

1. keeps no understanding of agent work. It uses the instructions, and may change them;
2. gets the concept's understanding, to explain its problems. Whether a run may change that understanding, since it uses it directly, is open;
3. keeps understanding of its own problem: one specific system's design;
4. keeps its own records, from the setup it was shipped;
5. puts knowledge on trial, uses each until this repo judges it, and offers it back. This repo's form for it today is the Approach on Trial, for ways of working only.

Seen already, where the repo differs from that intent:

- one convention manual, the middle level for one way of working, is written for both repos at once, this repo and every CBC Run, though the two need different things from it: one middle serving two repos (case 15);
- two of the repo's texts give one name two scopes. "Canonical Description" is the middle level only in the Idea-to-Output Model, §2, but in the glossary it covers the Idea Models too (case 8).

## 3. The axes of knowledge

Where text is kept so far, on each of the four axes, which §3.1 to §3.4 explain. Every text should have a place on each axis; one that doesn't is a finding.

| Where it's kept | Kind | Time | Who uses it | Where |
|---|---|---|---|---|
| Understanding files in the repo, such as the concept's chapters and the convention manuals | understanding | now | both | this repo |
| Agent Skills and rules | instruction | now | the agent acts on it; the human checks what they told it | this repo, and a copy in each run of those it ships |
| Devlog, the journal of the work, and commit messages | understanding | before | both, seldom | this repo; each run keeps its own |
| TODO, the backlog | understanding | later | both | this repo; each run keeps its own |
| The human's private working rules | instruction | now | the agent acts on it; the human wrote it | this repo |
| The agent's memory | both | now | the agent; the human rarely | this repo's work, outside its files |
| Knowledge on trial; today, in this repo, the Approach on Trial, for ways of working only | both | now, unchecked | the agent works by it; the human judges it | this repo, or a run |
| A shipped copy | instruction | now | the agent in the run | each run |
| The intent, §2's lists | understanding | later | both | this repo |

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

Some of that text is kept outside the repo: the agent's own memory, notes it writes for itself about working with the human, such as "never push" or "explain simpler first". The human rarely reads them. They overlap the human's own working rules and the repo's rules, and they can go stale like any other text.

### 3.2 The time of knowledge

Knowledge has a time too:

- before: what was known or thought in the past;
- now: what is known or thought now, not always checked;
- later: what is meant to be learned, or checked, afterwards.

Knowledge moves between the times, and the move is where it gets lost:

- later becomes now when something is learned or checked;
- now becomes before when it is replaced.

If a move isn't written down, the old text keeps claiming now.

New knowledge enters in several ways, so far: the human learns, a talk ends in a decision, the agent finds something in the work, a run shows something this repo reads back, or knowledge is put on trial (§3.3).

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
- instruction: text built on understanding, to apply it. Agent Skills and rules are instructions.

Understanding can have levels, so far:

- general: an idea bound to no project;
- adapted: the same idea narrowed to one project's needs, such as this repo's upkeep or a run's work.

An instruction comes from the adapted level where there is one, and the adapted level from the general.

An instruction has two readers too. The agent acts on it. The human reads it to know what they told the agent.

The two kinds go wrong differently. Understanding may be not always correct and still do its job. An instruction must be faithful to its understanding, since the agent acts on it as it stands. It is only as right as that understanding: Mistaken Knowledge passes into a faithful instruction unseen.

New knowledge can be used before it is judged: knowledge on trial. It may be a way of working, an understanding, or the form of a text. While it is new, a text can be both kinds: a way of working tried for the first time is written as one text, an instruction with its understanding inside it. It is split only when it is judged, since what is not yet understood cannot be split.

Some understanding is about the agent itself: how a change works, in four steps, `decide ──▶ make ──▶ check ──▶ record`; how a session starts empty; what loads when. Here the agent teaches the human. From what the human then understands, the two write instructions together, such as how a change is recorded.

An instruction stands on its understanding. When the understanding moves on, the instruction can go stale without anyone seeing it. An instruction that carries the whole why grows long.

One understanding can give several instructions. When each instruction retells the understanding, the same knowledge is written several times, and they can disagree.

An instruction can be copied to other repos, for the agents working there. Each copy can drift from the understanding it came from, and can change on its own.

### 3.4 Where the text is

A text is kept in this repo, or in a run. Some is in both: what this repo ships becomes a copy in each run, and a run's changes come back only when this repo reads them.

Some failures can happen in either repo. Others happen only between the two: a run's copy drifts from what was shipped; this repo judges a run's change wrongly, as a lesson when it was specific to the run, or the other way round; an update never reaches a run already running.

The two repos are not the two sides of §1. The human and the agent work in both.

## 4. What goes wrong

Most of what goes wrong is one drift: the text and the knowledge drift apart. Not every failure here is Knowledge Drift. In case 11 the text matches the knowledge, but the knowledge is wrong: Mistaken Knowledge. Drift is fixed by bringing the text up to the knowledge; Mistaken Knowledge is fixed in the knowledge first.

A third failure sits outside the text: the repo itself may not be what it is meant to be (§2). It is fixed in the repo, or in the intent, and it can cause drift. The next step of this work checks it first (§6).

- **When the text holds less than the knowledge, the why goes missing.** An Agent Skill is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **When the text is older than the knowledge, it goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. The agent then reads it as true and acts on it. This is felt as the bigger problem; §6 tests it. A text goes stale when its time is wrong: it still reads as now after the knowledge has moved on.

Wrong understanding is not, by that alone, the problem. Understanding that is incomplete or not correct, but honestly shows where the human is, does its job. An instruction is different: the agent acts on it as it stands (§3.3). The problem is text that no longer matches where the human is, or that the agent treats as settled fact.

The drift happens in three phases of a text's life: two moments, writing and reading, and the stretch between them, aging.

- **Writing:** knowledge goes into text, and part of it is lost, such as the why.
- **Aging:** the knowledge moves on, and the text grows older than it.
- **Reading:** the agent reads the text and builds a different understanding from it than the human holds.

The drift breaks the interface between the human's mind and the agent in these cases, found by thinking it through, each to be tested against real sessions (§6). Each is tagged with the phase it breaks in, the axis of §3 it lives on, and where: in either repo, or between this repo and a run (§3.4):

| Case | Phase | Axis | Where |
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
| 12. A move between times isn't written down: what was learned still sits in later, or replaced understanding isn't kept as before. | writing | time | either |
| 13. The agent reads a before text as now, such as an old devlog entry taken as current. | reading | time | either |
| 14. The agent reads understanding as an instruction, such as the human thinking aloud, in chat or in text, taken as an order, or applies an instruction where it wasn't meant to. | reading | kind | either |
| 15. One understanding text serves repos whose needs differ, and a change made for one changes the other. | writing | where | between |
| 16. One instruction covers several tasks, and a change made for one task changes the others. | writing | kind | either |
| 17. A later text is read as now: what is meant to be is taken for what is. | reading | time | either |
| 18. Unchecked knowledge is read as checked, such as knowledge on trial taken as proven. | reading | time | either |
| 19. A run's copy of a shipped instruction drifts from what was shipped. | aging | where | between |
| 20. This repo judges a run's change wrongly: a lesson taken as specific to the run, or something specific taken as a lesson. | reading | where | between |
| 21. An update never reaches a run already running, which works on from its old copy. | aging | where | between |
| 22. A run's change reaches this repo without its why: the run wrote down what it changed, not why. | writing | where | between |
| 23. An adapted understanding lags behind its general idea, which has moved on. | aging | kind | either |
| 24. A general idea is bent to one project's needs, and no longer fits the others. | writing | kind | between |

The same cases by phase and axis. Every cell has a case; an empty one would point at a missing case:

| | who uses it | time | kind | where |
|---|---|---|---|---|
| **writing** | 1, 4, 5 | 12 | 9, 11, 16, 24 | 15, 22 |
| **aging** | 3 | 2, 8 | 10, 23 | 19, 21 |
| **reading** | 6, 7 | 13, 17, 18 | 14 | 20 |

Seen on 2026-11-05: case 1, the purpose of an earlier attempt to rebuild this repo's way of working, written nowhere for 3 days; cases 4 and 5, the agent's dense answers, until the human said they had lost common ground.

## 5. What was tried

This repo keeps One Home per Fact, with a reference wherever another text needs the fact. It was built without full consideration, and it is felt to have cost too much to keep here; §6 tests where that cost comes from:

- **Finding is cheap, judging is not.** A search lists every place that points at a fact. Whether each place still holds needs reading. This repo has 398 section references pointing at 129 sections. The most pointed-at section has 22.
- **The fix becomes a loop.** A change in one referring place can force the home to change. Then every other reference has to be checked again. If they disagree, it's back to the home, and so on. A decision has to be weighed across many places, not taken in one pass.
- **It multiplies.** When references start disagreeing with each other, each disagreement starts its own loop.
- **A Knowledge Drift Repair starts with a sweep.** Every finding it makes can start a loop.

## 6. Where it may be wrong

The next step of this work tests these against this repo's history: the devlog's notes of what each session lacked, and the findings of past reviews of this repo:

- how often stale text actually hurt a session, and how;
- where staleness comes from: a retelling that drifted, a home that was wrong, or something never written down;
- whether every text must stay true, or only what the agent acts on;
- whether the cost lies in One Home per Fact itself, or in how it's kept, such as the sweep;
- whether only now decides that a change is needed, with before as input and not authority;
- when checking before costs more than it gives, and whether it can harm: by what reading it costs, by anchoring new thinking to old framing, or by being read as now;
- which parts of before pay, and which aren't worth keeping. This repo's devlog alone is 8,773 lines, after 4 months;
- whether the middle level is needed for every idea, or only for an idea that serves projects with different needs;
- whether part of the cost of One Home per Fact comes from levels missing or merged: an instruction written straight from a general idea is reread whenever the idea changes.

## 7. What would show it's solved

First checks only. They are refined once the next step shows which cases really happen. Each line can be checked:

- A new session continues without the human retelling. Count the retellings and corrections in each session.
- Behind each Agent Skill, its why can be found.
- The cost of one change stays about the same as the repo grows.

## 8. Options to consider

Answers met while stating the problem, kept to be weighed, not chosen:

- write an instruction only when work needs one, and keep it short;
- keep the why in the understanding, not in the instruction;
- let an instruction point up to its understanding instead of retelling it. How this differs from One Home per Fact (§5) is open.
- keep a middle level for an idea that serves projects with different needs, and none for an idea only one project uses. Weighed so far:

  | | With a middle level | Without one |
  |---|---|---|
  | The general idea | written once, fits any project | bent to fit each project, or repeated in each |
  | One idea, two projects with different needs | each gets its own adapted text | one text serves both, case 15 |
  | A change to the general idea | reread the adapted texts, a few | reread every instruction |
  | Its cost | one more level to keep, and drift between levels, cases 23 and 24 | the general idea retold everywhere |
