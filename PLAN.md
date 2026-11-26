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

## Step: Read and judge CBC Runs 4, 5 and 6  (the exchange-read Agent Skill; the exchange-reading and working-a-reading Agent Rules)    [~]

Goal: CBC Runs 4, 5 and 6 each have a CBC Run Reading by today's
exchange, and every item of the three has ended taken, declined or
held, kept for the rewrite.
Now: stage 4, decide and work, the three together.
Gate:

**At the opening.**

- [ ] The Plan Step's branch `runs-judged-2026-11-26`, if it has one,
      is cut from main after the reads, and nothing of the Plan Step
      was done on main except the reads
      (`.claude/rules/working-a-reading.md`, step 1).
- [x] This Plan Step Gate was written before the work started
      (2026-11-26, in `c7ef5580`, the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the exchange-read Agent
      Skill, for each read; the exchange-reading and working-a-reading
      Agent Rules, for each CBC Run Reading and its judging; the
      commit-plan Agent Skill, if the count calls for a branch
      (2026-11-26).

**The Plan Step's own items.**

- [x] CBC Run 6 has a CBC Run Reading in `temp/`, its first line
      naming the commit read through (2026-11-26, `67210ae1`,
      through `00fc075`).
- [x] CBC Run 4 has a CBC Run Reading in `temp/`, its first line
      naming the commit read through (2026-11-26, `2d81febc`,
      through `7637a79`).
- [-] CBC Run 5's CBC Run Reading reads in today's words, and each of
      its open items says whether today's texts already meet it
      (struck 2026-11-26: the reviewer chose to read CBC Run 5 again
      from its first commit, so the two items below replace it).
- [x] CBC Run 5's old CBC Run Reading, of 2026-10-22, is closed as
      overtaken: each open item says where it went, and the file is
      deleted (`docs/conventions/exchange/` §6.4, *How a CBC Run
      Reading closes*) (2026-11-26, `4a44c206` and `23744f02`).
- [x] CBC Run 5 has a new CBC Run Reading in `temp/`, its first line
      naming the commit read through (2026-11-26, `3f12fb5f`,
      through `80099b1`).
- [ ] Each edit, CBC Run Ask and finding of CBC Runs 4, 5 and 6 has
      one line in its CBC Run Reading.
- [ ] CBC Run 4's own questions and CBC Run 6's, listed in the Notes,
      each have a line in their CBC Run Reading.
- [ ] The three CBC Run Readings were judged together: a finding seen
      in more than one names each CBC Run it came from, and is judged
      once.
- [ ] Every finding has ended in a decision or a work item, or says
      why it needs neither.
- [ ] Every work item has ended taken, declined or held, and is
      marked in its CBC Run Reading.
- [ ] Each taken item names the text it lands with in the rewrite. No
      Master Copy changed and no Delivery Note was sent (ADR-0089,
      decision 3).
- [ ] Each held item has its line in TODO.
- [ ] Nothing in CBC Runs 4, 5 and 6 was written to.
- [ ] Each CBC Run's uncommitted work, if any, is named in its CBC Run
      Reading.
- [ ] The three CBC Run Readings stay in `temp/`, each header saying
      it is kept for the rewrite.
- [ ] `temp/RUN-4.md` is read, then deleted.

**Known already.** The exchange-read Agent Skill's *Gates* and
working-a-reading's *Gates*, checked against the own items by meaning:

- the CBC Run Reading to its form, its first line naming `HEAD`: in
  the first two items;
- every edit, CBC Run Ask and finding with one line, none decided at
  the read; the uncommitted work named; nothing written to the CBC
  Run: each joined as an item;
- every finding ended, every work item ended and marked: each joined
  as an item;
- the Delivery Note in the CBC Run: struck, since none is sent until
  the rewrite (ADR-0089, decision 3);
- the CBC Run Reading's lessons where they act, or in TODO: in the
  close's lessons item.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `runs-judged-2026-11-26` follows the
      commit-messages Agent Skill. Its subjects are counted by script:
      one up to 70 characters passes, and one past 70 is the
      reviewer's to keep or rewrite
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
  the rewrite about to begin. The reviewer stopped evolving the
  Maintainer Repo that day, to get back to the projects
  (`d7ace896`). Read and judged by today's exchange, and no Agent
  Skill of the layers model used (ADR-0089).
- The three CBC Runs:
  - CBC Run 6: unread; 233 commits on main, 34 branches, tag
    `v0.1.0`, born from our pin `657d372`. Its read starts from the
    hand-off, `temp/run-6-handoff/`.
  - CBC Run 4: unread; 158 commits, 42 branches, born by hand from
    CBC Run 3's kit at `dac4dd1`; 12 lines under *To the deliverer*.
  - CBC Run 5: read on 2026-10-22 through `80099b1`,
    `temp/reading-run-5-2026-10-22.md`, in git at `4a44c206`, its judging half done; no
    commit since, its tree clean. Its open DECISION-2 and
    DECISION-5, and WORK-1 and WORK-3 to WORK-10, are among the
    findings.
- The TODO item's Ideas, weighed now:
  - CBC Run 6 first, then CBC Run 4: taken. CBC Run 6 used the newest
    kit, so its findings are nearest today's texts.
  - each read with today's conventions: taken (ADR-0089).
  - read by needs, not by diff: declined for the read, which is the
    exchange-read Agent Skill's (ADR-0089, decision 1). Extended to
    the judging: an item whose need is gone ends declined, saying why.
  - CBC Run 5's Reading not read again: declined, 2026-11-26, the
    reviewer. CBC Run 5 is read again from its first commit. Its old
    Reading closes first, as overtaken, since the exchange-read Agent
    Skill extends a CBC Run Reading still open in `temp/`. Git keeps
    the old one, to compare.
  - judged by working-a-reading: taken (ADR-0089).
  - old words read through the refinement's Names table, at
    `55e2bd0^:temp/refinement-2026-10-18.md`: taken.
  - CBC Run 4's own questions: taken. CBC Run 3's and CBC Run 4's
    `RETRO.md` against the retrospective Agent Skill's form
    (ADR-0054); how it closed its Plan Step branches; whether its
    birth fired three triggers, shipping `temp/`, the
    ground-must-be-up rule, the cbc-bootstrap Agent Skill's hygiene;
    its "rules in force now" list on an append-only Decisions Log;
    the cbc-framing Agent Skill's README status line; whether it
    confirmed its Plan Steps once framed.
  - CBC Run 6's own questions: taken. Whether CBC Run 5's and CBC Run
    6's Entry Files added the ground-must-be-up rule unasked
    (ADR-0013).
  - a later update to a CBC Run born before names the renames in its
    Delivery Note, once: moved to TODO's map item, since no Delivery
    Note is sent here.
- Stages:
  1. read CBC Run 6 (the exchange-read Agent Skill);
  2. read CBC Run 4 (the same);
  3. close CBC Run 5's old CBC Run Reading as overtaken, then read
     CBC Run 5 again (the exchange-read Agent Skill);
  4. decide and work, the three together (working-a-reading, steps
     1 to 8), on the branch if the count calls for one;
  5. close (working-a-reading, step 9, without the Delivery Note).
- The reviewer signs each CBC Run Reading before the next stage, and
  each commit.
- Behind it: ADR-0082, decision 4; ADR-0089; devlog 2026-10-29,
  morning; `f097695`; `TODO-CONVERSATION-MEMORY.md` §5, *Run 4's
  reading: two moves from layer 6*, and §30, *Reading a CBC Run born
  before*.
