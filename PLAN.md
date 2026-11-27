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

## Step: Shrink the Tiers Model to what waits    [~]

Goal: every part of the Tiers Model, `docs/models/tiers.md`, that has
a home in the layers points there, and what stays says what it waits
for.
Now: stage 4, the close.
Gate:

**At the opening.**

- [x] The Plan Step's branch `tiers-2026-11-27`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-27, cut at `51cfcd51`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-27, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*, and from the Idea-to-Output Model's
      Plan Step; no Approach on Trial drafted (2026-11-27).

**The Plan Step's own items.**

- [x] The Tiers Model does not go: it keeps §2.2, §2.3, §3.1 and §3.3,
      the homes of 7 Glossary Names, and goes when the last of them
      has landed (decision A) (2026-11-27, `8bbb51b3`).
- [x] §2.1 keeps its heading and one line pointing at the layers
      document's open question 1, in keeping knowledge
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §5, *Open questions*). That question holds the rule a second
      Maintainer Repo follows and its trigger, cites ADR-0038, and no
      longer points at §2.1 (decision C) (2026-11-27, `c0a84d76`).
- [x] §3.2 has landed in how an agent works, in CBC backend design,
      §2, *The case nobody watches*, from §3.2's own lines; §3.2 points
      there, that text borrows Told Channel, and the Told Channel's
      glossary entry gives its second meaning that home (decision B)
      (2026-11-27, `8370ca43`).
- [x] §3.4 and §3.5 point at each fact's home in Change, in keeping
      knowledge, Change, in CBC backend design, and the layers
      document in keeping knowledge (2026-11-27, `f3a4c929`).
- [x] §4.1 points at Change §3, *How the layers fill*, and the layers
      of knowledge §3.4, *The layer of work* (2026-11-27, `f3a4c929`).
- [x] §4.2 points at Change, in keeping knowledge §2, *The arrows*,
      and the layers document in keeping knowledge §3, *The layers*
      (decision D) (2026-11-27, `f3a4c929`).
- [x] Each part the map's §9 lists for the model has landed, waits
      with its home named, or was judged not needed, and the commit
      that ends it names where (2026-11-27: §1, §2.1's second
      paragraph and §3.5's story line judged not needed, `f3a4c929`;
      the rest by the items above).
- [x] The model's opening says what it still holds and where each
      part goes, and the map's row for it says the same (2026-11-27,
      `8bbb51b3`; the map's QUESTION-5 corrected too, by decision D).
- [x] No pointer to the model elsewhere changed, and each still
      resolves: a section that leaves keeps its heading (2026-11-27,
      by script: 19 pointers, in 9 files, name 6 sections, each heading standing;
      the 2 that changed, the glossary's Told Channel and question 1,
      moved by decisions B and C).
- [x] A Change Walk over what stands on the model finds no line its
      changes make untrue
      (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md`
      §4, *The Change Walk*) (2026-11-27: 6 lines into §3.5 and 2 into
      §2.1 still hold, in each stage's commit body).

**Known already.** The Plan Step uses no Agent Skill or Agent Rule
with a *Gates* section; the own items stand alone.

**At the close.**

- [x] Every link and path in the records resolves (2026-11-27, by
      script: the 16 paths in lines the branch added exist, and the 13
      sections they name keep those titles).
- [x] Every ADR a record cites exists (2026-11-27, by script).
- [x] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill
      (2026-11-27: no file under `.claude/` or `delivery/` changed).
- [x] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed (2026-11-27, by script: 2
      hits, both in the model's opening, about the rewrite as a whole).
- [x] New and changed text meets `.claude/rules/writing.md`
      (2026-11-27: no title changed; the model writes CBC Run, the
      Glossary Name).
- [x] Every commit on `tiers-2026-11-27` follows the commit-messages Agent Skill.
      Its subjects are counted by script: one up to 70 characters
      passes, and one past 70 is the reviewer's to keep or rewrite
      (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*)
      (2026-11-27, by script: 6 subjects, from `51cfcd51` exclusive to
      `32bc25bd`, longest 49, none past 70).
- [x] No commit straddles agent and project paths
      (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*)
      (2026-11-27, by script: none touches `.claude/` or `CLAUDE.md`).
- [x] The Plan Step's lessons are written back where they came from:
      conventions, the playbook, the concept (2026-11-27: none new;
      two second cases of TODO Ideas, nowhere, on the reviewer's word).
- [x] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`knowledge/backbone-ideas/agent-files.md` §5, *How the Entry File is written*)
      (2026-11-27: its pointer to the model, §2.2, stands; no line
      changes).
- [x] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md` §3, *Close*)
      (2026-11-27: none drafted or used).

Notes:
- Opened 2026-11-27, the eighth Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the model needs no text first, and the exchange and shapes
  manuals wait on it (the map's §9). The TODO item stays: it is the
  whole rewrite.
- Checked at the opening, each part against its home, line by line:
  - held already: the five facts of §3.5, in Change, in keeping
    knowledge §3.5, *Deliver the Kit Update* (a Backend Repo cannot
    see the Maintainer Repo; nothing crosses without the human's
    word; every Kit Copy whole, at one Kit Version) and §3's picture
    (reads, writes nothing there); in the layers document in keeping
    knowledge §1 (the originals stay in the Maintainer Repo); in
    Change, in CBC backend design §2, *Changing a Kit Copy* (a Kit
    Copy changes only when the work shows it does not fit); §3.4's
    Delivery Pin moving at each take, in Change, in keeping knowledge
    §3.6, *Take the Kit Update*, item 4; §4.1's lesson as high as it
    is true, in Change §3, and a text true only for its project, in
    the layers of knowledge §3.4;
  - waits: §2.2 and §2.3, the homes of Concept Repo, Run Repo,
    Concept Garden, Concept Deliverer and CBC Run; §3.1, of CBC Run
    Birth, until birth lands in Change with the Pure Seed (the map's
    QUESTION-7); §3.3, of Record Harvest, until the exchange manual
    is rewritten;
  - judged not needed: §1, the drawing, which the layers document's
    picture in keeping knowledge draws; §2.1's second paragraph, the
    handbook's story, ADR-0038's.
- Decision A, at the opening, on the reviewer's word: the model
  shrinks to what waits, and does not go. 7 Glossary Names have their
  home in it, used across texts not yet rewritten, `CLAUDE.md` among
  them. A section that leaves keeps its heading and one line pointing
  at its new home, as the Idea-to-Output Model's did (devlog
  2026-11-27, evening, the Idea-to-Output Model, decision D).
  Removing it now, the 7 Names moved to the nearest Defined Terms,
  was rejected: those are close to theirs but not the same, and 22
  files of Living Text point at the model.
- Decision B, at the opening, on the reviewer's word: §3.2, a warning
  told by hand to a Backend Repo after its own work missed it, lands
  in how an agent works, in CBC backend design §2: a rule reaching a
  Backend Repo's agent outside its Kit Copies. No layered text held
  it. Keeping it in the model was rejected: its home exists. So was
  Change, in keeping knowledge: a warning told by hand is a channel,
  not a change travelling between the repos.
- Decision C, at the opening, on the reviewer's word: §2.1's rule, a
  second Maintainer Repo copies the parts it needs and a kit is
  weighed only after three have lived (ADR-0038), moves into the
  layers document's open question 1, which pointed at §2.1 for it.
  Leaving it in §2.1 was rejected: the question would rely on a text
  that is going, and §2.1 pointing back would make a circle.
- Decision D, at the opening, on the reviewer's word: §4.2, *The
  dependency rule*, points at Change, in keeping knowledge §2, and
  the layers document in keeping knowledge §3. Read whole, it says
  what crosses between the repos, and that each repo is one kind. The
  map's QUESTION-5 sends it to the layers rules on links, as "which
  text may point at which"; those rules hold nothing it says, and the
  map's row is corrected at stage 3.
- Its stages:
  1. the parts held already: §3.4, §3.5, §4.1 and §4.2 point at their
     homes; §1 and §2.1's second paragraph go, judged not needed;
  2. the parts that land: §2.1's rule in the layers document's
     question 1; §3.2 in how an agent works, in CBC backend design,
     with the Told Channel's glossary entry;
  3. what waits: the model's opening says what it still holds; the
     map's row says the same;
  4. the close, the closing items by script.
