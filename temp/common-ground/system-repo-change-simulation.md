# A System Repo's Change, Simulated

<!-- A draft of the knowledge work (ADR-0082). It simulates the cases
     of a System Repo's Change, step by step. It is the one home of
     the facts of Change until the change flow is done: the six
     parts, their rules and the cases. A part's rules are its steps'
     *Chosen* and *Adapted Case* fields. Then they move to their
     final home, written out as rules, and this file points there
     (TODO.md, the item "Define the Change idea"). Its input: the
     frozen temp/common-ground/between-repos-simulation.md, §5.2, *Work in a System
     Repo*, and §5.3, *Reading a System Repo*. It goes once what it
     holds has landed in the rewrite into the layers model, and git
     keeps every version. -->

This document simulates the cases of a System Repo's change (§2), step by step. It holds the facts of Change until the change flow is done, and its steps' *Chosen* and *Adapted Case* fields are the rules (§1). One case is simulated through every step: a System Repo changes one Adapted Case, and the System Kit takes the Change: its Adapted Case changes (depth b, §5). The other cases are checked against it (§2). It uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*).

Ten Defined Terms are shortened here to their last word or words. The short forms belong to this file only; the problem file keeps the full Defined Terms.

| Short form | Defined Term |
|---|---|
| Change | System Kit Copy Change |
| Record | System Kit Copy Change Record |
| Copy | System Kit Copy |
| Attention Note | System Kit Attention Note |
| Update | System Kit Update |
| Update Note | System Kit Update Note |
| Take | System Kit Update Take |
| Version | System Kit Version |
| Reading | System Repo Reading |
| Register | Maintainer Repo Register |

The scope of that case: a Change may touch the Adapted Understanding Text, an Instruction Text built on it, or both, in either order. Its reason may be the System Repo's own, or one any repo would meet. A stretch of work may hold several Changes (§2). No fixed example is used: each step's choice must hold at each end of this scope.

## 1. How it is worked

Three moves, in order:

1. **Simulate:** each step below says what must happen, what could be done, and what is chosen.
2. **Read the rules together:** once all of a part's steps are seen together, their *Chosen* and *Adapted Case* fields are read as one: they are the part's rules. They are written out as rules only when they move to their final home (the header comment).
3. **Check them:** each step is walked again against the rules. A step a rule does not hold for changes the rule or the step.

The steps make six parts, each done by one repo:

| Part | Who | Steps |
|---|---|---|
| Change | System Repo | §3, steps 1–2 |
| Read | Maintainer Repo | §4, steps 1–4 |
| Judge | Maintainer Repo | §5, steps 1–2 |
| Act on the verdicts | Maintainer Repo | §6, step 1 |
| Deliver | Maintainer Repo | §7, steps 1–2 |
| Take | System Repo | §8, step 1 |

Each step has these fields. A field with nothing in it is left out.

- **What must happen:** the outcome, and who acts.
- **Options:** what could be done here, today's way among them.
- **Chosen:** the option taken, and why the others were not.
- **Adapted Case:** which Adapted Case runs the step, whose it is, what loads it, and what it must say for this step. Once a part is done, these are read together: they give the rules, and later the Adapted Case texts.
- **Open:** what the step leaves undecided, each with the trigger that decides it.
- **Today:** what is borrowed from today, and what changes, each with its source. Today's things keep today's names, such as the Delivery Note.

## 2. The cases

The cases are simulated one at a time. The first is simulated whole; each other case is then checked against it, and what differs is written. A case that grows too complex goes to TODO, to be checked once the Common Ground Problem is finished. The cases are of two kinds:

- **What was changed:** these vary how the System Repo records its Change, and how the Maintainer Repo finds it. They are the same however deep the Change turns out to go, since that is known only once it is judged.
- **How deep it goes:** these vary how the Maintainer Repo decides, and how the Update is written.

| Kind | Case | Status | Differs so far |
|---|---|---|---|
| what changed | one Adapted Case, any of its texts | being simulated, §3 to §8 | — |
| what changed | a Defined Term | not yet checked | — |
| what changed | delivered Knowledge on Trial | not yet checked | read: compared like any Copy; decided: the original was never proven, so the Change is evidence for its trial |
| what changed | one reason behind Changes to several Adapted Cases | not yet checked | recorded: one why, naming every Copy it changed; read: the Changes are listed together |
| how deep | b. the System Kit's Adapted Case changes: layer 3 | being simulated, §5 to §8 | — |
| how deep | c, at layer 2. the idea above changes: its Work Domain Idea | not yet checked | the other Adapted Cases of that Work Domain Idea are surveyed, the Maintainer Repo's own only when they share it (§6, step 1) |
| how deep | c, at layer 1. the idea above changes: its Backbone Idea | not yet checked | every Work Domain Idea on that Backbone Idea is surveyed; how far down the survey reaches is open (§6, step 1) |
| how deep | d. the idea above already holds it: layer 3, or layer 2 | not yet checked | the loss sits at layer 2 when the Work Domain Idea lost a part its Backbone Idea holds: the Work Domain Idea is fixed from its Backbone Idea, then the Adapted Case from the Work Domain Idea. Which other texts are checked for the same loss is open (§5, step 1) |
| how deep | e. it asks to narrow the idea above: layer 3, or layer 2 | not yet checked | the narrowing goes into the text just below the idea that does not fit, marked with its why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*): the Adapted Case, or the Work Domain Idea when a part of its Backbone Idea does not fit its whole Work Domain. How that is known is open (§6, step 1) |
| how deep | f. several Adapted Cases need it, but not all: no layer | not yet checked | it cannot enter the idea above. When it holds for every Adapted Case of one Work Domain, it is depth c, at layer 2. Two cases are left: several Adapted Cases of one Work Domain, but not all; and Adapted Cases across Work Domains, but not all (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 1). Each Adapted Case gains it, and the same text has no shared home. Open; its trigger: the first change two Adapted Cases need, but not every one |

How deep a Change goes is how high it goes: each depth names the highest layer it changes, since a lesson goes as high as it is true (`temp/common-ground/knowledge-layers-general.md` §3.1, *How the layers fill*). The idea above is the Work Domain Idea an Adapted Case is written from, or the Backbone Idea that one is adapted from.

A stretch of work may hold several Changes, alike or mixed. Each is recorded and read on its own, so they add no row but one: one reason behind Changes to several Adapted Cases.

New text of the System Repo's own, on trial, is not a case here. It comes from no Copy, so it is not a Change. It is Knowledge on Trial, handed over at the System Repo's close (`temp/common-ground/knowledge-layers.md` §2.3, *The Adapted Case layer*). It is one of the other sources (below).

**Known, not ruled.** These can happen, and have no rules here until practice meets them. Rules once written for them are in git. Each says what can happen, and its trigger:

- **an Attention Note:** a System Repo has something for the Maintainer Repo that no Change carries: a misfit worked around with no Change made, a doubt about a line left as it is, something the System Kit lacked, a Copy no longer used. Its trigger: the first such thing a System Repo needs to tell.
- **a Change the System Kit does not take:** judged its own, depth a, the Change staying in the System Repo at layer 4; or unsound, misread or held. It stays only in the System Repo's Copy, and the Take takes every Copy whole. Whether the Copy keeps it past the Take is not ruled. Case D1 comes back with it (§4, step 1, *A look at main*). Its trigger: the first such verdict.

**Other sources.** A Change is one source of the Common Ground Problem. Others exist: a birth, a lesson found in the Maintainer Repo's own work, Knowledge on Trial a System Repo hands over at its close, and new knowledge from the human. They are left on purpose until Change is finished (`TODO.md`, the item on resuming the simulation).

**Change whole.** The six parts of §1 and the depths of the table above, in one picture. It is a summary: the sections it names hold the facts.

```
 System Repo  ┆ Maintainer Repo
 ───────────  ┆ ───────────────
              ┆
 1. Change ───┼── reads; writes nothing there ──▶ 2. Read ──▶ 3. Judge ──▶ 4. Act on the verdicts
    §3        ┆                                      §4          §5           §6
              ┆                                                               │
 6. Take ◀────┼── writes only into its temp/ ──── 5. Deliver ◀────────────────┘
    §8        ┆                                      §7

 How high each depth goes: 3. Judge sets it, 4. Act on the verdicts changes it

 depth                          b        c, at 2   c, at 1   d         e         f
                                         └─────────── not yet checked ────────────┘
 layer 1  Backbone Idea                            ●
 layer 2  Work Domain Idea               ●         ●         ○         ○
 layer 3  Adapted Case          ●        ●         ●         ●         ●
 layer 4  a System Repo's work  ●        ●         ●         ●         ●         ●
 ───────────────────────────────────────────────────────────────────────────────────────────
 highest layer                  3        2         1         3, or 2   3, or 2   none, open
 5. Deliver brings down         Update   Update    Update    Update    Update    Update
```

Key: ● is the Change's path, from its Copy up to the highest layer it changes. ○ is "or up to here", when the case asks it (the table above, rows d and e). The last row follows the layers document's arrows (`temp/common-ground/knowledge-layers.md` §3.2, *How a Change moves*). A § is a section of this document.

## 3. Change

Two steps:

1. A Copy is changed, with its Record.
2. The Plan Step's gate decides each Change.

**Step 1. A Copy is changed, with its Record.**

- **What must happen:** during its own work, the System Repo finds that a Copy does not fit what happened. The human decides the Change, the agent proposing. It is made then, and its Record is written with it. The Change may be edited or reversed later, its Record with it.
- **Options:**
  - a. the Copy is changed when the work shows it does not fit, and its Record written with it;
  - b. the Copy is changed ahead, for what the agent foresees;
  - c. the misfit is noted, and the Copy changed at the Plan Step's gate;
  - d. the Copy stays as it is, and the System Repo writes what it does instead in its own records.
- **Chosen:** a. The others:
  - b is a speculation, with nothing that happened behind it;
  - c gains nothing by waiting. A Record lets any Change be edited or reversed later. And until the gate, the Copy would say what the System Repo no longer does;
  - d leaves the Copy saying it for good, and the next agent reads the Copy, not the System Repo's records.

  **Where it sits.** The Record goes in a footer of the Copy's Adapted Understanding Text, which is not loaded for work. So the Change and its why land in one diff, and the why cannot lose its Copy. When only an Instruction Text changes, its Record goes there too.

  **What it holds:**
  - what changed, by meaning: the part, and what it says now. When some of the Adapted Case's texts were left as they were, it also says whether they still match the Change (Failure Case 8);
  - what happened, concretely, in the System Repo's own words. It is never written to sound general: rewording it is the Maintainer Repo's, after judging;
  - which work found it;
  - the System Repo's proposal: its own problem, or one any repo would meet. It is marked as a proposal. The Maintainer Repo judges every Change, and says whether it agrees, and why if not (§5).

  **When it is rewritten.** The Record says the Change as it stands. A later edit rewrites it, and git keeps the old one.

  **The commit.** The Change and its Record go in the same commit. A commit that changes a Copy and not its Record is stopped there. A Take is not a Change, so the check lets its commits pass: one replaces every Copy with the System Kit's and clears every Record. What the System Repo puts back at the Take is a Change, and carries a fresh Record (§8, step 1). Every Change that lasts passes through a commit. Work never committed is lost, the Change and its Record together.

  **Weighed and dropped:** a check at each session's end, comparing the Copies with their Records. It would run every session, needs an Adapted Case of its own, and never runs when a session stops with no warning. The commit's check and the gate's comparison (step 2) cover what it would find. It comes back if a gate finds a Change committed in an earlier session with its Record missing or wrong.
- **Adapted Case:** the System Repo's, for changing a Copy, itself a Copy. It loads when a Copy is touched. For this step it says:
  - a Copy changes only when the work shows it does not fit, never ahead;
  - the Record is written with the Change, with its four parts, and goes in the same commit;
  - the Record sits in a footer of the Copy's Adapted Understanding Text, and says the Change as it stands: a later edit rewrites it;
  - a commit that changes a Copy and not its Record is stopped. A Take is not a Change, and passes;
  - what happened is written concretely, in the System Repo's own words;
  - whether the Change is its own or any repo's is a proposal, never a verdict.
- **Today:**
  - borrowed: an edit comes from something that happened, never a speculation (`delivery/container/.claude/rules/delivered-copies.md`, rule 2; `docs/conventions/exchange/` §5.1, *When a copy may be edited*);
  - borrowed: the rule for changing a copy loads when a copy is touched (`delivery/container/.claude/rules/delivered-copies.md`, its `paths:`);
  - borrowed: the Record names which work found the Change, as a Decisions Log entry names its Plan Step (`delivery/container/.claude/rules/delivered-copies.md`, rule 2);
  - changed: today d is required when the need is the CBC Run's own: "never this CBC Run's own answer", and what only it needs goes in its records (`docs/conventions/exchange/` §5.1). So today forbids an edit for the System Repo's own reason. Here the System Repo makes it; what becomes of it at the Take is not ruled (§2, *Known, not ruled*);
  - changed: today nothing is written into a copy but the edit, since "a file says how to use it, never its own history", and the why goes in the Decisions Log (`docs/conventions/exchange/` §5.1). Here the why goes in the Copy's Adapted Understanding Text, which is not read while working;
  - changed: today every edit must claim to be for any CBC Run. Here the System Repo proposes, and the Maintainer Repo judges;
  - borrowed: a check fires at the commit because, before, it had to be remembered (`.claude/rules/foundation-check.md`, its header comment). That one is the Maintainer Repo's own.

**Step 2. The Plan Step's gate decides each Change.**

- **What must happen:** at the Plan Step's close, the step's Changes are seen together, now that the whole step is seen. The agent compares the Copies against where the Plan Step began, and shows each with its Record. The human decides each, the agent proposing: kept, edited, or reversed, its Record with it. Changes that share one reason are linked.
- **Options:**
  - a. the gate looks at the step's Changes together: the comparison, a decision on each, and the links;
  - b. the gate only checks that each Change has a Record that says it, and decides nothing;
  - c. the gate does nothing with Copies: the Maintainer Repo reviews the Changes when it reads them;
  - d. the gate writes one line per changed Copy, asking the Maintainer Repo to read it.
- **Chosen:** a. The others:
  - b keeps a Change made early in the step, though the end of the step may show it wrong, and leaves Changes with one reason unlinked;
  - c leaves the review to the side that cannot see what happened, and a wrong Change then reaches the Maintainer Repo's judging;
  - d adds nothing to the Records: a Reading compares every Copy, and reads the Records. It comes back if a Reading misses a changed Copy because nothing asked it to look.

  **After the decision.** A Change kept as it is needs nothing more. One edited gets its Record rewritten. When Changes share one reason, the reason is written in full in one Record, and each other one says how its own Copy was affected and points at that one. If the one holding the reason is reversed, the reason moves to one that stays, and the others point there.
- **Adapted Case:** the System Repo's, for closing a Plan Step, its gate list. It loads when the Plan Step closes. For this step it says:
  - compare the Copies against where the Plan Step began, and check each Change has a Record that says it;
  - the human decides each Change: kept, edited or reversed, its Record with it;
  - Changes with one reason are linked, and the reason never stays only in a reversed Record.
- **Open:** whether a reversed Change leaves a trace for the Maintainer Repo. One tried and undone may be evidence that the Copy was right. Its trigger: the first Change reversed at a gate.
- **Today:**
  - borrowed: the gate is a list of outcomes checked at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: each Approach on Trial the Plan Step used has its dated note at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). A Record checked at the gate is the same shape;
  - changed: today the close writes one CBC Run Ask per edited copy (`delivery/container/.claude/rules/delivered-copies.md`, rule 4), option d. Here the Records are what a Reading reads;
  - changed: today nothing at the close looks at the step's changes to copies together.

## 4. Read

Four steps:

1. The stretch of work ends, and the Maintainer Repo is told.
2. The Maintainer Repo finds the two snapshots it compares.
3. It compares the Copies, and reads each Record.
4. It lists what changed, nothing judged.

**Snapshots.** A Reading compares two snapshots of the System Repo, and never walks its commits. The *settled snapshot* is the one already taken into account: read, judged and acted on (`temp/common-ground/common-ground-problem.md`, *Defined Terms*). It holds the Version the System Repo had recorded by then (§8, step 1, *At the Take, in order*, item 5), which may be behind the newest. So the last Version the Maintainer Repo has seen the System Repo on is read from it, never stored anywhere else. Main's latest snapshot is the one checked, and becomes the Reading's stop. The commits between them are history, opened only to understand something deeper. The clean copy a Take leaves is the one special point, used only after a Take (step 2, *After a Take*).

**Step 1. The stretch of work ends, and the Maintainer Repo is told.**

- **What must happen:** a stretch of work ends where reading can stop, and the Maintainer Repo learns that the System Repo has work it has not read. The human decides which System Repo is read, and when.
- **Options,** for where a stretch ends:
  - a. at any commit, the System Repo's latest;
  - b. at a closed Plan Step's gate, the last one on main.
- **Options,** for how the Maintainer Repo learns:
  - c. the human tells it, and its Register is marked by hand;
  - d. the human names a System Repo, and the agent compares its main with where its last Reading stopped. Every System Repo is compared when the human asks what to read;
  - e. only when work resumes in the System Repo, by the fixed order: reading back, judging, then the Update.
- **Chosen:** b and d. The others:
  - a reads Changes the gate has not yet looked at, which the System Repo may still edit or reverse (§3, step 2);
  - c depends on the human remembering, and the Register then says a System Repo was read when it has new work (Failure Case 2);
  - e alone never reads a System Repo whose work does not resume, so what it learned is lost (Failure Case 1). It stands as it is, for every System Repo (§8, step 1, *Before the Take*), and d adds Readings between two resumptions of work.

  **Where a stretch ends.** Main moves only at a gate's close, so main is always at a closed gate, and nothing on it waits for a gate. Work past it, in a branch or not yet committed, is left for the next Reading.

  **A look at main.** d is a look at one System Repo. It makes two checks, both on whether there is something to read:
  1. **main moved:** the System Repo's main against the *settled snapshot*;
  2. **Changes:** the Copies, compared between the older snapshot and main (step 2, step 3).

  Whether an Update is due is Deliver's check, asked after Act at every look, since a verdict to send down exists only once the Changes are judged (§7, step 1, *When one is due*).

  With Deliver's check, a look ends in one of five cases. A and B differ only by its answer, as C1 and C2 do: nothing follows, or an Update follows. D has one case here, D2. Only a Change judged its own, with its proposal holding, leaves nothing to send after acting, and that case, D1, is not ruled (§2, *Known, not ruled*).

  | Case | Main moved | Copy changed | Update due, Deliver's check | What follows |
  |---|---|---|---|---|
  | A | no | — | no | nothing |
  | B | no | — | yes | an Update is made and delivered (§7) |
  | C1 | yes | no | no | Read's list is empty: nothing is judged, and Act sets the *settled snapshot* to main (§6, step 1) |
  | C2 | yes | no | yes | Read's list is empty: nothing is judged, and Act sets the *settled snapshot* to main (§6, step 1); an Update is made and delivered (§7) |
  | D2 | yes | yes | yes, after acting | the full Reading: listed, judged and acted on; an Update is made and delivered (§7) |

  Each column is one check's answer, the last Deliver's. Check 2 is asked only when main moved, so A and B show "—". An Update is due when the Version is behind the newest, or a verdict waits to go down.

  A Plan Step open in the System Repo changes no case: main stands at the last gate, so the look finds its case by what main holds. The open step's work waits for the next look, and an Update waits for the step's gate (§7, step 2, *Before staging*).

  An Update already waiting changes no case: the System Repo has not taken it, so its Version is still behind, Deliver's check finds an Update due, and the new one replaces the waiting one (§7, step 1, *One at a time*).

  **No state kept.** d keeps no state of its own: whether a System Repo has work comes from its main and the *settled snapshot*, never from a line someone must keep true.

  **Cleaned history.** If a stretch's history is cleaned before main moves, the Records are unharmed: they are in the Copies, not in the commits.
- **Adapted Case:**
  - the System Repo's gate list: main moves only at a gate's close. It is there today;
  - the Maintainer Repo's, for reading a System Repo. It loads when the human names a System Repo to read, or asks what to read. For this step it says:
    - compare the named System Repo's main with where its last Reading stopped, or every System Repo's when asked;
    - make the look's two checks; with Deliver's check after Act, the look ends in one of cases A, B, C1, C2 and D2.
- **Open:** a System Repo nobody names is not read until its work resumes. Its trigger: the first lesson found late because a System Repo went unread.
- **Today:**
  - borrowed: a Plan Step reaches main by fast-forward at its close, on the reviewer's word (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: the Maintainer Repo keeps where each System Repo lives (`ARCHITECTURE.md` §2.5, *The CBC Runs*);
  - changed: today the state of the list of CBC Runs, such as "through Release, not yet read", is written by hand (`ARCHITECTURE.md` §2.5). Here it is found by comparison when asked;
  - changed: today a CBC Run Reading runs to the CBC Run's `HEAD`, and names work not yet committed (`.claude/skills/exchange-read/SKILL.md`, Stages 2 and 3). Here it runs to main, and work past it waits.

**Step 2. The Maintainer Repo finds the two snapshots it compares.**

- **What must happen:** the agent finds the older snapshot, and writes the newer one, the stop, before reading anything. A later Reading's older snapshot must be where this one stopped, whether an Update follows this Reading or not, or the clean copy of a Take since.
- **Options,** for where the last Reading's stop is kept:
  - a. in the System Repo, carried there by the next Update;
  - b. in the Register, the *settled snapshot*'s commit beside where each System Repo lives;
  - c. in the Maintainer Repo, as the first line of each Reading, every Reading kept.
- **Chosen:** b. The others:
  - a fails when a Reading has no Update after it, which step 1 allows, since a Reading may come between two resumptions of work: the System Repo still holds the old stop, and the next Reading finds again what was read;
  - c keeps every Reading for good, only for its first line.

  **Where it starts.** The older snapshot is the Register's *settled snapshot*, and it is never empty. At birth, the Maintainer Repo's check of the delivery writes the System Repo's row, with the *settled snapshot* set to the start, the commit holding the Copies as they arrived (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Nothing before the start is the System Repo's own Change, so it stands as read. So every Reading, the first among them, starts at the *settled snapshot*, and a System Repo never read needs no rule of its own. The frozen birth scenario gains this when it resumes (`TODO.md`, the item on resuming the simulation).

  **Where it stops.** The stop is the System Repo's main, its latest snapshot, written first at every look, before anything is read: as the open Reading's first line, or, when nothing is found and no draft is written, handed on with the empty list. So a commit landing during the look falls into the next one.

  **After a Take.** When a Take came after the *settled snapshot*, the older snapshot is the clean copy instead: the commit the Take recorded with its Version (§8, step 1, *At the Take, in order*, item 5), every Copy at that Version. It is first checked against that Version, which the Maintainer Repo holds; a difference is said before anything is read. So the Take's own changes are never read as the System Repo's.

  **When the stop moves.** Act on the verdicts sets the *settled snapshot* to the stop at every look, whether or not anything was read (§6, step 1). When the verdicts ask for no change, or there are none, that is right after judging. It never moves before: a Reading left half done must not mark its Changes read. Whether the System Repo takes the Update does not hold it back: by then all between the two snapshots is read, judged and acted on, and what follows is the next Reading's. The Reading stays a draft, and goes once its work is done.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo. For this step it says:
  - the older snapshot is the Register's *settled snapshot*; after a Take, the clean copy, checked first against its Version;
  - the stop is the System Repo's main, written first at every look, before anything is read;
  - Act sets the *settled snapshot* to the stop at every look, once the verdicts, if any, are acted on.
- **Today:**
  - borrowed: the stop is written first, as the Reading's first line, before anything is read (`.claude/skills/exchange-read/SKILL.md`, Stage 2);
  - borrowed: the Register keeps where each System Repo lives, as today's list of CBC Runs does (`ARCHITECTURE.md` §2.5, *The CBC Runs*). It gains the *settled snapshot*;
  - borrowed: a CBC Run Reading is a draft in `temp/`, deleted once the work that needed it is done (`temp/README.md`; `.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today the stop, the Read-Through Commit, is kept in the CBC Run, carried there by the next Delivery Note, because "it is the only place the Concept Deliverer can look" (`docs/conventions/exchange/` §2.2, *The CBC Run*). Today every CBC Run Reading is followed by a delivery, so the stop always arrives. Here a Reading may have no Update after it;
  - changed: today a CBC Run is born with its Read-Through Commit written as *none*, and the exchange-read Agent Skill names no span for it (`delivery/installs/pure-seed.md`, step 2). Here birth writes the start as the *settled snapshot*, and the first Reading starts there.

**Step 3. The Maintainer Repo compares the Copies, and reads each Record.**

- **What must happen:** between the two snapshots, the older one and the stop, the agent finds every Change in the System Kit's folders, a new file among them, and pairs each with its Record. It only reads the System Repo, and writes only in the Maintainer Repo.
- **Options,** for how Changes are found:
  - a. each Copy compared between two snapshots of the System Repo's own: the older one and the stop;
  - b. each Copy compared with the Version the Copies came from;
  - c. only the Records read, with no comparison;
  - d. the commits between walked one by one.
- **Chosen:** a. The others:
  - b finds the same as a at the first Reading after birth or a Take. After it, a Change already read differs from that Version until the next Take, and is found again at every Reading before it;
  - c misses a Change with no Record, which the commit's check should have stopped, but which can still land (Failure Case 22);
  - d shows every edit on the way, and Changes the gate reversed. The gate has settled those (§3, step 2); what stands at the stop is what is read.

  **Pairing.** A Record lands in the same diff as its Change, in the Copy's Adapted Understanding Text, so pairing them is reading one diff. Three things can come out:
  - a Change with its Record: read with its what, what happened, which work found it, and the System Repo's proposal;
  - a Change with no Record: read from the comparison alone, and marked "no entry";
  - a Record changed with no Change, as when a why is rewritten: read as a change of its why.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo. For this step it says:
  - compare each Copy between the older snapshot and the stop; the commits between are history, opened only to understand something deeper;
  - pair each Change with its Record; mark one with none "no entry";
  - read a Record changed with no Change as a change of its why;
  - judge nothing.
- **Today:**
  - borrowed: every item is read from the copies' diff, the whys, and the lines to the Concept Deliverer (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*; `.claude/skills/exchange-read/SKILL.md`, Stage 3). Here the whys are in the diff, and nothing else is sent to the Maintainer Repo, so it is one: the diff;
  - borrowed: the CBC Run is only read, never written (`.claude/skills/exchange-read/SKILL.md`, *Gates*);
  - changed: today the diff runs against what was delivered, the Receipt Branch or the last delivery entry (`.claude/skills/exchange-read/SKILL.md`, Stage 3). That works because a Delivery Take makes every copy equal its original again. Here a Reading may come before the Take, while a Copy still holds Changes already read;
  - borrowed: a Receipt Branch holds the delivery as it arrived, and makes the next diff exact (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 4). The clean copy does the same after a Take;
  - changed: today the whys are read from the Decisions Log. Here they are read from the Records, in the Copies.

**Step 4. It lists what changed, nothing judged.**

- **What must happen:** the Reading gets one line per Change, nothing judged. The list may be empty: then no draft is written, and only the stop is handed on. The human checks that the list is whole. Then it is judged, and its stop moves into the Register once its verdicts are acted on (step 2).
- **Options:**
  - a. one line per Change, nothing decided; judging is §5's;
  - b. each Change judged as it is listed;
  - c. only the Changes the System Repo proposed as any repo's are listed;
  - d. one line per Copy, its Changes summed.
- **Chosen:** a. The others:
  - b judges before the whole list is seen, so Changes with one reason are judged apart, and each verdict tends to follow the System Repo's proposal (Failure Case 20). Listing is cheap and judging is not, so the list is checked whole first;
  - c takes the proposal for the verdict, and a lesson for every repo stays in one System Repo (Failure Case 20);
  - d merges two Changes to one Copy, and one of their reasons is lost.

  **What a line holds.** A line holds what step 3 found: the Copy and its part, what it says now, what happened, which work found it, and the System Repo's proposal, marked as one. A Change with no Record says "no entry". Changes linked by one reason are listed together, under it.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo. For this step it says:
  - one line per Change, nothing judged;
  - linked Changes listed together, under their reason;
  - a line holds what step 3 found, the proposal marked as one;
  - the human checks the list is whole; the stop moves into the Register once the verdicts are acted on.
- **Today:**
  - borrowed: one line per item, what it is and where, nothing decided (`.claude/skills/exchange-read/SKILL.md`, Stage 4 and *Gates*);
  - borrowed: the Reading is a draft to its form (`.claude/rules/exchange-reading.md`);
  - changed: today a line is one per edit, per CBC Run Ask and per finding, read from three places (`.claude/skills/exchange-read/SKILL.md`, Stage 3). Here a line is one per Change, with its Record;
  - changed: today the proposal is not asked for: every edit must claim to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each line carries it, as input to judging.

## 5. Judge

§5 to §8 are simulated first for depth b, the System Kit's Adapted Case changing: the shortest path into the System Kit through every step. Depth c, the idea above changing, at either layer, is then checked against them (§2, the "how deep" rows). Known before it was simulated:

- the four questions decide, in order, the cheapest first, and the System Repo's own view of its Change is input, never the verdict:
  1. Did the Copy already say this? Then it is a misreading (Failure Case 7). Nothing changes but, perhaps, the Copy's wording.
  2. Is it specific to that System Repo's problem? Then nothing changes here (§2, *Known, not ruled*).
  3. Does the idea above already hold it, the Work Domain Idea above the Adapted Case, or the Backbone Idea above that? Then the Adapted Case it came from lost it in narrowing, and is fixed from the idea above. When only the Backbone Idea holds it, the Work Domain Idea lost it too, and is fixed first.
  4. How high is it true? 4a, still true naming no Adapted Case: a lesson for its Work Domain Idea. 4b, still true naming no Work Domain: a lesson for its Backbone Idea.

  If none holds, it is a lesson for its Adapted Case: the Adapted Case it came from gains it, and the idea above stays as it is;
- the depth comes from the reason, never the edit. A cap raised from 50 to 60 is the System Repo's own, depth a, when its reason is "our scope names are long". The same edit is a lesson for its Work Domain Idea, depth c at layer 2, when its reason is "the cap counts the scope, which any repo with scopes meets". Only the recorded reason tells them apart;
- what the System Repo gets reaches it with the next Update (§7, step 1).

Two steps:

1. The list is judged.
2. The verdict is written.

**Step 1. The list is judged.**

- **What must happen:** each line of the Reading is first judged sound or not. A sound line is then judged by the four questions, in order, the cheapest first, until one holds (above). The agent proposes an answer to each, with what it read; the human decides. For depth b, none of the four holds: it is a lesson for its Adapted Case. An empty list gives no verdicts, and Judge hands Act only the stop.
- **Options,** for who judges:
  - a. the agent proposes each answer, with what it read, and the human decides each line;
  - b. the agent judges, and the human looks only at the lines where the agent disagrees with the System Repo's proposal;
  - c. the human judges alone.
- **Options,** for a line marked "no entry":
  - d. judged from the comparison alone;
  - e. held, until the human brings its why from the System Repo;
  - f. its why looked for in the System Repo first, in the commit that made the Change and in the System Repo's records, then asked of the human. The line says where its why was found, and is held while neither gives it.
- **Chosen:** a and f. The others:
  - b lets the agent's agreement with the proposal pass unchecked: two views agreeing is not a verdict (Failure Case 20);
  - c leaves the human to read every text the questions need, which the agent reads faster, and with nothing written down to check;
  - d judges on a guess at the why (Failure Case 22);
  - e asks the human for what the System Repo may already have written.

  **What each question reads:**
  - question 0, the Change is sound: what happened, the Change, and the original part. Does it fix what happened, without breaking something the Copy did? An unsound Change goes no further: the depth questions are not asked, and the verdict says why. What becomes of the Change is not ruled (§2, *Known, not ruled*);
  - question 1, the Copy already said it: the original part, in the Version the Copies came from, beside the Change. When the System Kit has moved since, its part as it is now is read too: a change the System Kit has since made the same way is covered, and nothing new is made, so one lesson is not made twice;
  - question 2, specific to that System Repo's problem: what happened, the System Repo's proposal, and its framing of its problem;
  - question 3, the idea above already holds it: the Work Domain Idea above the Adapted Case, then the Backbone Idea above that. When only the Backbone Idea holds it, the Work Domain Idea lost it too, and the loss sits at layer 2;
  - question 4, how high the lesson is true, since it goes as high as it is true (`temp/common-ground/knowledge-layers-general.md` §3.1, *How the layers fill*): 4a, still true naming no Adapted Case, for its Work Domain Idea, layer 2; 4b, still true naming no Work Domain, for its Backbone Idea, layer 1 (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, the arrow *lesson*). When 4a does not hold, it is a lesson for its Adapted Case, depth b. Depth c's step, checked later.

  **Lines together, lines split.** Lines listed together under one reason are judged together, and the reason is judged once. A line whose parts answer differently is split, each part judged on its own; the parts keep their one Record.

  **Not from the wording.** A question is answered from what the Change does and why, never from its wording. The System Repo writes in its own words on purpose (§3, step 1), and making a lesson general is rewording, after judging (§6, step 1). A Change worded for one project may still be a lesson for every repo. The agent's answer to question 2 says whether it agrees with the System Repo's proposal, and why if not.
- **Adapted Case:** the Maintainer Repo's, for judging a Reading. It loads when the human starts judging a Reading whose list was checked whole. For this step it says:
  - question 0 first: does the Change fix what happened, without breaking something the Copy did? An unsound Change goes no further, and its verdict says why;
  - then the four questions, in order, until one holds; for each, what it reads;
  - a line whose parts answer differently is split, each part judged on its own;
  - a question is answered from what the Change does and why, never from its wording;
  - the agent proposes each answer with what it read; the human decides;
  - lines under one reason are judged together;
  - a line with no Record: its why is looked for in the System Repo's commits and records, then asked of the human; the line says where its why was found, and is held while neither gives it.
- **Open:**
  - how question 4 is answered, and by whom. A first guess, not a rule: 4a first, and 4b only if 4a holds. 4a is the cheaper check, inside one Work Domain, and a lesson still true naming no Work Domain is true across its own. Its trigger: depth c is checked against these steps, or the first lesson judged at layer 1;
  - which other texts are checked for a loss question 3 finds. Nothing comes down the arrow *adapt*, since the idea above did not change (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 7). Today's draft checks only the Maintainer Repo's own Adapted Case of the same idea. A first guess: the texts built on the idea that holds the part, as the survey asks (§6, step 1). If several lost it, the idea's wording may be too weak, and is reworded clearer, never narrower. Its trigger: the first depth-d verdict.
- **Today:**
  - borrowed: the four questions, from the rules on deciding written in the problem file before this simulation. They leave how each is answered, and by whom, open; step 1 answers it for questions 1 to 3;
  - borrowed: a change may be declined as "not worth the change" (`docs/conventions/exchange/` §6.5, *Verdicts*). Question 0 asks it first, for every depth;
  - changed: the four questions gain question 0, and a line may be split into parts. The rules on deciding have neither;
  - borrowed: a verdict that cannot be reached yet is held, with its trigger and a line so it is not lost (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today a verdict says whether the Concept Deliverer takes a hunk: taken, declined or held (`docs/conventions/exchange/` §6.5). Here it says how deep the Change goes. Depth b is near today's taken: the Change enters the System Kit.

**Step 2. The verdict is written.**

- **What must happen:** each judged line, or part of one, gets a verdict, the agent drafting and the human deciding. It is the Maintainer Repo's decision, written for its own work: what it changes, in the System Kit or the idea above, starts from it (§6, step 1). Which verdicts the System Repo gets is §7, step 1's. For depth b: a lesson for its Adapted Case. The proposal holds when the System Repo gave it as one any repo would meet.
- **Options,** for what a verdict holds:
  - a. the answer only: unsound, misread, or its depth;
  - b. the answer, its why, and whether it agrees with the System Repo's proposal, with why if not;
  - c. b, and what the Maintainer Repo changes for it.
- **Chosen:** b. The others:
  - a leaves the change made from it with nothing to check it against, and a proposal judged wrong goes unseen;
  - c decides what changes before it is worked out: that is §6, step 1's, with the survey where the depth needs one.

  **The verdicts.** A verdict is one of:
  - unsound;
  - misread, question 1;
  - covered by a System Kit change since the System Repo's Version, question 1;
  - its own, question 2, depth a;
  - lost in narrowing, question 3, depth d;
  - a lesson for its Work Domain Idea, question 4a, depth c at layer 2;
  - a lesson for its Backbone Idea, question 4b, depth c at layer 1;
  - a lesson for its Adapted Case, depth b;
  - held, with its trigger.

  Lines under one reason share one verdict, and each line says how its own Copy is affected.

  **The agreement.** The agreement is said in one line, "the proposal holds" or "the proposal does not hold, because …". An unsound verdict says what the Change breaks or leaves unfixed; what becomes of the Change is not ruled (§2, *Known, not ruled*).
- **Adapted Case:** the Maintainer Repo's, for judging a Reading. For this step it says:
  - one verdict per line or part: its answer, its why, and whether the proposal holds;
  - the answer is one of the nine verdicts listed above; an unsound one says what the Change breaks or leaves unfixed;
  - lines under one reason share a verdict, each saying how its own Copy is affected.
- **Open:** whether an unsound verdict offers a fix. Its trigger: the first unsound verdict.
- **Today:**
  - borrowed: a verdict carries its why (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today every verdict goes down in the Delivery Note (`docs/conventions/exchange/` §6.5). Here the verdict is the Maintainer Repo's, and only those the System Repo can act on go down (§7, step 1);
  - changed: today a verdict is taken, declined or held (`docs/conventions/exchange/` §6.5). Here it is a depth, or unsound, misread, covered or held;
  - changed: today no verdict answers a proposal, since every edit claims to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each says whether the proposal holds.

## 6. Act on the verdicts

**Step 1. The Maintainer Repo makes its changes. For depth b, the System Kit's Adapted Case.**

- **What must happen:** from each verdict, the Maintainer Repo makes what its depth asks, the agent drafting and the human deciding. For depth b, the System Kit's Adapted Case gains the lesson, worded for every System Repo, and is committed in the Maintainer Repo: the System Kit stands at a new Version. The System Repo the lesson came from gets it back with the next Update, though its Copy already holds the Change in its own words (§7, step 1). The Reading stays a draft until that Update is made. Once the verdicts are acted on here, Act sets the *settled snapshot* to the stop, in the Register (§4, step 2). It does so at every look: with no verdicts, as in cases A and C, that is all it does (§4, step 1, *A look at main*).
- **Options,** for depth b:
  - a. the lesson is reworded for every System Repo, and the System Kit's Adapted Case gains it, its first wording kept beside it;
  - b. the Change goes into the System Kit's Adapted Case as the System Repo wrote it;
  - c. the lesson waits until a second System Repo makes the same Change.
- **Chosen:** a. The others:
  - b carries one project's words to every System Repo, since the System Repo writes what happened in its own words, on purpose (§3, step 1);
  - c waits for a second proof of what judging already found: question 2 found the Change is not that System Repo's own.

  **The other depths.** For the other depths, this step holds the work, each checked here later:
  - depth c changes the idea above at its layer, after the survey: its Work Domain Idea at layer 2, its Backbone Idea at layer 1;
  - depth d fixes the Adapted Case from the idea above, after fixing the Work Domain Idea from its Backbone Idea when the loss sits at layer 2;
  - depth e marks a narrowing with its why, in the text just below the idea that does not fit.

  **The survey.** Before a lesson enters the idea above, every other text built on that idea is asked whether it fits, the one the lesson came from excepted (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, the arrow *adapt*; §2.3, *The Adapted Case layer*). At layer 2, that is the other Adapted Cases of that Work Domain Idea, the Maintainer Repo's own only when they share it. At layer 1, it is every Work Domain Idea on that Backbone Idea. It is the arrow *adapt*'s check, run before the idea changes, so a conflict shows first. Each text answers "holds as it is", "must change", with what and why, or "conflicts", with why. A conflict is input to the human's decision, never a veto, and what the survey finds must change, changes. Its answers are also evidence for question 4: if every answer conflicts, the lesson is not true that high.

  A lesson is reworded here, never before: for every System Repo at depth b; at depth c, naming no Adapted Case at layer 2, and no Work Domain at layer 1 (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, the arrow *lesson*). Its first wording is kept beside it, since the rewording is the agent's reading.
- **Adapted Case:** the Maintainer Repo's, for judging a Reading. For this step it says:
  - a lesson for its Adapted Case is reworded for every System Repo, its first wording kept beside it, and the System Kit's Adapted Case gains it;
  - the Reading stays a draft until the Update carries what the System Repo needs;
  - once the verdicts are acted on, or when there are none, the *settled snapshot* is set to the stop, in the Register.
- **Open:**
  - at layer 1, how far down the survey reaches before the change: only the Work Domain Ideas, each checking its own Adapted Cases when it changes, or every Adapted Case below them at once. The first is cheaper; the second may catch a conflict two layers down. Its trigger: the first lesson judged at layer 1;
  - how a part of a Backbone Idea is known not to fit a whole Work Domain, when one System Repo's Change shows one Adapted Case. A first guess: the same survey, over that Work Domain Idea's Adapted Cases. Its trigger: the first depth-e verdict.
- **Today:**
  - borrowed: a taken change is committed here, and the next delivery carries it (`docs/conventions/exchange/` §6.5, *Verdicts*). It is depth b's path, and the other depths'.

## 7. Deliver

Two steps:

1. The Update is made: the System Kit's changes, and the verdicts the System Repo can act on.
2. The Update is delivered.

**Step 1. The Update is made: the System Kit's changes, and the verdicts the System Repo can act on.**

- **What must happen:** when work resumes in the System Repo, after it is read back and judged, the Maintainer Repo makes its Update, the agent drafting and the human deciding (§8, step 1, *Before the Take*). An Update is due when the System Kit has moved past the Version the System Repo's Copies came from, or when its Reading left a verdict that goes down. It reaches the System Repo on the human's word, in a step of its own: nothing crosses without that word, and the agent may carry it. For depth b, the System Kit has moved for this Change, so an Update is due: it carries the System Kit's Adapted Case at the new Version, with the lesson as its why. Its verdict goes down only if its proposal did not hold.
- **Options,** for which verdicts go down:
  - a. every verdict;
  - b. only those the System Repo can act on: unsound, misread, and a proposal that did not hold;
  - c. none; only the System Kit's changes.
- **Options,** for when an Update goes:
  - d. after every Reading, even with nothing to carry;
  - e. only when it carries something: a System Kit change, or a verdict that goes down.
- **Chosen:** b and e. The others:
  - a sends lines that ask nothing of the System Repo. A lesson taken into the System Kit, with its proposal holding, needs no answer: the Update brings the change and its why;
  - c leaves an unsound Change unknown to the only repo that can reverse it;
  - d sends an empty Update to carry where the Reading stopped. The *settled snapshot* is in the Register now (§4, step 2), so nothing needs carrying.

  **When one is due.** Whether an Update is due is found by comparison, as §4, step 1 finds work to read: the System Repo's Version, which it holds, against the newest. It runs after Act, at every look, and when the human names a System Repo to update, or asks which are behind. A System Repo cannot see the Maintainer Repo, so it cannot learn this itself. Nothing is sent to a System Repo whose work has not resumed.

  **What it is.** An Update is two things: every Copy, whole, at the new Version, and an Update Note. The System Repo then has the new version of each file, and finds its old one in its own history (§8, step 1). The Update Note holds:
  - the new Version;
  - the System Repo's *settled snapshot* it was built against, whether a Reading ran or not. The Take checks it before anything moves (§8, step 1). The Update Note names the check, so a System Repo whose Adapted Case for taking is older still meets it;
  - what changed since the System Repo's Version: each path changed, new, gone or renamed, and how many. The System Repo checks the files against it when they arrive, and a file that is gone cannot say so itself;
  - the why of each System Kit change since then, whatever its source: the Reading of this System Repo or of another, or the Maintainer Repo's own work. Each why stands on its own, and names no other repo; a change that comes from a lesson for the idea above quotes the lesson as its why. With it, the System Repo judges a change against its own needs without seeing the Maintainer Repo;
  - the verdicts that go down, from this System Repo's own Reading only, each naming the System Repo's own Copy and part, the System Repo's commit it judged, and what the System Repo may do now. The commit is the System Repo's own, so it can open it, and see whether the part has changed since (§8, step 1);
  - which files are taken first: the Adapted Case for taking an Update, so an Update is never taken by instructions older than it (§8, step 1, *At the Take, in order*, item 1; Failure Case 10);
  - the Update it replaces, when one was waiting.

  **What the Update Note is not.** The Update Note is no summary of the Maintainer Repo's work, which the System Repo cannot check. It is not a record either: it goes once the Update is taken, and what the System Repo decides goes in its Records.

  **What it cites.** Nothing in it cites what the System Repo cannot open: no path, record or word of the Maintainer Repo's own.

  **One at a time.** A Reading stays open until its Update is made, or until it is judged with nothing to send. One Reading is open per System Repo at a time: a Reading made while one is open extends it, and its lines are judged with the rest, so judging already done is kept. One Update waits for the System Repo at a time: a newer one replaces one not yet taken, since it carries every System Kit change since the Copies' Version, and the verdicts of both Readings.
- **Adapted Case:** the Maintainer Repo's, for making an Update. It loads on the human's word to update a System Repo. For this step it says:
  - it follows the System Repo's reading back and judging, never comes before them;
  - it goes only when it carries a System Kit change or a verdict;
  - it is due when the System Repo's Version is behind the newest, or a verdict goes down; the Versions are compared after Act at every look, and when the human names a System Repo or asks which are behind;
  - it carries every Copy whole, at the new Version, and an Update Note holding the seven things listed above;
  - it cites nothing the System Repo cannot open;
  - each verdict names the System Repo's commit it judged;
  - one Reading open per System Repo, a new Reading extending it; one Update waiting, a newer one replacing it.
- **Today:**
  - borrowed: the delivery is staged into the CBC Run's `temp/` on the reviewer's word, the CBC Run's tree checked clean first, and named by the commit it was final at (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: files go whole, every copy at every delivery after birth (`docs/conventions/exchange/` §3.2, *What goes*);
  - borrowed: a delivery goes after a CBC Run Reading, or when something a CBC Run holds has changed in the Concept Deliverer (`.claude/skills/exchange-deliver/SKILL.md`, its description);
  - borrowed: the Delivery Note says what changed since the Delivery Pin, as paths the CBC Run can check, and why it matters to this CBC Run; it never describes the Concept Deliverer's own practice (`docs/conventions/exchange/` §3.7, *The Delivery Note*; `.claude/skills/exchange-deliver/SKILL.md`);
  - borrowed: a verdict says the decision and what the CBC Run owes now, nothing else; no path or word of this repo's reaches it (`docs/conventions/exchange/` §3.7);
  - borrowed: a Delivery Note may arrive alone, with no files (`docs/conventions/exchange/` §6.6, *The Delivery Note after a read*). An Update of verdicts only is one;
  - borrowed: the Delivery Note carries what is gone (`docs/conventions/exchange/` §3.6, *Absence in a delivery*);
  - borrowed: one CBC Run Reading is open per CBC Run at a time, and a new read extends it (`.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today every read ends with a Delivery Note, even an empty one, to carry the Read-Through Commit (`docs/conventions/exchange/` §6.6). Here an Update goes only when it carries something;
  - changed: today the Delivery Note gives a verdict on everything the CBC Run addressed to the Concept Deliverer (`docs/conventions/exchange/` §3.7). Here only the verdicts the System Repo can act on go down.

**Step 2. The Update is delivered.**

- **What must happen:** on the human's word, the Update is staged into the System Repo's `temp/`, by the human or by the agent. It writes only into the System Repo's `temp/`, nowhere else there. Nothing in `temp/` is in force until the System Repo takes it (§8, step 1).
- **Options,** for checking what was staged:
  - a. a second Adapted Case of the Maintainer Repo's checks it, apart from the one that delivered, as at birth;
  - b. the delivering Adapted Case compares each staged file with the new Version, once staged, and the System Repo checks the Update Note against the files when it takes them;
  - c. only the System Repo's check, at the Take.
- **Chosen:** b. The others:
  - a was chosen at birth because the start becomes the base of every Reading (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Here a wrong file is held in `temp/`, never in force, and a comparison of files leaves little mistake to share. It comes back if a staged file is found, after a Take, to differ from the System Kit;
  - c leaves only the System Repo to check, and it cannot open the System Kit, so a staged file that differs from it passes.

  **Before staging.** The System Repo's tree is checked clean first, with no work under way. When it is not, the agent says what it found and waits for the word. An Update already waiting there is replaced by the new one (step 1). The Update is named by the Maintainer Repo's commit at which its files and Update Note were final, so its Version is exact.
- **Adapted Case:** the Maintainer Repo's, for delivering an Update. It loads on the human's word to deliver. For this step it says:
  - never stage unasked; check the System Repo's tree clean first;
  - write only into the System Repo's `temp/`, replacing an Update already waiting;
  - name the Update by the commit it was final at;
  - compare each staged file with the new Version.
- **Today:**
  - borrowed: the delivery and its Delivery Note are copied into the CBC Run's `temp/` on the reviewer's word, by the reviewer or by the agent when told; the agent never stages unasked; the tree is checked clean first; the Delivery Staging is named by the commit at which files and Delivery Note are final (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: one Agent Skill both writes the Delivery Note and stages the delivery (`.claude/skills/exchange-deliver/SKILL.md`). It also compares the staged files here;
  - borrowed: the CBC Run's `temp/` gains exactly the staging and its Delivery Note, and nothing tracked in the CBC Run changes (`.claude/skills/exchange-deliver/SKILL.md`, *Gates*);
  - changed: today the staged files are copied by a script, so they equal the Master Copies by how they are made, and no comparison follows; the CBC Run's Delivery Take checks the Delivery Note against the files (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 1).

## 8. Take

**Step 1. The System Repo takes the Update.**

- **What must happen:** the Update is taken between two Plan Steps, when the next is about to open, never in the middle of one, the agent proposing and the human deciding. Before that step opens, in a fixed order: the System Repo is read back to main, judged, and its Update, when one is due, made, delivered and taken. Then the step opens on the new Copies, or on the same ones when no Update was due. The Take runs on a branch of its own, and reaches main only at its gate's close.
- **Options,** for when an Update is taken:
  - a. whenever it arrives;
  - b. at a Plan Step's opening, right after a Reading that reached main;
  - c. at a Plan Step's opening, whatever was read.
- **Options,** for the System Repo's Records at the Take:
  - d. kept, since the merge keeps what only the System Repo added;
  - e. all cleared, every Copy taken whole.
- **Options,** for where the Take is committed:
  - f. on a branch of its own, one commit per part, a gate last, main moving by fast-forward at the gate's close;
  - g. as the next Plan Step's first commit;
  - h. as a Plan Step of its own;
  - i. as one commit on main, Read's rule narrowed so that only a Plan Step's work waits for a gate.
- **Chosen:** b, e and f. The others:
  - a lands in the middle of a step, which then runs on two sets of rules;
  - c takes the Update over Changes not yet read. The Update answered none of them, and clearing their Records loses them before they are read;
  - d keeps Records that say how a Copy differed from the old System Kit. After the Take some describe nothing, and none says how the Copy differs from the new one;
  - g leaves main on the old Version until the step's gate closes, so a look in between finds the Update due again;
  - h gives the Take a Plan Step's opening for work the Update Note already orders. f keeps what it needs from one: the gate;
  - i narrows Read's rule, that main moves only at a gate's close, for the Take alone. f keeps the rule whole, its gate checking that the Take finished.

  **Before the Take.** The opening order is fixed: reading back, judging, then the Update. An open Reading is extended. The human works on one project at a time, so the System Repo waits at little cost. A Plan Step open when the human returns finishes on the old Copies first; the human may instead drop or restart it, when the Update changes a rule it rests on. The Take checks first, from the Update Note, what the System Repo itself can see:
  - case 1, its main is still the *settled snapshot* the Update Note names: the Update is taken. Its Version needs no check of its own: it is recorded in main, so it cannot change while main stands still;
  - case 2, anything else: there is no Take, and the System Repo says so. The human has it looked at, and the look finds its case, C or D when main has moved (§4, step 1, *A look at main*). Deliver's check then finds a new Update due, made against the System Kit as it is now. It replaces the waiting one and carries its verdicts not yet sent (§7, step 1).

  **A check before delivery.** The Maintainer Repo may compare the System Repo's main with the *settled snapshot* before delivery too, to save a delivery bound to fail. A System Kit moved since the Update was made is no reason to refuse it: the Update is correct, if not the latest, and the next brings the rest.

  **Old Records.** A gate may have fixed, merged or dropped Records the Update answered. These show in the next Reading's comparison as Changes with their Records, and are judged like any. Records from before the *settled snapshot* still in the Copies are cleared at the Take.

  **At the Take, in order.** Once the check finds case 1, the Take cuts a branch from main, the *settled snapshot*. Its first commit is the Update as it arrived, in `temp/`, not yet in force: a record of what came, before the Take changes anything. Each item below is then a commit of its own, but items 2 and 4, a check and a reading. Main moves to the branch's last commit by fast-forward at the gate's close, so it still moves only at a gate's close (§4, step 1, *Where a stretch ends*).
  1. the Adapted Case for taking an Update is taken first, on its own, so the rest is taken by the new one (Failure Case 10);
  2. the files are checked against the Update Note: what changed, and how many (§7, step 1). A mismatch is said before anything moves;
  3. every Copy is taken whole, at the new Version; each path gone is removed, and each renamed is moved. Every Record is cleared: main is the *settled snapshot*, so each was read and judged. A part the System Repo never changed is taken, and work shows whether it fits (§3, step 1);
  4. each verdict is read. One on a Change the System Kit took asks nothing more: the new Version holds the Change. What follows any other is not ruled (§2, *Known, not ruled*);
  5. the new Version is recorded, with the commit that holds it: item 3's, the clean copy, every Copy at the new Version. So Deliver's check can compare it with the newest;
  6. the Update and its Update Note are removed from `temp/`;
  7. the Take's gate, last. It checks that the Take finished: the files matched the Update Note, every Copy is at the new Version, the Version is recorded, and `temp/` holds no Update.

  **A postponed Take.** A Take may be postponed, with its why. Work then goes on with the old Copies. At the next opening, the Take starts again from its check, case 1 or case 2 (*Before the Take*).

  **What a Record stands against.** Every Record stands against the last Version taken, or birth's, and every Record goes at a Take. This is confirmed at the first Update to reach a System Repo whose Copies have Records.
- **Adapted Case:**
  - the System Repo's, for taking an Update, itself in the Update and taken first. It loads when a Plan Step opens with an Update waiting. For this step it says:
    - check first that main is still the *settled snapshot*, and take nothing when it differs, saying so;
    - take only at a Plan Step's opening, or postpone with why;
    - take on a branch of its own, in the order above, one commit per item, the gate last, checking that the Take finished; main moves by fast-forward at the gate's close;
  - the System Repo's gate list, at a Plan Step's opening: was this System Repo read back, and its Update, when one was due, taken, since the last opening? A System Repo cannot see this itself; the human answers.
- **Open:**
  - finished work done under a rule the Update changed may now be wrong. New work follows the new Copy; the System Repo lists which System Kit changes touch rules its finished work followed, and the human decides. Its trigger: the first Update that changes a rule a finished Plan Step followed;
  - a Take postponed again and again leaves the System Repo far behind. Its trigger: the first Take postponed past two openings.
  - where a postponed Take's why is written, and so whether it is a commit, and who reads it. Its trigger: the first Take postponed.
  - whether the Take still needs a branch and a gate of its own, now that nothing is put back for the gate to decide. One commit on main, option i, would narrow Read's rule. Its trigger: the first Take, or putting back coming back (§2, *Known, not ruled*).
- **Today:**
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: the Delivery Take's order: the Delivery Note checked against the staging first, copies taken whole, what is gone removed, one entry with the new Delivery Pin, the staging removed (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, steps 1, 4, 5, 6 and 7);
  - borrowed: a Plan Step reaches main by fast-forward from its branch, at its close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). The Take's branch does the same;
  - borrowed: a Receipt Branch may hold the delivery as it arrived (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 4). Here the Update is committed as it arrived, on the Take's branch;
  - changed: today, with more than one commit, the Delivery Take's entry goes in the last, where every copy equals the Delivery Pin (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Here the Version names the clean copy, item 3's commit, where the next Reading starts (§4, step 2, *After a Take*);
  - changed: today nothing at the Delivery Take is decided at a gate. Here the Take's gate checks that the Take finished;
  - borrowed: being behind the Concept Deliverer is acceptable (`delivery/container/.claude/rules/delivered-copies.md`, rule 6). A postponed Take is that;
  - changed: today an edit made after the Read-Through Commit is re-applied on top, its record standing (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 3). Here the opening order leaves no such edit;
  - changed: today a declined edit is gone at the Delivery Take, and never edited back in (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Here what becomes of a Change the System Kit did not take is not ruled (§2, *Known, not ruled*);
  - changed: today work continues on the edited copy when a Plan Step opens before the reply (`delivery/container/.claude/rules/delivered-copies.md`, rule 6). Here the next step waits for the Take, unless it is postponed with why.

