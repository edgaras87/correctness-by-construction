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

## Step: Rewrite repo hygiene into the layers  (the commit-messages Agent Skill; the commit-plan Agent Skill if a Change Set needs it)    [~]

Goal: every part of the repo-hygiene manual, and of the texts that
wait on it alone, stands at its layer, and the manual is gone.
Now: stage 6, the close.
Gate:

**At the opening.**

- [x] The Plan Step's branch `hygiene-2026-11-26`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-26, cut at `caa86c58`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-26, in `6da07ad8`, the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*; no Approach on Trial drafted
      (2026-11-26).

**The Plan Step's own items.**

- [x] Repo hygiene is a Backbone Idea, `knowledge/backbone-ideas/repo-hygiene.md`,
      with its row in §3.1's table of the layers document in keeping
      knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*; the map's QUESTION-7)
      (2026-11-26).
- [x] Repo hygiene has a Problem Domain Idea in each Problem Domain,
      keeping knowledge and CBC backend design, each with its row in
      §3.2's table of the same document (2026-11-26).
- [x] The Backend Kit holds repo hygiene as an Adapted Case at layer 3,
      at its path by §3.5: the Hygiene Base and the Stack Overlay are
      its Instruction Text, and its why is its Adapted Understanding
      Text (the map's QUESTION-4, *Why it arrives this way*)
      (2026-11-26).
- [x] This repo's three files are its own Adapted Case at layer 4
      (§3.4, *The layer of a repo's work*): the files at its root, and
      an Adapted Understanding Text in `.claude/understanding/` only
      if they have a why of their own (2026-11-26, its why in
      `.claude/understanding/repo-hygiene.md`, `2262166b`).
- [x] Each part the map's §9 lists for the manual has landed, or was
      judged not needed, and the commit that ends it names where
      (2026-11-26, the commit that deletes the manual).
- [x] The manual and its `templates/` directory are gone, and every
      Living Text that named their paths or sections names the new
      home (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*)
      (2026-11-26).
- [-] The Glossary Names Hygiene Base and Stack Overlay are retired by
      the map's QUESTION-2: each a Defined Term at its new home, its
      lines gone from `docs/glossary.md` and from the container's
      delivered Glossary Names
      (struck 2026-11-26, the reviewer: six texts outside the layers
      model still use them, among them the cbc-bootstrap Agent Skill a
      CBC Run reads; they retire when the last of these is rewritten,
      as QUESTION-2 says of the glossary. Each is a Defined Term at its
      new home, and `docs/glossary.md` points there).

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
- [ ] Every commit on `hygiene-2026-11-26` follows the commit-messages Agent Skill.
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
- Opened 2026-11-26, the first Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the repo-hygiene manual needs no text first, and 7 texts
  wait on it (the map's §9, counted by grep). The TODO item stays: it
  is the whole rewrite, and this is one text of it. The lighter way
  first, by the reviewer's word of that day (devlog 2026-11-26, the
  Maintainer Repo stops evolving).
- The texts it rewrites, by the map's §9: the manual; the three pairs
  `.gitignore`, `.gitattributes` and `.editorconfig`, ours and
  `delivery/container/`'s; the three `.part` files of the Java and
  Spring Stack Overlay. `delivery/installs/pure-seed.md` also waits
  on the exchange manual, so it stays; its paths are fixed by the
  rename grep.
- Its stages, from the map:
  1. the Backbone Idea, from the manual's *What it is for* and §1 to §3;
  2. the two Problem Domain Ideas;
  3. the Backend Kit's Adapted Case, with the Stack Overlay;
  4. this repo's own Adapted Case;
  5. the manual goes: the rename grep, the Glossary Names retired;
  6. the close.
- Held, not this Plan Step's: TODO's "Decide whether the cbc-bootstrap
  Agent Skill points at the Spring Stack Overlay", its trigger the
  cbc-bootstrap Agent Skill's hygiene step rewritten. CBC Run 4's
  FINDING-38, CBC Run 5's FINDING-40 and CBC Run 6's FINDING-26, each
  a `.gitignore` written by hand, wait there. Its Context names the
  templates' path, which the rename grep fixes.
- Behind it: ADR-0082, decision 2; ADR-0089; the map's QUESTION-2,
  QUESTION-4 and QUESTION-7.
