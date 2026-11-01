# AGO: Agreement, our side

Reader AGO. Finding Kind: Agreement, read from our side, at `70404e1`.
Rule homes read whole: `docs/conventions/facts-in-sync/` §4 and §5;
`docs/conventions/conventions/` §1.3 and §2.4. Also read: the
refinement's Decisions 1 to 40, both lists of the agent's calls,
ADR-0079, and the leftovers.

17 findings. 6 checked, 8 resting on the reader, 3 uncertain.

Listed in order of weight: the first five change what an agent does.

---

## AGO-1. The one-home Agent Rule's example of what goes

- **Where:** `.claude/rules/one-home.md`, *The rules*, rule 2, line 25.
- **Quote:** `copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the`
- **The rule:** a Fact Reference saying other than its home is a
  disagreement (`docs/conventions/facts-in-sync/` §5, *A
  disagreement*). A retelling whose reference names a changed section
  is re-read (§4, *A Canonical Description's rule*, step 3).
- **What the text says:** after CBC Run Birth, only Agent Skills,
  Agent Rules, Output Shapes, Approaches on Trial and the concept go.
  Its home, `docs/conventions/exchange/` §3.2, *What goes*, line 205,
  also lists "each group's Glossary Names, in `docs/glossary/`". The
  retelling leaves out one of the five things that go.
- **Which side is wrong:** the Agent Rule. The exchange-deliver
  Agent Skill stages `docs/glossary/` too.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `3630ed9` (2026-10-31)
  added the Glossary Names to §3.2. The Change Walk's re-read of each
  retelling that names §3.2 should have caught it. `2158499`
  (2026-11-01) then edited this very line and kept the old list.
- **Proposed:** fix: "After CBC Run Birth, only the copies go: Agent
  Skills, Agent Rules, Output Shapes, Approaches on Trial, the Glossary
  Names and the concept (`docs/conventions/exchange/` §3.2, *What
  goes*)."

## AGO-2. The exchange-deliver Agent Skill calls the Delivery Note told

- **Where:** `.claude/skills/exchange-deliver/SKILL.md`, *Stage 1 —
  write the Delivery Note*, lines 17 to 19. Again at step 7, line 93.
- **Quote:** ``In `temp/note-to-<run>-<date>.md`, told, not delivered: the CBC Run``
- **The rule:** a derived thing and its Canonical Description agree
  (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's
  rule*, step 4; §5, *A disagreement*).
- **What the text says:** the Delivery Note is "told, not delivered",
  and the CBC Run "reads it through the Told Channel, as session
  input" (`docs/models/tiers.md` §3.2). Its foundation, the exchange
  manual, says otherwise in three places:
  - §6.6, line 562: "A Delivery Note alone, with no files, is still a
    delivery";
  - §3.1: the Delivery Note is copied into the CBC Run's `temp/` with
    the delivery;
  - §3.7: "in a Delivery Note or in a prompt ... A prompt is the Told
    Channel's text, so the same holds for it". The prompt is the Told
    Channel; the Delivery Note is not.

  The Fact Reference also misses: Tiers Model §3.2 says "The Told
  Channel is not delivery", a warning handed as session input after
  the Run Repo's own work missed it. A file staged in `temp/` and read
  under the delivered-copies Agent Rule is not that.
- **Which side is wrong:** the Agent Skill. The old wording, "told
  not delivered", meant only that the Delivery Note is not a pinned
  copy.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `31156de` (2026-11-01, a
  writing pass) grew "told not delivered" into the Told Channel claim
  and its Fact Reference. The Foundation Check's step 2 reads the
  exchange manual beside such a change.
- **Proposed:** fix line 17 to 19: "In `temp/note-to-<run>-<date>.md`.
  It goes down with the delivery, but it is not a copy: the CBC Run
  reads it at the Delivery Take, and it goes when the take is done
  (`docs/conventions/exchange/` §4, *The Delivery Take*, step 5)."
  Fix step 7: "The CBC Run cannot open this repo, and a citation it
  cannot follow reads as its own."

## AGO-3. The Tiers Model says the Delivery Pin moves at every take

- **Where:** `docs/models/tiers.md`, §3.4, *The Delivery Pin and
  documents*, lines 125 to 129.
- **Quote:** `it holds wrong. That is why the Delivery Pin moves with every`
- **The rule:** an Idea Model and what stands on it agree; either may
  be wrong (`docs/conventions/facts-in-sync/` §5, *A disagreement*;
  `docs/models/idea-to-output.md` §3.3, *Settling a disagreement*).
- **What the text says:** "every delivery is a document, and its
  Delivery Pin moves with it", and "the Delivery Pin moves with every
  Delivery Take". The exchange manual, which stands on this model,
  says a Delivery Note without files is a take that moves only the
  Read-Through Commit: §2.5, line 174, "leaves the Delivery Pin where
  it was"; §6.6, line 562, "the Read-Through Commit moves, the
  Delivery Pin does not".
- **Which side is wrong:** the Tiers Model. It is too general: a
  delivery with no copy changes nothing the pin describes.
- **Stands:** checked.
- **Why it was missed:** wrong from its first form, `ba29cb7`
  (2026-09-30), which cited the exchange for it. The exchange's
  note-only rule is older, `7c952e6` (2026-09-26). Missed again at
  `b06dc95` (2026-10-28), when the Tiers Model took the exchange's
  general facts: the Foundation Check's step 4 lists each
  disagreement.
- **Proposed:** fix: "That is why the Delivery Pin moves with every
  Delivery Take that brings a copy". Make the same change to "every
  delivery is a document, and its Delivery Pin moves with it": "every
  delivery that brings a copy".

## AGO-4. The Tiers Model says up is only records

- **Where:** `docs/models/tiers.md`, §3.3, *Upward harvest*, line 114;
  and §4.2, *The dependency rule*, line 169.
- **Quote:** `Up is harvest, and only through records: the tier above reads a`
- **The rule:** as AGO-3.
- **What the text says:** the tier above reads only the Run Repo's
  records ("Upward: only records", line 169). The exchange manual,
  which stands on it, reads three things, one of them not a record:
  "the diff of every held copy against its Delivery Pin" (§6.1,
  *Reading a CBC Run*, line 486). The model's own fact 4 (§3.5) says
  the same: "the edit is read from above as the diff". A copy is not
  a record (`docs/conventions/exchange/` §2.4, *The records'
  exception*: the records are the CBC Run's own, the copies are not).
- **Which side is wrong:** the Tiers Model's §3.3 and §4.2. Its §3.5
  and the exchange agree with each other.
- **Stands:** resting on the reader. The judgement is that a copy's
  diff is not a record.
- **Why it was missed:** older text, from the handbook's model.
  Missed at `b06dc95`, as AGO-3.
- **Proposed:** fix §3.3: "Up is harvest, and only through what the
  Run Repo committed: its records, and the diff of its copies. The tier
  above reads them, read-only, and the Run Repo sends nothing." Fix
  §4.2: "Upward: only records, and the diff of the copies."

## AGO-5. ARCHITECTURE's rule on the method's Output Shapes

- **Where:** `ARCHITECTURE.md`, §3, *What must stay true*, line 214.
- **Quote:** `| Every Agent Skill and Output Shape of the method states the concept version it derives from |`
- **The rule:** a Fact Reference saying other than its home is a
  disagreement (`docs/conventions/facts-in-sync/` §5, *A
  disagreement*).
- **What the text says:** every Output Shape of the method states a
  concept version, and the home is `docs/conventions/conventions/`
  §1.3. That section says an Output Shape names "the convention it
  lives under, `practice, under the shapes convention`". The four
  Output Shapes under `delivery/method/.claude/shapes/` all carry
  exactly that, and name no concept version. Only the two Agent
  Skills carry `concept v1`.
- **Which side is wrong:** ARCHITECTURE.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `c0eb1e6` (2026-11-01,
  a writing pass) turned "Every execution states the concept version"
  into this line and widened what it claims. The one-home rule's
  question at each changed line (rule 6) should have caught it.
- **Proposed:** fix: "| Every Agent Skill of the method states the
  concept version it derives from |".

## AGO-6. Where the concept's list of what derives from it lives

- **Where:** `ARCHITECTURE.md`, §2, *The delivery and the CBC Runs*,
  lines 133 to 134.
- **Quote:** `ship*). This list is kept here: the chapters carry none`
- **The rule:** "A Canonical Description lists what derives from it.
  An Idea Model leaves its list to the grep in step 3"
  (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's
  rule*, step 1, line 267).
- **What the text says:** the concept's list is kept in
  `ARCHITECTURE.md`, and cites step 1 for it. Step 1 allows no list
  kept elsewhere. It excuses only an Idea Model, and the concept is a
  Canonical Description. The cited home does not say what the line
  says.
- **Which side is wrong:** the rule, probably. The concept has no
  *What this is made usable as*, and ARCHITECTURE has kept its list
  since `53fda69` (2026-10-21). Step 1 never said so.
- **Stands:** resting on the reader.
- **Why it was missed:** the line was written against the conventions
  manual's old §3.5. The rule moved to facts-in-sync (`e2ad2e4`,
  ADR-0065), and nothing compared the two.
- **Proposed:** question: does facts-in-sync §4 step 1 gain "The
  concept's chapters carry no list: `ARCHITECTURE.md` §2 keeps it"? A
  Canonical Description may name a record, as long as it does not take
  a fact from it (§3.1, *What a Fact Reference is*). Or does the
  concept carry its own list, in `concept/00-cbc.md`?

## AGO-7. Facts-in-sync's list misses one-home rule 7

- **Where:** `docs/conventions/facts-in-sync/README.md`, *What this is
  made usable as*, lines 38 to 41. The same list is in
  `.claude/rules/one-home.md`, its header comment, lines 11 to 13.
- **Quote:** `  §2, *Point and derive*; §3.1, *What a Fact Reference is*; *The Concept Deliverer's seat*).`
- **The rule:** a manual's list names what each derived thing holds,
  and a change walks it (`docs/conventions/conventions/` §2.3, *The
  list of what derives*; `docs/conventions/facts-in-sync/` §4, step 1).
- **What the text says:** our one-home Agent Rule holds §1, §2, §3.1
  and the Concept Deliverer's seat. The Agent Rule's rule 7 holds §3.4,
  *A decision citation*, and cites it. Rule 4 also uses §3.3 and §4.
  A change to §3.4 would not find rule 7 by this list.
- **Which side is wrong:** the list, in both places.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `7d060af` (2026-10-31)
  added rule 7 and did not touch the list or the header comment. The
  Foundation Check's step 2 opens the manual beside the change.
- **Proposed:** fix both lists to add "§3.4, *A decision citation*"
  (in the comment, "§3.4, A decision citation"). Add §3.3 and §4 if
  the reviewer counts rule 4's references.

## AGO-8. The retrospective trial and the CBC Run Birth's close

- **Where:** `docs/conventions/retrospective/README.md`, *The
  Concept Deliverer's seat*, line 89. The same trial is in
  `docs/conventions/project-recording/README.md`, *The Concept
  Deliverer's seat*, item 1, lines 73 to 75.
- **Quote:** `At the close of the Plan Step that runs the next CBC Run Birth, it`
- **The rule:** each manual's seat agrees with the files its side
  holds (`docs/conventions/conventions/` §2.4, *The seats*).
- **What the text says:** at that close, this repo runs both
  retrospective Agent Skills on itself, "in place of that close line",
  the line "lessons written back where they came from". Our side
  holds three different answers:
  - `PLAN.md`'s open-but-stopped Plan Step "Birth CBC Run 6, on full
    auto" ran a CBC Run Birth (2026-10-29). Its close items, lines 182
    to 201, hold no retrospective, and still hold the close line the
    trial replaces (line 194). `PLAN.md`'s form says "A trial names
    the close that judges it."
  - `TODO.md` line 682 gives CBC Run 5's birth as the trigger, which
    has passed (that trigger is leftover E8; the disagreement here
    is the manual against `PLAN.md`).
  - Written on 2026-11-01, after CBC Run 6's birth, "the next" may
    mean CBC Run 7's.
- **Which side is wrong:** unclear. Either `PLAN.md`'s Birth Plan Step
  gains the trial, or both manuals name the CBC Run Birth whose close
  judges it.
- **Stands:** resting on the reader, on which Birth is meant.
- **Why it was missed:** the seat's text predates CBC Run 5's and 6's
  births. Neither Birth Plan Step's Gate was checked against it when
  written.
- **Proposed:** question: does the trial run at the close of "Birth
  CBC Run 6, on full auto", or at CBC Run 7's? Then fix whichever side
  is wrong, and name the Plan Step in both manuals.

## AGO-9. The Agent Model keeps an operator's file out of history

- **Where:** `docs/models/agent.md`, §4.1, *Ambient Channel*,
  *Ownership*, line 92.
- **Quote:** `  - stays out of the repo's history;`
- **The rule:** an Idea Model and the manual that stands on it agree
  (`docs/conventions/facts-in-sync/` §5, *A disagreement*).
- **What the text says:** an operator's own file "stays out of the
  repo's history". The agent-arrangement manual, which stands on this
  model and cites this part for the file, says "The Concept Deliverer
  tracks its own" (§3.7, *`CLAUDE.local.md`*; ADR-0062). This repo's
  `CLAUDE.local.md` is tracked.
- **Which side is wrong:** the model, probably. ADR-0062 never weighed
  it. But an Idea Model's rules may vary by repo
  (`docs/models/idea-to-output.md` §5, *An Idea Model and a concept*),
  so this may be an allowed adaptation.
- **Stands:** uncertain.
- **Why it was missed:** missed at a change. `a3fefe1` (2026-10-23)
  changed agent-arrangement §3.7. The Foundation Check's step 2 opens
  the Idea Model the manual names.
- **Proposed:** question: does §4.1 say "stays out of the repo's
  history, unless a repo with one operator tracks it"? Or is the
  difference an adaptation, said in agent-arrangement §3.7?

## AGO-10. The Agent Model's landing list has no Agent Rule

- **Where:** `docs/models/agent.md`, §9, *Where each convention
  lands*, lines 238 to 240.
- **Quote:** `Each convention's Work Approaches show where it lands: an Agent Skill`
- **The rule:** as AGO-9.
- **What the text says:** a convention lands as an Agent Skill, or as
  Record Stubs and Agent Skill Templates. The agent-arrangement
  manual, which stands on it, places a convention's rule in an Agent
  Rule as well: by path (§3.2, *`.claude/rules/`*), or with no path
  for a rule of every task (§3.9, *An Agent Rule always loaded*). Six
  of our Agent Rules and four of the Container Group's land so.
- **Which side is wrong:** the model. Its list predates the Agent
  Rules always loaded (ADR-0053).
- **Stands:** resting on the reader, that the list reads as whole.
- **Why it was missed:** older than ADR-0053. Missed at `9fce63c`
  (2026-11-01), which rewrote this line; the Foundation Check's step 3
  runs the Change Walk on what stands on the model.
- **Proposed:** fix: "Each convention's Work Approaches show where it
  lands: an Agent Skill for a rule bound to a moment, an Agent Rule
  for a rule bound to a path or to every task, Record Stubs and Agent
  Skill Templates for a rule carried in the files a project is born
  with."

## AGO-11. Three kinds of Work Approach, listed two ways

- **Where:** `docs/conventions/conventions/README.md`, §1, *A
  convention's Work Approaches*, lines 52 to 58.
- **Quote:** `- Record Stubs and Agent Skill Templates, for rules that sit in the`
- **The rule:** a manual and the Idea Model it names agree
  (`docs/conventions/facts-in-sync/` §5, *A disagreement*).
- **What the text says:** a Work Approach is one of three: an Agent
  Skill, an Agent Rule, or "Record Stubs and Agent Skill Templates".
  Its Idea Model, the Idea-to-Output Model, lists them otherwise:
  - §1 and §6.1: "Agent Skills, Agent Rules and Output Forms";
  - §2, line 38: "an Agent Skill, an Agent Rule, an Approach on Trial,
    a record's form in its header comment".

  The model never names an Agent Skill Template. ADR-0078's decision 1
  takes the model's words.
- **Which side is wrong:** unclear. A Record Stub carries a record's
  Output Form, so that part may only be wording. The Agent Skill
  Template is the real difference.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at the design that renamed both
  (ADR-0078, DECISION-32): the model's §6 and the manual's §1 were
  walked together, but their lists were not compared.
- **Proposed:** question: is an Agent Skill Template a Work Approach?
  If yes, the model's §2 names it. If not, the manual's third kind
  reads "Output Forms: a record's form, in its header or its Record
  Stub".

## AGO-12. Whether an Approach on Trial stands on anything

- **Where:** `docs/models/idea-to-output.md`, §3.1, *The four Chain
  Links*, line 61.
- **Quote:** `A Work Approach stands on a Canonical Description, never on an Idea Model directly.`
- **The rule:** as AGO-11.
- **What the text says:** every Work Approach stands on a Canonical
  Description, and §2 counts an Approach on Trial a Work Approach. The
  conventions manual, which stands on this model, says "An Approach on
  Trial carries none: it is first-time work, and stands on no
  Canonical Description until an evaluation places it" (§1.3, *The
  Foundation Line*, lines 114 to 116). The model's §4.2 agrees with
  the manual; its §3.1 does not.
- **Which side is wrong:** the model's §3.1, which is wider than its
  own §4.2.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule; neither text changed
  this part since the Approach on Trial was placed (ADR-0058).
- **Proposed:** fix: "A placed Work Approach stands on a Canonical
  Description, never on an Idea Model directly. An Approach on Trial
  stands on none yet (§4.2, *The upward direction*)."

## AGO-13. What a concept version is

- **Where:** `docs/models/tiers.md`, §3.1, *Downward delivery*,
  lines 88 to 89.
- **Quote:** `   what "a concept version" is;`
- **The rule:** as AGO-3.
- **What the text says:** the pin, a commit of the tier above, "is
  what 'a concept version' is". The exchange manual, which stands on
  this model, sends the concept's version to ADR-0003 and
  `CHANGELOG.md`'s comment (*What this does not cover*, line 592).
  There a concept version is a whole number, v1, moved only by a
  change that could invalidate a derived Agent Skill. The conventions
  manual's Foundation Line value is `concept v1` (§1.3). Many
  Delivery Pins share one concept version.
- **Which side is wrong:** the Tiers Model.
- **Stands:** resting on the reader.
- **Why it was missed:** older text, from the handbook's model
  (`fc0b078`, 2026-09-27). Missed when the exchange took the Tiers
  Model as its foundation, at the Foundation Check's step 2.
- **Proposed:** fix: "a copy, always pinned at a commit of the tier
  above. The copy also names the concept version it derives from,
  which the Concept Repo's own log sets;".

## AGO-14. The writing manual's seat leaves out our commits

- **Where:** `docs/conventions/writing/README.md`, *The seats*,
  lines 54 to 56.
- **Quote:** `commits. The Concept Deliverer writes under its own: its chat and`
- **The rule:** a seat says what its side does under the convention,
  and agrees with the files that side holds
  (`docs/conventions/conventions/` §2.4, *The seats*).
- **What the text says:** the Concept Deliverer writes "its chat and
  records" under its Agent Rule, beside what CBC Runs read and its
  manuals. The CBC Run's seat names its commits. Our Agent Rule,
  `.claude/rules/writing.md`, governs "commit messages, comments" as
  well, and the manual's §1 covers both in every repo.
- **Which side is wrong:** the seat.
- **Stands:** resting on the reader, that the seat reads as a whole
  list.
- **Why it was missed:** the rule check of Refinement Round 3 read
  the rule, not the seat beside our rule.
- **Proposed:** fix: "The Concept Deliverer writes under its own: its
  chat, its records, its commits and comments."

## AGO-15. Where a stopped Plan Step sits in our plan

- **Where:** `docs/conventions/project-recording/README.md`, *The
  Concept Deliverer's seat*, item 4, lines 81 to 82.
- **Quote:** `   work being done now, and below it any Plan Step stopped for it.`
- **The rule:** as AGO-14.
- **What the text says:** a stopped Plan Step sits below the one being
  worked. In `PLAN.md` the two stopped Plan Steps come first (lines
  135 and 213), and the open one, "Refine this repo against its own
  rules", comes last (line 301).
- **Which side is wrong:** the seat. `PLAN.md`'s form says nothing of
  order, so the seat's "below" is the only claim.
- **Stands:** checked.
- **Why it was missed:** the seat was written for one stopped Plan
  Step; a second one was stopped and the order was never read
  against it.
- **Proposed:** fix: "the piece of work being done now, and beside it
  any Plan Step stopped for it."

## AGO-16. The writing manual's rule 6 and the glossary's header

- **Where:** `docs/conventions/writing/README.md`, §2, *Why each
  rule*, rule 6, lines 96 to 97. Our Agent Rule follows it,
  `.claude/rules/writing.md` rule 6, line 30 to 31: "Define each
  Glossary Name once, in plain words, in `docs/glossary.md`."
- **Quote:** `   cannot check, so each is defined once, in the project's`
- **The rule:** a Canonical Description and what derives from it agree
  (`docs/conventions/facts-in-sync/` §5, *A disagreement*).
- **What the text says:** each coined word is defined in the
  project's glossary. The glossary, which derives from this manual,
  says "the home defines, the entry points" (`docs/glossary.md`,
  header comment, lines 8 to 9). The manual's own rule 9 says the same
  as the glossary: a Name goes into the glossary "pointing at the home
  that defines it".
- **Which side is wrong:** rule 6, in the manual and in our Agent
  Rule. It predates ADR-0076, which made the glossary a list of Names.
- **Stands:** uncertain. An entry also gives the meaning in plain
  words, so "defined" may mean only that.
- **Why it was missed:** rule 6 was not rewritten when rule 9 was
  (ADR-0076, ADR-0078).
- **Proposed:** question: does rule 6 read "so each has one Glossary
  Name, listed in the project's glossary with its plain meaning,
  pointing at the home that defines it"? Our Agent Rule's rule 6
  would follow.

## AGO-17. The operator's file holds the commit stop

- **Where:** `CLAUDE.local.md`, line 3.
- **Quote:** `- Before any commit: stage it, show me the diff, and stop. Commit`
- **The rule:** "It holds the operator's settings, never rules"
  (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*,
  line 367). A file this repo holds agrees with its manual's seat.
- **What the text says:** the stop at every commit, one commit at a
  time, no push without the word. That is the commit-messages
  convention's rule (`docs/conventions/commit-messages/` §2.4, *Commit
  on the word*). The agent-arrangement manual itself calls it so:
  "The commit stop is not such a rule" (§3.5, line 344, pointing at
  §2.4). Line 5 does the same for a Change Set (`commit-plan` §6). But
  §3.7 also names "how often the agent stops for review" as a setting.
- **Which side is wrong:** unclear. The manual says both.
- **Stands:** uncertain.
- **Why it was missed:** the rule is unclear: §3.7's example of a
  setting overlaps a rule another manual owns.
- **Proposed:** question: is "stop at every commit" a setting here, or
  the convention's rule? If a rule, lines 3 to 5 go, or keep only what
  differs from it. If a setting, §3.7 says the stop is one.

---

## Found true, so not listed

- **Our five Agent Skills against their manuals:** commit-messages,
  commit-plan and visual-comparison agree with their manuals' bodies
  and *What this is made usable as*. exchange-read agrees with
  exchange §6.1 to §6.3. exchange-deliver agrees with §3.1, §3.2,
  §3.3, §3.7 and §3.8, but for AGO-2.
- **Our six Agent Rules:** convention-manual against conventions §2,
  item by item; exchange-reading and working-a-reading against
  exchange §6.3 to §6.5; foundation-check against facts-in-sync §3.3,
  §4 and §5; writing against the writing manual §1 and §2 (rules 9 to
  11 now carry ADR-0079's lines); one-home against facts-in-sync §1,
  §2, §3.1, §3.4 (now names the CHANGELOG).
- **The records' header comments against project-recording:**
  `docs/adr/README.md` (§3.4), `devlog/README.md` (§4.3, §4.4),
  `TODO.md` (§5.4), `CHANGELOG.md` (§6.3, §6.4), `README.md` (§7.4,
  the Repo Tag), `ARCHITECTURE.md` (the seat's item 5),
  `TODO-CONVERSATION-MEMORY.md` (§14), `PLAN.md`'s Plan Step Form
  (§2.4, the seat's item 4, but for AGO-15).
- **`CLAUDE.md` and `.claude/decisions.md` against agent-arrangement:**
  the guard's three tests (§2.4), the size rule (§2.6), the records
  table (project-recording §13.1, eleven rows against §1's items 1 to
  10 and 13), the Decisions Log's header (§3.4, the seat).
- **`docs/glossary.md` against the writing manual:** the entry form
  and rule 9, but for AGO-16.
- **The seats against our files:** agent-arrangement's list of our
  five Agent Skills, six Agent Rules and Approaches on Trial matches
  `.claude/`; repo-hygiene's seat matches our three dotfiles, which
  differ from the Hygiene Base only by the "this repo" section;
  shapes, commit-plan, commit-messages, visual-comparison,
  facts-in-sync and conventions seats agree.
- **Each manual's *What this is made usable as*** names our files by
  their real paths, each with its Foundation Line, but for AGO-7.
- **The four manuals on Idea Models:** conventions and facts-in-sync
  against the Idea-to-Output Model §2, §3, §6 (but for AGO-11, AGO-12);
  agent-arrangement against the Agent Model §4, §5, §8, §10, §12 (but
  for AGO-9, AGO-10); exchange against the Tiers Model §3.5's five
  facts (but for AGO-3, AGO-4, AGO-13).
- **The Idea-to-Output Model's count** "8 of the 12 manuals stand on
  none" holds: 4 manuals carry a Foundation Line.

## Met in passing

- `docs/models/agent.md` §12.7, claim M1, line 414: "the
  commit-messages manual states '≤50 chars, imperative, **no
  period**'". The manual now says either mood (§2.2). Stale lines.
- `README.md` lines 9 to 11: Output Shapes "each pinned to the concept
  version it derives from". Same false claim as AGO-5, with no Fact
  Reference. Stale lines.
- `ARCHITECTURE.md` §2, line 131: "What derives from the concept is
  the method, the Stack Group and the playbook", where its own §2.2
  says the Stack Group is "Not derived from the concept but checked
  against it".
- `docs/conventions/agent-arrangement/` §2.4, line 206 to 208: "two
  files disagree while both look current" is claim M2, but the Fact
  Reference names only M1. Wiring.
- `docs/conventions/agent-arrangement/` *What this is made usable as*,
  third entry: no moment (`docs/conventions/conventions/` §2.3). Like
  leftover A1, in another manual.
- `.claude/rules/foundation-check.md` step 1 misses the playbook,
  `delivery/fills/cbc-run-pure-playbook.md`, whose Plan Step Form
  comment carries `foundation: the project-recording convention`. Like
  leftover F10.
- One-home rule 7 and exchange §3.8 put a *Decisions* footer on an
  Output Shape; facts-in-sync §3.4 item 3 says only "A Work Approach",
  and the Idea-to-Output Model's §2 does not count an Output Shape
  one. No shipped Output Shape has a footer today.
- `ARCHITECTURE.md` has a sixth part, *The words*, a one-line pointer;
  project-recording's seat lists five parts. Taste, not listed.
- The leftovers I met (F14, the CHANGELOG line in both `one-home.md`)
  are as the list says.

## Not read

All assigned files were read, with these limits, as the brief and
assignment allow:
- `TODO-CONVERSATION-MEMORY.md`, `.claude/decisions.md` and
  `CHANGELOG.md`: header comments only (history otherwise).
- `TODO.md` and `PLAN.md`: header comments and forms whole; the items
  and Plan Steps read where a seat or rule names them (TODO's
  retrospective item; PLAN's three Plan Step headings and the Birth
  Plan Step whole).
- `project-recording` and `agent-arrangement`: read whole.
- The concept chapters, the Approaches on Trial, `temp/README.md` and
  the repo-hygiene templates carry no Foundation Line; checked for
  one, then skipped as the assignment says.
- `docs/models/agent.md`: §1 to §12 read; it is a foundation, so read
  for the parts its manual uses.
