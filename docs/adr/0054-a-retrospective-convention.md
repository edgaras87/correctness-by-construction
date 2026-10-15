# 0054. The retrospective is a convention, with two skills

Date: 2026-10-15
Status: Proposed (under the commit plan for retrospective)

## Context

Project-recording placed the retrospective in `PLAN.md`: the
container's stub ends on "Retrospective (fill at project end)", six
questions and a line asking for lessons. Project-recording's §9
lifecycle and its §11 flow point at it.

Run 3, never-oversold, did far more than the section asked, and none
of it was written down as a way of working (its RETRO.md, D23):

- **It walked the run part by part,** in the order the run was
  built, each finding backed by a quoted line or a count.
- **It decided one thing at a time,** each decision with what was
  rejected and the place it lands.
- **It looked and changed nothing.** A step after it applied the
  lessons to run 3's own records, before Release, without touching
  what run 3 had proved (D24).

And it happened only because the reviewer asked: run 3 stopped
before Release, and the section waits for the project's end.

Run 3 kept both as skills, `retrospective` and
`apply-retrospective`, each with a plain guide for the reviewer
beside it, and offers all four files. The skills name run 3, its
short tags, its check script, and the reviewer's private file.

This repo has no project end. Its milestones close on "lessons
folded back where they came from", which names no place and no
method, the kind of item run 3's D4 judged weak.

## Options considered

- **The skills under project-recording,** as `one-home.md` is.
  Rejected: two skills, a record of their own and a procedure make
  a subject, and project-recording already runs past 800 lines.
- **A new convention beside project-recording, which keeps its
  lines.** Rejected: the retrospective would then be stated in two
  manuals.
- **A guide for the reviewer shipped beside each skill,** as run 3
  has them. Rejected: the guide repeats the skill, and the two
  drift; in run 3 the apply guide restates nearly every rule.
- **A section for the reviewer inside each skill.** Rejected: the
  skills already stop at each of the reviewer's decisions, and the
  manual's seats can say the rest.
- **Holding the guide question** until run 3's D25 is decided.
  Rejected: the reviewer would have nothing written meanwhile.
- **No seat for the deliverer.** Rejected: our gate item for
  lessons is the weak kind, and today's work found what a look back
  would have.

## Decision

1. **The retrospective is a convention of its own,** the eleventh:
   `docs/conventions/retrospective/`. The subject moves out of
   project-recording, which keeps a pointer. The PLAN stub's
   Retrospective section goes; `RETRO.md` gets a row in the records
   table.
2. **It ships two skills in the container,** `retrospective` and
   `apply-retrospective`, cleaned of run 3: no run named, no guide,
   the records check the playbook asks for in place of run 3's
   script, full-word tags. The stub's six questions move into the
   walk; one of them, the entry file read top to bottom, is
   agent-arrangement §2.6's only trigger.
3. **The reviewer's part is the manual's,** in its seats: what the
   reviewer decides and gets, marked as a summary of where the
   skills stop. No guide ships. Reopened if a reviewer works
   without this repo, or run 4's reading shows the guide was missed.
4. **The deliverer's seat is on trial.** At Step 10's close this
   repo runs both skills on itself, from `delivery/container/`, in
   place of "lessons folded back". The trial's verdict says whether
   we hold our own copies, and what our seat is.

## Consequences

- `ARCHITECTURE.md` counts eleven manuals; the container holds five
  skills.
- Project-recording §2.4, §9 and its seats, and agent-arrangement
  §2.6, point at the convention.
- The playbook's steps that open the two skills, before Release, are
  the playbook's work, after this decision.
- Run 3 holds its own copies at the same paths, with a guide beside
  each. A delivery lands ours over its skills; its guides stay its
  own files.
