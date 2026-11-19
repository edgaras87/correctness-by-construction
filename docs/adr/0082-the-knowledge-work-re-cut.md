# 0082. The knowledge work re-cut, the repo rewritten here

Date: 2026-11-19
Status: Accepted (2026-11-19, the reviewer, in the final records
commit of the close of the Plan Step "Find how what we know stays
true")

## Context

The Plan Step "Find how what we know stays true" opened on 2026-11-05.
Its goal: a way to keep what the reviewer and the agent know true,
from one session to the next, chosen from the problem in the
reviewer's words and from real cases. It had three stages: the
problem, the real-world record, the real cases.

By 2026-11-19 it had run 14 days and 503 commits, and was still in
stage 1. None of its four own Plan Step Gate items was ticked. Its
real work ran as TODO items marked "due now": the layers model, the
Change idea. The plan's form says a Plan Step is "the one piece of
work being done now" (`PLAN.md`, *The Plan Step Form*). This goal was
the goal of the whole knowledge work. It already stands in the
problem file's §1, *The purpose*, and §7, *What would show it's
solved* (`temp/common-ground/common-ground-problem.md`).

Three Plan Steps were stopped behind it, or behind steps before it:

- "Rebuild in cbc-concept", stopped for it on 2026-11-05. ADR-0081
  waits for that step's close for its verdict. The reviewer will not
  go back to `cbc-concept`; it holds ideas to consider once.
- "Birth CBC Run 6", stopped for the refinement, which closed on
  2026-11-02. Its own items were all done on 2026-10-29.
- "Take CBC Run 5's lessons", stopped for Birth CBC Run 6, four of
  its own items open.

CBC Runs 4 and 6 are unread. CBC Run 5 was read on 2026-10-22, and
its judging stopped half done.

## Options considered

**For the Plan Step:**

- **Keep it open.** Rejected: it would stay open until the whole
  knowledge work ends, and each talk would grow its Conversation
  Memory section, §31, which reached 1,031 lines.
- **Mark it skipped.** Rejected: `[-]` is for planned work not done,
  and it did 503 commits of work.
- **Move its goal into the layers document.** Rejected: that document
  models how knowledge sits. The goal is why the work is done, and
  the problem file's §1 already says it.
- **Close it, re-cut.** Taken.

**For the rebuild in `cbc-concept`:**

- **Resume it, or keep it stopped.** Rejected: the reviewer will not
  go back to it, and building from scratch in a new repo is no longer
  the way chosen.
- **End it, `cbc-concept` kept as a source until checked once.** Taken.

**For CBC Runs 4, 5 and 6:**

- **Read after the rewrite.** Rejected: the rewrite takes today's texts
  as its sources, and a reading says which of them failed in real
  work. Read after, those faults may land unseen; and memory of the
  old kit fades.
- **Read, judge and update now.** Rejected: an update fixes texts the
  rewrite is about to replace, so each line would change twice.
- **Read and judge now, update during the rewrite.** Taken.

## Decision

1. **The knowledge work is a goal, not a Plan Step.** Its goal is the
   problem file's §1 and §7. A Plan Step is one TODO item, opened when
   due. The closing step's own items are struck, each naming the TODO
   item it moved to; its stages are TODO items.
2. **Today's Maintainer Repo is rewritten into the layers model, in
   this repo.** Each of its texts is read, and each part it holds
   lands at its layer, in its Work Domain, as understanding or
   instruction. Where a part fits nowhere, the model changes. A text
   goes once everything it holds has landed, or has been judged not
   needed.
3. **The rebuild in `cbc-concept` ends.** The reviewer reads
   `cbc-concept` once, when the Agent Model's rewrite reaches the
   piece of work; the agent then checks it for ideas not yet taken in
   here; then it is dropped. ADR-0081 is superseded.
4. **CBC Runs 4, 5 and 6 are read and judged now, and the kit is
   updated during the rewrite.** Each CBC Run is read apart; their
   findings are judged together, by the simulation's Judge, by meaning,
   and kept for the rewrite. No old text is changed and no update is
   sent. Birth CBC Run 6 closes; Take CBC Run 5's lessons ends, its
   open items findings for that judging.

## Consequences

- `PLAN.md` holds no Plan Step until the next opens.
- The Conversation Memory's §31 goes with its item, by the file's own
  rule, once each of its open threads stands somewhere.
- The plan's form gains the lesson: a Plan Step's goal is one piece of
  work, and a step whose goal grew past one is re-cut.
- The drafts under `temp/common-ground/` stay until what they hold
  lands in the rewrite, not until a Plan Step closes.
- Decided with the reviewer on 2026-11-19, one question at a time; the
  devlog of that day tells it.
