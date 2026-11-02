# The idea-to-approach model: the problem

<!-- A draft: the problem this repo stands on, written so it can be
     worked. What model we try to build, where one home per fact
     breaks, how such a model could be kept, and what that costs.
     Drawn from the review of 2026-11-02, which was dropped once the
     problem was clear. Its home is decided when the problem is worked;
     this file goes then, and git keeps every version. -->

## 1. The model we try to build

**Turn ideas into Work Approaches an agent can use, and keep them
true as work teaches us.**

Every idea lives at three levels, from general to concrete:

```
            idea                       written once, bound to no project
       ┌─────┴──────┐
  for project A   for project B        the idea, adapted to one project's needs
   ┌───┴───┐          │
 approach approach  approach           what the agent follows, kept lean
```

1. **The idea.** What it is, in general, with no project in it. Example:
   work bigger than one commit is planned as a set of commits,
   checked at each step, and the plan bends to what the work turns up.
2. **The idea for one project.** The same idea, written for one
   project's needs. A second project writes its own, without finding
   the idea again.
3. **The Work Approach.** Lean instructions for the agent, made from
   the project's version.

Across the levels:

- **One idea, several Work Approaches.** In one project an idea can
  meet several cases. The exchange between the kit and a CBC Run is
  one idea, with reading, processing and writing back.
- **Ideas form a network.** They link to each other. A new idea
  extends the network and does not contradict it.
- **Each project knows its ideas:** which it took, which it left, which
  it should take.
- **What the work teaches flows back up.** A lesson changes the idea
  or its Work Approaches, and the change is recorded: what, why,
  where, from which project.
- **Each thing is written once.** Elsewhere it is reached by
  reference: one home per fact.

Two kinds of idea fit it: a concept, such as CBC; and a way of
working, such as the commit set, or committing itself.

## 2. Why we want it

- **Agent Skills and Agent Rules alone do not hold up.** Each needs
  context: how much of the story does it retell? When one must
  change, if nothing says why it is so, nobody can tell what may go.
- **The same work comes back on every project.** Committing, planning
  a commit set: written once, it is never worked out again.
- **It grows.** More ideas come, old ones change and merge. The system
  takes on harder work, and the cost of keeping it grows with it.

## 3. What a good model must do

Each line with its check: how we would see it holds.

| | Must | Check |
|---|---|---|
| 1 | Hold both kinds of idea | A concept and a way of working sit in the same shape, no special case |
| 2 | Keep an idea free of projects | The idea's text names no repo, stack or project step |
| 3 | Reuse, never rediscover | A second project writes only what differs |
| 4 | Let one idea feed several Work Approaches | Two Work Approaches point at one idea, neither repeats it |
| 5 | Keep ideas from contradicting | A contradiction is caught at a known step, before it lands |
| 6 | Know what a project applied | Its ideas, taken, left and wanted, read in one place |
| 7 | Bring lessons back | Each lesson leads to a recorded change, found from its idea |
| 8 | Trace both ways | From a Work Approach to its idea in one step, and back; each says why it is so |
| 9 | Keep a change local | A change touches only what derives from it; the count stays small as ideas grow |

A model that fails a check is out, however cheap. Among those left,
each is judged on:

- maintenance: what changing it takes;
- readability, for the agent and for the reviewer, each;
- future-proofing: how it takes work not yet seen;
- complexity;
- cost of use: what each session reads, and the reviewer's review
  time;
- cost of switching: the work to move to it, and the lived evidence
  the old model leaves behind.

Lived evidence comes before theory: what the CBC Runs and this repo
went through.

## 4. Where it pays

- **One project, few ideas:** it costs more than it gives. About twice
  the text, little reuse.
- **A second project:** it starts to pay. Ideas are not rediscovered,
  and a lesson reaches both.
- **Many ideas:** it pays only while the links between texts stay few.

The projects meet in one place: the starter kit. Running projects
are not checked; the kit is the one project where what differs is
settled. So for upkeep, the number of projects is one.

## 5. The one-home problem

**A fact is written once, and other texts point at it. Each place
that points at it relies on some meaning of it.**

When a fact must change, often because one place that uses it needs
something new:

1. Every place that points at it is found.
2. Each is read again: does its sentence still hold, with the new
   fact?
3. If one does not, either the fact changes again, or that place
   does.
4. Each change made in step 3 is itself a changed fact. Steps 1 to 3
   run again on it, until nothing new moves.

**Finding is cheap. Judging is not.** References are written out, so
a search lists every place. Whether each sentence still holds needs
reading, with its context. That is where the cost is.

**This repo, 2026-11-02,** leaving out the devlog and the ADRs:

- 398 section references point at 129 sections;
- the most pointed-at, facts-in-sync §4, has 22 places pointing at it;
- the next have 14, 12, 12 and 10.

**The first version that fits every place is not the best.** A fact
made general enough to fit everyone grows vague: it fits all and
helps none. When places need different things, the better moves are:

- **split the fact,** and each place points at the half it needs;
- **change the places,** when the new fact is truly better;
- **let one place keep its own version,** and stop pointing, when its
  need has moved away.

**The mesh.** References that run down the tree, from Work Approach to
project version to idea, grow with the texts and stay predictable.
References that run sideways, between texts on the same level or
between ideas, can grow far faster. Then one change reaches anywhere,
and how far is known only by searching.

## 6. How it could be kept

**Ways to keep the mesh small,** from how shared code is kept:

1. **Links point up only:** Work Approach to project version to idea.
   Never sideways between Work Approaches or project versions.
2. **A Work Approach stands alone.** The agent reads one text to work.
   The levels above serve upkeep, not each task.
3. **Ideas link by few, named links,** not by facts quoted across
   texts.
4. **Each reference says what it relies on,** in one line. A change is
   then checked against those lines, not against every paragraph.
5. **Facts many places use are core.** Few, stable, changed rarely
   and on purpose.
6. **A place may pin a version** of a fact, and move to the new one
   when it is ready.
7. **Copy when needs differ.** A little copying is cheaper than a
   reference that forces agreement.
8. **Rules on wording stay light.** They are paid on every text, at
   every change.

**Who does the checking:**

- **Up to about 5 places:** one agent holds them all and judges well.
- **Beyond:** several agents.
  1. One agent proposes the change.
  2. One checker for each place, in parallel: does my place still
     hold; if not, what would it need?
  3. One agent gathers the answers. All hold: the change goes in. A
     conflict: the options, split, change the places or copy, go to
     the reviewer.
  4. The reviewer decides the conflicts only.

  An agent that owns an idea need not live on. It is a check, run with
  the idea's text and the lines of what its places rely on.
- **The risk:** checkers that agree too easily. A sample of their
  answers is checked by hand.

## 7. What it costs

**Texts,** with about 2 Work Approaches for each idea in each project:

| Ideas | Projects | Ideas + project versions + Work Approaches |
|---|---|---|
| 10 | 1 | 10 + 10 + 20 = 40 |
| 30 | 2 | 30 + 50 + 100 = 180 |
| 100 | 5 | 100 + 400 + 800 = 1,300 |

Without the model, the first row is about 20 texts.

**What one change touches:**

| Change | Texts read again |
|---|---|
| A Work Approach | 1 |
| A project version | 1, and its Work Approaches |
| An idea | 1, its version in each project, their Work Approaches, its linked ideas |
| A new idea | 1, and the ideas it may contradict |
| A renamed or moved section | every place that points at it |
| A new project | one project version for each idea it takes |
| A lesson flowing back | Work Approach, project version, idea, the other projects' versions |

An idea with 2 projects and 3 linked ideas: about 10 texts. With 5
projects and 10 links: about 26.

**What drives the cost:**

1. **Sideways links,** above all.
2. **Projects,** each a copy of every idea's version. With the kit as
   the one project, this stays one.
3. **Rules on the text,** paid on every change.
4. **Reading for the agent,** if a Work Approach cannot be read alone.
5. **Judging each place,** the step a search cannot do. Lines of what
   each place relies on cut it.

Several agents cut the waiting, not the tokens.

## 8. Open

- Is today's chain, Idea Model to convention to Work Approach, this
  model, or a shallower one?
- Did the refinement's cost come from the levels, or from sideways
  links and rules on wording? Counting what its commits fixed would
  say.
- What do others do? Directions to search: software product line
  engineering, pattern languages, design rationale and ADRs,
  Zettelkasten, requirements traceability, agent instruction files.
- Is the project version a text of its own, or part of the Work
  Approach?
- Does the idea hold its why, or does the why live elsewhere?
- A test: the most pointed-at section, facts-in-sync §4, with a small
  change checked three ways: one agent reading all 22 places; lines of
  what each relies on; one checker for each place. Compared on cost,
  and on what each finds.
