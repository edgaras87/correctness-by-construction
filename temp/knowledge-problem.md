# The problem: keeping what we know true

<!-- A draft: the problem of the Plan Step "Find how what we know
     stays true", its stage 1, in the reviewer's words. Built from
     TODO-CONVERSATION-MEMORY.md §31, *Keeping what we know true*,
     and from what temp/idea-model-problem.md says of the problem,
     not of a model. Polished one insight at a time, each a commit,
     so the diffs show what changed. It states the problem only: an
     answer met on the way is kept as an option to consider (§7),
     not chosen. Its
     home is decided when the Plan Step closes; it goes then, and
     git keeps every version. -->

## 1. The purpose

Knowledge is what one knows, and how one understands it. It lives in a head. Text is where it is stored: a copy, made at one moment.

Text here is understanding and instruction (§2.3), wherever it is kept. So far it is kept in the repo's files, in commit messages, in the human's private working rules, and in the agent's memory.

The chat is not text. It is where knowledge passes between the human and the agent, and it is lost when the session ends unless something is written down.

Two sides work with the knowledge:

- **The human:** the person whose knowledge it is. They learn, decide, and carry the knowledge from one session to the next.
- **The agent:** the AI model working in a session. It knows its subjects from its training, but starts each session knowing the human and the work only from what it reads.

The human and the agent are on the same page when the agent's picture of the human's understanding, built from the text, matches that understanding and its level. Both learn, and write down what they learn. A new session reads it, and the human doesn't have to retell it. Both continue improving from there.

## 2. The axes of knowledge

Where text is kept so far, on each of the three axes, which §2.1 to §2.3 explain. Every text should have a place on each axis; one that doesn't is a finding.

| Where it's kept | Kind | Time | Who reads it |
|---|---|---|---|
| Understanding files in the repo | understanding | now | both |
| Agent Skills and rules | instruction | now | the agent acts on it; the human checks what they told it |
| Devlog, commit messages | understanding | before | both, seldom |
| TODO | understanding | later | both |
| The human's private working rules | instruction | now | the agent acts on it; the human wrote it |
| The agent's memory | both | now | the agent; the human rarely |

### 2.1 Who uses the text

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

### 2.2 The time of knowledge

Knowledge has a time too:

- before: what was known or thought before;
- now: what is known or thought now, not always checked;
- later: what is meant to be learned, or checked, later.

Knowledge moves between the times, and the move is where it gets lost:

- later becomes now when something is learned or checked;
- now becomes before when it is replaced.

If a move isn't written down, the old text keeps claiming now.

Before keeps why it changed, not only what was thought. Without that why, a later reader sees what changed but not the reason: the why goes missing (§3), this time between before and now.

Now has degrees of certainty: what is thought now isn't always what is known. Some of now is unchecked, and later holds what should be checked.

What before is for, so far:

- not repeating a mistake: a dead end marked as one isn't tried again;
- knowing why now is as it is: when a past decision is questioned, its reasons and what was rejected are there;
- seeing where the human has been: the path of their understanding, which helps the agent judge their level now;
- resuming work: where it stopped, and what was tried;
- going back: undoing to an earlier state;
- evidence: what things cost, so a choice can be judged.

### 2.3 The kind of text

Text comes in two kinds, so far:

- understanding: what is known, and how it is understood;
- instruction: text built on understanding, to apply it. Agent Skills and rules are instructions.

An instruction has two readers too. The agent acts on it. The human reads it to know what they told the agent.

The two kinds go wrong differently. Understanding may be not always correct and still do its job. An instruction must be faithful to its understanding, since the agent acts on it as it stands. It is only as right as that understanding: a mistaken understanding passes into a faithful instruction unseen.

Some understanding is about the agent itself: how a change works, `decide ──▶ make ──▶ check ──▶ record`; how a session starts empty; what loads when. Here the agent teaches the human. From what the human then understands, the two write instructions together, such as how a change is recorded.

An instruction stands on its understanding. When the understanding moves on, the instruction can go stale without anyone seeing it. An instruction that carries the whole why grows long.

One understanding can give several instructions. An Agent Skill and a rule differ mainly by when they load: a rule in every session, an Agent Skill at a task. When each instruction retells the understanding, the same knowledge is written several times, and the copies can disagree.

## 3. What goes wrong

Both problems below are one: the text and the knowledge drift apart. When the text holds less than the knowledge, the why goes missing. When the text is older than the knowledge, it goes stale.

Wrong understanding is not, by that alone, the problem. Understanding that is incomplete or not correct, but honestly shows where the human is, does its job. An instruction is different: the agent acts on it as it stands (§2.3). The problem is text that no longer matches where the human is, or that the agent treats as settled fact.

- **The why goes missing.** An Agent Skill is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **What was written goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. The agent then reads it as true and acts on it. This is the bigger problem. A text goes stale when its time is wrong: it still reads as now after the knowledge has moved on.

The drift happens in three places:

- **Writing:** knowledge goes into text, and part of it is lost, such as the why.
- **Time:** the knowledge moves on, and the text stays as it was.
- **Reading:** the agent reads the text and builds a different understanding from it than the human holds.

Where it breaks, at the interface between the human's mind and the agent. Cases found by thinking it through, each to be tested against real sessions in stage 2:

1. The human knows something the text doesn't hold.
2. The text is older than the human's understanding: they have moved on.
3. The agent's context is older than the text: it read the text earlier in the session, or from a summary, and the text has changed since.
4. The text is ahead of the human: the agent wrote it, and it holds the agent's understanding, not the human's.
5. The text is at the wrong level: too thin to recall from, or too dense to read.
6. The text is wrong, and the agent treats it as true instead of suggesting a fix.
7. The agent reads the text and builds a different understanding from it than the human meant.
8. Two texts disagree, and neither says which one is where the human is now.
9. The text holds the what, not the why.
10. An instruction still applies understanding that has moved on.
11. An instruction is faithful to an understanding that is mistaken, and neither side sees it until the work shows it.

Seen on 2026-11-05: case 1, the rebuild's purpose, written nowhere for 3 days; cases 4 and 5, the agent's dense answers, until the human said they were not on the same page.

## 4. What was tried

This repo keeps each fact in one home, with references pointing at it (one home per fact). It was built without full consideration, and it costs too much to keep:

- **Finding is cheap, judging is not.** A search lists every place that points at a fact. Whether each place still holds needs reading. This repo has 398 section references pointing at 129 sections. The most pointed-at section has 22.
- **The fix becomes a loop.** A change in one referring place can force the home to change. Then every other reference has to be checked again. If they disagree, it's back to the home, and so on. A decision has to be weighed across many places, not taken in one pass.
- **It multiplies.** When references start disagreeing with each other, each disagreement starts its own loop.
- **The refresh is a sweep.** One agent reads the whole repo once, and every finding it makes can start a loop.

## 5. Where it may be wrong

Stage 2 tests these against the record:

- how often stale text actually hurt a session, and how;
- where staleness comes from: a retelling that drifted, a home that was wrong, or something never written down;
- whether every text must stay true, or only what the agent acts on;
- whether the cost lies in the one-home idea itself, or in how it's kept, such as the sweep;
- whether only now decides that a change is needed, with before as input and not authority;
- when checking before costs more than it gives, and whether it can harm: by what reading it costs, by anchoring new thinking to old framing, or by being read as now;
- which kinds of before pay, and which aren't worth keeping. This repo's devlog alone is 8,773 lines, after 4 months.

## 6. What would show it's solved

Each line can be checked:

- A new session continues without the human retelling. Count the retellings and corrections in each session.
- Behind each Agent Skill, its why can be found.
- The cost of one change stays about the same as the repo grows.

## 7. Options to consider

Answers met while stating the problem, kept to be weighed, not chosen:

- write an instruction only when work needs one, and keep it short;
- keep the why in the understanding, not in the instruction;
- let an instruction point up to its understanding instead of retelling it. How this differs from one home per fact (§4) is open.
