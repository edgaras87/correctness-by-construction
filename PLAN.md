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

## Step: Rewrite the agent-arrangement manual into the layers  (the commit-messages Agent Skill; the commit-plan Agent Skill if a Change Set needs it)    [~]

Goal: every part of the agent-arrangement manual,
`docs/conventions/agent-arrangement/`, stands at its layer, with the
three texts that wait on it alone, and the manual is gone.
Now: stage 2, the two Problem Domain Ideas.
Gate:

**At the opening.**

- [x] The Plan Step's branch `agent-arrangement-2026-11-27`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-27, cut at `d9ef9969`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-27, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*; no Approach on Trial drafted
      (2026-11-27).

**The Plan Step's own items.**

- [x] Agent files is a Backbone Idea,
      `knowledge/backbone-ideas/agent-files.md`, with its row in
      §3.1's table of the layers document in keeping knowledge
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*; the map's QUESTION-7)
      (2026-11-27, stage 1).
- [ ] Agent files has a Problem Domain Idea in each Problem
      Domain, keeping knowledge and CBC backend design, each with its
      row in §3.2's table of the same document.
- [ ] Claude Code's Tool Binding, the manual's §5, stands as two
      Adapted Cases: the Backend Kit's at layer 3 and ours at layer 4,
      each at its path by §3.5 (the map's QUESTION-6).
- [ ] The Backend Kit's Entry File and its Decisions Log's Record Stub,
      today `delivery/container/.claude/CLAUDE.md` and
      `delivery/container/.claude/decisions.md`, are its Adapted Cases
      at layer 3, at their paths by §3.5; the Pure Seed copies them
      from there (the map's QUESTION-1).
- [ ] Our `CLAUDE.md` comes in whole as our own Adapted Case at layer
      4, its Local Rule among its lines; our `.claude/decisions.md`
      header is our Decisions Log's form at layer 4, where it is; each
      has an Adapted Understanding Text in `.claude/understanding/`
      for a why of that file alone.
- [ ] Each part the map's §9 lists for the manual has landed, or was
      judged not needed, and the commit that ends it names where. A
      part whose subject is how instructions are written for an agent
      is named in the map's QUESTION-5, for that idea.
- [ ] The manual is gone, and every Living Text that named its path or
      sections names where each part now stands
      (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*).
- [x] Each Defined Term a text in the layers model borrows from the
      manual, Agent Skill, Agent Rule and Paths Rule, has its home in
      the layers model, and each borrow points at it
      (2026-11-27, stage 1: `dc00764e`; 17 borrows repointed in
      `9aa0f28f` and `4006d64d`).
- [ ] Each Glossary Name whose home is the manual stays in
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
- [ ] Every commit on `agent-arrangement-2026-11-27` follows the commit-messages Agent Skill.
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
- Opened 2026-11-27, the fourth Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the manual needed only the Agent Model, gone in the last
  Plan Step, and 4 texts wait on it, more than on the retrospective
  manual, 2, or the visual-comparison manual, 1 (the map's §9, by
  script). The TODO item stays: it is the whole rewrite.
- The texts it rewrites, by the map's §9: the manual, and the three
  that wait on it alone: `CLAUDE.md`; `delivery/container/.claude/CLAUDE.md`;
  the Decisions Log's form, ours and the Backend Kit's. Not this Plan
  Step's: the commit-messages manual, an idea of its own; its
  pointers into this manual are fixed by the rename grep.
- The rewrite item's Idea "`CLAUDE.md` comes in whole with the
  agent-arrangement manual, its Local Rule among its lines: no
  understanding text for one line before the rest" became this Plan
  Step's item and left TODO.
- Decision A, at the opening, on the reviewer's word: the arrangement
  is an idea of its own, at layer 1, since both Problem Domains work
  by it (the map's QUESTION-7, whose list does not name it). It is
  not a part of how an agent works: that idea says how text reaches
  an agent; this one says which files a repo keeps for it, and what
  goes in each.
- Decision B, at stage 1, on the reviewer's word: the idea is named
  Agent files, `knowledge/backbone-ideas/agent-files.md`, a plain
  phrase the commit-messages and commit-plan manuals already use.
- Decision C, at stage 1, on the reviewer's word: Agent Skill, Agent
  Rule and Paths Rule are defined at layer 1, in Agent files, in
  words no tool owns; their paths go to the Tool Bindings, and the
  Backend Kit's Defined Terms keep Claude Code's words, their home
  repointed. By the same reasoning, Local Rule and Decisions Log are
  defined there too.
- Decision D, at stage 1, on the reviewer's word: the folder of
  Approaches on Trial is listed in plain words, with no Defined Term,
  until the idea of trying a new way of working defines one (the
  map's QUESTION-7).
- Its stages, from the map:
  1. the Backbone Idea, from the manual's opening, *What it is for*
     and §1 to §4;
  2. the two Problem Domain Ideas, with each seat's evidence;
  3. the Backend Kit's Adapted Cases: its Entry File, its Decisions
     Log's Record Stub, and Claude Code's Tool Binding for the Backend
     Repos;
  4. our own Adapted Cases: `CLAUDE.md` in whole, our Decisions Log's
     form, and our Tool Binding;
  5. the manual goes: the rename grep, 71 path hits in 32 files by
     `git grep` at `d9ef9969`, outside the devlog and `docs/adr/`; 5 Glossary Names
     repointed, Agent Rule, Agent Skill, Local Rule, Paths Rule and
     Decisions Log;
  6. the close.
- Open, decided at the stage it meets: the folder of the Backend
  Kit's Adapted Cases at layer 3; how the two Tool Bindings stay
  alike where the tool's facts are the same.
- Their trigger met at this Plan Step's close: TODO's "Write the
  understanding of the agent's memory", "Decide how work is run by
  agents" and "Read the frozen CLAUDE template's stance bullets
  against a full CBC Run's derived Entry File"; named to the reviewer
  then.
- Behind it: ADR-0082, decision 2; ADR-0087, decision 4; ADR-0089;
  the map's QUESTION-1, QUESTION-2, QUESTION-4, QUESTION-5,
  QUESTION-6 and QUESTION-7.
