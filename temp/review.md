# Review of the idea-to-approach model

<!-- A draft for the review of the idea-to-approach model under this
     repo: whether such a model is worth defining, and whether ours is
     the best among its alternatives. It began as a review of how this
     repo works, and was re-aimed at the model the repo stands on. Its
     first phase writes the reviewer's intent, told in stops, and locks
     it once the whole is told, by the intent-check Approach on Trial
     (.claude/approaches-on-trial/intent-check.md).
     Once locked, the intent changes only when the reviewer reopens it.
     Where the locked intent lives is decided at the review's end; this
     file goes once the review is done, and git keeps every version. -->

## Intent

### The intent, locked

Locked 2026-11-02, on the reviewer's word. It changes only when the
reviewer reopens it (intent-check, Stage 3). Its gaps and tensions,
below, stay open; the goals and the comparison take them up.

**Re-aimed:** the subject is now the idea-to-approach model under this
repo; the repo stands on it, and the delivery on the repo. What is
about the repo is kept apart, for later.

**The intent**

**The core: turn ideas into Work Approaches an agent can use, and
keep them true as work teaches us.** Everything below serves it.

*The model*

1. **Two kinds of idea.** A concept, such as CBC. A way of working,
   such as the commit set, or committing itself.
2. **An idea is written once, free of any project.** It is the idea
   itself, bound to no repo.
3. **Adapted, never discovered again.** The same idea is adapted to
   each project's needs, in more than one place. A new repo takes an
   idea another project found without finding it again.
4. **One idea, several Work Approaches.** In one project, an idea can
   meet several cases, each with its own Work Approach. The exchange
   between the kit and a CBC Run is one idea, with reading,
   processing and writing back.
5. **Ideas connect.** A new idea extends the others and does not
   contradict them.
6. **What a project applied is known:** which ideas it took, which it
   left, and which it should take.
7. **What the work teaches comes back.** Each project finds things to
   improve, in the ideas and in the Work Approaches built on them.
   What changed is tracked: why, where, and from which project.
8. **Traceable both ways.** From an idea one can follow to its Work
   Approaches, and back. Why each is as it is, and how much context it
   carries, are written, so a change knows what may go.
9. **Growth stays bearable.** More ideas, more Work Approaches, and
   more links between ideas must not make one change touch
   everything.

*The repo built on it, kept for later*

- R1. **Ready when a CBC project starts.** When a CBC project is
  needed, its Work Approaches are ready. The reviewer starts on the
  CBC problem itself, and writes no concept, Agent Rules or Agent
  Skills first.

**How, as pictured today**

Kept to help reveal the intent, and compared at intent-check's Stage
5. Not the intent.

- H1. **A delivery, prepared ahead,** carries the Work Approaches to a
  project: the CBC kit, and the common ones beside it.
- H2. **This repo uses the common ones too,** in keeping the delivery
  itself.
- H3. **One place in this repo** tracks what the work teaches.
- H4. **A model for writing and keeping Work Approaches,** seen from
  the agent's side.
- H5. **Open: is the model worth it?** The other ways: write each Work
  Approach from scratch each time; or keep steps that belong to one
  project, such as preparing its database. Work like committing, the
  same everywhere, argues for storing it once.
- H6. **Some of this may move later.** The common Work Approaches may
  move to a repo of their own that keeps them.
- H7. **Three layers per idea:** the idea's description, free of any
  project; its description for one project; and the lean Work
  Approach the agent follows, from that.
- H8. **An idea map:** ideas, or their sections, as separate texts,
  linked into a network.
- H9. **One home per fact,** reused elsewhere by reference.
- H10. **Upkeep split across several agents.** A separate question.

**Open questions,** for the comparison:

- Would this model work, and what would it cost to keep?
- What alternatives exist? Does anyone address this, and how?
- Is today's chain, Idea Model to convention to Work Approach, this
  model, or a shallower one?
- Is the cost felt in the refinement from how the model is defined,
  or from something else too?

**Noticed:**

- **Gaps:**
  - Line 2 and H7: is the project's description of an idea a text of
    its own, or part of the Work Approach?
  - Line 5, "does not contradict": checked how, and by whom?
  - Line 6: known where, in the project or with the idea?
  - Line 3, "each project": any project, or any project worked with
    an agent the way this one is?
  - Line 7, tracking: who reads it, the reviewer only, or the
    projects pinned to a version too? Does an improvement go to the
    next project only, or to one still running too?
  - R1, "starts on the CBC problem": who works a CBC project, the
    reviewer with an agent, or an agent on full auto? Is the stack
    part of what is ready, or chosen per project?
  - H4, "the model": what it holds. The why of each Work Approach;
    how much context each carries; how a change is checked; or all
    three?
- **Tensions:**
  - Lines 2 and 3 against line 9: an idea written once and reused by
    reference is what makes the mesh. One home pulls against a change
    that stays local.
  - H7 and the pain: three texts per idea, and more per case, is more
    to keep.
  - R1 and line 7: what is ready wants to be stable, and every project
    changes it. How often does it change: after each project, or in
    batches?
  - Line 3 and H6: reused on many projects, yet held in a repo about
    one concept. The core puts the ideas and their approaches first,
    and where they live after.

## Possible goals

Possibilities, not decisions: held until the intent is locked, then
set against it (intent-check, Stage 4). Not drawn on while the intent
is written.

Two answers locked by goal-finding, before it was dropped. The rounds
that gave them are in git: `7afe7f3` holds rounds 1 and 2; `3624553`
holds round 3, stopped.

- **Success, in six months:** the concept is sharper from what CBC
  Runs found; CBC Runs build real systems that keep their guarantees
  with little of the reviewer's attention; the way of working moved
  to a second concept repo with little change; the reviewer
  understands system design better, and the repo shows how; the repo
  is cheap to keep, most sessions going to new learning.
- **Failure, in six months:** writing cost more than it gave: too many
  records, each change rippling through them; rules about the writing
  costing more than the writing; text written before it was needed;
  text never read again; much read at each session's start; the
  reviewer's review time; rewording that changes how text reads, not
  what anyone does.

## Notes

Things noticed along the way, for the later phases: marks, doubts,
ideas. No fixes.

**Today's model and repo, for Stage 5.** Noticed while the intent was
told, and kept out of it:

- The core: the repo writes this chain down. Its Idea-to-Output
  Model goes from an Idea Model, to a Canonical Description, to a
  Work Approach, to an output (`docs/models/idea-to-output.md` §2,
  *The kinds*).
- "Work Approach": in the repo it is how one piece of work is done;
  an Agent Skill or an Agent Rule is one (`docs/glossary.md`). The
  whole kit, H1, is called the delivery.
- Line 3 and H1: the common Work Approaches ship today in the
  Container Group: the commit-messages, commit-plan, retrospective,
  apply-retrospective and visual-comparison Agent Skills, and the
  delivered-copies, one-home, shapes-lifecycle and writing Agent
  Rules.
- Line 3: the README puts "a general method or working arrangement"
  out of scope, held here until three repos have lived it
  (ADR-0038). Line 3 puts it in.
- H3: tracking is spread over `CHANGELOG.md`, the ADRs, the devlog
  and the CBC Run Readings; no one place.
- Line 5 and H4: a Work Approach names its manual, the Canonical
  Description that holds its why, in its Foundation Line.
- The README's *why*, the reviewer's understanding improving in a
  recorded way, is not in the intent yet.
