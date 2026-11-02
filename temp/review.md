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

### The intent, a draft

Told in stops; any line may change until the intent is locked.

**Re-aimed:** the subject is now the idea-to-approach model under this
repo; the repo stands on it, and the delivery on the repo. Lines 3 to
5 are the model's. Lines 1 and 2, and H1 to H6, are about the repo
built on it, kept for later.

**Why: the pain behind it**

- **Work beside the concept.** Some work is not about the concept,
  and comes back on every project. Committing to git, with commit
  messages that stay stable. A way of working: think, propose, draft
  the commits, write a provisional ADR, then work, each step free to
  steer the plan, so what is done follows what the work met, not
  theory alone.
- **It grows.** There are many such pieces of work, and more will
  come. They change over time, and merge into each other. The system
  takes on more complex work, predictably, and the cost of keeping it
  grows with it.
- **Agent Skills and Agent Rules alone do not hold up.** Each needs
  context: how much of the story does it retell? And when one is to
  change, if nothing says why it is so, nobody can tell what may be
  removed or changed.

**The intent**

**The core: turn ideas into Work Approaches an agent can use, and
keep them true as work teaches us.** Everything below serves it.

1. **Two kinds of idea.** A concept, such as CBC. A way of working,
   such as the commit set, or committing itself.
2. **Ready when a project starts.** When a CBC project is needed, its
   Work Approaches are ready. The reviewer starts on the CBC problem
   itself, and writes no concept, Agent Rules or Agent Skills first.
3. **Never derived again.** Work that comes back on every project,
   such as committing, is not worked out again each time.
4. **What the work teaches comes back.** Each CBC Run finds things to
   improve, in the concept and in the Work Approaches built on it.
   What changed is tracked: why, where, and from which CBC Run.
5. **A change knows what it may remove.** Why each Work Approach is
   as it is, and how much context it carries, are written, so a later
   change can tell what may go.

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

**Noticed:**

- **Gaps:**
  - Line 2, "starts on the CBC problem": who works a CBC project, the
    reviewer with an agent, or an agent on full auto, as CBC Run 6
    ran?
  - Line 2, "writes nothing first": is the stack, Spring and
    PostgreSQL today, part of what is ready, or chosen per project?
  - Line 3, "every project": any project, or any project worked with
    an agent the way this one is?
  - Line 4, tracking: who reads it, the reviewer only, or the CBC Runs
    pinned to a version of the kit too?
  - Line 4: does an improvement go to the next CBC Run only, or to
    one still running too?
  - Line 4: what the work teaches about a way of working, not the
    concept, is it tracked too?
  - H4, "the model": what it holds. The why of each Work Approach;
    how much context each carries; how a change is checked; or all
    three?
  - H5: who answers "is it worth it": this review?
- **Tensions:**
  - Line 2 and line 4: what is ready wants to be stable, and every CBC
    Run changes it. How often does it change: after each CBC Run, or
    in batches?
  - H4 and the pain: the model is meant to keep the cost down, and is
    itself kept at a cost.
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
