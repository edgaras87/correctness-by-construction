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

1. **A ready kit for starting a CBC project.** This repo keeps a
   delivery prepared ahead of time. When a CBC project is needed, the
   reviewer takes the delivery and starts on the CBC problem itself.
   They do not first write the concept, the Agent Rules or the Agent
   Skills: those are here, ready.
2. **One place for what CBC Runs teach.** Each CBC Run finds things to
   improve, in the concept and in the Work Approaches built on it.
   This repo is the one place those are tracked: what changed, why,
   where, and from which CBC Run.
3. **Some of this may move later.** The intent covers several things
   that live here today; some may get a home of their own.

**Noticed:**

- **Gaps:**
  - "Start working": who works a CBC project, the reviewer with an
    agent, or an agent on full auto, as CBC Run 6 ran?
  - "Not worry about other stuff": is the stack, Spring and
    PostgreSQL today, part of the kit, or chosen per project?
  - Tracking: who reads it, the reviewer only, or the CBC Runs pinned
    to a version of the kit too?
  - Where an improvement goes: to the next CBC Run only, or to one
    still running too?
- **A tension:** a ready kit wants to be stable, and every CBC Run
  changes it. How often does it change: after each CBC Run, or in
  batches?
- **Differences from the repo,** named, not argued:
  - "Work Approach": in the repo it is how one piece of work is done;
    an Agent Skill or an Agent Rule is one (`docs/glossary.md`). The
    whole kit is called the delivery.
  - Tracking: spread over `CHANGELOG.md`, the ADRs, the devlog and the
    CBC Run Readings; no one place.
  - The README's *why*, the reviewer's understanding improving in a
    recorded way, is not in the intent yet.
  - The way of working, the conventions and Idea Models, is not in
    the intent yet.

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
