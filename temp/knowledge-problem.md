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

## 1. The purpose

Knowledge is what one knows, and how one understands it. It lives in a head. Text is where it is stored: a copy, made at one moment.

Text here is understanding and instruction (§3.3), wherever it is kept. So far it is kept in the repo's files, in commit messages, in the human's private working rules, and in the agent's memory.

The chat is not text. It is where knowledge passes between the human and the agent, and it is lost when the session ends unless something is written down.

Two sides work with the knowledge:

- **The human:** the person whose knowledge it is. They learn, decide, and carry the knowledge from one session to the next.
- **The agent:** the AI model working in a session. It knows its subjects from its training, but starts each session knowing the human and the work only from what it reads.

The human and the agent are on the same page when the agent's picture of the human's understanding, built from the text, matches that understanding and its level, how deep it goes. Both learn, and write down what they learn. A new session reads it, and the human doesn't have to retell it. Both continue improving from there.

The problem holds wherever a human works with an agent across sessions. This repo is where it is seen first, and where it is tested.

## 2. The first case

This repo, `correctness-by-construction`, holds one concept, correctness by construction, written in plain words, and what is made from it. It holds documents only, no code. Other repos, each a CBC Run, or run for short, build real systems by the concept. Each starts from what this repo ships, and what it learns is read back here.

Among its instructions are Agent Skills and rules. An Agent Skill is an instruction the agent loads for a task; a rule is one it loads in every session.

Its understanding falls in two groups. Each gives instructions in two places, this repo's and each CBC Run's, which this repo calls its Convention Seats:

| Understanding | Instructions for this repo | Instructions shipped to each CBC Run |
|---|---|---|
| How work is done with an agent: a change, a commit, a plan | this repo's own Agent Skills and rules | the Container Group: the setup for the agent in a run, its Agent Skills, rules and records |
| How a CBC system is designed: the concept and its methods | none | the methods, such as the cbc-framing and cbc-slice Agent Skills |

The two groups are split today. They may turn out to be one understanding, sorted into two groups.

So knowledge written here becomes instructions that agents act on in other repos. The agent in a CBC Run starts with none of this repo's context, only what was shipped, and the copies there can drift, or change on their own.

What each side is meant to keep: the system as we mean it to be. This is later knowledge, what should be, not a description of the repo today, and the intent itself may change. Whether the repo does all of it is not yet checked.

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
8. its trials: work never done before, written as one text, an Approach on Trial, in a run or here, and judged here. Each stays on trial for more uses, lands as new understanding or spread across understanding that exists, or is dropped. A landing is a moment to refresh what it touches, here and in the runs' copies. This repo also judges its own trials, with no outside judge. A run's trial, once judged here, reaches back to that run by an update, or the run keeps working from its own version.

Each CBC Run:

1. keeps no understanding of agent work. It uses the instructions, and may change them;
2. gets the concept's understanding, to explain its problems. Whether a run may change that understanding, since it uses it directly, is open;
3. keeps understanding of its own problem: one specific system's design;
4. keeps its own records, from the setup it was shipped;
5. may lose the why of its changes: this repo reads only what the run wrote down.
6. drafts trials for work never done before, uses each until this repo judges it, and offers it back.

Seen already, where the repo differs from that intent: one convention manual, understanding, is written for both seats at once, this repo's and every CBC Run's, though the two need different things from it.

## 3. The axes of knowledge

Where text is kept so far, on each of the three axes, which §3.1 to §3.3 explain. Every text should have a place on each axis; one that doesn't is a finding.

| Where it's kept | Kind | Time | Who uses it |
|---|---|---|---|
| Understanding files in the repo | understanding | now | both |
| Agent Skills and rules | instruction | now | the agent acts on it; the human checks what they told it |
| Devlog, the journal of the work, and commit messages | understanding | before | both, seldom |
| TODO, the backlog | understanding | later | both |
| The human's private working rules | instruction | now | the agent acts on it; the human wrote it |
| The agent's memory | both | now | the agent; the human rarely |

### 3.1 Who uses the text

The text is the interface between the human's mind and the agent. Each uses it differently.

For the human, the text is, so far:

- how they see something, and how they understand it;
- where they are with it, at the level each idea needs: basics for one, details for another;
- not always correct;
- what they recall from.

For the agent, the text is, so far:

- what the human knows, and how much;
- where to start helping: applying the idea, learning more of it, keeping it up, going deeper, and anything else done with it.

The agent usually knows more about the subject than the text says.

Each list holds what has been found so far; more may come.

The text is also the agent's interface with itself, from one session to the next. What the agent learns in a session reaches the next only if it is written down.

Some of that text is kept outside the repo: the agent's own memory, notes it writes for itself about working with the human, such as "never push" or "explain simpler first". The human rarely reads them. They overlap the human's own working rules and the repo's rules, and they can go stale like any other text.

### 3.2 The time of knowledge

Knowledge has a time too:

- before: what was known or thought before;
- now: what is known or thought now, not always checked;
- later: what is meant to be learned, or checked, later.

Knowledge moves between the times, and the move is where it gets lost:

- later becomes now when something is learned or checked;
- now becomes before when it is replaced.

If a move isn't written down, the old text keeps claiming now.

New knowledge enters in several ways, so far: the human learns, a talk ends in a decision, the agent finds something in the work, a run shows something this repo reads back, or work never done before is tried.

Before keeps why it changed, not only what was thought. Without that why, a later reader sees what changed but not the reason: the why goes missing (§4), this time between before and now.

Now has degrees of certainty: what is thought now isn't always what is known. Some of now is unchecked, and later holds what should be checked.

What before is for, so far:

- not repeating a mistake: a dead end marked as one isn't tried again;
- knowing why now is as it is: when a past decision is questioned, its reasons and what was rejected are there;
- seeing where the human has been: the path of their understanding, which helps the agent judge their level now;
- resuming work: where it stopped, and what was tried;
- going back: undoing to an earlier state;
- evidence: what things cost, so a choice can be judged.

### 3.3 The kind of text

Text comes in two kinds, so far:

- understanding: what is known, and how it is understood;
- instruction: text built on understanding, to apply it. Agent Skills and rules are instructions.

An instruction has two readers too. The agent acts on it. The human reads it to know what they told the agent.

The two kinds go wrong differently. Understanding may be not always correct and still do its job. An instruction must be faithful to its understanding, since the agent acts on it as it stands. It is only as right as that understanding: a mistaken understanding passes into a faithful instruction unseen.

A text can be both kinds while its knowledge is new. Work never done before is written as one text, an instruction with its understanding inside it, and tried. It is split only when it is judged, since what is not yet understood cannot be split.

Some understanding is about the agent itself: how a change works, in four steps, `decide ──▶ make ──▶ check ──▶ record`; how a session starts empty; what loads when. Here the agent teaches the human. From what the human then understands, the two write instructions together, such as how a change is recorded.

An instruction stands on its understanding. When the understanding moves on, the instruction can go stale without anyone seeing it. An instruction that carries the whole why grows long.

One understanding can give several instructions. When each instruction retells the understanding, the same knowledge is written several times, and the copies can disagree.

An instruction can be copied to other repos, for the agents working there. Each copy can drift from the understanding it came from, and can change on its own.

## 4. What goes wrong

Everything here is one drift: the text and the knowledge drift apart.

- **When the text holds less than the knowledge, the why goes missing.** An Agent Skill is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **When the text is older than the knowledge, it goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. The agent then reads it as true and acts on it. This is the bigger problem. A text goes stale when its time is wrong: it still reads as now after the knowledge has moved on.

Wrong understanding is not, by that alone, the problem. Understanding that is incomplete or not correct, but honestly shows where the human is, does its job. An instruction is different: the agent acts on it as it stands (§3.3). The problem is text that no longer matches where the human is, or that the agent treats as settled fact.

The drift happens in three phases of a text's life: two moments, writing and reading, and the stretch between them, aging.

- **Writing:** knowledge goes into text, and part of it is lost, such as the why.
- **Aging:** the knowledge moves on, and the text grows older than it.
- **Reading:** the agent reads the text and builds a different understanding from it than the human holds.

The drift breaks the interface between the human's mind and the agent in these cases, found by thinking it through, each to be tested against real sessions (§6). Each is tagged with the phase it breaks in and the axis of §3 it lives on:

| Case | Phase | Axis |
|---|---|---|
| 1. The human knows something the text doesn't hold. | writing | who uses it |
| 2. The text is older than the human's understanding: they have moved on. | aging | time |
| 3. The agent's context is older than the text: it read the text earlier in the session, or from a summary, and the text has changed since. | aging | who uses it |
| 4. The text is ahead of the human: the agent wrote it, and it holds the agent's understanding, not the human's. | writing | who uses it |
| 5. The text is at the wrong level: too thin to recall from, or too dense to read. | writing | who uses it |
| 6. The text is wrong, and the agent treats it as true instead of suggesting a fix. | reading | who uses it |
| 7. The agent reads the text and builds a different understanding from it than the human meant. | reading | who uses it |
| 8. Two texts disagree, and neither says which one is where the human is now. | aging | time |
| 9. The text holds the what, not the why. | writing | kind |
| 10. An instruction still applies understanding that has moved on. | aging | kind |
| 11. An instruction is faithful to an understanding that is mistaken, and neither side sees it until the work shows it. | writing | kind |
| 12. A move between times isn't written down: what was learned still sits in later, or replaced understanding isn't kept as before. | writing | time |
| 13. The agent reads a before text as now, such as an old devlog entry taken as current. | reading | time |
| 14. The agent reads understanding as an instruction, such as the human thinking aloud, in chat or in text, taken as an order, or applies an instruction where it wasn't meant to. | reading | kind |
| 15. One understanding text serves sides whose needs differ, and a change made for one moves the other. | writing | who uses it |
| 16. One instruction covers several tasks, and a change made for one task changes the others. | writing | kind |
| 17. A later text is read as now: what is meant to be is taken for what is. | reading | time |
| 18. Unchecked knowledge is read as checked, such as a trial's text taken as proven. | reading | time |

The same cases by phase and axis. Every cell has a case; an empty one would point at a missing case:

| | who uses it | time | kind |
|---|---|---|---|
| **writing** | 1, 4, 5, 15 | 12 | 9, 11, 16 |
| **aging** | 3 | 2, 8 | 10 |
| **reading** | 6, 7 | 13, 17, 18 | 14 |

Seen on 2026-11-05: case 1, the purpose of an earlier attempt to rebuild this repo's way of working, written nowhere for 3 days; cases 4 and 5, the agent's dense answers, until the human said they were not on the same page.

## 5. What was tried

This repo writes each fact in one text, its home, and every other text that needs it points there by a reference instead of retelling it (one home per fact). It was built without full consideration, and it has cost too much to keep here:

- **Finding is cheap, judging is not.** A search lists every place that points at a fact. Whether each place still holds needs reading. This repo has 398 section references pointing at 129 sections. The most pointed-at section has 22.
- **The fix becomes a loop.** A change in one referring place can force the home to change. Then every other reference has to be checked again. If they disagree, it's back to the home, and so on. A decision has to be weighed across many places, not taken in one pass.
- **It multiplies.** When references start disagreeing with each other, each disagreement starts its own loop.
- **A refresh is a sweep.** To bring the text up to date, one agent reads the whole repo once, and every finding it makes can start a loop.

## 6. Where it may be wrong

The next step of this work tests these against the record: the devlog's notes of what each session lacked, and the findings of past reviews of this repo:

- how often stale text actually hurt a session, and how;
- where staleness comes from: a retelling that drifted, a home that was wrong, or something never written down;
- whether every text must stay true, or only what the agent acts on;
- whether the cost lies in the one-home idea itself, or in how it's kept, such as the sweep;
- whether only now decides that a change is needed, with before as input and not authority;
- when checking before costs more than it gives, and whether it can harm: by what reading it costs, by anchoring new thinking to old framing, or by being read as now;
- which kinds of before pay, and which aren't worth keeping. This repo's devlog alone is 8,773 lines, after 4 months.

## 7. What would show it's solved

First checks only. They are refined once the next step shows which cases really happen. Each line can be checked:

- A new session continues without the human retelling. Count the retellings and corrections in each session.
- Behind each Agent Skill, its why can be found.
- The cost of one change stays about the same as the repo grows.

## 8. Options to consider

Answers met while stating the problem, kept to be weighed, not chosen:

- write an instruction only when work needs one, and keep it short;
- keep the why in the understanding, not in the instruction;
- let an instruction point up to its understanding instead of retelling it. How this differs from one home per fact (§5) is open.
