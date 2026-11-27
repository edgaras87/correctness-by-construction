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
      (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*).
- [ ] No commit straddles agent and project paths
      (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*).
- [ ] The Plan Step's lessons are written back where they came from:
      conventions, the playbook, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`knowledge/backbone-ideas/agent-files.md` §5, *How the Entry File is written*).
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

## Step: Shrink the Idea-to-Output Model to what waits    [~]

Goal: every part of the Idea-to-Output Model,
`docs/models/idea-to-output.md`, whose home stands has landed there,
or was judged not needed; the model keeps only the parts whose home
is not yet written, and each names where it goes.
Now: stage 5, the close.
Gate:

**At the opening.**

- [x] The Plan Step's branch `idea-to-output-2026-11-27`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-27, cut at `01baebb3`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-27, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*; no Approach on Trial drafted
      (2026-11-27).

**The Plan Step's own items.**

- [x] The layers document,
      `knowledge/backbone-ideas/layers-of-knowledge.md`, holds which
      way a link points, the model's §3.2, and the 3 pointers to §3.2
      name it
      (2026-11-27, `71f49c34` and `92bf0bc6`).
- [x] §4, *The two directions*, has left the model, and the 5
      pointers to §4.2 name Change,
      `knowledge/backbone-ideas/change.md`
      (2026-11-27, `5b833e0d` and `4d4c0436`: 4 name Change; the 5th, the conventions manual's line 122, names the model's §3.1, the one text that holds its claim, on the reviewer's word at stage 2).
- [x] §1's count of manuals, §4.2's history, §7 and §8 are gone, each
      judged not needed in the commit that removes it
      (2026-11-27, §4.2's history in `5b833e0d`, the rest in `984534da`).
- [x] The model's header says what it still holds, and where each
      part goes: §1 to §3.1, the home of 5 Glossary Names, until the
      texts that use them are rewritten; §3.3 to the one-home idea;
      §5 to CBC design; §6 to the idea of how instructions are written
      for an agent; Output Shape and *governs* to the shapes manual
      (2026-11-27, `357b973a`).
- [x] The map's row for the model says the same
      (2026-11-27, `357b973a`).
- [x] The facts-in-sync manual can be rewritten next: what its §4
      relies on stands in the layers model, or in what the model
      still holds
      (2026-11-27, by grep: its §4 points only at the model's §2, which stays; the rest of the manual at §2, §3.1 and §3.3, which stay too).

**Known already.** The Plan Step uses no Agent Skill or Agent Rule
with a *Gates* section; the own items stand alone.

**At the close.**

- [x] Every link and path in the records resolves
      (2026-11-27, by script: 29 pointers in the Plan Step's added lines, none broken).
- [x] Every ADR a record cites exists
      (2026-11-27, by script: none missing in the 5 touched texts that cite one).
- [x] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill
      (2026-11-27, no paired copy touched: none of the 3 agent files has a delivered copy).
- [x] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed
      (2026-11-27, by script: only homes still unwritten, and content).
- [x] New and changed text meets `.claude/rules/writing.md`
      (2026-11-27, read at each stage; the 5 Glossary Names corrected in `357b973a`).
- [x] Every commit on `idea-to-output-2026-11-27` follows the commit-messages Agent Skill.
      Its subjects are counted by script: one up to 70 characters
      passes, and one past 70 is the reviewer's to keep or rewrite
      (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*)
      (2026-11-27, by script: 8 subjects to `357b973a`, the longest 51, none past 70).
- [x] No commit straddles agent and project paths
      (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*)
      (2026-11-27, by script: none).
- [x] The Plan Step's lessons are written back where they came from:
      conventions, the playbook, the concept
      (2026-11-27, one lesson as an Idea of TODO's "Rewrite today's Maintainer Repo into the layers model, by the map", in this commit).
- [x] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`knowledge/backbone-ideas/agent-files.md` §5, *How the Entry File is written*)
      (2026-11-27: no line names the model, each passes).
- [x] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md` §3, *Close*)
      (2026-11-27, none drafted or used: two had a pointer moved).

Notes:
- Opened 2026-11-27, the sixth Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the model needs no text first, and the facts-in-sync
  manual waits on it, with 4 texts waiting on that manual (the map's
  §9, by script). The TODO item stays: it is the whole rewrite.
- Checked at the opening, by subject against the model: the chain and
  the two directions are held, in the layers document §3 and Change
  §3 and §4; which way a link points is held by no text under
  `knowledge/`, by grep; settling a disagreement, §5 and §6 have homes
  not yet written (the map's QUESTION-5 and QUESTION-7).
- Decision A, at the opening, on the reviewer's word: the model does
  not go in this Plan Step. It keeps the parts whose home is not yet
  written, and goes when the last of them lands (ADR-0082, decision 2).
  Writing those homes now, or turning to the commit-plan manual first,
  was rejected.
- Decision B, at the opening, on the reviewer's word: §1, §2 and §3.1
  stay, though the layers document holds their idea. They are the
  home of 5 Glossary Names, Idea Model, Work Approach, Output Form,
  Output Shape and Chain Link, and texts not yet rewritten
  use them, such as the Foundation Check.
- Its stages, from the map:
  1. which way a link points, into the layers document, with the
     Change Walk on what stands on it; the 3 pointers to §3.2, in the
     facts-in-sync manual, `.claude/rules/convention-manual.md` and
     the model-placing Approach on Trial;
  2. §4 goes; the 5 pointers to §4.2, in the conventions manual
     twice, `TODO.md`, the approach-evaluation and model-placing
     Approaches on Trial; the pointers on the agent side in an agent
     follower;
  3. the parts judged not needed go;
  4. the model's header and the map's row;
  5. the close.
- Pointers counted by script on 2026-11-27, over 11 files of Living
  Text outside history, a pointer wrapped across two lines included.
