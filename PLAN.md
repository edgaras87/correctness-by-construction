# Plan: correctness-by-construction

<!-- One step at a time: the piece of work being done now, in the
     form below. How a step opens and closes is The step form's.
     Findings go to TODO.md the moment they appear, and docs/adr/ lists the ADRs
     itself (ADR-0041, ADR-0057). -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks) or stopped (+the step first)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.

---

## The step form

<!-- Copied into a step when it opens, and filled in. The run's
     form, delivery/fills/cbc-run-pure-playbook.md, adapted to this
     seat (ADR-0057).
     Why the form is as it is: (docs/conventions/project-recording/
     §2.4, How).
     foundation: the project-recording convention -->

**A step is the one piece of work being done now:** a reading of a
run, or a TODO item big enough for a branch. A change set inside it
is a commit plan, and a small item needs no step, nor does a
delivery alone. TODO never repeats the open step; a TODO item that
becomes a step leaves TODO.

```markdown
## Step: <title>  (<the skills, rules and approaches it uses, if any>)    [~]

Goal: <one sentence: what is true when this step is done>
Now: <the stage the step is in, one line>
Gate:
<the opening items below, filled in>
<this step's own items, asked of the goal, then checked against
 its Known already>
<the closing items below, filled in>
Notes: <opened <date>; its stages, and what each uses; what the
 reviewer signs and when; the ADRs and devlog entries behind it>
```

**The Now line names the stage the step is in, and changes when the
step enters a new one, not at every commit.** A step whose approach
is known lists its stages in its Notes: a skill's, an approach on
trial's, or those of earlier work.

Inside a commit plan, the plan and the branch's log show where the
work is.

**The gate is written when the step opens, before any of its
work.** A gate written at the close describes what happened. It
does not set a standard the work was held to.

**At the opening.**

- [ ] The step's branch `<branch>`, if it has one, is cut from main,
      and nothing of the step was done on main except a reading's
      read, which comes before the branch
      (`.claude/rules/working-a-reading.md`, step 1).
- [ ] This gate was written before the work started.
- [ ] The step's approach is known: the skills and rules it uses;
      an approach on trial in `.claude/approaches-on-trial/` that
      covers the work; or the stages its Notes list from earlier
      work. If none, the step drafted one
      (`.claude/approaches-on-trial/approach-drafting.md`).

**The step's own items,** written first, from the goal alone. Ask of
the goal: "how would I check that's true?" Each answer is one item:
a fact, checkable by looking, what and not how. Together they equal
the goal. For `exchange-birth`'s goal "a project born from this repo
alone", one item is "run 5's birth entry names one pin, ours, and
nothing from another repo". What a stage uses sets the order of
work, and its stages are not copied into the gate. An item is ticked
when it comes true, whenever that is.

**Known already.** The gates of the skills and rules a step uses,
their *Gates* sections. Once the own items are written, each is
checked against them by meaning: one already met adds nothing, and
one missed joins as an item. The step's Notes take their stages. A
step that uses none has only its own items.

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `<branch>` follows commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).
- [ ] The step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How*).
- [ ] Each approach on trial the step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

**When every item is ticked and committed,** main takes the step's
branch, if it has one, by fast-forward on the reviewer's word. Then
one commit on main closes the step: it removes the step from this
file and adds the devlog entry, which names the step, what diverged
from the plan, and the commit that holds the ticked gate. Nothing is recorded before the
fast-forward that it would make untrue.

**A step can stop when another must come first.** It stays in
the plan, marked `[!]`: "stopped: <the step that comes first>",
naming the devlog entry that says why. Its Now line
keeps the stage it stopped at. Main takes its branch so far by
fast-forward, on the reviewer's word, and the next step is cut
from main. To resume, its branch is fast-forwarded to main, it
restarts at that stage, and any stage whose input the other step
changed runs again. A ticked item stays ticked unless the other
step made it untrue.

**A trial names the close that judges it.** A piece of the way of
working put on trial says at which step's close it is judged. Its
verdict there is one line: kept, changed or dropped.

**A default that does not fit a step** is struck there, with its
reason. That is a finding about the default, not a step cutting a
corner.

---

## Step: Birth run 6, on full auto  (`.claude/approaches-on-trial/auto-run.md`, `delivery/installs/pure-seed.md`, the foundation check)    [~]

Goal: Run 6 is born from this repo at one pin on main, with the
reviewer's checkout briefing and a hand-off for full auto, ready for
the reviewer to start.
Now: the birth (`.claude/approaches-on-trial/auto-run.md`,
stage 6).
Gate:

**At the opening.**

- [x] The step's branch `run-6-birth-2026-10-29` is cut from main
      at `a002002`, and nothing of the step was done on main
      (2026-10-29).
- [x] This gate was written before the work started (2026-10-29).
- [x] The step's approach is known: `auto-run`, on trial, in its
      second use (2026-10-29).

**The step's own items.**

- [x] The lessons run 5 left for the next run each say keep, change
      or add for run 6, in its hand-off. Run 5 was read in full
      (`temp/reading-run-5-2026-10-22.md`), so this is stage 1's
      light read (2026-10-29, `657d372`).
- [x] Run 6's intent is the reviewer's: checkout, in
      `temp/run-6-briefing.md`, its areas meeting at a
      LAYER-5-INTERACTION question. Larger than run 5's, on the
      reviewer's word: three areas, 6 to 12 slices (2026-10-29,
      `aad9053`).
- [x] The playbook has no line meant for run 5 only: run 5's
      reading's WORK-1, taken here from the stopped step. It now
      names no run at all (2026-10-29, `7f6e3a8`).
- [x] Run 6's hand-off says what full auto means for it, part by
      part as `auto-run` stage 4 lists (2026-10-29, `657d372`).
- [x] What TODO says is due before a birth is settled:
      `exchange-birth` waits for the birth after run 6's (devlog
      2026-10-29, later; 2026-10-29).
- [x] Run 6 is born by `delivery/installs/pure-seed.md` at
      `~/IdeaProjects/cbc-pure-run-6`, its pin a commit on main, the
      seed's own checks all passing (2026-10-29, at `657d372`).
- [x] Run 6's intent and hand-off sit in its `temp/`, and the
      reviewer starts it with the seed's prompt, its review lines
      replaced by full auto (2026-10-29, started by the reviewer).
- [x] `ARCHITECTURE.md` §2.5 lists run 6 (2026-10-29).

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `run-6-birth-2026-10-29` follows
      commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).
- [ ] The step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How*).
- [ ] Each approach on trial the step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

Notes:
- Opened 2026-10-29, from the devlog's entry 2026-10-29, later: the
  reviewer wants run 6 born now, before run 5's lessons are all
  taken. The step for those lessons and the refinement resume
  after this one closes.
- Stages: `auto-run`'s six. Stage 1 is answered by run 5's
  reading; stage 3 is settled; the briefing is stage 2's.

---

## Step: Take run 5's lessons for run 6  (`.claude/rules/working-a-reading.md`, `commit-plan`, the foundation check)    [!] stopped: Birth run 6, on full auto (devlog 2026-10-29, later)

Goal: Run 6 can be born from files that carry what run 5 learned
for it: run 5's reading has DECISION-1, DECISION-2 and DECISION-5
settled, and WORK-1 and WORK-3 to WORK-10 ended.
Now: decide and work (`.claude/rules/working-a-reading.md`, steps 2
to 8).
Gate:

**At the opening.**

- [x] The step's branch `run-5-lessons-2026-10-29` is cut from main
      at `3f20857`, and nothing of the step was done on main
      (2026-10-29).
- [x] This gate was written before the work started (2026-10-29).
- [x] The step's approach is known: `.claude/rules/working-a-reading.md`
      for the reading's items, `commit-plan` for the items marked
      plan, the foundation check for each master changed
      (2026-10-29).

**The step's own items.**

- [ ] Run 5's reading marks DECISION-1, DECISION-2 and DECISION-5
      settled in place, each with how; one that needed an ADR has
      it, Accepted.
- [x] The exchange says how an edit the run never used is judged
      (`docs/conventions/exchange/` §5.2, *A copy the run has finished…*),
      as DECISION-1 settled it. The opening named §6.5. §5.2 is where
      the exchange already speaks of such an edit, and the endings do
      not change (2026-10-29).
- [ ] WORK-1 and WORK-3 to WORK-10 are each marked in the reading
      with its ending, taken, declined or held, and its commit. A
      held one names its trigger and has a TODO line.
- [ ] Each taken edit is in our master, checked against its
      foundation, its file read whole before the commit
      (`.claude/rules/working-a-reading.md`, step 4). A file both
      seats hold changed in both.
- [ ] The playbook has no line meant for run 5 only.
- [ ] The lessons run 5 left for the next hand-off sit where
      DECISION-2 placed them.
- [x] The reading's two slips, named in devlog 2026-10-29, are
      fixed in place: 7 plans, and 12 unused fixes with E1 a use
      note (2026-10-29).
- [ ] The reading's other items are untouched, left for the step
      after the refinement, and the reading stays in `temp/`.

**Known already.** The rule's *Gates* hold when a reading closes;
this step does not close it. Its "every work item has ended" is the
third own item, for this step's items only.

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `run-5-lessons-2026-10-29` follows
      commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).
- [ ] The step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How*).
- [ ] Each approach on trial the step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

Notes:
- Opened 2026-10-29, from the devlog's entry of that day: the
  reviewer chose to take what run 6 needs from run 5's reading
  before run 6's birth. The rest of the reading waits for the
  refinement's close. Run 5's DECISION-1 was taken in talk: each
  fix judged on its own evidence, with the same three endings.
- Stages: decide and work, by the rule's steps 2 to 8. WORK-3,
  WORK-4 and WORK-10 are commit plans of their own. No note goes
  to run 5: it waits for the rest of the reading
  (`exchange-deliver`).
- The reviewer decides each decision, and signs each commit at its
  boundary. Main takes the branch by fast-forward on the reviewer's
  word; then Birth run 6, on full auto, opens.

---

## Step: Refine this repo against its own rules  (`.claude/approaches-on-trial/refinement.md`, `approach-drafting`, `approach-evaluation`, `commit-plan`, the foundation check, `visual-comparison`)    [!] stopped: Take run 5's lessons for run 6, then Birth run 6, on full auto (devlog 2026-10-29)

Goal: Living text written before a rule now meets that rule, and project-recording's list of the records maps them in both seats
(`docs/conventions/project-recording/` §1, *The records at a glance*).
Now: round 2's close read: all the text round 2 covered, read again
against its four kinds
(`.claude/approaches-on-trial/refinement.md` §2.8, *A round's close*).
Gate:

**At the opening.**

- [x] The step's branch `refinement-2026-10-18` is cut from main,
      and nothing of the step was done on main (2026-10-18).
- [x] This gate was written before the work started (2026-10-18).
- [x] No skill, rule or earlier work said how to refine, so the
      step opened a provisional manual by first-time work,
      `2e9c26b:docs/conventions/refinement/README.md`, marked *on
      trial* (2026-10-18). Since ADR-0058 it is the approach on
      trial `.claude/approaches-on-trial/refinement.md`.

**The step's own items.**

- [x] The refinement's file holds every kind the TODO item asked
      for, each in its round, and the reviewer confirmed them
      (`.claude/approaches-on-trial/refinement.md` §2.1, *Group the kinds*; 2026-10-19,
      again with Wiring).
- [x] The refinement's file lists every living file in exactly one
      layer (`.claude/approaches-on-trial/refinement.md` §2.2, *List the files*;
      2026-10-19).
- [x] Before round 1, no rule among the refinement's kinds was in
      doubt, or each doubt was tried on a sample and ended; the
      refinement's file says which
      (`.claude/approaches-on-trial/refinement.md` §2.3, *Check the rules*; 2026-10-19).
- [ ] Before each later round, its rule check read what changed
      since the last, and each doubt ended; the refinement's file
      says which (`.claude/approaches-on-trial/refinement.md` §2.3, *Check the rules*).
- [ ] Every kind in the refinement's file was read in its round
      across all living text, and each read names the files it
      covered.
- [ ] Every finding has the reviewer's ending: fixed, declined
      with its reason, or a TODO item.
- [ ] The last read found nothing that breaks a rule
      (`.claude/approaches-on-trial/refinement.md` §2.9, *The last read*).
- [x] Project-recording's list of the records shows in one view which
      record answers what, in both seats
      (`docs/conventions/project-recording/` §1, *The records at a glance*). It includes
      `RETRO.md`, `COMMIT-PLAN.md`, `docs/system/`, and records
      another convention owns (2026-10-26; one view read as one
      section for both seats, not one screen, ADR-0067 decision 4).
- [x] The records map's form was chosen by `visual-comparison`,
      and that skill's gates hold for it (2026-10-26, ADR-0067;
      rendered by the reviewer before acceptance).
- [ ] Each round's close read has its counts
      (`.claude/approaches-on-trial/refinement.md` §2.8, *A round's close*).
- [ ] The refinement's approach is evaluated: each piece has the
      reviewer's ending, and an ADR records them with the ways
      rejected at the opening
      (`.claude/approaches-on-trial/approach-evaluation.md`).
- [ ] The trials of `approach-drafting` and `approach-evaluation`
      on our seat have their verdicts, one line each: kept, changed
      or dropped.

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `refinement-2026-10-18` follows
      commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).
- [ ] The step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How*).

Notes:
- Opened 2026-10-18 from TODO's refinement item. The records map
  item joined it, as its trigger asked. Both items, with their
  Ideas, are in `TODO.md` at `b3b2018`.
- Stages, from the refinement
  (`.claude/approaches-on-trial/refinement.md` §2, *The stages*):
  1. before round 1: group the kinds into rounds, which creates
     the refinement's file; list the files by layer; check the
     rules (`.claude/approaches-on-trial/refinement.md` §2.1, *Group the kinds* to
     §2.3). The reviewer confirms the kinds, their rounds, the
     layers, whether the method's texts are read here
     (`.claude/approaches-on-trial/refinement.md` §3, *Not known yet*), and that no
     rule is in doubt;
  2. each round: read, list, decide, work, then its close read;
  3. the last read, repeated until it finds nothing;
  4. the close: the refinement's file goes, then
     `.claude/approaches-on-trial/approach-evaluation.md` evaluates
     the refinement's approach.
- The records map is round 2's, in project-recording's layer, its
  form chosen by `visual-comparison`.
- When the work shows the approach wrong, it changes first, in a
  commit of its own
  (`.claude/approaches-on-trial/approach-drafting.md`, stage 2).
- The first use of first-time work on our seat, which ADR-0058
  made `approach-drafting`, and the first of `approach-evaluation`.
  This step's close judges both.
- The reviewer signs: the kinds, their rounds, the layers and the
  rules, before round 1;
  each finding's ending; every commit, at its boundary; each
  ending of the approach's evaluation; main taking the branch.
