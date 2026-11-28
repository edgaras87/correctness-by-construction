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

## Step: Rewrite the commit-plan manual into the layers  (the commit-messages Agent Skill)    [~]

Goal: every part of the commit-plan manual,
`docs/conventions/commit-plan/`, stands at its layer, with the Agent
Skill pair that waits on it, and the manual is gone; the plan file is
no agent file, the work it plans is named "Commit Set", and a second
way is tried before a choice, not looked for after the work.
Now: stage 1, the Backbone Idea.
Gate:

**At the opening.**

- [x] The Plan Step's branch `commit-plan-2026-11-28`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-28, cut at `69f618a8`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-28, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*, and from the visual-comparison manual's
      Plan Step; no Approach on Trial drafted (2026-11-28).

**The Plan Step's own items.**

- [ ] Commit sets is a Backbone Idea,
      `knowledge/backbone-ideas/commit-sets.md`, with its row in
      §3.1's table of the layers document in keeping knowledge
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*; the map's QUESTION-7). It
      defines "Commit Set" (decision D), says the plan file is no
      agent file (decision A), and holds the try before a choice
      (decision B).
- [ ] Commit sets has a Problem Domain Idea in each Problem Domain,
      keeping knowledge and CBC backend design, each with its row in
      §3.2.1's or §3.2.2's table of the same document, each holding
      what its own repos lived and do, and no rule of its own
      (decision C).
- [ ] The Backend Kit's commit-plan Agent Skill,
      `delivery/container/.claude/skills/commit-plan/SKILL.md`, is the
      Instruction Text of its Adapted Case at layer 3, with its
      Adapted Understanding Text at
      `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/commit-plan/understanding.md`.
      The Agent Skill stays where it is until the exchange is
      rewritten, as the visual-comparison manual's Plan Step kept its
      own. It points at the Maintainer Repo's texts by name, and
      carries no Foundation Line.
- [ ] Our commit-plan Agent Skill is our own Adapted Case at layer 4,
      where it is, with its Adapted Understanding Text at
      `.claude/understanding/commit-plan.md`. It borrows its Defined
      Terms as the defined-terms Agent Rule says, and carries no
      Foundation Line.
- [ ] In both commit-plan Agent Skills and both commit-messages Agent
      Skills, ours and the Backend Kit's, a commit of the plan file is
      plain `docs`, the plan file is not listed with the agent's
      files, and no rule makes a plan beside a TODO line or an ADR two
      commits (decision A).
- [ ] Both commit-plan Agent Skills name a second way worth trying at
      a boundary, tried on a `try/` branch on the human's word; their
      look back regroups the commits and no more. TODO's "Decide
      whether a commit plan's look-back also asks if the work could
      have been done better" has left TODO, its verdict in the commit
      that removes it (decision B).
- [ ] Every text this Plan Step writes or changes names "Commit Set",
      never "Change Set"; the glossary's "Change Set" points at its
      new home until no text outside the layers model uses it (the
      map's QUESTION-2; decision D).
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
- [ ] Every commit on `commit-plan-2026-11-28` follows the commit-messages Agent Skill.
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
- Opened 2026-11-28, the tenth Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the manual needs no text first, and is the smallest left,
  194 lines (the map's §9). The TODO item stays: it is the whole
  rewrite.
- The texts it rewrites, by the map's §9: the manual, and the Agent
  Skill pair that waits on it, ours and the Backend Kit's. Read for
  ideas, as the map's §9 says: `temp/model-example/idea/commit-set.md`
  and `temp/model-example/this-repo/committing.md`, an earlier try,
  input and not rules.
- Checked at the opening, by subject against the manual: the
  Glossary Name "Change Set" has its home in the manual's §1; no TODO
  item of the map's §8 lands with it; 26 lines in 13 files of Living
  Text name its path or name, by script, history and
  `temp/model-example/` left out.
- Decision A, at the opening, on the reviewer's word: the plan file,
  `COMMIT-PLAN.md`, is no agent file. It is the trail of one piece of
  work, as a commit message is, and tells the agent nothing of how to
  work. The manual's §2.9 had called it one from a lesson of
  2026-11-02, which gave no reason but the `docs(agent)` scope; agent
  files' list, closed, has no row for it
  (`knowledge/backbone-ideas/agent-files.md` §3, *The agent files*).
  Adding the row was rejected.
- Decision B, at the opening, on the reviewer's word: TODO's
  look-back item comes due, since this Plan Step changes the Agent
  Skill's rules. The look back at the way after the work is declined:
  CBC Runs 5 and 6 tried it, 13 lines and 0 tries, and 12 times
  nothing. The try before a choice is kept: CBC Run 4's 14 tries on
  `try/` branches changed 2 answers. The agent names a second way
  worth trying at a boundary, beside the diff, and tries it on the
  human's word.
- Decision C, at the opening, on the reviewer's word: each Problem
  Domain Idea holds what its own repos lived and do. Keeping
  knowledge's: the handbook's scratch file, 118 commit plans opened
  since 2026-08-27 by script, one revised four times on 2026-09-27
  and 28. CBC backend design's: where a Backend Repo opens one, at
  birth (`delivery/installs/pure-seed.md`) and when it applies a
  retrospective (the apply-retrospective Agent Skill, Stage 2); CBC
  Run 3's SL-3 plan split by a revision; CBC Runs 4 to 6 as decision
  B. How a full-auto run treats its plan is left out: no source says.
- Decision D, at the opening, on the reviewer's word: the work a
  commit plan plans is named "Commit Set", not "Change Set". It says
  what it is made of, commits, and fits work that adds, deletes or
  tries as well as work that changes. "Change" already names how
  knowledge moves in the layers model, and in Mercurial and
  Subversion a changeset is one commit. The plan, its file and the
  commit-plan Agent Skill keep their names. The Change idea's own
  title waits for TODO's depth c item (`69f618a8`).
- Decision E, at stage 2, on the reviewer's word: a Plan Step whose
  stages each land as one commit or a few needs no Commit Plan, its
  stages already listing its commits; a stage of many commits opens
  one. Its subject is the Plan Step, so records holds it
  (`knowledge/backbone-ideas/records.md` §4, *The plan*), and commit
  sets says only that no Commit Plan is opened where a Plan Step's
  stages list the commits. It holds in both Problem Domains, so it
  goes to layer 1, once: the rewrite's Plan Steps since 2026-11-26
  opened no Commit Plan, and CBC Run 4's framing, skeleton and slices
  ran as Plan Steps with small commits, a Commit Plan only for its
  retrospective. Writing it into each Problem Domain Idea was
  rejected: two copies of one rule
  (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The
  Problem Domain layer*). Putting it in commit sets was rejected: its
  subject is the Plan Step.
- Decision F, at stage 2, on the reviewer's word: a Commit Set's list
  of commits is named "Commit Plan", a Defined Term of commit sets,
  and commit sets never says a bare "plan" for it. "The plan" stays
  records' name for the record of Plan Steps, since the Commit Plan
  carries its own subject. The record's own subject waits for TODO's
  item on its name.
- Decision G, at stage 2, on the reviewer's word: commit sets names
  no Plan Step. The idea that uses it points at it: records says its
  stages list a Plan Step's commits, and holds the rule that a Plan
  Step Gate item closed inside a Commit Set names its commit. Commit
  sets says only that no Commit Plan is opened where a record agreed
  before the work lists the commits one by one, and calls its parts
  commits, never steps.
- Decided before the opening, on the reviewer's word: the stop at
  every commit stays (`knowledge/backbone-ideas/commit-messages.md`
  §5, *Commit on the word*); at a stop the reviewer finds what they
  want. Whether it costs the agent better solutions waits on TODO's
  "Rerun a finished Plan Step on full auto" (`ca431339`).
- Its stages, from the map:
  1. the Backbone Idea, from the manual's opening, *What it is for*
     without its lived history, §1 and §2.1 to §2.12; *What this does
     not cover* as its neighbours (the map's QUESTION-4); decisions
     A, B and D;
  2. the two Problem Domain Ideas, from *What it is for*'s lived
     history and the Backend Kit's own texts (decision C);
  3. the Backend Kit's Adapted Case: its Adapted Understanding Text
     from *Why it arrives this way*; its commit-plan Agent Skill's
     header, pointers and decisions A, B and D; its commit-messages
     Agent Skill's lines on the plan file; the delivered container
     glossary's entry;
  4. our own Adapted Case: `.claude/understanding/commit-plan.md`,
     and our commit-plan Agent Skill's Borrow Table, pointers and
     decisions A, B and D; our commit-messages Agent Skill's line on
     the plan file;
  5. the manual goes: the rename grep over its path, sections and
     name, and over "Change Set";
  6. the close.
