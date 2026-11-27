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
     Why the form is as it is: (records, knowledge/backbone-ideas/records.md
     §4, The plan; and records, in keeping knowledge,
     knowledge/problem-domain-ideas/keeping-knowledge/records-in-keeping-knowledge.md §3). -->

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

## Step: Rewrite the Agent Model into the layers  (the commit-messages Agent Skill; the commit-plan Agent Skill if a Change Set needs it)    [~]

Goal: every part of the Agent Model, `docs/models/agent.md`, stands
at its layer, and the Agent Model is gone.
Now: stage 3, this repo's own Adapted Case.
Gate:

**At the opening.**

- [x] The Plan Step's branch `agent-model-2026-11-27`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-27, cut at `cfa5c336`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-27, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*; no Approach on Trial drafted
      (2026-11-27).

**The Plan Step's own items.**

- [x] How an agent works is a Backbone Idea,
      `knowledge/backbone-ideas/how-an-agent-works.md`, with its row
      in §3.1's table of the layers document in keeping knowledge
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*; the map's QUESTION-7). The row
      says what it holds: how text reaches an agent, and what each way
      guarantees (2026-11-27).
- [x] The Backbone Idea holds the two things every Tool Binding must
      say, from the Agent Model's §10 (the map's QUESTION-6)
      (2026-11-27, its §8).
- [x] What one piece of agent work is stands as an open point, with
      its trigger, beside the rule it would join (2026-11-27, the
      Backbone Idea's §11, question 1).
- [x] How an agent works has a Problem Domain Idea in each Problem
      Domain, keeping knowledge and CBC backend design, each with its
      row in §3.2's table of the same document (2026-11-27).
- [-] ~~How an agent works, in CBC backend design, holds *At the gate*,
      the gate's part of closing one of the Backend Repo's Plan Steps,
      in one section. Its why stands in
      `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md`
      §2, *Changing a Kit Copy*; its steps in
      `temp/common-ground/backend-repo-change-simulation.md` §3,
      *Change a Kit Copy*, step 2.~~ Struck, on the reviewer's word:
      it is how a Backend Repo closes a Plan Step, the playbook's
      subject, and moved to the playbook's row of the map's §9.
- [ ] The Agent Model's §9, *Where each convention lands*, is this
      repo's own Adapted Case at layer 4, at its path by §3.5, or was
      judged not needed.
- [ ] Each part the map's §9 lists for the Agent Model has landed, or
      was judged not needed, and the commit that ends it names where.
- [ ] The Agent Model is gone, and every Living Text that named its
      path or sections names where each part now stands
      (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*).
- [ ] Each Glossary Name the new texts define stays in
      `docs/glossary.md`, pointing at its new home, while a text
      outside the layers model uses it (the map's QUESTION-2).

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
- [ ] Every commit on `agent-model-2026-11-27` follows the commit-messages Agent Skill.
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
- Opened 2026-11-27, the third Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the Agent Model needs no text first, and the
  agent-arrangement manual waits on it, with 4 texts waiting on that
  manual (the map's §9, by script). The TODO item stays: it is the
  whole rewrite.
- TODO's "Rewrite the Agent Model into the layers of knowledge" became
  this Plan Step and left TODO. Its scope, on the reviewer's word:
  the map's row, and *At the gate*. Two of its Ideas wait on the
  agent-arrangement manual's text, so they go with that manual's
  rewrite: `CLAUDE.md` coming in whole, now an Idea of the rewrite
  item; Claude Code's Tool Binding for the Backend Repos and ours,
  now in the map's QUESTION-6.
- Decision A, on the reviewer's word: the Backbone Idea holds what the
  Agent Model holds, how text reaches an agent and what each way
  guarantees. The layers document planned it as "what one piece of
  agent work is"; no text holds that, so it stays an open point,
  written when a second text needs it. TODO's "Check `cbc-concept`"
  waits on it.
- Its stages, from the map:
  1. the Backbone Idea, from §1 to §8, §10's two things, §11 and §12;
  2. the two Problem Domain Ideas, with *At the gate*, struck there;
  3. this repo's own Adapted Case, from §9;
  4. the Agent Model goes: the rename grep, 55 path hits in 21
     files by `git grep`, outside the devlog and the closed ADRs; the
     9 Glossary Names it defines repointed;
  5. the close.
- Open, decided at the stage it meets: what the agent-arrangement
  manual's Foundation Line, `the agent model`, becomes once the Agent
  Model goes. Where §12's evidence lines go was decided at stage 1,
  decision B on the reviewer's word: each where it was seen.
- Their trigger met at this Plan Step's close: TODO's "Write the
  understanding of the agent's memory" and "Decide how work is run by
  agents"; named to the reviewer then.
- Behind it: ADR-0082, decision 2; ADR-0087, decision 4; ADR-0089;
  the map's QUESTION-2, QUESTION-6 and QUESTION-7.
