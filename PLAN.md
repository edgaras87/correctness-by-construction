# Plan: correctness-by-construction

<!-- One step at a time: the piece of work being done now, in the
     form below. Its gate is written when it opens. When it closes
     it leaves this file, and the devlog entry that closes it names
     the step and the commit of its ticked gate. Findings go to
     TODO.md the moment they appear, and docs/adr/ lists the ADRs
     itself (ADR-0041, ADR-0057). -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks) or stopped (+the step first)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.

---

## The step form

<!-- Copied into a step when it opens, and filled in. The run's
     form, delivery/fills/cbc-run-pure-playbook.md, adapted to this
     seat (ADR-0057).
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
      (`docs/conventions/commit-messages/` §2).
- [ ] The step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4).
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
with a pointer to the devlog entry that says why. Its Now line
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

## Step: Refine this repo against its own rules  (`.claude/approaches-on-trial/refinement.md`, `approach-drafting`, `approach-evaluation`, `commit-plan`, the foundation check, `visual-comparison`)    [~]

Goal: Living text written before a rule now meets that rule, and
`docs/conventions/project-recording/` §1 is a map of the records
in both seats.
Now: round 2's work: every finding has its ending, and layer 1,
the conventions manual, is worked first
(`.claude/approaches-on-trial/refinement.md` §2.7).
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
      (`.claude/approaches-on-trial/refinement.md` §2.1; 2026-10-19,
      again with Wiring).
- [x] The refinement's file lists every living file in exactly one
      layer (`.claude/approaches-on-trial/refinement.md` §2.2;
      2026-10-19).
- [x] Before round 1, no rule among the refinement's kinds was in
      doubt, or each doubt was tried on a sample and ended; the
      refinement's file says which
      (`.claude/approaches-on-trial/refinement.md` §2.3; 2026-10-19).
- [ ] Before each later round, its rule check read what changed
      since the last, and each doubt ended; the refinement's file
      says which (`.claude/approaches-on-trial/refinement.md` §2.3).
- [ ] Every kind in the refinement's file was read in its round
      across all living text, and each read names the files it
      covered.
- [ ] Every finding has the reviewer's ending: fixed, declined
      with its reason, or a TODO item.
- [ ] The last read found nothing that breaks a rule
      (`.claude/approaches-on-trial/refinement.md` §2.9).
- [x] `docs/conventions/project-recording/` §1 shows in one view
      which record answers what, in both seats. It includes
      `RETRO.md`, `COMMIT-PLAN.md`, `docs/system/`, and records
      another convention owns (2026-10-26; one view read as one
      section for both seats, not one screen, ADR-0067 decision 4).
- [x] The records map's form was chosen by `visual-comparison`,
      and that skill's gates hold for it (2026-10-26, ADR-0067;
      rendered by the reviewer before acceptance).
- [ ] Each round's close read has its counts
      (`.claude/approaches-on-trial/refinement.md` §2.8).
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
      (`docs/conventions/commit-messages/` §2).
- [ ] The step's lessons are folded back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4).

Notes:
- Opened 2026-10-18 from TODO's refinement item. The records map
  item joined it, as its trigger asked. Both items, with their
  Ideas, are in `TODO.md` at `b3b2018`.
- Stages, from `.claude/approaches-on-trial/refinement.md` §2:
  1. before round 1: group the kinds into rounds, which creates
     the refinement's file; list the files by layer; check the
     rules (`.claude/approaches-on-trial/refinement.md` §2.1 to
     §2.3). The reviewer confirms the kinds, their rounds, the
     layers, whether the method's texts are read here
     (`.claude/approaches-on-trial/refinement.md` §3), and that no
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
