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

**A trial names the close that judges it.** A change to how work is
done, put on trial, names the Plan Step whose close judges it. Its
verdict there is one line: kept, changed or dropped.

**An item given here that does not fit a Plan Step** is struck there, with its
reason. That is a finding about the item, not a Plan Step skipping
work.

---

## Step: Find how what we know stays true  (none: its stages are listed in its Notes)    [~]

Goal: a way to keep what the reviewer and the agent know true, from
one session to the next, is chosen from the problem in the
reviewer's words and from real cases in this repo.
Now: stage 1, the problem, drafted in `temp/knowledge-problem.md`
and polished one insight at a time.
Gate:

**At the opening.**

- [x] The Plan Step's branch `knowledge-2026-11-05` is cut from main
      at `ca5c422`, and nothing of the Plan Step was done on main
      (2026-11-05).
- [x] This Plan Step Gate was written before the work started
      (2026-11-05).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the order set on 2026-11-05 (2026-11-05).

**The Plan Step's own items.**

- [ ] The problem is written in the reviewer's words, purpose first,
      and the reviewer says it is right.
- [ ] Where the same page failed is sorted by cause, with counts,
      from the devlog's "What context was missing" lines and a sample
      of the refinement's findings.
- [ ] At least two real cases are drawn side by side, and it is
      decided whether one fits both, the two stay apart, or one
      general one is drawn.
- [ ] The way chosen is written, set against one home per fact: what
      it keeps true, what it lets go stale, and what one change costs.

**Known already.** No Agent Skill or Agent Rule is used, so nothing is
known already. This Plan Step has only its own items.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `knowledge-2026-11-05` follows
      the commit-messages Agent Skill.
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
- Opened 2026-11-05, when the rebuild in `cbc-concept` stopped for it
  (devlog 2026-11-05, the rebuild frozen; the rebuild stopped). The
  talk behind it: `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what
  we know true*.
- Stages, in order, each taken off this list once done. The order
  changes only when something changes.
  1. The problem, written in the reviewer's words, starting from
     `temp/idea-model-problem.md`: it has the loop between a home and
     its references (§5) and 9 musts with checks (§3), not the
     purpose or the bottom-up direction.
  2. The real-world record: the devlog's 18 "What context was
     missing" lines since October, and the refinement's findings, 485
     in round 3's close read and 385 in its last read. A sample sorted
     by cause: a retelling that drifted, a home that was wrong, or
     something never written.
  3. The real cases: one drawn and defined, as `cbc-concept`'s step
     drawings did one change; a second set beside it, from outside
     this repo, such as a CBC Run, since the problem holds wherever a
     human works with an agent. Whether a general layer is needed at
     all is found here.
- Ideas carried from TODO, noted and not weighed: not everything must
  stay true, since history cannot go stale; check a text when it is
  about to be used, not by a sweep.
- If this repo's rules steer the answers, the reviewer or the agent
  says so when it is felt, and the reviewer decides then; signs set
  in advance were dropped as a check built ahead (2026-11-05).
- The reviewer signs each commit.
- Main takes the branch by fast-forward on the reviewer's word.

---

## Step: Rebuild in cbc-concept, until it stands on its own  (none: each step is chosen when the last is done)    [!] stopped: Find how what we know stays true (devlog 2026-11-05, the rebuild stopped)

Goal: `cbc-concept`, next to this repo, writes and commits by Work
Approaches of its own, built step by step by ADR-0081, and ADR-0081
is judged from what the steps cost.
Now: stopped in wave 2 of the ideas in `cbc-concept`, before the
Conversation Memory idea and the wave's checkpoint; the commit rule
and `CLAUDE.local.md` wait. `cbc-concept` is frozen at `118c6f5`.
Gate:

**At the opening.**

- [x] The Plan Step's branch `rebuild-2026-11-02` is cut from main
      at `f49de77`, and nothing of the Plan Step was done on main
      (2026-11-02).
- [x] This Plan Step Gate was written before the work started: first
      for moving exchange (2026-11-02), rewritten at the re-aim,
      before the rebuild's first step (2026-11-03).
- [x] The Plan Step's Work Approach is known: the steps of the draft
      order (`temp/rebuild-inventory.md` §5, *A draft order*), each
      chosen when the last is done. No Approach on Trial drafted, on
      the reviewer's word: start, and let the work show the next step
      (2026-11-03).

**The Plan Step's own items.**

- [x] `cbc-concept` is a git repo next to this one, with its three
      repo files, and its first commit made (2026-11-03, `72e27e5`).
- [x] It has a writing Work Approach, loaded in every session
      (2026-11-03, `a36675f`).
- [ ] It has a commit Work Approach, and every commit after it
      follows it.
- [ ] Each Work Approach there follows the layering's template
      (`temp/model-example/layers.md`, *The Work Approach*) and stands
      alone: no pointer to this repo.
- [ ] Each rule there is one its work needed when it was written:
      none taken because this repo has it (ADR-0081, decision 4).
- [ ] Each Work Approach rebuilt lists the lessons its texts here
      held, each carried over or dropped (ADR-0081, decision 5).
- [ ] Each step's cost, its rounds of correction and its files, is
      in this repo's devlog.
- [ ] The step after standing on its own is chosen and written down,
      in TODO here or in `cbc-concept`'s own records.
- [ ] ADR-0081 carries its verdict, kept, changed or dropped, from the
      steps' costs (ADR-0081, decision 7).

**Known already.** No Agent Skill or Agent Rule is used, so nothing is
known already. This Plan Step has only its own items.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `rebuild-2026-11-02` follows
      the commit-messages Agent Skill.
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
- Opened 2026-11-02 as "Move exchange to the new layering". Re-aimed
  2026-11-03, before any move, when moving in place proved to be
  another system to keep; ADR-0081 changed with it. Done before the
  re-aim, and kept: exchange counted (`ee8f3b0`), the inventory
  (`d6fe916`, `176a571`), the draft order (`d167535`).
- Steps, from the draft order: git hygiene, writing, commit messages.
  The next is chosen when the last is done. Git hygiene and writing
  are done. Then the work put two things first: `cbc-concept`'s TODO
  with its Conversation Memory, and its ideas, written in waves, one
  likely chain of ideas at a time (its `TODO.md`, the waves item).
  The waves go beyond this Plan Step's goal; on the reviewer's word,
  they are noted in that TODO, not opened as a Plan Step. Wave 1 is
  written and checked. The commit rule waits.
- Stopped 2026-11-05 for "Find how what we know stays true". It
  resumes or closes when that Plan Step ends, by what it finds.
  ADR-0081's verdict waits until then.
- The work is done in `cbc-concept`. This repo holds its plan and
  history until `cbc-concept` has records of its own. The rules of
  this repo govern only its own commits.
- The reviewer signs each commit, in both repos.
- Main takes the branch by fast-forward on the reviewer's word.

---

## Step: Birth CBC Run 6, on full auto  (`.claude/approaches-on-trial/auto-run.md`, `delivery/installs/pure-seed.md`, the Foundation Check)    [!] stopped: Refine this repo against its own rules (devlog 2026-10-29, morning)

Goal: CBC Run 6 is born from this repo at one Delivery Pin on main, with the
reviewer's CBC Run Briefing for `checkout`, CBC Run 6's project, and a CBC Run Hand-off for full auto, ready for
the reviewer to start.
Now: the close: its checks, the auto-run Approach on Trial's note of this use, main
taking the branch.
Gate:

**At the opening.**

- [x] The Plan Step's branch `run-6-birth-2026-10-29` is cut from main
      at `a002002`, and nothing of the Plan Step was done on main
      (2026-10-29).
- [x] This Plan Step Gate was written before the work started (2026-10-29).
- [x] The Plan Step's Work Approach is known: the auto-run Approach on
      Trial, in its second use (2026-10-29).

**The Plan Step's own items.**

- [x] The lessons CBC Run 5 left for the next CBC Run each say keep, change
      or add for CBC Run 6, in its CBC Run Hand-off. CBC Run 5 was read in full
      (`temp/reading-run-5-2026-10-22.md`), so the auto-run Approach on
      Trial's Stage 1 is a light read (2026-10-29, `657d372`).
- [x] CBC Run 6's CBC Run Briefing is the reviewer's: `checkout`, in
      `temp/run-6-briefing.md`, its Responsibility Areas meeting at a
      LAYER-5-INTERACTION question. Larger than CBC Run 5's, on the
      reviewer's word: three Responsibility Areas, 6 to 12 Invariant Slices (2026-10-29,
      `aad9053`).
- [x] The playbook has no line meant for CBC Run 5 only: CBC Run 5's
      CBC Run Reading's WORK-1, taken here from the stopped Plan Step. It now
      names no CBC Run at all (2026-10-29, `7f6e3a8`).
- [x] CBC Run 6's CBC Run Hand-off says what full auto means for it, part by
      part as the auto-run Approach on Trial's Stage 4 lists (2026-10-29, `657d372`).
- [x] What TODO says is due before a CBC Run Birth is settled: the
      exchange-birth Agent Skill waits for the CBC Run Birth after CBC Run 6's (devlog
      2026-10-29, later; 2026-10-29).
- [x] CBC Run 6 is born by `delivery/installs/pure-seed.md` at
      `~/IdeaProjects/cbc-pure-run-6`, its Delivery Pin a commit on main, the
      Pure Seed's own checks all passing (2026-10-29, at `657d372`).
- [x] CBC Run 6's CBC Run Briefing and CBC Run Hand-off sit in its `temp/`, and the
      reviewer starts it with the Pure Seed's prompt, its review lines
      replaced by full auto (2026-10-29, started by the reviewer).
- [x] `ARCHITECTURE.md` §2.5 lists CBC Run 6 (2026-10-29).

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `run-6-birth-2026-10-29` follows
      the commit-messages Agent Skill.
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
- Opened 2026-10-29, from the devlog's entry 2026-10-29, later: the
  reviewer wants CBC Run 6 born now, before CBC Run 5's lessons are all
  taken. The Plan Step for those lessons and the refinement resume
  after this one closes.
- Stages: the auto-run Approach on Trial's six. Stage 1 is answered by CBC Run 5's CBC
  Run Reading. Stage 3 is settled. The CBC Run Briefing is Stage 2's.

---

## Step: Take CBC Run 5's lessons for CBC Run 6  (`.claude/rules/working-a-reading.md`, the commit-plan Agent Skill, the Foundation Check)    [!] stopped: Birth CBC Run 6, on full auto (devlog 2026-10-29, later)

Goal: CBC Run 5's CBC Run Reading has DECISION-1, DECISION-2 and DECISION-5
settled, and WORK-1 and WORK-3 to WORK-10 ended.
Now: decide and work (`.claude/rules/working-a-reading.md`, steps 2
to 8).
Gate:

**At the opening.**

- [x] The Plan Step's branch `run-5-lessons-2026-10-29` is cut from main
      at `3f20857`, and nothing of the Plan Step was done on main
      (2026-10-29).
- [x] This Plan Step Gate was written before the work started (2026-10-29).
- [x] The Plan Step's Work Approach is known: `.claude/rules/working-a-reading.md`
      for the CBC Run Reading's items, the commit-plan Agent Skill for the items marked
      plan, the Foundation Check for each Master Copy changed
      (2026-10-29).

**The Plan Step's own items.**

- [ ] CBC Run 5's CBC Run Reading marks DECISION-1, DECISION-2 and DECISION-5
      settled in place, each with how; one that needed an ADR has
      it, Accepted.
- [x] The Exchange Convention says how an edit the CBC Run never used is judged
      (`docs/conventions/exchange/` §5.2, *A finished copy*),
      as DECISION-1 settled it. The opening named §6.5. §5.2 is where
      the Exchange Convention already speaks of such an edit, and the endings do
      not change (2026-10-29).
- [ ] WORK-1 and WORK-3 to WORK-10 are each marked in the CBC Run Reading
      with its ending, taken, declined or held, and its commit. A
      held one names its trigger and has a TODO line.
- [ ] Each taken edit is in our Master Copy, checked against its
      foundation, its file read whole before the commit
      (`.claude/rules/working-a-reading.md`, step 4). A file both
      Convention Seats hold changed in both.
- [x] The playbook has no line meant for CBC Run 5 only: taken by Birth CBC Run 6,
      on full auto (2026-10-29, `7f6e3a8`).
- [ ] The lessons CBC Run 5 left for the next CBC Run Hand-off sit where
      DECISION-2 placed them.
- [x] The CBC Run Reading's two slips, named in devlog 2026-10-29, are
      fixed in place, as that entry tells (2026-10-29).
- [ ] The CBC Run Reading's other items are untouched, left for the Plan Step
      after the refinement, and the CBC Run Reading stays in `temp/`.

**Known already.** The working-a-reading Agent Rule's *Gates* hold when a CBC Run Reading closes;
this Plan Step does not close it. Its "every work item has ended" is the
third own item, for this Plan Step's items only.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `run-5-lessons-2026-10-29` follows
      the commit-messages Agent Skill.
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
- Opened 2026-10-29, from the devlog's entry of that day: the
  reviewer chose to take what CBC Run 6 needs from CBC Run 5's CBC Run Reading
  before CBC Run 6's CBC Run Birth. The rest of the CBC Run Reading waits for the
  refinement's close. The CBC Run Reading's DECISION-1 was taken in talk: each
  fix judged on its own evidence, with the same three endings.
- Stages: decide and work, by working-a-reading steps 2 to 8. WORK-3,
  WORK-4 and WORK-10 are commit plans of their own. No Delivery Note
  goes to CBC Run 5: it waits for the rest of the CBC Run Reading
  (the exchange-deliver Agent Skill).
- The reviewer decides each decision, and signs each commit at its
  boundary. Main takes the branch by fast-forward on the reviewer's
  word.
