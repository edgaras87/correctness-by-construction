# A System Repo's Change, Simulated

<!-- A draft for the Plan Step "Find how what we know stays true",
     stage 1. It simulates one case of temp/common-ground-problem.md,
     *A System Repo's change*, step by step, until that draft's rules
     can be written from it: *Recording and reading* first, then
     *Deciding and updating*. The rules live there, never here. Its
     input: the frozen temp/between-repos-simulation.md, scenarios 2
     and 3. It goes when the Plan Step closes, and git keeps every
     version. -->

This document simulates one case: a System Repo changes both halves of one Adapted Case in its System Kit Copies, and the Maintainer Repo reads the change back. It uses the Common Ground Problem's Defined Terms (`temp/common-ground-problem.md`, *Defined Terms*).

The scope: the two halves are the Instruction Text and its Adapted Understanding Text. The change may have any reason, its own or one any repo would meet. Either half may change first. One stretch of work may hold several such changes. Each step's choice must hold for all of it, so no fixed example is used: a step is tried against the scope's edges.

## 1. How it is worked

Three moves, in order:

1. **Simulate:** each step below says what must happen, what could be done, and what is chosen.
2. **Write the rules:** once all of a half's steps are seen together, its rules are written in `temp/common-ground-problem.md` §2.1, *What passes between the repos*.
3. **Check them:** each step is walked again against the rules. A step a rule does not hold for changes the rule or the step.

Each step has these fields. A field with nothing in it is left out.

- **What must happen:** the outcome, and who acts.
- **Options:** what could be done here, today's way among them.
- **Chosen:** the option taken, and why the others were not.
- **Adapted Case:** which Adapted Case runs the step, whose it is, what loads it, and what it must say for this step. Once a half is done, these are read together: they give the rules, and later the Adapted Case texts.
- **Open:** what the step leaves undecided, each with the trigger that decides it.
- **Today:** what is borrowed from today, and what changes, each with its source.

## 2. The cases

The cases are simulated one at a time. The first is simulated whole; each other case is then checked against it, and what differs is written. A case that grows too complex goes to TODO, to be checked once the Common Ground Problem is finished. The first-half cases are what was changed; the second-half cases are how deep the change goes in the Maintainer Repo (`temp/common-ground-problem.md` §2.1, *A System Repo's change*).

| Half | Case | Status | Differs so far |
|---|---|---|---|
| first | both halves of one Adapted Case | being simulated, §3 | — |
| first | an Instruction Text only | not yet checked | recorded: says whether its Adapted Understanding Text still matches (Failure Case 8) |
| first | an Adapted Understanding Text only | not yet checked | recorded: says whether its Instruction Texts still match (Failure Case 8) |
| first | a Defined Term | not yet checked | — |
| first | delivered Knowledge on Trial | not yet checked | read: compared like any copy; decided: the original was never proven, so the change is evidence for its trial |
| first | new text of the System Repo's own, on trial | not yet checked | read: written in the System Kit's on-trial folder, so the comparison finds it as a new file; decided: with no original, the first question does not apply |
| first | a copy no longer used | not yet checked | read: nothing in the file changes, so only a mark shows it |
| first | one reason behind changes to several Adapted Cases | not yet checked | recorded: one why, naming every copy it changed; read: the changes are listed together |
| first | a note with no change | not yet checked | read: a line of its own, from the notes' place, with no copy's diff; decided: questions 1 to 4 fit a doubt about a line, not a lack or an unused copy |
| second | a. it stays in the System Repo | not yet checked | — |
| second | b. the System Kit's Adapted Case changes | not yet checked | the update brings it to this System Repo too, whose copy already has it |
| second | c. the project-agnostic text changes | not yet checked | the other Adapted Cases are surveyed, the Maintainer Repo's own among them |
| second | d. the project-agnostic text already holds it | not yet checked | question 3 checks only the Maintainer Repo's own Adapted Case for the same loss, though every Adapted Case on that idea may have lost it; if several did, the project-agnostic wording may be too weak, and is reworded clearer, never narrower |
| second | e. it asks to narrow the project-agnostic text | not yet checked | the narrowing goes into the Adapted Case, marked with its why (`temp/common-ground-problem.md` §2.1, *Narrowing, never shrinking*) |
| second | f. several Adapted Cases need it, but not all | not yet checked | it cannot enter the project-agnostic text, so each Adapted Case gains it, and the same text has no shared home. Open; its trigger: the first change two Adapted Cases need, but not every one |

A stretch of work may hold several changes, alike or mixed. Each is recorded and read on its own, so they add no row but one: one reason behind changes to several Adapted Cases.

## 3. The first half, recorded and read

Six steps:

1. The work meets a copy that does not fit, and the copy is changed, with its entry.
2. The Plan Step's gate: the step's changes are compared with their entries, and each is kept, edited or reversed, and linked when they share a reason.
3. The stretch of work ends, and the Maintainer Repo is told.
4. The Maintainer Repo finds where to start reading.
5. It compares the copies, and reads each entry.
6. It lists what changed, nothing judged.

**Step 1. The work meets a copy that does not fit, and the copy is changed, with its entry.**

- **What must happen:** during its own work, the System Repo finds that a System Kit Copy does not fit what happened. The human decides the change, the agent proposing. The change is made then, and its entry is written with it. Either may be edited or reversed later, the entry with the change.
- **Options:**
  - a. the copy is changed when the work shows it does not fit, and its entry written with it;
  - b. the copy is changed ahead, for what the agent foresees;
  - c. the misfit is noted, and the copy changed at the Plan Step's gate;
  - d. the copy stays as it is, and the System Repo writes what it does instead in its own records.
- **Chosen:** a. The others:
  - b is a speculation, with nothing that happened behind it;
  - c waits for no reason: an entry lets any change be edited or reversed later, and until the gate the copy says what the System Repo no longer does;
  - d leaves the copy saying it for good, and the next agent reads the copy, not the records.

  The entry goes in a footer of the copy's Adapted Understanding Text, which is not loaded for work. So the change and its why land in one diff, and the why cannot lose its copy. An Instruction Text changed alone has its entry there too. The entry holds:
  - what changed, by meaning: the part, and what it says now;
  - what happened, concretely, in the System Repo's own words. It is never written to sound project-agnostic: making it general is the Maintainer Repo's, after judging;
  - which work found it;
  - the System Repo's proposal: its own problem, or one any repo would meet. It is marked as a proposal. The Maintainer Repo judges every change, and says whether it agrees, and why if not (§4).

  The entry says the change as it stands. A later edit rewrites it, and git keeps the old one.

  The change and its entry go in the same commit. A commit that changes a copy and not its entry is stopped there. The commit is always reached: work never committed is lost, change and entry together.

  Weighed and dropped: a check at each session's end, comparing the copies with their entries. It would run every session, needs an Adapted Case of its own, and never runs when a session stops with no warning. The commit's check and the gate's comparison (step 2) cover what it would find. It comes back if a gate finds an entry missing or wrong whose change was committed in an earlier session.
- **Adapted Case:** the System Repo's, for changing a System Kit Copy, itself a System Kit Copy. It loads when a copy, or the notes' place, is touched. For this step it says:
  - a copy changes only when the work shows it does not fit, never ahead;
  - the entry is written with the change, with its four parts, and goes in the same commit;
  - what happened is written concretely, in the System Repo's own words;
  - whether the change is its own or any repo's is a proposal, never a verdict;
  - a note, written at any time, carries only what has no change; one about a change points at its entry, and never retells it (step 2).
- **Open:** which moment of the System Kit an entry is written against, and whether an entry goes once an update takes its change in. Before the first update, every entry stands against the moment the copies arrived. Its trigger: the first update to reach a System Repo whose copies have entries.
- **Today:**
  - borrowed: an edit comes from something that happened, never a speculation (`delivery/container/.claude/rules/delivered-copies.md`, rule 2; `docs/conventions/exchange/` §5.1, *When a copy may be edited*);
  - borrowed: the rule for changing a copy loads when a copy is touched (`delivery/container/.claude/rules/delivered-copies.md`, its `paths:`);
  - changed: today its paths do not hold `TODO.md`, where *To the deliverer* is. Here the notes' place loads it too;
  - borrowed: the entry names which work found the change, as a Decisions Log entry names its Plan Step (`delivery/container/.claude/rules/delivered-copies.md`, rule 2);
  - changed: today d is required when the need is the CBC Run's own: "never this CBC Run's own answer", and what only it needs goes in its records (`docs/conventions/exchange/` §5.1). So today forbids an edit for the System Repo's own reason. Here the copy keeps it (`temp/common-ground-problem.md` §2.1, *An update*);
  - changed: today nothing is written into a copy but the edit, since "a file says how to use it, never its own history", and the why goes in the Decisions Log (`docs/conventions/exchange/` §5.1). Here the why goes in the copy's Adapted Understanding Text, which is not read while working;
  - changed: today every edit must claim to be for any CBC Run. Here the System Repo proposes, and the Maintainer Repo judges;
  - borrowed: a check fires at the commit because, before, it had to be remembered (`.claude/rules/foundation-check.md`, its header comment). That one is the Maintainer Repo's own.

**Step 2. The Plan Step's gate: the step's changes are compared with their entries, and each is kept, edited or reversed, and linked when they share a reason.**

- **What must happen:** at the Plan Step's close, the step's changes to copies are seen together, now that the whole step is seen. The agent compares the copies against where the Plan Step began, and shows each change with its entry. The human decides each, the agent proposing: kept, edited, or reversed, its entry with it. Changes that share one reason are linked.
- **Options:**
  - a. the gate looks at the step's changes together: the comparison, a decision on each, and the links;
  - b. the gate only checks that each change has an entry that says it, and decides nothing;
  - c. the gate does nothing with copies: the Maintainer Repo reviews the changes when it reads them;
  - d. the gate writes one line per changed copy, asking the Maintainer Repo to read it.
- **Chosen:** a. The others:
  - b keeps a change made early in the step, though the end of the step may show it wrong, and leaves changes with one reason unlinked;
  - c leaves the review to the side that cannot see what happened, and a wrong change then reaches the Maintainer Repo's judging;
  - d adds nothing to the entries: reading compares every copy, and reads the entries. It comes back if a reading misses a changed copy because nothing asked it to look.

  A change kept as it is needs nothing more. A change edited gets its entry rewritten. When changes share one reason, the reason is written in full in one entry, and each other entry says how its own copy was affected and points at that one. If the entry holding the reason is reversed, the reason moves to one that stays, and the others point there.

  The gate also asks once: did an Adapted Case used in this step not fit, with no change made? A misfit worked around without a change leaves nothing for the comparison to find. The human, who saw every session of the step, answers. Each misfit named is written as a note for the Maintainer Repo.

  A note carries what has no change to carry it: a misfit with no change made, a doubt about a line left as it is, something the System Kit lacked, a copy no longer used, or anything the human wants the Maintainer Repo to check. It may be written at any time, not only at the gate. Notes are kept in one known place in the System Repo's records. A note never lists a change: the entry already says it, and a second line would have to follow every edit and reversal. A note about a change points at its entry, and never retells it. Reading reads the notes as well as the copies (step 5).
- **Adapted Case:** the System Repo's, for closing a Plan Step, its gate list. It loads when the Plan Step closes. For this step it says:
  - compare the copies against where the Plan Step began, and check each change has an entry that says it;
  - the human decides each change: kept, edited or reversed, its entry with it;
  - changes with one reason are linked, and the reason never stays only in a reversed entry;
  - ask once whether an Adapted Case did not fit, with no change made, and write each as a note.
- **Open:** whether a reversed change leaves a trace for the Maintainer Repo. A change tried and undone may be evidence that the System Kit Copy was right. Its trigger: the first change reversed at a gate.
- **Today:**
  - borrowed: the gate is a list of outcomes checked at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: each Approach on Trial the Plan Step used has its dated note at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). An entry checked at the gate is the same shape;
  - borrowed: a line the CBC Run disagrees with is quoted under *To the deliverer*, and a copy it does not use gets a CBC Run Ask there (`delivery/container/.claude/rules/delivered-copies.md`, rule 1). Notes can go under that heading;
  - changed: today the close writes one CBC Run Ask per edited copy (`delivery/container/.claude/rules/delivered-copies.md`, rule 4), option d. Here the entries are what reading reads;
  - changed: today nothing at the close looks at the step's changes to copies together.

**Step 3. The stretch of work ends, and the Maintainer Repo is told.**

- **What must happen:** a stretch of work ends where reading can stop, and the Maintainer Repo learns that the System Repo has work it has not read. The human decides which System Repo is read, and when.
- **Options,** for where a stretch ends:
  - a. at any commit, the System Repo's latest;
  - b. at a closed Plan Step's gate, the last one on main.
- **Options,** for how the Maintainer Repo learns:
  - c. the human tells it, and its register is marked by hand;
  - d. the human names a System Repo, and the agent compares its main with where its last reading stopped. Every System Repo is compared when the human asks what to read;
  - e. only when work resumes in the System Repo, by the fixed order: reading back, judging, then the update.
- **Chosen:** b and d. The others:
  - a reads changes the gate has not yet looked at, which the System Repo may still edit or reverse (step 2);
  - c depends on the human remembering, and the register then says a System Repo was read when it has new work (Failure Case 2);
  - e alone never reads a System Repo whose work does not resume, so what it learned is lost (Failure Case 1). It stands as it is, for every System Repo (`temp/common-ground-problem.md` §2.1, *An update*), and d adds the reading between.

  Main moves only at a gate's close, so main is always at a closed gate, and nothing on it waits for a gate. Work past it, in a branch or not yet committed, is left for the next reading.

  A look at work past main may be asked for, as when a change is in doubt before its gate. It is not a reading: it does not move where the last reading stopped, judges nothing, and gives only notes, for the human and for the System Repo's gate. The work is read when it reaches main.

  d keeps no state of its own: whether a System Repo has work comes from its main and the last reading's stop, never from a line someone must keep true.

  If a stretch's history is cleaned before main moves, the entries are unharmed: they are in the copies, not in the commits.
- **Adapted Case:**
  - the System Repo's gate list: main moves only at a gate's close. It is there today;
  - the Maintainer Repo's, for reading a System Repo. It loads when the human names a System Repo to read, or asks what to read. For this step it says: compare the named System Repo's main with where its last reading stopped, or every System Repo's when asked; a look past main moves nothing, and gives only notes.
- **Open:** a System Repo nobody names is not read until its work resumes. Its trigger: the first lesson found late because a System Repo went unread.
- **Today:**
  - borrowed: a Plan Step reaches main by fast-forward at its close, on the reviewer's word (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: the Maintainer Repo keeps where each System Repo lives (`ARCHITECTURE.md` §2.5, *The CBC Runs*);
  - changed: today the register's state, such as "through Release, not yet read", is written by hand (`ARCHITECTURE.md` §2.5). Here it is found by comparison when asked;
  - changed: today a reading runs to the CBC Run's `HEAD`, and names work not yet committed (`.claude/skills/exchange-read/SKILL.md`, Stages 2 and 3). Here it runs to main, and work past it waits.

**Step 4. The Maintainer Repo finds where to start reading.**

- **What must happen:** the agent finds where this reading starts, and writes where it stops, before reading anything. A later reading must start where this one stopped, whether an update follows this reading or not.
- **Options,** for where the last reading's stop is kept:
  - a. in the System Repo, carried there by the next update;
  - b. in the Maintainer Repo's register, a "read to" commit beside where each System Repo lives;
  - c. in the Maintainer Repo, as the first line of each reading, every reading kept.
- **Chosen:** b. The others:
  - a fails when a reading has no update after it, which step 3's readings between allow: the System Repo still holds the old stop, and the next reading finds again what was read;
  - c keeps every reading only for one line.

  The start is the register's "read to", and it is never empty. At birth, the Maintainer Repo's check of the delivery writes the System Repo's row, with "read to" set to the start, the commit holding the System Kit Copies as they arrived (`temp/between-repos-simulation.md` §5.1, step 2). Nothing before the start is the System Repo's own change, so it stands as read. So every reading, the first among them, starts at "read to", and no "none" needs a path of its own. The frozen birth scenario gains this when it resumes (`TODO.md`, the item on resuming the simulation). The stop is the System Repo's main, written as the open reading's first line before anything is read, so a commit landing during the reading falls into the next one. It moves into the register when the reading is done (step 6), never before: a reading left half done must not mark its changes read. The reading stays a draft, and goes once its work is done.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo. For this step it says:
  - the start is the register's "read to";
  - the stop is the System Repo's main, written as the reading's first line before anything is read;
  - the stop moves into the register when the reading is done.
- **Today:**
  - borrowed: the stop is written first, as the reading's first line, before anything is read (`.claude/skills/exchange-read/SKILL.md`, Stage 2);
  - borrowed: the register keeps where each System Repo lives (`ARCHITECTURE.md` §2.5, *The CBC Runs*). It gains the "read to" commit;
  - borrowed: a CBC Run Reading is a draft in `temp/`, deleted once the work that needed it is done (`temp/README.md`; `.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today the stop, the Read-Through Commit, is kept in the CBC Run, carried there by the next Delivery Note, because "it is the only place the Concept Deliverer can look" (`docs/conventions/exchange/` §2.2, *The CBC Run*). Today every reading is followed by a delivery, so the stop always arrives. Here a reading may have no update after it;
  - changed: today a CBC Run is born with its Read-Through Commit written as *none*, and the exchange-read Agent Skill names no span for it (`delivery/installs/pure-seed.md`, step 2). Here birth writes the start as "read to", and the first reading starts there.

**Step 5. The Maintainer Repo compares the copies, and reads each entry.**

- **What must happen:** across the span, from "read to" to the stop, the agent finds every change in the System Kit's folders, a new file among them, pairs each with its entry, and reads the notes written in the span. It only reads the System Repo, and writes only in the Maintainer Repo.
- **Options,** for how changes are found:
  - a. each copy compared across the span, in the System Repo's own history, from "read to" to the stop;
  - b. each copy compared with the System Kit, at the moment the copies came from;
  - c. only the entries read, with no comparison;
  - d. the span walked commit by commit.
- **Chosen:** a. The others:
  - b finds the same as a until the first update. After it, a copy that kept a change differs from the System Kit at every reading, and the change is found again each time;
  - c misses a change with no entry, which the commit's check should have stopped, but which can still land (Failure Case 22);
  - d shows every edit on the way, and changes the gate reversed. The gate has settled those (step 2); what stands at the stop is what is read.

  An entry lands in the same diff as its change, in the copy's Adapted Understanding Text, so pairing them is reading one diff. Three things can come out:
  - a change with its entry: read with its what, what happened, which work found it, and the System Repo's proposal;
  - a change with no entry: read from the comparison alone, and marked "no entry";
  - an entry changed with no change to the copy, as when a why is rewritten: read as a change of its why.

  The notes are found the same way: their place in the System Repo's records is compared across the span, and each new note is read beside the changes. A note about a change points at its entry, so it is read with that change.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo. For this step it says:
  - compare each copy from "read to" to the stop, in the System Repo's history;
  - pair each change with its entry; mark one with none "no entry";
  - compare the notes' place across the span, and read each new note;
  - judge nothing.
- **Open:** an update lands inside the next span, so its changes to the copies would read as the System Repo's own, with no entry. They might be told apart by starting the span after the update, by marking the update's commits, or by comparing with the System Kit minus the entries, option b. Its trigger: the first update to reach a System Repo whose copies have entries, step 1's trigger too.
- **Today:**
  - borrowed: every item is read from the copies' diff, the whys, and the lines to the Concept Deliverer (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*; `.claude/skills/exchange-read/SKILL.md`, Stage 3). Here the whys are in the diff, so it is two: the diff and the notes;
  - borrowed: the CBC Run is only read, never written (`.claude/skills/exchange-read/SKILL.md`, *Gates*);
  - changed: today the diff runs against what was delivered, the Receipt Branch or the last delivery entry (`.claude/skills/exchange-read/SKILL.md`, Stage 3). That works because a Delivery Take makes every copy equal its original again. Here a copy keeps its changes;
  - changed: today the whys are read from the Decisions Log. Here they are read from the entries, in the copies.

**Step 6. It lists what changed, nothing judged.**

- **What must happen:** the reading gets one line per change and one per note, nothing judged. The human checks that the list is whole. Then the reading is done, and its stop moves into the register (step 4).
- **Options:**
  - a. one line per change, nothing decided; judging is the second half;
  - b. each change judged as it is listed;
  - c. only the changes the System Repo proposed as any repo's are listed;
  - d. one line per copy, its changes summed.
- **Chosen:** a. The others:
  - b judges before the whole list is seen, so changes with one reason are judged apart, and each verdict leans on the System Repo's proposal (Failure Case 20). Listing is cheap and judging is not, so the list is checked whole first;
  - c takes the proposal for the verdict, and a lesson for every repo stays in one System Repo (Failure Case 20);
  - d merges two changes to one copy, and one of their reasons is lost.

  A line holds what step 5 found: the copy and its part, what it says now, what happened, which work found it, and the System Repo's proposal, marked as one. A change with no entry says "no entry". Changes linked by one reason are listed together, under it. A note is a line of its own; one about a change sits with that change.
- **Adapted Case:** the Maintainer Repo's, for reading a System Repo. For this step it says:
  - one line per change and per note, nothing judged;
  - linked changes listed together, under their reason;
  - the human checks the list is whole; then the stop moves into the register.
- **Today:**
  - borrowed: one line per item, what it is and where, nothing decided (`.claude/skills/exchange-read/SKILL.md`, Stage 4 and *Gates*);
  - borrowed: the reading is a draft to its form (`.claude/rules/exchange-reading.md`);
  - changed: today a line is one per edit, per CBC Run Ask and per finding, read from three places (`.claude/skills/exchange-read/SKILL.md`, Stage 3). Here a line is one per change, with its entry, and one per note;
  - changed: today the proposal is not asked for: every edit must claim to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each line carries it, as input to judging.

## 4. The second half, decided and updated

It is simulated first for depth a, the change staying in the System Repo: the shortest path through every step. Depth c, the project-agnostic text changing, is then checked against it (§2, the second-half rows). Known before it was simulated:

- the four questions decide (`temp/common-ground-problem.md` §2.1, *Judging a change read back*), and the System Repo's own view of its change is input, never the verdict;
- the depth comes from the reason, never the edit. A cap raised from 50 to 60 stays in the System Repo, depth a, when its reason is "our scope names are long". The same edit is a project-agnostic lesson, depth c, when its reason is "the cap counts the scope, which any repo with scopes meets". Only the recorded reason tells them apart;
- what the System Repo gets reaches it with the next update, and its copy keeps its change either way (`temp/common-ground-problem.md` §2.1, *An update*).

Seven steps, for depth a:

1. The list is judged.
2. The verdict is written.
3. The Maintainer Repo makes its changes. For depth a, none.
4. The update is made: the System Kit's changes, and the verdicts the System Repo can act on.
5. The update is delivered.
6. The System Repo takes the update.
7. The next reading does not find the change again.

**Step 1. The list is judged.**

- **What must happen:** each line of the reading is first judged sound or not. A sound line is then judged by the four questions, in order, the cheapest first, until one holds (`temp/common-ground-problem.md` §2.1, *Judging a change read back*). The agent proposes an answer to each, with what it read; the human decides. For depth a, question 2 holds: the change answers that System Repo's own problem.
- **Options,** for who judges:
  - a. the agent proposes each answer, with what it read, and the human decides each line;
  - b. the agent judges, and the human looks only at the lines where the agent disagrees with the System Repo's proposal;
  - c. the human judges alone.
- **Options,** for a line marked "no entry":
  - d. judged from the comparison alone;
  - e. held, until the human brings its why from the System Repo.
- **Chosen:** a and e. The others:
  - b lets the agent's agreement with the proposal pass unchecked: two readings agreeing is not a verdict (Failure Case 20);
  - c leaves the human to read every text the questions need, which the agent reads faster, and with nothing written down to check;
  - d judges on a guess at the why (Failure Case 22).

  What each question reads:
  - question 0, the change is sound: what happened, the change, and the original part. Does the change fix what happened, without breaking something the copy did? An unsound change spreads nowhere: the depth questions are not asked, and the verdict says why. The copy is the System Repo's own, so the change stays there unless the System Repo reverses it;
  - question 1, the copy already said it: the original part, at the moment the copies came from, beside the change;
  - question 2, specific to that System Repo's problem: what happened, the System Repo's proposal, and its framing of its problem;
  - question 3, the project-agnostic understanding already holds it: the Project-Agnostic Understanding Text the Adapted Case narrows;
  - question 4, true for every repo: depth c's step, checked later.

  Lines listed together under one reason are judged together, and the reason is judged once. A line whose parts answer differently is split, each part judged on its own; the parts keep their one entry.

  A question is answered from what the change does and why, never from its wording. The System Repo writes in its own words on purpose (§3, step 1), and making a lesson general is rewording, after judging (step 3). A change worded for one project may still be a lesson for every repo. The agent's answer to question 2 says whether it agrees with the System Repo's proposal, and why if not.
- **Adapted Case:** the Maintainer Repo's, for judging a reading. It loads when the human starts judging a reading whose list was checked whole. For this step it says:
  - question 0 first: does the change fix what happened, without breaking something the copy did? An unsound change spreads nowhere, and its verdict says why;
  - then the four questions, in order, until one holds; for each, what it reads;
  - a line whose parts answer differently is split, each part judged on its own;
  - a question is answered from what the change does and why, never from its wording;
  - the agent proposes each answer with what it read; the human decides;
  - lines under one reason are judged together;
  - a line with no entry is held until its why is brought.
- **Open:** how question 4 is answered, and by whom. Its trigger: depth c is checked against these steps.
- **Today:**
  - borrowed: the four questions, from the second-half rules written before this simulation (`temp/common-ground-problem.md` §2.1, *Judging a change read back*). They leave how each is answered, and by whom, open; step 1 answers it for questions 1 to 3;
  - borrowed: a change may be declined as "not worth the change" (`docs/conventions/exchange/` §6.5, *Verdicts*). Question 0 asks it first, for every depth;
  - changed: the four questions gain question 0, and a line may be split into parts. The second-half rules have neither;
  - borrowed: a verdict that cannot be reached yet is held, with its trigger and a line so it is not lost (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today a verdict says whether the Concept Deliverer takes a hunk: taken, declined or held (`docs/conventions/exchange/` §6.5). Here it says how deep the change goes. Depth a is near today's declined, "not general", but the copy keeps the change, where today the next Delivery Take overwrites it.

**Step 2. The verdict is written.**

- **What must happen:** each judged line, or part of one, gets a verdict, the agent drafting and the human deciding. It is the Maintainer Repo's decision, written for its own work: what it changes, in the System Kit or the project-agnostic understanding, starts from it (step 3). Which verdicts the System Repo gets is step 4's. For depth a: the change stays, as the System Repo's own, and nothing changes here.
- **Options,** for what a verdict holds:
  - a. the answer only: unsound, misread, or its depth;
  - b. the answer, its why, and whether it agrees with the System Repo's proposal, with why if not;
  - c. b, and what the Maintainer Repo changes for it.
- **Chosen:** b. The others:
  - a leaves the change made from it with nothing to check it against, and a proposal judged wrong goes unseen;
  - c decides what changes before it is worked out: that is step 3's, with the survey where the depth needs one.

  A verdict is one of: unsound; misread, question 1; its own, question 2, depth a; lost in narrowing, question 3, depth d; a project-agnostic lesson, question 4, depth c; a lesson for System Repos only, depth b; or held, with its trigger. Lines under one reason share one verdict, and each line says how its own copy is affected.

  The agreement is said in one line, "the proposal holds" or "the proposal does not hold, because …". An unsound verdict says what the change breaks or leaves unfixed; whether to reverse it is the System Repo's decision, once the verdict reaches it (step 4).
- **Adapted Case:** the Maintainer Repo's, for judging a reading. For this step it says:
  - one verdict per line or part: its answer, its why, and whether the proposal holds;
  - lines under one reason share a verdict, each saying how its own copy is affected.
- **Open:** whether an unsound verdict offers a fix. Its trigger: the first unsound verdict.
- **Today:**
  - borrowed: a verdict carries its why (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today every verdict goes down in the Delivery Note (`docs/conventions/exchange/` §6.5). Here the verdict is the Maintainer Repo's, and only those the System Repo can act on go down (step 4);
  - changed: today a verdict is taken, declined or held (`docs/conventions/exchange/` §6.5). Here it is a depth, or unsound, misread or held;
  - changed: today no verdict answers a proposal, since every edit claims to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each says whether the proposal holds.

**Step 3. The Maintainer Repo makes its changes. For depth a, none.**

- **What must happen:** from each verdict, the Maintainer Repo makes what its depth asks, the agent drafting and the human deciding. For depth a, nothing changes in the System Kit or the project-agnostic understanding. The verdict waits in the reading, which stays a draft until the update carries what the System Repo needs (step 4).
- **Options,** for depth a:
  - a. nothing changes here; the verdict waits in the reading;
  - b. nothing changes in the System Kit, and the verdict is also kept in a lasting record, by the part it changed, so a later reading sees when another System Repo makes the same change;
  - c. the change enters the System Kit as a variant, for System Repos like this one.
- **Chosen:** a. The others:
  - b builds a record before any part has been changed by two System Repos;
  - c is a speculation: one System Repo's own change, offered to System Repos that have not met it. Several Adapted Cases needing a change, but not all, is its own case (§2, row f).

  For the other depths, this step holds the work, each checked here later: depth b changes the System Kit's Adapted Case; depth c changes the project-agnostic understanding, after the survey; depth d fixes the Adapted Case from the project-agnostic understanding; a narrowing is marked with its why. A lesson is reworded here, never before: for every System Repo at depth b, naming no project at depth c (`temp/common-ground-problem.md` §2.1, *A project-agnostic lesson*).
- **Adapted Case:** the Maintainer Repo's, for judging a reading. For this step it says: a verdict of its own changes nothing here; the reading stays a draft until the update carries what the System Repo needs.
- **Open:** whether depth a's verdicts are kept beyond the update, so the same change by a second System Repo is seen. Without it, two System Repos making one change are each judged alone. Its trigger: the second System Repo read back.
- **Today:**
  - borrowed: a declined change moves nothing in the Concept Deliverer's tree (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - borrowed: a taken change is committed here, and the next delivery carries it (`docs/conventions/exchange/` §6.5). It is the other depths' path;
  - borrowed: the why of a declined change goes in the Delivery Note and nowhere else (`docs/conventions/exchange/` §6.5). Here the reading holds it until the update.

**Step 4. The update is made: the System Kit's changes, and the verdicts the System Repo can act on.**

- **What must happen:** when work resumes in the System Repo, after it is read back and judged, the Maintainer Repo makes its update, the agent drafting and the human deciding (`temp/common-ground-problem.md` §2.1, *An update*). An update is due when the System Kit has moved past the moment the System Repo's copies came from, or when its reading left a verdict that goes down. It reaches the System Repo on the human's word, in a step of its own: nothing crosses without that word, and the agent may carry it. For depth a, the System Kit has not changed for this change, so the update carries it only if its verdict is one the System Repo can act on.
- **Options,** for which verdicts go down:
  - a. every verdict;
  - b. only those the System Repo can act on: unsound, misread, and a proposal that did not hold;
  - c. none; only the System Kit's changes.
- **Options,** for when an update goes:
  - d. after every reading, even with nothing to carry;
  - e. only when it carries something: a System Kit change, or a verdict that goes down.
- **Chosen:** b and e. The others:
  - a sends lines that ask nothing of the System Repo. A change judged its own, with its proposal holding, needs no answer: the copy keeps it either way;
  - c leaves an unsound change unknown to the only repo that can reverse it;
  - d sends an empty update to carry where the reading stopped. "Read to" is in the register now (§3, step 4), so nothing needs carrying.

  Whether an update is due is found by comparison, as step 3 of the first half finds work to read: the System Repo's moment, which it holds, against the System Kit's. It runs when the human names a System Repo to update, or asks which are behind. A System Repo is blind, so it cannot learn this itself. Nothing is sent to a System Repo whose work has not resumed.

  An update holds:
  - every System Kit Copy, whole, at the System Kit's new moment, and the moment. The System Repo then has the new version of each file, and finds its old one in its own history (step 6);
  - the whys of the System Kit's changes since the System Repo's moment, whatever their source: this System Repo's reading, another System Repo's, or the Maintainer Repo's own work. Each why stands on its own, and names no other repo;
  - each path gone or renamed, since a copy cannot carry its own absence;
  - the verdicts that go down, from this System Repo's own reading only, each naming the System Repo's own copy and part, the System Repo's commit it judged, and what the System Repo may do now. The commit is the System Repo's own, so it can open it, and see whether the part has changed since (step 6).

  Nothing in it cites what the System Repo cannot open: no path, record or word of the Maintainer Repo's own. A depth-a change whose proposal held sends nothing, and the System Repo's copy keeps it.

  A reading stays open until its update is made, or until it is judged with nothing to send. One reading is open per System Repo at a time: a reading made while one is open extends it, and its lines are judged with the rest, so judging already done is kept. One update waits for the System Repo at a time: a newer one replaces one not yet taken, since it carries every System Kit change since the copies' moment, and the verdicts of both readings.
- **Adapted Case:** the Maintainer Repo's, for making an update. It loads on the human's word to update a System Repo. For this step it says:
  - it follows the System Repo's reading back and judging, never comes before them;
  - it goes only when it carries a System Kit change or a verdict;
  - it is due when the System Repo's moment is behind the System Kit's, or a verdict goes down; the moments are compared when the human names a System Repo or asks which are behind;
  - it carries every System Kit Copy whole, at the new moment, the whys of the changes since the System Repo's moment, whatever their source, what is gone, and the verdicts from this System Repo's reading that it can act on;
  - it cites nothing the System Repo cannot open;
  - each verdict names the System Repo's commit it judged;
  - one reading open per System Repo, a new reading extending it; one update waiting, a newer one replacing it.
- **Today:**
  - borrowed: the delivery is staged into the CBC Run's `temp/` on the reviewer's word, the CBC Run's tree checked clean first, and named by the commit it was final at (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: files go whole, every copy at every delivery after birth (`docs/conventions/exchange/` §3.2, *What goes*);
  - borrowed: a delivery goes after a reading, or when something a CBC Run holds has changed in the Concept Deliverer (`.claude/skills/exchange-deliver/SKILL.md`, its description);
  - borrowed: the note says what changed since the Delivery Pin, and why it matters to this CBC Run (`docs/conventions/exchange/` §3.7, *The Delivery Note*);
  - borrowed: a verdict says the decision and what the CBC Run owes now, nothing else; no path or word of this repo's reaches it (`docs/conventions/exchange/` §3.7);
  - borrowed: a note may arrive alone, with no files (`docs/conventions/exchange/` §6.6, *The Delivery Note after a read*). An update of verdicts only is one;
  - borrowed: the note carries what is gone (`docs/conventions/exchange/` §3.6, *Absence in a delivery*);
  - borrowed: one CBC Run Reading is open per CBC Run at a time, and a new read extends it (`.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today every read ends with a Delivery Note, even an empty one, to carry the Read-Through Commit (`docs/conventions/exchange/` §6.6). Here an update goes only when it carries something;
  - changed: today the note gives a verdict on everything the CBC Run addressed to the Concept Deliverer (`docs/conventions/exchange/` §3.7). Here only the verdicts the System Repo can act on go down.

**Step 5. The update is delivered.**

- **What must happen:** on the human's word, the update is staged into the System Repo's `temp/`, by the human or by the agent. It is the only time the Maintainer Repo writes into a System Repo, and it writes nowhere else there. Nothing in `temp/` is in force until the System Repo takes it (step 6).
- **Options,** for checking what was staged:
  - a. a second Adapted Case of the Maintainer Repo's checks it, apart from the one that delivered, as at birth;
  - b. the delivering Adapted Case compares each staged file with the System Kit at the new moment, once staged, and the System Repo checks the note against the files when it takes them;
  - c. only the System Repo's check, at the take.
- **Chosen:** b. The others:
  - a was chosen at birth because the start becomes the base of every reading (`temp/between-repos-simulation.md` §5.1, step 2). Here a wrong file is held in `temp/`, never in force, and a comparison of files leaves little mistake to share. It comes back if a staged file is found, after a take, to differ from the System Kit;
  - c leaves only the System Repo to check, and it cannot open the System Kit, so a staged file that differs from it passes.

  The System Repo's tree is checked clean first, with nothing in flight. When it is not, the agent says what it found and waits for the word. An update already waiting there is replaced by the new one (step 4). The update is named by the Maintainer Repo's commit at which its files and note were final, so its moment is exact.
- **Adapted Case:** the Maintainer Repo's, for delivering an update. It loads on the human's word to deliver. For this step it says:
  - never stage unasked; check the System Repo's tree clean first;
  - write only into the System Repo's `temp/`, replacing an update already waiting;
  - name the update by the commit it was final at;
  - compare each staged file with the System Kit at the new moment.
- **Today:**
  - borrowed: the delivery and its note are copied into the CBC Run's `temp/` on the reviewer's word, by the reviewer or by the agent when told; the agent never stages unasked; the tree is checked clean first; the Delivery Staging is named by the commit at which files and note are final (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: one Agent Skill both writes the note and stages the delivery (`.claude/skills/exchange-deliver/SKILL.md`). It also compares the staged files here;
  - borrowed: the CBC Run's `temp/` gains exactly the staging and its note, and nothing tracked in the CBC Run changes (`.claude/skills/exchange-deliver/SKILL.md`, *Gates*);
  - changed: today the staged files are copied by a script, so they equal the Master Copies by how they are made, and no comparison follows; the CBC Run's Delivery Take checks the note against the files (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 1).

