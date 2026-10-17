# 0057. Our plan holds the step being worked

Date: 2026-10-17
Status: Accepted (2026-10-17, at the set's records commit; opened
Proposed under the commit plan for plan steps, and revised at two
boundaries on the reviewer's questions — a step takes the gates of
the skills and rules it uses, so a reading's live in its rule, and
its own items are written first, the gates checked after)

## Context

ADR-0041 made this repo's `PLAN.md` hold milestones only: things
that become true once, like a birth or a release. Recurring work,
such as reading a run, was not a step; TODO's Now held what was
next.

The plan still did not lead the work. From 2026-09-30 to `534daba`,
where this work began, 364 commits landed and 3 touched `PLAN.md`;
none of the three was a step being worked. Step 10 has been in
progress since 2026-09-20, its three open items waiting on a birth
nobody was working toward. Release was never opened.

Meanwhile the reading of run 3 ran from 2026-10-15 with 13 work
items and 10 decisions. Its gate, what must be true for it to close,
lived in `working-a-reading.md` step 9 and in the reading file,
never in the plan. TODO's Now is headed "current plan step", and no
step existed.

ADR-0041 named its own reopen condition: "when a milestone's work
runs long enough to need a step's rolling wave again." A reading is
that work. And run 3's retrospective gave the playbook a step form
(ADR-0055) built for exactly this: a gate written at opening, a Now
line by stage, opening and closing items.

## Options considered

- **Keep ADR-0041.** Rejected on the evidence: 3 commits of 364.
- **Only readings as steps.** Rejected: `exchange-birth` and the
  TODO pass are the same kind of long work, and would still have
  no step.
- **A step per change set.** Rejected again, as ADR-0041 did: a
  change set has `COMMIT-PLAN.md` and the devlog.
- **The playbook's form kept whole, the one-line closed gate
  included.** Rejected: a run keeps its finished steps because its
  playbook is folded from them; nothing is folded from ours.
- **The form in a rule or a skill,** or only in project-recording.
  Rejected: opening a step is a moment in `PLAN.md` itself, and a
  manual reaches its maintainer, not the step.
- **The reading's work items as gate items.** Rejected: two homes,
  and the list grows while it is worked.
- **A reading's close items listed in PLAN's form.** Rejected on
  the reviewer's word: a second home for what its rule holds, and
  every new kind of step would edit PLAN.
- **The read and the work as two steps.** Rejected: the read alone
  has no outcome worth a gate, and an extension would reopen a
  closed step.
- **`exchange-read` and `working-a-reading.md` merged.** Rejected:
  a skill fires only when called and a reading is worked across
  sessions; a rule never loads before the reading file exists; and
  the two stand on different foundations.
- **Step 10 and Release kept in PLAN,** as named milestones or with
  Step 10 open until the birth. Rejected: an unworked step in the
  plan is how it went stale.
- **Our `first-time-work` opening at a step only.** Rejected: new
  work inside a step, or too small for one, would have no moment.
- **The open step also listed in TODO's Now.** Rejected: two homes.

## Decision

1. **A step is the one piece of work being done now:** a reading,
   or a TODO item big enough for a branch. One at a time, its gate
   written when it opens. A change set inside it stays in
   `COMMIT-PLAN.md`, and a small item needs no step.
2. **The run's step form, taken almost whole,** as `## The step
   form` at the top of our `PLAN.md`: Goal, a Now line by stage,
   the gate written at opening, Notes; the opening items, with the
   branch "if it has one"; the step's own items, written first
   from the goal; Known already, the gates of the skills and rules
   a step uses, checked against them after by meaning.
   Dropped: *For run 5 only*, the shapes item, decision before code,
   and the one-line closed gate, since a step leaves the plan and
   the devlog names it with the commit of the ticked gate. Kept from
   ADR-0041 as every step's closing items: lessons folded back, and
   `CLAUDE.md` re-read.
3. **A reading is one step.** Its gates and stages are those of the
   skills and rules it uses: `working-a-reading.md` holds the close
   (every finding ended, every work item ended and marked, the note
   in the run, the lessons placed, the reading deleted), copied into
   the step when it opens. Its F, D and W stay in the reading. An
   extension returns Now to read, and the branch is cut right after
   the read. A delivery is a reading step's note stage, an own item
   of the step whose change it sends, or, alone, a TODO item. The two
   reading rules stay apart, each on its own foundation. Run 3's
   reading finishes as it began; run 4's is the first step.
4. **Step 10 and Release leave the plan.** The birth joins TODO's
   `exchange-birth`, due at run 5's birth. Our retrospective becomes
   a TODO item, due at the birth step's close, the moment Step 10's
   close stood for. Release waits in TODO's Later with its four own
   items.
5. **Our `first-time-work` opens at three moments,** each with
   nothing to say how: a step's opening item, a work item inside a
   step, a small TODO item come due.
6. **PLAN holds the open step, and TODO never repeats it.** TODO's
   Now holds small items due while the step is open; Next, the next
   step's candidates and items not yet due. A TODO item that becomes
   a step leaves TODO. Until run 3's reading closes, PLAN says no
   step is open.
7. **Amends ADR-0041's decisions 1 and 2, and ADR-0056's decision
   6.** ADR-0041's decisions 3 to 7 stand.

## Consequences

- `PLAN.md` holds its step form and the open step, or a line saying
  none is open.
- project-recording's deliverer seat says steps, not milestones,
  and points at the step form. The retrospective's trial moves to
  the close of the step that runs the next birth.
- `.claude/rules/working-a-reading.md` holds a reading's gates and
  stages, for its step. Our `first-time-work` opens at a step too.
- The reason that rested on the deliverer having no steps or gates,
  in shapes' deliverer seat and conventions §3.3, is gone. Both say
  our forms are rules today, and whether they become shapes is open
  (TODO).
- `exchange-read` step 4 names `.claude/rules/exchange-reading.md`
  where it said "the shape".
- Reopen if steps go stale as milestones did: an open step nobody
  works, or work running with no step around it.
