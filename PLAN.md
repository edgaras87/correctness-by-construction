# Plan: correctness-by-construction

<!-- One Plan Step at a time: the piece of work being done now, in the
     form below. How a Plan Step opens and closes is the Plan Step Form's.
     Findings go to TODO.md the moment they appear, and docs/adr/ lists the ADRs
     itself (ADR-0041, ADR-0057). -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks) or stopped (+the Plan Step first)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A Plan Step is done only when every gate item is true.

---

## The Plan Step Form

<!-- Copied into a Plan Step when it opens, and filled in. The CBC Run's
     form, delivery/fills/cbc-run-pure-playbook.md, adapted to this
     Convention Seat (ADR-0057).
     Why the form is as it is: (docs/conventions/project-recording/
     §2.4, How a plan is written).
     foundation: the project-recording convention -->

**A Plan Step is the one piece of work being done now:** a Run Reading of a
CBC Run, or a TODO item big enough for a branch. A Change Set inside it
is a commit plan, and a small item needs no Plan Step, nor does a
delivery alone. TODO never repeats the open Plan Step; a TODO item that
becomes a Plan Step leaves TODO.

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

**The Now line names the stage the Plan Step is in, and changes when the
Plan Step enters a new one, not at every commit.** A Plan Step whose Work Approach
is known lists its stages in its Notes: a skill's, an Approach on
Trial's, or those of earlier work.

Inside a commit plan, the plan and the branch's log show where the
work is.

**The gate is written when the Plan Step opens, before any of its
work.** A gate written at the close describes what happened. It
does not set a standard the work was held to.

**At the opening.**

- [ ] The Plan Step's branch `<branch>`, if it has one, is cut from main,
      and nothing of the Plan Step was done on main except a Run Reading's
      read, which comes before the branch
      (`.claude/rules/working-a-reading.md`, step 1).
- [ ] This gate was written before the work started.
- [ ] The Plan Step's Work Approach is known: the skills and Agent Rules it uses;
      an Approach on Trial in `.claude/approaches-on-trial/` that
      covers the work; or the stages its Notes list from earlier
      work. If none, the Plan Step drafted one
      (`.claude/approaches-on-trial/approach-drafting.md`).

**The Plan Step's own items,** written first, from the goal alone. Ask of
the goal: "how would I check that's true?" Each answer is one item:
a fact, checkable by looking, what and not how. Together they equal
the goal. For `exchange-birth`'s goal "a project born from this repo
alone", one item is "CBC Run 5's birth entry names one Delivery Pin, ours, and
nothing from another repo". What a stage uses sets the order of
work, and its stages are not copied into the gate. An item is ticked
when it comes true, whenever that is.

**Known already.** The gates of the skills and Agent Rules a Plan Step uses,
their *Gates* sections. Once the own items are written, each is
checked against them by meaning: one already met adds nothing, and
one missed joins as an item. The Plan Step's Notes take their stages. A
Plan Step that uses none has only its own items.

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `<branch>` follows commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
- [ ] The Plan Step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How the entry file is written*).
- [ ] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

**When every item is ticked and committed,** main takes the Plan Step's
branch, if it has one, by fast-forward on the reviewer's word. Then
one commit on main closes the Plan Step: it removes the Plan Step from this
file and adds the devlog entry, which names the Plan Step, what diverged
from the plan, and the commit that holds the ticked gate. Nothing is recorded before the
fast-forward that it would make untrue.

**A Plan Step can stop when another must come first.** It stays in
the plan, marked `[!]`: "stopped: <the Plan Step that comes first>",
naming the devlog entry that says why. Its Now line
keeps the stage it stopped at. Main takes its branch so far by
fast-forward, on the reviewer's word, and the next Plan Step is cut
from main. To resume, its branch is fast-forwarded to main, it
restarts at that stage, and any stage whose input the other Plan Step
changed runs again. A ticked item stays ticked unless the other
Plan Step made it untrue.

**A trial names the close that judges it.** A piece of the way of
working put on trial says at which Plan Step's close it is judged. Its
verdict there is one line: kept, changed or dropped.

**A default that does not fit a Plan Step** is struck there, with its
reason. That is a finding about the default, not a Plan Step cutting a
corner.

---

## Step: Birth CBC Run 6, on full auto  (`.claude/approaches-on-trial/auto-run.md`, `delivery/installs/pure-seed.md`, the Foundation Check)    [!] stopped: Refine this repo against its own rules (devlog 2026-10-29, morning)

Goal: CBC Run 6 is born from this repo at one Delivery Pin on main, with the
reviewer's checkout Run Briefing and a Run Hand-off for full auto, ready for
the reviewer to start.
Now: the close: its checks, `auto-run`'s note of this use, main
taking the branch.
Gate:

**At the opening.**

- [x] The Plan Step's branch `run-6-birth-2026-10-29` is cut from main
      at `a002002`, and nothing of the Plan Step was done on main
      (2026-10-29).
- [x] This gate was written before the work started (2026-10-29).
- [x] The Plan Step's Work Approach is known: `auto-run`, on trial, in its
      second use (2026-10-29).

**The Plan Step's own items.**

- [x] The lessons CBC Run 5 left for the next CBC Run each say keep, change
      or add for CBC Run 6, in its Run Hand-off. CBC Run 5 was read in full
      (`temp/reading-run-5-2026-10-22.md`), so this is stage 1's
      light read (2026-10-29, `657d372`).
- [x] CBC Run 6's intent is the reviewer's: checkout, in
      `temp/run-6-briefing.md`, its areas meeting at a
      LAYER-5-INTERACTION question. Larger than CBC Run 5's, on the
      reviewer's word: three areas, 6 to 12 slices (2026-10-29,
      `aad9053`).
- [x] The playbook has no line meant for CBC Run 5 only: CBC Run 5's
      Run Reading's WORK-1, taken here from the stopped Plan Step. It now
      names no CBC Run at all (2026-10-29, `7f6e3a8`).
- [x] CBC Run 6's Run Hand-off says what full auto means for it, part by
      part as `auto-run` stage 4 lists (2026-10-29, `657d372`).
- [x] What TODO says is due before a birth is settled:
      `exchange-birth` waits for the birth after CBC Run 6's (devlog
      2026-10-29, later; 2026-10-29).
- [x] CBC Run 6 is born by `delivery/installs/pure-seed.md` at
      `~/IdeaProjects/cbc-pure-run-6`, its Delivery Pin a commit on main, the
      Pure Seed's own checks all passing (2026-10-29, at `657d372`).
- [x] CBC Run 6's intent and Run Hand-off sit in its `temp/`, and the
      reviewer starts it with the Pure Seed's prompt, its review lines
      replaced by full auto (2026-10-29, started by the reviewer).
- [x] `ARCHITECTURE.md` §2.5 lists CBC Run 6 (2026-10-29).

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `run-6-birth-2026-10-29` follows
      commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
- [ ] The Plan Step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How the entry file is written*).
- [ ] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

Notes:
- Opened 2026-10-29, from the devlog's entry 2026-10-29, later: the
  reviewer wants CBC Run 6 born now, before CBC Run 5's lessons are all
  taken. The Plan Step for those lessons and the refinement resume
  after this one closes.
- Stages: `auto-run`'s six. Stage 1 is answered by CBC Run 5's
  reading; stage 3 is settled; the Run Briefing is stage 2's.

---

## Step: Take CBC Run 5's lessons for CBC Run 6  (`.claude/rules/working-a-reading.md`, `commit-plan`, the Foundation Check)    [!] stopped: Birth CBC Run 6, on full auto (devlog 2026-10-29, later)

Goal: CBC Run 6 can be born from files that carry what CBC Run 5 learned
for it: CBC Run 5's Run Reading has DECISION-1, DECISION-2 and DECISION-5
settled, and WORK-1 and WORK-3 to WORK-10 ended.
Now: decide and work (`.claude/rules/working-a-reading.md`, steps 2
to 8).
Gate:

**At the opening.**

- [x] The Plan Step's branch `run-5-lessons-2026-10-29` is cut from main
      at `3f20857`, and nothing of the Plan Step was done on main
      (2026-10-29).
- [x] This gate was written before the work started (2026-10-29).
- [x] The Plan Step's Work Approach is known: `.claude/rules/working-a-reading.md`
      for the Run Reading's items, `commit-plan` for the items marked
      plan, the Foundation Check for each Master Copy changed
      (2026-10-29).

**The Plan Step's own items.**

- [ ] CBC Run 5's Run Reading marks DECISION-1, DECISION-2 and DECISION-5
      settled in place, each with how; one that needed an ADR has
      it, Accepted.
- [x] the Exchange Convention says how an edit the CBC Run never used is judged
      (`docs/conventions/exchange/` §5.2, *A finished copy*),
      as DECISION-1 settled it. The opening named §6.5. §5.2 is where
      the Exchange Convention already speaks of such an edit, and the endings do
      not change (2026-10-29).
- [ ] WORK-1 and WORK-3 to WORK-10 are each marked in the Run Reading
      with its ending, taken, declined or held, and its commit. A
      held one names its trigger and has a TODO line.
- [ ] Each taken edit is in our Master Copy, checked against its
      foundation, its file read whole before the commit
      (`.claude/rules/working-a-reading.md`, step 4). A file both
      Convention Seats hold changed in both.
- [ ] The playbook has no line meant for CBC Run 5 only.
- [ ] The lessons CBC Run 5 left for the next Run Hand-off sit where
      DECISION-2 placed them.
- [x] The Run Reading's two slips, named in devlog 2026-10-29, are
      fixed in place: 7 plans, and 12 unused fixes with E1 a use
      note (2026-10-29).
- [ ] The Run Reading's other items are untouched, left for the Plan Step
      after the refinement, and the Run Reading stays in `temp/`.

**Known already.** The rule's *Gates* hold when a Run Reading closes;
this Plan Step does not close it. Its "every work item has ended" is the
third own item, for this Plan Step's items only.

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `run-5-lessons-2026-10-29` follows
      commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
- [ ] The Plan Step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How the entry file is written*).
- [ ] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

Notes:
- Opened 2026-10-29, from the devlog's entry of that day: the
  reviewer chose to take what CBC Run 6 needs from CBC Run 5's Run Reading
  before CBC Run 6's birth. The rest of the Run Reading waits for the
  refinement's close. CBC Run 5's DECISION-1 was taken in talk: each
  fix judged on its own evidence, with the same three endings.
- Stages: decide and work, by the rule's steps 2 to 8. WORK-3,
  WORK-4 and WORK-10 are commit plans of their own. No note goes
  to CBC Run 5: it waits for the rest of the Run Reading
  (`exchange-deliver`).
- The reviewer decides each decision, and signs each commit at its
  boundary. Main takes the branch by fast-forward on the reviewer's
  word; then Birth CBC Run 6, on full auto, opens.

---

## Step: Refine this repo against its own rules  (`.claude/approaches-on-trial/refinement.md`, `approach-drafting`, `approach-evaluation`, `commit-plan`, the Foundation Check, `visual-comparison`)    [~]

Goal: Living text written before a rule now meets that rule, and project-recording's list of the records maps them in both Convention Seats
(`docs/conventions/project-recording/` §1, *The records at a glance*).
Now: Refinement Round 3 reads (`.claude/approaches-on-trial/refinement.md` §2.4, *Reading the Finding Kinds*),
`temp/refinement-2026-10-18.md`'s *Met in round 2, of other kinds* first.
Gate:

**At the opening.**

- [x] The Plan Step's branch `refinement-2026-10-18` is cut from main,
      and nothing of the Plan Step was done on main (2026-10-18).
- [x] This gate was written before the work started (2026-10-18).
- [x] No skill, Agent Rule or earlier work said how to refine, so the
      Plan Step opened a provisional manual by first-time work,
      `2e9c26b:docs/conventions/refinement/README.md`, marked *on
      trial* (2026-10-18). Since ADR-0058 it is the Work Approach on
      trial `.claude/approaches-on-trial/refinement.md`.

**The Plan Step's own items.**

- [x] The refinement's file holds every Finding Kind the TODO item asked
      for, each in its Refinement Round, and the reviewer confirmed them
      (`.claude/approaches-on-trial/refinement.md` §2.1, *Group the Finding Kinds*; 2026-10-19,
      again with Wiring).
- [x] The refinement's file lists every living file in exactly one
      Refinement Layer (`.claude/approaches-on-trial/refinement.md` §2.2, *List the files*;
      2026-10-19).
- [x] Before Refinement Round 1, no rule among the refinement's Finding Kinds was in
      doubt, or each doubt was tried on a sample and ended; the
      refinement's file says which
      (`.claude/approaches-on-trial/refinement.md` §2.3, *Check the rules*; 2026-10-19).
- [ ] Before each later Refinement Round, its rule check read what changed
      since the last, and each doubt ended; the refinement's file
      says which (`.claude/approaches-on-trial/refinement.md` §2.3, *Check the rules*).
- [ ] Every Finding Kind in the refinement's file was read in its Refinement Round
      across all living text, and each read names the files it
      covered.
- [ ] Every finding has the reviewer's ending: fixed, declined
      with its reason, or a TODO item.
- [ ] The last read found nothing that breaks a rule
      (`.claude/approaches-on-trial/refinement.md` §2.9, *The last read*).
- [x] Project-recording's list of the records shows in one view which
      record answers what, in both Convention Seats
      (`docs/conventions/project-recording/` §1, *The records at a glance*). It includes
      `RETRO.md`, `COMMIT-PLAN.md`, `docs/system/`, and records
      another convention owns (2026-10-26; one view read as one
      section for both Convention Seats, not one screen, ADR-0067 decision 4).
- [x] The records map's form was chosen by `visual-comparison`,
      and that skill's gates hold for it (2026-10-26, ADR-0067;
      rendered by the reviewer before acceptance).
- [ ] Each Refinement Round's close read has its counts
      (`.claude/approaches-on-trial/refinement.md` §2.8, *A Refinement Round's close*).
- [ ] The refinement's Work Approach is evaluated: each piece has the
      reviewer's ending, and an ADR records them with the ways
      rejected at the opening
      (`.claude/approaches-on-trial/approach-evaluation.md`).
- [ ] The trials of `approach-drafting` and `approach-evaluation`
      on our Convention Seat have their verdicts, one line each: kept, changed
      or dropped.

**At the close.**

- [ ] Every link and path in the records resolves; every ADR a
      record cites exists; each pair of copies agrees, such as the
      worked example in `cbc-framing` and in `cbc-slice`.
- [ ] No living line in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `refinement-2026-10-18` follows
      commit-messages.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
- [ ] The Plan Step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How the entry file is written*).

Notes:
- Opened 2026-10-18 from TODO's refinement item. The records map
  item joined it, as its trigger asked. Both items, with their
  Ideas, are in `TODO.md` at `b3b2018`.
- Stages, from the refinement
  (`.claude/approaches-on-trial/refinement.md` §2, *The Approach Stages*):
  1. before Refinement Round 1: group the Finding Kinds into Refinement Rounds, which creates
     the refinement's file; list the files by Refinement Layer; check the
     rules (`.claude/approaches-on-trial/refinement.md` §2.1, *Group the Finding Kinds* to
     §2.3). The reviewer confirms the Finding Kinds, their Refinement Rounds, the
     Refinement Layers, whether the method's texts are read here
     (`.claude/approaches-on-trial/refinement.md` §3, *Not known yet*), and that no
     rule is in doubt;
  2. each Refinement Round: read, list, decide, work, then its close read;
  3. the last read, repeated until it finds nothing;
  4. the close: the refinement's file goes, then
     `.claude/approaches-on-trial/approach-evaluation.md` evaluates
     the refinement's Work Approach.
- The records map is Refinement Round 2's, in project-recording's Refinement Layer, its
  form chosen by `visual-comparison`.
- When the work shows the Work Approach wrong, it changes first, in a
  commit of its own
  (`.claude/approaches-on-trial/approach-drafting.md`, stage 2).
- The first use of first-time work on our Convention Seat, which ADR-0058
  made `approach-drafting`, and the first of `approach-evaluation`.
  This Plan Step's close judges both.
- The reviewer signs: the Finding Kinds, their Refinement Rounds, the Refinement Layers and the
  rules, before Refinement Round 1;
  each finding's ending; every commit, at its boundary; each
  ending of the Work Approach's evaluation; main taking the branch.
