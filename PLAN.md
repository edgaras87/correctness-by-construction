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
      Its subjects are counted by script: one up to 70 characters
      passes, and one past 70 is the reviewer's to keep or rewrite
      (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*).
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

## Step: Map today's Maintainer Repo for the rewrite  (the commit-messages Agent Skill; the commit-plan Agent Skill if a Change Set needs it)    [~]

Goal: the rewrite has a map of today's Maintainer Repo: each text of
Living Text, the parts it holds, the layer each part goes to, and which
text needs another first; and every TODO item due at the map has ended.
Now: stage 4, the shared questions.
Gate:

**At the opening.**

- [-] The Plan Step's branch `map-2026-11-26`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (skipped 2026-11-26, the reviewer: no branch; the map writes
      only `temp/` and `TODO.md`, nothing ships, and each commit is
      signed; the Plan Step runs on main).
- [x] This Plan Step Gate was written before the work started
      (2026-11-26, in `f83d146b`, the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the inventory of 2026-11-03,
      `temp/rewrite-map.md`, renamed from `temp/rebuild-inventory.md`; no
      Approach on Trial drafted (2026-11-26).

**The Plan Step's own items.**

- [x] The map is a kept file in `temp/`, its header naming the commit
      it was counted at (`temp/README.md`) (2026-11-26,
      `temp/rewrite-map.md`, at `491e673e`).
- [x] Every file of Living Text at that commit has one line on the
      map, checked by script against `git ls-files` (2026-11-26: 171
      files on 161 lines, 10 of them pairs; §9).
- [x] Each text on the map names the parts it holds, and the layer
      each part goes to (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*), or the question that keeps
      it open (2026-11-26, stage 3).
- [x] Each text on the map names the texts it needs rewritten first,
      or none (2026-11-26, stage 3: all 161 lines of §9, with item 3;
      the open parts name QUESTION-1 to 6 in §10).
- [ ] A question many texts share is decided once, on the map, on
      the reviewer's word, and each text it touches points at it.
- [ ] How much of today's repo is rewritten is decided on the
      reviewer's word, from what the map shows.
- [x] Each TODO item whose trigger was the refinement's close has
      ended: put on the map, given a new trigger, or dropped
      (2026-11-26, stage 1: 5 on the map, 8 with new triggers, 3 of
      them merged into one item).
- [x] Each TODO item whose trigger names the map has ended: decided,
      put on the map, or given a new trigger (2026-11-26, stage 1: all
      6 on the map).
- [x] The TODO item on the shared names of five conventions and their
      Agent Skills or Agent Rules has ended the same way (2026-11-26,
      stage 1: dropped, since the rewrite makes a manual and its Agent
      Skill one Adapted Case).
- [ ] Each Idea of the TODO item this Plan Step opened from has ended
      as its Notes weigh it.

**Known already.** The commit-messages and commit-plan Agent Skills
have no *Gates* section; the own items stand alone.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `map-2026-11-26` follows the commit-messages Agent Skill.
      Its subjects are counted by script: one up to 70 characters
      passes, and one past 70 is the reviewer's to keep or rewrite
      (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*).
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
- Opened 2026-11-26, from TODO's item of the same title, its trigger
  "CBC Runs 4, 5 and 6 judged" fired at `bc4faabd`. The reviewer
  stopped evolving the Maintainer Repo that day: the lighter way
  first, and how much is rewritten left to what the map shows.
  Behind it: ADR-0082, decision 2; ADR-0089; devlog 2026-11-23, the
  order before the rewrite.
- What the map starts from, counted by script at `bc4faabd`: 264
  tracked files, 68 of them changed since the inventory's `ee8f3b0`
  (38 added, 26 changed, 3 deleted, 1 renamed). History is not
  mapped: it is never updated (`.claude/rules/one-home.md`, *Not a
  second home*).
- The TODO items due, found by script at `bc4faabd`:
  - 13 whose trigger names the refinement's close, against the 14
    counted on 2026-11-02;
  - 6 whose trigger names the map: the drafts' words of walking
    commits, the problem file's next pass, the CBC Runs' Approaches
    on Trial and check scripts, how much a CBC Run records, our forms
    as Output Shapes, `docs/baselines/` by kind;
  - the shared names of five conventions.
- The TODO item's Ideas, weighed now:
  - the 14 items first: taken, as stage 1.
  - the inventory brought up to date, not started again: taken.
  - which of today's ideas are Backbone Ideas, open question 4 of the
    layers document: taken, as a question the map decides once.
  - how much is rewritten, decided by what the map shows: taken, as
    an own item.
  - a later update to a CBC Run born before names the renames in its
    Delivery Note: put on the map, at the exchange-deliver Agent
    Skill.
  - the lessons in §7 of the three CBC Run Readings: put on the map,
    at working-a-reading and the exchange-read Agent Skill.
- Stages:
  1. the items due: each ends put on the map, with a new trigger, or
     dropped; an item done before the rewrite keeps a TODO line, and
     is not done in this Plan Step;
  2. the inventory brought up to date, at one commit;
  3. each text's parts, their layers, and what each needs first;
  4. the shared questions, decided once, one at a time, with the
     reviewer;
  5. close.
- The reviewer signs each stage's result before the next, and each
  commit.
