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

## Step: Rewrite the visual-comparison manual into the layers  (the commit-messages Agent Skill)    [~]

Goal: every part of the visual-comparison manual,
`docs/conventions/visual-comparison/`, stands at its layer, with the
Agent Skill pair that waits on it alone, and the manual is gone.
Now: stage 1, the Backbone Idea.
Gate:

**At the opening.**

- [x] The Plan Step's branch `visual-comparison-2026-11-27`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-27, cut at `9061f0d8`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-27, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*, and from the commit-messages manual's
      Plan Step; no Approach on Trial drafted (2026-11-27).

**The Plan Step's own items.**

- [ ] Visual comparison is a Backbone Idea,
      `knowledge/backbone-ideas/visual-comparison.md`, with its row in
      §3.1's table of the layers document in keeping knowledge
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*; the map's QUESTION-7). It
      holds the buildable notations under the condition that makes
      them so (decision B), and its opening says which way a repo
      draws is that repo's own (decision C).
- [ ] Visual comparison has a Problem Domain Idea in each Problem
      Domain, keeping knowledge and CBC backend design, each with its
      row in §3.2.1's or §3.2.2's table of the same document. Each
      says its repos hold to plain text that renders with no build
      step (decision B). Keeping knowledge's holds the case of
      2026-09-18 (decision A) and this repo's Mermaid trial; CBC
      backend design's says a Backend Repo picks its own notations,
      and the trial does not reach it (decision C).
- [ ] The Backend Kit's visual-comparison Agent Skill,
      `delivery/container/.claude/skills/visual-comparison/SKILL.md`,
      is the Instruction Text of its Adapted Case at layer 3, with its
      Adapted Understanding Text at
      `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/visual-comparison/understanding.md`.
      The Agent Skill stays where it is until the exchange is
      rewritten, as the commit-messages manual's Plan Step kept its
      own (devlog 2026-11-27, evening, decision C). It points at the
      Maintainer Repo's texts by name, and carries no Foundation Line.
- [ ] Our visual-comparison Agent Skill is our own Adapted Case at
      layer 4, where it is, with its Adapted Understanding Text at
      `.claude/understanding/visual-comparison.md`. It borrows its
      Defined Terms as the defined-terms Agent Rule says, and carries
      no Foundation Line.
- [ ] Each Agent Skill's §4, *What the render has caught*, keeps its
      entries as checks read at the comparison (decision A).
- [ ] Each part the map's §9 lists for the manual has landed, or was
      judged not needed, and the commit that ends it names where.
- [ ] The manual is gone, and every Living Text that named its path,
      sections or name names where each part now stands
      (`knowledge/backbone-ideas/one-home.md` §5, *When a home moves*).

**Known already.** The commit-messages Agent Skill has no *Gates*
section; the own items stand alone.

**At the close.**

- [ ] Every link and path in the records resolves.
- [ ] Every ADR a record cites exists.
- [ ] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill.
- [ ] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text meets `.claude/rules/writing.md`.
- [ ] Every commit on `visual-comparison-2026-11-27` follows the commit-messages Agent Skill.
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

Notes:
- Opened 2026-11-27, the ninth Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the manual needs no text first, and is the smallest left,
  113 lines (the map's §9, by script). The TODO item stays: it is the
  whole rewrite.
- The texts it rewrites, by the map's §9: the manual, and the Agent
  Skill pair that waits on it alone, ours and the Backend Kit's.
- Checked at the opening, by subject against the manual: no Glossary
  Name has its home in the manual; no TODO item of the map's §8 lands
  with it; 8 lines in 4 files of Living Text name its path, by script:
  2 in each Agent Skill, 1 in `ARCHITECTURE.md`, 3 in the map. The
  conventions manual names it among four shared names, without its
  path (`docs/conventions/conventions/` §1.5, *Naming a Work Approach*).
- Decision A, at the opening, on the reviewer's word: the case of
  2026-09-18, two Mermaid dialects that failed only when drawn and a
  table that won, goes to the Problem Domain Idea in keeping
  knowledge: a Backbone Idea gives no example from one Problem
  Domain's work. Each Agent Skill's §4 keeps its entry for the same
  case: a check read at the comparison is instruction, not a second
  home. Moving §4's entries out of the Agent Skills was rejected: the
  agent would lose them at the moment it compares.
- Decision B, at the opening, on the reviewer's word: the Backbone
  Idea holds the manual's §2.4 under its condition: where a repo holds
  to plain text that renders on GitHub and in the IDE with no build
  step, the buildable notations are Mermaid and Unicode box drawing.
  Each Problem Domain Idea says its repos hold to it. Stating §2.4 as
  a flat fact was rejected: it writes one repo's choice into layer 1.
  So was §2.4 whole in each Problem Domain Idea: the condition is
  general.
- Decision C, at the opening, on the reviewer's word: which notations
  a repo uses is its own. This repo's Mermaid trial, provisional and
  not delivered (ADR-0027, decision 3), goes to the Problem Domain
  Idea in keeping knowledge; that a Backend Repo picks its own goes to
  CBC backend design's; the Backbone Idea's opening says each Problem
  Domain Idea says it. Each Agent Skill's §5 keeps its line; the
  Backend Kit's names the Maintainer Repo, not the Concept Deliverer.
- Its stages, from the map:
  1. the Backbone Idea, from the manual's opening, *What it is for*
     without its case, §1 and §2; *What this does not cover* as its
     neighbours (the map's QUESTION-4);
  2. the two Problem Domain Ideas: keeping knowledge's from *What it
     is for*'s case, *The seats* and the Mermaid trial; CBC backend
     design's from *The seats* and the Backend Kit's §5;
  3. the Backend Kit's Adapted Case: its Adapted Understanding Text
     from *Why it arrives this way*; its Agent Skill's pointers and
     header;
  4. our own Adapted Case: `.claude/understanding/visual-comparison.md`,
     and our Agent Skill's Borrow Table and pointers;
  5. the manual goes: the rename grep over its path, sections and
     name;
  6. the close.
