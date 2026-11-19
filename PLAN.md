# Plan: correctness-by-construction

<!-- One Plan Step at a time: the piece of work being done now, in the
     form below. How a Plan Step opens and closes is the Plan Step Form's.
     Findings go to TODO.md the moment they appear, and docs/adr/ lists the ADRs
     itself (ADR-0041, ADR-0057). -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks) or stopped (+the Plan Step that must come first)  ·  `[-]` skipped (+why)

**Plan Step Gate** = exit criteria: verifiable facts, not intentions. A Plan Step is done only when every Plan Step Gate item is true.

---

## The Plan Step Form

<!-- Copied into a Plan Step when it opens, and filled in. The CBC Run's
     form, delivery/fills/cbc-run-pure-playbook.md, adapted to this
     Convention Seat (ADR-0057).
     Why the form is as it is: (docs/conventions/project-recording/
     §2.4, How a plan is written).
     foundation: the project-recording convention -->

**A Plan Step is the one piece of work being done now:** a CBC Run Reading,
or a TODO item big enough for a branch. A Change Set inside it is a
commit plan. A small item needs no Plan Step, nor does a delivery
alone. TODO never repeats the open Plan Step; a TODO item that
becomes a Plan Step leaves TODO.

```markdown
## Step: <title>  (<the Agent Skills, Agent Rules and Approaches on Trial it uses, if any>)    [~]

Goal: <one sentence: what is true when this Plan Step is done>
Now: <the Agent Skill Stage or Approach on Trial Stage this Plan Step is in, or a stage its Notes list; one line>
Gate:
<the opening items below, filled in>
<this Plan Step's own items, asked of the goal, then checked against
 its Known already>
<the closing items below, filled in>
Notes: <opened <date>; its stages, and what each uses; what the
 reviewer signs and when; the ADRs and devlog entries behind it>
```

**The Now line names the stage the Plan Step is in, and changes when the
Plan Step enters a new one, not at every commit.** A Plan Step whose Work Approach
is known lists its stages in its Notes: an Agent Skill's, an Approach on
Trial's, or those of earlier work.

Inside a commit plan, the plan and the branch's log show where the
work is.

**The Plan Step Gate is written when the Plan Step opens, before any of its
work.** A Plan Step Gate written at the close describes what happened. It
does not set a standard the work was held to.

**At the opening.**

- [ ] The Plan Step's branch `<branch>`, if it has one, is cut from main,
      and nothing of the Plan Step was done on main except a CBC Run Reading's
      read, which comes before the branch
      (`.claude/rules/working-a-reading.md`, step 1).
- [ ] This Plan Step Gate was written before the work started.
- [ ] The Plan Step's Work Approach is known: the Agent Skills and Agent Rules it uses;
      an Approach on Trial in `.claude/approaches-on-trial/` that
      covers the work; or the stages its Notes list from earlier
      work. If none, the Plan Step drafted one
      (`.claude/approaches-on-trial/approach-drafting.md`).

**The Plan Step's own items,** written first, from the goal alone. Ask of
the goal: "how would I check that's true?" Each answer is one item:
a fact, checkable by looking, what and not how. Together they equal
the goal. For the goal of the Plan Step Birth CBC Run 6, "CBC Run 6 is born from
this repo at one Delivery Pin on main", one item is "CBC Run 6's birth entry names
one Delivery Pin, ours, and nothing from another repo". What a stage uses sets the order of
work, and its stages are not copied into the Plan Step Gate. An item is ticked
when it comes true, whenever that is.

**Known already.** The gates of the Agent Skills and Agent Rules a Plan Step uses,
their *Gates* sections. Once the own items are written, each is
checked against them by meaning: one already met adds nothing, and
one missed joins as an item. The Plan Step's Notes take their stages. A
Plan Step that uses none has only its own items.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `<branch>` follows the commit-messages Agent Skill.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
- [ ] The Plan Step's lessons are written back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How the Entry File is written*).
- [ ] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md` §3, *Close*).

**When every item is ticked and committed,** main takes the Plan Step's
branch, if it has one, by fast-forward on the reviewer's word. Then
one commit on main closes the Plan Step. It removes the Plan Step from
this file and adds the devlog entry. The entry names the Plan Step,
what diverged from the plan, and the commit that holds the ticked
Plan Step Gate. Nothing is recorded before the
fast-forward that it would make untrue.

**A Plan Step can stop when another must come first.** It stays in
the plan, marked `[!]`: "stopped: <the Plan Step that comes first>",
naming the devlog entry that says why. Its Now line
keeps the stage it stopped at. Main takes its branch so far by
fast-forward, on the reviewer's word, and the next Plan Step is cut
from main. To resume, its branch is fast-forwarded to main, and it
restarts at that stage. Any stage whose input the other Plan Step
changed runs again. A ticked item stays ticked unless the other
Plan Step made it untrue.

**A Plan Step whose goal grew past one piece of work is re-cut.** Its
own items are struck, each naming the TODO item it moved to; its
stages become TODO items; and it closes as above, its devlog entry
saying why.

**A trial names the close that judges it.** A change to how work is
done, put on trial, names the Plan Step whose close judges it. Its
verdict there is one line: kept, changed or dropped.

**An item given here that does not fit a Plan Step** is struck there, with its
reason. That is a finding about the item, not a Plan Step skipping
work.

---

## Step: Give Change one home  (the commit-plan Agent Skill)    [~]

Goal: each fact of Change is written once, in the simulation, until
the change flow is done, and every other place points there.
Now: the commit plan's work, `COMMIT-PLAN.md`.
Gate:

**At the opening.**

- [x] The Plan Step's branch `change-home-2026-11-19` is cut from main
      at `385a684`, and nothing of the Plan Step was done on main
      (2026-11-19).
- [x] This Plan Step Gate was written before the work started
      (2026-11-19, in `96426d4`, the branch's first commit).
- [x] The Plan Step's Work Approach is known: the commit-plan Agent
      Skill, for its Change Set; the one-home, writing and
      foundation-check Agent Rules (2026-11-19).

**The Plan Step's own items.**

- [x] The simulation's header says it holds the facts of Change until
      the change flow is done, and that they then move to their final
      home, by the TODO item's third step (2026-11-19).
- [x] The problem file's §2.1 states no fact of Change: its rules,
      from *Change* to *Take*, and its paragraphs on the six parts and
      the cases, point at the simulation (2026-11-19).
- [x] Each line taken out of the problem file's §2.1 is placed, and
      its commit body says where: already in the simulation, moved
      there, kept elsewhere as not a fact of Change, or dropped as
      superseded by the simulation (2026-11-19).
- [ ] The layers document's §3.2 states only what is its own, where
      each part and depth sits in the picture and the arrows it
      travels, and points at the simulation for the six parts and the
      depths.
- [ ] The movements between the repos are written once, and the
      other place points there.
- [ ] Every Fact Reference to a section this Plan Step moved,
      retitled or cut resolves, across Living Text.

**Known already.** The commit-plan Agent Skill and the three Agent
Rules have no *Gates* section, so nothing is known already. This
Plan Step has only its own items.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `change-home-2026-11-19` follows the
      commit-messages Agent Skill.
- [ ] No commit straddles agent and project paths
      (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
- [ ] The Plan Step's lessons are written back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2.4, *How the Entry File is written*).
- [ ] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md` §3, *Close*).

Notes:
- Opened 2026-11-19, the Change idea's first step (`TODO.md`, the
  item "Define the Change idea").
- The way, decided in talk on 2026-11-19: the simulation is the one
  place until the change flow is done, then everything moves once.
  Rejected:
  - the simulation as the final home: its *Options* and *Today*
    fields are workings, and a comparison with today's kit;
  - the rules moved now to their final home: each rework in the
    change flow would then edit a fact in two places again, and Judge
    to Take are checked against depth a only.
- Found at the opening: at least 4 of the 6 parts in the problem
  file's §2.1 say something older than the simulation: Read, Judge,
  Deliver and Take.
- Stages: the commit plan's (the commit-plan Agent Skill §4, *The
  lifecycle*). The reviewer signs the plan, then each commit.
