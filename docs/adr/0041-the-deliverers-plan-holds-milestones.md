# 0041. The deliverer's plan holds milestones

Date: 2026-09-29
Status: Accepted (2026-09-29, at the set's records commit; opened
Proposed under the commit plan for the PLAN pass, and amended at
two boundaries on the reviewer's readings — decision 6 gained its
reason, a run's gates come from the skill holding the step, and
decision 7, the default playbook goes)

## Context

`docs/conventions/project-recording/` §2 gives `PLAN.md` three
questions — where are we, what's next, what does *done* mean — and
a shape built for a journey: steps from a playbook, a rolling wave,
a Retrospective at the project's end whose lessons fold back into
that playbook. A run is that journey, and its plan works: run 3's
steps lead its work, and each gate is derived when its step opens.

This repo's plan did not lead its work. From 2026-09-20, with
Step 10 in progress, 203 commits landed and two touched `PLAN.md`,
one of them an index catch-up. Change set after change set ran with
no step around it — the exchange, shapes, the conventions manual,
the walk, the TODO pass — and what was next lived in TODO's Now and
in each devlog entry's Resume. Step 7 was written after its work was
done, over sixteen decisions and three seeded runs; its own notes
said so, and one of Step 10's gate items was ticked for work done
before the step existed. The decision index went stale twice,
0014 to 0020 and 0035 to 0040. "Discovered along the way" never
held a finding. The Retrospective waited for a project end that
the deliverer's seat already said it does not have.

The work this repo does is mostly recurring: reading runs,
delivering, keeping the conventions. Only some of it becomes true
once and stays true — a birth, a release, a concept version.

## Options considered

- **Keep the plan as §2 describes it and keep it current.** Rejected
  on the evidence: two catch-ups of the index and a retroactive step
  show the upkeep does not happen, because nothing in the work
  reaches for the plan.
- **A step per change set.** Rejected: a change set already has its
  plan, `COMMIT-PLAN.md`, and its record, the devlog. A step around
  each would describe it a third time, and after the fact.
- **Finished steps kept as one line each, a "Reached" list.** Tried
  and removed at the reviewer's question. Its two jobs were keeping
  seven "PLAN Step 2/3" pointers resolvable and a short timeline.
  The devlog's entries for Steps 0 to 6 are titled by step, so the
  pointers resolve there, and its headings are the timeline.
- **Change §2 for both seats.** Rejected: a run's plan works, and its
  finished steps are the evidence its playbook is folded from. The
  misfit is the deliverer's alone, as `CHANGELOG`'s was.

## Decision

1. **The deliverer's `PLAN.md` holds milestones only** — things
   that become true once and have a gate.
2. **Recurring work is not a step.** TODO's Now holds what is next;
   the devlog tells what happened.
3. **A reached milestone leaves the plan.** The devlog entry that
   closes it names the step, so a pointer to it still resolves.
4. **Each milestone closes with the retrospective's two jobs** as
   gate items: its lessons folded back where they came from, and
   `CLAUDE.md` re-read against its three tests.
5. **No Retrospective, no "Discovered along the way", no decision
   index** in the deliverer's plan: no project end, TODO takes
   findings at once, and `docs/adr/` lists itself.
6. **A seat difference, not a change to §2.** project-recording's
   deliverer seat states it as its fourth difference; the run's
   seat, §2, §3's index and the container's `PLAN.md` stub stay as
   they are. The seat says why: a run's step names the skill that
   holds it and derives its gate from that skill; the deliverer's
   milestones come from the situation, and no skill holds them.
7. **The default playbook goes** (the reviewer, at step 6's
   boundary). `playbooks/default.md` had three jobs and none is
   live. It was the fallback for a birth with no typed playbook,
   but only CbC runs are born here, and the container's stub
   already covers a birth without one. It was the base for new
   typed playbooks, and the CbC playbook no longer builds on it.
   And it was what this repo's retrospective folded into, which
   decision 5 removes. If a new repo needs a playbook, it is
   derived from this repo's history.

## Consequences

- `PLAN.md` went from 419 lines to 56: a header saying where
  finished milestones go, the legend, Step 10 and Release.
- README's Plan row answers which milestones are open; its Backlog
  row answers what is next.
- The seven pointers to "PLAN Step 2" and "Step 3" in the concept
  chapters, the startup snippet and `delivery/README.md` now resolve
  through the devlog.
- `playbooks/` is gone. project-recording names one playbook, the
  CbC run's, and §9 says a birth without one fills the stub in
  place.
- ADR-0024 decision 4 was wrong since 2026-09-18 and the correction
  lived only in the removed Step 8 gate; it carries a dated
  amendment now.
- Reopen when a milestone's work runs long enough to need a step's
  rolling wave again — the case §2 was built for.
