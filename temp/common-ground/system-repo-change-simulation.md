# A System Repo's Copy Change, Simulated

<!-- A draft of the knowledge work (ADR-0082). It simulates the cases
     of a System Repo's Copy Change, step by step. It is the one home of
     the facts of Change until the change flow is done: the six
     parts, their rules and the cases. A part's rules are its steps'
     *Chosen* and *Adapted Case* fields. Then they move to their
     final home, written out as rules, and this file points there
     (TODO.md, the item "Define the Change idea"). Its input: the
     frozen temp/common-ground/between-repos-simulation.md, §5.2, *Work in a System
     Repo*, and §5.3, *Reading a System Repo*. It goes once what it
     holds has landed in the rewrite into the layers model, and git
     keeps every version. -->

This document simulates the cases of a System Repo's change (§2), step by step. It holds the facts of Change until the change flow is done, and its steps' *Chosen* and *Adapted Case* fields are the rules (§1). One case is simulated through every step: a System Repo changes one Adapted Case, and the System Kit takes the Copy Change: its Adapted Case changes (depth b, §5). The other cases are checked against it (§2). It uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*).

It shortens ten Defined Terms to their last two words, as the layers document does, in its table (`temp/common-ground/knowledge-layers.md` §2, *The layers*).

The scope of that case: a Copy Change may touch the Adapted Understanding Text, an Instruction Text built on it, or both, in either order. Its reason may be the System Repo's own, or one any repo would meet. A stretch of work may hold several Copy Changes (§2). No fixed example is used: each step's choice must hold at each end of this scope.

## 1. How it is worked

Three moves, in order:

1. **Simulate:** each step below says what must happen, what could be done, and what is chosen.
2. **Read the rules together:** once all of a part's steps are seen together, their *Chosen* and *Adapted Case* fields are read as one: they are the part's rules. They are written out as rules only when they move to their final home (the header comment).
3. **Check them:** each step is walked again against the rules. A step a rule does not hold for changes the rule or the step.

The steps make six parts. Who does each, and how they make one movement, are the layers document's (`temp/common-ground/knowledge-layers.md` §3.2, *How a change travels*):

| Part | Steps |
|---|---|
| Change a Kit Copy | §3, steps 1–2 |
| Read Copy Changes | §4, steps 1–4 |
| Judge Copy Changes | §5, steps 1–2 |
| Act on the verdicts | §6, step 1 |
| Deliver the Kit Update | §7, steps 1–2 |
| Take the Kit Update | §8, step 1 |

Each step has these fields. A field with nothing in it is left out.

- **What must happen:** the outcome, and who acts.
- **Options:** what could be done here, today's way among them.
- **Chosen:** the option taken, and why the others were not.
- **Adapted Case:** which Adapted Case runs the step, whose it is, what loads it, and what it must say for this step. Once a part is done, these are read together: they give the rules, and later the Adapted Case texts.
- **Open:** what the step leaves undecided, each with the trigger that decides it.
- **Today:** what is borrowed from today, and what changes, each with its source. Today's things keep today's names, such as the Delivery Note.

## 2. The cases

The cases are simulated one at a time. The first is simulated whole; each other case is then checked against it, and what differs is written. A case that grows too complex goes to TODO, to be checked once the Common Ground Problem is finished. The cases are of two kinds:

- **What was changed:** these vary how the System Repo records its Copy Change, and how the Maintainer Repo finds it. They are the same however deep the Copy Change turns out to go, since that is known only once it is judged.
- **How deep it goes:** these vary how the Maintainer Repo decides, and how the Kit Update is written.

| Kind | Case | Status | Differs so far |
|---|---|---|---|
| what changed | one Adapted Case, any of its texts | simulated, §3 to §8 | — |
| what changed | a Defined Term | not yet checked | — |
| what changed | delivered Knowledge on Trial | not yet checked | read: compared like any Kit Copy; decided: the original was never proven, so the Copy Change is evidence for its trial |
| what changed | one reason behind Copy Changes to several Adapted Cases | not yet checked | recorded: one why, naming every Kit Copy it changed; read: the Copy Changes are listed together |
| how deep | b. the System Kit's Adapted Case changes: layer 3 | simulated, §5 to §8 | — |
| how deep | c, at layer 2. the idea above changes: its Work Domain Idea | not yet checked | the other Adapted Cases of that Work Domain Idea are surveyed, the Maintainer Repo's own only when they share it (§6, step 1) |
| how deep | c, at layer 1. the idea above changes: its Backbone Idea | not yet checked | every Work Domain Idea on that Backbone Idea is surveyed; how far down the survey reaches is open (§6, step 1) |
| how deep | d. the idea above already holds it: layer 3, or layer 2 | not yet checked | the loss sits at layer 2 when the Work Domain Idea lost a part its Backbone Idea holds: the Work Domain Idea is fixed from its Backbone Idea, then the Adapted Case from the Work Domain Idea. Which other texts are checked for the same loss is open (§5, step 1) |
| how deep | e. it asks to narrow the idea above: layer 3, or layer 2 | not yet checked | the narrowing goes into the text just below the idea that does not fit, marked with its why (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, its **Rules**, *Narrowing, never shrinking*): the Adapted Case, or the Work Domain Idea when a part of its Backbone Idea does not fit its whole Work Domain. How that is known is open (§6, step 1) |
| how deep | f. several Adapted Cases need it, but not all: no layer | not yet checked | it cannot enter the idea above. When it holds for every Adapted Case of one Work Domain, it is depth c, at layer 2. Two cases are left: several Adapted Cases of one Work Domain, but not all; and Adapted Cases across Work Domains, but not all (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 1). Each Adapted Case gains it, and the same text has no shared home. Open; its trigger: the first change two Adapted Cases need, but not every one |

How deep a Copy Change goes is how high it goes: each depth names the highest layer it changes, since a lesson goes as high as it is true (`temp/common-ground/knowledge-layers-general.md` §3.1, *How the layers fill*). The idea above is the Work Domain Idea an Adapted Case is written from, or the Backbone Idea that one is adapted from.

A stretch of work may hold several Copy Changes, alike or mixed. Each is recorded and read on its own, so they add no row but one: one reason behind Copy Changes to several Adapted Cases.

New text of the System Repo's own, on trial, is not a case here. It comes from no Kit Copy, so it is not a Copy Change. It is Knowledge on Trial, handed over at the System Repo's close (`temp/common-ground/knowledge-layers.md` §2.3, *The Adapted Case layer*). It is one of the other sources (below).

**Known, not ruled.** These can happen, and have no rules here until practice meets them. Rules once written for them are in git. Each says what can happen, and its trigger:

- **an Attention Note:** a System Repo has something for the Maintainer Repo that no Copy Change carries: a misfit worked around with no Copy Change made, a doubt about a line left as it is, something the System Kit lacked, a Kit Copy no longer used. Its trigger: the first such thing a System Repo needs to tell.
- **a Copy Change the System Kit does not take:** judged its own, depth a, the Copy Change staying in the System Repo at layer 4; or unsound, misread or held. It stays only in the System Repo's Kit Copy, and the Update Take takes every Kit Copy whole. Whether the Kit Copy keeps it past the Update Take is not ruled. Only such a verdict lets a Look for Lessons end in *Copy Change read* with no Kit Update due after (§7, step 1, *When one is due*). Its trigger: the first such verdict.
- **a verdict sent down:** a verdict the System Repo would act on: unsound, misread, or a proposal that did not hold. In the case simulated every Copy Change is taken, and the Kit Update brings it back with the lesson as its why. A proposal that did not hold is cleared with its Change Record at the Update Take, and the human already decided it in Judge Copy Changes. Today's Delivery Note sends every verdict (`docs/conventions/exchange/` §6.5, *Verdicts*). Its trigger: the first Copy Change the System Kit does not take, or a System Repo that needs a verdict it was not sent.

**Other sources.** A Copy Change is one source of the Common Ground Problem. Others exist: a birth, a lesson found in the Maintainer Repo's own work, Knowledge on Trial a System Repo hands over at its close, and new knowledge from the human. They are left on purpose until Change is finished (`TODO.md`, the item "Define the Change idea", its idea on the sources; the Maintainer Repo's own lesson in the item "Simulate depth c, then bring the Change idea to it").

**The whole flow.** The six parts of §1 and the depths of the table above, in one picture. It is a summary: the sections it names hold the facts.

```
 System Repo               ┆ Maintainer Repo
 ───────────               ┆ ───────────────
                           ┆
 1. Change a Kit Copy ─────┼── reads; writes nothing there ──▶ 2. Read Copy Changes ──▶ 3. Judge Copy Changes ──▶ 4. Act on the verdicts
    §3                     ┆                                   §4                       §5                        §6
                           ┆                                                                                      │
 6. Take the Kit Update ◀──┼── writes only into its temp/ ──── 5. Deliver the Kit Update ◀────────────────────────┘
    §8                     ┆                                   §7

 How high each depth goes: 3. Judge Copy Changes sets it, 4. Act on the verdicts changes it

 depth                          b        c, at 2   c, at 1   d         e         f
                                         └─────────── not yet checked ────────────┘
 layer 1  Backbone Idea                            ●
 layer 2  Work Domain Idea               ●         ●         ○         ○
 layer 3  Adapted Case          ●        ●         ●         ●         ●
 layer 4  a System Repo's work  ●        ●         ●         ●         ●         ●
 ───────────────────────────────────────────────────────────────────────────────────────────
 highest layer                  3        2         1         3, or 2   3, or 2   none, open
```

At every depth, 5. Deliver the Kit Update brings a Kit Update down.

Key: ● is the Copy Change's path, from its Kit Copy up to the highest layer it changes. ○ is "or up to here", when the case asks it (the table above, rows d and e). The line after the picture follows the layers document's arrows (`temp/common-ground/knowledge-layers.md` §3.2, *How a change travels*). A § is a section of this document.

## 3. Change a Kit Copy

Two steps:

1. A Kit Copy is changed, with its Change Record.
2. The gate of the System Repo's Plan Step decides each Copy Change.

**Step 1. A Kit Copy is changed, with its Change Record.**

- **Options:**
  - a. the Kit Copy is changed when the work shows it does not fit, and its Change Record written with it;
  - b. the Kit Copy is changed ahead, for what the agent foresees;
  - c. the misfit is noted, and the Kit Copy changed at the gate of the System Repo's Plan Step;
  - d. the Kit Copy stays as it is, and the System Repo writes what it does instead in its own records.
- **Chosen:** a. The others:
  - b is a speculation, with nothing that happened behind it;
  - c gains nothing by waiting. A Change Record lets any Copy Change be edited or reversed later. And until the gate, the Kit Copy would say what the System Repo no longer does;
  - d leaves the Kit Copy saying it for good, and the next agent reads the Kit Copy, not the System Repo's records.

  **Weighed and dropped:** a check at each session's end, comparing the Kit Copies with their Change Records. It would run every session, needs an Adapted Case of its own, and never runs when a session stops with no warning. The commit's check and the gate's comparison (step 2) cover what it would find. It comes back if a gate finds a Copy Change committed in an earlier session with its Change Record missing or wrong.
- **Its rules:** the layers document's (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*).
- **Today:**
  - borrowed: an edit comes from something that happened, never a speculation (`delivery/container/.claude/rules/delivered-copies.md`, rule 2; `docs/conventions/exchange/` §5.1, *When a copy may be edited*);
  - borrowed: the rule for changing a copy loads when a copy is touched (`delivery/container/.claude/rules/delivered-copies.md`, its `paths:`);
  - borrowed: the Change Record names which work found the Copy Change, as a Decisions Log entry names the CBC Run's Plan Step (`delivery/container/.claude/rules/delivered-copies.md`, rule 2);
  - changed: today d is required when the need is the CBC Run's own: "never this CBC Run's own answer", and what only it needs goes in its records (`docs/conventions/exchange/` §5.1). So today forbids an edit for the System Repo's own reason. Here the System Repo makes it; what becomes of it at the Update Take is not ruled (§2, *Known, not ruled*);
  - changed: today nothing is written into a copy but the edit, since "a file says how to use it, never its own history", and the why goes in the Decisions Log (`docs/conventions/exchange/` §5.1). Here the why goes in the Kit Copy's Adapted Understanding Text, which is not read while working;
  - changed: today every edit must claim to be for any CBC Run. Here the System Repo proposes, and the Maintainer Repo judges;
  - borrowed: a check fires at the commit because, before, it had to be remembered (`.claude/rules/foundation-check.md`, its header comment). That one is the Maintainer Repo's own.

**Step 2. The gate of the System Repo's Plan Step decides each Copy Change.**

- **Options:**
  - a. the gate looks at the step's Copy Changes together: the comparison, a decision on each, and the links;
  - b. the gate only checks that each Copy Change has a Change Record that says it, and decides nothing;
  - c. the gate does nothing with Kit Copies: the Maintainer Repo reviews the Copy Changes when it reads them;
  - d. the gate writes one line per changed Kit Copy, asking the Maintainer Repo to read it.
- **Chosen:** a. The others:
  - b keeps a Copy Change made early in the step, though the end of the step may show it wrong, and leaves Copy Changes with one reason unlinked;
  - c leaves the review to the side that cannot see what happened, and a wrong Copy Change then reaches the Maintainer Repo's judging;
  - d adds nothing to the Change Records: Read Copy Changes compares every Kit Copy, and reads the Change Records. It comes back if Read Copy Changes misses a changed Kit Copy because nothing asked it to look.
- **Its rules:** the layers document's (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*).
- **Today:**
  - borrowed: the gate is a list of outcomes checked at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: each Approach on Trial the CBC Run's Plan Step used has its dated note at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). A Change Record checked at the gate is the same shape;
  - changed: today the close writes one CBC Run Ask per edited copy (`delivery/container/.claude/rules/delivered-copies.md`, rule 4), option d. Here the Change Records are what Read Copy Changes reads;
  - changed: today nothing at the close looks at the step's changes to copies together.

## 4. Read Copy Changes

Four steps:

1. The stretch of work ends, and the Maintainer Repo is told.
2. The Maintainer Repo finds the two snapshots it compares.
3. It compares the Kit Copies, and reads each Change Record.
4. It lists what changed, nothing judged.

**Snapshots.** Read Copy Changes compares two snapshots of the System Repo, the older snapshot and the stop, and never walks its commits. The *settled snapshot* is the one already taken into account: read, judged and acted on (`temp/common-ground/common-ground-problem.md`, *Defined Terms*). It holds the Kit Version the System Repo had recorded by then (§8, step 1, *At the Update Take, in order*, item 4), which may be behind the newest. So the last Kit Version the Maintainer Repo has seen the System Repo on is read from it, never stored anywhere else. Main's latest snapshot is the one checked, and becomes the stop. The commits between them are history, opened only to understand something deeper. The *version snapshot* an Update Take leaves is the one special point, used only by the first Look for Lessons after that Update Take (step 2, *The first Look for Lessons after an Update Take*).

**Step 1. The stretch of work ends, and the Maintainer Repo is told.**

- **What must happen:** a stretch of work ends where a Look for Lessons can stop, and the Maintainer Repo learns that the System Repo has work it has not taken into account. The human decides which System Repo gets a Look for Lessons, and when.
- **Options,** for where a stretch ends:
  - a. at any commit, the System Repo's latest;
  - b. at the gate where one of the System Repo's Plan Steps closed, the last one on main.
- **Options,** for how the Maintainer Repo learns:
  - c. the human tells it, and its Repo Register is marked by hand;
  - d. the human names a System Repo, and the agent compares its main with its *settled snapshot*. Every System Repo's main is compared with its *settled snapshot* when the human asks which have new work;
  - e. only when work resumes in the System Repo, by the fixed order: a Look for Lessons, then the Kit Update.
- **Chosen:** b and d. The others:
  - a reads Copy Changes the gate has not yet looked at, which the System Repo may still edit or reverse (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*);
  - c depends on the human remembering, and the Repo Register then says a System Repo has nothing new when it has new work (Failure Case 2);
  - e alone gives no Look for Lessons to a System Repo whose work does not resume, so what it learned is lost (Failure Case 1). The Look for Lessons when work resumes still runs, as d: the human names the System Repo to update, which starts a Look for Lessons (§7, step 1, *When one is due*).

  **Where a stretch ends.** Main moves only at a gate's close, so main is always at a closed gate, and nothing on it waits for a gate. Work past it, in a branch or not yet committed, is left for the next Look for Lessons.

  **Two checks at main.** d starts a Look for Lessons at one System Repo (`temp/common-ground/knowledge-layers.md` §3.2, *How a change travels*). It makes two checks, both on whether there are Copy Changes to judge:
  1. **main moved:** the System Repo's main against the *settled snapshot*;
  2. **Copy Changes:** the Kit Copies, compared between the older snapshot and main (step 2, step 3).

  A Look for Lessons ends in one of three cases:

  | Case | Main moved | Kit Copy changed | What follows |
  |---|---|---|---|
  | *not moved* | no | — | nothing new; Act sets the *settled snapshot* to the stop, as it was (§6, step 1) |
  | *no Copy Change* | yes | no | Read Copy Changes finds no Copy Change: nothing is judged, and Act sets the *settled snapshot* to the stop (§6, step 1) |
  | *Copy Change read* | yes | yes | the Copy Changes listed in a Repo Reading, judged and acted on (§5, §6) |

  Check 2 is asked only when main moved, so the first row shows "—".

  A System Repo's open Plan Step changes no case: main stands at the last gate, so the Look for Lessons finds its case by what main holds. The open step's work waits for the next Look for Lessons, and a Kit Update waits for the step's gate (§7, step 1, *When one is due*).

  **No state kept.** d keeps no state of its own: whether a System Repo has work comes from its main and the *settled snapshot*, never from a line someone must keep true.

  **Cleaned history.** If a stretch's history is cleaned before main moves, the Change Records are unharmed: they are in the Kit Copies, not in the commits.
- **Adapted Case:**
  - the System Repo's gate list: main moves only at a gate's close. It is there today;
  - the Maintainer Repo's, for reading a System Repo's Copy Changes. It loads when the human names a System Repo, for its lessons or to update it, or asks which have new work. For this step it says:
    - compare the named System Repo's main with its *settled snapshot*, or every System Repo's when asked;
    - make the two checks; the Look for Lessons ends once Act is done, in one of three cases: *not moved*, *no Copy Change*, *Copy Change read*; when the human named the System Repo to update, the check in Deliver the Kit Update follows.
- **Open:** a System Repo nobody names gets no Look for Lessons until its work resumes. Its trigger: the first lesson found late because a System Repo went without one.
- **Today:**
  - borrowed: a CBC Run's Plan Step reaches main by fast-forward at its close, on the reviewer's word (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: the Maintainer Repo keeps where each System Repo lives (`ARCHITECTURE.md` §2.5, *The CBC Runs*);
  - changed: today the state of the list of CBC Runs, such as "through Release, not yet read", is written by hand (`ARCHITECTURE.md` §2.5). Here it is found by comparison when asked;
  - changed: today a CBC Run Reading runs to the CBC Run's `HEAD`, and names work not yet committed (`.claude/skills/exchange-read/SKILL.md`, Stages 2 and 3). Here a Look for Lessons runs to main, and work past it waits.

**Step 2. The Maintainer Repo finds the two snapshots it compares.**

- **What must happen:** the agent finds the older snapshot, and takes the newer one, the stop, when the Look for Lessons begins. The next Look for Lessons must start where this one stopped, whether a Kit Update follows or not, or at the *version snapshot* of an Update Take since.
- **Options,** for where the last stop is kept:
  - a. in the System Repo, carried there by the next Kit Update;
  - b. in the Repo Register, the *settled snapshot*'s commit beside where each System Repo lives;
  - c. in the Maintainer Repo, as the first line of each Repo Reading, every Repo Reading kept.
- **Chosen:** b. The others:
  - a fails when a Look for Lessons has no Kit Update after it, which step 1 allows, since one may come between two resumptions of work: the System Repo still holds the old stop, and the next Look for Lessons finds again what was judged;
  - c keeps every Repo Reading for good, only for its first line.

  **Where it starts.** The older snapshot is the Repo Register's *settled snapshot*, and it is never empty. At birth, the Maintainer Repo's check of the delivery writes the System Repo's row, with the *settled snapshot* set to the start, the commit holding the Kit Copies as they arrived (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Nothing before the start is the System Repo's own Copy Change, so it stands as taken into account. So every Look for Lessons, the first among them, starts at the *settled snapshot*, and a System Repo with none yet needs no rule of its own. The frozen birth scenario gains this when it resumes (`TODO.md`, the item on resuming the simulation).

  **Where it stops.** The stop is the System Repo's main as it stands when the Look for Lessons begins: its latest snapshot, named by its commit. Everything is compared against that commit, never against main as it moves, so a commit landing during the Look for Lessons falls into the next one. The Repo Reading names its stop. When the list is empty, no Repo Reading is written, and Act sets the *settled snapshot* to the stop.

  **The first Look for Lessons after an Update Take.** It has to start from the *version snapshot*, not the *settled snapshot*. The *settled snapshot* still holds the Kit Copies of the previous Kit Version. Starting there, the Look for Lessons would read the Update Take's changes as the System Repo's. The agent finds the *version snapshot* at main (§8, step 1, *At the Update Take, in order*, item 4). The agent does not check the *version snapshot*'s Kit Copies against the new Kit Version: Deliver the Kit Update and the Update Take check the files three times before (§7, step 2; §8, step 1, items 2 and 6). That check comes back if an Update Take is found to have put a Kit Copy in wrong.

  **When the stop moves.** Act on the verdicts sets the *settled snapshot* to the stop at every Look for Lessons, whether or not a Copy Change was found (§6, step 1). When the verdicts ask for no change, or there are none, that is right after judging. It never moves before: a Look for Lessons left half done must not mark its Copy Changes taken into account. Whether the System Repo takes the Kit Update does not hold it back: by then all between the two snapshots is read, judged and acted on, and what follows waits for the next Look for Lessons. The Repo Reading stays a draft, and goes once its work is done.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo's Copy Changes. For this step it says:
  - the older snapshot is the Repo Register's *settled snapshot*; at the first Look for Lessons after an Update Take, the *version snapshot*;
  - the stop is the System Repo's main as it stands when the Look for Lessons begins, named by its commit; everything is compared against it;
  - Act sets the *settled snapshot* to the stop at every Look for Lessons, once the verdicts, if any, are acted on.
- **Today:**
  - changed: today the stop is written first, as the Repo Reading's first line, before anything is read (`.claude/skills/exchange-read/SKILL.md`, Stage 2). Here it is taken when the Look for Lessons begins, and the Repo Reading names it when it is written;
  - borrowed: the Repo Register keeps where each System Repo lives, as today's list of CBC Runs does (`ARCHITECTURE.md` §2.5, *The CBC Runs*). It gains the *settled snapshot*;
  - borrowed: a CBC Run Reading is a draft in `temp/`, deleted once the work that needed it is done (`temp/README.md`; `.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today the stop, the Read-Through Commit, is kept in the CBC Run, carried there by the next Delivery Note, because "it is the only place the Concept Deliverer can look" (`docs/conventions/exchange/` §2.2, *The CBC Run*). Today every CBC Run Reading is followed by a delivery, so the stop always arrives. Here a Look for Lessons may have no Kit Update after it;
  - changed: today a CBC Run is born with its Read-Through Commit written as *none*, and the exchange-read Agent Skill names no span for it (`delivery/installs/pure-seed.md`, step 2). Here birth writes the start as the *settled snapshot*, and the first Look for Lessons starts there.

**Step 3. The Maintainer Repo compares the Kit Copies, and reads each Change Record.**

- **What must happen:** between the two snapshots, the older one and the stop, the agent finds every Copy Change in the System Kit's folders, a new file among them, and pairs each with its Change Record. It only reads the System Repo, and writes only in the Maintainer Repo.
- **Options,** for how Copy Changes are found:
  - a. each Kit Copy compared between two snapshots of the System Repo's own: the older one and the stop;
  - b. each Kit Copy compared with the Kit Version the Kit Copies came from;
  - c. only the Change Records read, with no comparison;
  - d. the commits between walked one by one.
- **Chosen:** a. The others:
  - b finds the same as a at the first Look for Lessons after birth or an Update Take. After it, a Copy Change already judged differs from that Kit Version until the next Update Take, and is found again at every Look for Lessons before it;
  - c misses a Copy Change with no Change Record, which the commit's check should have stopped, but which can still land (Failure Case 22);
  - d shows every edit on the way, and Copy Changes the gate reversed. The gate has settled those (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*); what stands at the stop is what is read.

  **Pairing.** A Change Record lands in the same diff as its Copy Change, in the Kit Copy's Adapted Understanding Text, so pairing them is reading one diff. Three things can come out:
  - a Copy Change with its Change Record: read with its what, what happened, which work found it, and the System Repo's proposal;
  - a Copy Change with no Change Record: read from the comparison alone, and marked "no entry";
  - a Change Record changed with no Copy Change, as when a why is rewritten: read as a change of its why.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo's Copy Changes. For this step it says:
  - compare each Kit Copy between the older snapshot and the stop; the commits between are history, opened only to understand something deeper;
  - pair each Copy Change with its Change Record; mark one with none "no entry";
  - read a Change Record changed with no Copy Change as a change of its why;
  - judge nothing.
- **Today:**
  - borrowed: every item is read from the copies' diff, the whys, and the lines to the Concept Deliverer (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*; `.claude/skills/exchange-read/SKILL.md`, Stage 3). Here the whys are in the diff, and nothing else is sent to the Maintainer Repo, so it is one: the diff;
  - borrowed: the CBC Run is only read, never written (`.claude/skills/exchange-read/SKILL.md`, *Gates*);
  - changed: today the diff runs against what was delivered, the Receipt Branch or the last delivery entry (`.claude/skills/exchange-read/SKILL.md`, Stage 3). That works because a Delivery Take makes every copy equal its original again. Here a Look for Lessons may come before the Update Take, while a Kit Copy still holds Copy Changes already judged;
  - borrowed: a Receipt Branch holds the delivery as it arrived, and makes the next diff exact (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 4). The *version snapshot* does the same after an Update Take;
  - changed: today the whys are read from the Decisions Log. Here they are read from the Change Records, in the Kit Copies.

**Step 4. It lists what changed, nothing judged.**

- **What must happen:** the Repo Reading gets one line per Copy Change, nothing judged. The list may be empty: then no Repo Reading is written, and Act sets the *settled snapshot* to the stop (step 2). The human checks that the list is whole. Then it is judged, and its stop moves into the Repo Register once its verdicts are acted on (step 2).
- **Options:**
  - a. one line per Copy Change, nothing decided; judging is §5's;
  - b. each Copy Change judged as it is listed;
  - c. only the Copy Changes the System Repo proposed as any repo's are listed;
  - d. one line per Kit Copy, its Copy Changes summed.
- **Chosen:** a. The others:
  - b judges before the whole list is seen, so Copy Changes with one reason are judged apart, and each verdict tends to follow the System Repo's proposal (Failure Case 20). Listing is cheap and judging is not, so the list is checked whole first;
  - c takes the proposal for the verdict, and a lesson for every repo stays in one System Repo (Failure Case 20);
  - d merges two Copy Changes to one Kit Copy, and one of their reasons is lost.

  **What a line holds.** A line holds what step 3 found: the Kit Copy and its part, what it says now, what happened, which work found it, and the System Repo's proposal, marked as one. A Copy Change with no Change Record says "no entry". Copy Changes linked by one reason are listed together, under it.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo's Copy Changes. For this step it says:
  - one line per Copy Change, nothing judged;
  - linked Copy Changes listed together, under their reason;
  - a line holds what step 3 found, the proposal marked as one;
  - the human checks the list is whole; the stop moves into the Repo Register once the verdicts are acted on.
- **Today:**
  - borrowed: one line per item, what it is and where, nothing decided (`.claude/skills/exchange-read/SKILL.md`, Stage 4 and *Gates*);
  - borrowed: the Repo Reading is a draft to its form (`.claude/rules/exchange-reading.md`);
  - changed: today a line is one per edit, per CBC Run Ask and per finding, read from three places (`.claude/skills/exchange-read/SKILL.md`, Stage 3). Here a line is one per Copy Change, with its Change Record;
  - changed: today the proposal is not asked for: every edit must claim to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each line carries it, as input to judging.

## 5. Judge Copy Changes

§5 to §8 are simulated first for depth b, the System Kit's Adapted Case changing: the shortest path into the System Kit through every step. Depth c, the idea above changing, at either layer, is then checked against them (§2, the "how deep" rows). Known before it was simulated:

- the four questions decide, in order, the cheapest first, and the System Repo's own view of its Copy Change is input, never the verdict:
  1. Did the Kit Copy already say this? Then it is a misreading (Failure Case 7). Nothing changes but, perhaps, the System Kit's wording.
  2. Is it specific to that System Repo's problem? Then nothing changes here (§2, *Known, not ruled*).
  3. Does the idea above already hold it, the Work Domain Idea above the Adapted Case, or the Backbone Idea above that? Then the Adapted Case it came from lost it in narrowing, and is fixed from the idea above. When only the Backbone Idea holds it, the Work Domain Idea lost it too, and is fixed first.
  4. How high is it true? 4a, still true naming no Adapted Case: a lesson for its Work Domain Idea. 4b, still true naming no Work Domain: a lesson for its Backbone Idea.

  If none holds, it is a lesson for its Adapted Case: the Adapted Case it came from gains it, and the idea above stays as it is;
- the depth comes from the reason, never the edit. A cap raised from 50 to 60 is the System Repo's own, depth a, when its reason is "our scope names are long". The same edit is a lesson for its Work Domain Idea, depth c at layer 2, when its reason is "the cap counts the scope, which any repo with scopes meets". Only the recorded reason tells them apart;
- what the System Repo gets reaches it with the next Kit Update (§7, step 1).

Two steps:

1. The list is judged.
2. The verdict is written.

**Step 1. The list is judged.**

- **What must happen:** each line of the Repo Reading is first judged sound or not. A sound line is then judged by the four questions, in order, the cheapest first, until one holds (above). The agent proposes an answer to each, with what it read; the human decides. For depth b, none of the four holds: it is a lesson for its Adapted Case. An empty list gives no verdicts, and Judge Copy Changes hands Act only the stop.
- **Options,** for who judges:
  - a. the agent proposes each answer, with what it read, and the human decides each line;
  - b. the agent judges, and the human looks only at the lines where the agent disagrees with the System Repo's proposal;
  - c. the human judges alone.
- **Options,** for a line marked "no entry":
  - d. judged from the comparison alone;
  - e. held, until the human brings its why from the System Repo;
  - f. its why looked for in the System Repo first, in the commit that made the Copy Change and in the System Repo's records, then asked of the human. The line says where its why was found, and is held while neither gives it.
- **Chosen:** a and f. The others:
  - b lets the agent's agreement with the proposal pass unchecked: two views agreeing is not a verdict (Failure Case 20);
  - c leaves the human to read every text the questions need, which the agent reads faster, and with nothing written down to check;
  - d judges on a guess at the why (Failure Case 22);
  - e asks the human for what the System Repo may already have written.

  **What each question reads:**
  - question 0, the Copy Change is sound: what happened, the Copy Change, and the original part. Does it fix what happened, without breaking something the Kit Copy did? An unsound Copy Change goes no further: the depth questions are not asked, and the verdict says why. What becomes of the Copy Change is not ruled (§2, *Known, not ruled*);
  - question 1, the Kit Copy already said it: the original part, in the Kit Version the Kit Copies came from, beside the Copy Change. When the System Kit has moved since, its part as it is now is read too: a change the System Kit has since made the same way is covered, and nothing new is made, so one lesson is not made twice;
  - question 2, specific to that System Repo's problem: what happened, the System Repo's proposal, and its framing of its problem;
  - question 3, the idea above already holds it: the Work Domain Idea above the Adapted Case, then the Backbone Idea above that. When only the Backbone Idea holds it, the Work Domain Idea lost it too, and the loss sits at layer 2. A part lost in narrowing has no mark, and one left out on purpose has its mark, so the two are told apart (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, its **Rules**, *Narrowing, never shrinking*);
  - question 4, how high the lesson is true, since it goes as high as it is true (`temp/common-ground/knowledge-layers-general.md` §3.1, *How the layers fill*): 4a, still true naming no Adapted Case, for its Work Domain Idea, layer 2; 4b, still true naming no Work Domain, for its Backbone Idea, layer 1 (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, its **Rules**). When 4a does not hold, it is a lesson for its Adapted Case, depth b. Depth c's step, checked later.

  **Lines together, lines split.** Lines listed together under one reason are judged together, and the reason is judged once. A line whose parts answer differently is split, each part judged on its own; the parts keep their one Change Record.

  **Not from the wording.** A question is answered from what the Copy Change does and why, never from its wording. The System Repo writes in its own words on purpose (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*), and making a lesson general is rewording, after judging (§6, step 1). A Copy Change worded for one project may still be a lesson for every repo. The agent's answer to question 2 says whether it agrees with the System Repo's proposal, and why if not.
- **Adapted Case:** the Maintainer Repo's, for judging a Repo Reading. It loads when the human starts judging a Repo Reading whose list was checked whole. For this step it says:
  - question 0 first: does the Copy Change fix what happened, without breaking something the Kit Copy did? An unsound Copy Change goes no further, and its verdict says why;
  - then the four questions, in order, until one holds; for each, what it reads;
  - a line whose parts answer differently is split, each part judged on its own;
  - a question is answered from what the Copy Change does and why, never from its wording;
  - the agent proposes each answer with what it read; the human decides;
  - lines under one reason are judged together;
  - a line with no Change Record: its why is looked for in the System Repo's commits and records, then asked of the human; the line says where its why was found, and is held while neither gives it.
- **Open:**
  - how question 4 is answered, and by whom. A first guess, not a rule: 4a first, and 4b only if 4a holds. 4a is the cheaper check, inside one Work Domain, and a lesson still true naming no Work Domain is true across its own. Its trigger: depth c is checked against these steps, or the first lesson judged at layer 1;
  - which other texts are checked for a loss question 3 finds. Nothing comes down the arrow *adapt*, since the idea above did not change (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 6). A first guess: the texts built on the idea that holds the part, as the survey asks (§6, step 1). If several lost it, the idea's wording may be too weak, and is reworded clearer, never narrower. Its trigger: the first depth-d verdict.
- **Today:**
  - borrowed: the four questions, from the rules on deciding written in the problem file before this simulation. They leave how each is answered, and by whom, open; step 1 answers it for questions 1 to 3;
  - borrowed: a change may be declined as "not worth the change" (`docs/conventions/exchange/` §6.5, *Verdicts*). Question 0 asks it first, for every depth;
  - changed: the four questions gain question 0, and a line may be split into parts. The rules on deciding had neither;
  - borrowed: a verdict that cannot be reached yet is held, with its trigger and a line so it is not lost (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today a verdict says whether the Concept Deliverer takes a hunk: taken, declined or held (`docs/conventions/exchange/` §6.5). Here it says how deep the Copy Change goes. Depth b is near today's taken: the Copy Change enters the System Kit.

**Step 2. The verdict is written.**

- **What must happen:** each judged line, or part of one, gets a verdict, the agent drafting and the human deciding. It is the Maintainer Repo's decision, written for its own work: what it changes, in the System Kit or the idea above, starts from it (§6, step 1). No verdict goes down to the System Repo (§2, *Known, not ruled*). For depth b: a lesson for its Adapted Case. The proposal holds when the System Repo gave it as one any repo would meet.
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
  - covered by a System Kit change since the System Repo's Kit Version, question 1;
  - its own, question 2, depth a;
  - lost in narrowing, question 3, depth d;
  - a lesson for its Work Domain Idea, question 4a, depth c at layer 2;
  - a lesson for its Backbone Idea, question 4b, depth c at layer 1;
  - a lesson for its Adapted Case, depth b;
  - held, with its trigger.

  Lines under one reason share one verdict, and each line says how its own Kit Copy is affected.

  **The agreement.** The agreement is said in one line, "the proposal holds" or "the proposal does not hold, because …". An unsound verdict says what the Copy Change breaks or leaves unfixed; what becomes of the Copy Change is not ruled (§2, *Known, not ruled*).
- **Adapted Case:** the Maintainer Repo's, for judging a Repo Reading. For this step it says:
  - one verdict per line or part: its answer, its why, and whether the proposal holds;
  - the answer is one of the nine verdicts listed above; an unsound one says what the Copy Change breaks or leaves unfixed;
  - lines under one reason share a verdict, each saying how its own Kit Copy is affected.
- **Open:** whether an unsound verdict offers a fix. Its trigger: the first unsound verdict.
- **Today:**
  - borrowed: a verdict carries its why (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today every verdict goes down in the Delivery Note (`docs/conventions/exchange/` §6.5). Here the verdict is the Maintainer Repo's, and none goes down (§2, *Known, not ruled*);
  - changed: today a verdict is taken, declined or held (`docs/conventions/exchange/` §6.5). Here it is a depth, or unsound, misread, covered or held;
  - changed: today no verdict answers a proposal, since every edit claims to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each says whether the proposal holds.

## 6. Act on the verdicts

**Step 1. The Maintainer Repo makes its changes. For depth b, the System Kit's Adapted Case.**

- **What must happen:** from each verdict, the Maintainer Repo makes what its depth asks, the agent drafting and the human deciding. For depth b, the System Kit's Adapted Case gains the lesson, worded for every System Repo, and is committed in the Maintainer Repo: the System Kit stands at a new Kit Version. The System Repo the lesson came from gets it back with the next Kit Update, though its Kit Copy already holds the Copy Change in its own words (§7, step 1). The Repo Reading then goes: nothing in the Kit Update is read from it (§7, step 1, *What it is*). Once the verdicts are acted on here, Act sets the *settled snapshot* to the stop, in the Repo Register (§4, step 2). It does so at every Look for Lessons: with no verdicts, as in cases *not moved* and *no Copy Change*, that is all it does (§4, step 1, *Two checks at main*).
- **Options,** for depth b:
  - a. the lesson is reworded for every System Repo, and the System Kit's Adapted Case gains it;
  - b. the Copy Change goes into the System Kit's Adapted Case as the System Repo wrote it;
  - c. the lesson waits until a second System Repo makes the same Copy Change.
- **Chosen:** a. The others:
  - b carries one project's words to every System Repo, since the System Repo writes what happened in its own words, on purpose (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*);
  - c waits for a second proof of what judging already found: question 2 found the Copy Change is not that System Repo's own.

  **The other depths.** For the other depths, this step holds the work, each checked here later:
  - depth c changes the idea above at its layer, after the survey: its Work Domain Idea at layer 2, its Backbone Idea at layer 1;
  - depth d fixes the Adapted Case from the idea above, after fixing the Work Domain Idea from its Backbone Idea when the loss sits at layer 2;
  - depth e marks a narrowing with its why, in the text just below the idea that does not fit.

  **The survey.** Before a lesson enters the idea above, every other text built on that idea is asked whether it fits, the one the lesson came from excepted (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, its **Rules**; §2.3, *The Adapted Case layer*). At layer 2, that is the other Adapted Cases of that Work Domain Idea, the Maintainer Repo's own only when they share it. At layer 1, it is every Work Domain Idea on that Backbone Idea. It is the arrow *adapt*'s check, run before the idea changes, so a conflict shows first. Each text answers "holds as it is", "must change", with what and why, or "conflicts", with why. A conflict is input to the human's decision, never a veto, and what the survey finds must change, changes. Its answers are also evidence for question 4: if every answer conflicts, the lesson is not true that high.

  A lesson is reworded here, never before: for every System Repo at depth b; at depth c, naming no Adapted Case at layer 2, and no Work Domain at layer 1 (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, its **Rules**).
- **Adapted Case:** the Maintainer Repo's, for judging a Repo Reading. For this step it says:
  - a lesson for its Adapted Case is reworded for every System Repo, and the System Kit's Adapted Case gains it;
  - the Repo Reading goes once its verdicts are acted on;
  - once the verdicts are acted on, or when there are none, the *settled snapshot* is set to the stop, in the Repo Register.
- **Open:**
  - at layer 1, how far down the survey reaches before the change: only the Work Domain Ideas, each checking its own Adapted Cases when it changes, or every Adapted Case below them at once. The first is cheaper; the second may catch a conflict two layers down. Its trigger: the first lesson judged at layer 1;
  - how a part of a Backbone Idea is known not to fit a whole Work Domain, when one System Repo's Copy Change shows one Adapted Case. A first guess: the same survey, over that Work Domain Idea's Adapted Cases. Its trigger: the first depth-e verdict;
  - whether a Look for Lessons is one of the Maintainer Repo's Plan Steps, and whether Act gets an Adapted Case of its own, apart from the one for Judge Copy Changes. Today a CBC Run Reading is one of the Concept Deliverer's Plan Steps, and its work follows it. Its trigger: the Adapted Case texts written from these rules.
- **Today:**
  - borrowed: a taken change is committed here, and the next delivery carries it (`docs/conventions/exchange/` §6.5, *Verdicts*). It is depth b's path, and the other depths'.

## 7. Deliver the Kit Update

Two steps:

1. The Kit Update is made: the System Kit at its newest Kit Version.
2. The Kit Update is delivered.

**Step 1. The Kit Update is made: the System Kit at its newest Kit Version.**

- **What must happen:** when work resumes in the System Repo, after a Look for Lessons, the Maintainer Repo makes its Kit Update, the agent drafting and the human deciding (§8, step 1, *Before the Update Take*). A Kit Update is due when the System Kit has moved past the Kit Version the System Repo's Kit Copies came from. It reaches the System Repo on the human's word, in a step of its own: nothing crosses without that word, and the agent may carry it. For depth b, the System Kit has moved for this Copy Change, so a Kit Update is due: it carries the System Kit's Adapted Case at the new Kit Version, with the lesson as its why.
- **Options,** for when a Kit Update goes:
  - a. after every Look for Lessons, even with nothing to carry;
  - b. only when it carries a System Kit change.
- **Options,** for when the check in Deliver the Kit Update runs:
  - c. after Act, at every Look for Lessons;
  - d. only when the human names the System Repo to update, after the Look for Lessons that starts.
- **Chosen:** b and d. The others:
  - a sends an empty Kit Update to carry where the Look for Lessons stopped. The *settled snapshot* is in the Repo Register now (§4, step 2), so nothing needs carrying;
  - c answers, at a Look for Lessons, a question nothing acts on: nothing is made until work resumes, and the System Kit may move again before then.

  **When one is due.** A Kit Update is due when the System Repo's Kit Version, which it holds, is behind the newest. It is found by comparison, as §4, step 1 finds new work. Two Kit Versions are compared by the System Kit's files at their two commits, never by the commits themselves: a Maintainer Repo commit that touches no System Kit file leaves every System Repo where it was. A System Repo cannot see the Maintainer Repo, so it cannot learn this itself.

  The check runs only when work resumes. Work resumes when the human, about to open the System Repo's next Plan Step, names it to update; neither repo can see that moment itself (§8, step 1, *Before the Update Take*). Nothing is made for, or sent to, a System Repo whose work has not resumed. Then, in order:
  1. a Look for Lessons runs (§4, step 1). It comes first: a Kit Update is built against the *settled snapshot*, and a Copy Change not yet taken into account would make the Update Take refuse it;
  2. the Kit Versions are compared. When the System Repo's is the newest, nothing follows;
  3. the agent checks that none of the System Repo's Plan Steps is open. If one is, it says so, and makes nothing: finishing that step would move main, and the Update Take would refuse the Kit Update too (§8, step 1, *Before the Update Take*);
  4. the Kit Update is made.

  When the human only asks which System Repos are behind, the Kit Versions are compared, and nothing is made.

  **What it is.** A Kit Update is two things: every Kit Copy, whole, at the newest Kit Version, and an Update Note. The System Repo then has the new version of each file, and finds its old one in its own history (§8, step 1). The Update Note holds:
  - the new Kit Version;
  - the System Repo's *settled snapshot* it was built against, whether a Repo Reading was written or not. The Update Take checks it before anything moves (§8, step 1). The Update Note names the check, so a System Repo whose Adapted Case for taking is older still meets it;
  - what changed since the System Repo's Kit Version, from the same comparison of files: each path changed, new, gone or renamed, and how many. The System Repo checks the files against it when they arrive, and a file that is gone cannot say so itself;
  - the why of each System Kit change since then, whatever its source: a Look for Lessons at this System Repo or at another, or the Maintainer Repo's own work. It is read from the bodies of the Maintainer Repo's commits that changed a System Kit file between the two Kit Versions, since a body says why (`docs/conventions/commit-messages/` §1, *What a commit message is*). Each why stands on its own, and names no other repo; a change that comes from a lesson, at any depth, quotes the lesson as Act reworded it (§6, step 1). With it, the System Repo judges a change against its own needs without seeing the Maintainer Repo;
  - which files are taken first: the Adapted Case for taking a Kit Update, so a Kit Update is never taken by instructions older than it (§8, step 1, *At the Update Take, in order*, item 1; Failure Case 10);
  - the Kit Update it replaces, when one was waiting.

  **What the Update Note is not.** The Update Note is no summary of the Maintainer Repo's work, which the System Repo cannot check. It is not a record either: it goes once the Kit Update is taken, and what the System Repo decides goes in its records.

  **What it cites.** Nothing in it cites what the System Repo cannot open: no path, record or word of the Maintainer Repo's own.

  **One at a time.** A Repo Reading stays open until its verdicts are acted on. One Repo Reading is open per System Repo at a time: a Repo Reading made while one is open extends it, and its lines are judged with the rest, so judging already done is kept. One Kit Update waits for the System Repo at a time: a newer one replaces one not yet taken, since it carries every System Kit change since the Kit Copies' Kit Version.
- **Adapted Case:** the Maintainer Repo's, for making a Kit Update. It loads on the human's word to update a System Repo. For this step it says:
  - it follows the System Repo's Look for Lessons, never comes before it;
  - it goes only when it carries a System Kit change;
  - it is due when the System Repo's Kit Version is behind the newest; the Kit Versions are compared by the System Kit's files, never by the commits; it is checked only when the human names a System Repo to update, once the Look for Lessons has run; asking which are behind only compares, and makes nothing;
  - before making the Kit Update, check that none of the System Repo's Plan Steps is open; if one is, say so, and make nothing;
  - it carries every Kit Copy whole, at the new Kit Version, and an Update Note holding the six things listed above;
  - it cites nothing the System Repo cannot open;
  - one Repo Reading open per System Repo, a new Repo Reading extending it; one Kit Update waiting, a newer one replacing it.
- **Today:**
  - borrowed: the delivery is staged into the CBC Run's `temp/` on the reviewer's word, the CBC Run's tree checked clean first, and named by the commit it was final at (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: files go whole, every copy at every delivery after birth (`docs/conventions/exchange/` §3.2, *What goes*);
  - borrowed: a delivery goes after a CBC Run Reading, or when something a CBC Run holds has changed in the Concept Deliverer (`.claude/skills/exchange-deliver/SKILL.md`, its description);
  - borrowed: the Delivery Note says what changed since the Delivery Pin, as paths the CBC Run can check, and why it matters to this CBC Run; it never describes the Concept Deliverer's own practice (`docs/conventions/exchange/` §3.7, *The Delivery Note*; `.claude/skills/exchange-deliver/SKILL.md`);
  - borrowed: the Delivery Note carries what is gone (`docs/conventions/exchange/` §3.6, *Absence in a delivery*);
  - borrowed: one CBC Run Reading is open per CBC Run at a time, and a new read extends it (`.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today every read ends with a Delivery Note, even an empty one, to carry the Read-Through Commit (`docs/conventions/exchange/` §6.6). Here a Kit Update goes only when it carries a System Kit change;
  - changed: today the Delivery Note gives a verdict on everything the CBC Run addressed to the Concept Deliverer (`docs/conventions/exchange/` §3.7). Here none goes down (§2, *Known, not ruled*).

**Step 2. The Kit Update is delivered.**

- **What must happen:** on the human's word, the Kit Update is staged into the System Repo's `temp/`, by the human or by the agent. It writes only into the System Repo's `temp/`, nowhere else there. Nothing in `temp/` is in force until the System Repo takes it (§8, step 1).
- **Options,** for checking what was staged:
  - a. a second Adapted Case of the Maintainer Repo's checks it, apart from the one that delivered, as at birth;
  - b. the delivering Adapted Case compares each staged file with the new Kit Version, once staged, and the System Repo checks the Update Note against the files when it takes them;
  - c. only the System Repo's check, at the Update Take.
- **Chosen:** b. The others:
  - a was chosen at birth because the start becomes the base of every Look for Lessons (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Here a wrong file is held in `temp/`, never in force, and a comparison of files leaves little mistake to share. It comes back if a staged file is found, after an Update Take, to differ from the System Kit;
  - c leaves only the System Repo to check, and it cannot open the System Kit, so a staged file that differs from it passes.

  **Before staging.** The System Repo's tree is checked clean first, with no work under way. When it is not, the agent says what it found and waits for the word. A Kit Update already waiting there is replaced by the new one (step 1). The Kit Update is named by the Maintainer Repo's commit at which its files and Update Note were final, so its Kit Version is exact.
- **Adapted Case:** the Maintainer Repo's, for delivering a Kit Update. It loads on the human's word to deliver. For this step it says:
  - never stage unasked; check the System Repo's tree clean first;
  - write only into the System Repo's `temp/`, replacing a Kit Update already waiting;
  - name the Kit Update by the commit it was final at;
  - compare each staged file with the new Kit Version.
- **Today:**
  - borrowed: the delivery and its Delivery Note are copied into the CBC Run's `temp/` on the reviewer's word, by the reviewer or by the agent when told; the agent never stages unasked; the tree is checked clean first; the Delivery Staging is named by the commit at which files and Delivery Note are final (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: one Agent Skill both writes the Delivery Note and stages the delivery (`.claude/skills/exchange-deliver/SKILL.md`). It also compares the staged files here;
  - borrowed: the CBC Run's `temp/` gains exactly the staging and its Delivery Note, and nothing tracked in the CBC Run changes (`.claude/skills/exchange-deliver/SKILL.md`, *Gates*);
  - changed: today the staged files are copied by a script, so they equal the Master Copies by how they are made, and no comparison follows; the CBC Run's Delivery Take checks the Delivery Note against the files (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 1).

## 8. Take the Kit Update

**Step 1. The System Repo takes the Kit Update.**

- **What must happen:** the Kit Update is taken between two of the System Repo's Plan Steps, when the next is about to open, never in the middle of one, the agent proposing and the human deciding. Before that step opens, in a fixed order: a Look for Lessons runs to main, and the System Repo's Kit Update, when one is due, made, delivered and taken. Then the step opens on the new Kit Copies, or on the same ones when no Kit Update was due. The Update Take runs on a branch of its own, and reaches main only at its gate's close.
- **Options,** for when a Kit Update is taken:
  - a. whenever it arrives;
  - b. at the opening of the System Repo's next Plan Step, right after a Look for Lessons that reached main;
  - c. at the opening of the System Repo's next Plan Step, whatever the Look for Lessons reached.
- **Options,** for the System Repo's Change Records at the Update Take:
  - d. kept, since the merge keeps what only the System Repo added;
  - e. all cleared, every Kit Copy taken whole.
- **Options,** for where the Update Take is committed:
  - f. on a branch of its own, one commit per part, a gate last, main moving by fast-forward at the gate's close;
  - g. as the first commit of the System Repo's next Plan Step;
  - h. as the System Repo's Plan Step, for the Update Take alone;
  - i. as one commit on main, the rule that main moves only at a gate's close (§4, step 1, *Where a stretch ends*) narrowed so that only the work of the System Repo's Plan Steps waits for a gate.
- **Chosen:** b, e and f. The others:
  - a lands in the middle of a step, which then runs on two sets of rules;
  - c takes the Kit Update over Copy Changes not yet judged. The Kit Update answered none of them, and clearing their Change Records loses them before they are judged;
  - d keeps Change Records that say how a Kit Copy differed from the old System Kit. After the Update Take some describe nothing, and none says how the Kit Copy differs from the new one;
  - g leaves main on the old Kit Version until the step's gate closes, so naming the System Repo to update in between finds the Kit Update due again;
  - h gives the Update Take an opening, as the System Repo's Plan Steps have, for work the Update Note already orders. f keeps what it needs from one: the gate;
  - i narrows that rule for the Update Take alone. f keeps the rule whole, its gate checking that the Update Take finished.

  **Before the Update Take.** The opening order is fixed: a Look for Lessons, then the Kit Update. An open Repo Reading is extended. The human works on one project at a time, so the System Repo waits at little cost. A System Repo's Plan Step open when the human returns finishes on the old Kit Copies first, and the human names the System Repo to update at the next opening (§7, step 1, *When one is due*). The Update Take checks first, from the Update Note, what the System Repo itself can see:
  - case 1, its main is still the *settled snapshot* the Update Note names: the Kit Update is taken. Its Kit Version needs no check of its own: it is recorded in main, so it cannot change while main stands still;
  - case 2, anything else: there is no Update Take, and the System Repo says so. The human names it to update again, and the Look for Lessons finds that main has moved (§4, step 1, *Two checks at main*). The check in Deliver the Kit Update then finds a new Kit Update due, made against the System Kit as it is now. It replaces the waiting one (§7, step 1).

  **When the System Kit moves on.** The System Kit may move after the Kit Update is made. That is no reason to refuse the Kit Update: it is correct, if not the latest, and the next brings the rest.

  **At the Update Take, in order.** Once the check finds case 1, the Update Take cuts a branch from main, the *settled snapshot*. Its first commit is the Kit Update as it arrived, in `temp/`, not yet in force: a record of what came, before the Update Take changes anything. Each item below is then a commit of its own, but item 2, a check. Main moves to the branch's last commit by fast-forward at the gate's close, so it still moves only at a gate's close (§4, step 1, *Where a stretch ends*).
  1. the Adapted Case for taking a Kit Update is taken first, on its own, so the rest is taken by the new one (Failure Case 10);
  2. the files are checked against the Update Note: what changed, and how many (§7, step 1). A mismatch is said before anything moves;
  3. every Kit Copy is taken whole, at the new Kit Version; each path gone is removed, and each renamed is moved. Every Change Record is cleared: main is the *settled snapshot*, so each was read and judged. A part the System Repo never changed is taken, and work shows whether it fits (`temp/common-ground/knowledge-layers.md` §3.2.1, *Change a Kit Copy*);
  4. the new Kit Version is recorded, with the commit that holds it: item 3's, the *version snapshot*, every Kit Copy at the new Kit Version. So the check in Deliver the Kit Update can compare it with the newest. It names item 3's commit because a commit cannot hold its own hash, and item 3's is the last before it;
  5. the Kit Update and its Update Note are removed from `temp/`;
  6. the Update Take's gate, last. It checks that the Update Take finished: the files matched the Update Note, every Kit Copy is at the new Kit Version, the Kit Version is recorded, and `temp/` holds no Kit Update.

  **What a Change Record stands against.** Every Change Record stands against the last Kit Version taken, or birth's, and every Change Record goes at an Update Take. This is confirmed at the first Kit Update to reach a System Repo whose Kit Copies have Change Records.
- **Adapted Case:** the System Repo's, for taking a Kit Update, itself in the Kit Update and taken first. It loads when the System Repo's next Plan Step opens with a Kit Update waiting. For this step it says:
  - check first that main is still the *settled snapshot*, and take nothing when it differs, saying so;
  - take only at the opening of the System Repo's next Plan Step;
  - take on a branch of its own: first the Kit Update as it arrived, then the items in the order above, one commit each but item 2, a check, the gate last, checking that the Update Take finished; main moves by fast-forward at the gate's close.
- **Open:**
  - finished work done under a rule the Kit Update changed may now be wrong. New work follows the new Kit Copy; the System Repo lists which System Kit changes touch rules its finished work followed, and the human decides. Its trigger: the first Kit Update that changes a rule one of the System Repo's finished Plan Steps followed;
  - postponing an Update Take after its Kit Update is staged, so the step opens on the old Kit Copies and the Kit Update waits. For now there is no such choice: a staged Kit Update is taken at the opening, unless the Update Take's check finds main moved (case 2). Once an Update Take can be postponed, main can move before it, so decide then whether the Maintainer Repo must check main before delivery, and whether main alone is enough: a Plan Step on a branch leaves main where it is. Its trigger: the first staged Kit Update the human does not want taken.
  - dropping or restarting the System Repo's open Plan Step so the Kit Update is taken sooner, when the Kit Update changes a rule the step rests on. Its trigger: the first Kit Update the human wants taken before an open step finishes.
  - whether each opening of the System Repo's Plan Steps asks: was this System Repo named to update? Without that question, a System Repo nobody names opens each step on the old Kit Copies, and falls further behind each time. Its trigger: the first time one of the System Repo's Plan Steps opens on old Kit Copies because nobody named the System Repo to update.
  - where in the System Repo the Kit Version and the *version snapshot*'s hash are written. Today a Delivery Take writes one entry with the new Delivery Pin (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Its trigger: the Adapted Case for taking a Kit Update written from these rules.
- **Today:**
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: the Delivery Take's order: the Delivery Note checked against the staging first, copies taken whole, what is gone removed, one entry with the new Delivery Pin, the staging removed (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, steps 1, 4, 5, 6 and 7);
  - borrowed: a CBC Run's Plan Step reaches main by fast-forward from its branch, at its close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). The Update Take's branch does the same;
  - borrowed: a Receipt Branch may hold the delivery as it arrived (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 4). Here the Kit Update is committed as it arrived, on the Update Take's branch;
  - changed: today, with more than one commit, the Delivery Take's entry goes in the last, where every copy equals the Delivery Pin (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Here the Kit Version names the *version snapshot*, item 3's commit, where the next Look for Lessons starts (§4, step 2, *The first Look for Lessons after an Update Take*);
  - changed: today nothing at the Delivery Take is decided at a gate. Here the Update Take's gate checks that the Update Take finished;
  - borrowed: being behind the Concept Deliverer is acceptable (`delivery/container/.claude/rules/delivered-copies.md`, rule 6). A System Repo not named to update is that;
  - changed: today an edit made after the Read-Through Commit is re-applied on top, its record standing (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 3). Here the opening order leaves no such edit;
  - changed: today a declined edit is gone at the Delivery Take, and never edited back in (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Here what becomes of a Copy Change the System Kit did not take is not ruled (§2, *Known, not ruled*);
  - changed: today work continues on the edited copy when a CBC Run's Plan Step opens before the reply (`delivery/container/.claude/rules/delivered-copies.md`, rule 6). Here the next step waits for the Update Take, once the human has named the System Repo to update.

