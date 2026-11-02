# Review of how this repo works

<!-- A draft for the review of how this repo works and what it costs:
     whether the reviewer's ideas and intent are put here the right
     way, what each part costs, and what could be better. Its first
     phase writes the reviewer's intent, told in stops, and locks it
     once the whole is told, by the intent-check Approach on Trial
     (.claude/approaches-on-trial/intent-check.md).
     Once locked, the intent changes only when the reviewer reopens it. The
     locked intent goes to its home in the README, and this file goes
     once the review is done; git keeps every version. -->

## Intent

### The intent, a draft

Told in stops; any line may change until the intent is locked.

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

*The CBC kit*

1. **A ready kit for starting a CBC project.** This repo keeps a
   delivery prepared ahead of time. When a CBC project is needed, the
   reviewer takes the delivery and starts on the CBC problem itself.
   They do not first write the concept, the Agent Rules or the Agent
   Skills: those are here, ready.
2. **One place for what CBC Runs teach.** Each CBC Run finds things to
   improve, in the concept and in the Work Approaches built on it.
   This repo is the one place those are tracked: what changed, why,
   where, and from which CBC Run.

*Common Work Approaches*

3. **Written once, reused.** Work that comes back on every project,
   such as committing, is written once and reused, never derived
   again each time. The delivery carries it beside the CBC kit.
4. **This repo uses them too.** One place they are reused is this
   repo, in keeping the delivery itself.

*A model behind them*

5. **A model for writing and keeping Work Approaches,** seen from the
   agent's side: how much context each carries, and why each is as it
   is, so a later change knows what it may remove.
6. **Open: is the model worth it?** The other ways: write each Work
   Approach from scratch each time; or keep steps that belong to one
   project, such as preparing its database. Work like committing, the
   same everywhere, argues for storing it once.

*Where things live*

7. **Some of this may move later.** The intent covers several things
   that live here today. The common Work Approaches may move to a repo
   of their own that keeps them.

**Noticed:**

- **Gaps:**
  - Line 1, "start working": who works a CBC project, the reviewer
    with an agent, or an agent on full auto, as CBC Run 6 ran?
  - Line 1, "not worry about other stuff": is the stack, Spring and
    PostgreSQL today, part of the kit, or chosen per project?
  - Line 2, tracking: who reads it, the reviewer only, or the CBC Runs
    pinned to a version of the kit too?
  - Line 2: does an improvement go to the next CBC Run only, or to
    one still running too?
  - Line 3, "every project": any project, or any project worked with
    an agent the way this one is?
  - Line 5, "the model": what it holds. The why of each Work
    Approach; how much context each carries; how a change is checked;
    or all three?
  - Line 6: who answers "is it worth it": this review?
- **Tensions:**
  - Line 1 and line 2: a ready kit wants to be stable, and every CBC
    Run changes it. How often does it change: after each CBC Run, or
    in batches?
  - Line 5 and the pain: the model is meant to keep the cost down,
    and is itself kept at a cost.
  - Line 3 and line 7: reused on many projects, yet held in a repo
    about one concept.
- **Differences from the repo,** named, not argued:
  - "Work Approach": in the repo it is how one piece of work is done;
    an Agent Skill or an Agent Rule is one (`docs/glossary.md`). The
    whole kit is called the delivery.
  - Line 2: tracking is spread over `CHANGELOG.md`, the ADRs, the
    devlog and the CBC Run Readings; no one place.
  - Line 3: the common Work Approaches ship today in the Container
    Group: the commit-messages, commit-plan, retrospective,
    apply-retrospective and visual-comparison Agent Skills, and the
    delivered-copies, one-home, shapes-lifecycle and writing Agent
    Rules.
  - Line 3: the README puts "a general method or working arrangement"
    out of scope, held here until three repos have lived it
    (ADR-0038). Line 3 puts it in.
  - Line 5: the repo has a chain for this. An Idea Model, then a
    Canonical Description, such as a convention's manual, which holds
    the why, then the Work Approach derived from it
    (`docs/models/idea-to-output.md` §2, *The kinds*). A Work Approach
    names its manual in its Foundation Line.
  - The README's *why*, the reviewer's understanding improving in a
    recorded way, is not in the intent yet.

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
