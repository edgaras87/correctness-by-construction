# Commit plan: the deliverer's PLAN holds milestones

## Summary — the state after all commits

`PLAN.md` does a job this repo has, rather than a run's. It holds
milestones: things that become true once and have a gate, like a
birth, a release or a concept version. Recurring work is not a
step. Reading runs, delivering and keeping the conventions live in
TODO's Now and in the devlog, which is where they have lived since
2026-09-20: 203 commits since then, and two touched PLAN.

Finished steps are gone, because the stories in them are the
devlog's and the ADRs', and the devlog names the early steps in its
own headings. What is left open is true today. Nothing in the file waits for a project
end the deliverer does not have. project-recording's deliverer seat
says all of this as its fourth difference, and the run's seat and
the container's `PLAN.md` stub do not change.

## Commits

**1. `docs(agent): add commit plan for the PLAN pass`**
This plan.

**2. `docs: PLAN's finished steps take a line each`**
Steps 0 to 9, 279 lines, become one line each: the goal, the
closing date, and where the story lives. Each step's gate facts and
notes are checked against the devlog and the ADRs first, as the
TODO prune checked its entries. A fact with no other home goes into
the devlog in this same commit, before it leaves here.

**3. `docs: PLAN's open steps say what is true today`**
*Provisional.* Step 10 and Release are rewritten so their goals and
gates hold today: the birth as the one open milestone, and Release
read against what "consultable by a stranger" means now. The
header comment still says "kit stub" and goes. Whether anything
else is a milestone, such as concept v2, is decided at this
boundary with the reviewer.

**4. `docs: PLAN's sections serve the deliverer`**
*Provisional.* A decision for each section the stub gave us. The
Retrospective waits for a project end we do not have. "Discovered
along the way" is unused, since TODO takes that job. The decision
index went stale for six ADRs without anyone noticing. Each one is
kept, changed or dropped on the material after steps 2 and 3. The
wording waits on those answers.

**5. `docs: PLAN's finished steps go`**
The reviewer's question at step 4's boundary: what is the Reached
list for? Neither of its two jobs needs it. The seven files citing
"PLAN Step 2" or "Step 3" resolve through the devlog, whose entries
for Steps 0 to 6 are titled by step. And the devlog's headings give
the timeline. PLAN keeps only open milestones, and its header says
where finished ones went.

**6. `docs(conventions): the deliverer plans milestones`**
*Provisional in wording.* The deliverer's seat in
project-recording gains its fourth difference, stated from what
steps 2 to 5 settled, and ADR-0041 opens as Proposed. The run's
seat, §2 and the container's stub stay as they are. README's
records row changes with it if PLAN no longer answers "what's
next" here.

**7. `docs(conventions): the default playbook goes`**
The reviewer's call at step 6's boundary. `playbooks/default.md`
had three jobs and none is live: a fallback for births with no
typed playbook, where this repo births only CbC runs and the
container's stub already covers a birth without one; the base for
new typed playbooks, which the CbC playbook no longer uses; and
the base this repo's retrospective folds into, which ADR-0041
removed. The file goes, and project-recording's list, seat and §9
stop naming it. The CbC playbook's provenance line says it was
removed. ADR-0041, still Proposed, gains a seventh decision. The
seat also gains the sentence behind the whole difference: a run's
step gates are derived from the skill that holds the step, while
the deliverer's milestones come from the situation, no skill
holds them, and their gates are written when they are named.

**8. `docs: the CbC playbook's header says what it is`**
The reviewer's question at step 7's boundary. The playbook opens
with 78 lines of history: its provenance, and each version from v1
to v7 with its reasons. A 10-line version line follows. None of it
reaches a run, because the birth copies from the first step down.
Its stories are ADR-0016's, ADR-0011's and ADR-0007's, the devlog's
for each version, and the file's own git log. §9 asks for a version
and a note of who last updated it, and no more. Each version's
facts are checked against those homes first. What has no other
home goes into the devlog in this same commit, as the TODO prune
did. What stays is what the file is, how a birth uses it, its
current version, and where its history lives. `pure-seed.md`'s
pointer to "its own header" for the v1 deltas is reworded to
point at that history.

**9. `chore(agent): the entry file says where next is`**
*Provisional.* The records table in `CLAUDE.md` gives PLAN "current
state, next steps, gates". Step 6 moved "next" to TODO's Now, so
this row says so. The agent's files never share a commit with the
records, so this is a step of its own.

**10. `docs: devlog carries the PLAN pass`**
The session's entry. ADR-0041 flips to Accepted here. TODO changes
twice. The item on run 3's step form gains an idea: a step form as
PLAN's shape. And a Later item asks whether the playbook needs a
convention of its own, triggered by a second typed playbook. It records
one error of mine from the TODO pass: I closed "Does this repo's
working arrangement still fit it?" as answered by the seats, but its
third fact, what PLAN is for here, was never answered. This set is
the answer.

**11. `docs(conventions): tag two citations in §3 and §7`**
The reviewer's call at step 10's boundary. The check the reviewer
asked for found two slips in project-recording: "(ADR-0020)" and
"(ADR-0038, 1d)" cite this repo's decisions bare, in a manual that
tags them everywhere else. Both gain `CBC`. The third bare
citation there names a fictional project's ADR inside an example,
and stays bare.

**12. `docs(agent): close commit plan for the PLAN pass`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The deliverer's seat, not the manual.** A run's PLAN works:
  run 3's steps lead its work, and its gates are derived at
  opening. The misfit is ours alone, so the change is a seat
  difference, as `CHANGELOG` was one.
- **Material first, the rule after**, as in the TODO pass. Which
  sections stay and what counts as a milestone show up on the
  cleaned file, so the ADR is written from what held.
- **Finished steps go** — reversed at step 4's boundary. The plan
  first said they shrink, since a line each would tell a reader what
  this repo had been through. The reviewer asked what that was for,
  and neither job held: the pointers resolve through the devlog, and
  the devlog's headings are the timeline. It is the TODO rule again,
  where closed work goes.
- **The run-3 reading waits** until this set closes, on the
  reviewer's word. The TODO item stays first in Now.
