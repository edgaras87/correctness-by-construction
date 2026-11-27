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

## Step: Rewrite the facts-in-sync manual into the layers    [~]

Goal: every part of the facts-in-sync manual,
`docs/conventions/facts-in-sync/`, stands at its layer, with the
three Agent Rules that wait on it, and the manual is gone.
Now: stage 6, the close.
Gate:

**At the opening.**

- [x] The Plan Step's branch `facts-in-sync-2026-11-27`, if it has one, is cut
      from main, and nothing of the Plan Step was done on main
      (`.claude/rules/working-a-reading.md`, step 1)
      (2026-11-27, cut at `7a844ad4`, before the opening commit).
- [x] This Plan Step Gate was written before the work started
      (2026-11-27, in the Plan Step's opening commit).
- [x] The Plan Step's Work Approach is known: the stages its Notes
      list, from the map, `temp/rewrite-map.md` §9, *Every text*, and
      §10, *Shared questions*; no Approach on Trial drafted
      (2026-11-27).

**The Plan Step's own items.**

- [x] One home is a Backbone Idea, `knowledge/backbone-ideas/one-home.md`,
      with its row in §3.1's table of the layers document in keeping
      knowledge
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
      §3.5, *Where each layer is kept*; the map's QUESTION-7). It
      holds settling a disagreement
      (2026-11-27, `ad7ede7f`).
- [x] The Idea-to-Output Model's §3.3, *Settling a disagreement*, has
      landed in the Backbone Idea; its heading stays, with one line
      pointing there, and the model's header and the map's row for it
      say so (2026-11-27, `ad7ede7f`).
- [x] One home has a Problem Domain Idea in each Problem Domain,
      keeping knowledge and CBC backend design, each with its row in
      §3.2's table of the same document. The one in keeping knowledge
      holds how a Fact Reference is written here, numbering a
      section's parts (decision D), and the Change Walk
      (2026-11-27, `dd8ca7fa`, `e74fd88f`).
- [x] The Backend Kit's one-home Agent Rule,
      `delivery/container/.claude/rules/one-home.md`, is the
      Instruction Text of its Adapted Case at layer 3, with its
      Adapted Understanding Text at
      `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/one-home/understanding.md`.
      The rule stays where it is until the exchange is rewritten, as
      the commit-messages Agent Skill did (devlog 2026-11-27, evening,
      the commit-messages manual, decision C)
      (2026-11-27, `89034a00`).
- [x] Our one-home Agent Rule and our Foundation Check are two
      Adapted Cases at layer 4, each with its Adapted Understanding
      Text in `.claude/understanding/`. The Foundation Check's steps
      stand as they work today, but for their pointers (decision B)
      (2026-11-27, `e0624cf7`).
- [x] TODO's "Simulate depth c, then bring the Change idea to it"
      holds an Idea: what replaces the Foundation Check in the layers
      model (decision B) (2026-11-27, `132d6189`).
- [x] Living Text and Fact Reference are Defined Terms of the Backbone
      Idea, Change Walk of the Problem Domain Idea in keeping
      knowledge, and Foundation Check of its Adapted Understanding
      Text. Each one's glossary entry points at its new home, and
      Canonical Description's at the Idea-to-Output Model's §2, *The
      kinds* (decision C) (2026-11-27, `ad7ede7f`, `dd8ca7fa`,
      `e0624cf7`, `f7a7d9f2`).
- [x] The 3 Foundation Lines that name `the facts-in-sync convention`,
      in the three Agent Rules, are gone: each rule's understanding is
      written beside it (`docs/conventions/conventions/` §1.3, *The
      Foundation Line*) (2026-11-27, `89034a00`, `e0624cf7`).
- [x] Each part the map's §9 lists for the manual has landed, or was
      judged not needed, and the commit that ends it names where
      (2026-11-27, `f7a7d9f2`).
- [x] The manual is gone, and every Living Text that named its path or
      sections names where each part now stands
      (`knowledge/backbone-ideas/one-home.md` §5, *When a home moves*)
      (2026-11-27, `f7a7d9f2`, `cd56b211`; 0 Fact References to it
      left in Living Text, by grep).

**Known already.** The Plan Step uses no Agent Skill or Agent Rule
with a *Gates* section; the own items stand alone.

**At the close.**

- [x] Every link and path in the records resolves (2026-11-27, by
      script against `7a844ad4`: the one path the branch added that is
      missing is this Plan Step's own mention of the deleted manual).
- [x] Every ADR a record cites exists (2026-11-27, by script).
- [x] Each pair of copies agrees, such as the worked example in the
      cbc-framing Agent Skill and in the cbc-slice Agent Skill
      (2026-11-27: nothing under `delivery/method/` changed).
- [x] No line of Living Text in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed (2026-11-27: 15 added
      lines use the words, by script, and none claims so).
- [x] New and changed text meets `.claude/rules/writing.md`
      (2026-11-27: one title past 30 characters, shortened in
      `d7132ed9`).
- [x] Every commit on `facts-in-sync-2026-11-27` follows the commit-messages Agent Skill.
      Its subjects are counted by script: one up to 70 characters
      passes, and one past 70 is the reviewer's to keep or rewrite
      (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*)
      (2026-11-27: 16 subjects by script, from `7a844ad4` exclusive to
      `3e3f7bbc`, longest 58, none past 70).
- [x] No commit straddles agent and project paths
      (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*)
      (2026-11-27, by script).
- [x] The Plan Step's lessons are written back where they came from:
      conventions, the playbook, the concept (2026-11-27: one, held as
      an Idea of TODO's rewrite item, since no convention changes
      before the rewrite, ADR-0089; `3e3f7bbc`).
- [x] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`knowledge/backbone-ideas/agent-files.md` §5, *How the Entry File is written*)
      (2026-11-27: no line names what the Plan Step changed).
- [x] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md` §3, *Close*)
      (2026-11-27, none drafted or used: two had pointers moved).

Notes:
- Opened 2026-11-27, the seventh Plan Step of TODO's "Rewrite today's
  Maintainer Repo into the layers model, by the map", chosen by the
  reviewer: the manual needed only the Idea-to-Output Model's §4,
  which landed in the last Plan Step, and 4 texts wait on it, against
  2 on the Tiers Model and 1 on the commit-plan manual (the map's §9,
  by script). The TODO item stays: it is the whole rewrite.
- The texts it rewrites, by the map's §9: the manual; our one-home
  Agent Rule and the Backend Kit's; our Foundation Check. Not this
  Plan Step's: the Foundation Line's own details, at home in the
  conventions manual's §1.3, which the manual only retells; TODO's
  "Decide how texts are checked to stay true after the rewrite",
  whose trigger is the rewrite done (the map's QUESTION-7).
- Checked at the opening, by rule against the manual:
  - layer 1: the opening, *What it is for* in general, §1, §2 in
    general, what a Fact Reference is, the rename grep in general,
    where a decision is cited by its reader, §4's rule in general,
    and §5;
  - layer 2, keeping knowledge: the handbook's evidence, how a Fact
    Reference is written here, §3.2, the commit plan's sweep, the
    Change Walk's greps, each new line asked at the commit, where a
    disagreement is raised, and a finding declined only for not
    being general;
  - layer 2, CBC backend design: CBC Run 3's four records, ids as
    Fact References written bare, and a shipped line standing alone;
  - layers 3 and 4: each seat, and its half of *Why it arrives this
    way*;
  - the manual's own sections: by QUESTION-4;
  - judged not needed: that the concept's meaning changed once since
    v1, history's.
- The three earlier drafts the map names for this manual are first
  sources of the Backbone Idea, read for ideas:
  `temp/model-example/idea/one-home.md`,
  `temp/model-example/this-repo/one-home.md` and
  `temp/model-example/approaches/change-a-home.md`. Three of their
  ideas the manual does not hold: the limits of one home, the ways
  rejected, and three ways out when a pointer no longer holds. Each
  is taken or left at stage 1, on the reviewer's word.
- Decision A, at the opening, on the reviewer's word: the Backbone
  Idea is called One home, as the map's QUESTION-7 and the
  Idea-to-Output Model's header name it, and as both one-home Agent
  Rules are; a disagreement is one fact stated twice. "Facts in sync"
  was rejected: a figure of speech, against writing rule 5.
- Decision B, at the opening, on the reviewer's word: the Foundation
  Check is not redesigned. Its step 3 is today's form of Change's
  survey for this repo's own change to a text others stand on
  (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
  §3.4, *Act on the verdicts*), and depth c, never simulated, decides
  what replaces it. It becomes a light Adapted Case of its own, its
  steps as they work. Dropping it was rejected: since 2026-11-26, 84
  of 88 commit bodies name it, by script, and the rewrite changes
  upper texts at nearly every step. Leaving it untouched was
  rejected: its Foundation Line and 9 of its lines name the manual.
  So was one Adapted Case for both our rules: writing a line and
  staging a commit are two pieces of agent work
  (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
  §3.3, *The Adapted Case layer*).
- Decision C, at the opening, on the reviewer's word: each Glossary
  Name whose home is the manual becomes a Defined Term at its new
  home, by the map's QUESTION-2, but Canonical Description. It
  becomes none: the Backbone Idea says its rule in the layers' own
  words, a text others stand on and what stands on it, and its
  glossary entry retires with the glossary. Defining it in the
  Backbone Idea was rejected: a second word beside the layers'
  Understanding Text.
- Decision D, at the opening, on the reviewer's word: §3.2,
  *Numbering a section's parts*, goes to one home, in keeping
  knowledge, beside how a Fact Reference is written: a reference
  names the number, and only this repo writes references by path,
  section and title. The writing manual was rejected: it is not yet
  rewritten, and the part would move twice.
- Decision E, at stage 1, on the reviewer's word: the Backbone Idea
  takes all three of the drafts' ideas the manual does not hold. The
  ways rejected go to §2, the three ways out to §8, and the limits to
  §9. The third limit is reworded: "copy" became two places each
  holding a fact of their own, since a copy with no owner is a second
  home. The drafts' list of what each project decides is left to the
  Problem Domain Ideas. `ad7ede7f`'s body calls it decision 5.
- Decision F, at stage 2, on the reviewer's word: the manual's "a
  finding is declined only for not being general" is held already.
  Change, in keeping knowledge, §3.3 lists the verdicts, "its own"
  and "held" among them, and one home's §8 says neither side is right
  for being upper. Restating it in keeping knowledge was rejected: a
  second home for Change's verdicts.
- Decision G, at stage 2, on the reviewer's word: a Backend Kit
  file points at a Maintainer Repo text by the text's name, "kept in
  the Maintainer Repo", then its section, the form the rewritten Kit
  files already use. The manual's "the Concept Deliverer's" was
  rejected: a twin of Maintainer Repo (`.claude/rules/defined-terms.md`,
  rule 2). Its 22 lines under `delivery/` stay until their files are
  rewritten.
- Decision H, at stage 2, on the reviewer's word: Change Walk keeps
  its name. Fact Change was rejected: it names the change, not the
  re-read, and sits beside Copy Change as if the same kind. Reliance
  Check was rejected: a twin beside Change Walk in 49 lines of 20
  files, by script, until they are rewritten.
- Decision I, at stage 2, on the reviewer's word: a case stays in a
  Problem Domain Idea only where a text relies on it. CBC Run 3's
  stays in CBC backend design's, for the Backend Kit's understanding
  text, which may name no project. The handbook's leaves keeping
  knowledge's: its home is agent files, in keeping knowledge §2, and
  no text of one home relies on it (`e74fd88f`).
- Stage 4 grew, on the reviewer's word: with their understanding in
  `.claude/understanding/`, both our rules came under the
  defined-terms Agent Rule. Each gained a Borrow Table, and its twins
  gave way to Defined Terms or plain words: rule 2's example was
  replaced, and the Foundation Check's "Idea Model" became "a model
  under `docs/models/`", since Backbone Idea would be false of those
  files. The gate had planned pointers alone (`e0624cf7`).
- At stage 5, on the reviewer's word, two parts no stage had placed
  were judged: the concept's list of what stands on it is held by
  `ARCHITECTURE.md` §2, which says it itself; the edges of ADR-0039
  and ADR-0003 are those decisions', and need no new text
  (`f7a7d9f2`).
- Its stages, from the map:
  1. the Backbone Idea, from the manual's layer-1 parts, the
     Idea-to-Output Model's §3.3 and the three drafts; the model's
     §3.3 points at it;
  2. the two Problem Domain Ideas, from the manual's layer-2 parts;
  3. the Backend Kit's Adapted Case: its Adapted Understanding Text
     from *The CBC Run's seat* and *Why it arrives this way*; the
     shipped rule's header points at it, and its Foundation Line
     goes;
  4. our two Adapted Cases: their Adapted Understanding Texts from
     *The Concept Deliverer's seat* and *Why it arrives this way*;
     both Foundation Lines go; the depth c Idea;
  5. the manual goes: the rename grep, 74 lines in 19 files that
     name facts-in-sync outside history, the drafts and the map, by
     script on 2026-11-27; the glossary entries;
  6. the close.
