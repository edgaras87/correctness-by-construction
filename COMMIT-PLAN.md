# Commit plan: the retrospective

## Summary — the state after all commits

A run looks back on itself with two skills, shipped in the
container: `retrospective` walks the finished run part by part and
writes `RETRO.md`, what the next run does differently; then
`apply-retrospective` applies those lessons to the run's own records
before Release, without touching what it proved. Run 3 wrote and
lived both (its RETRO.md, D23 and D24).

They are a convention of their own, the eleventh. The subject moves
out of project-recording, which keeps a pointer: the `PLAN.md`
stub's "Retrospective (fill at project end)" section goes, and its
six questions, the entry-file re-read among them, move into the
skill. `RETRO.md` gets a row in the records table.

The reviewer's part, what they decide and what they get, sits in
the manual's seats, marked as a summary of where the skills stop.
No guide ships beside a skill. This repo holds neither skill: it
tries them once, at Step 10's close, on itself, and that close
judges our seat. ADR-0054 records it.

## Commits

**1. `docs(agent): add commit plan for retrospective`**
This plan, agreed.

**2. `docs(adr): 0054, a retrospective convention`**
The decision, opened Proposed. Rejected: the skills under
project-recording; a guide shipped beside each skill; a reviewer's
section inside each skill; holding the guide question; the
deliverer with no seat.

**3. `docs: a retrospective convention, and its skills`**
The manual, `docs/conventions/retrospective/README.md`: the need
from run 3, the reviewer's part in the seats, run 3's evidence as
the why, the deliverer's seat on trial at Step 10's close. The
shipped `delivery/container/.claude/skills/retrospective/SKILL.md`
and `apply-retrospective/SKILL.md`, cleaned of run 3: no run named,
no guide or provisional manual, the records check the playbook
asks for in place of the script, "the records later steps were
built on" in place of "exports", full-word tags, tests "where the
project has them". The PLAN stub's six questions folded into the
walk. The container's birth entry; `ARCHITECTURE.md`'s counts and
owners; agent-arrangement's run's seat; TODO's conventions-map
counts.

**4. `docs: the retrospective leaves project-recording`**
The PLAN stub's Retrospective section goes, and its header comment
points at `RETRO.md`. A records-table row for `RETRO.md` in the
container's entry file. Project-recording §2.4, §9's lifecycle and
its seats point at the convention; agent-arrangement §2.6 says the
skill asks the entry-file re-read.

**5. `docs: Step 10 tries the retrospective here`**
`PLAN.md`: Step 10's "lessons folded back" item becomes the
retrospective run on this repo and applied, on trial; the trial's
verdict says whether we hold the skills.

**6. `docs: records carry the retrospective`**
ADR-0054 Accepted.

**7. `docs(agent): close commit plan for retrospective`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **A convention of its own, taken over from project-recording.**
  Project-recording names the retrospective in three places; left
  there, the subject would live in two manuals. It keeps one
  pointer, as commit-messages does for `commit-plan`.
- **The reviewer's part in the manual's seats, no guide file.** The
  skills already stop at each of the reviewer's decisions; a list
  elsewhere is a summary, and says so. Reopened if a reviewer works
  without reading this repo, or run 4's reading shows the missing
  guide cost something.
- **The PLAN stub's questions are kept, inside the skill.** Run 3's
  walk replaced the questionnaire, but "the entry file read top to
  bottom" is agent-arrangement §2.6's only trigger, and the other
  five are good prompts for finding what went wrong.
- **Container, not method.** Nothing in either skill needs the
  method; slices and kills appear only as examples.
- **No copy here for the trial.** The shipped skills are run from
  `delivery/container/` at Step 10's close; our own copies wait for
  the trial's verdict.
- **The playbook's steps are group C's.** The skills say they run
  before Release; the steps that open them land with the playbook
  (W3), after this set.
- **Run 3 holds its own copies at the same paths, with a guide
  beside each.** Our skills land over its own at the next delivery,
  and its two guides stay as its own files; the note says so.
