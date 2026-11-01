<!-- The refinement of this repo, opened 2026-10-18 on
     refinement-2026-10-18. Data only: how this file is made is
     .claude/approaches-on-trial/refinement.md §2. It grows a part
     at each stage, and goes at the close. -->

# Refinement, 2026-10-18

## Before round 1

### Kinds and rounds (§2.1)

Collected from TODO's refinement item, at `b3b2018`. The three
default rounds hold: every kind fits one, and each round has a
kind.

| Round | Kind | What a finding is | The rule |
|---|---|---|---|
| 1 | Stale lines | a line no longer true | none needed: a false line is wrong |
| 1 | Wiring | a link the rules require that is missing or does not resolve: a manual's list of what derives from it, a `foundation` line, a pointer's path or section | `docs/conventions/conventions/` §3.5, steps 1 and 2; §3.2 |
| 1 | Agreement | a manual and what derives from it say different things, read from both sides: each derived file against its manual, and each seat against the files its side holds | `docs/conventions/conventions/` §3.4, §3.5 |
| 2 | One home | a fact told in more than one place | `.claude/rules/one-home.md` |
| 2 | Dependencies | a retelling where a pointer would do, or a pointer not needed | `docs/conventions/facts-in-sync/` §2 |
| 2 | Lessons | a case written as the rule | `docs/conventions/conventions/` §3.7 |
| 2 | Layout | a section that holds two subjects, or one subject spread over several sections | `docs/conventions/conventions/` §3.3, once it says one subject to a section (§2.3) |
| 3 | Writing | all living text, against the whole rule; "text older than ADR-0053" until 2026-10-29, when rules 9 and 10 made every text older than the rule (*Round 3*) | `.claude/rules/writing.md` |

Not a kind: the item's two "words" ideas, "run" as a verb for a
skill or a step, and "small steps" in `commit-plan`. Each is
already found, so nothing is searched for. Round 3 lists them as
Writing findings, against `.claude/rules/writing.md`, rule 6.

Agreement joins two kinds, on the reviewer's word on 2026-10-19:
Foundations, read from each derived file up, and Seats, read from
each seat down. Seats had been in doubt: §3.4 sets no limit on what
a seat says, so "a seat that says too much" had no rule. Read as
agreement between a seat and its side's files, it has one. A seat
that retells another home stays a One home finding.

Wiring was added by the reviewer on 2026-10-19, after the first
confirmation: the links the foundation check walks are checked
first, before round 2 moves text along them.

Layout was added by the reviewer on 2026-10-19, after the rule
check's walk: its problems sit between sections and files, where a
walk one section at a time does not see them.

Also in round 2, joined from its own TODO item: the map of the
records, project-recording §1, in project-recording's layer.

Confirmed by the reviewer, 2026-10-19, before Wiring was added,
and again with it the same day, with Agreement, and with
Layout.

### Files by layer (§2.2)

Living text at `c4c6bc0`: 106 files, each in exactly one layer.
Left out: the devlog's months, the 57 ADRs, all closed, and
`docs/baselines/` (§1); `temp/RUN-4.md`, run 3's text, kept for
run 4's reading; and this file.

| Layer | Files | Count |
|---|---|---|
| 1. The conventions manual | `docs/conventions/conventions/README.md` | 1 |
| 2. Project-recording | `docs/conventions/project-recording/README.md` | 1 |
| 3. The other manuals, the models, the concept | `docs/conventions/README.md`; the 11 other manuals; `docs/conventions/repo-hygiene/templates/` (3); `docs/models/` (2); `concept/` (5) | 22 |
| 4. `ARCHITECTURE.md`, `README.md`, the records | `ARCHITECTURE.md`, `README.md`, `CHANGELOG.md`, `PLAN.md`, `TODO.md`, `devlog/README.md`, `temp/README.md`, `.editorconfig`, `.gitattributes`, `.gitignore` | 10 |
| 5. Our agent setup | `CLAUDE.md`; `.claude/` (13) | 14 |
| 6. `delivery/`, what ships | `delivery/README.md`; `container/` (22); `fills/` (1); `installs/` (1); `method/` (14); `spring-postgres/` (19) | 58 |

Three layers widened, each to hold files that fit none:

- **Layer 3 takes `docs/models/`:** two descriptions of how this
  repo's work is shaped, read like manuals.
- **Layer 4 takes `devlog/README.md`, `temp/README.md` and the
  root's three dotfiles:** each says how a record, a folder or the
  repo is kept.
- **Layer 5 takes `CLAUDE.md`:** the agent's entry file, beside
  `.claude/`.

The writing kind reads the method's texts here too:
`delivery/method/` (14), `delivery/spring-postgres/` (19),
`concept/` (5). One pass, on text rounds 1 and 2 have made true,
against a writing rule just rechecked. TODO's plain-rewrite item
is weighed at the close against what round 3 did.

Confirmed by the reviewer, 2026-10-19.

### The rules' check (§2.3)

TODO searched on 2026-10-19 for each rule's name and its manual's
path. Each manual is read whole, then its rules.

| Manual | Kinds that stand on it | Doubt from | Result |
|---|---|---|---|
| `docs/conventions/conventions/` | Wiring, Agreement, Dependencies, Lessons, Layout | the reviewer; TODO: the manuals' recheck; a moved section outside the descriptions; the reviewer again, after the redesign | fixed: a moved section is grepped at its commit, `7061c89`, `d1fb072`, and its TODO item ended, `8defb6c`; a record's form names its description, `c06943d`, `242d248`; Seats read as Agreement, `83347b8`. Read again after the redesign: the top line states the subject, `ac796df`; "What it is for" says its own need, `4a8c0c3`; the opening statement is the subject in one sentence, `5af7355`; a section holds one subject, `aba2897`; the manual form follows, `d0628b2`. Left to round 1: §1's "holds ten", and nine opening lines that do not fit `5af7355`. Left to round 2: the Layout findings in the note below. |
| `docs/conventions/project-recording/` | One home | the reviewer; TODO: the manuals' recheck | fixed: a link moves when its home moves, `5f3a601`, `c74516b`; a TODO item's story is written when it is added, `06de359`, `2de55db`, `2200e81`. Two findings left to round 1's Agreement: where `PLAN.md`'s step form is described, and what TODO's Now holds, told three ways. |
| `docs/conventions/writing/` | Writing | the reviewer; TODO: the manuals' recheck | fixed: rule 8, start from what the reader holds, tried on a sample the reviewer judged clearer, `8e86560`, `6e56e72`. One finding left to round 1's Agreement: the manual says coined words go in the project's glossary, our rule says `ARCHITECTURE.md`'s *The words*, and the seats do not name the difference. |

Confirmed by the reviewer, 2026-10-19: no rule is in doubt.

Met in the search, not doubts, each with its own trigger: a TODO
item's story written when it is added (project-recording, due); a
rule that writes a skill or rule from its convention (conventions
§2, at this step's close); a check on the worked example's two
copies (one home, rule 5); numbering the concept's sections
(conventions §3.2); a playbook convention (project-recording §9);
the readability pass (the writing rule, at this step's close); the
conventions' full local map.

### Handed over from the redesign (2026-10-19)

The redesign of the conventions ran two iterations on the
conventions manual. Both were refinement work, so the conventions
manual is in doubt again, and the rule check goes through it
section by section, top to bottom, fixing in place.

- **The top line: done,** at `ac796df`. It states the manual's
  subject; "may break only with a reason" stays in §1, its one
  place.
- **"What it is for": agreed, to apply first.** The section keeps
  only this manual's need, then its failure and trigger:

  > So that a way of working has one place that says why it is so,
  > and everything an agent acts on can be traced back to it. A
  > rule can then be questioned against its reason. A change to a
  > reason reaches every rule made from it.
  >
  > What went wrong without it: the rules for conventions lived in
  > the conventions index, against that index's scope, and two of
  > them were rules nobody had followed (ADR-0039). The trigger:
  > the descriptions item filed on 2026-09-27, and the index read
  > against it the next day.

  The general rule it opened with goes: §3.3 holds it. §3.3 gains
  the two details only that sentence held: "the work it makes
  possible", and "after which the need is rewritten from what was
  seen or the convention goes".
- **§3.3's parts, a Layout finding for round 2:** each part of a
  manual gets a numbered part of its own, so a pointer lands on
  one, and `convention-manual.md` then follows part by part.
- **The walk's verdicts,** by the reviewer on 2026-10-19: the top
  line, `ac796df`, kept; "What it is for", `4a8c0c3`, kept.
- **The walk stops after these two.** A walk one section at a time
  mixes the kinds and misses what sits between sections, so the
  rounds take the rest. Three rule fixes come first, in §3.3, the
  form every manual is read against: the opening statement is the
  manual's subject, in one sentence; a numbered section holds one
  subject, and a subject has one section; and
  `convention-manual.md` follows, with "or the convention goes".
- **For round 2, as Layout findings, from the redesign's
  reading:** §3 holds two subjects, how a manual is written (§3.3,
  §3.4, §3.7) and how everything stays in step (§3.1, §3.2, §3.5,
  §3.6); the links between a manual, its rules and other manuals
  are spread over many sections, with no one place. Not a finding:
  "The seats" is this manual's own seats and §3.4 the rule for
  every manual's, two subjects, checked 2026-10-19.
- **Its candidate fix, named 2026-10-20 (ADR-0059):** staying in
  step becomes a convention of its own. Its manual holds the
  general idea: one home, followers and their tags, the re-read on
  change, the walk, a disagreement. Today these sit in
  project-recording §11 and conventions §3.1, §3.2, §3.5 and §3.6.
  Then a rule for each case: ours, manuals tagged by path and
  section and re-read by the walk before every commit; a run's,
  its invariants, kills and slices tagged by id; and records
  linking records.

## Round 1: what is true

Kinds: Stale lines, Wiring, Agreement (§2.1). Read at `ffc6f7c`,
2026-10-19. Line numbers are at that commit.

### The read (§2.4)

Eight readers, each reading for one kind, side by side. Each
finding below was checked against the tree, by its reader and
again before listing: the take's order, the verdicts, the lasting
forms, the plan's confirmation and `ARCHITECTURE.md`'s lines were
read in place.

| Kind | Files covered | How |
|---|---|---|
| Stale lines | all 106: layers 1–3 in two parts (7, 17), layers 4–5 (24), layer 6 in two parts (25, 33) | each file whole |
| Wiring | all 106 | a sweep by script: paths, section numbers, ADRs, relative links, `foundation` lines, each description's list |
| Agreement, our side | 36: the 13 manuals' seats, `.claude/` (13), `CLAUDE.md`, the records, `ARCHITECTURE.md` | each derived file whole beside its manual |
| Agreement, the run's side | 64: `delivery/` but `spring-postgres/` (30), the manuals (12), our copies of shipped files (6), `concept/` (5); `spring-postgres/` (19) swept for concept claims | each derived file whole beside its manual or the concept; each pair of copies diffed |

Agreement covers the files that derive from a description, and
the descriptions. A file with no such link has nothing to agree
with.

Found true, so not listed: the worked example's two copies are
byte-identical; all 31 skills, rules and shapes carry a
`foundation` line naming what exists; all 52 ADRs cited exist;
the method agrees with `concept/` in substance.

### Findings (§2.5)

Collapsed at round 1's close: FINDING-1 to 88, each with its
ending and commit, are in git at `4cd8d0d`, this file's
*Findings (§2.5)*. Every fix is in the text round 2 reads, and the
commits cite each number.

### Decisions

**DECISION-1.** What "manual" means in a run. Rests: FINDING-2.
- (a) The conventions manual and `convention-manual.md` say a run
  writes no convention manual; first-time work's provisional one
  is named as the exception.
- (b) The run's provisional manual gets another name.
- Recommended: (a). The provisional manual is a manual in the
  same sense, only on trial.
- Ending: neither option, by ADR-0058 (`a345760`): the draft is an
  approach on trial, and "manual" keeps one meaning.

**DECISION-2.** Does `working-a-reading.md` stand under the
exchange? Rests: FINDING-22, FINDING-23.
- (a) Yes: the exchange lists it, and its boundary stops sending
  "how the deliverer works a reading" elsewhere.
- (b) No: the rule's `foundation` names commit-plan or
  project-recording.
- Recommended: (a). The rule's line already says so, and
  agent-arrangement and first-time-work point at it.
- Chosen: (a), by the reviewer, 2026-10-20. The exchange lists the
  rule as practice under it, and points at it for how a reading is
  worked. Fixed in round 1's work, layer 3.

**DECISION-3.** Must every section pointer carry the path?
Rests: FINDING-36.
- (a) Yes, every one in living text.
- (b) Only where no path names the file earlier in the paragraph.
- (c) Decline: each lands on the right heading.
- Recommended: (a), but for a shipped file that names a deliverer
  manual a run cannot open (`one-home.md`), which is declined.
  §3.2's reason is the grep, and a name escapes it.
- Narrowed by ADR-0059 (`e9109a6`): a pointer beside a retelling
  always names its path and section
  (`docs/conventions/conventions/` §3.2). Still open: whether every
  plain pointer must carry its path.
- Chosen: (a), by the reviewer, 2026-10-20: every pointer carries
  its path, but the container's `one-home.md`, which names a manual
  a run cannot open. Fixed in each layer's work.
- Widened at round 2's layer 6 (FINDING-205): the container's
  `writing.md` too, which names the deliverer's writing manual.

**DECISION-4.** Does a manual on trial count among the manuals?
Rests: FINDING-37.
- (a) No: `docs/conventions/conventions/` §4 runs step 5,
  `ARCHITECTURE.md`'s count, at first-time work's close. Declined.
- (b) Yes: count it now, and the close uncounts it if dropped.
- Recommended: (a). The count then agrees with the rule today.
- Ending: settled by ADR-0058. The refinement's manual is an
  approach on trial (`1790d09`, `8e5f093`), and `docs/conventions/`
  holds eleven manuals.

**DECISION-5.** Did run 4's birth fire the "next birth" and
"fourth run" triggers? Rests: FINDING-54.
- (a) Run 4's reading weighs each: the three join that TODO
  item's Ideas.
- (b) They fired: each is worked or ended now.
- Recommended: (a). Run 4 was born by hand, outside our steps,
  and its reading is where its birth is read.
- Chosen: (a), by the reviewer, 2026-10-20. The three triggers join
  run 4's reading's TODO item, to be checked there. Moved in round
  1's work, layer 4.

**DECISION-6.** Our three skills identical to the container's:
which tag? Rests: FINDING-60.
- (a) Ours cite `ADR-nnnn`, and stop being identical; three
  manuals' "identical today" change.
- (b) §2 gains one line: a copy identical to its shipped master
  keeps `CBC ADR`.
- Recommended: (b). The numbers name the same ADRs, and a diff
  that comes back empty is the cheapest agreement check there is.
- Chosen: (b), by the reviewer, 2026-10-20. Conventions §2 gains
  the line; "identical" stays where copies are byte for byte, and a
  copy that differs names each difference. Fixed in round 1's work,
  layer 1.

### Counts

88 findings, about 100 before duplicates were merged:

- by kind: 28 Stale lines, 13 Wiring, 47 Agreement, FINDING-21
  counted as Agreement;
- by how they stand, the first word of each: 59 checked, 23
  resting on the reader, 6 uncertain;
- known: all 5 found again, the third as FINDING-11 and
  FINDING-12.

Six decisions.

Ended by the approaches design change, 2026-10-20
(`.claude/approaches-on-trial/refinement.md` §2.7): DECISION-1 and
DECISION-4; FINDING-2, 25, 26, 27, 49, 50 and 62 fixed; FINDING-37
narrowed. 81 findings and four decisions remain.

The four decisions chosen by the reviewer, 2026-10-20: DECISION-2,
3 and 5 as recommended, (a); DECISION-6 as recommended, (b).

Layer 1 worked, 2026-10-20: FINDING-1, 3, 4, 6, 7, 8 and 60 fixed;
FINDING-5 declined.

Layer 2 worked, 2026-10-20: FINDING-9 to 18 fixed; FINDING-36's
project-recording part fixed.

Layer 3 worked, 2026-10-21: FINDING-19 to 24 and 28 to 35 fixed,
FINDING-33's back-link declined, FINDING-34 moved to layer 4;
FINDING-36's layer 3 part fixed, one quoted pointer declined.

Layer 4 worked, 2026-10-21: FINDING-34, 37 to 45, 47, 48 and 51 to
55 ended, DECISION-5 among them; FINDING-46 moved to the
refinement's close; FINDING-57 declined; FINDING-36, 56 and 58
narrowed to layers 5 and 6.

Layer 5 worked, 2026-10-21: FINDING-56 and 59 to 67 ended, our part
of FINDING-61 by the approaches change; FINDING-58 and 36 narrowed
to layer 6, three log pointers declined.

Layer 6 worked, 2026-10-21: FINDING-68 to 76, 78 and 82 to 88
fixed, 79 in part; FINDING-77 and 81 moved to run 4's reading,
82's other half to the method's plain rewrite; FINDING-80 and 79's
other part declined; FINDING-36, 58 and 61 ended. A defect of the
work's own, the container's `visual-comparison` frontmatter joined
by a rewrap in `b6ecf85`, was repaired in `bdeca06`.

### Met in round 1, for round 2

Not findings: true lines, met while working, whose question is
where a fact lives. Round 2 reads them first. The talk behind them
is `TODO-CONVERSATION-MEMORY.md` §7.

1. **The playbook's version in four places:** its own line and the
   seed's three. Tag the copies, or have the seed read the version
   from the playbook at birth.
2. **The seed's retold list of pinned copies,**
   `docs/conventions/exchange/` §3.2. The seed does not ship, so it
   can be tagged, or point instead.
3. **Shipped files that retell a deliverer manual with no tag:**
   `commit-messages`, agent-arrangement §1; `cbc-bootstrap` and its
   walkthrough, repo-hygiene §2 and §3. A run cannot open our
   paths: the run's case of ADR-0059, still to design.
4. **A footer's decision line names the section it backs,** a
   candidate line for `docs/conventions/conventions/` §2. ADR-0030's
   line in `visual-comparison`, and the two added in `0ebac21`, do it.
5. **Footers in shipped files:** their `CBC ADR` lines name ADRs a
   run can never open. Kept as provenance, dropped at delivery, or
   kept with a line saying what they are for.

## Round 1's close read

All 106 living files read again at `9f7e8dd`, 2026-10-21, against
round 1's three kinds (§2.8), by eight readers as in round 1's
read. Each finding was checked against the tree before listing, and
says whether its text changed in round 1 (`ffc6f7c..9f7e8dd`). Where
a finding shows a round 1 fix that missed a place, it says
"reopens". Each carries the agent's proposed ending.

Found true, so not listed: every path, git reference and ADR
resolves; the frontmatter of all 29 skills, rules and shapes is
intact; every `foundation` line names what exists, and every
manual lists back what names it; every identical pair is
byte-identical; the method agrees with the concept.

### Findings

Collapsed with round 1's: FINDING-89 to 134, each with its ending
and commit, are in git at `4cd8d0d`, this file's *Round 1's close
read*.

### The close read's counts

46 findings, FINDING-89 to 134: 25 Stale lines (FINDING-93 counted
here, also Agreement), 5 Wiring, 16 Agreement.

- In text round 1 changed: 15, FINDING-97 counted here, being part
  changed. In text it did not: 31.
- Reopening a round 1 fix that missed a place: 8, those of FINDING-4,
  34, 36, 44, 53, 56, 59 and 85.
- By how they stand: 24 checked, 12 resting on the reader, 10
  uncertain.
- Proposed: 39 fixed, 6 declined, 1 moved to round 3.

The reviewer took all 46 proposed endings, 2026-10-21. None of the
six declines is taste: each line is true, or another item carries
it. The plan worked them by layer: the manuals in `64af2a5`, the records in
`2856421`, ours in `8a7e554`, what ships in `76ec7ef`. One commit
was inserted, `8042a18`: the reviewer's question on FINDING-114's
line became a TODO item.

Round 1 is closed. Round 2 is next: its kinds are in *Kinds and
rounds*. Before it reads, its rule check (*Round 2*, below); when
it reads, *Met in round 1, for round 2* first.

## Round 2: where it lives

Its kinds are One home, Dependencies, Lessons and Layout
(*Kinds and rounds*), with the map of the records,
project-recording §1. It reads *Met in round 1, for round 2*
first.

### The rules' check (§2.3)

What changed since round 1's check, at `775fc16`, and the TODO
items that name each rule, searched 2026-10-25.

| Kind | Rule | Changed since | TODO items naming it | Doubt |
|---|---|---|---|---|
| One home | `.claude/rules/one-home.md`; `docs/conventions/project-recording/` §11 | a retelling may stand where the reader acts on it, tagged to its source (ADR-0059, `0c2149b`, `0148ce1`) | 8 | yes: where the rule lives, and what its tag is |
| Dependencies | `docs/conventions/conventions/` §3.1 | a tagged retelling is a follower, not a second statement (`e9109a6`) | 1 | yes: where the rule lives |
| Lessons | `docs/conventions/conventions/` §3.7 | nothing | 0 | no |
| Layout | `docs/conventions/conventions/` §3.3 | the channel section's tag (`f473d31`, `89e2290`); "a section holds one subject" unchanged | 0 | no |

Two items doubt a rule:

- **"Write the staying-in-step convention"** moves project-recording
  §11 and conventions §3.1, §3.2, §3.5 and §3.6 into a convention
  of their own: both doubted rules change their home.
- **"Define the fact reference"** settles what a tag is, and asks
  that a missing one be found. One home's findings rest on it: a
  retelling without its tag is a second home.

The other six that name one home ask when it is checked, or name it
in passing: the sweep, a session's end, the index as a full local
map, how work is run by agents, which ideas are models, and the
worked example's two copies.

The fix proposed: the staying-in-step convention, with the fact
reference defined in it, landed before round 2 reads, as a commit
plan, each fix judged on §2.3's four questions.

How each check ended, 2026-10-25, under the commit plan for
facts-in-sync (ADR-0065):

- **One home:** in doubt, fixed. Its rule's home moved:
  project-recording §11 rule 1 is now
  `docs/conventions/facts-in-sync/` §1, and both `one-home.md`
  rules stand on it. The tag is named the fact reference, with two
  readers, the agent and the walk (§3). Its form with a title, and
  one name for it, stay open (TODO, the fact-reference item).
- **Dependencies:** in doubt, fixed. Its rule moved whole, from
  conventions §3.1 to facts-in-sync §2.
- **Lessons and Layout:** not in doubt.

The verdict, kept. Before, the rules were told in 5 sections of 2
manuals; now in 1 manual, of 281 lines. The conventions manual went
from 456 lines to 309, project-recording from 954 to 906.

1. **Maintenance:** a change to how facts are kept in sync touches
   one manual, not two.
2. **Readability:** the rules sit in one manual, under one
   statement, not among two manuals' other subjects.
3. **Future-proofing:** the fact reference's written form, when
   settled, changes at §3 alone.
4. **Complexity:** one manual more, twelve in all; 195 lines left
   two manuals and 281 came in, the difference mostly its own frame: the
   opening, the seats, the channel and the boundary.

Two rules also gained a line in the same plan, before round 2
reads. One home: a description states what is true today, so a
history sentence in one retells its ADR (facts-in-sync §4).
Dependencies: a fact reference has one target, the home of the fact
its line relies on (facts-in-sync §3).

Searched again after the plan closed, at `f2a0221`: no TODO item
doubts a rule of round 2's kinds. Four name a rule or its manual
and are due during round 2, its reading their evidence; none
changes a rule:

- "Decide which way a fact reference may point": Dependencies asks
  whether a reference is needed, not which way it points.
- "Decide whether each seat's copy is written for its seat": it
  asks whether the claims that two copies are the same stay, not
  what a second home is.
- "Decide what kind of text our ARCHITECTURE is, and its size":
  facts-in-sync §2 has ARCHITECTURE point, not restate, whatever its
  kind.
- "Move conventions §1 to the idea-to-output model": §3.3 and §3.7
  stay.

Confirmed by the reviewer, 2026-10-25: no rule of round 2's kinds
is in doubt, and round 2 reads.

### Files by layer (§2.2)

Living text at `620fe22`: 112 files, each in exactly one layer.
Left out, as before round 1: the devlog's months, the 65 ADRs, all
closed, `docs/baselines/`, `temp/RUN-4.md` and this file. Also left
out: `temp/reading-run-5-2026-10-22.md`, the reading of run 5, a
draft its own step works after the refinement.

| Layer | Files | Count |
|---|---|---|
| 1. The conventions manual | `docs/conventions/conventions/README.md` | 1 |
| 2. Project-recording | `docs/conventions/project-recording/README.md` | 1 |
| 3. The other manuals, the models, the concept | `docs/conventions/README.md`; the 10 other manuals; `docs/conventions/repo-hygiene/templates/` (3); `docs/models/` (3); `concept/` (5) | 22 |
| 4. `ARCHITECTURE.md`, `README.md`, the records | as before round 1, and `TODO-CONVERSATION-MEMORY.md` | 11 |
| 5. Our agent setup | `CLAUDE.md`, `CLAUDE.local.md`; `.claude/` (16) | 18 |
| 6. `delivery/`, what ships | `delivery/README.md`; `container/` (23); `fills/` (1); `installs/` (1); `method/` (14); `spring-postgres/` (19) | 59 |

What changed since round 1's list, at `c4c6bc0`:

- **Came in, 9:** the facts-in-sync manual and
  `docs/models/idea-to-output.md` (layer 3);
  `TODO-CONVERSATION-MEMORY.md` (layer 4); `CLAUDE.local.md`
  (ADR-0062) and three approaches on trial,
  `approach-drafting.md`, `approach-evaluation.md` and
  `auto-run.md` (layer 5); the container's `approach-drafting.md`
  and `temp/README.md` (layer 6).
- **Moved, 1:** the refinement's manual, from layer 3 to layer 5,
  as `.claude/approaches-on-trial/refinement.md` (ADR-0058).
- **Went, 3:** the first-time-work manual and its two skills, ours
  and the container's (ADR-0058).

No layer widened: each new file fits one as it stands.

### The read (§2.4)

Read at `8acc4d4`, 2026-10-25. Seven readers, one kind and one
side each, side by side. Each checked its findings in the tree. The
agent then checked 25 of them again before listing: every quoted
text held, but one line number of the 25 was wrong. So a finding
below names its path and section, and gives a line only where the
agent checked it.

| Kind | Side | Files covered | How |
|---|---|---|---|
| One home | ours, layers 1–5 | 53 | each whole, then a sweep by grep; `TODO.md` in part, `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md` by header and grep (DECISION-13) |
| One home | what ships, layer 6 | 59 | each whole; the pairs of copies diffed |
| Dependencies | ours | 53 | each whole; `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md` in part (DECISION-13) |
| Dependencies | what ships | 59 | each whole |
| Lessons | ours | 53 | each whole |
| Lessons | what ships | 59 | each whole |
| Layout | all | 112 | the manuals, models, concept, `ARCHITECTURE.md`, `README.md`, `.claude/` and layer 6's skills, rules, shapes and references whole; `PLAN.md`, `TODO.md`, `TODO-CONVERSATION-MEMORY.md`, `CHANGELOG.md`, `.claude/decisions.md`, the templates, the container's records and the dotfiles by headings |

The Layout reader read layer 6 through a fork of its own.

Found true, so not listed:
- every pair of copies that must agree is byte-identical: the
  worked example in `cbc-framing` and `cbc-slice`; our
  `commit-messages`, `commit-plan`, `visual-comparison` and
  `approach-drafting.md` against their masters;
- the two `one-home.md` and the two `writing.md` differ as their
  manuals say;
- all 12 manuals have the nine sections of
  `.claude/rules/convention-manual.md`, in order;
- the concept chapters, the tiers model and the agent model hold no
  case written as a rule and no section with two subjects.

### Findings (§2.5)

Collapsed at round 2's close: FINDING-135 to 228, each with its
ending and commit, are in git at `1a9f76d`, this file's
*Findings (§2.5)* under *Round 2: where it lives*. Every fix is in
the text round 3 reads, and the commits cite each number.

### Decisions

**DECISION-7.** Does a lesson taken (conventions §3.7) reach text
other than manuals? Rests: FINDING-222, 223, 224, 206.
- (a) Yes, every text: a derived file states a rule in general, and
  a case goes or becomes a dated italic.
- (b) Manuals only: the rest is declined.
- (c) Manuals, and the files derived from a convention in both
  seats. The method's and the stack's texts go to TODO's "Rewrite
  the method's texts plain".
- Recommended: (c). The method's texts are rewritten anyway, and a
  second pass now would be undone there. Facts-in-sync §4 already
  says a derived file "applies, it does not explain".
- Chosen: (c), by the reviewer, 2026-10-25. FINDING-222 is fixed
  in this round. FINDING-223, 224 and 206's citations of run 3's
  RETRO move to TODO's "Rewrite the method's texts plain".

**DECISION-8.** Does Layout reach text other than manuals? Rests:
FINDING-180, 227, 228; the reach of 198, 225, 226.
- (a) Manuals only.
- (b) Every description: the manuals, the models, `ARCHITECTURE.md`,
  the concept. Facts-in-sync §3's numbering speaks of any
  "document".
- (c) Every text, skills and approaches too.
- Recommended: (b), with the method's texts left to the plain
  rewrite, as in DECISION-7.
- Chosen: (b), by the reviewer, 2026-10-25, with DECISION-7's line:
  the descriptions, and the files derived from a convention.
  FINDING-198 and 226 are fixed in this round; FINDING-180 when
  TODO's "Move conventions §1 to the idea-to-output model" moves
  text there; FINDING-227 and 228 move to TODO's "Rewrite the
  method's texts plain". FINDING-225 is bound by conventions §2
  either way.

**DECISION-9.** How are §3.3's parts numbered? Rests: FINDING-136.
ADR-0065 kept §3.3, §3.4 and §3.7 and left the gap.
- (a) `#### 3.3.1` and on, under §3.3. Every pointer to §3.3 still
  lands.
- (b) Renumber §3: the option ADR-0065 rejected, now for a change
  of form.
- (c) New numbers after §3.7, out of order.
- Recommended: (a).
- Chosen: (d), raised by the reviewer, 2026-10-25: no gap and no
  third level. TODO's "Move conventions §1 to the idea-to-output
  model" is due, its trigger round 2's read of layer 1, and moving
  §1 shifts every number anyway. So layer 1's work moves §1 first,
  then renumbers the manual once: §1 the artifact, its parts 1.1 to
  1.4 (FINDING-138); §2 the manual, its parts 2.1 to 2.9, one for
  each section of the form (FINDING-136); §3 adding a convention.
  The 28 living pointers into the manual are fixed in that commit
  (`docs/conventions/facts-in-sync/` §3). ADR-0065 rejected a
  renumbering that changed no meaning; this one gives each part of
  the form a home. Splitting the convention in two was weighed and
  not taken: the `foundation` line ties its two halves, and a second
  manual adds its own frame.

**DECISION-10.** Does facts-in-sync §4 step 2, "every line that uses
a part of a document, its root included, carries a fact reference",
reach a derived file's lines about its own manual, and our record
headers? Rests: FINDING-191, 196. On 2026-10-21 the reviewer held
that the `foundation` grep reaches such a line
(`TODO-CONVERSATION-MEMORY.md` §7); §4 step 2 was written later.
- (a) Yes: each such line gains a section reference now.
- (b) No: the `foundation` line covers lines about its own root,
  and §4 step 2 says so.
- (c) Decided in TODO's "Decide how a fact reference is written",
  with the form.
- Recommended: (c). Fixing now, in a form that item may change,
  does the work twice.
- Chosen: (c), by the reviewer, 2026-10-25. FINDING-191 and 196
  move to that item. It is done between round 2 and round 3, with
  "Decide which way a fact reference may point", so round 3 and the
  last read meet the settled form.

**DECISION-11.** Where do the rules of a step live? Rests:
FINDING-144.
- (a) Project-recording. `PLAN.md`'s step form keeps the form, and
  each retelling carries a fact reference.
- (b) `PLAN.md`'s step form. Project-recording points at it.
- Recommended: (a). A description states, and a record's form
  applies (facts-in-sync §4).
- Chosen: (c), raised by the reviewer, 2026-10-25: each holds its
  own fact. `PLAN.md`'s step form, and the playbook's in a run's
  seat, is the home of how a step is worked. Project-recording
  describes what a step is and why, and its seats say where each
  seat's form lives. An agent rule per record was weighed and not
  taken: it hides the rules from a person opening the record, loads
  only after a read, and adds 14 files. It is what the
  idea-to-output model §2 and project-recording's own "the stubs
  state the rules" already say. FINDING-144 is fixed this way; the
  other records' *How* sections go to a TODO item.

**DECISION-12.** Where does "which record answers what" live?
Rests: FINDING-145, and the records map.
- (a) Project-recording §1, the map this step builds. `CLAUDE.md`'s
  table derives from it. README and the codemap point.
- (b) `CLAUDE.md`'s table, as one-home rule 1 says today. The map
  is a summary that names it.
- Recommended: (a), decided with the map's form by
  `visual-comparison`. The map covers both seats; the table, one.
- Chosen: (a), by the reviewer, 2026-10-25, done for both seats,
  as DECISION-11 divides them: each holds its own fact. The map in
  project-recording §1 is the home of what each record is and why,
  one row per record, marked as held by both seats, ours only or
  the run's only, with each difference between the seats said once.
  Each seat's records table derives from it, ours in `CLAUDE.md`
  and the run's in `delivery/container/.claude/CLAUDE.md`: its
  *When* is its own, and its *What's in it* is a summary naming the
  map. README's column, the codemap's descriptions and
  `temp/README.md`'s line point at the map. §13 keeps the when. The
  run's table carries today's fact reference until the shipped form
  is settled, with FINDING-204.
- Refined by the reviewer, 2026-10-26 (ADR-0067): the map is a
  summary that answers which record answers what, home to nothing;
  each item points at its fact's home, and *The seats* keeps the
  differences. The run's table follows the map without naming it.

**DECISION-13.** Are `.claude/decisions.md`'s entries and
`TODO-CONVERSATION-MEMORY.md`'s parts history? Rests: FINDING-192,
and the round's coverage of the two files. The one-home rule's
*Not a second home* names neither.
- (a) Yes: both are dated and never rewritten. Their headers are
  living. The rule's list gains them after the round.
- (b) No: One home and Dependencies read them whole before the
  round's work.
- Recommended: (a).
- Chosen: (a), by the reviewer, 2026-10-25. Their entries and parts
  are history, each header living. FINDING-192 is declined, and the
  round's coverage of both files stands as read. The one-home rule's
  *Not a second home* names neither: that rule is round 2's, so it
  changes at round 2's close, in both seats, in
  `docs/conventions/facts-in-sync/` §1 and both `one-home.md`. A
  living line never takes an entry as a fact's home: FINDING-154's
  fix already moves `TODO.md`'s off one.
- Made at round 2's close, 2026-10-27: facts-in-sync §1 and both
  `one-home.md` name the two logs. The line on taking an entry as a
  home was left out: a run reads its pin from its log's last
  delivery entry (`delivered-copies.md`, rule 1).

**DECISION-14.** Where does the concept's bump rule live? Rests:
FINDING-176.
- (a) `ARCHITECTURE.md` §1.1. `CHANGELOG.md`'s comment carries a
  fact reference, and facts-in-sync §4 names one target. Two edits.
- (b) `CHANGELOG.md`'s comment. §1.1 points, and four pointers
  change.
- Recommended: (a). Three manuals already point at §1.1.
- Chosen: (b), by the reviewer, 2026-10-25, on the agent's changed
  recommendation: DECISION-11 makes a record's form the home of how
  it is kept, and the bump rule is when the CHANGELOG's version
  moves. Project-recording's deliverer seat already says what the
  CHANGELOG is and why. `ARCHITECTURE.md` §1.1 keeps "versioned as a
  whole" and points at the comment; the three manuals and
  facts-in-sync §4 point at it, each keeping ADR-0003 as the why.

### Met in round 2, of other kinds

Not round 2's kinds. Listed so the work can fix them where it
touches the same file, or the last read (§2.9) takes them.

- `TODO.md`: "a `paths:` rule loads only on a Read". Since
  agent-arrangement §5.6, a shell read loads one too.
- `.claude/approaches-on-trial/approach-drafting.md`, both copies:
  "The refinement is open." goes stale at the close.
- `docs/conventions/shapes/`: "a trial for run 4's second slice",
  where TODO's item names run 5's first.
- The container's `.gitignore` names `.claude/settings.json` as "the
  committed shape"; the container ships none.
- `ARCHITECTURE.md` §2.2: two stack skills carry templates;
  `cbc-framing` does too.
- `cbc-bootstrap` and `establishment-walk.md` call the container's
  README a stub; `delivery/README.md` §4 says it carries a composed
  body. Fixed in layer 6, `003407e`.
- `commit-plan`'s frontmatter `requires: project-recording`, a skill
  that does not exist.
- 29 mid-sentence `CBC ADR` citations in the method's and stack's
  texts, against conventions §2.
- `one-home.md` rule 3 says `ARCHITECTURE.md` §1.2 gives "the manual
  for the rest"; §1.2 gives no paths.
- `apply-retrospective`: "Links point at labels, never section
  numbers", against facts-in-sync §3, for the run's seat.
- `system-readiness.md` breaks READINESS-5 "on a branch";
  `cbc-slice` takes the red "in a state that never lands in
  history".
- `cbc-framing-workflow.md`'s "so far" claims, from before runs 4
  and 5.
- `exchange-read` names its phases as steps, not stages
  (conventions §2).
- The refinement's §1 defines its own words outside *The words*;
  round 3's, and its §3 already names "stage".

### The read's counts

94 findings, FINDING-135 to 228, from 114 before duplicates were
merged:
- by kind: 30 One home, 24 Dependencies, 19 Lessons, 21 Layout;
- by how they stand: 71 checked, 20 resting on the reader, 3
  uncertain;
- known before the read: all 5 of *Met in round 1, for round 2*,
  items 1 to 5 as FINDING-200, 201, 202 with 203, 142 and 199; and
  the 3 Layout items from the redesign. Of those, §3 now holds one
  subject, and its stale count goes with FINDING-135. The links are
  still split in two places, FINDING-141 and 175. §3.3's parts are
  FINDING-136;
- proposed: 67 fixed, 4 declined, 5 to TODO, 1 split between a fix
  and TODO (FINDING-179), 4 waiting on the run's case, and 13
  resting on a decision.

Eight decisions, DECISION-7 to 14.

### Endings (§2.6)

The reviewer took the proposed endings, 2026-10-25, as the eight
decisions left them and with one side of each "or" chosen. The
work names each fixed finding's commit.

- **Fixed, 73:** FINDING-135 to 178, 180, 182, 184 to 190, 193,
  197 to 201, 206, 207, 209, 210, 212 to 215, 217 to 219, 222, 225,
  226. 206 and 219 are fixed in part, their rest moved below. Where
  a proposal held an "or", the fix was taken: 151, 158, 172, 177,
  178, 190. FINDING-140 is fixed
  whole, the gap going by DECISION-9. FINDING-135, 137, 138 and 140
  are worked in DECISION-9's renumbering of the conventions manual.
- **Declined, 5:** FINDING-181, the concept's repeated claim, its
  chapter 00 the declared overview; 183, *Where to look* repeating a
  page's pointers, which the form allows; 192, conversation-memory
  being history (DECISION-13); 205, the shipped `writing.md` naming
  the deliverer's manual, round 1's DECISION-3 exception widened to
  name both rules; 221, `approach-drafting.md`'s line labelled for
  the deliverer.
- **Declined in part:** 146's ADR §3.5, small and cited twice; 157's
  exchange §5.4, an example; 198's §2.3 and its four questions;
  207's ten template headers, read when a template is copied.
- **Moved to TODO, 15:**
  - "Decide how a fact reference is written": 191, 196
    (DECISION-10); 202, 204, 208, 216, the run's case of a retelling
    (ADR-0059), which no item tracked; 219's paths within a skill;
    220.
  - "Rewrite the method's texts plain": 223, 224, 227, 228
    (DECISION-7 and 8), and 206's citations of run 3's RETRO.
  - "Decide how work is run by agents": 194.
  - "Decide whether each seat's copy is written for its seat": 195.
  - "Decide whether cbc-bootstrap points at the Spring hygiene
    parts": 203.
  - "Decide how an approach and a shape divide an output": 211.
- **Split, 1:** FINDING-179. "Approach" is fixed; "description"
  moves to "Decide what kind of text our ARCHITECTURE is".

None of the five declines is taste alone: each line is true, or
history, or another item carries it.

## Round 2's close read

All 114 living files read again at `d37a08f`, 2026-10-27, against
round 2's four kinds (§2.8), by seven readers as in round 2's read:
One home, Dependencies and Lessons in each seat, Layout across both.
Each reader checked its findings in the tree, and the agent checked
25 of them again before listing, with lines joined; every quote
held. Each finding says whether its text changed in round 2
(`8acc4d4..d37a08f`), and "reopens" where a round 2 fix missed a
place. Each carries the agent's proposed ending. Three findings two
readers made are merged, one is split by seat, and three come from
what readers met in passing (FINDING-250, 257, 264).

Found true, so not listed:
- every `§` pointer in our 53 files read whole lands on a heading
  (532), and every root path in what ships resolves in the run's
  tree;
- every section renumbered or split in round 2 holds one subject,
  its parts numbered, and no living pointer names an old number;
- the pin, the sweep, the `foundation` line, the fact reference,
  where the concept lands, the bump rule and what this repo is each
  have one home, the other tellings pointing;
- the worked example's two copies are byte-identical; our three
  convention skills differ from the container's only as ADR-0069
  allows; `approach-drafting.md` is one text in both seats;
- round 2's other fixes hold.

### Findings

Collapsed at round 2's close: FINDING-229 to 281, each with its
ending and commits, are in git at `1a9f76d`, this file's *Round 2's
close read*.

### Decisions

**DECISION-15.** When is a bold lead a part
(`docs/conventions/facts-in-sync/` §3.2)? Rests: FINDING-252. The
rule says bold emphasis inside running prose is not a part, and
says nothing of a bold-led bullet. `79bc4a2` read commit-plan §2's
bullets as parts. Read that way, 16 more sections in 10 documents
are unnumbered parts: facts-in-sync §1; writing §1;
agent-arrangement §4; project-recording §12 and §14; retrospective
§2 and §3; shapes §2; repo-hygiene §2; idea-to-output §5 and §8;
the agent model §5, §10 and §11; the refinement's §1 and §3. Bold
labels on their own line are the same question: project-recording
§1's group labels, the commit-plan skill's §6, two in
`apply-retrospective`.
- (a) Every bold-led bullet is a part: number all of them.
- (b) A bold-led bullet is a part when it holds a paragraph of its
  own, with its own reason or dated case; a short list item is not.
  Commit-plan §2 stays; FINDING-252's two sections are numbered;
  the rest are judged against the line at the last read.
- (c) A bullet is never a part, only a heading is; commit-plan §2
  goes back to bullets.
- Recommended: (b). It keeps `79bc4a2` and the pointers into
  commit-plan §2.10 and §2.13, and gives the rule the line it lacks.
  A rule round 2 reads against does not change mid-round (§2.4), so
  the line lands after round 2 closes, before round 3's rule check,
  and FINDING-252 is worked with it.
- Chosen: (b), by the reviewer, 2026-10-27. The line, and
  FINDING-252, are TODO's "Write when a bold lead is a part".

### The close read's counts

53 findings, FINDING-229 to 281: the readers' 52, three merged, one
split, three raised from what they met in passing:
- by kind: 17 One home, 19 Dependencies, 10 Lessons, 6 Layout, and
  1 of another kind, Agreement;
- in text round 2 changed, in whole or in part: 22; in text it did
  not: 31;
- reopening a round 2 fix that missed a place: 32;
- by how they stand: 41 checked, 9 resting on the reader, 3
  uncertain;
- proposed: 50 fixed, 2 declined, 1 resting on DECISION-15;
  FINDING-249 declined in part, and FINDING-256's second half to
  TODO.

One decision, DECISION-15.

### Endings (§2.6)

The reviewer took the proposed endings, 2026-10-27:
- **Fixed, 50:** FINDING-229 to 281 but those below. The work names
  each commit.
- **Declined, 2:** FINDING-234, the map's pictures being ADR-0067's
  form; 268, a step applying §1's rule where it is acted on.
- **Declined in part:** 249's project-recording §13 italic, true and
  about its own number.
- **Moved to TODO:** 252, with DECISION-15's line, to "Write when a
  bold lead is a part"; 256's second half to "Decide how a fact
  reference is written".

The reviewer took all 53 proposed endings, and DECISION-15 as
recommended, 2026-10-27. Neither decline is taste: each line is true
where it stands. The plan worked the fixes by layer, in ten commits:
- the manuals in `2d1e5bd`, `78c51bf`, `de7238c` and `a2d446d`;
- the records in `6c83d84`;
- ours in `1c6c35c`;
- what ships in `89b8b35`, `4fab07b`, `b2368c6` and `7857b48`.

No commit was inserted. Two choices a proposal left open were shown
at their boundary: the glossary's "harvest" points at the tiers
model alone (FINDING-254), and `visual-comparison`'s two cases go
rather than take a date (FINDING-265).

Round 2 is closed. Round 3 is next: its kinds are in *Kinds and
rounds*. Before its rule check comes the work due at round 2's
close:
- DECISION-13's change to the one-home rule's *Not a second home*;
- TODO's four items whose trigger is round 2's close.

When round 3 reads, *Met in round 2, of other kinds* comes first.

## Round 3: how it reads

Its kind is Writing (*Kinds and rounds*), read against the whole of
`.claude/rules/writing.md` and its manual. It reads *Met in round
2, of other kinds* first. Rules 9 and 10 are newer than every text,
so the row's "text older than ADR-0053" is widened on 2026-10-29:
round 3 reads all living text against the whole rule.

### The rules' check (§2.3)

What changed since round 2's check, at `f2a0221`, and the TODO
items that name the rule or its manual, searched 2026-10-29.

| Kind | Rule | Changed since | TODO items naming it | Doubt |
|---|---|---|---|---|
| Writing | `.claude/rules/writing.md`, on `docs/conventions/writing/` | rule 6 names `docs/glossary.md`, a file of its own since `8919dac`, grouped and pointing at its homes (`38a7c2d`, `06be504`, `42abf12`); the rule's lines carry fact references (`ed96ed0`, ADR-0070); the manual's lesson notes point at their stories (`ae53ed7`, ADR-0073); rule 9, a word with more than one meaning here carries its subject, with the glossary's two kinds of entry (`fe8e7ef`..`793f675`, `4157c23`, ADR-0074); rule 10, a title names its subject (`0567e8d`, `5654381`, ADR-0075) | 6 | yes, three |

The six items: "List the remaining words with more than one meaning
here" and "Retitle the numbered sections to labels", due at this
check; "Decide how an edit or a new text is shaped, line width
included", due at this check; "Rewrite the method's texts plain" and
"Try a readability pass", due at the close, the round's reading
their evidence; and the examples item, which names `writing.md` in
passing. The first and the third doubt the rule; the retitle item
waits on rule 10 being tried.

**Doubt 1: rule 9, tried on the ten candidate words.** The item's
list, measured over the living text on 2026-10-29:

| Word | Uses | Ours | Plain, or another sense | Taken |
|---|---|---|---|---|
| run | 1,382 | the repository, 964 | the verb, 238 | second kind: cbc run, so a bare "run" is English; the reviewer's choice over the test, which found one noun sense |
| step | 635 | PLAN's step, about 420 | a numbered step in a text, "step 4", 131; a casual phase, "the first step from a convention to a model" | second kind: plan step; a text's step named by its owner, "the walk's step 3"; a casual use stays bare |
| skill | 605 | a skill file | none | not listed |
| stage | 401 | a skill's stage, 228; an approach on trial's stage; the exchange's staging, 37 | git's staged and the verb, 52 | second kind: skill stage, approach stage; delivery staging keeps its entry; the exchange's verb names its object, "stage a delivery", since git's verb is the same word |
| model | 336 | our models, 270 | the Claude model, 29; the data and role model, the adversity model and the world model in what ships | second kind: idea model; the agent, tiers and idea-to-output models keep their names |
| take | 229 | the run's take, 18 | the verb, 211 | second kind: a cbc run's take; the reviewer's choice, as for run |
| log | 156 | the decisions log, 33 named and up to 82 bare | git log, 10; the verb, 31 | second kind: decisions log |
| fill | 147 | the noun, a body written into a record stub, 7 | the verb, 115 | the noun goes: "composed body" |
| master | 86 | the deliverer's copy | none here | first kind stays |
| tag | 47 | the repo tag CBC, 19 | the method's tags; git's tag, 1 | second kind: repo tag |

The trial found the clause for a first-kind word too strict in two
ways, each fixed in the manual before the round reads:

- a word of another part of speech is another word: "a run" is ours
  and "it runs" is English; without this, 238 verbs "run" and 211
  verbs "take" break the clause for no reader's gain;
- a listed word's entry names every sense in use, each with its
  subject, ours and others' alike: "git log" beside "decisions log",
  "the Claude model" beside "idea model". The entry is a contents
  page: one line per sense and the address of the home that defines
  it. A use stays bare only where it is casual English and no subject
  would be true of it. The agent first proposed a weaker form, a
  mark on a first-kind word's plain use, with model and then step as
  its case; the reviewer asked for the whole catalogue, and no
  first-kind word needs the mark once those two are listed.

Both change ADR-0074's decision 2 in part. The same trial moved
where rule 9's old text is reworded: about 800 lines, which
ADR-0074 put in round 3's read as findings, go instead to a
scripted-and-hand pass by layer before the read, in one plan with
the retitle, so the read lists only what the pass missed. That
changes ADR-0074's decision 8 in part. Both are ADR-0076.

**Doubt 2: rule 10, tried on commit-plan §2's thirteen titles,**
all statements, eight past 30 characters. Labels proposed and judged
by the reviewer, 2026-10-29:

| Now | Label |
|---|---|
| Its own convention, and not a record | A convention, not a record |
| Root placement | Root placement |
| No status in the file | Status in the file |
| Material-first is a first-class mode, not a failure | Material-first |
| The records commits are planned | The records commits |
| A plan counts commits | What a plan counts |
| An inserted commit takes a letter; a commit may repeat | Inserted and repeated commits |
| Subjects are counted where they are first written | Counting subjects |
| The agent's files are a commit of their own | The agent's files |
| The sweep, before the close and unwrapped | The sweep |
| Small steps inside a planned commit, on the reviewer's grant | Small commits |
| A look back before the close | The look back |
| The stop at every boundary is commit-messages' rule | The stop at every boundary |

The reviewer: they read right. Rule 10 holds as written; the
thirteen land with the rest in the pass. One label shows rule 9 at
work: "Small steps" used PLAN's word in its plain sense.

**Doubt 3: the item on how an edit is shaped,** due at this check.
Measured 2026-10-29: 985 lines over 72 characters in 83 of 99 living
Markdown files, tables aside; a scripted rewrap has broken structure
twice. The reviewer took one rule, writing rule 11: an edit changes
the lines its change needs and leaves the rest as they stand;
Markdown has no line width here, and nothing is rewrapped to one.
The 72 stays commit-messages' alone. ADR-0077. Not taken: a width
shown as a guide in `.editorconfig`, or a change about as long as
what it replaces.

The fixes landed before round 3 reads, under the commit plan for
round 3's rule check, 2026-10-29. How each doubt ended:

- **Doubt 1, rule 9:** in doubt, fixed twice. The catalogue above
  landed first (`fc00f67`): seven words with a prefix, every sense
  listed. At its boundary the reviewer read "staging" and saw that
  the problem was not words but about thirty defined things, each
  hung on one English word, so a reader decided at every use which
  was meant. Rule 9 is now one sentence: every defined thing has a
  Glossary Name of two or more words, owner or kind first, each word
  capitalized; a lowercase word is English (`ec1f048`). The table's
  *Taken* column is replaced: CBC Run, Plan Step, Skill Stage and
  Approach Stage, Delivery Staging, Idea Model, Delivery Take,
  Decisions Log, Repo Tag, Master Copy; "fill" the noun went; skill
  is not a thing of ours. The glossary is the list of 41 Names, each
  pointing at its home; the two kinds of entry, the first-kind
  clause, the move rule and the catalogue went with it. Our
  `writing.md` (`cb4dc61`), the container's and the glossary Skill
  Template in `cbc-framing` (`3e4a7f5`) follow. ADR-0076 was
  rewritten whole while Proposed (`5a9e6ac`) and is Accepted
  (`c65d04e`); it changes six of ADR-0074's decisions in part.
- **Doubt 2, rule 10:** not in doubt. The rule gained one clause, a
  Glossary Name inside a title keeps its capitals (`ec1f048`); the
  thirteen labels wait for the pass.
- **Doubt 3, an edit's shape:** in doubt, fixed. Rule 11 is in the
  manual with its why (`de3f171`) and in both `writing.md`; ADR-0077
  is Accepted (`c65d04e`).

The verdict on rule 9, kept:

1. **Maintenance:** one sentence and no list of words to keep. A
   Name is given at the commit that first uses the thing, by one
   question: does the text give the word a meaning English does not.
2. **Readability:** the capitals say a word is defined before it is
   read, as a contract's "the Deliverer" does; two words say what the
   thing is and whose.
3. **Future-proofing:** a new thing gets a Name and nothing else
   changes; no collision reopens the rule, since a lowercase word is
   never ours.
4. **Complexity:** the glossary lost its two kinds, its clause, its
   move rule and the catalogue. The cost is the pass: about 3,000
   lines, 964 of them "run", taken before round 3 reads so that the
   read lists only what the pass missed.

Searched again at the plan's close: no TODO item doubts the rule.
Two are due now, before round 3 reads, and ride in one commit plan:
the pass that gives old text its Names and its titles their labels,
and the history told inline in six living texts, found when rule 9's
why was first written as a story. The two items due at the close
stand, the round's reading their evidence.

### Files by layer (§2.2)

Living text at `124ae80`: 115 files, each in exactly one layer. Left
out, as before round 2, with `temp/run-6-briefing.md` and
`temp/run-6-handoff/`, run 6's own text.

| Layer | Files | Count |
|---|---|---|
| 1. The conventions manual | `docs/conventions/conventions/README.md` | 1 |
| 2. Project-recording | `docs/conventions/project-recording/README.md` | 1 |
| 3. The other manuals, the models, the concept | as round 2, and `docs/glossary.md` | 23 |
| 4. `ARCHITECTURE.md`, `README.md`, the records | as round 2, and `docs/adr/README.md` | 12 |
| 5. Our agent setup | as round 2, and `.claude/approaches-on-trial/model-placing.md` | 19 |
| 6. `delivery/`, what ships | as round 2 | 59 |

What changed since round 2's list, at `620fe22`: three came in, the
glossary (layer 3, ADR-0070's homes), the ADR folder's form (layer
4) and `model-placing.md` (layer 5); none went; no layer widened.
At the read, `00420b9`, 115 still: in layer 6 the glossary Skill
Template left and `delivery/container/docs/glossary.md` came in, the
Names pass's work.

### The pass before the read

The pass that gives old text its Glossary Names and its titles their
labels ran 2026-10-29 to 2026-10-30 as the commit plan "the
Names-and-labels pass", `4a15920` to `fbc4294`, 21 commits: 17
planned, two revisions of the plan, two inserted for the sweep's
fixes, 14a and 14b. Its order was the Refinement Layers' order; the
history item of 2026-10-29 rode first, as commit 2. The hand read
every living file whole; a script, kept in the session's scratchpad
and never committed, capitalized the lowercase Names the hand
confirmed, replaced the italic title in every Fact Reference to a
retitled section, and counted headings, references, front matter and
code fences before and after each commit.

**Counts.** Measured at the opening, 2026-10-29, over 92 files, and
at the close, 2026-10-30, at `fbc4294`, over 90: the glossary Skill
Template left and the shipped glossary came in, and the close's script
was rebuilt after a compaction, so the two file lists differ by one
convention file each way.

| Measure | Opening | Close |
|---|---|---|
| lines that spell a Glossary Name in lowercase | 171 | 50, all the fixed heading *What this is made usable as* and the verb "made usable" |
| lines that carry a bare word ending some Name | 5,131 | 4,724, English where read: "it runs", "step 4 of the walkthrough", "the shape a CBC Run gets" |
| numbered titles | 360 | 360 |
| of them past 30 characters, or with a gloss | 174, and about 230 statements among the rest | 19, each kept by a decision below |
| Fact References whose title differs from its heading | not measured | 0 in living text; 1 in the plan file, deleted at the close |

**What the hand changed beyond the script.**

- Eight things found defined without a Name got one: Delivery Fill,
  Run Ask and Foundation Check in the manuals; Concept Repo, Run Repo
  and Concept Garden in the Tiers Model; Change Set in the commit-plan
  manual; Master Copy was already Named. Each entered
  `docs/glossary.md` in its commit.
- The CBC Run's glossary is a Record Stub born filled,
  `delivery/container/docs/glossary.md`: 27 Names the shipped texts
  use, one plain sentence each from the CBC Run's side; the CBC Run
  adds its own below. cbc-framing's glossary Skill Template left, and
  the skill says framing adds each thing it defines as a Glossary
  Name.
- The four Output Shapes are titled by their output: the Kill Shape,
  the Evidence Test Shape, the Registry Entry Shape, the Slice Record
  Shape.
- The method's and the stack's own words stayed: slice, kill, fold,
  framing, promise, census, witness, wall, harness, ground. They are
  the concept's, and the five concept chapters left the pass
  untouched.
- The container's `approach-drafting` is byte-identical to ours
  again; `visual-comparison`'s footer is two pointers; the playbook
  is v11; the Pure Seed's prompt says "one commit at a time" where
  "step" meant a commit; its sed cuts the playbook at *The
  Plan Step Form*.
- The sweep ran before the close, over the 90 files unwrapped, by
  two checks: every Name spelled in lowercase, and every Fact
  Reference's title against the heading it points at. It found seven
  stale titles and thirteen lowercase Names, fixed in 14a, 14b and
  the agent commit; the plan's "cut form with …" grep found nothing
  the title check had not.

**Kept by decision, and so left to the read as settled.**

- ARCHITECTURE.md's seven area titles keep their paths after the
  dash (the plan's decision).
- The two walks of `infra-establish` keep their nine stage and step
  headings' words; `spring-boot-walkthrough`'s two long step headings
  the same. Rule 10 leaves stage headings alone; only "1 ·" became
  "1." (commit 13's boundary).
- The manual form's fixed headings keep their words, *The seats*,
  *What this is made usable as*; "made usable" as a verb is English.
- `.claude/decisions.md`'s entries are history and keep their words.

**Left to the read.** `shapes-lifecycle.md` §4, *When an Output
Shape names work*, is 31 characters. The other writing rules, 1 to 8
and 11, were not read in the pass; the hand changed words and titles
only. Round 3 reads all living text against the whole rule, so its
Writing findings are what the pass missed, not the pass.

### The read (§2.4)

Read at `00420b9`, 2026-10-30. Living text: 115 files, the list at
`124ae80` with one change, in layer 6: the glossary Skill Template
left and the CBC Run's glossary, `delivery/container/docs/glossary.md`,
came in. Nine readers, one Refinement Layer or part of one each, side
by side, each file whole, against rules 1 to 10; rule 11 governs
edits, so nothing was read for it. A script swept all 115 files first
for three things: a numbered title past 30 characters or with a gloss
(rule 10), a Glossary Name spelled in lowercase (rule 9), and each
Fact Reference's title against the heading it points at (rule 6).
Each reader re-read its quotes after writing. The agent then checked
every finding's first quote against the tree by script: 597 of 644
matched at the line named; the 47 the script could not parse were
sampled by hand, 7 of them, and all held. A finding names its path,
its section and its line; line numbers are at `00420b9`.

| Reader | Files covered | How |
|---|---|---|
| A | layers 1 and 2: the conventions manual, project-recording (2) | each whole |
| B | layer 3: the index, agent-arrangement, commit-messages, commit-plan, exchange, facts-in-sync (6) | each whole |
| C | layer 3: repo-hygiene and its 3 templates, retrospective, shapes, visual-comparison, writing, `docs/glossary.md` (9) | each whole; the writing manual as a text under its own rule |
| D | layer 3: the 3 Idea Models, the 5 concept chapters (8) | each whole; a chapter's proposals marked editorial or not |
| E | layer 4: the 12 records and folder forms | each whole; `TODO-CONVERSATION-MEMORY.md` by header and headings, `CHANGELOG.md`'s released entry read as history |
| F | layer 5: `CLAUDE.md`, `CLAUDE.local.md`, `.claude/` (19) | each whole; `.claude/decisions.md` by header; the container's 4 copies diffed and read with ours |
| G | layer 6: `delivery/README.md`, the Pure Seed, the playbook, the Container Group but those 4 (23) | each whole |
| H | layer 6: the Method Group (13) | each whole; the worked example once for both copies |
| I | layer 6: the Stack Group (19) | each whole; the yaml, sql, properties and conf templates by their comments |

Checked first:

- ***Met in round 2, of other kinds*, 14 items.** Gone, 7: TODO's
  "loads only on a Read" (`3d70b55`); shapes' "second slice"
  (`ae53ed7`); `ARCHITECTURE.md` §2.2's templates (`1e6870f`); the
  container README called a stub (`003407e`); `commit-plan`'s
  `requires:` (`aa01710`); one-home rule 3's "the manual for the rest"
  against §1.2, which gives each manual's path since `f18f280`; the
  refinement's words, Names since `ec1f048`. True as it stands, 1:
  `apply-retrospective`'s "Links point at labels, never section
  numbers" agrees with facts-in-sync's *The CBC Run's seat*, where a
  bare id is a CBC Run's Fact Reference. True today and stale at the
  close, 1: `approach-drafting.md`'s "The refinement is open.", both
  copies; the close's "now, today or not yet" check takes it. Still
  true, 5, listed: the `.gitignore` comment, FINDING-923; the
  mid-sentence `CBC ADR` citations, FINDING-924; readiness "on a
  branch", FINDING-925; `cbc-framing-workflow.md`'s "so far", with
  FINDING-786; `exchange-read`'s "four steps", FINDING-672.
- ***Kinds and rounds*' two words.** "small steps" in `commit-plan`:
  FINDING-671. "run" as a verb for a skill or a step: not a finding;
  since ADR-0076 a lowercase word is English, and the pass read "it
  runs" so.
- **The pass's one title left to the read,** `shapes-lifecycle.md`
  §4: FINDING-922.
- **TODO's items due at this read:** none. Nine are due at the
  refinement's close; two name the round's reading as their evidence,
  "Rewrite the method's texts plain" and "Try a readability pass".

Found true, so not listed:

- 375 numbered titles, 360 outside `TODO-CONVERSATION-MEMORY.md`'s
  parts. 29 are past 30 characters or carry a gloss: `ARCHITECTURE.md`'s
  7 area titles and the walks' 11 headings, kept by the pass's
  decision, the first reopened in DECISION-31; 10 in the Conversation
  Memory's parts, history; 1 listed, FINDING-922.
- 951 section references with a title, 367 of them with a path: each
  points at a heading with that title, but one, FINDING-586, and the
  seven cut at `ARCHITECTURE.md`'s dash, DECISION-31.
- 59 lines spell a Name in lowercase: 28 the fixed heading *What this
  is made usable as* or the verb "made usable"; 23 in history, the
  Decisions Log's entries and the Conversation Memory's parts; 1 a
  devlog title quoted; 7 listed, in FINDING-607, 657, 690 and 708.
- Every pair of copies that must agree does: the worked example is
  byte-identical, `approach-drafting.md` is one text in both seats,
  and our `commit-messages`, `commit-plan` and `visual-comparison`
  differ from the container's as ADR-0069 allows.
- Rule 11: no living file states a width for Markdown or asks for a
  rewrap.
- Rule 4 in the manuals' *What it is for* sections, the Agent Model's
  claims, the method's worked example and the stack's references:
  every size claim carries its number.

### Findings (§2.5)

By Refinement Layer, in the order the work takes them. Each says its
rule, or its kind where it is of another kind, how it stands, and its
reader's proposed ending; a count inside a finding is the reader's, of
the lines in that section that break the rule the same way. A
reader's "the brief" is the reading brief each was given: the rules'
letter, the decisions already settled, and the concept's words left
out. The numbering follows the readers' lists, FINDING-282 to 925.

#### Layer 1: the conventions manual

##### `docs/conventions/conventions/README.md`

**FINDING-282.** rule 8; resting on the reader. `docs/conventions/conventions/README.md` *What it is for* (line 20): "descriptions item filed on 2026-09-27, and the index read against". A label the reader does not hold: "the descriptions item" is a TODO item no longer in `TODO.md` (grep finds the words only here and in `temp/`), and nothing says what it asked. Proposed: say it in plain words ("the TODO item that asked for a description of each convention, filed on 2026-09-27"), or point at devlog 2026-09-28.

**FINDING-283.** rule 2; resting on the reader. `docs/conventions/conventions/README.md` *What this is made usable as* (line 31): "it points: the chain, relations only (ADR-0032), and one line sending a reader here and to the map". One bullet carries three facts in one chained sentence: what the index holds, that it holds relations only, its one outward line. Proposed: "it points. It holds the chain, relations only (ADR-0032). One line sends a reader here and to the map (…)."

**FINDING-284.** rule 8; resting on the reader. Same section (line 31): "the chain". Met here first with no plain words; §3 step 4 (line 274) is the first to say it is the order the conventions act in during a piece of work. Proposed: "the chain, the order the conventions act in during a piece of work, relations only (ADR-0032)".

**FINDING-285.** rule 6; uncertain. Same section (line 32): "(`ARCHITECTURE.md` §1.2, *The conventions…*)", also line 277. The italic title is cut at the dash with an ellipsis; the heading is "The conventions — `docs/conventions/`". The same cut stands in `.claude/rules/one-home.md` rule 3, so it may be a settled form. Question for the reviewer: settled form, or waiting on ARCHITECTURE.md's §1.2 heading losing its gloss under rule 10 (not in this layer)?

**FINDING-286.** rule 3; checked. `docs/conventions/conventions/README.md` §1, *A convention's artifacts* (lines 49–52): "A skill file for a rule bound to a moment; an Agent Rule for a rule bound to a path, or, with no path, to every task; Record Stubs and templates for rules that ride in the files a project is born with." Three kinds of artifact chained with semicolons in one sentence; a list would show the count. Proposed: a three-item list, one kind per line, led "An artifact is one of three:".

**FINDING-287.** rule 5; resting on the reader. §1 (line 51): "rules that ride in the files a project is born with"; *Why it arrives this way* (line 296): "The Foundation Line rides in the frontmatter of every shipped skill". "Rides in" is a figure for "sits in". Proposed: "rules that sit in the files a project is born with"; "The Foundation Line sits in the frontmatter … and travels with the file".

**FINDING-288.** rule 9; resting on the reader. §1 (line 51): "Record Stubs and templates for rules". The thing meant is the Skill Template (the glossary's Name: a file under a skill's `templates/`, copied and filled by the project); "templates" is lowercase. Proposed: "Record Stubs and Skill Templates for rules".

**FINDING-289.** rule 2; checked. §1.1, *How a rule is written* (lines 66–72): "A skill or an Agent Rule lists the decisions it rests on once, in a footer headed *Decisions*: each as `CBC ADR-nnnn` in one that ships, `ADR-nnnn` in one that stays here, the Repo Tag being `project-recording`'s rule (…), and a decision this repo inherited is adopted before a shipped file cites it (ADR-0038)." One sentence, four ideas: the footer; the citation's form by seat; whose rule the Repo Tag is; the adoption rule. Proposed: three sentences: the footer; "A shipped one cites `CBC ADR-nnnn`, one that stays here `ADR-nnnn`; the Repo Tag is project-recording's rule (…)."; "A decision this repo inherited is adopted before a shipped file cites it (ADR-0038)."

**FINDING-290.** rule 9; uncertain. §1.1 (line 74): "Say what a rule is not only when a consumer lived the misreading, and then name the CBC Run." "Consumer" is a lowercase word for the project holding the artifact; the sentence then names a CBC Run. Question: is a consumer a CBC Run (then the Name) or any project holding a copy, this repo included (then English, no finding)?

**FINDING-291.** rule 9; resting on the reader. §1.1 (line 69): "the Repo Tag being `project-recording`'s rule"; §2.5 (line 221): "The facts-in-sync manual asks the same of a convention's subject across the manuals". The glossary's header says a convention is named by its path in backticks or by its Name, never by the bare word; `project-recording` is backticked but is not the path, "facts-in-sync" is bare. Proposed: "`docs/conventions/project-recording/`'s rule"; "`docs/conventions/facts-in-sync/` asks the same".

**FINDING-292.** rule 2; resting on the reader. §1.3, *The Foundation Line* (lines 97–99): "`foundation` says what the whole file stands on *now* — a live claim, never history — and a file has one". Three ideas joined by dashes and "and": what the line says; that it is live; that a file has one. Proposed: "`foundation` says what the whole file stands on now. It is a live claim, never history. A file has one (…)."

**FINDING-293.** rule 2; resting on the reader. §2, *The Convention Manual* (lines 154–156): "It explains and points at the ADRs; the artifact says what a project does, and its `foundation` line names the manual it derives from." Three ideas chained with a semicolon and "and". Also lines 170–172: "A section two manuals need becomes the next candidate: a pair recurred, the test an Output Shape is written by (…)" packs the rule and its reason into one sentence. Proposed: split each into two sentences.

**FINDING-294.** rule 5; uncertain. §2 (lines 168–169): "The list is the floor, and content that fits none of it takes its own heading in the body." "Floor" stands for "the least a manual has"; the same figure heads `.claude/rules/convention-manual.md` (*The list is the floor, not the ceiling*). Question: dead metaphor (as in a price floor), or write "The list is the least a manual has"?

**FINDING-295.** rule 5; checked. §2.2, *What it is for* (lines 192–193): "Never intent dressed as evidence." "Dressed as" is the costume figure CBC Run 3's retrospective names as a word to drop (`docs/conventions/writing/` §2, *Why each rule*, rule 5). The same words stand in `.claude/rules/convention-manual.md` line 36, derived from this section. Proposed: "Never a wish written as evidence", with the rule's own gloss: "so that X is easier" is not a need.

**FINDING-296.** rule 2; resting on the reader. §2.2 (lines 188–191): "Or as intent marked on trial, with what would make it evidence and when to look again, after which the need is rewritten from what was seen or the convention goes." Four ideas in one sentence. Proposed: "Or as intent marked on trial. The mark says what would make it evidence, and when to look again. Then the need is rewritten from what was seen, or the convention goes."

**FINDING-297.** rule 3; resting on the reader. §2.3, *The list of derived artifacts* (lines 197–199): "every derived artifact, by path from the repo root, each marked shipped or the Concept Deliverer's, with the moment it opens at, placed as the answer to the need." Four requirements on an entry chained with commas, plus where the list sits; the count is hidden. Proposed: a list: each entry has (1) its path from the repo root, (2) shipped or the Concept Deliverer's, (3) the moment it opens at; the list is placed as the answer to the need.

**FINDING-298.** rule 2; checked. §2.4, *The seats* (lines 205–207): "A convention has two Convention Seats, the CBC Run's and the Concept Deliverer's, and a manual names both: what each does under it, the CBC Run first — what each holds is the list in *what this is made usable as*." Four ideas in one sentence: two seats; the manual names both; what it says and in what order; where what each holds lives. Proposed: "A convention has two Convention Seats, the CBC Run's and the Concept Deliverer's. The manual says what each does under it, the CBC Run first. What each holds is the list in *What this is made usable as*."

**FINDING-299.** rule 6; uncertain. §2.4 (line 207, and lines 212–213): "*what this is made usable as*". A reference to a fixed heading, in italics and lowercase; the heading reads "What this is made usable as". Rule 9 exempts the fixed heading from being a Name; whether a reference to it writes the heading as it is is the open question. Proposed: write "*What this is made usable as*" in both places, or decline as English.

**FINDING-300.** rule 2; resting on the reader. §3, *Adding a convention*, step 6 (lines 278–281): "What the Concept Deliverer holds of it, derived from the manual: for a skill, its own under `.claude/skills/`, in its own agent-scoped commit, with an entry in `.claude/decisions.md` when it changes how this repo's agent works." Four ideas in one sentence. Proposed: split after `.claude/skills/`: "That skill lands in its own agent-scoped commit, with an entry in `.claude/decisions.md` when it changes how this repo's agent works."

**FINDING-301.** rule 8; resting on the reader. §3 step 6 (line 281): "No registry entry: the Concept Deliverer receives no conventions (ADR-0042)." "Registry" is met here first with no plain words; the reader has to know a CBC Run keeps a registry of the conventions it received. Proposed: "No entry in a registry of received conventions, as a CBC Run keeps: the Concept Deliverer receives none (ADR-0042)."

**FINDING-302.** rule 6; uncertain. §1.4 (line 137): ""Step" is PLAN's:"; §3 (line 288): "the PLAN has no per-convention Plan Steps". The file `PLAN.md` written as "PLAN": neither the path written as it is nor a Name. The other file does the same throughout: "PLAN.md's Decision index" (285, the path outside backticks), "then ARCHITECTURE, then PLAN" (507), "What TODO holds" (384, a title), "TODO's form" (405), "TODO's anti-patterns" (433), "ARCHITECTURE current" (535), "which ARCHITECTURE points into" (605). Question for the reviewer: is the bare record name a settled short form, or an inexact name? If the latter: "`PLAN.md`'s", "`PLAN.md` has no", and so on, in both files.

**FINDING-303.** rule 10; uncertain. §2.2 *What it is for* (line 185), §2.7 *Why it arrives this way* (line 244), §2.8 *What this does not cover* (line 250). Numbered sections titled with a fixed heading's name; each carries a pronoun, "it" or "this", with no referent when the title stands alone in a Fact Reference: "§2.2, *What it is for*" reads as this convention's own need. §2.4 *The seats* and §2.9 *Where to look* are noun phrases and stand alone. The form's fixed headings are exempt; these are numbered sections about them. Question: does a title that names a fixed heading stand alone as a label? If not: *The need* (2.2), *The channel* (2.7), *The boundary* (2.8).

**FINDING-304.** rule 2; resting on the reader. *Why it arrives this way* (lines 292–295): "The form of a manual is an Agent Rule, loading when a manual is read, so it is in view while one is worked; a manual written new is written without it (…)." Four ideas: what the form is; when it loads; why; the exception. Proposed: "The form of a manual is an Agent Rule. It loads when a manual is read, so it is in view while one is worked. A manual written new is written without it (…)."

#### Layer 2: project-recording

##### `docs/conventions/project-recording/README.md`

**FINDING-305.** rule 2; resting on the reader. `docs/conventions/project-recording/README.md` *What it is for* (lines 15–18): "Lived since: four CBC Runs kept their records under these Record Stubs, and every Run Reading of CBC Run 3 has been a reading of its Decisions Log, its backlog and its devlog — the need proved by being the only channel there is." Three ideas joined by "and" and a dash: the four CBC Runs; what every Run Reading read; what that proves. Lines 9–12 are one sentence with a dashed aside listing the readers. Proposed: split at "and" and at the dash.

**FINDING-306.** rule 5; resting on the reader. *What this is made usable as* (line 32): "this convention's one stake (§13, *The records table*)"; §13 (line 774): "This convention keeps one stake in it". "Stake" stands for the one part of the entry file this convention owns. Proposed: "the one part of the entry file this convention owns".

**FINDING-307.** rule 9; checked. *What this is made usable as* (line 41): "on trial, which has no stub (§14, *Conversation Memory*, ADR-0060)". A Record Stub is meant; ADR-0074 gave "stub" its Name. Proposed: "which has no Record Stub".

**FINDING-308.** rule 9; resting on the reader. *What this is made usable as* (lines 35–36): "the playbook's Plan Steps, filled into a CBC Run's `PLAN.md` at birth". The thing is the Delivery Fill, the glossary's Name for exactly this; the manual never uses the Name (also lines 58, 73, 234–235, 255, 649). Proposed: name it once here: "the Delivery Fill: the playbook's Plan Steps, put into a CBC Run's `PLAN.md` at birth".

**FINDING-309.** rule 2; resting on the reader. *The seats* (lines 50–53): "The same records in both Convention Seats, each derived from this page — the CBC Run's through the Record Stubs, the Concept Deliverer's directly — with seven differences of rule or ownership, so a section each". One sentence, three ideas. Proposed: "Both Convention Seats keep the same records, each derived from this page: the CBC Run's through the Record Stubs, the Concept Deliverer's directly. They differ in seven things, so each has a section."

**FINDING-310.** rule 3; checked. *The Concept Deliverer's seat* (line 67): "and differs in seven things". The seven are then told in prose: three inside the first paragraph (lines 68–74), then four paragraphs each opening "And its…" or "And it…" (lines 76, 88, 109, 115). The count is claimed and hidden; a reader finds seven only by counting clauses. Proposed: a numbered list of seven, one bold lead each (no project end; the playbook; `CHANGELOG.md`; `PLAN.md`; `ARCHITECTURE.md`; the ADRs' length; Conversation Memory), the prose under each.

**FINDING-311.** rule 2; checked. *The Concept Deliverer's seat* (lines 80–84): "A CBC Run keeps its finished Plan Steps in its plan, each closed to one line, because they are the evidence its playbook is folded from; no playbook is folded from the Concept Deliverer's own plan, so its finished Plan Steps are only history, which is the devlog's." Four ideas chained by "because", a semicolon, "so" and "which". Proposed: "A CBC Run keeps its finished Plan Steps in its plan, each closed to one line: they are the evidence its playbook is folded from. No playbook is folded from the Concept Deliverer's plan. Its finished Plan Steps are history, and history is the devlog's."

**FINDING-312.** rule 4; resting on the reader. *The Concept Deliverer's seat* (line 111): "several numbered decisions each". A count exists in `docs/adr/`, as the median line count beside it shows. Also §7.5 (line 536): "most Plan Steps make nothing projectable true", where the playbook's Plan Steps can be counted. Proposed: "N to M numbered decisions each"; "K of the playbook's N Plan Steps make nothing projectable true"; or decline where the count is not worth keeping current.

**FINDING-313.** rule 9; checked. §1, *The records at a glance*, the pictures (line 166): "(the deliverer's; a run holds none)". The Concept Deliverer and a CBC Run in lowercase; also "step" for a Plan Step at lines 188, 199, and in §11's picture at 722, 723, 724. Proposed: "(the Concept Deliverer's; a CBC Run holds none)", "the one Plan Step being worked, and any Plan Step it stopped", "at each Plan Step's close", "why a Plan Step diverged"; or decline for the pictures where width forbids, and say so above them.

**FINDING-314.** rule 5; checked. §7, *README.md* (line 492): "The front door."; §7.1 (line 499): "README is the front door for people; the entry file is the one for agents"; the pictures (lines 181, 201): "the front door: what this is, where the rest is". The figure the rule names. The same words stand in `CLAUDE.md` line 28 and `delivery/container/.claude/CLAUDE.md` line 51, outside this layer. Proposed: "The first page a person reads."; "README is the first page for people; the entry file is the first for agents"; "the first page: what this is, where the rest is".

**FINDING-315.** rule 5; checked. §2, *PLAN.md* (line 211): "The spine the other records hang off."; also §2.4 (line 245): "stays the spine the other records hang off", and "(the spine)" in both pictures (lines 169, 187). Proposed: "The record the others point back to."

**FINDING-316.** rule 5; checked. §2.1, *What a plan is* (lines 215–216): "the full journey sketched coarsely, the next 1–2 Plan Steps detailed finely (rolling wave)". "Journey" for the whole of the work; "rolling wave" is a term the text does not define. Proposed: "the whole of the work sketched coarsely, the next 1–2 Plan Steps detailed finely, the detail moving forward as Plan Steps close".

**FINDING-317.** rule 5; checked. §2.4, *How a plan is written* (lines 242–243): "A closed Plan Step's line says what diverged from the plan: that is retro fuel." Proposed: "that is what the retrospective reads."

**FINDING-318.** rule 3; checked. §2.6, *A plan's anti-patterns* (lines 260–261): "Plan Steps without gates (it's just a wish list); detailing Step 9 before Step 2 is done; letting statuses go stale so the plan lies." Three or more parts chained with semicolons in one sentence; the same form in §3.7 (322–324), §4.6 (374–376), §5.6 (435–437), §6.6 (484–486), §9.6 (676–678). §7.6 and §8.5 have two parts each and are not listed. One pattern over six sections, listed once so the reviewer can end it once. Proposed: one bullet per anti-pattern in each.

**FINDING-319.** rule 2; checked. §3.5, *Numbers across repos* (lines 308–312): "A reference to another repo's decision carries that repo's Repo Tag before the number — `CBC ADR-0012`, as a CBC Run cites the Concept Deliverer's — a short upper-case name each repo declares once in its README's decisions row (§7, *README.md*)." Three ideas: the rule; the example; what a Repo Tag is and where it is declared. Proposed: "A reference to another repo's decision carries that repo's Repo Tag before the number: `CBC ADR-0012`, as a CBC Run cites ours. A Repo Tag is a short upper-case name each repo declares once in its README's decisions row (§7, *README.md*)."

**FINDING-320.** rule 2; resting on the reader. §3.2, *Why an ADR* (lines 277–280): "Six months later, "why is this Postgres and not Mongo" has an answer, and — equally important — "we already considered that and rejected it because…" stops the same debate from recurring." Two ideas with a dashed aside. Proposed: two sentences; drop "equally important".

**FINDING-321.** rule 5; resting on the reader. §4, *The devlog*: §4.1 (lines 335–336): "The lab notebook of the project."; §4.2 (line 344): "it is the raw material that gets distilled upward"; §4.4 (line 363): "the cheapest save-point that exists". A notebook, distilling, a game's save-point. Proposed: "The project's dated notes, kept as written."; "it is what the records above it are written from"; "the cheapest place to resume from".

**FINDING-322.** rule 5; checked. §5.4, *How an item is written* (lines 409–410): "A 200-item "later" list is a graveyard, not a plan"; §5.2, *Why a TODO* (line 391): "An open loop held in the head costs attention". Proposed: "A 200-item "later" list is never read, and is not a plan"; "A thing known and not written down costs attention".

**FINDING-323.** rule 2; resting on the reader. §6.3, *Where the changelog lives* (lines 460–462): "What a version *is* depends on the repo type — an application releases SemVer versions; a concept or docs repo versions something else, and says what at Framing." Three ideas chained with a dash and a semicolon. Proposed: "What a version is depends on the repo type. An application releases SemVer versions. A concept or docs repo versions something else, and says what at its Framing Plan Step."

**FINDING-324.** rule 5; checked. §7.5, *When a README changes* (lines 531–532): "Projection follows truth, so the README never claims what is not yet true (ADR-0038, 1d)."; "projectable" and "its projection" (lines 534, 537). "Projection" is a coined use, the README as a projection of the repo's state, defined neither here nor in the glossary. Also line 538: "trains rubber-stamping". Proposed: "The README says only what is already true"; "a Plan Step whose gate makes true something the README should say includes updating the README"; "trains ticking it unread".

**FINDING-325.** rule 2; resting on the reader. §7.5 (lines 532–536): "The mechanism is a gate item where relevant: a Plan Step whose gate makes something projectable true includes updating its projection, exactly as record upkeep is already expressed in lived gates ("ARCHITECTURE current")." Three ideas. Proposed: split at "exactly as".

**FINDING-326.** rule 7; checked. §8.2, *Why a map* (line 568): "Newcomers read it second, right after the README (§7.2, *Why a README*)." The same fact with the same Fact Reference is §8.4's first bullet (lines 584–585): "a newcomer reads it second, after the README (§7.2, *Why a README*)", and §7.2 states it (line 507). Proposed: keep it in §8.4, where it is the reason for the page count; cut the sentence from §8.2.

**FINDING-327.** rule 5; checked. §8.2 (lines 567–568): "It's the difference between a stack of route decisions and a map."; §8.5, *The map's anti-patterns* (lines 598–599): "it maps the forest, the code is the trees." Proposed: cut the first, since the sentence before it says it ("ADRs are a history of individual choices; this is the synthesized present"); "it describes the whole, the code describes each part".

**FINDING-328.** rule 2; checked. §8.6, *Local Maps* (lines 603–606): "An area whose parts relate in ways the map should not carry — how they connect, hand work to each other, or land elsewhere — gets a Local Map: its directory's `README.md`, which ARCHITECTURE points into." Four ideas: when an area gets one; what the relations are; what a Local Map is; how it is reached. Proposed: "A Local Map is a directory's `README.md`, which `ARCHITECTURE.md` points into. An area gets one when its parts relate in ways the map should not carry: how they connect, hand work to each other, or land elsewhere."

**FINDING-329.** rule 5; checked. §9.4, *How a playbook is written* (line 647): "has four acts, each with its how where its doer reads it:". "Act" is the theatre figure the rule itself names ("a third act of the exchange"). Proposed: "Its lifecycle has four moments, and each says where its doer reads how:".

**FINDING-330.** rule 5; resting on the reader. §9.2, *Why a playbook* (lines 629–631): "The first plan of a familiar project type writes itself, and past mistakes are pre-loaded as warnings at exactly the Plan Step where they bit."; §9.1 (line 622): "distilled from completed plans". Proposed: "The first plan of a familiar project type is already written, and past mistakes stand as warnings at the Plan Step where they happened"; "written from completed plans".

**FINDING-331.** rule 6; resting on the reader. §9.5, *When a playbook changes* (line 672): "updated at every retro thereafter"; also lines 243, 345, 677, and "Retro" in the picture (line 170). "Retro" clips the retrospective's name; the convention is `docs/conventions/retrospective/` and its file is `RETRO.md`. Proposed: "retrospective" in prose; the picture may keep `RETRO.md`.

**FINDING-332.** rule 6; resting on the reader. *The CBC Run's seat* (line 59): "Its retrospective runs before Release"; also "The Release gate" (538), "Framing and Release have their own copies" (666), "before Release" in §11's picture (725), "says what at Framing" (461–462). "Release" and "Framing" are labels of the playbook's Plan Steps used outside it without their owner; rule 6 asks the owner. ("Framing" is also a method word, which the brief exempts.) Proposed: "before its Release Plan Step", "The Release Plan Step's gate", "The Framing and Release Plan Steps have their own copies there".

**FINDING-333.** rule 5; checked. §11, *The flow between records* (lines 715–716): "Records form a distillation pipeline — raw experience at the bottom, durable knowledge at the top:". Proposed: "Each record is written from the one below it: the devlog holds what happened, the records above it keep what lasts:".

**FINDING-334.** rule 8; resting on the reader. §13, *The records table* (line 774): "the only ambient part of project-recording". "Ambient" is the Agent Model's channel word (`docs/models/agent.md` §4.1, *ambient*), met here with no plain words and no Fact Reference. Proposed: "the only part of project-recording loaded before any task (`docs/models/agent.md` §4.1, *ambient*)".

**FINDING-335.** rule 5; resting on the reader. §13.1, *What a row holds* (line 784): "The moment is the half that is new and the half that is load-bearing." Proposed: "The moment is the half that is new, and the half the table is for."

**FINDING-336.** rule 7; resting on the reader. §13.1 (line 782): "This is a requirement, not a convenience." The bold sentence before it already states the requirement; this adds emphasis only. Proposed: cut.

**FINDING-337.** rule 1; resting on the reader. §14, *Conversation Memory* (lines 807–810): "A TODO item keeps what triage needs, and its story is the devlog's. The talk that shaped it is neither: … That talk is the Conversation Memory." The section's point, what a Conversation Memory is, arrives in the third sentence after two of context. Proposed: lead with "The Conversation Memory is the talk that shaped a TODO item: what was asked, the options weighed, what was said for and against, the reviewer's own words. The item keeps what triage needs; its story is the devlog's; the talk is neither."

**FINDING-338.** rule 9; resting on the reader. §1 (line 204): "The entry file is agent-arrangement's"; §13 (line 772): "is agent-arrangement's"; (line 774): "part of project-recording". Conventions named by the bare word; the glossary's header asks the path in backticks or the Name. Proposed: "`docs/conventions/agent-arrangement/`'s", "part of `docs/conventions/project-recording/`".

**FINDING-339.** rule 9; uncertain. Three lowercase phrases name defined things throughout the file and have no Glossary Name: "the entry file" (lines 30, 204, 499, 739, 771, 797, 844, 847, 853, 869), "the records table" (32, 161, 254, 316, 369, 429, 480, 531, 740, 765, 779, 845), "the map" for `ARCHITECTURE.md` (91, 550, 552, 564, 572, 576, 578, 581, 595, 603, 606). Rule 9: a thing a text defines, giving a word a meaning English does not, has a Name; the glossary's header: a word whose English meaning is ours has none. Question for the reviewer: English in its English sense, or defined things that want Names (Entry File, Records Table; the map written as `ARCHITECTURE.md`)?

**FINDING-340.** rule 3; resting on the reader. §14 (lines 826–828): "**Read before the Ideas are weighed,** so the talk shapes the weighing, and gone with its item, so nothing outlives what it was about." One bold lead covers two rules: when a section is read, and when it goes. Proposed: two bullets, "**Read before the Ideas are weighed**" and "**Gone with its item**".

#### Layer 3: the other manuals, the Idea Models, the concept

##### `docs/conventions/README.md`

**FINDING-341.** rule 6; checked. `docs/conventions/README.md`, opening (line 8): "(`ARCHITECTURE.md` §1.2, *The conventions…*)". A Fact Reference's title is the heading, carried whole; "…" is for a numbered rule's bold lead only (`docs/conventions/facts-in-sync/` §3.1). The heading at home is "The conventions — `docs/conventions/`", 37 characters with a gloss after a dash: a rule 10 break in `ARCHITECTURE.md` (its §1.1, §1.3 and §2.1–2.4 have the same form), not in this file. Proposed: fix at home: retitle `ARCHITECTURE.md` §1.2 *The conventions* (and its sisters), write the title whole here, rename grep.

**FINDING-342.** rule 2; resting on the reader. `docs/conventions/README.md`, opening (lines 7–9): "Which conventions there are and what each covers is the map's (…); what a convention is, how one is written and how one is added is `docs/conventions/conventions/`." Two subjects with two homes in one sentence on a semicolon. Proposed: fix: split at the semicolon.

##### `docs/conventions/agent-arrangement/README.md`

**FINDING-343.** rule 9; checked. `docs/conventions/agent-arrangement/README.md` §5.6, *Rules files* (line 510): "show `paths:` failing silently in some formats and Convention Seats". The bug reports are about Claude Code's surfaces, not a convention's two sides; the Name stands where the English word stood (commit 1576044 replaced "formats and seats"). Proposed: fix: "in some formats and surfaces".

**FINDING-344.** rule 9; checked. *The seats*, *The Concept Deliverer's seat* (line 72): "*"A Concept Repo… Documents only — no code, no runs."*". Quotes `CLAUDE.md` line 7, which now reads "no code, no CBC Runs"; "runs" is a CBC Run, and the quote has gone stale. Proposed: fix: "no code, no CBC Runs".

**FINDING-345.** rule 3; checked. *The seats*, *The Concept Deliverer's seat* (lines 72–81): "It holds the convention skills `commit-messages`, `commit-plan` and `visual-comparison`, not the retrospective's, whose Convention Seat here is on trial; the Exchange Convention's skills, `exchange-read` and `exchange-deliver`; the Agent Rules every session loads, …". Five kinds of file in one semicolon sentence, each with a gloss inside it; the count (3 + 2 + 3 + 3 + the Approaches on Trial) is hidden. Two more in the same section: the CBC Run's inventory (lines 55–59) and *What the difference is* (lines 91–95, three things the same on semicolons). Proposed: fix: a list, one line per kind, in each.

**FINDING-346.** rule 1; resting on the reader. *The seats*, *What the difference is* (lines 91–95): "Each Convention Seat's skills and Agent Rules are derived from their manuals and written for their Convention Seat, never copied across (ADR-0042, ADR-0069); the records table has the same shape; …". The part titled *What the difference is* opens with what is the same; the difference ("What differs is the job") is sentence 2, line 95. Proposed: fix: open with line 95's sentence; the sameness follows.

**FINDING-347.** rule 1; resting on the reader. §1, *What the arrangement is* (line 111): "The theory this leans on is `docs/models/agent.md`: the ambient channel…". The section opens with its theory; what the arrangement is (a closed list of paths, detachable, not records) arrives only in §1.1–1.3. Proposed: fix: one first sentence, "The arrangement is a closed list of agent-side paths a copy of the project can drop", then the theory.

**FINDING-348.** rule 1; resting on the reader. §2.2, *Why an entry file* (lines 164–166): "The records teach their own use, and so does every Record Stub in the arrangement — each carries its rules in embedded comments, met at the moment the file is opened." The answer is sentence 3 (line 167): "The entry file is the one piece of text present before anything is looked up." Proposed: fix: lead with that sentence.

**FINDING-349.** rule 2; checked. *What it is for* (lines 15–19): "The failure it answers was measured before it was adopted, in the handbook's entry file, and is reported here, since this repo cannot re-check it: restating convention rules "so they are always in context" grew the entry file to 98 lines, split across two files, with three disagreeing copies of one rule." Five ideas in one sentence. One more: lines 20–24 ("CBC Run 3 moved its entry file … — which is why the Container Group now ships it there"), four ideas on commas and a dash. Proposed: fix: one idea a sentence.

**FINDING-350.** rule 2; checked. *The seats*, *The CBC Run's seat* (lines 51–55): "Its entry file says that `docs/concept/` and the skills, Agent Rules, Output Shapes and Approaches on Trial under `.claude/` are delivered copies, pinned, and that until the framing artifacts exist the only method work is running `cbc-framing` jointly with the human." Two claims of the entry file in one sentence. One more: lines 81–85, the Decisions Log sentence (four ideas on a colon and two "and"s). Proposed: fix: split each.

**FINDING-351.** rule 2; checked. §2, *The entry file*: §2.4 (lines 193–197): "A line with a moment goes where the moment is — the record's Record Stub, README, a skill, or, for a rule true only under one directory, an Agent Rule with a `paths:` list (§3.2, *`.claude/rules/`*) — and is read there, at the moment it is about, instead of on every task it is not." A four-item list between dashes with a Fact Reference in it. Four more: §2.4 lines 208–211; §2.6 lines 242–245, 246–250 ("The cost is what the harness delivers, not the file: HTML comments are dropped on load (…), so the guard and the records comment cost nothing per task and are read when the file is opened to edit it — the moment they govern"), 254–257. Proposed: fix: the list on its own lines; one idea a sentence.

**FINDING-352.** rule 3; checked. §2.4, *How the entry file is written* (lines 203–206): "What passes, in practice, is five kinds of content: what the project is · the records table · build and test commands, where the project has them · how to work here · local rules that have no moment." Five parts chained with middle dots in one sentence; three of them get a paragraph each below. Proposed: fix: a list of five.

**FINDING-353.** rule 7; checked. §2.4, *How the entry file is written* (lines 228–230): "fails: each has a moment, and goes where the moment is — the record's Record Stub, README, a skill the project adds under `.claude/skills/`, an Agent Rule under `.claude/rules/` (§3.2, *`.claude/rules/`*)". Repeats lines 193–195 of the same section ("goes where the moment is — the record's Record Stub, README, a skill, or … an Agent Rule with a `paths:` list"). Proposed: fix: at 228, "and goes where the moment is, as the second test says."

**FINDING-354.** rule 5; resting on the reader. §2.4, *How the entry file is written* (line 206): "That is a description of what the tests leave, not a fence". A figure for "not a rule of its own". One more word in the section: "start rebuilding the rulebook" (line 223; also 376, 393). Proposed: fix: "not a rule of its own"; "restating the rules".

**FINDING-355.** rule 8; uncertain. §2.6, *The entry file's size* (line 247): "The cost is what the harness delivers, not the file". "Harness" is one of the method's words (the concept's test harness); here it is Claude Code, which the file calls "the tool" elsewhere (lines 22, 121, 252). Proposed: fix: "what the tool delivers".

**FINDING-356.** rule 2; checked. §3.7, *`CLAUDE.local.md`* (lines 330–332): "One person, one checkout; the hygiene base ignores it, and its words never enter a record — a record that quotes it has let one operator's preference into the project's truth." Four ideas on a semicolon, an "and" and a dash. Proposed: fix: split.

**FINDING-357.** rule 7; checked. §3.7, *`CLAUDE.local.md`* (lines 336–337): "it has one operator, and a setting kept out of git is one no reader of the repo can see (ADR-0062). Outside practice ignores the file, as the tool's documentation advises. Ours differs only because this repo has one operator." The one-operator reason is given twice in three sentences. Proposed: fix: cut the last sentence.

**FINDING-358.** rule 4; resting on the reader. §3.9, *A rule loaded in every session* (lines 378–379): "It is paid for in every session (§2.6, *The entry file's size*), so few qualify." The count exists and is in this file: two in the Container Group (line 58), three at the Concept Deliverer (lines 76–77). Proposed: fix: "so two qualify in a CBC Run and three here"; or decline, the count stands in *The seats*.

**FINDING-359.** rule 5; checked. §4, *Arrangement anti-patterns* (line 384): "a rule that is true in another project is a convention wearing a stance's clothes." A costume metaphor; the writing manual names "costume" as a word to drop. One more: line 389, "a header waiting for content is weight with no guard in it". Proposed: fix: "is a convention written as a stance"; "is cost with no guard in it".

**FINDING-360.** rule 8; resting on the reader. §5.1, *The mapping* (line 425): "| Layer 1 | Claude Code mechanism |". "Layer 1" is the Agent Model's word for its channels; nothing before the table says so (§5's opening says "the channels and the gate"). Proposed: fix: "Channel (the Agent Model's Layer 1)".

**FINDING-361.** rule 2; checked. §5.3, *Memory files' comments* (lines 442–446): "The loader drops every block-level `<!-- … -->` comment before the text enters context — one inside a code block is kept — so a comment in an entry file is never ambient: it reaches the agent only when the file is opened with a tool, which for the entry file is edit time." Five ideas. One more: lines 449–451 (`claudeMdExcludes`: what it does, how it matches, what that gives). Proposed: fix: split each.

**FINDING-362.** rule 7; resting on the reader. §5.6, *Rules files* (lines 485–486): "`.claude/rules/` holds instruction files like `CLAUDE.md`, with one extra: a `paths:` list at the top." Repeats §3.2 (lines 280–281): "Instruction files read like the entry file, with one extra: a `paths:` list at the top." §3.2 already points here for the loading. Proposed: fix: §5.6 opens at its own subject, "Without a `paths:` list, the file is read every session…"; or decline, §5 is the binding and reads alone.

**FINDING-363.** rule 8; resting on the reader. *What it is for* (line 16): "in the handbook's entry file". "The handbook" is said in plain words nowhere, here or in the Agent Model (which uses it the same way, `docs/models/agent.md` lines 270–405). The same at `docs/conventions/facts-in-sync/README.md` line 16. Proposed: fix: once, at the first use in each: "the handbook, the repo this convention came from".

**FINDING-364.** rule 8; resting on the reader. §1.3, *Not records* (lines 141–142): "a CBC Run's Decisions Log's promotion queue". The phrase occurs nowhere else in living text, and the shipped Decisions Log stub holds no queue; the reader cannot look it up. The same for "registry" (line 83 "and no registry", line 86 "keeps its registry"): the stub holds no "registry"; §3.4 says the birth entry "lists the conventions it holds". Proposed: question: are both stale? If the thing is the birth entry's list of conventions, say that; else cut.

**FINDING-365.** rule 6; resting on the reader. *Why it arrives this way* (line 533): "the entry file's comments carry points-never-restates, the guard and the size rule". A hyphenated label coined for the bold at line 190 ("It points; it never restates"). Proposed: fix: "carry the rule that it points and never restates, the guard and the size rule".

**FINDING-366.** rule 5; resting on the reader. File-wide, "rides" for "is written in": line 36 "Every rule here rides as a comment in the file it governs"; 187 "the rule rides in a skill or a stub"; 300 "rides as a comment in the artifact it governs"; 305 "Its rules ride in its own Record Stub"; 533 "rides in it as a comment". Proposed: fix: "is a comment in" / "sits in"; or decline as a dead metaphor.

**FINDING-367.** rule 9; uncertain. File-wide: "entry file". §2.1 defines it ("One file, loaded into an agent's context at the start of every session before it is given any task"), a meaning English does not give the words; used about 45 times here, across the repo, and in the glossary's Agent Rule entry, with no Glossary Name. Rule 9's last sentence sends such a thing to the glossary. Proposed: question: coin *Entry File* and sweep, or rule that "entry file" is English and say so in the glossary's header comment.

**FINDING-368.** rule 10; uncertain. Three titles with a comma: `docs/conventions/agent-arrangement/README.md` §1.2 *Detachable, and kept so* (line 127); `docs/conventions/commit-plan/README.md` §2.1 *A convention, not a record* (line 67); `docs/conventions/exchange/README.md` §2.5 *One cycle, drawn* (line 138). Rule 10 wants one noun phrase with no gloss after a dash or colon; a comma is not named, and the first is not a noun phrase. Proposed: question: does a comma gloss count? If yes: *Detachability*, *Not a record*, *One cycle*.

##### `docs/conventions/commit-messages/README.md`

**FINDING-369.** rule 2; checked. `docs/conventions/commit-messages/README.md`, *What it is for* (lines 12–17): "The failure it answers is measured: with the subject limit ambient in an entry file and the rule pulled in by a skill, fifteen of the first twenty commits of the repo it came from broke the limit — present, correct, unfollowed (`docs/models/agent.md` §12, *Claims*, A1) — which is why the rule is opened at the commit moment and not read once." Four ideas on a colon, two dashes and a "which". Proposed: fix: "The failure it answers is measured. The subject limit sat ambient in an entry file, and a skill pulled the rule in. 15 of the first 20 commits of the repo it came from broke it: present, correct, unfollowed (…). So the rule is opened at the commit, not read once."

**FINDING-370.** rule 1; resting on the reader. §3, *The Concept Deliverer's habit* (lines 88–93): "The Concept Deliverer's product is documents, so `docs` could swallow everything. One answer is to make the type carry the signal — …". The habit itself, "the type is nearly always `docs`, and the scope … carries the signal", is line 105, after the rejected answer and the list. Proposed: fix: open with line 105's sentence.

**FINDING-371.** rule 2; checked. §3, *The Concept Deliverer's habit* (lines 105–108): "So the type is nearly always `docs`, and the **scope**, where one is given, carries the signal here, which is the mirror of the other answer, not a weaker version of it." Three ideas on "and" and "which". Proposed: fix: split after "here".

**FINDING-372.** rule 2; checked. §2.2, *Mood and tense* (lines 63–66): "A subject says what the commit changes; a change to the work reads naturally as a command, a record as what became true, and both read well in the log." Three ideas on a semicolon and an "and". Proposed: fix: split.

**FINDING-373.** rule 2; resting on the reader. *Why it arrives this way* (lines 117–119): "The commit is also the moment other conventions' discipline binds at — the `agent` scope, the stop — which is why those sentences live in this skill and nowhere else." Two ideas with a two-item aside between dashes. One more: *The seats* (lines 38–40), "and has one local habit — which scope carries the signal — stated in its own section, and not shipped". Proposed: fix: name the two in a clause, not between dashes.

**FINDING-374.** rule 8; resting on the reader. §2.1, *Conventional Commits* (line 57): "Conventional Commits, not just 50/72." Nothing in this manual says what 50/72 is; the reader meets it first here (the writing manual says only that 72 is a body line's limit). Proposed: fix: "not just the 50/72 limits, 50 characters for the subject and 72 for a body line".

**FINDING-375.** rule 6; resting on the reader. §1, *What a commit message is* (lines 50–51): "A good commit body is a micro-ADR for a change too small to deserve a real one." A coined word, not in the glossary, not defined. Proposed: fix: "A good commit body does for a small change what an ADR does for a large one."

**FINDING-376.** rule 9; resting on the reader. *What it is for* (line 11): "Adopted with the container (ADR-0038, 1a, 1c, 1f)." The thing is the Container Group; agent-arrangement writes the same phrase with the Name (its line 20, "Adopted with the Container Group (ADR-0038, 1c)"). The same at `docs/conventions/commit-plan/README.md` line 11. The possessive "like the container's" (commit-messages line 29, commit-plan line 28) matches the writing rule's own comment and may be the Made Usable sense the glossary gives "the container". Proposed: fix: "Adopted with the Container Group" at both line 11s; question: is "the container's" English here?

**FINDING-377.** rule 7; resting on the reader. §3, *The Concept Deliverer's habit* (line 110): "This section is the Concept Deliverer's and does not ship." *The seats* (lines 39–40) says it: "stated in its own section, and not shipped (§3, …)". Proposed: fix: cut line 110; or decline, the reader of §3 acts on it there.

**FINDING-378.** rule 5; resting on the reader. §3, *The Concept Deliverer's habit* (line 88): "so `docs` could swallow everything". Proposed: fix: "so `docs` could be every commit's type".

**FINDING-379.** rule 10; uncertain. §2.4 title *Commit on the word* (line 78). It reads as an imperative; rule 10 asks a noun phrase. It is pointed at from `docs/conventions/commit-plan/README.md` (lines 161, 170) and `docs/conventions/agent-arrangement/README.md` (line 317); a retitle greps them. Proposed: question: *The commit on the word*; or decline, read as a noun phrase.

**FINDING-380.** rule 10; uncertain. §2 title *Why it is shaped this way* (`docs/conventions/commit-messages/README.md` line 53; `docs/conventions/commit-plan/README.md` line 65). "It" leans on the title above; rule 10 wants a title that stands alone. The fixed heading *Why it arrives this way* has the same "it". Proposed: decline, parallel to the fixed heading; or *Why this shape*.

##### `docs/conventions/commit-plan/README.md`

**FINDING-381.** rule 2; checked. `docs/conventions/commit-plan/README.md`, *What it is for* (lines 14–19): "Lived here since: every set since 2026-08-27 has run under it, and on 2026-09-27 and 28 one set was revised four times at its boundaries on the reviewer's readings, each revision on its own commit — the failure it guards against, doing otherwise than the plan and fixing it afterwards or not at all, has not happened here." Five ideas in one sentence. One more: lines 11–14 ("Adopted with the container (ADR-0038, 1b): the failure it answered was lived elsewhere — … — and is not ours to restate"). Proposed: fix: one idea a sentence.

**FINDING-382.** rule 9; checked. *What it is for* (line 15): "every set since 2026-08-27 has run under it". "Set" is a Change Set. Three more: line 16 "one set was revised", §2.10 line 133 "every name the set moved", §2.12 line 153 "nothing showed the set". Proposed: fix: "Change Set" each.

**FINDING-383.** rule 2; checked. §1, *What a commit plan is* (lines 50–54): "The plan is one file at the repo root, `COMMIT-PLAN.md`, committed after it is agreed and deleted at the close; everything durable in it survives as the commit messages it produced, and the close commit's body is the cheapest retrospective that exists." Four ideas. Two more: lines 46–49 (the patch series, four clauses) and 58–62 ("**Order follows where the decision lives**: … ; …, with the durable record written from what held"). Proposed: fix: split each.

**FINDING-384.** rule 7; resting on the reader. *The seats* (lines 37–39): "A CBC Run runs its Change Sets under the skill, the plan file at its root its own. The Concept Deliverer runs its Change Sets under the same skill, the plan file at its root its own." The second sentence repeats the first with the subject changed; the manual form allows one paragraph when the seats are alike. Proposed: fix: "A CBC Run and the Concept Deliverer each run their Change Sets under the skill, the plan file at their own root."

**FINDING-385.** rule 1; resting on the reader. §2, *Why it is shaped this way*: six parts open with the failure or the context and reach the rule second. §2.11, *Small commits* (lines 141–144): "Each planned commit landing as one leaves no room to try: two ways meant reworking a commit in place. Small commits give the room, and are folded into the planned commit before its boundary, so the reviewer still sees one commit there." Also §2.5 (lines 94–96, the walk of the records table is sentence 2), §2.6 (100–101, that a plan counts commits is never said outright), §2.8 (116–118, that subjects are counted when written is implied), §2.10 (130–133, the sweep is sentence 2), §2.12 (153–154, the look back is sentence 2). Proposed: question: in a section titled *Why…*, does each part lead with its rule, then the why? If yes, fix: reorder the six.

**FINDING-386.** rule 2; checked. §2, *Why it is shaped this way*: §2.1 (lines 69–72): "It is a scaffold, not a record: nothing about it is meant to be read a year later except through `git log`, so it sits outside `docs/conventions/project-recording/`, whose records are all append-or-evolve (ADR-0038, 1b)." Four ideas on a colon, a "so" and a "whose". Three more: §2.8 lines 116–118 ("A plan writes every subject before any lands; counted only at each boundary, a long one lands long, or is rewritten there with nothing in the plan saying why"); §2.11 lines 144–148 ("The grant is the reviewer's because a small commit is still a commit, and the stop at every commit is commit-messages' rule (…); without the grant, every commit is a boundary"); §2.12 lines 153–154 ("two commits can turn out one change, or one two, and are regrouped on the reviewer's word", where "or one two" packs a second idea into two words). Proposed: fix: split each; at 154, "two commits can turn out to be one change, or one commit two changes".

**FINDING-387.** rule 6; resting on the reader. §2.9, *The agent's files* (lines 125–126): "*The same plan put two changes under `.claude/` inside its records Plan Step, and split it by revision.*" "The same plan" is CBC Run 3's Step 10, named two parts up (§2.7, line 109); outside that part the reference carries no owner. Proposed: fix: "*CBC Run 3's Step 10 plan put…*".

**FINDING-388.** rule 5; resting on the reader. §2.1 (line 69): "It is a scaffold, not a record". Also §2.3 (line 83) "makes a neglected plan lie", §2.4 (line 90) "are the normal road, not a sign the plan failed". Proposed: fix: "It is temporary, not a record"; "makes a neglected plan wrong"; "are the normal course".

##### `docs/conventions/exchange/README.md`

**FINDING-389.** rule 3; checked. `docs/conventions/exchange/README.md`, *What it is for* (lines 16–21): "Until 2026-09-26 the receiver's protocol, `convention-lifecycle`, 154 lines, was held by the Concept Deliverer, which never once ran it, while CBC Run 3 ran it at every Delivery Take; the Concept Deliverer's half was `bundle-update.md`, 527 lines; and the rule for editing a copy was written twice in two repos, six elements the same in different words (§5.1, *When a copy may be edited*)." Three failures chained with semicolons in one sentence. Proposed: fix: "Three things were wrong until 2026-09-26:" and a list of three.

**FINDING-390.** rule 2; checked. *What it is for* (lines 12–14): "So that the Concept Deliverer and a blind CBC Run stay in step: files go down whole, what the CBC Run learned comes back as a Run Reading, and a verdict returns — each side holding only the half it can run." Four ideas. Proposed: fix: "…stay in step. Files go down whole. What the CBC Run learned comes back as a Run Reading, and a verdict returns. Each side holds only the half it can run."

**FINDING-391.** rule 8; resting on the reader. *What this is made usable as* (line 38): "read the three things, write the Run Reading". The three are named in §6.1 (line 424), after. Proposed: fix: "read the three things §6.1 names".

**FINDING-392.** rule 2; checked. §2.4, *The records' exception* (lines 127–131): "They never update: `PLAN`, `TODO` and the devlog are delivered once as Record Stubs, the entry file once as a composed file; the CBC Run fills them; no later delivery touches them." Four ideas on a colon and two semicolons. Proposed: fix: split.

**FINDING-393.** rule 8; resting on the reader. §2.4, *The records' exception* (lines 135–136): "Skeleton sync is reopened if a CBC Run re-applies the same declined edit after two re-pins." "Skeleton sync" and "re-pins" are said nowhere in plain words; the line also stands alone after the section's *Its story* line. Proposed: fix: "Whether the Record Stubs are synced again is reopened if a CBC Run re-applies the same declined edit after two Delivery Takes", moved above the story line.

**FINDING-394.** rule 9; resting on the reader. §2.5, *One cycle, drawn* (lines 152–159, the drawing's legend): "D   the deliverer's history.  R   the run's." The legend writes the Concept Deliverer, the CBC Run, the Delivery Pin, the Read-Through Commit, the Run Reading, the Master Copies, the Delivery Note and the Delivery Staging in lowercase ("the deliverer" 3, "the run" 4, "pin" 5, "read-through" 3, "the reading", "masters", "the note", "the staging"), inside a code block. Proposed: question: does rule 9 reach drawn text? If yes, fix the legend lines; the drawing's letters stay.

**FINDING-395.** rule 7; resting on the reader. §2.5, *One cycle, drawn* (lines 162–163): "Read from the Read-Through Commit, forward in their tree. Deliver from the Delivery Pin, forward in ours." §2.2 (lines 103–105) says it: "To deliver, read the CBC Run's Delivery Pin and diff forward in the Concept Deliverer's tree. To read, read the CBC Run's Read-Through Commit and go forward in the CBC Run's." Proposed: fix: cut lines 162–163; the legend holds it.

**FINDING-396.** rule 2; checked. §3.1, *Delivery Staging* (lines 175–178): "The Delivery Staging is named by the commit at which the files and the Delivery Note are both final — commit the Delivery Note last, then name the bundle — so the Delivery Pin the CBC Run records points at exactly the Delivery Note it read." Three ideas with an instruction between dashes. One more: lines 172–175 ("Whoever copies, the CBC Run's tree is checked quiet first — `git status` there, nothing in flight — and when it is the agent, it reports…"). Proposed: fix: split each; "the bundle" to "the delivery".

**FINDING-397.** rule 2; checked. §3, *Down to the CBC Run*: §3.4 (lines 214–218): "When one group's words must sit in another group's file — the Method Group's playbook inside the Container Group's `PLAN.md` — that is a **Delivery Fill**: the owning group's file has a marked place, the other group provides the text, the Delivery Staging writes it in." Four ideas. Five more: §3.2 lines 188–191; §3.3 lines 198–200 and 201–204; §3.4 lines 211–214; §3.5 lines 229–232. Proposed: fix: split each.

**FINDING-398.** rule 3; checked. §3.7, *The Delivery Note* (lines 256–259): "Where a claim cannot avoid it — a thin Delivery Note, which ships no copy; material outside the delivery; a negative claim, which is about our whole tree — the Delivery Note says so, in a clause." Three cases between dashes with semicolons. One more: §3.2 lines 186–188 (three groups' copies on semicolons). Proposed: fix: a list of three.

**FINDING-399.** rule 4; resting on the reader. §3.4, *One group per file* (lines 218–219): "Delivery Fills are the only step that is not a copy; they are listed in one place and there are few. One exists." "Few" where the count follows at once; "one place" unnamed. Proposed: fix: "they are listed here. One exists. One is owed:".

**FINDING-400.** rule 6; checked. §3.7, *The Delivery Note* (line 272): "the one it gave itself at its Identity Plan Step." Written as a Glossary Name; not in `docs/glossary.md`, not defined here (also `ARCHITECTURE.md` line 169). Proposed: fix: a glossary entry (the Plan Step at which a CBC Run names itself), or plain words: "at the Plan Step where it names itself".

**FINDING-401.** rule 5; resting on the reader. §3.7, *The Delivery Note* (line 256): "gives the CBC Run a hedge it cannot close". Proposed: fix: "gives the CBC Run a claim it cannot check".

**FINDING-402.** rule 3; checked. §4, *The Delivery Take*, step 2 (lines 290–294): "each edit is either answered in the Delivery Note (taken — the new copy carries it; declined — it goes, and the need it served goes to the CBC Run's records) or unanswered, which means it was made after the Concept Deliverer last read, and it is re-applied on top." Three endings (taken, declined, unanswered) nested in parentheses, dashes and semicolons. Proposed: fix: a sub-list of three.

**FINDING-403.** rule 2; checked. §4, *The Delivery Take*, step 3 (lines 298–301): "A receipt branch — the delivery as it arrived, named by the Delivery Pin — is worth cutting when the CBC Run expects to edit, because it makes step 2's diff exact next time. Optional." One more: step 5 (lines 308–310), "Then the Delivery Staging goes — the directory named for the Delivery Pin and its Delivery Note — and nothing else: `temp/` may hold…". Proposed: fix: split each; the definition first, then the advice.

**FINDING-404.** rule 9; uncertain. Delivery Staging is used for two things: the act (the glossary: "copying the delivery and its Delivery Note into a CBC Run's `temp/`") and the staged directory. §4 step 5 (line 308): "Then the Delivery Staging goes — the directory named for the Delivery Pin and its Delivery Note"; also line 97 "the Delivery Staging's name", 176 "is named by the commit", 237 "not in this Delivery Staging", 241, 248 "diff the Delivery Staging against what it holds", 284. Line 177 calls the directory "the bundle". Proposed: question: one Name for both, widened in the glossary; or "the delivery" for the directory and Delivery Staging for the act.

**FINDING-405.** rule 9; resting on the reader. Bold marks a Name at its defining line: `docs/conventions/exchange/README.md` line 95 "**the Delivery Pin**", 96 "**the Read-Through Commit**", 216 "**Delivery Fill**", 333 "**Run Ask**", and italic at 374 "*the Concept Deliverer*"; `docs/conventions/facts-in-sync/README.md` lines 119–120 "**Fact Reference**", 244 "**the Change Walk**". Rule 9: no Markdown mark marks a Name. Proposed: question: is bold at the defining line allowed (the glossary bolds each entry's Name)? If not, unbold the seven.

**FINDING-406.** rule 2; checked. §5, *Editing a copy*: §5.2 (lines 354–357): "A copy the CBC Run has finished with is edited the same way, whenever the evidence is in the CBC Run, and never kept as a note for a later CBC Run: the Concept Deliverer takes or declines an exact hunk rather than translating a note, and the CBC Run that lived the mistake writes the fix." Five ideas. Four more: §5.1 lines 333–335 and 335–338; §5.2 lines 358–362; §5.6 lines 389–391. Proposed: fix: split each.

**FINDING-407.** rule 7; checked. §5.2, *A finished copy* (lines 363–364): "is its trial (ADR-0051). *Its story: ADR-0051.*" The same pointer twice in a row; the same at §5.6 (lines 393–394). Proposed: fix: cut the parenthetical in each; the italic line is the form.

**FINDING-408.** rule 5; resting on the reader. §5.3, *Edits made before a verdict* (lines 368–369): "They stack on the CBC Run's side only. Behind the Concept Deliverer is acceptable; behind the CBC Run's own lessons is not." "Stack" and "behind" stand in for what happens, and the section says it in no other words. Proposed: fix: "They wait on the CBC Run's side. A copy may lag the Master Copy; it may not lag what the CBC Run itself has learned."

**FINDING-409.** rule 9; checked. §5.8, *Filling a Skill Template* (line 408): "such as a line every run needs". "Run" is a CBC Run. Proposed: fix: "every CBC Run needs".

**FINDING-410.** rule 2; checked. §6, *Up from the CBC Run*: §6.3 (lines 447–450): "The read produces a Run Reading, or extends the one open for that CBC Run — a document in `temp/` listing every edit, every Run Ask and every finding, one line each, revised as items close and deleted when the work does." Five ideas. Two more: §6.4 lines 469–472; §6.6 lines 497–500. Proposed: fix: split each.

**FINDING-411.** rule 6; resting on the reader. §6.5, *Verdicts* (line 482): "(`docs/conventions/facts-in-sync/` §5, *A disagreement* owns that rule; it is about every Canonical Description, not only this one)". Prose inside the parentheses; a Fact Reference gives only the address (`docs/conventions/facts-in-sync/` §3.1, lines 166–167). Proposed: fix: "…says otherwise": facts-in-sync owns that rule, for every Canonical Description (`docs/conventions/facts-in-sync/` §5, *A disagreement*).

**FINDING-412.** rule 2; resting on the reader. *Why it arrives this way* (lines 506–508): "The CBC Run's half is an Agent Rule rather than a skill because its moment is a copy, or a file in `temp/`, being read, and it loads then instead of waiting to be opened by name (…)." Three ideas. Proposed: fix: split after "read".

**FINDING-413.** rule 8; resting on the reader. §3.2, *What goes* (line 189): "its records, the two entry files, the Decisions Log, the hygiene files". Which two? §2.4 (line 128) delivers "the entry file once". Proposed: question: `CLAUDE.md` and `temp/README.md`? Name them, or make it one.

##### `docs/conventions/facts-in-sync/README.md`

**FINDING-414.** rule 3; checked. `docs/conventions/facts-in-sync/README.md`, *What it is for* (lines 14–18): "duplicated facts diverged, and diverged records stopped being trusted; the handbook's entry file held three disagreeing copies of one rule (…); CBC Run 3 told one Plan Step's story in four records (its RETRO.md, D1)." Three cases on semicolons. Proposed: fix: a list of three.

**FINDING-415.** rule 7; resting on the reader. *What it is for* (lines 20–21): "Refinement Round 2 of the refinement found its One home and Dependencies kinds". "Of the refinement" adds nothing to the Name, and "its" then has no clear owner. Proposed: fix: "Refinement Round 2 found the One home and Dependencies Finding Kinds standing on rules split that way".

**FINDING-416.** rule 1; resting on the reader. §4, *A Canonical Description's rule* (line 211): "This page included. A Canonical Description is how we understand a thing today…". The section opens on a fragment whose subject comes after it. Proposed: fix: "…the concept, each Idea Model, each manual, this page included."

**FINDING-417.** rule 2; checked. §4, *A Canonical Description's rule* (lines 214–218): "It may be wrong or incomplete, and it is canonical regardless — everything derived from it agrees with it until it changes, and it changes only for a reason recorded, practice being the evidence." Four ideas. Proposed: fix: "It may be wrong or incomplete. It is canonical regardless: everything derived from it agrees with it until it changes. It changes only for a reason recorded, and practice is the evidence."

**FINDING-418.** rule 7; checked. §4, step 2 (lines 227–229): "Every line that uses a part of a document, its root included, carries a Fact Reference to that part (§3.1, *What a Fact Reference is*), the root's parts as much as any other's." "Its root included" and "the root's parts as much as any other's" say one thing twice. Proposed: fix: cut the tail.

**FINDING-419.** rule 9; uncertain. §4, step 2 (lines 225–231): "one `foundation` per file, its root, what the whole of it stands on", then "the root's parts" (229), "one part of the root" (230), "The root says which document to open" (231). "Root" is a second word for what the Foundation Line names. Proposed: question: say "the Foundation Line's document" (or "the foundation") throughout, or keep "root" as defined at line 225.

**FINDING-420.** rule 3; checked. §4, *A Canonical Description's rule* (lines 256–258): "Where a manual and the concept are handled differently — versioning, shipping, the kind of derivative, the Convention Seats, what each asserts — is ADR-0039". Five parts between dashes. Proposed: fix: cut the five (ADR-0039 lists them): "Where a manual and the concept are handled differently is ADR-0039"; or a list.

**FINDING-421.** rule 3; checked. §5, *A disagreement* (lines 268–271): "It is raised where it is found — a finding in a Run Reading, an edit a CBC Run made to its copy, a question at a boundary, the Foundation Check at a commit — and decided, never defaulted: neither side is right for being the Canonical Description, nor for being newer." Four places between dashes, then two more ideas. Proposed: fix: "It is raised where it is found, in one of four places:" a list; then "It is decided, never defaulted. Neither side is right for being the Canonical Description, nor for being newer."

**FINDING-422.** rule 2; checked. §2, *Point and derive* (lines 108–111): "Two relations, two verbs — point and derive — and a reader who finds the subject stated twice has found a defect; the measured case is `docs/conventions/agent-arrangement/`'s, its *What it is for*." Three ideas. Proposed: fix: split at "and a reader" and at the semicolon.

**FINDING-423.** rule 2; checked. §1, *One home* (lines 83–86): "One is the owner and the other follows it: where two copies cannot be avoided, as the version in the build file is followed by the CHANGELOG, or where the reader acts on the fact in place, retold beside its Fact Reference." Two cases, each with an example, nested in one sentence. Proposed: fix: "One is the owner and the other follows it. Two cases: a copy that cannot be avoided, as the CHANGELOG follows the version in the build file; a retelling where the reader acts on the fact in place."

**FINDING-424.** rule 2; checked. §3.2, *Numbering a section's parts* (lines 188–191): "A section divided into labelled parts numbers them, `### N.M`, and so does every section of the same form in the document, whether anything points there yet or not: a Fact Reference names the number, and a reader meets one structure throughout." Four ideas. Proposed: fix: split at "and so does" and at the colon.

**FINDING-425.** rule 2; checked. *Why it arrives this way* (lines 300–302): "One home's moment is every text written: a fact is retold in the record being written, and that record's Record Stub says nothing of the record the fact was taken from, so no Record Stub is open at the moment." Four ideas. One more: lines 305–308 (the check's moment, the `paths:` loading, the script's edit, in one sentence). Proposed: fix: split each.

**FINDING-426.** rule 2; resting on the reader. *The seats*, *The CBC Run's seat* (lines 54–56): "The Change Walk and the disagreement (§4, *A Canonical Description's rule*; §5, *A disagreement*) reach a CBC Run as the Exchange Convention's Run Reading of what it sends back (…)." One idea carrying three Fact References and a possessive chain. Proposed: fix: "A CBC Run meets the Change Walk and the disagreement (…) through the Run Reading we write of what it sends back (…)."

**FINDING-427.** rule 9; resting on the reader. §1, *One home* (line 82): "a retelling whose host is itself a source walks on." "Source" for a Canonical Description; the glossary's Foundation Line entry sets *source* aside. Proposed: fix: "a retelling whose host is itself a Canonical Description is walked in turn".

**FINDING-428.** rule 5; resting on the reader. §1, *One home* (line 82): "walks on". The Change Walk's verb stretched to mean "is walked in turn"; the fix in FINDING-427 covers it. Proposed: fix: as FINDING-427.

**FINDING-429.** rule 5; resting on the reader. §3.1, *What a Fact Reference is* (lines 159–160): "The number lands the reader on a paragraph rather than a wall." "Wall" is one of the method's words, in another sense. Proposed: fix: "rather than on the whole document".

**FINDING-430.** rule 5; resting on the reader. §5, *A disagreement* (line 291): "Whether the concept bends rarely because it is right". Proposed: fix: "changes rarely".

**FINDING-431.** rule 4; resting on the reader. §5, *A disagreement* (lines 291–292): "the concept bends rarely". A frequency; `CHANGELOG.md` counts the concept's changes. Proposed: fix: give the count; or decline, the sentence is about why, not how often.

**FINDING-432.** rule 9; resting on the reader. *Why it arrives this way* (line 305): "The check's moment is every commit". The Foundation Check, named at lines 36 and 60–61. Proposed: fix: "The Foundation Check's moment".

**FINDING-433.** rule 7; checked. *What this does not cover* (line 315): "`docs/conventions/project-recording/` §13, *The records table*, the records table." The title is repeated after itself. Proposed: fix: cut ", the records table".

**FINDING-434.** rule 7; resting on the reader. *Why it arrives this way* (lines 303–305): "and CBC Run 3 still told one Plan Step's story in four records: PLAN, the devlog, the slice record and the commits (its RETRO.md, D1)." Told at lines 17–18 too, without the four names. Also §1 lines 74–75 repeat lines 14–15 ("Duplicated facts diverge, and diverged records stop being trusted"). Proposed: fix: tell the story once with the four names and point from the other; or decline, one is the need and one the channel's reason.

##### `docs/conventions/repo-hygiene/README.md`

**FINDING-435.** rule 2; checked. `docs/conventions/repo-hygiene/README.md` *What it is for* (line 8): "So that a repo never commits what it should not, and never accumulates line-ending noise, from its first commit — the worst ignore is the one added after the junk is committed." Two ideas chained by a dash: what the files are for, and why from the first commit. Proposed: end the sentence at "from its first commit." and let §1's table cell carry the worst-ignore line (FINDING-438).

**FINDING-436.** rule 3; checked. `docs/conventions/repo-hygiene/README.md` *What it is for* (line 12): "Lived since: every CBC Run was born with the base; CBC Run 3 ignored `CLAUDE.local.md` in its own `.gitignore` before the base did (its `aa9b3ec`), and the base carries the line now; CBC Run 3 appended its stack's ignores at its skeleton Plan Step (its `5336563`)." Three parts chained with semicolons in one sentence; a list shows the count. Proposed: "Lived since:" and three bullets.

**FINDING-437.** rule 2; checked. `docs/conventions/repo-hygiene/README.md` §3, *The hygiene rules* (line 82): "A fix that would be true of any project comes back the way every lesson does — the Concept Deliverer reads the CBC Run (`docs/conventions/exchange/` §6, *Up from the CBC Run*) and changes the Master Copy here, so the next birth starts corrected." Three ideas (how a fix comes back; who reads and changes; what the next birth gets) chained with a dash, "and" and "so". Proposed: three sentences.

**FINDING-438.** rule 7; checked. `docs/conventions/repo-hygiene/README.md` *What it is for* (line 9): "the worst ignore is the one added after the junk is committed" — said again in §1's table (line 48): "The worst ignores are the ones added *after* the junk is committed". One can go. A second pair, uncertain: line 31 "they shape the repo by existing" and lines 95-96 "three files that shape the repo by existing". Proposed: keep the table cell and cut the clause at lines 9-10; keep *Why it arrives this way* and cut line 31's second clause, or decline the second pair as each standing where the reader acts.

**FINDING-439.** rule 9; checked. `docs/conventions/repo-hygiene/README.md` §2, *Base and Stack Overlays* (line 68): "# at the skeleton step, with the overlay at hand:". The code block's comment writes a Plan Step as "step" and a Stack Overlay as "overlay"; a lowercase word is English only. Also line 69, "the overlay's directory". Proposed: "# at the Plan Step that makes the stack true, with the Stack Overlay at hand:" and "t=<the Stack Overlay's directory>".

**FINDING-440.** rule 9; uncertain. `docs/conventions/repo-hygiene/README.md` §2, *Base and Stack Overlays* (line 59): "**The base** — stack-agnostic; correct for any repo including a records-only one." The section defines two things; its counterpart "A Stack Overlay" has a Glossary Name and "the base" has none, and the glossary's Stack Overlay entry leans on it (line 151, "below the base's marked line"). 8 other lines: 12, 14, 21, 29, 39, 41, 62, 113. "Base" may be English enough ("a word whose English meaning is ours has no Name"). Question for the reviewer: does "the base" get a Name, or is it English?

**FINDING-441.** rule 9; uncertain. `docs/conventions/repo-hygiene/README.md` *What it is for* (line 15): "CBC Run 3 appended its stack's ignores at its skeleton Plan Step (its `5336563`)." The playbook's label is "Step 4: Skeleton & bootstrap" (`delivery/fills/cbc-run-pure-playbook.md` line 177); a label keeps its case, and here it is a lowercase adjective. Proposed: "at the Plan Step that makes the stack true", the manual's own phrase (lines 38, 61), or "its Skeleton Plan Step".

**FINDING-442.** rule 5; uncertain. `docs/conventions/repo-hygiene/README.md` §1, *The three files* (line 46): "| File | What it governs | Why it must exist from day zero |". "Day zero" stands in for "the first commit", which the opening statement says plainly; it may be a dead idiom. Proposed: "Why it must exist from the first commit", or decline.

##### The hygiene templates

**FINDING-443.** rule 9; uncertain. `docs/conventions/repo-hygiene/templates/java-spring/editorconfig.part` (line 3): "# --- java-spring overlay ---". "Overlay" where a Stack Overlay is meant; the same marker in `gitattributes.part` line 2 and `gitignore.part` line 2, "# --- java-spring (Maven) overlay ---…". A comment is under the rule; whether a config file's marker line names its kind by an English word is the reviewer's. Proposed: "# --- java-spring Stack Overlay ---" in all three, or decline as a marker, not prose.

##### `docs/conventions/retrospective/README.md`

**FINDING-444.** rule 8; resting on the reader. `docs/conventions/retrospective/README.md` *What it is for* (line 9): "The failure is lived, in CBC Run 3, never-oversold." "never-oversold" is CBC Run 3's repository name; the only living line that says so is `ARCHITECTURE.md` line 176, and the apposition reads as a label with no plain words. The same sentence opens `docs/conventions/writing/README.md` (lines 7-8). Proposed: "in CBC Run 3 (its repository, `never-oversold`)" once, or cut the name; both files alike.

**FINDING-445.** rule 8; resting on the reader. `docs/conventions/retrospective/README.md` *What it is for* (line 11): "CBC Run 3 stopped before Release, so the section's moment never came". "Release" is the playbook's last Plan Step, "Step N: Release" (`delivery/fills/cbc-run-pure-playbook.md` line 216); the manual never says so, and outside its owner a label carries it. 5 other lines: 22, 32, 35, 87, 91. Proposed: at line 11, "before Release, the playbook's last Plan Step", and leave the rest; or decline: the reader holds the playbook.

**FINDING-446.** rule 4; uncertain. `docs/conventions/retrospective/README.md` *What it is for* (line 11): "with a few questions". A count exists if §2's "old questions" (lines 109-112: five, and the entry-file re-read) are the section's. Also line 13, "It then did far more than the section asked". Proposed: the count, or decline if the section's questions are not §2's.

**FINDING-447.** rule 6; uncertain. `docs/conventions/retrospective/README.md` *What it is for* (line 23): "and left what CBC Run 3 had proved alone (D24)." A number local to CBC Run 3's RETRO.md carried bare; the owner is named 8 lines above (line 15) and at line 178. Proposed: "(its RETRO.md, D24)".

**FINDING-448.** rule 6; uncertain. `docs/conventions/retrospective/README.md` *What it is for* (line 15): "(its RETRO.md, D23)". The same file writes "`RETRO.md`" with backticks at lines 35, 142 and 178; a reference written two ways in one file. `docs/conventions/writing/README.md` lines 21 and 67 write it bare too. Proposed: backticks on all three bare ones.

**FINDING-449.** rule 3; checked. `docs/conventions/retrospective/README.md` *The CBC Run's seat* (line 51): "**In the look back, the reviewer decides** whether small commits are free on the branch; each decision: agree, correct, or drop; each experiment: keep or drop; when the branch lands." Four decisions chained with semicolons in one sentence, then three things "They get" the same way (lines 53-56); the apply bullet chains six decisions (lines 57-60). Proposed: a list under each bold lead, one decision per line; or decline: "In summary of them" says the skills hold the list.

**FINDING-450.** rule 4; uncertain. `docs/conventions/retrospective/README.md` *The CBC Run's seat* (line 65): "CBC Run 3's apply guide restated nearly every rule of its skill." A count (n of m rules) exists if the guide is still readable in CBC Run 3. Proposed: the count, or decline if the guide is gone.

**FINDING-451.** rule 2; checked. `docs/conventions/retrospective/README.md` *The Concept Deliverer's seat* (line 73): "At the close of the Plan Step that runs the next Run Birth, it runs both skills on itself, from `delivery/container/`, in place of that item: the parts are its own (the concept, the conventions, the delivery, the exchange, its records), and the next Plan Step stands where a CBC Run has its next CBC Run." Four ideas (when; what runs and from where; what its parts are; what stands for the next CBC Run) in one sentence with a colon, a parenthesis and "and". Lines 71-73 chain two more with a semicolon and "which". Proposed: one sentence per idea.

**FINDING-452.** rule 8; resting on the reader. `docs/conventions/retrospective/README.md` §3, *How the lessons are applied* (line 129): "**The order of the commits follows influence.** Repeats go before rewriting, so no text is polished and then deleted. Owners go before the records that summarize them, README last. Plain words last." "Repeats" and "Plain words" are the apply skill's Stage 2 list compressed to labels (the skill says "remove repeats before rewriting", "plain words last"); the manual gives no plain words for what they are as commits. Proposed: "Removing repeats goes before rewriting" and "The plain-words rewrite goes last".

**FINDING-453.** rule 7; uncertain. `docs/conventions/retrospective/README.md` §1, *Two Plan Steps, not one* (line 91): "Both come before Release, so they happen even when Release is skipped. That is the failure of a section filled at the project's end." The same lesson is told at lines 11-13 (*What it is for*) and lines 158-160 (*Why it arrives this way*). Rule 7 names only a sentence that repeats its predecessor; these sit in three sections. Proposed: cut §1's last paragraph (lines 91-93), which §1's first paragraph and the channel section already say; or decline.

**FINDING-454.** rule 10; uncertain. `docs/conventions/retrospective/README.md` §1 (line 81): "## 1. Two Plan Steps, not one". "Not one" is a gloss after a comma, and the title states the point rather than naming the subject (the manual's rule 10: "a title that states the point says it twice"). Proposed: "The two Plan Steps".

**FINDING-455.** rule 2; uncertain. `docs/conventions/retrospective/README.md` *Why it arrives this way* (line 158): "A section in the plan did not work: its moment was the project's end, which a CBC Run that stops early never reaches, and a section can hold questions but not a way of working." Three ideas chained with a colon, "which" and "and". Proposed: three sentences.

**FINDING-456.** rule 3; uncertain. `docs/conventions/retrospective/README.md` §2, *How the look back decides* (line 109): "**The old questions still ask:** which Plan Steps took longer or shorter, what needed to happen earlier, what was tried and dropped, what had no home, which gate items caught nothing; and the entry file read top to bottom, its only re-reading (…)." Six parts in one sentence, five by comma and one after a semicolon. Proposed: a sub-list of six; or decline: they are prompts, read as one.

##### `docs/conventions/shapes/README.md`

**FINDING-457.** rule 2; checked. `docs/conventions/shapes/README.md` *What it is for* (line 14): "Made a convention, with this page as its manual, on 2026-09-27 (ADR-0037): the Agent Rule binds, and this page is why the Agent Rule is as it is, so that "why is this a directory and not a rules file?" has an answer that is not archaeology." Four ideas (made a convention; the Agent Rule binds; this page is the why; what question it answers) chained with a colon, "and" and "so that". Lines 11-14 chain two more with "and". Proposed: one sentence per idea.

**FINDING-458.** rule 5; checked. `docs/conventions/shapes/README.md` *What it is for* (line 18): "has an answer that is not archaeology". A figure for "an answer that needs no digging through old records". Proposed: "has an answer on this page".

**FINDING-459.** rule 2; uncertain. `docs/conventions/shapes/README.md` *What this is made usable as* (line 24): "**`delivery/container/.claude/rules/shapes-lifecycle.md` — the Agent Rule, shipped**, held at `.claude/rules/shapes-lifecycle.md` and loading when a file under `.claude/shapes/` is touched (§1, …; §3, …; §4, …; §5, …), from the CBC Run's Convention Seat, with the definition repeated because a CBC Run cannot open this page." Five facts in one sentence; the section's form packs the first two in every manual, the last three could stand alone. Proposed: end after the Fact References, then "It states the CBC Run's Convention Seat, and repeats the definition, since a CBC Run cannot open this page."

**FINDING-460.** rule 2; checked. `docs/conventions/shapes/README.md` *The Concept Deliverer's seat* (line 54): "Two of its own forms, a Run Reading's and a manual's, are Agent Rules today, with a Governs line, loaded when the file is read, not while a new one is written (…); whether they become Output Shapes read at a Plan Step's gate is the TODO item "Decide whether our own forms become Output Shapes"." Two ideas joined by a semicolon, the first carrying three qualifiers. Line 53 (a dash aside) and lines 58-61 ("It holds … and reads …") the same. Proposed: one sentence per idea.

**FINDING-461.** rule 2; checked. `docs/conventions/shapes/README.md` §3, *One place, read at the gate* (line 145): "And where an Output Shape names a part only the work can produce — a backstop "seen at the red run" can only be known by looking during the red run — the skill that runs the work asks for it too." The example sits inside the rule between dashes; the sentence must be held whole. Proposed: the rule first, the example as its own sentence.

**FINDING-462.** rule 1; checked. `docs/conventions/shapes/README.md` §4, *An Output Shape between repos* (line 155): "Stated here once; `delivery/README.md` points here." The section opens with where the fact is stated and a pointer (*What this is made usable as* lines 34-35 already gives both); its point, "Between repositories, an Output Shape follows the group of the thing it shapes", is the third sentence. Proposed: open with the third sentence; cut the first (rule 7) or move it to the end.

**FINDING-463.** rule 3; uncertain. `docs/conventions/shapes/README.md` §4, *An Output Shape between repos* (line 158): "A slice record's Output Shape is `method/`; a Spring harness file's is `spring-postgres/`; a devlog entry's or a commit plan's is `container/`." Three parts chained with semicolons; short, and the count readable. Proposed: three bullets, or decline.

**FINDING-464.** rule 5; uncertain. `docs/conventions/shapes/README.md` §4.1, *Nothing fetched* (line 176): "*Named in ADR-0037 as a third act of the exchange, and never built: …*". "A third act of the exchange" is the figure writing rule 5 gives as its own example; here it is ADR-0037's naming, reported. Proposed: quotation marks on ADR-0037's words, or "a third step of the exchange".

**FINDING-465.** rule 9; checked. `docs/conventions/shapes/README.md` §4.3, *Birth and delivery, drawn* (line 209): `subgraph HERE["the deliverer"]`. The picture's labels write the Concept Deliverer, an Output Shape, a Plan Step, a Run Reading, a Delivery Pin and a CBC Run as "the deliverer", "a shape" (line 211), "a step" (line 216), "a reading", "its pin", "the run's own shapes" (line 222); a lowercase word is English only. "a Run Repo" (line 214) is a Name. Proposed: the Names in the labels, the boxes widening; or the reviewer says a picture's labels are outside the rule.

**FINDING-466.** rule 9; checked. `docs/conventions/shapes/README.md` §5.1, *Use, drawn* (line 252): `CLOSE["a step closes"] --> GOV{"does any shape govern<br/>what this step made?"}`. "Step" for Plan Step and "shape" for Output Shape, also lines 254, 259, 260, 262. Proposed: as FINDING-465, decided with it.

**FINDING-467.** rule 2; checked. `docs/conventions/shapes/README.md` §4.3, *Birth and delivery, drawn* (line 226): "The traffic model — nothing sent upward, nothing fetched, the Concept Deliverer reading a CBC Run and never the reverse — is the Tiers Model's (…), and the Run Reading is the Exchange Convention's (…)." Two ideas, the first with a three-part aside between dashes. Lines 229-233 and 235-237 ("…one project saying what it arrived at — and it travels by being *read*, not by being sent.") chain the same way. Proposed: one sentence per idea; the aside as its own sentence.

**FINDING-468.** rule 5; checked. `docs/conventions/shapes/README.md` §4.3, *Birth and delivery, drawn* (line 226): "The traffic model". "Traffic" stands in for the flows between the tiers; the Tiers Model's word is "flow" (`docs/models/tiers.md` §3, *The flows*; §3.5, *What holds on every flow*), and "traffic" is not in it. Proposed: "The flows — … — are the Tiers Model's".

**FINDING-469.** rule 3; checked. `docs/conventions/shapes/README.md` §5.2, *A tick, and a difference* (line 278): "It ends one of four ways, decided per difference and never by a policy of preferring one side: **the output drifted**, so it is brought to the Output Shape; **the Output Shape was wrong here**, so it changes and the output stands; **each had something**, and both move; or **the output is a different kind**, so both stand and a new Output Shape starts from it (§1.2, *How an Output Shape is born*)." Four parts chained with semicolons in one sentence; the picture above (lines 259-262) and `.claude/rules/foundation-check.md` step 5 show the same four as a list. Proposed: the lead sentence to the colon, then four bullets.

**FINDING-470.** rule 2; uncertain. `docs/conventions/shapes/README.md` §5.2, *A tick, and a difference* (line 267): "A gate reads what a Plan Step made against every Output Shape governing it, and **what it ticks records what it checked against** — including that nothing governed, which is an answer rather than an omission." Three ideas chained with "and", a dash and "which". Proposed: three sentences.

**FINDING-471.** rule 10; uncertain. `docs/conventions/shapes/README.md` §3 (line 133): "## 3. One place, read at the gate". Two phrases, the second a gloss after a comma; §4.3 (line 195) "Birth and delivery, drawn" and §5.1 (line 243) "Use, drawn" the same, and "Use, drawn" does not stand alone. Rule 10 names a dash or colon, not a comma. Proposed: "Where an Output Shape lives", "The birth and delivery picture", "The gate picture"; or decline: a comma is not the gloss the rule names.

**FINDING-472.** rule 10; uncertain. `docs/conventions/shapes/README.md` §4.1 (line 170): "### 4.1 Nothing fetched". A statement (nothing is fetched) rather than a noun phrase naming the subject. Proposed: "What a project fetches", or decline.

**FINDING-473.** rule 8; uncertain. `docs/conventions/shapes/README.md` §2, *What an Output Shape is not* (line 111): "The differences are the reason the entry exists." Nothing in the file names an entry; the line reads as left from when the definition was a vocabulary entry (ADR-0035), and the reader cannot resolve it. Proposed: "The differences are why this section exists", or cut (rule 7).

**FINDING-474.** rule 9; uncertain. `docs/conventions/shapes/README.md` §1.1, *What an Output Shape says* (line 67): "An **Output Shape** says what a kind of output looks like: its form, never its content." Bold marks the Name at its definition; rule 9 says no Markdown mark marks a Name. The glossary bolds Names, but that is the list's form. Proposed: drop the bold.

##### `docs/conventions/visual-comparison/README.md`

**FINDING-475.** rule 2; checked. `docs/conventions/visual-comparison/README.md` *What it is for* (line 10): "The failure is lived, twice, on 2026-09-18: two Mermaid dialects, each built for the job in hand, failed only when rendered — `block-beta` lost its arrow labels, and `sequenceDiagram` had to draw a read-only Run Reading as an arrow into the other repo, asserting the opposite of the rule the procedure existed to keep (ADR-0027, ADR-0028)." Four ideas (two dialects failed at the render; what each lost; what the second asserted) held in one sentence with a colon, a dash, "and" and a participle. Lines 15-17 chain two more with "which". Proposed: one sentence per idea; the two failures as a labeled pair.

**FINDING-476.** rule 8; uncertain. `docs/conventions/visual-comparison/README.md` §1, *What a comparison is* (line 44): "The general method, plus the one failure mode only a picture has: a notation that asserts something you did not mean." A fragment; "The general method" names nothing the file has said, and the reader must guess it is the first paragraph. Proposed: "A comparison is that method, plus the one failure mode only a picture has: …".

**FINDING-477.** rule 2; uncertain. `docs/conventions/visual-comparison/README.md` §1, *What a comparison is* (line 52): "A name that named a picture would have kept the table and the numbered list out of the set, which is where ADR-0028's best answer to one requirement came from." Two ideas chained by "which". Proposed: "…out of the set. ADR-0028's best answer to one requirement was one of those."

**FINDING-478.** rule 4; checked. `docs/conventions/visual-comparison/README.md` §2.4, *The buildable notations* (line 82): "The buildable notations are few, and the constraint is not aesthetic." "Few" where the count is two, and the next sentence names them (Mermaid and Unicode box drawing). Proposed: "The buildable notations are two, and the constraint is not aesthetic."

**FINDING-479.** rule 5; checked. `docs/conventions/visual-comparison/README.md` §2.4, *The buildable notations* (line 86): "A diagram nobody can read in review is a binary blob with extra steps." A joke figure for "as unreadable in a diff as a binary file". Proposed: "A diagram nobody can read in review is as opaque in a diff as a binary file."

**FINDING-480.** rule 5; uncertain. `docs/conventions/visual-comparison/README.md` §2.3, *Fighting a notation* (line 75): "Fighting a notation is losing." and line 78, "which parts are load-bearing". Both figures; both common technical idiom, perhaps dead. Proposed: decline, or "A candidate that works against its notation has already failed" and "which parts carry meaning".

**FINDING-481.** rule 2; uncertain. `docs/conventions/visual-comparison/README.md` §2.3, *Fighting a notation* (line 75): "Invisible links, spacer nodes, nodes declared out of meaning order — a candidate needing them has already failed, because the next person to edit it will not know which parts are load-bearing." Three examples, a dash, the rule, and its reason in one sentence. Proposed: the rule first, the examples as a sentence, the reason as a sentence.

**FINDING-482.** rule 7; uncertain. `docs/conventions/visual-comparison/README.md` §2.1, *A non-picture in the set* (line 64): "This is the rule the naming mistake would have broken, written down so the mistake is not available again." §1's last paragraph (lines 50-54) already tells the naming point. Proposed: cut; or decline: §1 says why the name, §2.1 says the rule it protects.

##### `docs/conventions/writing/README.md`

**FINDING-483.** rule 2; checked. `docs/conventions/writing/README.md` *The seats* (line 46): "The Concept Deliverer writes under its own: its chat and records, and also what CBC Runs read, since an agent copies the voice it reads: every new or changed line of a skill, Agent Rule, Output Shape, Approach on Trial, concept chapter or note follows it, and so do its manuals." Four ideas (what it writes under; what that covers; why; which lines) in one sentence with two colons, "since" and "and so do". Proposed: one sentence per idea.

**FINDING-484.** rule 2; checked. `docs/conventions/writing/README.md` §2, *Why each rule* (line 101): "A thing hung on one English word makes the reader decide at every use which is meant, "staging" the exchange's or git's; two words say what the thing is and whose, and the capitals say it is defined before the words are read, as a contract's "the Deliverer" or Kubernetes' "a Pod" do." Four ideas chained with a semicolon, "and" and "as". Rule 10's lines 114-117 ("A title is read in every Fact Reference to its section, where the sentence already says the point; a title that states the point says it twice, and changes when the rule does.") the same. Proposed: one sentence per idea.

**FINDING-485.** rule 5; uncertain. `docs/conventions/writing/README.md` §2, *Why each rule* (line 101): "A thing hung on one English word". "Hung on" stands in for "named by". Proposed: "A thing named by one English word".

##### `docs/glossary.md`

**FINDING-486.** rule 6; checked. `docs/glossary.md` header comment (line 13): "the Exchange Convention, never by the bare word." The header gives "the Exchange Convention" as the example Name for a convention, and 36 living lines use it (`ARCHITECTURE.md` 54, 76; `docs/models/tiers.md` 71; `docs/conventions/shapes/README.md` 229; the exchange skills and rules; …), but no entry lists it. Rule 6 defines each Glossary Name once in the glossary; rule 9 writes it "exactly as `docs/glossary.md` lists it". Proposed: an entry under Kinds of text after Convention Manual, "**Exchange Convention** — the convention at `docs/conventions/exchange/`; a convention's Name is its directory's word and Convention", or a sentence in the Convention Manual entry saying how a convention is Named.

**FINDING-487.** rule 9; checked. `docs/glossary.md` Stack Overlay entry (line 151): "repo-hygiene's `.part` files for one stack". The glossary's own header (lines 11-13) says a convention is named by its path in backticks or by its Name, never by the bare word. Also line 202, "How a skill names them is the conventions manual's", and `docs/conventions/writing/README.md` line 132, "commit-messages' rule for a body and nothing else". Proposed: "the `.part` files under `docs/conventions/repo-hygiene/templates/`"; "How a skill names them: (…)" with the Fact Reference alone; "the rule of `docs/conventions/commit-messages/` for a body".

**FINDING-488.** rule 9; checked. `docs/glossary.md` Newborn Run entry (line 35): "It holds what the seed put there, one Delivery Pin included, and no earlier state." "The seed" for the Pure Seed; a lowercase word is English only. Proposed: "what the Pure Seed put there".

**FINDING-489.** rule 3; uncertain. `docs/glossary.md` Refinement Layer entry (line 207): "**Refinement Layer**, **Refinement Round**, **Finding Kind** — the refinement's words: a set of files fixed together; the kinds whose fixes do the same to the text, read together; one rule read against, and the findings it makes". Three Names paired with three definitions by position across semicolons; the reader pairs them by counting. Same at lines 23-26 (three Names, three definitions after commas) and 80-84 (three Names, three paths). Proposed: one entry per Name, as the header (line 6) says; or decline: the grouped form is the glossary's.

**FINDING-490.** rule 8; uncertain. `docs/glossary.md` Made Usable entry (line 105): "what a stated body becomes in the delivery: the concept as the method, the conventions as the container." "A stated body" has no plain words; the reader infers "a body of text that states". Proposed: "what a body of text becomes in the delivery: the concept becomes the method, the conventions become the container".

**FINDING-491.** rule 2; uncertain. `docs/glossary.md` Canonical Description entry (line 90): "It may be wrong or incomplete and is the one that counts regardless; what derives from it applies it and does not explain." Three ideas chained with "and" and a semicolon. Proposed: three sentences.

##### `docs/models/agent.md` (FINDING-492 to 494 span the three models)

**FINDING-492.** rule 1; resting on the reader. `docs/models/agent.md` (lines 3-4): "Deliberately incomplete — a structure to test, not a finished description." The first line says the point; here the first line is the file's status, and what the file is comes at line 8 ("A structured description of what an AI agent..."). The same order in `docs/models/idea-to-output.md` line 3 ("A draft: written from one full chain...") and `docs/models/tiers.md` line 3 ("A draft: revised when..."). Proposed: question — is the status line a fixed opening of the model form, standing outside rule 1 as the manual form's fixed headings stand outside rule 10; if not, put the description first in all three files.

**FINDING-493.** rule 2; checked. `docs/models/agent.md` (lines 12-14): "It binds what stands on it, and when the two disagree, either side may be the wrong one". One idea per sentence; this one carries two, joined by "and when". The same sentence in `docs/models/idea-to-output.md` lines 12-14 and `docs/models/tiers.md` lines 11-13. Proposed: fix: "It binds what stands on it. When the two disagree, either side may be the wrong one (...)." in all three.

**FINDING-494.** rule 9; resting on the reader. `docs/models/agent.md` (line 12): "This is an **Idea Model**: the top Canonical Description of its chain." No Markdown mark marks a Name; the bold sits on the Name. Also `docs/models/idea-to-output.md` 12; `docs/models/tiers.md` 11, 44 ("A **Concept Repo**"), 53 ("The **Concept Garden**"), 61 ("A **Run Repo**"), 129 ("**the Delivery Pin**"): 7 lines in all. Proposed: fix: drop the bold at the 7; or decline, if the reviewer reads it as the defining sentence's emphasis, which rule 9 does not except.

**FINDING-495.** rule 8; checked. `docs/models/agent.md` (line 18): "Layer 1 — vendor-neutral. One tool's mechanisms are a **binding**". A label is said in plain words before it is used; "Layer 1" is used here and said at §10, line 239 ("Bindings are Layer 2. Layer 1 names capabilities"), 220 lines on. It also sits beside the concept's LAYER-1-ENVIRONMENT (glossary: System Layer). Proposed: fix: "Vendor-neutral: this Idea Model names capabilities, its Layer 1. The mechanisms one tool gives them are a binding, its Layer 2 (§10, *The bindings*)."

**FINDING-496.** rule 2; checked. `docs/models/agent.md` §4, *The channels* (lines 70-73): "They differ in **when they fire** and **what they guarantee** — and a rule's reliability is a property of the channel it travels, not of how well the rule is written." Two ideas joined by a dash: how the channels differ; where a rule's reliability lies. Also 81-82 ("Grows without bound if used as a rulebook; each addition dilutes the rest."), 83-85, 136-137: 3 more. Proposed: fix: end the sentence at "guarantee"; then "A rule's reliability is a property of the channel it travels, not of how well the rule is written."

**FINDING-497.** rule 3; checked. `docs/models/agent.md` §4.1, *ambient* (lines 86-89): "An operator's standing file fires and costs like the entry file but belongs to one person and one checkout, stays out of the repo's history, and its words never enter records." Parts get their own line; four properties are chained in one sentence with "but", commas and "and". Proposed: fix: four sentences, or a sub-list of four under *Ownership*.

**FINDING-498.** rule 2; checked. `docs/models/agent.md` §5, *The context window* (lines 174-178): "The harness does mark three things apart — its own wiring, the prompt, and what tools return — and an agent weighs them in that order: a rule in the prompt beats the same rule's contrary in a file, and a file's rule holds only until the prompt says otherwise (§12, *Claims* W2)." Four ideas in one sentence: three things marked; their order; prompt beats file; file holds until the prompt says. Proposed: fix: "The harness marks three things apart: its own wiring, the prompt, and what tools return. An agent weighs them in that order. A rule in the prompt beats the same rule's contrary in a file. A file's rule holds only until the prompt says otherwise (§12, *Claims* W2)."

**FINDING-499.** rule 5; resting on the reader. `docs/models/agent.md` §5 (line 174): "**Roled above that.**" A coined word; English has no verb "to role". Also 190 "evaporate at session end"; 231 "a rule that rides in the files a project is born with"; 255 "Backend-ness does not change how context loads"; 73 "the channel it travels" (near dead, counted only): 4 more. Proposed: fix: "Ranked by role above that."; "are gone at session end"; "a rule carried in the files"; "Being a backend does not change how context loads."; leave "travels".

**FINDING-500.** rule 7; resting on the reader. `docs/models/agent.md` §6, *Write-back and persistence* (lines 188-190): "Only what is written into the repo survives the session. The context window, the reasoning that filled it, and every decision not recorded evaporate at session end." The second sentence says the first, negated; it adds only the list of what is lost. Proposed: fix: one sentence: "Only what is written into the repo survives the session: the context window, the reasoning that filled it, and every decision not recorded are gone at its end."; or decline: the list is the point.

**FINDING-501.** rule 3; resting on the reader. `docs/models/agent.md` §7, *The gate* (lines 200-203): "Only a check outside the text — a hook, CI, a human review, or the tool's own permission prompt, which is a human review the tool forces — turns "should" into "cannot"." Four kinds of check inside dashes in one sentence, the fourth with a nested gloss; also 206 "ambient/pulled/pushed", three channels joined by slashes. Proposed: fix: "Only a check outside the text turns "should" into "cannot": a hook, CI, or a human review. The tool's permission prompt is a human review the tool forces."; at 206, "ambient, pulled or pushed".

**FINDING-502.** rule 2; resting on the reader. `docs/models/agent.md` §10, *The bindings* (lines 241-243): "It changes with the tool's releases, so the repo that uses the tool writes it, beside its arrangement, and this Idea Model changes only when an idea does." Three ideas: it changes with releases; so the using repo writes it; the model changes only with an idea. Proposed: fix: "It changes with the tool's releases. So the repo that uses the tool writes it, beside its arrangement. This Idea Model changes only when an idea does."

**FINDING-503.** rule 8; checked. `docs/models/agent.md` §12, *Claims* (line 270): "where it was seen: the handbook's history, this repo's, or a CBC Run's." The reader meets "the handbook" here first, with no words saying it is the repo that held the working arrangement before this one and is history (ADR-0038; `docs/models/tiers.md` §2.1 tells it without the name). Not in `docs/glossary.md`. Also 282, 283, 292, 353, 390, 405; `docs/models/idea-to-output.md` 110 "the Idea Models before this one came from the handbook": 7 more. Proposed: fix: at 270, "the handbook, the repo that held the working arrangement before this one and is history (ADR-0038)"; question: a Glossary Name, or a proper name one line defines.

**FINDING-504.** rule 8; resting on the reader. `docs/models/agent.md` §12.2, *On pulled* (line 319): "**this is the claim that decides router vs rulebook.**" Two labels for the two ways to write an entry file, said in plain words nowhere (§4.1 has "used as a rulebook", 82, and "orientation and routing", 92); 419 writes the pair as "router versus rulebook". Also 373 "a change-plans stop", a skill of the time named as if held. Proposed: fix: at 319, "decides whether the entry file is a router, pointing at each rule at its moment, or a rulebook, holding the rules"; "versus" at both; at 373, "a stop the change-plans skill of the time asked for".

**FINDING-505.** rule 2; checked. `docs/models/agent.md` §12.5, *On the context window* (lines 366-369): "Text in the harness's own wiring outranks the prompt, which outranks anything a tool returned — so a file's rule loses to a contrary rule in the prompt, and a told rule exists only in the session it was told to." Three ideas chained with "which", a dash and "and". Also in §12: 285-288 (A1's second evidence), 291-295 (A1's open question), 362-364 (W1's precedence note): 3 more. Proposed: fix: "Text in the harness's own wiring outranks the prompt. The prompt outranks anything a tool returned. So a file's rule loses to a contrary rule in the prompt, and a told rule exists only in the session it was told to."

**FINDING-506.** rule 3; resting on the reader. `docs/models/agent.md` §12.4, *On observed* (lines 345-346): "here, three divergences were missed until a comparison was run for another reason." The three are told in running prose to line 354; a list would show the count the sentence gives. Proposed: fix: three sub-bullets, one per divergence; or decline: the section's evidence lines are prose by its form.

**FINDING-507.** rule 10; resting on the reader. `docs/models/agent.md` §4.1 (line 75): "### 4.1 ambient". A title is in sentence case; the six channel titles (75, 95, 106, 118, 128, 139) are lowercase, the channel's word as the model writes it in prose. 15 Fact References in living text name a lowercase §4.n title, 2 of them from outside this file (`docs/models/tiers.md` 88, `docs/conventions/agent-arrangement/README.md` 526, both *told*). Proposed: question — keep the lowercase as the model's convention and have rule 10 say so, or capitalise the six and run the rename grep on the 15.

**FINDING-508.** rule 6; resting on the reader. `docs/models/agent.md` §3, *The components, drawn* (line 62): "next session starts empty (§6)". A reference is written in full; this one has no title. Also the bare convention names 287 "commit-messages skill", 288 "commit-plan revisions", 293 "commit-plan's own revision form", 350 "project-recording said", 389 "commit-messages states": the glossary's header says a convention is named by its path in backticks or by its Name, never by the bare word (283 has `commit-messages` in backticks): 5 more. Proposed: fix: "(§6, *Write-back and persistence*)" in the drawing; backticks on the five.

**FINDING-509.** rule 9; uncertain. `docs/models/agent.md` §4, *The channels* (line 70): "Five carry text into the context window." A thing a text defines gets a Glossary Name; the six channels (ambient, pulled, pushed, told, observed, installed), the gate, the write-back and a binding are defined here, each on one lowercase English word, and none is in `docs/glossary.md`; `docs/models/tiers.md` 83 titles a section "The told channel". The round's brief excepts the concept's words, not the Agent Model's; 422 "**installed**" and 18 "**binding**" carry bold besides. Proposed: question — are the Agent Model's words its own, like the concept's, to be said so where that exception lives; or does each get a Name (Ambient Channel, Told Channel, ...), a change that reaches every manual's *Why it arrives this way*.

##### `docs/models/idea-to-output.md`

**FINDING-510.** rule 4; checked. `docs/models/idea-to-output.md` §1, *The chain* (line 29): "most manuals stand on none." A count exists: 4 of the 12 manuals carry a `foundation:` line (conventions, facts-in-sync, exchange, agent-arrangement), so 8 of 12 stand on none. Proposed: fix: "8 of the 12 manuals stand on none (2026-10-30)"; or decline: the number moves with each manual written, and "most" does not go stale.

**FINDING-511.** rule 9; checked. `docs/models/idea-to-output.md` §1 (line 21): "model ──► description ──► approach ──► output" and (line 24) "shape ◄── written from outputs". A lowercase word is English only; the drawing writes Idea Model, Canonical Description, Work Approach and Output Shape by their second word. §4.2's drawing (99-100) mixes: "Approach on Trial" by Name, "convention ──► model" and "outputs ──► shape" not. Proposed: fix: the Names in both drawings, widened; or decline: a drawing's labels are short by design and §2's table gives the Names.

**FINDING-512.** rule 9; checked. `docs/models/idea-to-output.md` §4.2, *Up, work to an idea* (lines 108-109): "by an Approach still on Trial," A Name is written exactly; "still" splits it. Proposed: fix: "by an Approach on Trial still open,".

**FINDING-513.** rule 9; resting on the reader. `docs/models/idea-to-output.md` §4.1, *Down, an idea to an output* (lines 90-91): "the manual is made usable as skills, Agent Rules and forms;" — "forms" where Output Forms are meant (glossary: Output Form, a Work Approach), beside "Agent Rules" by Name. Also 152 "the skills, Agent Rules and forms a project acts on"; 24 "a form" in the drawing: 2 more. 37 "a record's form" is the glossary's own wording for a particular one. Proposed: fix: "Output Forms" at 91 and 152; or they agree: skills have no Name and stand lowercase in the same list, and "forms" is the same kind of English.

**FINDING-514.** rule 3; resting on the reader. `docs/models/idea-to-output.md` §4.1 (lines 90-92): "An Idea Model is adapted by a manual; the manual is made usable as skills, Agent Rules and forms; work done with them leaves outputs." Three steps chained with semicolons. Proposed: fix: three sentences, or a numbered list of three; or decline: it reads §1's drawing left to right in one line.

**FINDING-515.** rule 8; resting on the reader. `docs/models/idea-to-output.md` §7, *One chain here* (line 173): "above `agent-arrangement`, which stands above the entry file's guard" — "guard" is agent-arrangement's word (its manual, line 183, "the Record Stub's guard comment"), met here first with no plain words. Proposed: fix: "the entry file's guard, the comment in it that says what the file must not become,"; or a Fact Reference to the manual's section.

**FINDING-516.** rule 2; resting on the reader. `docs/models/idea-to-output.md` §2, *The kinds* (lines 41-43): "It is written from outputs, and governs the next one; written from the Work Approach, it would describe intent, as a template does." Three ideas, "and", a semicolon and an "as" clause. Also 172-174 ("The Agent Model stands above `agent-arrangement`, which stands above ... ; their content is the output."), 107-110: 2 more. Proposed: fix: "It is written from outputs and governs the next one. Written from the Work Approach, it would describe intent, as a template does."

**FINDING-517.** rule 10; uncertain. `docs/models/idea-to-output.md` (line 88): "### 4.1 Down, an idea to an output" and (line 94) "### 4.2 Up, work to an idea". A title is one phrase with no gloss after a dash or colon; these carry a gloss after a comma. 7 Fact References name §4.2's title, 1 names §4.1's. Proposed: question — is a comma gloss a gloss under rule 10? If yes: "The downward direction" / "The upward direction", and the rename grep on the 8.

##### `docs/models/tiers.md`

**FINDING-518.** rule 1; checked. `docs/models/tiers.md` §2.1, *The empty top tier* (lines 33-36): "A repo that owns the working arrangement — how projects are recorded, how conventions are authored and delivered, what an agent is — was built once, ahead of its evidence, and is history (ADR-0038)." The first sentence is history; the section's point, that the Concept Repo holds the method today and a repo above waits for three lived repos, is sentences 2 and 3. Proposed: fix: open with "The top tier is empty: today the Concept Repo holds the method its Run Repos are born with, as its own." and let the history follow.

**FINDING-519.** rule 2; checked. `docs/models/tiers.md` §2.2, *Concept Repos* (lines 44-50): "A **Concept Repo**: one repo per concept, each keeping the full records any project keeps, derived from the manuals (ADR-0042), and holding two layers: its Canonical Descriptions (the plain-words statement of the idea, its rationale, open questions, and the log of what changed it and why) and what is Made Usable from them (agent skills, checklists, templates, birth materials for projects that follow the concept), each stating which concept version it derives from." One sentence of seven lines: what it is; its records; two layers, each with a list in parentheses; a trailing clause. Also 53-55 (the Concept Garden sentence: a dashed aside, a list of three, an "until" clause), 33-36 (FINDING-518's sentence), 62-64: 3 more. Proposed: fix: "A Concept Repo is one repo per concept. It keeps the full records any project keeps, derived from the manuals (ADR-0042). It holds two layers. 1. Its Canonical Descriptions: the plain-words statement of the idea, its rationale, its open questions, and the log of what changed it and why. 2. What is Made Usable from them: agent skills, checklists, templates, birth materials for projects that follow the concept. Each states which concept version it derives from."

**FINDING-520.** rule 3; resting on the reader. `docs/models/tiers.md` §2.1 (lines 37-39): "A second repo that needs it copies parts; a third does the same; only after three is a repo above them considered, from what the three lived." Three steps with semicolons. Proposed: fix: three sentences; or decline: a count to three reads as one line.

**FINDING-521.** rule 2; checked. `docs/models/tiers.md` §3.1, *Downward delivery* (lines 76-80): "And a Delivery Fill: text written at birth into a file the Run Repo owns from then on, never re-copied (here, for example, a playbook's Plan Steps written into a CBC Run's plan: `delivery/README.md` §2, *Three ways a file lands*), and folded back by name at the Run Repo's retrospective, into the playbook that seeded it." Four ideas with an example and a Fact Reference inside. Also §3.2 87-90 ("That is the told channel, unpinned by design (...), and the Run Repo's records say it was told; it is not a third form of delivery, and a Run Repo that leans on it has the diagnostic told carries."), 90-92, §3.3 98-100, §3.4 106-109: 4 more. Proposed: fix: "And a Delivery Fill: text written at birth into a file the Run Repo owns from then on. It is never re-copied. At the Run Repo's retrospective it is folded back by name into the playbook that seeded it. Here, for example, a playbook's Plan Steps are written into a CBC Run's plan (`delivery/README.md` §2, *Three ways a file lands*)."

**FINDING-522.** rule 8; uncertain. `docs/models/tiers.md` §3.1 (lines 80-81): "At a Run Birth the two meet, both input to Framing rather than agreement." Which two meet (the copy and the Delivery Fill? the playbook and the concept?) and what "rather than agreement" means are said nowhere in the file. Proposed: question for the reviewer — say in plain words what meets and what "agreement" would be; or cut the sentence if §3.5's five facts already hold it.

**FINDING-523.** rule 8; resting on the reader. `docs/models/tiers.md` §3.4, *The Delivery Pin and the talk* (line 105): "The Delivery Pin follows the talk." "the talk" is not said in plain words here or in the title (103); 107 "leaves the registry lying" names a registry the file has not introduced. Proposed: fix: "The Delivery Pin follows the talk, the documents the tiers exchange: no tier's agent reads a tier above it, so every delivery is a document, and its Delivery Pin moves with it."; name the registry once, "the Run Repo's registry of what it holds".

**FINDING-524.** rule 9; checked. `docs/models/tiers.md` §1, *The tiers, drawn* (line 24): "harvest: a run's surprises" — "a run" where a Run Repo is meant; a lowercase word is English only. Also 81 "both input to Framing", one capitalised word, neither English nor a two-word Name (the concept writes "framing", `concept/03-cbc-framing.md`); 62 "a container copy", the Container Group's copy by a bare word; 26 the tier label "runs": 3 more. Proposed: fix: "a Run Repo's surprises" (the drawing has room), "input to framing", "a Container Group copy"; the tier label stays as the drawing's own word.

**FINDING-525.** rule 9; uncertain. `docs/models/tiers.md` §2.3, *Run Repos* (line 62): "consumed what a Concept Repo Made Usable and a container copy," — the Name Made Usable (glossary: "what a stated body becomes in the delivery", a noun) used as a verb in the past tense; 48 and 99 use it as a noun ("what is Made Usable"). The brief excepts the lowercase verb "made usable". Proposed: question — "consumed a Concept Repo's Made Usable and a container copy", or the lowercase verb, "what a Concept Repo made usable".

**FINDING-526.** rule 7; resting on the reader. `docs/models/tiers.md` §3.3, *Upward harvest* (line 96): "Up is harvest, through records. Learning moves up only through records:" The second sentence repeats the first, adding "only". Proposed: fix: "Up is harvest, and only through records: the tier above reads a Run Repo's records, read-only, and the Run Repo sends nothing."

**FINDING-527.** rule 5; resting on the reader. `docs/models/tiers.md` §3.4 (line 107): "leaves the registry lying" — a registry that lies, for one that is wrong. Also 3 "earns machinery", 61 "where a concept meets reality" (both near dead, counted only): 2 more. Proposed: fix: "leaves the registry wrong about what the Run Repo holds"; leave the two.

**FINDING-528.** rule 3; resting on the reader. `docs/models/tiers.md` §4.1, *Where a lesson lands* (lines 140-143): "About how to work → the tier above, which today is the Concept Repo that holds the method. About what is true of a concept → that concept's repo, as a Record Harvest. About this particular attempt → the Run Repo's own records, and nowhere else unless harvested." Three cases in one paragraph, joined by arrows. Proposed: fix: a list of three; or decline: the arrows label the three already.

**FINDING-529.** rule 8; resting on the reader. `docs/models/tiers.md` §4.2, *The dependency rule* (line 149): "today its method, is tier-two work, and not a Run Repo." The tiers carry no numbers in the text; the drawing names them "(no repo)", "concepts", "runs", and §2.1 says "the empty top tier". Proposed: fix: "is the concepts tier's work, and not a Run Repo's".

##### `concept/00-cbc.md`

**FINDING-530.** rule 5; resting on the reader. `concept/00-cbc.md`, *The shape of the work* (line 81): "The work has two movements, each with its own chapter:" — "movements", a symphony's word, for the work's two parts; also `concept/03-cbc-framing.md` 3 "The first movement of the work" and `concept/04-cbc-slice.md` 3 "The second movement of the work". No skill or delivered text uses the word (grep). Proposed: fix: "two parts" / "The first part of the work" / "The second part of the work"; editorial, no meaning moves ("phase" is taken by the slice's four phases).

**FINDING-531.** rule 5; resting on the reader. `concept/00-cbc.md`, *How it rots* (line 124): "## How it rots" — and under it four failure modes named by figures: "**Guarantee erosion by feature.**" (128), "**The escape hatch.**" (130), "**Testing theater.**" (132), "**The theory swamp.**" (134; also `concept/01-layered-system.md` 49). Three of the four are the shipped `cbc-slice` skill's working words (`delivery/method/.claude/skills/cbc-slice/SKILL.md` 114 and 225; `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` 208-215; `delivery/method/.claude/shapes/slice-record.md` 41), so a rename runs the rename grep into deliveries, and CBC Runs' records already carry them. Proposed: decline for the four labels, naming them the method's words; fix the title: "## How it fails" (editorial; no meaning moves). Question for the reviewer.

**FINDING-532.** rule 5; resting on the reader. `concept/00-cbc.md`, *The two components and their joint* (line 60): "The discipline has exactly two components, and it lives in their joint:" — "joint", the carpenter's, for the pair's combination; also 58 (the title) and 73 "The joint:"; line 77 says it plain, "The thing being defined here is the pair." Elsewhere in the file, counted only: 15 "bolted on afterwards", 37 "feature-thin", 54 "Its closest kin in kind", 100 "covers a region and stops", 117-118 "Rigor is *spent*, not applied: the budget goes to": 5 more. Proposed: fix: "the pair" for "joint" at 58, 60, 73 (editorial; line 77 equates them, so no meaning moves); the five: decline as dead, or one word each.

**FINDING-533.** rule 2; checked. `concept/00-cbc.md`, *The two components and their joint* (lines 73-75): "The joint: the inversion without the layers has nowhere to stand — a never-event is only meaningful relative to a described world; asked in a vacuum it produces either slogans or endless theorizing." Three ideas, a dash and a semicolon. Also 47-49 ("The discipline cannot: its unit is ..., and it is violated by ... even when ..."), 104-107: 2 more. Proposed: fix: "The inversion without the layers has nowhere to stand. A never-event is only meaningful relative to a described world. Asked in a vacuum, it produces slogans or endless theorizing." Editorial.

**FINDING-534.** rule 3; checked. `concept/00-cbc.md`, *Where it comes from* (lines 92-98): "Bounded contexts (domain-driven design) built the same ownership walls against language drift; SLOs (site reliability engineering) made promises explicit and falsifiable; threat modeling already thinks in never-events first; design-before-code culture found that the cheapest place to catch a flaw is a document; the academic correctness-by-construction lineage owns "errors prevented by structure, not found by search."" Five lineages in one sentence with semicolons; 104 then counts them, "five practices". 100-103 chain four of them again; 62-66 chain the five nested layers in one sentence: 2 more. Proposed: fix: a list of five at 92-98 and a list at 100-103, one line each; editorial.

**FINDING-535.** rule 1; resting on the reader. `concept/00-cbc.md`, *The inversion* (lines 14-15): "Most software is designed by asking *"what should it do?"* and listing features." The section's point, that this discipline asks "what must never happen?" first, arrives at line 18, after the contrast. Proposed: fix: open with "This discipline asks *"what must never happen?"* first." and let the contrast follow; or decline: the title carries it. Editorial.

##### `concept/01-layered-system.md`

**FINDING-536.** rule 5; resting on the reader. `concept/01-layered-system.md`, *LAYER-1-ENVIRONMENT* (line 26): "not vibes ("networks are unreliable")." — slang for impressions; also `concept/03-cbc-framing.md` 38 "attackable facts, not vibes". In this file, counted: 5 "each layer manufactures the precondition" (also `concept/03-cbc-framing.md` 13, `concept/04-cbc-slice.md` 41), 4 "five nested boxes" (also 88), 46 "gets checked at the door" (also `concept/02-guarantees-and-walls.md` 55, 61), 73 "fits in one head", 81 "the signature failure", 83 "the between-space", 83 "emergent wrongness": 7 more, most near dead. Proposed: fix: "not generalities" for "vibes" (both places); "produces" for "manufactures" (three places); "the space between the areas" for "the between-space"; the rest decline. Editorial; no meaning moves.

**FINDING-537.** rule 10; uncertain. `concept/01-layered-system.md` (line 21): "## LAYER-1-ENVIRONMENT — The environment" — a gloss after a dash, at 21, 37, 53, 64, 75; and `concept/02-guarantees-and-walls.md` 82 "## The stance underneath: prevented, not detected", a gloss after a colon. Rule 10 names numbered sections; the chapters' sections are unnumbered and LAYER-n is the System Layer's label. No Fact Reference outside the chapters names these headings. Proposed: question — does rule 10 reach the chapters' headings? If yes: "## LAYER-1-ENVIRONMENT" alone, the gloss opening the body, and "## The stance underneath"; editorial.

##### `concept/02-guarantees-and-walls.md`

**FINDING-538.** rule 5; checked. `concept/02-guarantees-and-walls.md`, *The guarantee inventory* (line 34): "the promise is scope creep wearing a safety costume." A costume worn: the figure CBC Run 3's retrospective named to drop (`docs/conventions/writing/` §2, *Why each rule*, rule 5); already an idea under TODO.md's "Rewrite the method's texts plain" (line 543). In this file, counted: 13 "Falsifiable is the load-bearing word", 30 "The promise's negation space", 37 "that is where the rigor budget goes" (also `concept/00-cbc.md` 118): 3 more. Proposed: fix: "one with no relation to the promise is scope creep presented as safety." Editorial; no meaning moves; strike the idea from the TODO item when done. The three: "the word that matters" for load-bearing; decline "negation space" and "rigor budget" as defined by their sentences, or question.

**FINDING-539.** rule 3; checked. `concept/02-guarantees-and-walls.md`, *The ownership map* (lines 53-57): "the store's refusal binds every code path ever written, including future ones; a type error binds everything that compiles; a single checked entry path binds everything that goes through the door; a runtime check binds only the paths that reach it; review and hope bind no one." Five parts, one per wall of the ranking at 44-50, chained with semicolons in one sentence. Proposed: fix: a list of five in the ranking's order, or each line folded into the ranking ("→ type system, binds everything that compiles"); editorial.

**FINDING-540.** rule 2; resting on the reader. `concept/02-guarantees-and-walls.md`, *The ownership map* (lines 65-68): "And the store refuses by withholding as well as by checking: an identity that holds no right to an operation is refused it on every path that uses that identity — the strongest wall for an operation that must never happen." Three ideas: two ways to refuse; what withholding does; its rank. Also 61-63 ("So the described adversary says who ... — trusted, or defended against — and each wall is assigned against that answer."), 78-80: 2 more. Proposed: fix: "The store refuses by withholding as well as by checking. An identity that holds no right to an operation is refused it on every path that uses that identity. That is the strongest wall for an operation that must never happen." Editorial.

##### `concept/03-cbc-framing.md`

**FINDING-541.** rule 1; resting on the reader. `concept/03-cbc-framing.md`, *The derivation order* (lines 19-20): "The layered system presents outside-in: environment first, then the system, then its interior." The point, "It starts from the promise", is the third sentence (20-21). Proposed: fix: "Framing starts from the promise, because the promise is the filter every other question needs. The layered system presents outside-in: environment first, then the system, then its interior. Framing does **not** derive in that order." Editorial.

**FINDING-542.** rule 2; resting on the reader. `concept/03-cbc-framing.md`, *The derivation order* (lines 25-27): "Candidate promises that are really features in disguise get rejected; a second genuine purpose means the intent is overloaded, and the choice is forced." Three ideas. Also 27-28 ("This is the hardest step and everything else is downstream of it."), 59-61, 70-72: 3 more. Proposed: fix: "A candidate promise that is really a feature is rejected. A second genuine purpose means the intent is overloaded, and one must be chosen." Editorial.

**FINDING-543.** rule 6; uncertain. `concept/03-cbc-framing.md`, *The derivation order* (line 35): "**Take the census of enemies.**" — "enemies" (also 41 "Each enemy fact", 59 "The enemy census") where `concept/00-cbc.md` and `concept/02-guarantees-and-walls.md` say "adversary" and "adversity", and this chapter says "actor" (36): two words for one thing, or two things. "enemy" is the shipped `cbc-framing` skill's word, 16 uses across five of its and `cbc-slice`'s files. Also 42 "never the cure", paired with the kill. Proposed: question — is "enemy" the concept's own word beside "adversary" (not a finding), or one name reworded (rule 6)? A change reaches the skills; "cure" stays with the kill.

##### `concept/04-cbc-slice.md`

**FINDING-544.** rule 2; checked. `concept/04-cbc-slice.md`, *Why the invariant is the unit* (lines 13-16): "Cutting by invariant keeps the derivation direction intact all the way into code — every unit of work is a guarantee becoming enforceable, and the feature surface grows only as a side effect of guarantees needing somewhere to live." Three ideas, a dash and "and". Also 27-29, 53-55, 59-61: 3 more. Proposed: fix: "Cutting by invariant keeps the derivation direction intact all the way into code. Every unit of work is a guarantee becoming enforceable. The feature surface grows only as a side effect, where a guarantee needs somewhere to live." Editorial.

**FINDING-545.** rule 1; resting on the reader. `concept/04-cbc-slice.md`, *Why the invariant is the unit* (lines 12-13): "Cutting work by feature reproduces the inversion the discipline exists to avoid: features first, correctness later." The answer to the title is the second sentence. Proposed: fix: swap the two sentences; editorial.

#### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

**FINDING-546.** rule 9; checked. `ARCHITECTURE.md` §3, *What must stay true* (line 193-194): "a rule is held by a line that travels with a file, a standing comment, a procedure, the Output Shape of the tree, or a check at commit review". A lowercase word is English; the tree's shape is English (the directory layout), and the table's Held-by cells say "the tree". The Name was put where English was meant. Proposed: fix: "the shape of the tree" or "the layout of the tree".

**FINDING-547.** rule 9; checked. `ARCHITECTURE.md` Overview (line 26-27): "under the models in `docs/models/`". The thing meant is the Idea Models, written by a word that is not the Name; also §4 line 233 "the models (§1.3)". 2 lines. Proposed: fix: "the Idea Models" in both.

**FINDING-548.** rule 9; checked. `ARCHITECTURE.md` Overview (line 30-31): "what it learned changes our masters". Master Copy is the Name; "masters" is not. Also line 45 (the diagram's "masters"), `README.md` line 20 "the masters made from them", `TODO.md` line 1096 "landed in the masters". 4 lines. Proposed: fix: "our Master Copies" in each; the diagram's box has room.

**FINDING-549.** rule 9; checked. `ARCHITECTURE.md` §1.3, *The Idea Models — `docs/models/`* (line 120-121): "the agent, the tiers, and idea to output". The glossary names a particular Idea Model "the Agent Model, the Tiers Model, the Idea-to-Output Model". Also `TODO.md` line 637 "three Idea Models exist: agent, tiers, idea-to-output" and line 674 "Idea-to-output has an Idea Model come from". 3 lines. Proposed: fix: write the three Names.

**FINDING-550.** rule 9; checked. `ARCHITECTURE.md` §2.3, *The Container Group — `delivery/container/`* (line 150-151): "a Work Approach on trial". The Name is Approach on Trial. Also `PLAN.md` line 314-315 "it is the Work Approach on trial `.claude/approaches-on-trial/refinement.md`". 2 lines. Proposed: fix: "an Approach on Trial" / "the Approach on Trial".

**FINDING-551.** rule 9; checked. `ARCHITECTURE.md` §2.5, *The CBC Runs* (line 186-187): "What each side holds for it is the exchange's *What this is made usable as*." The glossary's header says a convention is named by its path in backticks or by its Name, never by the bare word; line 54 of the same file writes "the Exchange Convention's". 1 line. Proposed: fix: "the Exchange Convention's".

**FINDING-552.** rule 9; checked. `ARCHITECTURE.md` Overview diagram (line 36): "a run"; §4 Codemap (line 236): "what a run is born into (§2.3)". "the run" for a CBC Run is the rule's own example. Also line 143 "A run on another stack", 234 "withheld from runs", 240 "how a run is seeded", 239 "a newborn's own files" (Newborn Run), 237 "their shapes" (Output Shapes). 7 lines. Proposed: fix: write the Names; the codemap's description column holds "what a CBC Run is born into (§2.3)".

**FINDING-553.** rule 6; checked. `ARCHITECTURE.md` §3, *What must stay true* (line 200): "Every execution states the concept version it derives from". "execution" is in no glossary entry and defined nowhere living; here it means a derived skill (its Held-by cell says "its Foundation Line, which travels with every copy"). `README.md` line 47 "Graduating an execution to its own Concept Repo" uses the same word for a Run Repo. Outside these two lines only `docs/models/tiers.md` line 24's diagram still carries it. 2 lines. Proposed: fix: say the thing in each place ("Every skill and Output Shape a CBC Run receives states…"; "Graduating a CBC Run to…"); question: which thing was an execution?

**FINDING-554.** rule 2; resting on the reader. `ARCHITECTURE.md` Overview (line 29-31): "A CBC Run is born from that delivery, takes newer copies at each Delivery Pin, and is read back here; what it learned changes our masters (§2, *The delivery and the CBC Runs*)." Four ideas chained with commas and a semicolon. Also lines 52-55 (two pointers joined by a semicolon), §1.1 lines 75-77, §1.2 lines 89-91, §2 lines 127-129, §2.5 lines 181-186 (four Fact References in one sentence). 6 places. Proposed: fix: split at each semicolon; or decline, as the overview's one-paragraph summary.

**FINDING-555.** rule 8; resting on the reader. `ARCHITECTURE.md` §2, *The delivery and the CBC Runs* (line 128-129): "the chapters carry none". None of what is not said; the reader has to know that a Canonical Description normally lists what derives from it. Also header comment line 8 "owning the pairing", before §1 says what the pairing is. 2 lines. Proposed: fix: "the chapters carry no such list"; "the pairing of stated and made usable".

**FINDING-556.** rule 5; uncertain. `ARCHITECTURE.md` §1, *What is stated here* (line 62-63): "the pairing is the spine of this repo". A figure for what the repo is built around. Proposed: fix: "the pairing is what this repo is built around"; or decline as a dead metaphor.

**FINDING-557.** rule 2; checked. `README.md` opening (line 3-5): "One canonical home for a single concept: **correctness by construction** — the design principle that correctness is built into the structure of a thing rather than tested in afterwards." Each sentence of the paragraph holds three or four ideas inside dashes and parentheses: lines 5-9 (the concept, its rationale and log, what is Made Usable, the pinning), 9-12 (the Container Group, three ADRs, one upstream), 15-20 (the tier, two Fact References, what comes back and to what). 4 sentences. Proposed: fix: one idea per sentence.

**FINDING-558.** rule 3; checked. `README.md` opening (line 3-22): one paragraph of 20 lines carries seven parts: what the concept is, what the repo holds, the Container Group, the Concept Deliverer, documents only, the tier, why it exists. A list would show the count. Proposed: fix: a labelled line per part, the first sentence kept as the lead.

**FINDING-559.** rule 7; resting on the reader. `README.md` opening (line 17-18): "CBC Runs happen in other repos pinned to a concept version". Said at line 12-13 ("each CBC Run is born from what this repo ships, and is read back from here") and again in Out of scope, line 38-39 ("CBC Runs happen in their own repos, pinned to a concept version"). 3 places. Proposed: fix: say it once, in the opening, and let Out of scope point at it.

**FINDING-560.** rule 8; checked. `README.md` Out of scope (line 43): "anything general waits on three". Three what is not said; the Tiers Model's three-repos rule is the reader's to know. Also line 49-50 "the two directories named in the birth briefing": no path, and a reader from outside, whom the header comment names, cannot find the briefing. 2 lines. Proposed: fix: "waits on three repos"; name where the birth briefing is, or drop the bullet.

**FINDING-561.** rule 9; uncertain. `README.md` opening (line 7-8): "what is Made Usable from it". The Name written as a verb with capitals; also line 31 "what this repo Made Usable", and `ARCHITECTURE.md` line 62 "that is it *made usable*", italics marking the phrase. The brief allows "made usable" as a verb in lowercase. 3 lines. Proposed: question: is "Made Usable" here the Name (a noun, "the Made Usable") or the verb? If the verb, lowercase and no italics.

**FINDING-562.** rule 9; uncertain. `README.md` Out of scope (line 41-42): "held for CBC Runs and changed by what runs live". If "runs" means the CBC Runs, the Name is lowercase; if it is a verb, the clause has no subject. Proposed: fix: "changed by what the CBC Runs live through".

**FINDING-563.** rule 6; uncertain. `README.md` Project records (line 66): "[project-recording §1](docs/conventions/project-recording/README.md)". A pointer to a section with no title and the bare name; the table above links whole files. Proposed: fix: "(`docs/conventions/project-recording/` §1, *The records at a glance*)" as a Fact Reference, kept as a link if the README wants links; question: does the README's link form stand outside the Fact Reference form?

**FINDING-564.** rule 5; resting on the reader. `README.md` header comment (line 71-72): "projection follows truth". A slogan; `TODO.md` line 1103 "the projection law's deeper lifecycle" builds on it, and no living text says what the law is. 2 lines. Proposed: fix: "a section arrives when what it says is true"; the TODO item says in plain words what the projection law is.

**FINDING-565.** rule 9; checked. `CHANGELOG.md` [Unreleased], Added (line 37): "from run 3's records". CBC Run 3. Also line 35-36 "the shapes their gates read" (Output Shapes), line 40 "for a Spring and PostgreSQL run, with the templates a run fills" (CBC Run; Skill Templates), line 55-56 "corrected from the runs", line 67-68 "a run's copy needs … which the run's own rule gives". 5 lines. Proposed: fix: write the Names; an unreleased entry is living.

**FINDING-566.** rule 9; resting on the reader. `CHANGELOG.md` [Unreleased], Changed (line 45): "harvested from never-oversold". A CBC Run is named by its number (glossary, CBC Run; `ARCHITECTURE.md` §2.5 "We call a CBC Run by its ordinal"). Also line 61 "From never-oversold's retrospective"; `TODO.md` lines 841, 859, 874 "(…, never-oversold)" and 938 "the handbook and never-oversold". 6 lines. Proposed: fix: "CBC Run 3", its own name once in parentheses where the stranger needs it.

**FINDING-567.** rule 2; resting on the reader. `CHANGELOG.md` [Unreleased], Added (line 29-33): "**The method**, derived from concept v1: `cbc-framing` — an idea worked into one falsifiable promise, a layered system definition and a slice registry — and `cbc-slice` — one invariant carried through specify, plan, build and document until a test that creates its adversity shows it holds." Paired dashes nest two skills' descriptions in one sentence. Also Changed lines 47-51 ("A new paragraph says who each wall leaves unbound — whoever can remove it — so …, and …"), Removed lines 66-69, and the intro lines 3-5. 4 places. Proposed: fix: one skill per sentence, the parts labelled; or decline, since the entry is released at v2 with these words.

**FINDING-568.** rule 2; resting on the reader. `CHANGELOG.md` [v1] (line 78-80): "Imported from the archive (system-design-method/birth-materials/concept/ @ fe0075d) unchanged in substance; the archive copy is now a historical snapshot." A released entry keeps its words. Proposed: decline: history.

**FINDING-569.** rule 5; resting on the reader. `CHANGELOG.md` header comment (line 11-12): "editorial fixes ride with the next version". A figure. Proposed: fix: "editorial fixes go in the next version"; or decline as dead.

**FINDING-570.** rule 9; checked. `PLAN.md` The Plan Step Form (line 34): "Goal: <one sentence: what is true when this step is done>". "a step" for a Plan Step is the rule's own example; the prose around the form says Plan Step. Also line 35 "the stage the step is in" and line 38 "this step's own items". 3 lines. Proposed: fix: "this Plan Step" in the three placeholders.

**FINDING-571.** rule 9; uncertain. `PLAN.md` Step: Birth CBC Run 6 (line 155-156): "so this is stage 1's light read". The glossary spells a Skill Stage "`cbc-slice`'s Stage 3" and says an Approach Stage is "numbered the same way"; the rule says a label inside its owner keeps its case. Also line 166 "`auto-run` stage 4", lines 205-206 "Stage 1 is answered by CBC Run 5's reading; stage 3 is settled; the Run Briefing is stage 2's" (both cases in one sentence), line 400 "stage 2"; `TODO.md` lines 200, 237, 524. `auto-run.md` itself writes "stage 1's" (line 35) and "Stage 4's" (line 86); `approach-evaluation.md` "stage 6" (line 109) and "Stage 3" (line 132). 8 lines here. Proposed: question: does an Approach Stage keep the capital as a Skill Stage does? Then one case everywhere, the approaches included; at least lines 205-206 take one case.

**FINDING-572.** rule 9; checked. `PLAN.md` Step: Birth CBC Run 6, Notes (line 205-206): "Stage 1 is answered by CBC Run 5's reading". Run Reading. Also line 289-290 "No note goes to CBC Run 5" (Delivery Note), and lines 157 and 173 "CBC Run 6's intent" for what the Goal (line 136) calls its Run Briefing. 4 lines. Proposed: fix: "CBC Run 5's Run Reading"; "No Delivery Note goes"; "CBC Run 6's Run Briefing".

**FINDING-573.** rule 3; resting on the reader. `PLAN.md` The Plan Step Form, At the close (line 87-89): "Every link and path in the records resolves; every ADR a record cites exists; each pair of copies agrees, such as the worked example in `cbc-framing` and in `cbc-slice`." Three checks under one tick, joined by semicolons; the same item at lines 180-182, 262-264 and 361-363. 4 places. Proposed: fix: three items; or decline, since one tick is meant to cover the three.

**FINDING-574.** rule 3; checked. `PLAN.md` Step: Refine this repo, Notes (line 404-407): "The reviewer signs: the Finding Kinds, their Refinement Rounds, the Refinement Layers and the rules, before Refinement Round 1; each finding's ending; every commit, at its boundary; each ending of the Work Approach's evaluation; main taking the branch." Five signatures chained by semicolons. Proposed: fix: a list of five.

**FINDING-575.** rule 2; resting on the reader. `PLAN.md` The Plan Step Form (line 26-27): "A Change Set inside it is a commit plan, and a small item needs no Plan Step, nor does a delivery alone." Two unrelated ideas joined by "and". Also lines 108-110 ("it removes the Plan Step from this file and adds the devlog entry, which names the Plan Step, what diverged from the plan, and the commit that holds the ticked gate"), lines 118-120 ("To resume, its branch is fast-forwarded to main, it restarts at that stage, and any stage whose input the other Plan Step changed runs again"), Refine Notes lines 384-390 (stage 1 of the list). 4 places. Proposed: fix: split each.

**FINDING-576.** rule 5; uncertain. `PLAN.md` The Plan Step Form, At the close (line 93): "New and changed text reads to `.claude/rules/writing.md`." "reads to" is not a plain phrase for meeting a rule; also lines 186, 268, 367; and line 128-129 "not a Plan Step cutting a corner". 5 lines. Proposed: fix: "meets `.claude/rules/writing.md`"; "not a Plan Step skipping it".

**FINDING-577.** rule 8; resting on the reader. `PLAN.md` Step: Take CBC Run 5's lessons (line 251-252): "fixed in place: 7 plans, and 12 unused fixes with E1 a use note". What E1 is, and what a use note is, the plan's reader cannot tell. Proposed: fix: say what E1 is, or drop the detail and leave it to the devlog entry.

**FINDING-578.** rule 9; checked. `TODO.md` Next (line 130-131): "each delegation leaves one line: the kind of work, the Idea Model, the effort, whether it paid." The thing meant is the agent's model (Opus, Sonnet): the Context says "none given a model" (line 123) and the Ideas "one default model for every subagent" (line 134). The Name was put where English was meant. Proposed: fix: "the model".

**FINDING-579.** rule 9; checked. `TODO.md` Next (line 604): "so this is its own Run Reading, not a tidy-up". Sorting `docs/baselines/` is a careful read of its own, not a Run Reading (the reading of a CBC Run). The Name was put where English was meant. Proposed: fix: "so this is a piece of work of its own, read with care, not a tidy-up".

**FINDING-580.** rule 9; checked. `TODO.md` Next (line 83-84): "Run 4 tried each Real question's options on `try/` branches". CBC Run 4. Also Later line 785-786 "runs run 5's birth", line 792 "for runs pinning a version", line 624 "the next newborn" (Newborn Run), line 417 "its step branches" (Plan Step), line 950 "They are spring-postgres" (the Stack Group), line 1093 "the harvest discipline" (Record Harvest), lines 259, 358, 367 "a set moved", "a set's commits", "a set is open" (Change Set), line 547 "Refinement Round 2's lessons and layout" (the Lessons and Layout Finding Kinds, which lines 261, 555 and 688 write with their case). 11 lines. Proposed: fix: write the Names.

**FINDING-581.** rule 9; checked. `TODO.md` Next (line 518): "a `paths:` rule loads only when a file is touched". The glossary names the kind a Paths Rule; backticks mark the key, not the Name. Proposed: fix: "a Paths Rule".

**FINDING-582.** rule 6; checked. `TODO.md` Next (line 409-410): "It left twelve lines under To the Concept Deliverer." The heading in a CBC Run's backlog is *To the deliverer* (`delivery/container/TODO.md` line 45; glossary, Run Ask). A reference reworded points elsewhere. Proposed: fix: "under *To the deliverer*".

**FINDING-583.** rule 6; checked. `TODO.md` Next (line 422): "'a fourth run deriving `.gitignore` by hand'" quotes a trigger that now reads "a fourth CBC Run deriving `.gitignore` by hand" (line 960-961). Proposed: fix: requote.

**FINDING-584.** rule 6; checked. `TODO.md` Next (line 548-554): "the refinement's DECISION-7 and 8: FINDING-223, the harness reference's "passes"; 224, the "lived" markers; 227, …; 228, …; and 206, …". Labels shortened to bare numbers after the first. 5 labels. Proposed: fix: DECISION-7 and DECISION-8; FINDING-224, FINDING-227, FINDING-228, FINDING-206.

**FINDING-585.** rule 6; checked. `TODO.md` Next (line 561-562): "(2026-10-17, from Step 10's gate)"; line 566 "Step 10's gate held it until ADR-0057". A number local to this repo's former plan with no owner; line 778 writes it right, "from PLAN's Step N". 2 lines. Proposed: fix: "PLAN's Step 10".

**FINDING-586.** rule 6; checked. `TODO.md` Later (line 898-899): "§2, *What a Output Shape is not*". The heading is *What an Output Shape is not* (`docs/conventions/shapes/README.md` line 108); line 204 has it right. Proposed: fix: "an".

**FINDING-587.** rule 6; resting on the reader. `TODO.md` Later (line 945): "Decide whether cbc-bootstrap points at the Spring hygiene parts". The skill is `cbc-bootstrap` in backticks everywhere else (line 956); also line 960 "cbc-bootstrap's hygiene step", Next line 423 "cbc-bootstrap's hygiene", line 1047 "both cbc-slice files", line 413 "the retrospective skill's form". 5 lines. Proposed: fix: backticks.

**FINDING-588.** rule 6; resting on the reader. `TODO.md` Next (line 299): "the `claude-md-management` part, and §14." A Fact Reference with no title. Also lines 587, 926, 1018, 1029 "(…, the user)" where every other item writes "the reviewer" for the same person. 5 lines. Proposed: fix: "§14, *A sweep, and what looking back is*"; "the reviewer".

**FINDING-589.** rule 3; checked. `TODO.md` Next (line 723-729): "the scenarios: a fact changed at its home; a section renamed, renumbered or retitled; a file renamed; a fact moved to a new home, a placed Approach on Trial among them; a foundation changed; …; a line with no Fact Reference." Eleven scenarios chained by semicolons in one bullet. Proposed: fix: eleven lines.

**FINDING-590.** rule 3; checked. `TODO.md` Later (line 966-971): "An opening ordered by weight let them plan their commit split from four lines; "we are not asking you to write the convention" removed a pressure we did not have to name; all four additions were usable with no follow-up question." The three candidate rules the item is to weigh, chained. Also lines 985-986, two Ideas with no list marks: "Ideas: the overtaken Run Reading sends a Delivery Note: read, asks open. the next read goes back to the last Delivery Note's Read-Through Commit." 2 places. Proposed: fix: a list each.

**FINDING-591.** rule 4; checked. `TODO.md` Next (line 769-770): "Of 97 uses in living text, only some say." The count exists. Proposed: fix: the number.

**FINDING-592.** rule 5; uncertain. `TODO.md` Next (line 495): "what is read most first: the front door, our skills and rules, what ships". The brief lists "front door" as a metaphor; it is also the records table's own phrase for README (`CLAUDE.md` line 28, both Convention Seats; `docs/conventions/project-recording/README.md` lines 181, 201, 492, 499). Proposed: question: is "front door" the convention's word for README, and so stays; or does it go here and at its home, "the README"?

**FINDING-593.** rule 5; uncertain. `TODO.md` Later (line 1028): "Could a project need its own mould of a shipped skill?" "mould" is a figure for a variant. Also Next line 90 "the better way on a `try/` branch, compared, the loser kept" (is the worse try kept?), and `temp/README.md` line 7 "a Run Briefing being molded before it goes to a CBC Run". 3 lines. Proposed: fix: "its own variant"; say which try is kept and why; "being written".

**FINDING-594.** rule 8; resting on the reader. `TODO.md` Next (line 83-84): "each Real question's options". A `commit-plan` label used with no words saying what a Real question is. Also line 216-217 "a fifth kind of difference at the gate", 351-352 "ADR-0063's kinds now place either", 539-540 "the fenced collisions", 588-591 "walk-1-era method half … the stance bullets … Three ways", 564 "both skills run on this repo", 627 "teaches this fill", 929-930 "lived newborn text adopted on provenance, unaudited", 938 and 965 "the handbook", 951 "decision 5's beside-it rule", 1095-1097 "its flow-back split sure adoptions … a named promotion path", 1106-1107 "the safe-reservations node's projection model". 13 places. Proposed: fix: a plain phrase before each; or decline for items whose reader is the one who raised them.

**FINDING-595.** rule 9; uncertain. Conventions named by the bare hyphenated word. `TODO.md` line 245 "Facts-in-sync calls both a Canonical Description"; also 325 "Project-recording asks", 168 "agent-arrangement counts", 64 and 970-971 "the exchange manual", 1012-1013 "the arrangement's to say", 465 "the shapes manual", 452 "the shapes convention", 504 "the conventions manual"; `PLAN.md` line 300 "project-recording's list", lines 94, 188, 270, 369 "follows commit-messages"; `ARCHITECTURE.md` line 216 "project-recording's"; `README.md` line 66. The glossary's header says a convention is named by its path in backticks or by its Name, never by the bare word; `ARCHITECTURE.md` §1.2's list and the writing manual's "commit-messages' rule" write the hyphenated word. 16 lines. Proposed: question: does the hyphenated folder name count as the path? If not, each becomes the path in backticks or a Name, and "the exchange manual", "the arrangement" and "the shapes manual" go first.

**FINDING-596.** rule 10; resting on the reader. `TODO-CONVERSATION-MEMORY.md` §5 (line 274): "## 5. Run 4's reading: two moves from layer 6". A numbered section's title with a gloss after a colon; also §6 line 297 "## 6. The method's plain rewrite: `cbc-slice`'s opening". The titles are the items' words when added, and `TODO.md`'s See lines quote them (lines 436, 559). 2 titles. Proposed: question: are the section titles living text under rule 10, or the part's words? If living: "CBC Run 4's Run Reading" and "The method's plain rewrite", with the rename grep.

**FINDING-597.** rule 9; resting on the reader. `TODO-CONVERSATION-MEMORY.md` §5 (line 274): "Run 4's reading … layer 6" (CBC Run 4's Run Reading; Refinement Layer 6). Also §8 line 373 "Run 5's full-auto birth", §2 line 28 "an approach and a shape" (Work Approach, Output Shape), §3 line 98 "Layouts as shapes", §21 line 851 and §22 line 907 "fact references". 6 titles. Proposed: as FINDING-596, decided together.

**FINDING-598.** rule 7; checked. `devlog/README.md` (line 3-4): "One file per month, `<YYYY-MM>.md`, newest entries on top; a new month opens its own file." The second clause repeats the first. Proposed: fix: drop "a new month opens its own file".

**FINDING-599.** rule 2; checked. `devlog/README.md` (line 7-8): "2–5 minutes at the end of each session, and a TODO item's story when the item is added (`TODO.md`'s header)." A sentence with no verb joining when an entry is written to what else the devlog holds. Proposed: fix: "An entry takes 2 to 5 minutes at a session's end. A TODO item's story is written here when the item is added (`TODO.md`'s header)."

**FINDING-600.** rule 3; checked. `temp/README.md` (line 17-20): "what a draft said and why lives in the records, which the records map lists (…) — the devlog logs a draft made, passed, or deleted; decisions go to the ADRs; the backlog to TODO." Three homes chained after a dash. Proposed: fix: a list of three. The file is the Master Copy's twin (`delivery/container/temp/README.md`): check both.

**FINDING-601.** rule 7; resting on the reader. `temp/README.md` (line 17): "Not records. Nothing here is the record of anything:". The second sentence repeats the first. Proposed: fix: keep one.

**FINDING-602.** rule 9; checked. `temp/README.md` (line 8): "while the sets that fix it work through it". Change Sets. Proposed: fix: "the Change Sets that fix it".

**FINDING-603.** rule 6; checked. `docs/adr/README.md` header comment (line 34-35): "(docs/conventions/project-recording/ §3.4, How)". The heading is *How an ADR is written* (`docs/conventions/project-recording/README.md` line 287); the title was cut to the word the rule forbids as a title. Proposed: fix: "§3.4, How an ADR is written". The same form at the Master Copy, `delivery/container/docs/adr/README.md`, if it carries it.

#### Layer 5: our agent setup

**FINDING-604.** rule 2; resting on the reader. `CLAUDE.md`, opening paragraph (line 5): "Concept Deliverer: each CBC Run, a separate repository that builds a real". One idea per sentence; the sentence at lines 4–7 carries three: this repo is the Concept Deliverer, what a CBC Run is, and that a CBC Run is born from here and read back. 1 instance. Proposed: fix: "It is the Concept Deliverer. A CBC Run is a separate repository that builds a real system by the concept. Each is born from what this repo ships, and is read back from here."

**FINDING-605.** rule 3; resting on the reader. `CLAUDE.md`, *Records*, header comment (line 13): "once opened, and nothing else says when. Three things per row —". Parts get their own line or label, not dashes; lines 13–15 chain the three things a row holds and the exclusion in one sentence with two dashes and a colon. 1 instance. Proposed: decline if a header comment may stay terse; else fix: "Three things per row: the moment, what it holds, the path. Never the rule itself: what an ADR contains is inside the ADR."

**FINDING-606.** rule 5; checked. `CLAUDE.md`, *Records* table (line 28): "| Something became true the outside should see | The front door: what this is, how to use it | README.md |". Plain words, not metaphor; "front door" stands for the first page an outsider reads. The row summarizes `docs/conventions/project-recording/` §1 (lines 181, 201; §7 lines 492, 499 too), and `delivery/container/.claude/CLAUDE.md` line 51 carries the same words. 1 instance here. Proposed: question for the reviewer: fix the home first, project-recording §1 and §7 (Refinement Layer 2), then this row and the container's follow: "The first page: what this is, how to use it".

**FINDING-607.** rule 9; checked. `CLAUDE.local.md` (line 5): "- In a change set, stop at every commit's boundary the same way." A defined thing is written by its Name; Change Set is listed (`docs/glossary.md`, *The work*) and "change set" means it. Line 7, "In a change set it is an inserted commit.", is the second. 2 instances. Proposed: fix: "Change Set" in both, if the reviewer's private file is under the rule at all.

**FINDING-608.** rule 9; checked. `.claude/decisions.md`, header comment (line 3): "<!-- The working arrangement's decision log. Append-only, newest". Decisions Log is the Name for this very file (`docs/glossary.md`, *Kinds of text*: "ours is the same file here"); "decision log" is it in other words. 1 instance. Proposed: fix: "The working arrangement's Decisions Log."

**FINDING-609.** rule 2; resting on the reader. `.claude/decisions.md`, header comment (line 10): "Division of labor: the standing rule rides as a comment in the". Lines 10–12 hold three ideas in one sentence: where a standing rule is written, what this log keeps, that neither repeats the other. 1 instance. Proposed: fix: "Division of labor: a standing rule is written as a comment in the file it governs. This log keeps the why and the rejected options. Neither repeats the other."

**FINDING-610.** rule 5; resting on the reader. `.claude/decisions.md`, header comment (line 10): "the standing rule rides as a comment in the". "Rides" is a figure for "is written as". 1 instance here; the same figure is at `.claude/skills/exchange-deliver/SKILL.md` line 11 (FINDING-632). Proposed: fix: "is written as a comment in" (the fix in FINDING-609 does it).

**FINDING-611.** rule 3; checked. `.claude/rules/convention-manual.md`, *The sections, in this order*, item 2 (line 32): "— and the event that made it. Evidence; or intent marked *on". Lines 32–36 chain three kinds of need, evidence, intent on trial, adopted, with semicolons and dashes, so their count is hidden. Item 4 (lines 44–47: four cases of *The seats* chained with semicolons) and item 5 (lines 48–55: two rules on Fact References chained with a semicolon) do the same. 3 instances. Proposed: fix: each item's cases as a sub-list, as `foundation-check.md` *The check* step 1 does.

**FINDING-612.** rule 5; checked. `.claude/rules/convention-manual.md`, *The sections, in this order*, item 2 (line 36): "where it came from and what has been lived under it since. Never intent dressed as". "Dressed as" is a figure of the costume kind the rule names. 1 instance. Proposed: fix: "Never intent written as evidence".

**FINDING-613.** rule 5; checked. `.claude/rules/convention-manual.md`, heading (line 84): "## The list is the floor, not the ceiling". Floor and ceiling stand for "the least, not the most". 1 instance. Proposed: fix: "## The list is the least a manual holds", with the first sentence saying the point.

**FINDING-614.** rule 9; checked. `.claude/rules/exchange-reading.md`, *The sections, in this order*, item 1 (line 40): "read-through, and the span between." Read-Through Commit is the Name; "the previous read-through" is it in lowercase. 1 instance. Proposed: fix: "the previous Read-Through Commit".

**FINDING-615.** rule 5; resting on the reader. `.claude/rules/exchange-reading.md`, *The sections, in this order*, item 7 (line 58): "line each, written as they happen — this is where the form". "Where the form learns": a form does not learn; the writer changes it from these lines. 1 instance. Proposed: fix: "— these lines are what the form is changed from."

**FINDING-616.** rule 5; resting on the reader. `.claude/rules/foundation-check.md`, header comment (line 7): "§5, A disagreement; §3.3, The rename grep) fire at the commit, where they waited". "Where they waited to be remembered" is a figure for "which before had to be remembered". 1 instance. Proposed: fix: "fire at the commit; before, they had to be remembered."

**FINDING-617.** rule 6; checked. `.claude/rules/one-home.md`, *The rules*, rule 3 (line 30): "reads it in the owner's place. The map does this (`ARCHITECTURE.md` §1.2, *The conventions…*):". A Fact Reference's title is the heading it points at; the heading is "1.2 The conventions — `docs/conventions/`", and "The conventions…" is a cut. 1 instance. Proposed: question for the reviewer: the heading itself has a gloss after a dash (rule 10, Refinement Layer 4); when it is retitled, the rename grep fixes this line; until then, write the title whole.

**FINDING-618.** rule 2; resting on the reader. `.claude/rules/one-home.md`, header comment (line 12): "§2, Point and derive; §3.1, What a Fact Reference is; The Concept Deliverer's seat),". Lines 10–15 are one sentence carrying three ideas: what ours derives from, what the container's derives from, where the difference is said. Rule 5 at lines 39–42 ("A retelling with a Fact Reference is one; two copies that cannot be avoided are another: the worked example sits in…") chains three too. 2 instances. Proposed: fix: split at the semicolons into sentences.

**FINDING-619.** rule 2; checked. `.claude/rules/working-a-reading.md`, *The steps*, step 1 (line 25): "needed. The count undercounts: one item's set can run to twenty". Lines 25–29 are the rule's own *Before* example (`.claude/rules/writing.md`, *Before and after*, lines 70–72), still standing in the file it was taken from; the *After* (lines 76–78) is already written. Other chained sentences in the section: step 3 lines 42–44, step 4 lines 48–51, step 5 lines 56–59. 4 instances. Proposed: fix: put the *After* text in step 1, keeping the Fact Reference: "The count is of items, not of work. One item can take twenty commits. An item that edits a skill both Convention Seats hold is two commits: the Master Copy, then our own copy (…)."; split steps 3–5 the same way.

**FINDING-620.** rule 5; resting on the reader. `.claude/rules/working-a-reading.md`, *The steps*, step 2 (line 36): "list never asked: the options written down are not the space. When". "The space" (of options) is a figure. 1 instance. Proposed: fix: "the options written down are not all the options."

**FINDING-621.** rule 3; resting on the reader. `.claude/rules/working-a-reading.md`, *The steps*, step 9 (line 81): "line. A Delivery Note may go before the list closes, since one alone is". Step 9 (lines 76–86) holds six parts of the close, when it is closed, how the Delivery Note is written, an early Delivery Note, the lessons, the fast-forward, the deleting commit, as one paragraph with dashes and semicolons. 1 instance. Proposed: fix: a sub-list, one line per part.

**FINDING-622.** rule 3; checked. `.claude/rules/working-a-reading.md`, *Stages* (lines 103–104): "For a Run Reading's Plan Step, its Notes and its Now line: read / (`exchange-read`); decide and work (steps 1 to 8 here); note". Four stages chained with semicolons in one sentence. 1 instance. Proposed: fix: a four-line list, as `exchange-deliver` lists its Skill Stages.

**FINDING-623.** rule 3; resting on the reader. `.claude/rules/writing.md`, *The rules*, rule 9 (lines 47–48): "carries its owner and number, "working-a-reading rule 2", "the / walk's step 3"; a label inside its owner keeps its case, "Step 0";". Three sub-rules chained with semicolons in one sentence; rule 10 (lines 53–57) chains five properties of a title the same way. 2 instances; the manual's §2 rule 9 (lines 107–110) and rule 10 (lines 117–122) carry the same sentences, read in Refinement Layer 3. Proposed: question for the reviewer: decline as a rule's compressed lead, or fix as sub-lists, in the manual first.

**FINDING-624.** rule 2; resting on the reader. `.claude/skills/commit-messages/SKILL.md` and `delivery/container/.claude/skills/commit-messages/SKILL.md`, *The agent's own files* (line 103): "`CLAUDE.md` and `.claude/` are the working arrangement, and". Lines 103–104 carry three ideas: what the working arrangement is, that `COMMIT-PLAN.md` is committed with it, that none is a record. 1 instance, in both copies. Proposed: fix: "`CLAUDE.md` and `.claude/` are the working arrangement. `COMMIT-PLAN.md` is committed with them. None is a project record."

**FINDING-625.** rule 9; uncertain. Same line (103), both copies, and `.claude/decisions.md` line 3: "working arrangement" names the agent's files as one thing, and no Name lists it; `docs/models/tiers.md` line 33 and `README.md` line 40 use the same words. 3 instances in my files. Proposed: question for the reviewer: English (the agent-arrangement convention's subject, said in plain words), or a Name wanted; if English, decline.

**FINDING-626.** rule 9; resting on the reader. `.claude/skills/commit-plan/SKILL.md` and shipped, opening (line 9): "A **Change Set** is a body of work that needs more than one commit." No Markdown mark marks a Name; the bold marks Change Set on its first use. 1 instance, both copies; `.claude/skills/exchange-read/SKILL.md` lines 18–19 mark Delivery Pin and Read-Through Commit the same way (FINDING-639). Proposed: fix: drop the bold.

**FINDING-627.** rule 2; resting on the reader. `.claude/skills/commit-plan/SKILL.md` and shipped, §2 *The plan file* (line 53): "- Commit subjects follow commit-messages, and are counted against". Lines 53–56 chain three ideas: subjects follow commit-messages; counted when the plan is written; why. 1 instance, both copies. Proposed: fix: "Commit subjects follow commit-messages. They are counted against its limit when the plan is written, not when each commit lands. A subject planned too long lands too long, or is rewritten at its boundary with nothing in the plan saying why."

**FINDING-628.** rule 5; resting on the reader. `.claude/skills/commit-plan/SKILL.md` and shipped, §2 *The plan file* (lines 59–60): "- **The list may roll.** Commits near at hand are firm. Commits / past the decision horizon, whatever a not-yet-seen result must". "Roll" and "horizon" are figures; the text glosses horizon in the same line. §7 lines 168–169, "A provisional tail refined at its boundary", is the same figure's third word. 3 instances, both copies. Proposed: fix: "**The list may change past a point.** Commits near at hand are firm. Commits that a result not yet seen must shape are provisional and marked so…"; §7: "A provisional commit refined at its boundary is not this."

**FINDING-629.** rule 5; checked. `.claude/skills/commit-plan/SKILL.md` and shipped, §5 *Divergence* (line 142): "Refining a provisional commit travels the same road and is planned". "Travels the same road" stands for "follows the same four steps". 1 instance, both copies. Proposed: fix: "Refining a provisional commit follows the same four steps, and is planned refinement, not divergence."

**FINDING-630.** rule 2; checked. `delivery/container/.claude/skills/commit-plan/SKILL.md` only, §3 *How the commits are split* (line 95): "(`.claude/skills/commit-messages/SKILL.md`, *The agent's own files*): and a records commit planned to carry one has to be split". The shipped line joins a second idea to the sentence with ": and"; ours (line 95) ends the sentence and starts a new one. 1 instance. Proposed: fix: the shipped line as ours: "…*The agent's own files*). A records commit planned to carry one has to be split when it opens."

**FINDING-631.** rule 9; resting on the reader. `.claude/skills/commit-plan/SKILL.md` and shipped, §2 (line 53): "follow commit-messages". A convention is named by its path in backticks or its Name, never the bare word (`docs/glossary.md`, header comment); lines 148 ("The rule is commit-messages', and binds"), 159 ("follows commit-messages too") and 187 do the same. 4 instances, both copies. Proposed: fix in ours: `docs/conventions/commit-messages/` or "the commit-messages convention"; in the shipped copy, the skill's name in backticks, `commit-messages`.

**FINDING-632.** rule 5; resting on the reader. `.claude/skills/exchange-deliver/SKILL.md`, opening (line 11): "verdicts and the Read-Through Commit ride only when one did." "Ride" stands for "go with it". 1 instance. Proposed: fix: "go only when one did".

**FINDING-633.** rule 8; resting on the reader. `.claude/skills/exchange-deliver/SKILL.md`, *Stage 1* (line 17): "In `temp/note-to-<run>-<date>.md`, told not delivered." "Told" is the Tiers Model's channel word (`docs/models/tiers.md` §3.2, *The told channel*), used with no plain words; step 7 line 69, "The Delivery Note is told text", is the second. 2 instances. Proposed: fix: "told, not delivered: the CBC Run reads it as session input, not as a copy it keeps (`docs/models/tiers.md` §3.2, *The told channel*)."

**FINDING-634.** rule 2; checked. `.claude/skills/exchange-deliver/SKILL.md`, *Stage 1*, step 0 (lines 21–22): "empty, `exchange-read` steps 2–4 on it. The three things it reads are the / filter — the CBC Run's own building yields nothing and the extension". Lines 21–24 chain four ideas with a dash, a semicolon and "which": the three things are the filter; building yields nothing; a copy edited yields items; they take the next numbers and are worked first. Step 1 lines 42–45 and *A Delivery Note without files* lines 143–145 chain three each. 3 instances. Proposed: fix: one sentence per idea.

**FINDING-635.** rule 3; checked. `.claude/skills/exchange-deliver/SKILL.md`, *Stage 1*, step 3 (line 54): "the CBC Run owes now; never a description of our own practice, which". Lines 53–55 chain what a verdict is and two things it is never, with semicolons. 1 instance. Proposed: fix: "A verdict is the decision and what the CBC Run owes now. Never: a description of our own practice, which the CBC Run cannot check; "accepted" for something not decided." as two labelled lines.

**FINDING-636.** rule 5; checked. `.claude/skills/exchange-deliver/SKILL.md`, *Stage 1*, step 6 (line 64): "check from its own tree is a hedge it can never close. Where one". "A hedge it can never close" is a figure. 1 instance. Proposed: fix: "is a claim it can never check, so it stays open."

**FINDING-637.** rule 1; resting on the reader. `.claude/skills/exchange-deliver/SKILL.md`, *Stage 2*, step 2 (line 125): "root gets 700 there, which git does not show. The `chmod` is why." The paragraph (lines 123–125) explains `mktemp` and the copied mode first; its point, why the `chmod` is in the script, is its last three words. 1 instance. Proposed: fix: lead with "The `chmod` is there because `mktemp -d` makes the folder owner-only, and the copy in step 3 carries its mode: …".

**FINDING-638.** rule 9; resting on the reader. `.claude/skills/exchange-deliver/SKILL.md`, *Gates* (line 154): "- The CBC Run's `temp/` gained exactly the bundle and the Delivery Note, and". Delivery Staging is the Name for what is copied; "the bundle" is the directory's name, `bundle-H`, used as the thing. 1 instance. Proposed: fix: "gained exactly the Delivery Staging, `bundle-H`, and the Delivery Note"; or decline as the path's own word.

**FINDING-639.** rule 9; resting on the reader. `.claude/skills/exchange-read/SKILL.md`, §1 *How a CBC Run is read*, step 1 (line 18): "Its last delivery entry carries the **Delivery Pin** `P` — our commit its". Bold marks the Names Delivery Pin and Read-Through Commit (lines 18–19). 1 instance, two Names. Proposed: fix: drop the bold; `P` and `R` in backticks already stand out.

**FINDING-640.** rule 8; uncertain. `.claude/skills/exchange-read/SKILL.md`, §1, step 3 (line 44): "`<base>` is the CBC Run's receipt branch for `P` when it cut one;". "Receipt branch" is a label with no plain words, and no living text under `docs/` or `.claude/` says what one is; ADR-0016, 0018 and 0019 (closed) do. 1 instance. Proposed: fix: "the branch the CBC Run cut to receive the delivery at `P`, its receipt branch, when it cut one"; see Met in passing for the missing living home.

**FINDING-641.** rule 2; resting on the reader. `.claude/skills/exchange-read/SKILL.md`, §1, step 4 (line 66): "the next numbers. Otherwise write `temp/reading-<run>-<date>.md`,". Lines 66–69 chain where to write, to which form, what one line holds, and that nothing is decided, with colons and a dash; §3 lines 87–89 ("`exchange-deliver` does — and a read that sends no Delivery Note has not finished, because…") chain three. 2 instances. Proposed: fix: one sentence each.

**FINDING-642.** rule 5; checked. `.claude/skills/visual-comparison/SKILL.md` and shipped, opening (line 13): "The spine is requirements first, every candidate built, judged per". "The spine" stands for the method's fixed order. §4 lines 124–127, "**Using a dialect is not fighting it.** … are the fight", is a second figure, ADR-0027's own words, cited in *Decisions*. 2 instances, both copies. Proposed: fix: "The steps are: requirements first, …"; for §4, question for the reviewer, since the Decisions list quotes the phrase.

**FINDING-643.** rule 3; resting on the reader. `.claude/skills/visual-comparison/SKILL.md` and shipped, opening (lines 13–14): the same sentence chains four steps with commas; §4 bullet 4 lines 113–115 chain three things not run ("no non-picture candidate, requirements written after…, no verdict settled by looking") after a dash. 2 instances, both copies. Proposed: fix: list the four steps; label bullet 4's three or leave it.

**FINDING-644.** rule 8; checked. `delivery/container/.claude/skills/visual-comparison/SKILL.md` only, §4 *What the render has caught* (line 98): "Run Reading as an arrow into the other repo — asserting the opposite". The shipped reader holds `delivery/container/docs/glossary.md`, which lists no Run Reading, and no shipped text says what one is (the only other shipped use is `delivery/container/.claude/rules/shapes-lifecycle.md` line 93). 1 instance. Proposed: fix: in the shipped copy, "a read-only reading of this project by the Concept Deliverer"; or add Run Reading to the shipped glossary.

**FINDING-645.** rule 2; resting on the reader. `delivery/container/.claude/skills/visual-comparison/SKILL.md` only, §5 *What this does not do* (line 132): "its cases is the Concept Deliverer's provisional trial, which does not". Lines 131–133 chain what the Mermaid is, that it does not travel, and that this project decides its forms, with "which" and a semicolon. 1 instance. Proposed: fix: "The Mermaid in its cases is the Concept Deliverer's provisional trial. It does not travel. This project decides its own forms."

**FINDING-646.** rule 8; checked. `delivery/container/.claude/approaches-on-trial/approach-drafting.md` only, *Stages* §1 *Open*, step 3 (line 41): "   - its Approach Stages, in order;". The shipped glossary lists Skill Stage but no Approach Stage, and the shipped text gives no plain words; ours is covered by `docs/glossary.md`, *The work*. 1 instance. Proposed: fix: add Approach Stage to the shipped glossary, or write "its stages, in order".

**FINDING-647.** rule 9; checked. `.claude/approaches-on-trial/approach-drafting.md` and shipped, *Uses* (line 107): "*The deliverer, working a reading, 2026-10-01.* A draft in `temp/`". Names in lowercase where the thing is meant: "The deliverer" for Concept Deliverer (lines 107, 111, 117, 123), "Run 3" for CBC Run 3 (101), "a reading"/"readings" for Run Reading (107–108), "a rule" for Agent Rule (108–109), "the tiers model", "the exchange", "a model" for the Tiers Model, the Exchange Convention, an Idea Model (123–125), "This approach" for Approach on Trial (120). 12 instances. Proposed: question for the reviewer: are dated *Uses* notes history, which keeps its words, or living text? `refinement.md` §1 lists what history is and does not name them. If living: fix each Name. (FINDING-653, FINDING-657, FINDING-659 rest on the same answer.)

**FINDING-648.** rule 8; checked. `delivery/container/.claude/approaches-on-trial/approach-drafting.md` only, *Uses* (line 104): "built at the close. Both skills came out that way and were taken". "Taken here" means the Concept Deliverer, which a CBC Run's reader reads as its own repo; `approach-evaluation.md` *Seats* lines 80–81 say not to write "here". "The refinement" (112, 117–121), "the redesign" (111) and "the tiers model and the exchange" (124–125) are this repo's things with no plain words for that reader. 5 instances. Proposed: fix: "taken into the Concept Deliverer", and name each thing ("the Concept Deliverer's refinement of its own text"); or question: do shipped *Uses* notes travel at all?

**FINDING-649.** rule 8; resting on the reader. `.claude/approaches-on-trial/approach-evaluation.md`, *What it is for* (line 13): "(ADR-0056). The redesign of 2026-10-19 closed as three pieces, which". "The redesign" names an event with no plain words for what was redesigned (the conventions manual); the *Uses* note at line 139 repeats it, and `approach-drafting.md` line 111 does too. 3 instances. Proposed: fix: "The redesign of the conventions manual, on 2026-10-19, closed…".

**FINDING-650.** rule 2; resting on the reader. `.claude/approaches-on-trial/approach-evaluation.md`, *The stages of an Approach on Trial*, item 3 (line 24): "it meets what its Approach on Trial named would settle it, or dropped at". The nested clause must be held whole; *Uses* line 130 ("One use behind the approach, so every piece stayed on trial and stage 6 was the work: rewritten…") chains three. 2 instances. Proposed: fix: "a piece is placed into a convention when it meets what its Approach on Trial said would settle it. A piece can be dropped at any evaluation."

**FINDING-651.** rule 9; uncertain. `.claude/approaches-on-trial/approach-evaluation.md`, heading (line 17): "## The stages of an Approach on Trial". "Stages" here is the life of an Approach on Trial (drafted, on trial, placed); *Stages* at line 38 is this page's Approach Stages. One lowercase word carries two meanings in one file. 1 instance. Proposed: fix: "## The life of an Approach on Trial"; or decline if the English word is clear enough.

**FINDING-652.** rule 9; checked. `.claude/approaches-on-trial/approach-evaluation.md`, *Not known yet* (line 109): "- **Whether generalizing is work of its own.** Today it is stage 6." A label inside its owner keeps its case; this file writes "stage 6" (109, 130–131) and "Stage 3" (132), "stage 3's" (147) for the same kind of thing; `model-placing.md` line 91 "stage 7"; `auto-run.md` line 86 "Stage 4's". 5 instances across three files. Proposed: fix: "Stage 6", "Stage 3", "Stage 7", as the glossary writes Stage 3; or a ruling that an unlabelled numbered stage is lowercase, and then line 132 and auto-run change instead.

**FINDING-653.** rule 9; checked. `.claude/approaches-on-trial/approach-evaluation.md`, *Uses* (line 129): "*The deliverer, `model-placing.md`'s first evaluation, 2026-10-28.*". Lowercase Names: "The deliverer" (129, 139, 145), "the approach" (130), "a model" (132, 133), and *Not known yet* line 101 "stays in approaches" for Approaches on Trial. 7 instances. Proposed: as FINDING-647.

**FINDING-654.** rule 2; checked. `.claude/approaches-on-trial/auto-run.md`, *Stages*, stage 1 (lines 25–26): "the CBC Run's Run Reading (`exchange-read`), which harvests its lessons; / the cost, that those lessons do not reach this CBC Run, is said to". Three ideas chained with "which", a semicolon and a nested clause. Stage 6 lines 56–58 and *Not known yet* lines 68–72 do the same. 3 instances. Proposed: fix: "This is not the CBC Run's Run Reading (`exchange-read`), which harvests its lessons. Those lessons do not reach this CBC Run. The reviewer is told that cost."

**FINDING-655.** rule 8; uncertain. `.claude/approaches-on-trial/auto-run.md`, *Stages*, stage 4 (lines 44, 46): "- how far it may grow or shrink: the Run Briefing's Out is closed," and "areas and slices, past which is a Real question; every trouble". "Out" and "Real question" are labels from the method's framing with no plain words. 2 instances. Proposed: question for the reviewer: the reader holds the concept and the shipped `cbc-framing`; if that is enough, decline; else "the Run Briefing's Out, what the system will not do, is closed".

**FINDING-656.** rule 3; checked. `.claude/approaches-on-trial/auto-run.md`, *Uses* (lines 94–95): "*The deliverer, run 5's birth, 2026-10-21 to 2026-10-22.* Prepared / and born in one evening, 19 commits: three readers on run 4 at the". Lines 94–100 chain six parts of the preparation with semicolons in one sentence; lines 116–118 chain three open questions the same way. 2 instances. Proposed: fix: a list, as the note's "Taught:" already is.

**FINDING-657.** rule 9; checked. `.claude/approaches-on-trial/auto-run.md`, *Uses* (line 111): "- **a budget without a check does not hold:** the decision log". Lowercase Names: "the decision log" (Decisions Log, 111), "The deliverer" (94), "run 5"/"run 4"/"Run 5"/"the run"/"a running run" (94, 95, 100, 108, 117: CBC Run), "the briefing" (96: Run Briefing), "a hand-off"/"its hand-off"/"the hand-off" (98, 103, 113, 116: Run Hand-off), "the seed's prompt" (99: Pure Seed), "the newborn" (103: Newborn Run), "an approach on trial"/"approaches"/"the approach" (104, 106, 115), "its reading" (118: Run Reading). About 20 instances. Proposed: as FINDING-647.

**FINDING-658.** rule 7; resting on the reader. `.claude/approaches-on-trial/auto-run.md`, *Uses* (line 116): "Not known still: what in the hand-off is general; how the reviewer". Lines 116–118 restate two items of *Not known yet* (lines 62–67) in other words. 1 instance. Proposed: fix: "Not known still: the first two items of *Not known yet*, and whether the light read cost CBC Run 5 anything, which its Run Reading will say."

**FINDING-659.** rule 9; checked. `.claude/approaches-on-trial/model-placing.md`, *Uses* (line 77): "`c94438e`..`a22529d`.* The tiers model sent its reader down four". Lowercase Names: "The deliverer" (76), "the tiers model" (76, 77), "the exchange" (76, 78, 79, 81, 82, 90), "the model" (80, 83, 85, 87), "its pin" (79: Delivery Pin), "The fill" (81: Delivery Fill), "stage 7" (91). About 16 instances. Proposed: as FINDING-647.

**FINDING-660.** rule 6; resting on the reader. `.claude/approaches-on-trial/model-placing.md`, *Uses* (line 80): "went into a new tiers §3.5; the other two the model already held,". A reference is written exactly; "tiers §3.5", "its §1" (83) and "exchange §1" (90) carry no path and no title (`docs/models/tiers.md` §3.5, *What holds on every flow*; `docs/conventions/exchange/` §1, *What cannot change*). 3 instances. Proposed: fix: full Fact References; or decline if a dated note may abbreviate.

**FINDING-661.** rule 3; resting on the reader. `.claude/approaches-on-trial/model-placing.md`, *Uses* (line 87): "Taught: read the model whole before sorting (`4fedbb3`); a "today"". Three lessons chained with semicolons (lines 87–89); `auto-run.md`'s note lists its lessons. 1 instance. Proposed: fix: a list under "Taught:".

**FINDING-662.** rule 9; resting on the reader. `.claude/approaches-on-trial/approach-evaluation.md`, *Stages*, step 5 (line 60): "A new convention is added as the conventions manual says". A convention is named by its path or its Name, never the bare word (`docs/glossary.md`, header comment): also `model-placing.md` line 56 "likely the conventions manual", `refinement.md` line 131 "project-recording, with the map of the records", `foundation-check.md` line 82 "the check stands on facts-in-sync", `one-home.md` line 67 "one home is facts-in-sync's". 5 instances across 5 files (`refinement.md` line 129 gives the path and is fine). Proposed: fix: the path in backticks, `docs/conventions/conventions/`; or decline: the bare word is settled English here, and the glossary's header line changes instead.

**FINDING-663.** rule 4; uncertain. `.claude/approaches-on-trial/refinement.md`, *What it is for* (line 20): "The need was written down on 2026-10-17. Most of this repo's text". "Most" where a count could be given; the writing manual's §2 rule 11 counts "83 of the 99 living files" for a like claim. 1 instance. Proposed: question for the reviewer: is a count of files predating the four rules worth taking? Else decline.

**FINDING-664.** rule 9; resting on the reader. `.claude/approaches-on-trial/refinement.md`, §1 *What it reads, and its words* (line 62): "- **living text** — every file but history. History is the". The page says "The words of this page, each defined once" and gives "living text" a meaning English does not; a defined thing gets a capitalized Name of two words, and the glossary lists none, while the other three words in the list are Names. Used as the defined thing at: this file 125, 138; `foundation-check.md` 62; `one-home.md` 54–55; and as "live text" in `commit-plan/SKILL.md` (both copies) 118, 125. 7 instances. Proposed: question for the reviewer: a Name, Living Text, in the glossary pointing at facts-in-sync §1; or a ruling that it is English, and then commit-plan's "live text" follows the others' words.

**FINDING-665.** rule 10; uncertain. `.claude/approaches-on-trial/refinement.md` (line 55): "## 1. What it reads, and its words". A title is one noun phrase; this is two, joined by a comma. 1 instance; it is a Fact Reference title at line 125. Proposed: question for the reviewer: a section of its own for the words, with the rename grep; or decline.

**FINDING-666.** rule 10; uncertain. `.claude/approaches-on-trial/refinement.md`, §2.1 (line 99): "### 2.1 Group the Finding Kinds". An imperative, not a noun phrase; §2.2 *List the files*, §2.3 *Check the rules*, §2.5 *List the findings* are the same, while §2.4, 2.6, 2.7 are gerund phrases. 4 instances. Proposed: question for the reviewer: are §2.1–2.10 Approach Stage headings, exempt as a stage heading is (the §2 map calls them the Approach Stages), or numbered sections? If sections: "Grouping the Finding Kinds", "Listing the files", "Checking the rules", "Listing the findings", with the rename grep, since each is a Fact Reference title in this file.

**FINDING-667.** rule 2; checked. `.claude/approaches-on-trial/refinement.md`, §2.3 *Check the rules*, story line (lines 188–189): "*Found 2026-10-25, before round 2: a convention TODO had due when / round 2 reads would move the rules its One home and Dependencies". The sentence nests "had due when … reads would move the rules … stand on, mid-read" and cannot be read once. *What it is for* lines 33–35 and §3 lines 346–348 (two parentheses in a row, then two clauses) are chained too. 3 instances. Proposed: fix: "A convention TODO item was due when round 2 would read. Its fix would have moved the rules the One home and Dependencies kinds stand on, in the middle of the read."

**FINDING-668.** rule 9; checked. `.claude/approaches-on-trial/refinement.md`, §2.3 story line (line 188): "round 2". Refinement Round is the Name, and the file writes "Refinement Round 1" at line 338; the story lines write "round 2" (188, 189, 298), "the first round", "each round" (191), "round 1" (273, 297), and "in a run" (274) for a CBC Run. 8 instances. Proposed: fix: "Refinement Round 2" etc., "in a CBC Run"; or question: are the italic *Found* lines history?

**FINDING-669.** rule 7; checked. `.claude/approaches-on-trial/refinement.md`, §2.8 *A Refinement Round's close* (line 301): "Then the next Refinement Round reads." Lines 292–293 say it ("The next Refinement Round reads the text, not the findings"), and §2's map says it (line 94). 1 instance. Proposed: fix: delete line 301 and its blank line.

**FINDING-670.** rule 8; resting on the reader. `.claude/approaches-on-trial/refinement.md`, §3 *Not known yet* (line 347): "that has lived it; a draft into both step forms was undone before". "Both step forms" has no plain words: ours and the container's Plan Step Form. 1 instance. Proposed: fix: "a draft into both Plan Step Forms, ours and the container's, was undone".

##### From the items checked first

**FINDING-671.** rule 9; resting on the reader. `.claude/skills/commit-plan/SKILL.md` and `delivery/container/.claude/skills/commit-plan/SKILL.md`, §6's table, its bold lead and the *Decisions* footer (lines 104, 151, 191): "| Small steps | tries, fixes, a way abandoned | inside a planned commit, on the reviewer's grant; …". The manual's §2.11 was retitled *Small commits* in the Names pass, since "Small steps" used Plan Step's word in its plain sense (`temp/refinement-2026-10-18.md`, *The rules' check*, doubt 2); the skill derived from it still says it in three places. One of the two words *Kinds and rounds* promised this round under rule 6. Proposed: fix: "Small commits" in the row, the lead and the footer's gloss, both copies.

**FINDING-672.** rule 9; resting on the reader. `.claude/skills/exchange-read/SKILL.md`, opening (line 9): "Four steps, and the fourth is a document." The four numbered instructions under §1 are the skill's phases; `docs/conventions/conventions/` §1.4, *Skill Stages*, has a skill's phases as Skill Stages, each under its own heading, and lets a numbered instruction inside a Skill Stage be called a step. Round 2's note, met in passing and held since. Proposed: question: are the four Skill Stages, each under a `## Stage n — …` heading, or steps inside one Skill Stage; if steps, the line stands.

#### Layer 6: `delivery/`, what ships

##### `delivery/README.md`

**FINDING-673.** rule 2; resting on the reader. `delivery/README.md` opening (line 5): "How a CBC Run is born is `delivery/installs/pure-seed.md`; how it is updated afterwards, and how what it learns comes back, is the Exchange Convention". Two ideas (birth; update and return) chained with a semicolon. Proposed: split at the semicolon.

**FINDING-674.** rule 3; resting on the reader. `delivery/README.md` §2, *Three ways a file lands* (line 29): "**Pinned copies.** The container's convention skills, Agent Rules and Approach on Trial; the method's and the stack practice's skills, Agent Rules and Output Shapes; and the concept, at `docs/concept/`". Three sources chained with semicolons; a list would show three. Proposed: three sub-bullets under the bold lead, or decline: the bullet is already a labelled part.

**FINDING-675.** rule 2; resting on the reader. `delivery/README.md` §2, *Three ways a file lands* (line 41): "its Plan Steps replace everything between the PLAN Record Stub's STEPS markers, and the "Steps from:" line names it at the Delivery Pin (`delivery/installs/pure-seed.md` step 4); the CBC Run holds no copy of the playbook". One table cell, three ideas. The same at §4 line 66 (three ideas with a colon and a semicolon), §5 lines 74-76 ("which … ; and … since") and §6 lines 82-84 ("so an early copy is inert, and one moment keeps…"): 3 more. Proposed: split each at the semicolon; a cell may hold two short sentences.

**FINDING-676.** rule 6; checked. `delivery/README.md` §4, *What the tree does not show* (line 66): "the pre-framing guard and the pin stance". Two coined labels for the entry files' two paragraphs; not in the glossary, not defined where they stand, and grep finds them nowhere else but `delivery/installs/pure-seed.md` lines 22-23. Proposed: say each in plain words at its first use ("the paragraph that forbids method work before framing, and the line that says the concept is a pinned copy") and drop the labels.

**FINDING-677.** rule 8; checked. `delivery/README.md` §5, *What a CBC Run does not get* (line 75): "and the archive's agent definitions, since". Nothing in this file says what "the archive" is; it is `README.md`'s word (its lines 27-49) for the repo the concept came from. Proposed: "the agent definitions of the archive repo the concept came from", or cut the clause: ADR-0006 holds it.

**FINDING-678.** rule 9; resting on the reader. `delivery/README.md` §2, *Three ways a file lands* (line 30): "the method's and the stack practice's skills". The Method Group and the Stack Group are meant; "the stack practice" is neither a Name nor plain English. "The container" (lines 25, 36, 48, 65, 69) reads as English for `container/` and is not counted. Proposed: "the Method Group's and the Stack Group's skills".

**FINDING-679.** rule 8; uncertain. `delivery/README.md` §6, *When it lands* (line 82): "Each practice skill's readiness gate refuses to start". "Readiness gate" names a skill's Stage 0 check in words the skills do not use. Proposed: "Each skill's Stage 0 refuses to start", or decline: this repo's reader knows the skills.

##### `delivery/installs/pure-seed.md`

**FINDING-680.** rule 2; checked. `delivery/installs/pure-seed.md` opening (lines 4-9): "Every delivery is a commit on a receipt branch, `birth-seed`, so that branch is the manifest — what arrived, from where, at which Delivery Pin — while main stays at the hygiene commit with the same files in its worktree, untracked: the newborn's agent finishes the birth itself by reading what is there and committing it under its own sequence and split (ADR-0018)." One sentence, five ideas, chained with dashes, "while" and a colon. The prose does this throughout: lines 9-14, 21-24, 62-65, 128-130, 132-135, 137-140, 151-154, 154-157, 194-198, 198-202, 203-206, 209-211, 223-229, 233-239: 14 more sentences. Proposed: rewrite the prose paragraphs under rules 2 and 3 in work of their own (the rule's *Where it applies*: older text is rewritten in work of its own); the code blocks stay.

**FINDING-681.** rule 2; checked. `delivery/installs/pure-seed.md` step 6, the prompt (lines 163-168): "This repo was seeded, not born whole — the branch birth-seed shows it: one delivery from correctness-by-construction, in two halves — first the records, the conventions and the two entry files, then docs/concept/, five method and stack skills, the method's four Output Shapes and the Plan Steps in PLAN — every seed commit naming that one Delivery Pin." One sentence; the two halves and their seven parts chained with dashes. Its reader is a Newborn Run's agent, before it has read anything. Proposed: short sentences, the two halves as two lines; question for the reviewer: is the hand-back prompt held to the rule, or kept as it ran in CBC Run 4?

**FINDING-682.** rule 3; checked. `delivery/installs/pure-seed.md` closing (lines 249-260): "What the agent is left to do — the reader's checklist for the Run Reading afterwards, not instructions delivered to it: every delivered file committed on main by the agent, under its own sequence and the commit split the skills define (…); a commit plan whose sequence is chosen and justified (…); the Record Stubs filled; Step 0 closed clean on its container gates — …; the agent/project commit split held throughout, from the skills, unprompted." A checklist of five, in one 12-line sentence with semicolons and nested parentheses, right after a list that is a list (lines 223-247). Also lines 9-14, the five fills in one sentence, and lines 194-198, the five things the prompt carries: 2 more. Proposed: a bulleted list of five, each time.

**FINDING-683.** rule 5; resting on the reader. `delivery/installs/pure-seed.md` opening (line 16): "What the agent cannot derive rides in the seed commits' subjects". "Rides" for "is in", 5 times: lines 16, 19, 138, 140, 208. Also "Fire the agent" and "before firing" (lines 159, 154) for starting a session; "no voice above the file says anyone is watching" (lines 200-201); "the answer sheet" and "hard backstop" (lines 210-211); "the claim has nothing to land on" (line 217); "meets the container and the method raw" (line 20). Proposed: "is in", "start the agent", "nothing outside the file says a reviewer is present", "the baselines a CBC Run must not read", "has nothing to compare against".

**FINDING-684.** rule 6; checked. `delivery/installs/pure-seed.md` closing (lines 263-264): "the derived arrangement against the walk-1 baseline and the shipped template". "Walk-1" is a number local to something not named, and grep finds it in no living text but this line; "the shipped template" uses the word ADR-0074 retired, where the container's Record Stubs are meant. Proposed: name the baseline by its path under `docs/baselines/`, and "the shipped Record Stubs"; question: does a walk-1 baseline still exist?

**FINDING-685.** rule 6; resting on the reader. `delivery/installs/pure-seed.md` step 4, shell comment (line 98): "(docs/conventions/exchange/ §3.3)." A Fact Reference with no title; again at lines 106-107. Proposed: add *A group's place in the tree*, or decline: inside a code block, the comment's length is the shell's.

**FINDING-686.** rule 8; checked. `delivery/installs/pure-seed.md` opening (line 15): "no bundle birth entry". "Bundle" is the delivery's old word (the Exchange Convention's §*What it is for* names `bundle-update.md` as history); no living text says what a bundle birth entry is; again at line 243, and `bundle_dir`, `bundle_pin` and `<bundle-commit>` (`delivery/container/.claude/decisions.md` line 33) keep the word. Other labels the reader meets cold: "the session channel" (line 194), "a measured object" (line 202), "assembly conclusion" (line 239), "the entrance doc" (line 255), "container gates" (line 258): 5 more. Proposed: plain words at each ("no entry copied from this repo's own birth", "the prompt holds what is true of this session only", "the entry file"), and `deliverer_dir`/`deliverer_pin` when the block is next edited.

**FINDING-687.** rule 9; checked. `delivery/installs/pure-seed.md` opening (line 8): "the newborn's agent finishes the birth itself". "The newborn" where Newborn Run, the glossary's Name, is meant; 6 times: lines 8, 130, 159, 213, 216, 247. Proposed: "the Newborn Run" at each; line 216 "a Newborn Run holds no earlier state".

**FINDING-688.** rule 7; resting on the reader. `delivery/installs/pure-seed.md` step 1 (line 35): "One Delivery Pin, ours, and one directory". Said again at line 65 ("One Delivery Pin, because the CBC Run holds one delivery (ADR-0025, ADR-0036)") and line 128 ("One Delivery Pin in every subject, ours"): one fact, three sentences. "No playbook file" likewise at lines 13-14 and 18-19 (line 238-239 is a check item and stays). Proposed: keep line 65, the one with the ADRs; cut the sentences at 35 and 128; keep one of 13-14 and 18-19.

**FINDING-689.** rule 6; uncertain. `delivery/installs/pure-seed.md` step 6, the prompt (line 180): "I am the reviewer the commit-plan convention names". The Newborn Run holds the `commit-plan` skill, not the convention, and the skill is what names the reviewer. Proposed: "the reviewer the commit-plan skill names".

##### `delivery/fills/cbc-run-pure-playbook.md`

**FINDING-690.** rule 9; uncertain. `delivery/fills/cbc-run-pure-playbook.md` header comment (line 1): "The CbC run playbook." "CbC run" where the Name is CBC Run; again in the title, line 14, "# Playbook: CbC run — pure". Line 5, "Harvest lands here, the one copy", where Record Harvest is meant. Proposed: "The CBC Run playbook", "# Playbook: CBC Run — pure", "The Record Harvest lands here"; or decline: "CbC run" is the playbook's own name, `cbc-run-pure`, kept as a label.

**FINDING-691.** rule 2; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` header comment (lines 5-9): "Harvest lands here, the one copy (ADR-0007): each lesson as a changed gate, a new Plan Step, or a line under a Plan Step's Known already, Framing's and Release's in this playbook's own copies of those Plan Steps; each fold bumps the version line." Four ideas in one sentence; lines 9-12 ("Its history — … — is in the devlog and in this file's git log.") carry a three-part list inside a dash pair: 1 more. The comment stays here, so its reader is this repo's. Proposed: split; the history as three items.

**FINDING-692.** rule 3; uncertain. `delivery/fills/cbc-run-pure-playbook.md` Step N-2, Goal (lines 196-199): "every lesson the next CBC Run should act on is a decision in RETRO.md, with an example from this CBC Run and the place it lands; this CBC Run's Run Asks point to those decisions; and what only the next CBC Run can check is listed, each with the Plan Step that judges it." Three outcomes chained with semicolons; the Plan Step Form fixes "Goal: <one sentence>", which forces the chain. Step N-1's Goal (lines 208-210) and Steps 5..N-3's Goal (lines 187-189) chain two each: 2 more. Proposed: decline, the form asks for one sentence; or let the form say a Goal may be up to three short sentences.

**FINDING-693.** rule 2; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` Step 1, CbC comment (lines 147-149): "this Plan Step opens on the Run Briefing — its starting input, the first prompt of project work, committed unchanged at docs/system/framing/briefing.md (cbc-framing)." Three ideas with a dash; lines 125-127 ("To resume, its branch is fast-forwarded to main, it restarts at that stage, and any stage whose input the other Plan Step changed runs again.") chain three: 1 more. Proposed: split each.

**FINDING-694.** rule 8; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` *The Plan Step Form* (line 80): "Items the playbook already knows a Plan Step needs". A CBC Run holds no playbook file; its PLAN's "Steps from:" comment names one. "The playbook" is met with no words saying it is the source its Plan Steps were copied from; `delivery/container/.claude/skills/retrospective/SKILL.md` line 10 does the same. Proposed: "Items the playbook these Plan Steps were copied from already knows" at the first use; or an entry in the container's glossary under *From the delivery*.

##### The container's records and hygiene files

**FINDING-695.** rule 9; checked. `delivery/container/PLAN.md` header comment (line 5): "the seed replaces the region between the STEPS markers". "The seed" where Pure Seed, a Name in the CBC Run's glossary, is meant. Proposed: "the Pure Seed replaces".

**FINDING-696.** rule 5; resting on the reader. `delivery/container/PLAN.md` *Legend* (line 23): "keep later Plan Steps coarse (rolling wave)." A project-management figure the reader must translate; "coarse" already says it. Proposed: cut the parenthesis.

**FINDING-697.** rule 2; checked. `delivery/container/README.md` opening (lines 3-7): "A backend built by [correctness-by-construction](docs/concept/): a system whose design is derived from one falsifiable promise — asking what must never happen before what it should do — and whose every invariant is held by a wall that a test creating its adversity proves." One sentence, three ideas, a dash interruption. `delivery/container/.claude/CLAUDE.md` lines 3-6 have the same shape: 1 more. Proposed: "…derived from one falsifiable promise. It asks what must never happen before what it should do. Every invariant is held by a wall, and a test that creates its adversity proves the wall."

**FINDING-698.** rule 9; checked. `delivery/container/README.md` opening (line 8): "briefing that opens framing". "The briefing" where Run Briefing is meant (`.claude/CLAUDE.md` line 6 writes it so); "framing" lowercase where the Plan Step's label is "Framing" (the playbook's Step 1; the Pure Seed's prompt, line 187, "opens Framing"). Proposed: "the Run Briefing that opens Framing".

**FINDING-699.** rule 5; resting on the reader. `delivery/container/README.md` header comment (lines 31-32): "it arrives when a Plan Step's gate makes it true — projection follows truth." A figure after a sentence that already says what happens. Proposed: cut "— projection follows truth".

**FINDING-700.** rule 2; checked. `delivery/container/TODO.md` header comment (lines 17-19): "The story goes in that session's devlog entry when the item is added, and See points at it; an item that is its story's only home keeps it and has no See." Two ideas chained; lines 19-21 ("Ideas are noted … — each is then taken, extended or declined, and the verdict goes with the work.") and 21-24 ("rewrite it true for today — never stack a dated update on it; the change's story is the devlog's.") do the same: 2 more. Proposed: split each at the semicolon or dash. Ours too: `TODO.md` lines 19–27 carry the same sentences (reader E).

**FINDING-701.** rule 5; resting on the reader. `delivery/container/TODO.md` header comment (line 3): "Add items the moment they're discovered — that's what empties your head." Also line 4, "Prune "Later" ruthlessly". Proposed: "Add items the moment they're discovered, so nothing has to be held in memory." "Delete from Later freely". Ours too: `TODO.md` lines 3–4 (reader E).

**FINDING-702.** rule 5; resting on the reader. `delivery/container/devlog/devlog.md` header comment (line 9): "Mark dead ends loudly with "DEAD END:" so they're greppable." Also line 10, "cheapest save-point there is", and line 5, "For future-you". Proposed: "Mark dead ends with "DEAD END:" so they're greppable." "End every session with a "Resume:" line: the next session starts there." "For your later self". Ours too: `devlog/README.md` lines 11 and 13, "Mark dead ends loudly" and "cheapest save-point there is" (reader E).

**FINDING-703.** rule 4; uncertain. `delivery/container/devlog/devlog.md` header comment (line 11): "When this file gets long, split into devlog/<YYYY-MM>.md per month." "Long" where a line count could be given; this repo's own devlog is split per month from the start. `delivery/container/.claude/CLAUDE.md` line 66, "Longer than a screen means a line is failing.", is the same kind: 1 more. Proposed: a number ("past 300 lines"; "past 60 lines"), or decline: no measured threshold exists.

**FINDING-704.** rule 5; uncertain. `delivery/container/CHANGELOG.md` header comment (lines 9-11): "in user-speak ("order creation is 3x faster"), not developer-speak ("refactored OrderService") — users may be future-you". Coined words; the examples beside them define them. Proposed: "in the user's words (…), not the developer's (…)"; or decline: the examples carry it.

**FINDING-705.** rule 9; uncertain. `delivery/container/docs/adr/0001-record-architecture-decisions.md` *Decision* (line 24): "using this template (context / options / decision / consequences)". "Template" where the record's form is meant; ADR-0074 retired the word for all but a Skill Template. Line 39, "Template for the next ADR: copy this file", the same: 1 more. The body is a shipped ADR, Accepted at birth: question for the reviewer, is its body living text or a closed ADR? Proposed: "using this form"; "The form of the next ADR: copy this file".

**FINDING-706.** rule 5; uncertain. `delivery/container/docs/adr/0001-record-architecture-decisions.md` *Context* (line 10): "Without a record, the *why* evaporates:". A figure. Proposed: "the why is lost"; or decline with FINDING-705 if the body is history.

**FINDING-707.** rule 2; resting on the reader. `delivery/container/temp/README.md` opening (lines 5-6): "It is tracked, so what was drafted here shows in history; a file is deleted once it has served, and git keeps it." Three ideas. Lines 12-14 ("They are taken as the delivered-copies Agent Rule says (…), and a Delivery Staging is never committed: the Delivery Take removes it, and only it.") chain three: 1 more. Proposed: split each.

**FINDING-708.** rule 9; checked. `delivery/container/.editorconfig` header comment (lines 15-16): "Stack overlay blocks are appended at app bootstrap below the marker at the bottom." "Stack overlay" where the Name is Stack Overlay, which the CBC Run's glossary lists. Also `.editorconfig` line 53, `.gitattributes` line 9 and `.gitignore` line 29, "stack overlays — appended below this line at app bootstrap": 3 more lines in 3 files. Grep finds no skill or script that matches the marker text, so its case can change. Proposed: "Stack Overlay blocks", "Stack Overlays — appended below this line at app bootstrap".

**FINDING-709.** rule 3; resting on the reader. `delivery/container/.editorconfig` header comment (lines 10-13): "Layout conventions (hand-kept - no tool formats this file): each comment+setting group is separated from the previous entry by one blank line; comments are whole lines, above their setting; a ruler line marks each file-type block." Three conventions chained with semicolons; a list would show three. Proposed: three comment lines, one convention each. Both copies: the root `.editorconfig` lines 10–13 carry the same comment (reader E).

##### The container's agent files

**FINDING-710.** rule 2; checked. `delivery/container/.claude/CLAUDE.md` *Correctness by construction* (lines 16-17): "The method is in `docs/concept/` — read `docs/concept/00-cbc.md` first; the other chapters deepen it." Three ideas with a dash and a semicolon. Lines 21-24 ("Until the framing artifacts exist (…), the project is pre-framing: the only method work is running cbc-framing jointly with the human — never invent the artifacts to fill the gap.") and the header comment's lines 10-12 ("No current state — a state clause has a moment and stales at every Plan Step's close; where the project stands is PLAN's") do the same: 2 more. Proposed: "The method is in `docs/concept/`. Read `docs/concept/00-cbc.md` first. The other chapters deepen it."

**FINDING-711.** rule 6; resting on the reader. `delivery/container/.claude/CLAUDE.md` *Correctness by construction* (line 23): "running cbc-framing jointly with the human". Every other shipped file calls this person the reviewer (the rules and skills, 20 and more times; the Pure Seed's prompt, "I am the reviewer"); grep finds "the human" in the container only here. One role, two names. Proposed: "jointly with the reviewer".

**FINDING-712.** rule 8; uncertain. `delivery/container/.claude/CLAUDE.md` header comment (line 10): "a state clause has a moment and stales at every Plan Step's close". "Has a moment" is agent-arrangement's sense, a time at which a line is read, and nothing here says so; the three-tests comment, line 61, uses it again ("No moment — else it goes where the moment is"). Proposed: "a state clause is true at one time and stales at every Plan Step's close"; or decline: test 2 explains it in place.

**FINDING-713.** rule 5; resting on the reader. `delivery/container/.claude/decisions.md` header comment (lines 8-9): "the standing rule rides as a comment in the artifact it governs". Also lines 16-17, "each entry graduates to the Concept Deliverer, stays local, or dies." Proposed: "the standing rule is a comment in the artifact it governs"; "each entry goes to the Concept Deliverer, stays local, or is dropped".

**FINDING-714.** rule 2; resting on the reader. `delivery/container/.claude/decisions.md` header comment (lines 22-24): "Beside it the entry carries the Read-Through Commit, the commit of this project the Concept Deliverer last read up to; at birth nothing has been read, and the first Delivery Note sets it." Three ideas. Proposed: split at the semicolon.

**FINDING-715.** rule 8; checked. `delivery/container/.claude/decisions.md` birth entry (line 41): "Rejected: none — see the Concept Deliverer's ADRs." The reader cannot open them (`.claude/rules/delivered-copies.md` line 34: "this CBC Run cannot open them"); the line sends it to what it cannot read. Proposed: "Rejected: none here. The Concept Deliverer's ADRs hold what it rejected; this project cannot open them."

**FINDING-716.** rule 8; checked. `delivery/container/.claude/rules/delivered-copies.md` *Decisions* (line 181): "built from the seven rules never-oversold wrote for its own method skills". "Never-oversold" is CBC Run 3's repository name, which the CBC Run's reader does not hold. Also `.claude/rules/shapes-lifecycle.md` line 106, `.claude/skills/retrospective/SKILL.md` line 141 and `.claude/skills/apply-retrospective/SKILL.md` line 148: 3 more files. Proposed: "an earlier CBC Run, CBC Run 3" at each, CBC being the Repo Tag the reader already meets in `CBC ADR-nnnn`.

**FINDING-717.** rule 6; uncertain. `delivery/container/.claude/rules/delivered-copies.md` *Decisions* (line 184): "CBC ADR-0046 — item 5: the Delivery Take's commits". The file's numbered parts are rules (the glossary's own example: "delivered-copies rule 4"); "item 5" names one by another kind. Proposed: "rule 5".

**FINDING-718.** rule 9; uncertain. `delivery/container/.claude/rules/delivered-copies.md` rule 8 (line 163): "it is **off-template**:". Bold marks a coined label, defined by the list that follows and not in the glossary. Proposed: drop the bold; or question: is "off-template" a defined thing wanting a Name and a glossary entry?

**FINDING-719.** rule 8; resting on the reader. `delivery/container/.claude/rules/delivered-copies.md` rule 4 (line 87): "The Run Ask is done at the re-pin." "The re-pin" is met here, and in the title (line 12), before rule 5 (line 89) says it is the Delivery Take. Proposed: "The Run Ask is done at the Delivery Take (rule 5)."

**FINDING-720.** rule 5; resting on the reader. `delivery/container/.claude/rules/delivered-copies.md` closing (line 171): "The Delivery Pin is the truth of origin, and the Decisions Log is the why." Also rule 4, line 80: "so the Concept Deliverer reads those hunks hardest". Proposed: "The Delivery Pin says where a copy came from; the Decisions Log says why it changed." "reads those hunks most carefully".

**FINDING-721.** rule 9; checked. `delivery/container/.claude/rules/one-home.md` header comment (line 12): "The why is in the deliverer's facts-in-sync manual". "The deliverer" where Concept Deliverer, the glossary's Name, is meant. Also `.claude/rules/writing.md` line 12, "The why of each rule is the deliverer's writing manual.": 1 more. (The heading `## To the deliverer` is a fixed label and stays.) Proposed: "the Concept Deliverer's" at both.

**FINDING-722.** rule 9; uncertain. `delivery/container/.claude/rules/shapes-lifecycle.md` opening (line 9): "An **Output Shape** says what a kind of output looks like in this project". Bold marks the Name in prose. The file keeps the definition because a CBC Run cannot open the manual (CBC ADR-0037); the glossary's entries bold a Name as their form, and this is not the glossary. Proposed: drop the bold.

**FINDING-723.** rule 8; checked. `delivery/container/.claude/rules/shapes-lifecycle.md` §5, *Offering an Output Shape back* (lines 92-93): "the Concept Deliverer reads it at its next Run Reading." Run Reading is a Name of this repo's; the CBC Run's glossary does not list it, and nothing in the file says what it is. (`.claude/skills/visual-comparison/SKILL.md` line 98 uses it too; another reader's file.) Proposed: "reads it the next time it reads this project's records"; or an entry under *From the delivery* in the container's glossary.

**FINDING-724.** rule 8; resting on the reader. `delivery/container/.claude/rules/shapes-lifecycle.md` §1, *Written from work that exists* (line 38): "The reviewer settles what the look finds". "The look" names the side-by-side reading above it without saying so. Proposed: "settles what this reading finds".

**FINDING-725.** rule 9; checked. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` frontmatter (line 3): "Do NOT use to decide what the next run does differently". "The next run" where CBC Run is meant; `.claude/skills/retrospective/SKILL.md` line 3, "Do NOT use to fix this run's records": 1 more. Proposed: "the next CBC Run"; "this CBC Run's records".

**FINDING-726.** rule 1; uncertain. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` opening (line 9): "The retrospective decided and changed nothing. This Plan Step applies it to the CBC Run itself, before Release". The first sentence is what the previous skill did; the point is the second. Proposed: "This Plan Step applies the finished retrospective to the CBC Run itself, before Release. The retrospective decided and changed nothing."

**FINDING-727.** rule 3; checked. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 0 (lines 22-28): "Its own items come from the goal: every decision has a row; every applied row names its commits; the CBC Run's proof unchanged (where the project has tests: green, as many as at the last close); history untouched; the records later Plan Steps were built on changed only by dated revision entries; each delivered copy edited has its Decisions Log entry and its Run Ask; what trying taught is written back." Seven gate items chained with semicolons; a list would show seven. Stage 4 item 1 (lines 113-116) chains four checks the same way: 1 more. Proposed: a sub-list, one item per line, both places.

**FINDING-728.** rule 4; resting on the reader. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 3 (line 94): "A second fresh read if the fixes were more than a few, never a third." "A few" where a count could be set. Proposed: "more than five"; or decline: the number is not known yet.

**FINDING-729.** rule 11; uncertain. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 3 (line 107): "**A tool that edits text** (a rewrap, a replace) is checked on what it must not touch". Names a rewrap as a tool a CBC Run may run on its records; writing rule 11 says Markdown has no line width, so a rewrap of a record has no reason. Proposed: "(a replace, a move)"; or decline: the sentence governs any tool, and does not ask for one.

**FINDING-730.** rule 9; uncertain. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 3 (line 92): "Then a **fresh reader** with no part in the rewrite checks". Bold on a coined label, explained in place; "Fresh readers" at line 97-98. Proposed: drop the bold.

**FINDING-731.** rule 8; resting on the reader. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 1 (line 39): "written in the note's form". "The note" is `retrospective`'s word for RETRO.md (its line 22, "Write the note, `RETRO.md`"); this file says "RETRO.md" (line 37) and then "the note" without tying them. Proposed: "written in RETRO.md's decision form".

**FINDING-732.** rule 6; resting on the reader. `delivery/container/.claude/skills/retrospective/SKILL.md` Stage 0 (line 20): "until the retro lands." "The retro" for the retrospective, 3 times: lines 20, 99, 101. Proposed: "the retrospective" at each.

**FINDING-733.** rule 2; resting on the reader. `delivery/container/.claude/skills/retrospective/SKILL.md` Stage 3 (lines 101-103): "At the close the reviewer keeps it (`retrospective` fast-forwards to it) or drops it (the branch is deleted, and the note's commits move back)." Three ideas, two nested parentheticals. Proposed: "At the close the reviewer keeps it or drops it. Kept: `retrospective` fast-forwards to it. Dropped: the branch is deleted, and the note's commits move back."

**FINDING-734.** rule 8; resting on the reader. `delivery/container/.claude/skills/retrospective/SKILL.md` opening (lines 10-11): "the skills, the Agent Rules, the playbook, the Skill Templates, the reviewer's local file". "The playbook" (see FINDING-694) and "the reviewer's local file" are met with no words saying what they are. Proposed: "the playbook the Plan Steps came from, the Skill Templates, the reviewer's `CLAUDE.local.md`".

**FINDING-735.** rule 8; resting on the reader. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 4 item 7 (line 132): "The look back and the `-detail` branch are commit-plan's". Two labels of commit-plan's, met before the Fact Reference on the next line; `.claude/skills/retrospective/SKILL.md` line 122 is the same sentence: 1 more. Proposed: decline, the Fact Reference names where both are defined; or "The closing look at the landed commits, and the `-detail` branch that keeps what was tried, are commit-plan's".

##### The four Output Shapes

**FINDING-736.** rule 3; resting on the reader. `delivery/method/.claude/shapes/evidence-test.md` *What to check at a close* (line 177): "On every reading after the adversity: is the witness asserted". Rule 3 asks for a line per part; check 2 (lines 177-180) chains three checks (witness before answer; promise before numbers; the invariant where it differs) and a fourth question in one item. Proposed: fix: split check 2 into three numbered questions.

**FINDING-737.** rule 5; uncertain. `delivery/method/.claude/shapes/evidence-test.md` *The order of its assertions* (line 102): "adversity only checks the scene is set; it owes nothing." "Scene" is a theatre figure for the state a test sets up before the adversity; the manual names theatre words as ones to drop. Also line 134 "The helper a scene relies on". Proposed: fix: "checks the setup is in place", "the helper a setup relies on"; or decline if "scene" is a word the CBC Run's test code uses.

**FINDING-738.** rule 8; uncertain. `delivery/method/.claude/shapes/evidence-test.md` *What is exempt, and why* (line 166): "a catalog test, or the store's refusals". A label the reader meets with no plain words saying what it is, here or anywhere in the group. Proposed: question for the reviewer: what is a catalog test; say it in plain words or drop the example.

**FINDING-739.** rule 9; resting on the reader. `delivery/method/.claude/shapes/evidence-test.md` whole file (line 25): "a tripwire, which pins a decision and is not evidence." Rule 9 gives a defined thing a Glossary Name of two or more words; the file defines things on one English word with no Name in the CBC Run's glossary: tripwire (25, 56, 71, 160), structural test (24), evidence test (7), skeleton and illustration (32-34), a reading (97, 126). One question governs this and every roll-up below (FINDING-741, FINDING-744, FINDING-747, FINDING-775, FINDING-799, FINDING-808, FINDING-819, FINDING-823): do the method's coined terms get Names in the delivered glossary's first group, are they the CBC Run's to name at framing as `cbc-framing/SKILL.md` lines 107-111 say, or are they the concept's words, like slice and kill, and not Names? Proposed: question for the reviewer; the answer ends all nine.

**FINDING-740.** rule 9; checked. `delivery/method/.claude/shapes/kill.md` *What to check at a close* (line 123): "shape wrong, did each have something, or is it a different kind?" "The shape" written lowercase where the Output Shape is meant; `evidence-test.md` line 182-183 writes "was the Output Shape wrong". Proposed: fix: "was the Output Shape wrong".

**FINDING-741.** rule 9; resting on the reader. `delivery/method/.claude/shapes/kill.md` whole file (line 9): "against one possession. Its form, never its content". Defined things with no Name: possession (9, 57, 78), fence (44, 52, 65-70, 78, 106), collision (10, 20, 48), case (38, 63), death (59), the `*Say:*` line (72). Proposed: the FINDING-739 question.

**FINDING-742.** rule 9; checked. `delivery/method/.claude/shapes/registry-entry.md` *What this document controls* (line 22): "shape accepts can still cut the wrong slice; that is framing's". Lowercase "shape" for the Output Shape; also line 107 "shape wrong, did each have something, or is it a different kind?". Count 2. Proposed: fix: "this Output Shape", "was the Output Shape wrong".

**FINDING-743.** rule 5; uncertain. `delivery/method/.claude/shapes/registry-entry.md` *The shape* (line 40): "- **Rider:** <a structural condition checked, never battle-tested,". A military figure for "never put under adversity"; the same slot in `delivery/method/.claude/skills/cbc-framing/templates/registry.md` line 34. Count 2. Proposed: fix: "never tested under adversity"; or decline as a dead idiom.

**FINDING-744.** rule 9; resting on the reader. `delivery/method/.claude/shapes/registry-entry.md` whole file (line 42): "- **Flag riding:** <what cannot be staged the normal way, and what". Defined things with no Name: rider (40), flag riding (42), presumes (44), judgment logged (46), answered at close (48), status values (57); the same slots in the template (34-50, 70-96). Proposed: the FINDING-739 question.

**FINDING-745.** rule 9; checked. `delivery/method/.claude/shapes/slice-record.md` *What to check at a close* (line 221): "shape wrong, did each have something, or is it a different kind?" Lowercase "shape" for the Output Shape. Proposed: fix: "was the Output Shape wrong".

**FINDING-746.** rule 9; resting on the reader. `delivery/method/.claude/shapes/slice-record.md` *A guarantee's block* (line 55): "The block grows by stage. The specification writes the claim, the". "Stage" lowercase where cbc-slice's Skill Stages are meant (55; 58 "The reviewer signs a stage"), and the stages are named "the specification", "the plan", "the close" where the skill names them specify-correctness, plan, document (see FINDING-815). Proposed: question for the reviewer: is "stage" here the Skill Stage or English; if the Name, "grows by Skill Stage".

**FINDING-747.** rule 9; resting on the reader. `delivery/method/.claude/shapes/slice-record.md` whole file (line 42): "as planned, the deviations and provisionals." Defined things with no Name: provisionals (42), the red (41, 44), standing guards (46), sign-offs (48), evidence criterion (76), options weighed (88), backstop (187), red run (187). Proposed: the FINDING-739 question.

##### `cbc-framing/SKILL.md`

**FINDING-748.** rule 1; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 150): "At close, **check that each export reads alone**, then remove its". The section's subject, the three artifacts and where they go, arrives at line 171 after 20 lines on the residue filter and the commit order; a reader who stops after the first sentence has a check, not the point. Proposed: fix: open with lines 171-176, then the checks.

**FINDING-749.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` opening (line 11): "and ready). All paper — no code, no tech choices; the CBC Run's repo,". Three ideas in one sentence, chained by a dash and a semicolon (11-12); also 15-16 (three ideas), 17-18. Count 3. Proposed: fix: one sentence per idea.

**FINDING-750.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The mode — non-negotiable* (line 37): "**Delegated-verdict mode.** A CBC Run may hand these verdicts to the". The sentence runs 37-41, about 55 words, four ideas (who may delegate; through what record; naming what; the cost); also 41-44. Count 2. Proposed: fix: four sentences or a list.

**FINDING-751.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The derivation order* (line 60): "output. Upward corrections only as logged return trips (a census finding". The sentence (60-62) carries the rule, an example in parentheses and what is refused; also 59-60. Count 2. Proposed: fix: rule, example, refusal as three sentences.

**FINDING-752.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Per-stage gates* (line 76): "not an assumption inventory** — list what can hurt, never what you trust,". The sentence (75-81) runs about 55 words with three dashes nesting the two allowed blocks and a question inside one; also 66-70, 71-73, 83-86, 92-96. Count 5. Proposed: fix: one idea per sentence; the blocks as a list (FINDING-753).

**FINDING-753.** rule 3; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Per-stage gates* (line 77): "outside the two labelled blocks the workflow allows beside the facts:". The two blocks and the question one must answer are chained with dashes inside one sentence (77-81) where a two-item list would show them. Proposed: fix: a two-item list under the Stage 2 bullet.

**FINDING-754.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The record* (line 137): "3. **The escape valve:** a genuinely bulky mechanical sweep may". One sentence (137-141) with five qualifiers on one allowance; also 121-124. Count 2. Proposed: fix: "A bulky mechanical sweep may live in an appendix file beside the derivation. The file carries sweep output only, never decisions."

**FINDING-755.** rule 3; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The record* (line 143): "Where each record kind lives: framing verdicts — inline here; a". Three record kinds and their homes chained with dashes and semicolons (143-146). Proposed: fix: a three-line list.

**FINDING-756.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 159): "practice: **commit in derivation order** — the intent; the system". The sentence (158-165) runs about 65 words: five commits in order, the layer order inside one, a parenthesis, and why; others at 153-158, 165-169, 194-202, 207-209, 221-223, 230-234. Count 8. Proposed: fix: the commit order as a numbered list; one idea per sentence elsewhere.

**FINDING-757.** rule 3; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 178): "**The registry's outcomes** (what the file must carry, whatever its". Six outcomes chained with semicolons in one sentence (178-187). Proposed: fix: a numbered list of six.

**FINDING-758.** rule 5; uncertain. `delivery/method/.claude/skills/cbc-framing/SKILL.md` opening (line 11): "All paper — no code". "Paper" stands for documents; also 12 "the paper's home". Count 2. Proposed: fix: "Documents only, no code, no tech choices; they live in the CBC Run's repo"; or decline as a dead idiom.

**FINDING-759.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The mode — non-negotiable* (line 35): "Silence is the only forbidden channel." "Channel" is a figure for not writing something down; also 202 "Silent edits and stale claims are the same forbidden channel." and the workflow's line 66 (FINDING-787). Count 2 here. Proposed: fix: say what is forbidden: "Dropping one unwritten is the one thing not allowed."

**FINDING-760.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The derivation order* (line 60): "logged return trips". A journey figure for a logged revision of an earlier layer; 62 "polish passes" for a scheduled re-read. Count 2. Proposed: fix: "a logged revision of an earlier layer, never a scheduled re-read"; or decline if "return trip" becomes a Name (FINDING-775).

**FINDING-761.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Per-stage gates* (line 70): "intent is overloaded: force the choice. Bank rejected candidates." "Bank" stands for "record"; also 73 "they are debt stage 2 pays", 84 "park any mechanism the instant it surfaces", 89 "Name seams that fail the bar", 93 "Folds ride into the spec". Count 5. Proposed: fix: "Record rejected candidates", "stage 2 makes them exact", "set aside", "that fail the test", "Folds go into the spec".

**FINDING-762.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The record* (line 122): "nested beside the truth it". "The truth it earns" for the exports; 137 "**The escape valve:**" for the one allowed exception. Count 2. Proposed: fix: "beside the exports it leads to"; "The one exception:".

**FINDING-763.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 153): "false. The **residue filter** holds throughout: an export never". Coined figures: residue filter (153, 227), "the projected surface" (204), "a routing link" (220), "one click away" (222), "riders and flags ride the entry they guard" (183), "a named breach closes (intent's staging honesty)" (197). Count 7. Proposed: fix: say the rule each stands for ("an export never names the derivation's machinery or this skill"); for 197 say what a named breach and staging honesty are, or cut.

**FINDING-764.** rule 6; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 191): "(`.claude/rules/delivered-copies.md`, rule 8, *A Skill Template is". The italic title is the first half of rule 8's bold lead, "A Skill Template is copied and filled, never edited in place."; the same in the template's header, lines 6-7. Count 2. Proposed: question for the reviewer: is a shortened lead an exact reference; if not, quote it whole or keep "rule 8" alone.

**FINDING-765.** rule 6; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The record* (line 98): "## The record — the exports, and one derivation doc". The derivation record is named four ways: "derivation doc" (98, 154), "The derivation" (121), "The doc" (140), "the derivation record" (207); the three outputs are "artifacts" (9, 171; `system-readiness.md` 3, 11) and "exports" (98, 113, 150, 178). Proposed: fix: one name for each, used everywhere.

**FINDING-766.** rule 6; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The mode — non-negotiable* (line 25): "human works it with you. The hard rule, from the method itself:". The party who gives verdicts is "the human" (25, 28, 45; `cbc-slice/SKILL.md` 62, 98, 127, 207), "the user" (20, 230; `cbc-slice/SKILL.md` 224), "the reviewer" (template 11; `cbc-slice-workflow.md` 115; `slice-record.md` 57) and "the signer" (`cbc-slice/SKILL.md` 110; `cbc-slice-workflow.md` 117). Four words for one party. Proposed: fix: one word throughout.

**FINDING-767.** rule 6; uncertain. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 235): "begins only when the human signs off readiness; the cbc-slice skill will". A skill named bare where the glossary writes `cbc-slice` in backticks; also line 3 ("that is cbc-slice") and `cbc-slice/SKILL.md` line 3 ("that is cbc-framing"). Count 3. Proposed: question: do skill names take backticks in prose; if so, "the `cbc-slice` skill".

**FINDING-768.** rule 6; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 169): "is off-default: log why." A coined word defined nowhere and not in the glossary; also 224; "off-template" (189; template 3) is glossed by its colon. Count 3. Proposed: fix: "departs from the default: log why"; or a Name if kept.

**FINDING-769.** rule 7; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The mode — non-negotiable* (line 32): "stays human." "Every verdict stays human" (32) and "every verdict is the human's" (45) repeat line 28 "Every exit is the human's verdict."; line 35 restates 34 "recorded, never silently dropped". Count 3. Proposed: fix: say it once, at 28.

**FINDING-770.** rule 7; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 226): "status line), re-derived from the masters, never patched in place." The README rule is said at 205, 208-209 and 226; line 202 repeats 194. Count 3. Proposed: fix: say the rule once, at 205.

**FINDING-771.** rule 8; uncertain. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 183): "riders and flags ride the entry they guard; any". The reader meets "riders and flags" here with no plain words; the template (34-40) and the Registry Entry Shape define them later. Line 197 "claims — a named breach closes (intent's staging honesty), a": "staging honesty" occurs once in the whole delivery and is said in plain words nowhere. Count 2. Proposed: fix: "a rider (a condition the slice checks but never attacks) and a flag (an adversity that cannot be created the normal way) sit on the entry they concern"; for 197, say what is meant or cut.

**FINDING-772.** rule 9; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *The record* (line 100): "**The briefing comes first.** Framing opens by committing it,". "The briefing" where the Run Briefing, a Name in the CBC Run's glossary, is meant; also 104, 105; template 103, 105. Count 5. Proposed: fix: "The Run Briefing comes first", and so on.

**FINDING-773.** rule 9; checked. `delivery/method/.claude/skills/cbc-framing/SKILL.md` opening (line 16): "stage 0 and keep it open; this file is the operating rules, not a substitute.". A label inside its owner keeps its case, "Stage 0", as the file's own gates write it (66); lowercase at 16, 50-56 (7, in the code block), 73, 114-115 (3). Count 12. Proposed: fix: "Stage 0" throughout; or decline for the code-block table alone.

**FINDING-774.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` *Export and handoff* (line 206): "every claim on it has a master in `docs/system/`. A fact the". "Master" is given our meaning, the export that owns a fact, while the reader holds "Master Copy" as a Name meaning the Concept Deliverer's copy; the container's one-home rule calls this a fact's home. Also 209 (twice), 222, 223, 226; template 81. Count 7. Proposed: fix: "has its home in `docs/system/`", "a second home", "the home".

**FINDING-775.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-framing/SKILL.md` whole file (line 51): "hostage test; refusals in writing". Defined things with no Name: demonstration mode (30), delegated-verdict mode (37), hostage test (51, 71), mirror test (73), return trip (60, 201), fold-candidates (86), fold-reconciliation line (94), chosen-next (95), export (98), derivation doc (98), draft line (116), escape valve (137), residue filter (153), agent language (156), riders and flags (183), the written zero (186), logged revision entry (199), the bootstrap (231), the readiness checklist (233). About 20. Lines 107-111 say each thing framing defines gets its Name "when framing first uses it", which leaves the skill's own words unnamed while the skill is read. Proposed: the FINDING-739 question.

##### `cbc-framing/references/cbc-framing-workflow.md`

**FINDING-776.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` opening (line 8): "*When a stage's required output changes here,". One sentence (8-10) carries the rule, its reason and the ownership; 10-11 another. Count 2. Proposed: fix: three sentences: changes in the same commit; why; which file owns.

**FINDING-777.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *The order* (line 40): "— the promise is derivable on rough enemy *sketches*; the full census comes". Each inversion is one sentence of three ideas (39-41, 41-43). Count 2. Proposed: fix: one idea per sentence.

**FINDING-778.** rule 3; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *How the layers communicate* (line 50): "promise feeds the hostage test; the possessions feed the census scope;". Six handoffs chained with semicolons (49-53). Proposed: question: keep as one chain (one idea, each stage feeds the next) or list six.

**FINDING-779.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 0* (line 102): "real purpose is not a second promise — an intent carrying two is overloaded;". Three ideas in one sentence (101-103); also 99 (three imperatives with semicolons), 107-110, 111-113. Count 4. Proposed: fix: one idea per sentence.

**FINDING-780.** rule 3; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 0* (line 114): "- **What "done" demonstrably means, spelled out:** the named". Three parts (the adversity created; the witness never firing; the path followable) chained with dashes and commas in one sentence (114-117). Proposed: fix: three sub-lines.

**FINDING-781.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 1* (line 137): "sketch-debt. **Boundary note:** this is also where the edge lives — every". Three ideas in one sentence (137-138); also 127-130, 131-133. Count 3. Proposed: fix: split.

**FINDING-782.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 2* (line 168): "against it. Left unsaid, each slice answers it alone, and the". The sentence (168-170) carries four ideas with a dash and a colon; the section has about 20 such: 144-146, 147-149, 152-153, 156-158, 160-161, 163-166, 166-168, 172-190, 192-194, 194-196, 198-202, 203-207, 208-210, 212-215, 218-221, 223-224, 225-227, 234-236, 238-240, 241-246. Proposed: fix: rewrite the section one idea per sentence; the TODO item's plain rewrite covers it.

**FINDING-783.** rule 3; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 2* (line 173): "short block under its own label, **"The runtime ground"** — what the". One sentence from 172 to 186, about 150 words, holds the six items of the runtime ground chained with semicolons and dashes; the text counts them itself ("Six lines, not a design", 187). Also 218-221: four audit questions in one sentence. Count 2. Proposed: fix: a numbered list of six under the label; the audit checklist as four lines.

**FINDING-784.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 3*, *Stage 4*, *Stage 5* (line 258): "parked the instant they surface. Split two kills into two concerns only". Lines 258-260 carry the split rule and the dedupe rule with a parenthesis; also 260-263, 265-267, 276-278, 288-290, 290-293. Count 6. Proposed: fix: one idea per sentence.

**FINDING-785.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 6* (line 305): "1. **The sort.** Every concern stamped **theorem** (carries an". The sentence (305-311) runs about 60 words with two nested parentheses and a dash; also 311-313, 314-318, 320-323, 325-327, 337-340. Count 6. Proposed: fix: define theorem and definition in two sentences, then the rule.

**FINDING-786.** rule 4; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *The order* (line 39): "Two inversions, both tested: **LAYER-2-SYSTEM before LAYER-1-ENVIRONMENT**". "Tested" with no count of the framings that tested them; *Open* 344 "all lived framings" and 348 "every lived framing so far" where the count of CBC Runs framed exists. Count 3. Proposed: fix: "tested in N framings", "all N lived framings". Also Round 2's note, met in passing and held since: "all lived framings" (344) and "every lived framing so far" (348) were written before CBC Runs 4 to 6 framed, and nobody has checked them since (Stale lines).

**FINDING-787.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *The order* and *How the layers communicate* (line 41): "after and pays off the sketches. **LAYER-4-PROBLEMS before LAYER-3-AREAS**". A debt figure; also 54 "logged return trips", 57 "polish pass", 59 "Enemy-talk", 66 "Silence is the only forbidden channel." Count 5. Proposed: fix: "the census then makes the sketches exact"; "a logged revision"; "a scheduled re-read".

**FINDING-788.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 0* (line 97): "*Question: what claim is this project selling, and to whom?*". "Selling" and "sold to" (97, 107, 109) stand for "who the proof is for"; 112 "not a mood"; 121 "banked". Count 5. Proposed: fix: "what claim does this project make, and to whom does the proof matter"; "recorded".

**FINDING-789.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 1* (line 127): "The engine is the **hostage test**: for each candidate possession — *"if". "Engine"; 131 "sketch-enemies"; 132 "to power the test"; 133 "Those sketches are **debt**; stage 2 pays it."; 137 "sketch-debt", "where the edge lives". Count 6. Proposed: fix: "The test is: ..."; "rough enemies"; "stage 2 makes them exact"; decline "hostage test" only if it becomes a Name.

**FINDING-790.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 2* (line 203): "2. **The timeline stretched.** Run the film long, three questions:". A film figure; the section's others: "The trap" (151, 161), "an ally with guaranteed tools" (154), "The probe machinery — how saturation is earned" (192), "lens" (193-196, 208, 223-226), "re-scans the same territory" (195), "blind to" (196), "hunt" (198, 200), "stamp" (212-216), "in ink" (215, 231, 235), "ledgers" (231, 237, 248), "An unprobed door" (239), "another promise's territory" (244), "Hands up" (248). About 20. Proposed: fix: say the act: "a second way of scanning", "a written mark", "written down", "three lists"; decline lens, stamp and ledger only if they become Names.

**FINDING-791.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 3* (line 263): "kills and keeps none is the stage, not a victim — normal." The manual names this phrase as one to drop (`docs/conventions/writing/` §2, *Why each rule*, rule 5); also 258 "parked", 260 "Wording holes". Count 3. Proposed: fix: "A possession whose every fact is used by other kills, and that has none of its own, is normal."

**FINDING-792.** rule 5; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 6* (line 309): "adversity stages against it), with a written *because* per stamp". "Stage" as a verb for creating an adversity (309; 317 "stageable"), a theatre figure and a third sense of a word the group uses for a Skill Stage and the glossary for Delivery Staging; also `cbc-slice/SKILL.md` 95-96 (2), `registry-entry.md` 36, 42, template 36, 39. Count 8 in 4 files. Proposed: fix: "create", the verb the skills use elsewhere: "no adversity to create against it", "cannot be created the normal way".

**FINDING-793.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 4*, *Stage 5*, *Open* (line 277): "the bar, name it and refuse to draw it — a noted-not-drawn seam is better". "Fails the bar"; 292 "consistency at the joints"; 342 "settled by living"; 344 "a genuinely raw itch" (and 18 "an itch"). Count 5. Proposed: fix: "fails the test", "consistency across the seams", "a raw idea".

**FINDING-794.** rule 6; uncertain. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 2* (line 246): "verdicts follow the mode's rule on who decides." "The mode" points at `SKILL.md`'s section *The mode — non-negotiable* by a reworded label and no path. Proposed: fix: "(`.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*)".

**FINDING-795.** rule 6; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 2* (line 219): "out-deriving him: did each line get the assumption question? was". Coined words defined nowhere: "out-deriving" (219), "framer" (9, 218), "near-miss's doubt" (310), "censused-and-fenced" (245), "noted-not-drawn" (277), "theorem-shaped" (312), "stageable" (317). Count 7. Proposed: fix: plain words: "without deriving it again himself"; "the agent framing".

**FINDING-796.** rule 7; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *How the layers communicate* (line 66): "silence. Silence is the only forbidden channel." Restates 65-66 "recorded, never dropped in silence"; the whole rule 4 (64-66) is `SKILL.md` 33-35 again. Proposed: fix: cut the last sentence; keep the rule in one file and point from the other.

**FINDING-797.** rule 8; uncertain. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` *Stage 2* (line 188): "design. The ground's readiness check reads this block first; a". Names `system-readiness.md` with no path or plain words, to a reader at Stage 2 who has not met cbc-slice; 190 "lived twice" is a count with no plain words for what was lived. Count 2. Proposed: fix: "the readiness check before slicing (`.claude/skills/cbc-slice/references/system-readiness.md`)"; "two CBC Runs left it out and wrote it later".

**FINDING-798.** rule 9; checked. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` whole file (line 55): "census (stage 2) may reveal a missed possession or an unwritten refusal —". "Stage n" lowercase inside its owner; also 30-36 (7, code block), 80-87 (7, table), 91, 133, 235, 286, 311; while 327 "Stage 6's deliverable" and the headings keep the capital. Count 20. Proposed: fix: "Stage 2" throughout.

**FINDING-799.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` whole file (line 80): "| a possession (stage 1) | POSSESSION-<n> | POSSESSION-4 |". Defined things with no Name: tag (72), possession (80), fact (81), trust assumption (82), fence (83), scope verdict (84), hostage test (127), mirror (129), sketch-enemies (131), the three negations (146), the trap (151), the runtime ground (173), probe (193), lens (195), the assumption hunt (198), silent singulars and successes (200-201), the three-stamp rule (212), the audit checklist (218), saturation (223), the probe log (225), the fence list (233), the not-probed ledger (237), the scope verdicts (241), concern (258), fold-candidate (262), theorem and definition (305-308), the sort, the dedupe, the folds (305-320), presumption order (325). About 30. Proposed: the FINDING-739 question.

##### `cbc-framing/references/the-whole-system-in-plain.md`

**FINDING-800.** rule 1; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md` *The one idea* (line 15): "Most software is designed by asking "what should it do?" and listing". The point, ask "what must never happen?" first, arrives in the second sentence after a contrast. Proposed: fix: open with the method's question, then the contrast; or decline as a teaching page.

**FINDING-801.** rule 2; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md` opening (line 8): "**What this is, in one sentence:** a design discipline that derives a". The one sentence (8-11) chains three ideas with two dashes, by design; also 18-19, 20-22. Count 3. Proposed: question: keep the one-sentence form, or let it be three.

**FINDING-802.** rule 3; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md` *How it rots* (line 89): "New features shipping without re-checking the guarantees. An admin script". Four ways in one paragraph without labels under a heading that says "watch for these"; *Working one slice* (71-76) has four stages labelled in bold inside one paragraph. Count 2. Proposed: fix: four bullets each.

**FINDING-803.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md` *The order of work* (line 62): "5. **Check between owners** (LAYER-5-INTERACTION) — only if stage 4". "Stage 4" lowercase in a list the page says matches the workflows "stage for stage" (67). Proposed: fix: "Stage 4"; or "step 4" if the list's own numbers are meant.

##### `references/worked-example.md` (both copies)

**FINDING-804.** rule 3; checked. `delivery/method/.claude/skills/cbc-framing/references/worked-example.md` and `delivery/method/.claude/skills/cbc-slice/references/worked-example.md` *Stage 0* (line 28): "Done, demonstrably: identical submissions genuinely fired at once and". Three parts chained with semicolons and nested dashes (28-31); also *Stage 2* 77-81 (three probes in one sentence), 83-89 (the runtime ground's six items in one sentence), *Part 2* 223-229 (four guarantees in one bullet), 230-234 (three criteria), 236-241 (four owners in one sentence). Count 6. Proposed: fix: lists where the count matters: the three "done" parts, six ground items, four guarantees, four owners.

**FINDING-805.** rule 2; checked. Both `worked-example.md` paths, *Stage 0* (line 26): "Falsifiable: the breaking scenario is concrete — a timeout retry creates". Also 23-25, 46-48, 60-62, 156-157, 158-160, 186-189, 195-196, 242-245, 247-250. Count 10. Proposed: fix: one idea per sentence.

**FINDING-806.** rule 5; resting on the reader. Both `worked-example.md` paths, *Stage 0* (line 14): "Idea brought to the walk: "a backend where shops submit customer orders."". "The walk" for the framing session (`SKILL.md` 30 "A first-time walker"); 16 "banked"; 46 "debt for stage 2"; 244 "a hand at the store's console"; 268 "the zero-translation handoff". Count 5. Proposed: fix: "Idea brought to the framing", "recorded", "someone at the store's console".

**FINDING-807.** rule 9; checked. Both `worked-example.md` paths, *Stage 1* (line 46): "Sketch-enemies used (debt for stage 2): a retrying caller, a store that". "Stage n" lowercase inside its owner; also 172, 265, 267, 269; the stage labels "**specify-correctness**", "**plan**", "**build**", "**document**" (216, 236, 247, 256) in bold lowercase. Count 9. Proposed: fix: "Stage 2"; "Stage 1, specify-correctness".

**FINDING-808.** rule 9; resting on the reader. Both `worked-example.md` paths, whole file (line 178): "Operational test — two kills are two slices only if their evidence must". Defined things with no Name: the walk (14), the ledgers (94), fold-candidate (158), operational test (178), guarantee challenge (223), evidence criteria (230), escape-hatch hunt (242), the wall's own check (253), evidence-closed (259). Proposed: the FINDING-739 question.

##### `cbc-framing/templates/registry.md`

**FINDING-809.** rule 5; checked. `delivery/method/.claude/skills/cbc-framing/templates/registry.md` group heading (line 24): "one group share a kind of storm (or a stage), nothing more.>". "Storm" for an adversity class; "a version stage" (22) is a third sense of "stage". Count 2 (34 "battle-tested" is in FINDING-743). Proposed: fix: "share an adversity class (or a version), nothing more".

**FINDING-810.** rule 2; checked. `delivery/method/.claude/skills/cbc-framing/templates/registry.md` SLICE-1 entry (line 36): "- **Flag riding:** <what cannot be staged the normal way — name the". The slot's guidance (36-40) runs about 45 words, four ideas chained with dashes and semicolons; also 11-14, 78-83, 98-101. Count 4. Proposed: fix: two short sentences: what the flag is; what the slice does with it.

##### `cbc-slice/SKILL.md`

**FINDING-811.** rule 3; checked. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Stage 3 — build* (line 178): "**Gate: every guarantee has an adversity-creating test, all pass,". The gate is one sentence of six conditions (178-181); the *Stage 4* gate (209-214) chains three with semicolons. Count 2. Proposed: fix: a numbered list of conditions under each gate.

**FINDING-812.** rule 2; resting on the reader. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Stage 3 — build* (line 154): "- A race whose red needs its window held open (a pause added so". One sentence (154-156) with a nested parenthesis and two rulings (where the pause goes; the record says so). Count 1. Proposed: fix: "A race may need a pause so the interleaving it is named for happens. The pause lives on the red tree only, and the record says so."

**FINDING-813.** rule 5; resting on the reader. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Standing guards* (line 225): "guarantee erosion, testing theater, escape-hatch watch". "Testing theater" is a theatre figure and "erosion" a figure, as names of two guards; also 149 "plant the violation it forbids", 182 "is not known to be watching"; the workflow's 208 "Guarantee erosion", 211 "Testing theater", 177 "on display", 227 "front-load a schema". Count 9 in 2 files. Proposed: fix: name the guards by what they watch ("a wall weakened to a test"; "a feature touching the state"; "a new path around the wall"); or decline if the three become Names.

**FINDING-814.** rule 6; uncertain. `delivery/method/.claude/skills/cbc-slice/SKILL.md` opening (line 29): "`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, "The slice's record".". The heading is "The slice's record — its outline" (workflow 32); line 226 ""Standing guards"" for "Standing guards (after the slice closes)" (workflow 206). Count 2. Proposed: fix: quote each heading whole; or retitle the headings to their subjects (FINDING-827).

**FINDING-815.** rule 6; resting on the reader. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Stage 4 — document* (line 184): "## Stage 4 — document". The Skill Stages are named specify-correctness, plan, build, document (23, 65, 100, 129, 184), and elsewhere "the specification" (75, 190), "the spec" (92-98), "the close" (191; workflow 54, 179; `slice-record.md` 55-57), "Specify" and "Document" (`the-whole-system-in-plain.md` 71-75). Stage 4 is "document" by name and "the close" by event. About 12 in 5 files. Proposed: question: one name per stage in every file; is Stage 4 "document" or "close"?

**FINDING-816.** rule 6; uncertain. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Stage 4 — document* (line 189): "2. **Close the slice in the registry** as evidence-closed. The row". The registry's status value is "closed (date, evidence)" (`cbc-framing/SKILL.md` 182; template 18; `registry-entry.md` 72); "evidence-closed" (here; worked example 259; template 73) is a second spelling. Count 3. Proposed: fix: "as `closed (date, evidence)`".

**FINDING-817.** rule 8; checked. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Stage 3 — build* (line 157): "- For each wall removed, note whether its backstop was seen". "Backstop" is first met here with no plain words saying what it is, and is said nowhere in the group (`slice-record.md` 187-189, 219; workflow 150-152 use it; the shape's slot at 84 says "what stands behind it" without the word); 155 "the red tree" is first met here, inferable from 141-142. Count 2 here, 7 in 3 files. Proposed: fix: at 157, "its backstop, what stands behind the wall if the wall is wrong, was seen"; at 155, "the red tree, the working tree with the wall absent".

**FINDING-818.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-slice/SKILL.md` *Stage 4 — document* (line 198): "rows in ARCHITECTURE's Invariants table,** as its header comment". A path written short: "ARCHITECTURE" for `ARCHITECTURE.md` (198, 211; workflow 188, where 191 writes it whole). Count 3. Proposed: fix: "`ARCHITECTURE.md`'s Invariants table".

**FINDING-819.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-slice/SKILL.md` whole file (line 166): "- A **tripwire** guards a decided option, not the promise, and". Defined things with no Name: readiness gate (31), guarantee challenge (79), strategy-free guarantee (81), evidence criterion (83), flag (94), structural owner (102), red tree (155), backstop (157), tripwire (166), the wall's own check (169), provisionals (192), hand-ons (210), the three standing guards (225). Proposed: the FINDING-739 question.

##### `cbc-slice/references/cbc-slice-workflow.md`

**FINDING-820.** rule 2; resting on the reader. `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` *Stage 1 — why, and an example* (line 89): "this workflow forbids. An ADR for it stays Proposed until the close". The sentence (89-91) carries the rule, its reason and a contrast; also 179-181, 208-210, 211-214. Count 4. Proposed: fix: split.

**FINDING-821.** rule 3; resting on the reader. `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` *Stage 4 — why* (line 182): "of what a close hands on: a wall that already holds part of a later". Three examples chained with semicolons (181-184). Proposed: fix: three bullets.

**FINDING-822.** rule 6; checked. `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` *The slice's record — its outline* (line 36): "per guarantee. The Slice Record Shape, in `.claude/shapes/`, adds to". The Name is written "Slice Record Shape" here, at 194 and as `slice-record.md`'s title (line 5), while `docs/glossary.md` line 127 writes "the Slice-Record Shape". One side is inexact. Proposed: question: which spelling; fix the other side in the same commit.

**FINDING-823.** rule 9; resting on the reader. `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` whole file (line 47): "the opening, where something was". Defined things with no Name: the opening (47; `cbc-slice/SKILL.md` 74), the close (54), correctness spec (103), adversity model (104), red tree (147), backstop (150), tripwire (159), the wall's own check (166), working defaults (218). Proposed: the FINDING-739 question.

##### `cbc-slice/references/system-readiness.md`

**FINDING-824.** rule 2; checked. `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md` *READINESS-4* (line 51): "Only this slice's class is required — a later slice's class is checked at". Three ideas in one sentence (51-53); also 3-7 (2), 25-27, 65-67, 69-70, 74-76, 80-83. Count 8. Proposed: fix: one idea per sentence.

**FINDING-825.** rule 5; checked. `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md` *READINESS-2* (line 26): "already run; fighting the toolchain mid-slice pollutes the record with". "Fighting", "pollutes", "noise"; 53 "is ceremony"; 72 "record surfaces". Count 5. Proposed: fix: "toolchain problems met mid-slice fill the record with lines that are not method feedback"; "is an empty check"; "The CBC Run's records exist".

**FINDING-826.** rule 10; uncertain. `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md` (line 9): "## READINESS-1 — The framing artifacts are in the repo". Six tag-numbered sections whose titles are statements after a dash (9, 19, 29, 39, 59, 72), the longest 59 characters (39). Rule 10's letter names `## 3.` and `### 3.2`. Proposed: question: is a tag-numbered section a numbered section under rule 10; if so, retitle each to its subject.

##### Across the group

**FINDING-827.** rule 10; uncertain. `delivery/method/.claude/skills/cbc-framing/SKILL.md` (line 22): "## The mode — non-negotiable". Unnumbered headings carry a gloss after a dash, colon or parenthesis, or are statements: `cbc-framing/SKILL.md` 7, 22, 47, 64, 98; `cbc-framing-workflow.md` 1, 23, 70, 342; `the-whole-system-in-plain.md` 24, 43, 78, 87, 94; `worked-example.md` 10, 214 ("# Part 1 — the framing", numbered parts), 200, 263; template 9, 96, 103; `cbc-slice/SKILL.md` 7, 216, 222; `cbc-slice-workflow.md` 1, 32, 206; `system-readiness.md` 1. Count 27. Rule 10 reaches numbered sections only; the references at `cbc-slice/SKILL.md` 29 and 226 already drop these glosses, which is what the manual's reason for rule 10 predicts. Proposed: question: does rule 10 reach unnumbered headings in skills and references; if so, retitle them to subjects.

##### `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md

**FINDING-828.** rule 2; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` frontmatter (line 3): "Bootstrap a framed project's system on an established ground - decide the stack and the bootstrap set at capability-and-constraint grain, compose a requirements document, implement an empty-but-running skeleton wired to the real services, and prove an evidence harness creates one named adversity end to end." Rule 2 asks one idea per sentence; the description chains four outcomes, then three more sentences with dashes. The same at `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` line 3 and `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` line 3. Question: is a skill description's form settled (one paragraph for the trigger), so it rests outside the rule?

**FINDING-829.** rule 1; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *The seam you must keep — WHAT before HOW* (line 16): "This skill was distilled from a two-seat discipline: one seat decides **what** is being bootstrapped and under which constraints; another decides **how** it is realized in code." The point, that Stages 1–2 name no mechanism and Stage 4 decides the code, arrives at line 20 after the origin story. Proposed: lead with the boundary; the origin goes last or out.

**FINDING-830.** rule 5; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *The seam you must keep* (lines 14, 16, 18, 26): "Never let a mechanism chosen early masquerade as a requirement." Figures: "seam" (14, 18), "two-seat discipline" (16), "distilled" (16), "masquerade" (26). 5 instances. Proposed: "The boundary you must keep: what before how"; "two roles"; "written from"; "pass for a requirement".

**FINDING-831.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, opening and *The seam you must keep* (lines 9–12, 26–29, 31–34): "One run, one exit: ***system bootstrapped*** — stack settled, an empty-but-running skeleton wired to the real, already-established ground, and an evidence harness proven able to **create** one named adversity end to end." Three outcomes chained with dashes in one sentence; 2 more: 26–29, 32–34. Proposed: one sentence per idea; the three outcomes as a list.

**FINDING-832.** rule 9; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, opening (line 9): "***system bootstrapped***"; also `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` line 3: "the *system bootstrapped* step". A Markdown mark marks what reads as a defined milestone; it is in neither glossary and not in the concept. Question: a defined thing (then a Name, unmarked, in the glossary) or English (then unmarked)?

**FINDING-833.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 0 — readiness check* (lines 49–53): "Then **verify the ground live** per the operator manual before any wiring — records prove it *was* verified; the wiring needs it up *now*." 1 more: 52–53. Proposed: "Verify the ground live before wiring. The records say it was verified; the wiring needs it up now."

**FINDING-834.** rule 5; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 0* (lines 52–53): "Record the receipt: what stood, what was checked, any observations. Not a blocker-hunt — observations ride the record; only a missing member stops." "receipt" and "blocker-hunt" stand for a record of what was checked and a search for blockers ("ride" is FINDING-912). 2 instances. Proposed: "Record what stood, what was checked and what was noticed. Only a missing member stops; a note goes in the record."

**FINDING-835.** rule 3; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 1 — decide* (lines 62–65): "Record the decision **in the project's log before any code exists**, including: the migration tool stays outside the app; the app knows one identity (the runtime role); the migrations home confirmed." Three parts in one sentence with semicolons; the same shape in the capability set (84–91, four parts), the constraints (92–96, four parts) and the exclusions (97–106, six parts). 4 instances. Proposed: a sub-list under each bold lead.

**FINDING-836.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 1* (lines 59–80, 97–106): "Read, too, **from how many instances** the adversity comes: the definition's runtime ground says whether the system runs as more than one instance, and if it does, a single-process pass proves a shape nobody runs — the proof must cross the process boundary (the stack walkthrough's step 5)." Four ideas in one sentence; 4 more: 59–61, 68–69, 75–80, 101–106 (one sentence of 70 words). Proposed: one sentence per idea.

**FINDING-837.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 2 — compose the requirements document* (lines 112–114, 120–125, 126–128): "Write `bootstrap-requirements.md` at the path the project's records choose — beside the builder's other manuals; both lived CBC Runs put it at `docs/construction/` — in the project's language:" Three ideas with dashes and a semicolon; 2 more: 120–125 (§4), 126–128 (§5). Proposed: split.

**FINDING-838.** rule 3; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 5 — certify and close* (lines 186–191): "§1 identity exact; §2 all capabilities present **and bounded** (probe carries no business meaning and is documented to die at the first slice); §3 all constraints visible in the delivered files (runtime identity alone in config, password from environment, deliberate absences commented, nothing structure-controlling on the runtime path, migrations home honestly empty, nothing ahead of need); §6 exclusions respected." Four checks and six sub-checks in one sentence; the same at 181–185 (§5, nested parentheses) and 193–195 (five records in one sentence). 3 instances. Proposed: one line per check.

**FINDING-839.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 5* (lines 197–213): "What a slice may rely on from now on is ARCHITECTURE's, so the close writes its components as they stand: the store, the application, the harness, each with what a slice may rely on and the ADR that shaped it." 3 more: 197–198, 206–209, 210–213. Proposed: split.

**FINDING-840.** rule 5; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 5* (line 212): "container stays, direction goes — and they arrive now because the harness is real." The phrase says nothing on its own; also "project into the README" (206) and "no banner listing what changed since" (198). The same phrase in `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` line 154: "ships without the section — container stays, direction goes — and the section arrives now because this gate made it true." 4 instances. Proposed: "The container's README has no Run or Test section, because the container is the same for every CBC Run and these sections say what this one built."

**FINDING-841.** rule 6; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 5* (line 199): "may rely on from now on is ARCHITECTURE's". The file is `ARCHITECTURE.md`; rule 9 writes a path as it is. Proposed: "`ARCHITECTURE.md`'s".

##### `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md

**FINDING-842.** rule 8; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, header comment (line 1): "A reference on CBC ADR-0008's imitated side: a decision surface, nothing to paste or fill." "imitated side" rests on an ADR the CBC Run cannot open; the harness reference says it in words (its lines 24–26). Proposed: "A reference: read and imitated, never copied and filled."

**FINDING-843.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, opening (lines 6–14): "This doc carries the lived default, the decision rule, and the vocabulary of the named alternatives — so the choice is conscious, recallable months later, and means the same thing to the person and the agent." 2 more: 6–9, 9–11. Proposed: split.

**FINDING-844.** rule 5; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, opening, *The lived default*, *The vocabulary*, *What this doc does not carry* (lines 1, 4, 31, 96, 105): "of choice, and they would stale; the two lines above are for". "would stale" is a verb English does not have; "decision surface" (1, 4; also `spring-boot-walkthrough.md` line 25), "storms" (31; also `spring-harness-reference.md` line 410 "What weakens the storm"), "The default's nearest kin" (96; also `establishment-walk.md` line 60 "`compose.yaml` and its kin"). 8 instances. Proposed: "would go stale"; "the choices"; "bursts"; "nearest to the default"; "the other ground files".

**FINDING-845.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The lived default* (lines 39–61): "**Depth is earned per feature, never stamped.** A feature starts as few classes as its slice demands (one lived feature: a controller and a domain class); an internal service or persistence split appears inside one feature when that feature's own complexity earns it, and appears nowhere else." 2 more: 42–46, 53–57. Proposed: split.

**FINDING-846.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The decision rule* (lines 67–79): "the slices rarely discriminate between structures, so the deciding inputs are the CBC Run's own — fluency, audience, and a stated intent (*"this CBC Run practices pattern X"* is a legitimate deciding input when it is written down)." 2 more: 72–76, 77–79. Proposed: split.

**FINDING-847.** rule 8; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The decision rule* (line 74): "and the rest is (`.claude/rules/delivered-copies.md`, rule 8, *A Skill Template is copied and filled*)." The sentence ends in a Fact Reference standing for what the rule says and does not say it. The same form at `spring-boot-walkthrough.md` line 15 ("from the outcomes here, and the rest is") and `postgres-setup-walkthrough.md` line 21. 3 instances. Proposed: "record the deviation, as delivered-copies rule 8 says (…)".

**FINDING-848.** rule 8; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The decision rule* (line 78): "entry below stops being vocabulary and gains a harvest line." "harvest" is this repo's word (Record Harvest); the CBC Run's glossary has no entry. Also `spring-harness-reference.md` line 457: "deviation, expect it to harvest." 2 instances. Proposed: "comes back into this doc with a later delivery"; "expect the deviation to come back as a change to this file".

**FINDING-849.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The vocabulary* and *What this doc does not carry* (lines 85–100, 104–109): "- **Classic layered** *(unlived here)* — packages by technical role (`controller/`, `service/`, `repository/`); a request flows down the layers. The long-standing enterprise default; every class public across layer packages, so the boundaries are convention." Each of the four entries chains two or three ideas with semicolons (85–88, 89–93, 94–96, 97–100); 104–106 and 107–109 the same. 6 instances. Proposed: the two lines each entry is allowed as two sentences.

**FINDING-850.** rule 6; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *What this doc does not carry* (line 107): "- **Application code** — the executor's, always (CBC ADR-0008); the". "executor" is a coined role word, in neither glossary and defined nowhere in the shipped files; also `spring-harness-reference.md` lines 23, 427, 470. 4 instances. Proposed: "the CBC Run's".

##### `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md

**FINDING-851.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, opening (lines 3–19): "Stack line: **Spring Boot 4.x · Java 21 · Maven**, on an established PostgreSQL ground under a role split (`<project>_migrator` / `<project>_runtime`), migrations home `infrastructure/flyway/migrations/` (empty), rootless podman as the container runtime." Four facts in one sentence; 3 more: 11–13, 14–17, 18–19. Proposed: the stack line as a list of five.

**FINDING-852.** rule 5; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, opening (line 18): "Governing principle at every tier: *something outside the app migrates; the app runs.*" "tier" is undefined here; `spring-harness-reference.md` uses it for the layered test bases (lines 40, 162) and `postgres-role-split.md` for a database-owner role (line 43). 4 instances, three senses. Proposed: "in the ground and in the harness alike"; "the web-plus-database base"; "a database-owner role".

**FINDING-853.** rule 3; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §1 (lines 23–28): "Before any code, the project's log carries: the stack; the application structure, decided against the lived default — `.claude/skills/cbc-bootstrap/references/app-structure.md` beside this walkthrough is the decision surface, and deviating from its default is a logged off-default decision; Flyway staying outside the app (no migrator credentials in any profile); the migrations home confirmed." Four parts chained with semicolons. Proposed: a list of four.

**FINDING-854.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §2 (lines 37–42, 50–51, 54–59): "root** — beside the infrastructure dirs. Never overwrite: each hygiene file takes its Stack Overlay below the marked line it carries — `.gitignore` (build output, IDE, OS, log sets), `.gitattributes` (wrapper line endings: shell wrapper LF, cmd wrapper CRLF), `.editorconfig` — and `README.md` is kept." 3 more: 50–51 (three checks chained), 54–57, 58–59. Proposed: split; the three files as a list.

**FINDING-855.** rule 8; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §2 (line 37): "- Initialize to the identity fields and **extract into the existing repo". The reader meets Spring Initializr here unnamed; it is named only at line 56 ("Initializr on Boot 4 already emits both"). Proposed: "Generate the skeleton with Spring Initializr from the identity fields, and extract…".

**FINDING-856.** rule 6; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §2 (line 48): "- Pom written per the pom convention (sibling reference)." A sibling file named by a nickname where the file's other pointers are paths. The same: "the harness reference" (`app-structure.md` 36, 108), "the stack walkthrough" (`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 74, 138), "the walkthrough reference" (`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 33), "the setup walkthrough" (`postgres-role-split.md` 6), "(walkthrough, step 4)" (`spring-harness-reference.md` 47, 164, 202, 288). 10 instances. Proposed: the path once per section, then the short name; or decline, since each file's opening names its siblings by path.

**FINDING-857.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §3 (lines 63–65, 69–72, 75–78, 80–82, 84–95): "same fact, lived: started with nothing exported, the app *starts* — Boot's configuration binding leaves an unresolvable `${VAR}` as the literal string, so the literal becomes the password; the store logs `password authentication failed`, health answers DOWN with the db component DOWN, and nothing else says so." Six ideas in one sentence; 6 more: 63–65, 69–72 (three absences chained with semicolons), 75–78, 80–82, 89–92, 92–95. Proposed: split; the three absences as a list.

**FINDING-858.** rule 5; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §2–§4 (lines 56, 84, 99, 106): "comment). Initializr on Boot 4 already emits both, so the trap bites". "bites"; "The flip side of the same fact" (84); "operator-manual territory" (99; also `testcontainers.properties` line 7 and `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` line 49 "the framing job's territory"); "a long "no valid Docker environment" hunt" (106). 6 instances. Proposed: "the trap is met when"; "The same fact, seen the other way"; "the operator manual's"; "the framing's work"; "a long search".

**FINDING-859.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §4, *The test runtime* (lines 108–118): "If Ryuk fails on a host, the switch is `TESTCONTAINERS_RYUK_DISABLED=true` in the environment, never a properties line; a hard-killed test JVM can then strand a throwaway — `podman ps` shows it by image (`postgres:<major>` with a random name, and `testcontainers/ryuk`); remove those and only those with `podman rm -f <name>`." Four ideas; 2 more: 108–111, 111–112. Proposed: trap 2 as three numbered facts.

**FINDING-860.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §4, *The harness in the codebase* (lines 126–133, 149–153, 155–158, 165–170, 174–175): "- **Test-scope capabilities only**: drive a real PostgreSQL container from tests; integrate with the Spring test context; run migrations **harness-side**." Three capabilities chained; then "On Boot 4 the engine enters, not Boot's Flyway module: the engine alone runs no auto-configuration, so the harness's own call is the only migration path" (129–131); 4 more: 149–153, 155–158, 165–170 (trap 2), 174–175. Proposed: split; the three capabilities as a list.

**FINDING-861.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §5 (lines 188–192, 196–205): "is then **N ≥ 2 instances of the system as separate processes** against one store, each addressed through its own door, requests released at one instant across all of them, every response asserted, and the witness read from the store from outside — never through an instance." Five parts in one sentence; 2 more: 188–191, 196–199. Proposed: the five parts as a list.

**FINDING-862.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §5, *Lived realization (once)* (lines 207–227): one paragraph of 8 sentences, each with two to five ideas chained with dashes and semicolons, as at line 217: "started with the three environment facts a real instance gets — the store's port, the runtime password, its own listen port — and nothing else from the harness; its output goes to a log file under `target/`." Lines 207–213, 214–219, 220–225, 224–227. Proposed: a labelled list: what is forked; what each instance gets; how "up" is read; who owns the lifecycle; what the probe answers.

**FINDING-863.** rule 7; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *Recall list — the traps compressed* (lines 237–261): "4. `~/.testcontainers.properties` binds only from `$HOME`." Each of the 11 items restates a trap already bold-led where it stands (item 4 repeats lines 105–106). The list says it is a summary, as one-home rule 3 asks. Question: keep as the reader's checklist, or cut?

##### `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md

**FINDING-864.** rule 3; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, opening (lines 10–16): "The *outcomes* these files satisfy are `.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`'s, steps 4 and 5; what enters the build and how each entry is written is `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`'s; the machine setup that makes containers reachable is the project's operator manual's." Three owners in one sentence. Proposed: a list of three.

**FINDING-865.** rule 1; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, opening (line 18): "**Why code exists here at all.** The walkthrough deliberately carries none: two projects may end with different code for the same thing." The answer, "This file exists to make that read unnecessary" (lines 23–24), arrives fourth, after the reasons. Proposed: lead with "This file carries code so that no CBC Run reads the last CBC Run's source."

**FINDING-866.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, opening (lines 20–27): "That holds for the application and does not hold for these five, which are shaped by the stack and the harness outcomes rather than by the problem — three projects produced them near-identically, and each executor's only route was reading the previous project's source." Four ideas; 1 more: 24–27. Proposed: split.

**FINDING-867.** rule 5; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, whole file (lines 39, 74, 130, 158, 177, 205, 255, 275, 278, 408, 458, 467): " * The container is a faithful miniature of the ground: the same image". "miniature" for the test container (39, 74, 130, 205, 255, 275, 278: 7), "reopen that door" (158), "travel the real door" (177), "that is the law here" (408), "The missing-home hole" (458), "a knob, not a law" (467). 12 instances. Proposed: "a copy of the ground, set up by the same SQL"; "would add a second migration path"; "cross the boundary"; "the rule"; "the missing-home gap"; "a number to choose, not a rule".

**FINDING-868.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §1, *The database base* (lines 47–56, 74–82, 123–158): "**Outcomes it realizes** (walkthrough, step 4): one PostgreSQL container of the ground's major version per test JVM, started once and shared, its lifecycle explicitly the harness's own; migration run **harness-side, immediately after the container starts and before any application context boots**, pointed at the **one migrations home on the filesystem**, never a classpath copy — and, the third pass's correction, **the ground's authority split held in evidence runs**: the container is initialized by the SAME bootstrap SQL the ground uses, migration runs as the migrator identity, and the application context connects as runtime alone." One sentence of 100 words carrying four outcomes; 5 more: javadoc 74–78, 123–127, 128–132, 135–137, 153–157. Proposed: the outcomes as a list of four; one sentence per idea in the javadoc and the bound facts.

**FINDING-869.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §2, *The evidence tier* (lines 176–179, 193–198): "2. The bases stay lean — no shared protected fields; a test autowires what it uses (`JdbcClient`, `TestRestTemplate`), so attacking through the door and inspecting persisted state directly are both one line away." 2 more: javadoc 176–179, 196–198. Proposed: split.

**FINDING-870.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §3, *The migration-path test* (lines 202–205, 219–223, 267–271, 278–284): "**Outcome** (step 4): the migration path **proven, not assumed** — and, riding on it, the connection identity asserted and the authority split witnessed: the runtime identity cannot change structure in the miniature, refused with the ground's own message." 4 more: javadoc 219–222, 267–271, 278–281, 281–284. Proposed: split.

**FINDING-871.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §4, *The probe pair* (lines 288–294, 351–354, 403–406, 407–411, 417–423): "**Outcomes** (step 5): one **probe endpoint** in the main source doing a real round-trip as the runtime identity, documented as scaffolding that dies when the first real slice lands; and a **contention probe test** — many requests held at a barrier and released at one instant, each a full HTTP → application → real-PostgreSQL round-trip through the same door a real caller uses, every response asserted." 4 more: javadoc 351–354, 403–406, 407–411, 419–423. Proposed: the two outcomes as two paragraphs; split the rest.

**FINDING-872.** rule 3; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §6, *The variation points*, item 8 (lines 473–494): "it: the container and the migration lifted out of the database base into a **store holder** of their own, so a test with no application context shares the store — the base keeps only the datasource override, and the layering is the two bases plus the holder; a **process helper** that starts one instance of the build's own output on a free port against the holder's store, waits for its door to answer UP with the store's component UP, and stops it on close; the **probe answering its process id** beside the identity, so the race asserts the pids served are exactly the instances started; and the **race test running no Spring context of its own**, the requests released at one instant round-robin across the instances, the witness read from the store as the runtime identity while the instances are still up." Four parts in one sentence of 120 words; item 9 (495–507) chains three parts the same way. 2 instances. Proposed: numbered sub-lists.

**FINDING-873.** rule 1; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §6, item 9 (line 495): "9. **How the evidence asserts on a body** is a stack convention this file left unsaid, so each CBC Run decided by habit." The convention, by path and never by substring, arrives in the third sentence after the history. Proposed: lead with "A body is asserted by path, never by substring."

**FINDING-874.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` §6 (lines 451–464): "here are the establishment's coupling (`bootstrap.sql` ↔ `.env.example`) carried into the harness, and they keep the suite self-contained — no environment set, no ground up." 3 more: 454–457, 458–461, 461–464. Proposed: split.

##### `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-pom-convention.md

**FINDING-875.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-pom-convention.md` (lines 3–5, 9–13, 20–23, 24–27, 42–45): "deliberately small; the harness, the driver, and every later library arrive at their own commits, each with its earning reason live in the file." 4 more: 3–5, 20–23, 24–27, 42–45. Proposed: split.

**FINDING-876.** rule 5; uncertain. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`, *Every entry carries its why* (line 21): "capability it buys in the project's own terms — what the system does with". "buys"; "a provisioning wishlist" (10); "each capability's story" (40). 3 instances, near-dead. Proposed: "gives"; "a list of what might be needed"; "the dependencies of one capability".

##### `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates

**FINDING-877.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/readme-run-test.md`, header comment (lines 6–10): "line joins the Prerequisites section infra-establish opened; the command bodies are the lived Spring/Maven shape — a different stack writes its own, keeping the shape: Run stands the ground up and ends in a proof of life; Test is the one standard test command, with what it really drives stated beside it." Five ideas in one sentence. Proposed: split; the two sections' shape as two lines.

**FINDING-878.** rule 2; checked. `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/testcontainers.properties`, header (lines 2–8): "# ~/.testcontainers.properties and fill — it binds ONLY from $HOME, never the project root (step 4 of .claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md); machine-level, once per machine, operator-manual territory." Four ideas in one sentence. Proposed: "Copy to ~/.testcontainers.properties and fill. It binds only from $HOME, never from the project root (…). It is set once per machine, and the operator manual says so." `application.yaml` has no finding of its own; its "rides" (21) and "world is up" (27) are FINDING-912 and FINDING-919.

##### `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md

**FINDING-879.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, opening (lines 9–13, 15–20): "Take one framed project to **ground**: the environment chosen and running, the services the problem's reasoning chain requires stood up, constrained to need, verified both ways, with the manuals that make the ground usable and reproducible." Five parts in one sentence; 1 more: 15–20. Proposed: the five parts as a list.

**FINDING-880.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Stage 0 — readiness gate*, check 2 (lines 32–42): "added by a dated revision entry in LAYER-1-ENVIRONMENT — what changed, why, triggered by this check — one commit, no possession, refusal or verdict touched; then the check passes." 2 more: 32–36, 36–38. Proposed: split.

**FINDING-881.** rule 7; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Stage 0* (line 48): "Framing work is never done here — that is the framing job's territory." Repeats line 41: "Framing work is not done here; a fact the framing left unstated is written where it belongs." Proposed: keep one.

**FINDING-882.** rule 5; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *The walk and its gates* and *Deviations* (lines 68–69, 105–106): "choose the environment; **the levers the evidence pulls are proven by the harness that pulls them**, not here." "levers … pulls" (also `establishment-walk.md` lines 31–36: "A lever the evidence pulls — starting several instances, killing one, freezing the store — is proven where the harness that pulls it is built"); "lived captures, not law — but a silent deviation poisons the record" (105–106). 4 instances. Proposed: "what the evidence must be able to do is proven by the harness that does it"; "written from what was done, not rules"; "a deviation not logged makes the record wrong".

**FINDING-883.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *The walk and its gates* (lines 65–71, 72–77, 82–86): "- **Stage 1 gate:** the environment decision is logged with its why *before* any ground file exists. **No compose file is born at stage 1** — its content is stages 2–5's outcome." 4 more: 68–69, 69–71, 72–74, 82–85. Proposed: split.

**FINDING-884.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Records and outputs* (lines 113–123, 124–128, 141–146, 155–157): "project): **no establishment log.** Decisions are ADRs — the environment; the service set with its not-provisioned list; the constraints, each with its enforcement." Three ADRs chained; 5 more: 116–119, 120–123, 124–128, 141–146 (five parts of the contract in one sentence), 155–157. Proposed: lists.

**FINDING-885.** rule 6; checked. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Records and outputs* (line 108): "## Records and outputs (the repo's own conventions win)". Three Fact References give the title as *Records and outputs*: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 44, `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` lines 19 and 57. The italic title is not the heading. Proposed: drop the gloss from the heading; its first line says it.

**FINDING-886.** rule 5; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Records and outputs* (line 150): "- README `Prerequisites` section — projected at the exit, when the". "projected"/"a projection" for a derived copy (also 156–157; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 206 "project into the README"; `establishment-walk.md` 145 "projects outward", 158). 5 instances. Proposed: "derived from the operator manual"; "written from".

**FINDING-887.** rule 5; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Records and outputs* (line 148): "truth, written **from the lived setup, contemporaneously** —". "truth" for facts; also `establishment-walk.md` 91 ("its own truth"), 99 ("project truth"), 107, 145 ("the ground's truth"). 5 instances. Proposed: "facts"; "what the operator did".

##### `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md

**FINDING-888.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, *Inputs, before the first move* (lines 10–19): "move, not the stop: a dated revision entry in the definition's LAYER-1-ENVIRONMENT, one commit, then the walk begins (Stage 0, check 2)." 2 more: 10–13, 14–15. Proposed: split.

**FINDING-889.** rule 5; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, opening, *Inputs* and §1 (lines 3, 5, 8, 17, 26): "move, not the stop: a dated revision entry in the definition's". "the return trip is the move, not the stop" (17), "before the first move" (8), "the walking project's" (3), "This capture" (5), "the stage's living half" (26). 5 instances. Proposed: "the definition is revised first, and the walk goes on"; "before the walk starts"; "the project's"; "This walk"; "the part of this stage that decides".

**FINDING-890.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` §1 (lines 23–27, 29–36, 60–68): "the evidence pulls — starting several instances, killing one, freezing the store — is proven where the harness that pulls it is built, in the form it pulls it: the bootstrap's harness for its first adversity, each slice's readiness check for the rest." 5 more: 23–27, 29–31, 60–63, 63–65, 66–68. Proposed: split.

**FINDING-891.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` §3 (lines 81–85, 87–94): "Where governing knowledge for a decided service already stands (for PostgreSQL: `.claude/skills/infra-establish/references/postgres-role-split.md` in this skill's references), its constraint set is the **rebuttable default**: check it against this project's facts; deviate only when a project fact defeats it, naming the defeater." 3 more: 81–83, 90–93, 93–94. Proposed: split.

**FINDING-892.** rule 5; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` §3, §4 (lines 79, 87, 89, 92, 96, 116; `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` 44): "enforcement mechanisms, standing knowledge as the rebuttable". "standing knowledge" and "governing knowledge", two coined phrases for one thing, a reference already written; "rebuttable default", a legal term. 7 instances. Proposed: "a reference already written" / "the reference"; "the default, unless a project fact defeats it".

**FINDING-893.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` §5 (lines 107–111): "Ground files land as project truth: declarations (`compose.yaml`), bootstrap scripts, tool configs — **secrets split out** per the project's credential handling (`.env` git-ignored + committed `.env.example`; decided identities stay literal, secrets and machine variance are variables)." Four ideas in one sentence. Proposed: split; the credential rule as its own sentence.

**FINDING-894.** rule 3; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` §6 (lines 129–135): "The builder-facing manual — a **living document, one section per service**, grown at every later re-entry: what services exist, how to reach them (inside vs. outside the environment's network), **which identity to connect as and which never to use**, what the constraints allow and refuse (the refusals written as contract terms), how schema changes are made." Five parts in one sentence (its three homes are Round 2's FINDING-227). Proposed: a list of five, in one home.

**FINDING-895.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` §7 (lines 145–155): "When the exit test passes, the ground's truth projects outward: the CBC Run's README gains its **Prerequisites** section — the environment lines a stranger's machine needs before this ground can stand, derived from the operator manual, carrying only what a stranger needs in hand and linking the manual for the rest." 3 more: 149–151, 151–153, 153–155. Proposed: split.

**FINDING-896.** rule 9; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, *Vocabulary* (line 162): "- **Execution Environment** — the local runtime host for". Three Names defined here (162–166), written as Names at line 21 and `postgres-setup-walkthrough.md` lines 6 and 30, and lowercase ("the environment decision", "every constraint names", "the service set") in the skill and the walk everywhere else; none is in the CBC Run's glossary, whose header says the delivered Names arrive in its first group. Question: Names (then into the delivered glossary and used as Names) or English (then the capitals and this section go)?

**FINDING-897.** rule 9; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` (lines 12, 65–87), `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` (lines 30, 65, 123), `delivery/spring-postgres/.claude/skills/infra-establish/templates/verify-database-model.sql` (line 9): "- **Stage 1 gate:** the environment decision is logged with its why" against "at stage 5" and "the walk's stage 7". The walk's sections are headed `## 1.` to `## 7.` with no "Stage" label; the skill writes "Stage N" for them, the walk and the template "stage N". Rule 9: a label keeps its case inside its owner. Proposed: one spelling; or head the walk's sections "Stage N", as the skill's own Stage 0 is.

##### `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md

**FINDING-898.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md`, *The roles* (lines 26–31): "- **`migrator`** — the structure authority. Owns the application schema and every object in it; the **only identity migrations run as** (Flyway or equivalent connects as `migrator`, nothing else does). DDL within that schema — and only there: it does not own the database, cannot drop it, creates no schemas beyond its own." 5 more across the file: *The principle* 16–20, *The roles* 36–40, *The application schema* 48–53, *The grant boundaries* 79–84, *Naming across a cluster* 92–96. Proposed: split.

**FINDING-899.** rule 5; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md`, *Naming across a cluster* (lines 95–96): "not legal in unquoted SQL identifiers, and quoted names are a permanent tax." 1 instance ("outermost door", 83, is FINDING-910). Proposed: "quoted names cost at every use".

**FINDING-900.** rule 3; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md`, *What a using project supplies* (lines 112–118): "Concrete role names under the cluster naming rule and their credentials (secrets handling is the project's), the schema name and the application's `search_path`, which migration tool connects as `migrator`, where the bootstrap SQL lives and how it is applied, and how the model is verified on the ground (catalog checks plus a behavioral DDL-refusal check) — all in the project's manuals and ground files, referencing this model, never restating it." Six things in one sentence. Proposed: a list of six.

##### `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md

**FINDING-901.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, opening (lines 3–8, 14–22): "**Masters nothing**: the authority shape — roles, grants, the why — is mastered in `.claude/skills/infra-establish/references/postgres-role-split.md`; on any conflict the model wins." 3 more: 6–8, 14–17, 18–22. Proposed: split.

**FINDING-902.** rule 3; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` §2 (lines 48–52): "Keys: the bootstrap password, the migrator password (**must equal** the literal in the bootstrap SQL), optional `POSTGRES_PORT`, and the runtime application password (**must equal** the runtime literal in the bootstrap SQL) — the app reads it from the environment at bootstrap." Four keys in one sentence; the same shape in §1 40–43 (three podman notes), §4 78–82 (four claims), §9 156–161 (six facts). 4 instances. Proposed: lists.

**FINDING-903.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` §3, §4, §9 (lines 60–67, 75–82, 162–170): "Skill Template: `.claude/skills/infra-establish/templates/bootstrap.sql` — its comments are the recall layer, carried in full; the load-bearing lines are the default privileges (every table and sequence a future migration creates arrives already granted to runtime, so the split needs no per-migration discipline and cannot erode)." 5 more: 60–62, 75–77, 162–164, 164–167, 168–170. Proposed: split.

**FINDING-904.** rule 1; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` §9 (lines 162–170): "Day-to-day IDE/psql inspection: runtime — the identity the application writes with, so whoever inspects holds a password that can change every table." The instruction, say which identity people inspect with or make a read-only one, comes second, after the problem. Proposed: lead with "Decide, and write in the manuals, which identity people inspect with."

**FINDING-905.** rule 5; checked. `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` §5, §9 (lines 87, 161, 169): "the bootstrap identity is an occasional admin lens, never wired in." "lens"; "whether that hand is a writer to defend against" (169); "the url speaks the compose network's service name" (87; also `flyway.conf` line 7 and `spring-harness-reference.md` line 405 "the application speaks as runtime"). 5 instances. Proposed: "used by hand for admin, never in config"; "whether that reader can write"; "the url names the service"; "connects as runtime".

##### `delivery/spring-postgres/.claude/skills/infra-establish/templates

**FINDING-906.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-establish/templates/bootstrap.sql` (lines 33–39, 14–17): "-- cluster-wide). One dedicated cluster in one container — the lived normal — takes the model's bare names, migrator and runtime; then the verify suite's role filter becomes an explicit IN list, and the other templates' <project>_ role references drop the prefix too." 1 more: 14–17. Proposed: split.

**FINDING-907.** rule 2; uncertain. `delivery/spring-postgres/.claude/skills/infra-establish/templates/readme-prerequisites.md`, header (lines 5–7): "A different ground writes different lines; the shape (each line one thing a stranger's machine needs, the manual linked) is what carries." Two ideas joined with a semicolon, a list inside the parentheses. Proposed: "A different ground writes different lines. The shape stays: each line one thing a stranger's machine needs, and the manual linked." `compose.yaml`, `.env.example`, `flyway.conf` and `verify-database-model.sql` have no finding of their own; their instances are in FINDING-910 ("Front door", 6; "no side door", `bootstrap.sql` 55), FINDING-905 ("speaks", `flyway.conf` 7), FINDING-912 ("ride", `verify-database-model.sql` 18) and FINDING-914 ("load-bearing", `bootstrap.sql` 59; `verify-database-model.sql` 63).

##### `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md

**FINDING-908.** rule 3; checked. `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`, *Stage 0 — the ground stands?* (lines 16–23): "Verify: the ground's record exists with the original service evaluation and its not-provisioned list — the establishment log, or the ADR that holds the evaluation in a repo with records (…); the infrastructure contract and operator manual exist; the ground currently comes up (`podman compose ps` or the project's equivalent — read the actual output)." Three checks chained with semicolons where `infra-establish`'s Stage 0 numbers its three. Also *Hard lines* (65–69): "Never re-frame the problem; never build the system (the ground ends where application code and schema content begin); destructive acts need explicit confirmation; host-level installs are the user's own acts; project files speak the project's language." Five rules in one sentence. 2 instances. Proposed: numbered lists.

**FINDING-909.** rule 2; checked. `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`, *The re-entry, one pass* (lines 38–42, 48–54, 55–61): "4. **Stand up and verify both ways.** Ground files as complete files (never fragments); secrets split out; then the catalog check *and* the behavioral check for the new capability — expected result stated before running, outcome read from actual output." 3 more: 38–41, 55–58, 58–61. Proposed: split.

**FINDING-910.** rule 5; uncertain. "door": `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 85: "arrives through the real door); operational health (every evidence run". The concept writes "checked at the door" for the boundary (`concept/01-layered-system.md` line 46; `02-guarantees-and-walls.md` 56, 61), so "the real door"/"its own door" may be the method's word: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 85, 217; `spring-boot-walkthrough.md` 190, 201, 222; `spring-harness-reference.md` 42, 177, 195, 293, 311, 352, 404, 486; `app-structure.md` 35, 56 (15). The others are not the concept's: "front door" for `podman compose` (`establishment-walk.md` 50; `postgres-setup-walkthrough.md` 27; `compose.yaml` 6), "the outermost door" for CONNECT (`postgres-role-split.md` 83), "no side door" for `public` (`bootstrap.sql` 55), "reopen that door" for Flyway auto-configuration (`spring-harness-reference.md` 158). 6 instances. Proposed: keep "the door" where it is the boundary; elsewhere "the command", "the connect right", "no second schema", "a second migration path". Question: is "door" the concept's word, and so exempt where it means the boundary?

**FINDING-911.** rule 5; checked. "masters/mastered/master" as a verb or for a home: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md` line 16: "**Masters nothing else.** What classes exist is the slices'". Also `spring-harness-reference.md` 10; `establishment-walk.md` 134, 158, 160; `postgres-setup-walkthrough.md` 4, 5; `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` 157; `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` 61. 9 instances (the template headers' "Master Copy" is the Name, not counted). Proposed: "owns"; "is the home of"; "a second home".

**FINDING-912.** rule 5; checked. "ride(s)/riding" for "is carried in": `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 53: "observations ride the record"; `spring-boot-walkthrough.md` 64; `application.yaml` 21; `readme-run-test.md` 14; `postgres-setup-walkthrough.md` 81; `verify-database-model.sql` 18; `spring-harness-reference.md` 203 ("riding on it"). 7 instances. Proposed: "go in"; "sit beside each query"; "comes with it".

**FINDING-913.** rule 5; uncertain. "honest/honestly" of a file or a state: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 94: "migration tooling test-scope only; one migrations home, honestly empty;". Also 181, 191, 194; `spring-boot-walkthrough.md` 176, 234; `spring-harness-reference.md` 222, 267, 269; `postgres-setup-walkthrough.md` 106. 10 instances. Proposed: "empty, with no placeholder migration"; "deviations stated"; "'no business behavior yet', said outright"; "the real 'up'".

**FINDING-914.** rule 5; uncertain. "load-bearing": `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 146: "The **ordering is load-bearing; the commit split is judgment**." Also `spring-boot-walkthrough.md` 7; `spring-harness-reference.md` 152; `postgres-role-split.md` 79; `postgres-setup-walkthrough.md` 64, 80; `bootstrap.sql` 59; `verify-database-model.sql` 63. 8 instances; near-dead in technical English. Proposed: "the order matters; the split is judgment"; "the lines the split depends on"; or decline as a dead metaphor.

**FINDING-915.** rule 5; uncertain. "born/births" of a file or table and "dies/death" of scaffolding: `spring-boot-walkthrough.md` line 186: "that dies when the first real slice lands**. Never grows business". "born"/"births": `spring-boot-walkthrough.md` 150, 251; `spring-harness-reference.md` 220, 267, 414, 504; `establishment-walk.md` 60, 62, 152; `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` 66, 113 ("container-born"). "dies"/"death": `spring-boot-walkthrough.md` 194, 234; `spring-harness-reference.md` 42, 290, 306, 412; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 98, 187, 195. 20 instances. "born" is this repo's own figure (Run Birth); "dies" is not the concept's. Proposed: "is created"; "is deleted at the first slice".

**FINDING-916.** rule 6; resting on the reader. "lived/unlived" as a coined adjective, Round 2's FINDING-224, left to the plain-rewrite TODO item: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md` line 85: "- **Classic layered** *(unlived here)* — packages by technical role". 64 lines across 10 files (`app-structure.md` 11, `spring-boot-walkthrough.md` 11, `spring-harness-reference.md` 7, `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 4, `readme-run-test.md` 1, `establishment-walk.md` 8, `postgres-setup-walkthrough.md` 3, `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` 13, `bootstrap.sql` 1, `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` 3). Listed for the count; nothing new.

**FINDING-917.** rule 5; uncertain. "to life"/"proof of life": `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 7: "# cbc-bootstrap — bring a framed system to life"; also 3, 209; `readme-run-test.md` 9, 27. 5 instances. Proposed: "make a framed system run"; "health UP, db UP".

**FINDING-918.** rule 5; uncertain. "world is up": `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 86: "needs a cheap world-is-up check"; `application.yaml` 27: "evidence runs gate on "world is up, store included"". 2 instances. Proposed: "a cheap check that the system and its store answer".

**FINDING-919.** rule 9; uncertain. "the log" for a CBC Run record: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 62: "Record the decision **in the project's log". Also `app-structure.md` 8, 63, 67; `spring-boot-walkthrough.md` 23; `spring-harness-reference.md` 415. 6 instances. `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` lines 113–114 say a repo with records keeps no establishment log, decisions are ADRs; in a CBC Run "log" reads as the Decisions Log or the devlog. Proposed: "in an ADR"; "where the records table puts a decision".

**FINDING-920.** rule 9; uncertain. "Stage N" outside its skill: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/readme-run-test.md` line 2: "Merge into the CBC Run's README at Stage 5, when the"; `spring-boot-walkthrough.md` 94 ("decided at Stage 1 by name"). The Skill Stage's owner is the folder, not the sentence. 2 instances. Proposed: "at `cbc-bootstrap`'s Stage 5"; or decline, the owner being the skill the file belongs to.

**FINDING-921.** rule 6; uncertain. Skill names bare: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` line 12: "to end. After this, cbc-slice has somewhere to land." Also 7, 41, 47, 217; `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` 30; `establishment-walk.md` 77; `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` 22; `readme-run-test.md` 6. 9 instances outside frontmatter; both glossaries write `cbc-slice` in backticks. Proposed: backticks; or decline if a skill name is not a reference under rule 6.

##### From the items checked first

**FINDING-922.** rule 10; resting on the reader. `delivery/container/.claude/rules/shapes-lifecycle.md` §4 (line 77): "## 4. When an Output Shape names work". 31 characters, one past the rule; the one title the Names pass left to the read. Proposed: fix: *An Output Shape naming work*, 27 characters, with the rename grep on its Fact References.

**FINDING-923.** Stale lines; resting on the reader. `delivery/container/.gitignore` (lines 20–21), and `.gitignore` at the root (lines 20–21): "# Claude Code machine-local settings — permissions and local overrides; # the committed shape is .claude/settings.json". Neither the Container Group nor this repo holds a `.claude/settings.json`; `docs/conventions/agent-arrangement/` §3.5, *`.claude/settings.json`*, says a project adds one when it has a rule that must not depend on text. Round 2's note, met in passing and held since. Proposed: fix: "its committed counterpart, when a project adds one, is .claude/settings.json"; or decline: the line names the pair, not a file that exists.

**FINDING-924.** Agreement; checked. 20 lines in 18 files of the Method Group and the Stack Group cite a decision mid-sentence, `(CBC ADR-0008)` or `(CBC ADR-0013)`: the header line of 10 Skill Templates, "Skill Template — the Master Copy is in correctness-by-construction (CBC ADR-0008)", under `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/` (3), `delivery/spring-postgres/.claude/skills/infra-establish/templates/` (6) and `delivery/method/.claude/skills/cbc-framing/templates/registry.md`; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md` lines 1 and 107; `delivery/method/.claude/skills/cbc-framing/SKILL.md` 189; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` 25; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` 13; `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` 15; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/testcontainers.properties` 8; `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 206; `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` 152; `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` 153. `docs/conventions/conventions/` §1.1, *How a rule is written*: "Cite no decision mid-sentence. A skill or an Agent Rule lists the decisions it rests on once, in a footer headed *Decisions*". Round 2's note, 29 lines then, 20 now. Rests: DECISION-29. Proposed: fix: each citation in a body moves to its file's *Decisions* footer, or goes where the footer already lists the ADR; a Skill Template's header keeps its sentence without the citation.

**FINDING-925.** Agreement; resting on the reader. `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md`, *READINESS-5* (lines 61–63): "Self-test: break an invariant deliberately (drop the constraint, comment the guard — on a branch) and confirm the adversity test goes red, then restore." `delivery/method/.claude/skills/cbc-slice/SKILL.md`, Stage 3 (lines 141–142 and 178–180), has the red seen "in a state that never lands in history". CBC Run 5 saw its reds on `red/` branches never merged, so the two may agree in substance; the words differ. Round 2's note, met in passing and held since. Proposed: fix: readiness takes cbc-slice's words, "in a state that never lands in history, a branch never merged for one"; or decline.

### Decisions

Seventeen, DECISION-16 to DECISION-32, the last raised by the
reviewer while deciding. Four of them end most of the
list between them: DECISION-16, where the method's and the stack's
188 findings are worked; DECISION-26, which figures are dead; DECISION-19,
whether the method's own words are Names; DECISION-18, whether dated
notes are history.

**DECISION-16.** Where the method's and the stack's findings are
worked. Rests: FINDING-736 to 921, the Method Group's 92 and the Stack
Group's 94, and FINDING-924 and 925. TODO's "Rewrite the method's texts
plain" names these texts, about 26,000 words, and its trigger says what
this round did leaves the item.
- (a) All worked in this round's layer 6, as a commit plan per group;
  the item closes with them, or keeps what the work left.
- (b) The exact findings worked now, in layer 6: rules 4, 6, 8, 9 and 10
  and the two Agreement ones, 55 findings. The rewrites, rules 1, 2,
  3, 5 and 7, 133 findings, move to the item, which becomes a Plan
  Step of its own after the refinement closes, this list its input
  (`.claude/approaches-on-trial/refinement.md` §2.7, *Working the
  findings*: a change too big for one commit plan is a Plan Step of
  its own).
- (c) All 188 move to the item.
- Recommended: (b). The exact fixes are each one edit and carry
  Names the CBC Run's glossary lists. A plain rewrite of 32 files is
  a Plan Step, not a layer's commit plan, and the refinement's last
  read would wait on it.
- Chosen: (b), by the reviewer, 2026-10-30. The 133 rewrites are the
  item's worklist: no second read finds them again, and the one check
  read after the rewrite is its Plan Step's gate, as it would be this
  round's close read under (a). The rewrite adds what this read did
  not do: each rewritten section keeps its meaning, checked against
  the concept by the Foundation Check. The refinement's last read
  does not list a moved finding again, as with DECISION-7's. The cost:
  a CBC Run born before the rewrite lands gets today's text, with the
  exact fixes only.
- Reopened and chosen: (a), by the reviewer, 2026-10-30, the same
  day, on the reviewer's question whether this round is the plain
  rewrite. It is: round 3 rewords what stays, and on 2026-10-19 the
  reviewer had it read the method's texts so that one pass would do
  the rewrite (*Files by layer*, before round 1). The plain-rewrite
  item's trigger says the same: it keeps what this round leaves. (b)
  was recommended on size and not checked against that choice. All
  188 are worked in layer 6, the Method Group and the Stack Group each
  as a commit plan; the check after the work is this round's close
  read, and the meaning of each rewritten section is checked against
  the concept by the Foundation Check.

**DECISION-17.** The concept chapters. Rests: FINDING-530 to 545, the
reader's 16, every proposal marked editorial; three ask a question
that could move a meaning or reach the skills: FINDING-531, the four
failure-mode labels; 537, the chapters' headings; 543, "enemy".
- (a) Worked in layer 3 as editorial changes to concept v1, with one
  CHANGELOG line under [Unreleased]; the three questions decided
  here.
- (b) Moved to TODO's plain-rewrite item, with the method's
  (DECISION-16).
- (c) Declined: the chapters keep their voice.
- Recommended: (a) for the 13 editorial ones. FINDING-531: the four
  labels stay, they are the method's words in the skills and in CBC
  Runs' records; *How it rots* becomes *How it fails*. FINDING-537:
  declined, the chapters' headings are unnumbered (DECISION-20).
  FINDING-543: declined, "enemy" is the census's word for an actor and
  "adversary" the walls' word for what they defend against; a rename
  reaches 16 uses in five shipped files.
- Chosen: (a), by the reviewer, 2026-10-30, as recommended. (b) was
  ruled out by DECISION-16's reopening: the plain-rewrite item keeps
  only what this round leaves. The 13 editorial findings are worked in
  layer 3, concept v1 staying v1, with one CHANGELOG line under
  [Unreleased]. FINDING-531: the four labels stay, *How it rots*
  becomes *How it fails*. FINDING-537 and 543 declined.

**DECISION-18.** Whether dated notes are history. Rests: the
approaches' *Uses* notes and the refinement's *Found* lines,
FINDING-647, 653, 656 to 661 and 668, about 60 lowercase Names among
them; the CHANGELOG's released entry, FINDING-568; the Conversation
Memory's part headings, FINDING-596 and 597; the shipped
`docs/adr/0001`'s body, FINDING-705 and 706.
- (a) History: an Approach on Trial's dated notes, a CHANGELOG's
  released entries and a Conversation Memory part's heading keep
  their words, and the one-home rule's *Not a second home* and
  facts-in-sync §1 name them at the round's close, as DECISION-13 did
  for the two logs. The shipped `docs/adr/0001` is a Master Copy born
  Accepted in every CBC Run: living.
- (b) Living, all: fixed like any line.
- (c) The released entry and the headings history; the approaches'
  notes living, since an Approach on Trial is rewritten as it goes.
- Recommended: (a). A dated note records what one use taught, as a
  devlog entry does; rewording it rewords evidence. Under (a),
  FINDING-568, 596, 597, 647, 653, 656 to 661 and 668 are declined,
  and 705 and 706 stand.
- Chosen: (c), by the reviewer, 2026-10-30, on the agent's changed
  recommendation after the reviewer asked why not fix. The test is who
  reads the text: nobody works from the devlog, but the agent reads an
  approach's notes each time it does that work, and copies the voice
  it reads; the shipped copy is read by every CBC Run. A Name spelled
  right changes no fact a note records. So the approaches' *Uses*
  notes and the refinement's *Found* lines are living: their Names
  are fixed, what each says stays. FINDING-647, 653, 656 to 661 and
  668 fixed so; 648, the shipped "here", fixed. The released CHANGELOG
  entry and the Conversation Memory's part headings are history:
  FINDING-568, 596 and 597 declined, and the one-home rule's *Not a
  second home* and facts-in-sync §1 name a released CHANGELOG entry at
  the round's close. 705 and 706 stand.

**DECISION-19.** Whether the method's and the stack's own words are
Glossary Names. Rests: the roll-ups FINDING-739, 741, 744, 747, 775,
799, 808, 819 and 823, about 100 words; FINDING-832, "system
bootstrapped"; 896, the walk's three capitalized terms; 919, "the
log"; 813, the standing guards' names; 815, the Skill Stages' names;
531 and 543; 440, repo-hygiene's "the base". The pass left slice,
kill, fold, framing, promise, census, witness, wall, harness and
ground as the concept's; the readers found about 100 more words the
skills define on one English word: fence, tripwire, backstop, probe,
lens, ledger, rider, flag, possession.
- (a) Not Names. The concept's words and the words a method or stack
  skill defines are the method's vocabulary, defined where they stand
  and in the concept; a CBC Run names what it defines at framing, as
  `cbc-framing` says. Rule 9 gains the line at the round's close,
  before the last read. A word with a rival among the delivered Names
  is fixed as its finding says: "stage" as a verb beside Skill Stage,
  FINDING-792; "master" beside Master Copy, FINDING-774.
- (b) Each gets a Name of two words in the shipped glossary's first
  group, about 100 entries.
- (c) The CBC Run names them at framing, and the skills' own text
  stays as it is.
- Recommended: (a). Rule 9's reason is a reader deciding at every use
  which of two meanings is meant; inside a CBC Run's work these words
  have no rival, and a hundred capitalized Names would make every
  skill harder to read. Under (a) the roll-ups and 832, 896, 919, 813,
  815, 440 are declined; 792 and 774 fixed.
- Chosen: (b), by the reviewer, 2026-10-30, against the agent's
  recommendation. The CBC Run's own rule 9 already asks it: a word a
  delivered text gives a meaning English does not is a Glossary Name,
  and the method's and the stack's words are not. Whoever writes a
  text defines its words: this repo, the concept, manuals, skills,
  rules and Output Shapes; a CBC Run, its records' problem words and
  its Approaches on Trial's words, the latter marked on trial in its
  glossary and read at each Run Reading, a general one harvested into
  ours. The shape:
  - our glossary grouped by who uses a Name: ours only; shared, whose
    CBC Run twins stay in the container's glossary; the concept's; the
    method's; the stack's;
  - the concept's and the method's Names reach a CBC Run's
    `docs/glossary.md` by a Delivery Fill from the Method Group, the
    stack's by one from the Stack Group, so a stack swapped swaps its
    words; each from a source file of its own, not the playbook;
  - a delivered entry is a follower of ours, written from the CBC
    Run's side, since a CBC Run cannot open our manuals; the
    Foundation Check carries a change in one to the other;
  - the CBC Run's own group keeps two parts: its problem's words, and
    its Approaches on Trial's, on trial.
  A design change, not a finding's fix (`.claude/approaches-on-trial/refinement.md`
  §2.7, *Working the findings*): an ADR and a commit plan of its own,
  inside the refinement, built before layer 6's work; it changes the
  Exchange Convention's list of Delivery Fills, the Pure Seed and both
  glossaries. The method's and the stack's rule 9 findings wait for
  it, the roll-ups and 832, 896, 919, 813, 815 among them; 792 and 774
  are fixed as proposed. Every other finding goes on.
- A question for the design, found at DECISION-28 by the reviewer,
  2026-10-30: how a CBC Run already born gets a Name added later. A
  record is delivered once and never updated
  (`docs/conventions/exchange/` §2.4, *The records' exception*), and a
  Delivery Fill writes only at birth, while the delivered Agent Skills
  that use a new Name update at every delivery. One way: the delivered
  groups' Names live in a file that is a pinned copy, updated with
  every delivery, and only the CBC Run's own group in the record.
- Its design decided, 2026-10-31, ADR-0078: the delivered Names are
  pinned copies, one file per group, updated with every delivery, in
  place of the Delivery Fill; the concept's ten words take two-word
  Names; every candidate is judged in one table first.

**DECISION-19's Names table: the concept's group.** Proposed
2026-10-31 from the chapters under `concept/`, under writing rule 9
as it stands after ADR-0078's decision 12: a Name built on another
carries it whole, and past 4 words, every word counted, a shorter
true one is looked for. A hyphenated word counts as one. "English"
means the word stays lowercase, its plain meaning ours. Fold,
witness, harness and ground are not defined in the concept; they go
to the method's and the stack's groups. Judged by the reviewer,
2026-10-31: every row and every question's proposal taken.

| # | Word today | What it means (chapter) | Proposed | Built on it | Why |
|---|---|---|---|---|---|
| 1 | slice | one invariant made real, end to end (04) | Invariant Slice | Invariant Slice Registry; the method's Invariant Slice Record | says what the work is cut along |
| 2 | kill | what dies when an enemy fact meets what we own (03) | Enemy Collision Kill | Enemy Collision Kill Shape, 4 words | built on row 3, whole |
| 3 | collision | each enemy fact run against each possession (03) | Enemy Collision | row 2 | pairs with Enemy Fact |
| 4 | census | the list of attackable facts, done when fresh attacks find nothing (03) | Enemy Census | | the chapter's own "the enemy census" |
| 5 | enemy fact | one attackable fact | Enemy Fact | rows 3 and 4 are its family | the census's item |
| 6 | enemy | whatever can hurt: a caller, the store | English | | its plain meaning; rows 2 to 5 carry it as English |
| 7 | possession | what the system owns (03) | System Possession | | "system" English, as below |
| 8 | area | a division of the system by ownership (01) | Responsibility Area | | chapter 01's own title for LAYER-3-AREAS |
| 9 | owner | who owns a fact (02, 03) | English | | its plain meaning |
| 10 | system | the thing being built | English | rows 7, 12, 13, 19, 21 | see question 1 |
| 11 | promise | one falsifiable commitment to a named party (01) | Falsifiable Promise | | its defining property |
| 12 | guarantee | a never-event stated against a named source (00) | System Guarantee | System Guarantee Inventory, System Guarantee Erosion | owner first; GUARANTEE-n ids stay |
| 13 | guarantee inventory | the few never-events whose violation is costly (02) | System Guarantee Inventory | | built on row 12, whole |
| 14 | never-event | what must never happen, before a source is named (00, 02) | System Never-Event | | one word as written; see question 2 |
| 15 | invariant | a property that always holds | English | | its technical English meaning is ours |
| 16 | wall | what makes a guarantee impossible to break, ranked by what it binds (02) | Structural Wall | | the chapter's own bold phrase |
| 17 | framing | the first movement: the idea worked into three documents (03) | CBC Framing | rows 18 and 19 | matches the cbc-framing Agent Skill |
| 18 | what framing produces | its three documents, "artifacts" or "exports" today (03) | CBC Framing Export | | one Name for both words |
| 19 | intent | the first export: the promise and the purposes refused (03) | CBC Framing Intent | | built on row 17, whole |
| 20 | system definition | the second export: authority, boundary, adversary, owners (03) | System Definition | | used as a document |
| 21 | slice registry | the third export: the work, cut into invariants (03) | Invariant Slice Registry | | built on row 1, whole |
| 22 | layered system | the concept's world model, five layers (01) | Layered System | System Layer, the method's file | the chapter's title |
| 23 | the inversion | asking what must never happen before what it should do (00) | CBC Inversion | | "the inversion" alone is English |
| 24 | guarantee erosion by feature | features shipped without re-checking guarantees (00) | System Guarantee Erosion | | whole would be 6 words; see question 3 |
| 25 | the escape hatch, testing theater, the theory swamp | three more ways it fails (00) | Escape Hatch, Testing Theater, Theory Swamp | | kept by DECISION-17, now capitalized |
| 26 | authority, boundary | fields of the system definition (01) | English | | plain meanings |
| 27 | feature-thin | with few features | English | | an adjective, defined where it stands |
| 28 | technique, process framework, composition | what the concept is not (00) | English | | plain words |

Questions the rule raised, each taken as proposed:

1. **Whether "system" is English.** Chapter 01 titles LAYER-2-SYSTEM
   "System of Interest". If that title is a Name, every "System"
   Name above is built on it, and System Guarantee becomes System of
   Interest Guarantee. Proposed: the layer titles are labels, like
   Step 0, and "system" is English, the thing being built.
   Responsibility Area is the exception, since the chapters use
   "area" in prose with its defined meaning.
2. **Whether a never-event is a guarantee.** Chapter 00 says
   "Guarantees are the never-events, each stated against a named
   source": one thing before and after its source is named. Proposed:
   two Names, since chapter 02 uses both; the other way is one Name,
   System Guarantee, with "never-event" rewritten to it.
3. **The trigger, once.** "Guarantee erosion by feature" built whole
   is System Guarantee Erosion by Feature, 6 words. Proposed: System
   Guarantee Erosion, the "by feature" going to its entry, since what
   erodes is the guarantee and features are its cause.

**DECISION-19's Names table: the method's group.** Proposed
2026-10-31 from the Method Group's files under `delivery/method/.claude/`,
under writing rule 9 as it stands after ADR-0078's decision 12: a
Name built on another carries it whole, and past 4 words, every word
counted, a shorter true one is looked for; a hyphenated word counts
as one. "English" means the word stays lowercase, its plain meaning
ours. "Label" means a label inside its owner, keeping its case, never
a Name. "One thing" means the word is another word for a thing that
already has a Name, and is rewritten to it. The concept's 23 Names
are in `delivery/method/docs/glossary/method.md` and are not repeated.
Files: F `cbc-framing/SKILL.md`, FW `cbc-framing/references/cbc-framing-workflow.md`,
WE `references/worked-example.md`, S `cbc-slice/SKILL.md`, SW
`cbc-slice/references/cbc-slice-workflow.md`, SR
`cbc-slice/references/system-readiness.md`; the Output Shapes under
`shapes/` by their file's first word: kill, test, entry, record. Judged by the reviewer, 2026-10-31: every row, trigger and question's proposal taken.

| # | Word today | What it means (file:line) | Proposed | Built on it | Why |
|---|---|---|---|---|---|
| | **The cbc-framing Agent Skill** | | | | |
| 1 | stage 0 to stage 6 | one phase of framing's derivation (F 50-56, FW 30-36) | Agent Skill Stage, the shared Name; "Stage 3" a label | | one thing; a label keeps its case |
| 2 | fold, FOLD-n | a definition-shaped concern folded into the first slice that consumes it, its checks riding along (FW 86, 320) | Invariant Slice Fold | Invariant Slice Fold Candidate | built on Invariant Slice, whole |
| 3 | fold-candidate | a concern with no enemy, marked at stage 3 to become a fold (F 86, FW 262) | Invariant Slice Fold Candidate | | built on row 2, whole; 4 words |
| 4 | concern | one item stage 6 sorts: kills with one proof obligation, or an enemy-less wording hole (FW 258-262, 300) | CBC Framing Concern | | covers both sources, so not built on the kill |
| 5 | fold-reconciliation line, reconciliation line | the registry's line accounting every concern as slices and folds, absences included (F 94, 185; FW 322) | CBC Framing Reconciliation | | whole it would be 6 words; see trigger 1 |
| 6 | the written zero | an absence stated in the reconciliation (F 186) | English | | plain words, defined where they stand |
| 7 | slice surface | what stage 6 cuts: the slices and folds (F 56, FW 17, 298) | Invariant Slice Registry | | one thing |
| 8 | operational test | two kills are two slices only if their evidence must create different adversity (F 92, FW 314, WE 178) | Invariant Slice Split Test | | says what it decides; 4 words |
| 9 | theorem, definition | stage 6's two stamps on a concern (FW 300-309) | Label | | see question 3 |
| 10 | the sort, the dedupe, the folds | stage 6's three passes (FW 305-323) | Label | | numbered parts of one stage |
| 11 | hostage test | for each candidate possession: could someone else owning it break the promise? (F 51, 71; FW 127) | System Possession Test | | built on System Possession, whole; "hostage" a figure, rule 5 |
| 12 | refusal | a candidate fact or responsibility deliberately not owned, written (F 72, FW 130) | System Refusal | System Refusal Test | the counterpart of System Possession |
| 13 | mirror test, the mirror | can the promise stay true if this goes wrong elsewhere? Yes means refused (F 73, FW 129) | System Refusal Test | | built on row 12, whole; "mirror" a figure |
| 14 | sketch-enemies, sketches, sketch-debt | rough enemies stage 1 runs on, a debt stage 2 pays (F 73, FW 131-137) | Enemy Sketch | | "enemy" English as in Enemy Fact; the debt is said in its entry |
| 15 | probe | a re-scan of the census through a different lens (F 81, FW 192-196) | Enemy Census Probe | rows 16 to 18 | built on Enemy Census, whole |
| 16 | lens | the angle a probe scans by; three, each mechanical (FW 193-210) | Enemy Census Probe Lens | | built on row 15, whole; 4 words |
| 17 | probe log | each probe's lens, stamps and findings, recorded in LAYER-1-ENVIRONMENT (F 82, FW 225) | Enemy Census Probe Log | | built on row 15, whole; 4 words |
| 18 | stamp, the three-stamp rule | one of three marks on every probe result: new fact, nothing new, out of scope (FW 212-216) | Enemy Census Probe Stamp | | built on row 15, whole; the rule is its entry |
| 19 | saturation | the census's exit: two consecutive lenses find zero new facts (F 27, 81; FW 223) | Enemy Census Saturation | | built on Enemy Census, whole |
| 20 | assumption hunt, silent singulars, silent successes, timeline stretched, resource lens | the three lenses and their moves (FW 198-210) | Label | | see question 4; whole Names would pass 5 words |
| 21 | the audit checklist | the human's four questions to check the framer's census (FW 218) | Enemy Census Audit Checklist | | 4 words |
| 22 | trust assumption, ASSUMPTION-n | a deliberate acceptance beside the facts, not defended (F 78, FW 82, 157) | Trust Assumption | | "trust" English |
| 23 | fence, NOT-OURS-n | a written-out scope exclusion that visibly stops facts at stage 3 (FW 83, 233; kill 44-70) | Scope Exclusion | | the workflow's own phrase; "fence" a figure |
| 24 | fence list, not-probed ledger, scope verdicts, the ledgers | the three lists the census's exit leaves (FW 231-246, WE 94) | English "list"; the items are rows 23, 25, 26 | | "ledger" a figure; whole Names would pass 5 words; see trigger 3 |
| 25 | what the not-probed ledger names | a door the census did not examine, named (FW 237-240) | Enemy Census Gap | | built on Enemy Census, whole |
| 26 | scope verdict, SYSTEM-BOUNDARY-n | a boundary question put as a named verdict: in, out, censused-and-fenced (FW 84, 241) | Scope Verdict | | "scope" English; its three values are labels |
| 27 | runtime ground, the ground | where the system runs: the machine, the instances, the store, the clock, the size; the definition's block names it, the work after framing establishes it (F 80, 230; FW 172-190) | Runtime Ground | | the method defines it; see question 8 |
| 28 | derivation doc, the derivation | `docs/system/framing/derivation.md`: how each stage ran, kept forever (F 98, 121) | CBC Framing Derivation | CBC Framing Derivation Appendix | built on CBC Framing, whole |
| 29 | escape valve | an appendix beside the derivation, for bulky sweep output only (F 137) | CBC Framing Derivation Appendix | | built on row 28, whole; "valve" a figure beside Escape Hatch |
| 30 | briefing | the problem as brought, committed unchanged at framing's start (F 100-105) | Run Briefing, the shared Name, CBC Run Briefing once renamed | | one thing: the container's entry is this text |
| 31 | residue filter | an export never refers to the derivation's machinery (F 153, 227) | CBC Framing Export Filter | | built on CBC Framing Export, whole; 4 words; see question 6 |
| 32 | agent language | words naming an Agent Skill, a workflow stage or the CBC Run's arrangement, refused in an export (F 156) | Agent Language | | "agent" English; defined where it stands |
| 33 | logged return trip, logged revision, revision entry | a dated change to an export: what changed, why, what triggered it, during framing and after (F 60, 199; FW 54-58) | CBC Framing Export Revision | | one thing, three words today; 4 words |
| 34 | draft line | a line on an export's top until the close (F 116) | English | | whole it would be 5 words, and "a draft line" says it plainly; see trigger 2 |
| 35 | demonstration mode | framing with reasoning fully visible, teaching the moves; every verdict still the human's (F 30) | Demonstration Mode | | names the mode it is |
| 36 | delegated-verdict mode | the human's verdicts handed to the agent by a recorded decision (F 37) | Delegated-Verdict Mode | | 2 words, the hyphen one |
| 37 | joint work, the mode | the default: the agent derives, the human gives every verdict (F 22-35) | English | | plain words; rows 35 and 36 are the Names |
| 38 | audience | who the claim is sold to, never a consumer of the running system (F 67, FW 107) | Falsifiable Promise Audience | | narrower than English; built on Falsifiable Promise, whole |
| 39 | Exit, Hands down, Hands up, Residue | each stage's closing parts (FW 119-121, 248) | Label | | parts inside a stage |
| 40 | tag | KIND-n, one spelling everywhere (FW 70-93) | English | | a label in plain words; each tag kind is a Name the CBC Run gives (F 109) |
| 41 | seam | the line between two Responsibility Areas, drawn or noted-not-drawn (F 88, FW 276, 286) | Responsibility Area Seam | | built on Responsibility Area, whole |
| 42 | division | a candidate Responsibility Area (F 87, FW 274) | English | | plain meaning |
| 43 | walk, walker, framer | a framing run, and whoever runs it (F 30, WE 14) | CBC Framing; "framer" English | | one thing |
| 44 | actor, the three negations (vanishes, duplicates, lies) | what a request touches beyond control, and how each fails (FW 144-147) | English; the negations Label | | plain meanings |
| 45 | chosen-next, open, in-progress, closed | the registry's status values (F 182) | Label | | values in backticks, keeping their case |
| 46 | presumption order, presumes | the order by what each proof takes as standing (FW 325) | English | | plain meaning, defined where it stands |
| | **The cbc-slice Agent Skill** | | | | |
| 47 | guarantee, GUARANTEE-n, strategy-free guarantee | one property, derived by attack, that the slice's invariant needs (S 79-82, SW 96-101) | Invariant Slice Guarantee | rows 48, 49 | see question 1 |
| 48 | guarantee's block | one guarantee's section of the record (S 28, record 53) | Invariant Slice Guarantee Block | | built on row 47, whole; 4 words |
| 49 | guarantee challenge | the attack on the invariant that yields the guarantees (S 79, WE 223) | Invariant Slice Guarantee Challenge | | built on row 47, whole; 4 words |
| 50 | evidence test | a test that creates the adversity and reads the witness (S 135, test 7, 22) | Evidence Test | Evidence Test Shape | already the Output Shape's base; "evidence" English, see question 7 |
| 51 | evidence criterion, EVIDENCE-n | what test would create a guarantee's adversity and show the invariant surviving (S 83, SW 104, record 76) | Evidence Criterion | | named before the test is built |
| 52 | witness | the state read from outside, where the truth is stored, that shows whether the invariant held (FW 116, S 139, test 97-103) | State Witness | State Witness Reading | says what is read |
| 53 | a reading | one read of the witness (S 138, test 97, 126) | State Witness Reading | | built on row 52, whole |
| 54 | the red, red run, seen red | an evidence test run with its wall absent, failing on the witness, in a state that never lands in history (S 141-160, SW 150, record 187) | Red Run | Red Run Tree | "red" the test term; the conditions are the method's |
| 55 | red tree | the working tree of a red run, where a race's pause may stand (S 156, SW 147) | Red Run Tree | | built on row 54, whole |
| 56 | backstop | what stands behind a wall, seen catching at the red run or unproven (S 157, SW 150, record 187) | Structural Wall Backstop | | built on Structural Wall, whole |
| 57 | the wall's own check | a test that sends a wall its refusal directly, or reads it where defined; not evidence (S 169, SW 166) | Structural Wall Check | | built on Structural Wall, whole; see question 9 |
| 58 | tripwire | a test that pins a decided option, not the promise; not evidence (S 166, SW 159, test 25, 56) | Decision Test | | says what it guards; "tripwire" a figure |
| 59 | structural owner | the one wall per guarantee (S 102) | Structural Wall | | one thing; concept chapter 02 |
| 60 | correctness spec, the spec, the specification | Stage 1's output: invariant, guarantees, evidence criteria, adversity model (S 92, SW 103) | Correctness Specification | | one thing, three words today; see question 2 |
| 61 | adversity model | the specification's part saying what attacks and how the evidence creates it (SW 104) | Adversity Model | | "adversity" English |
| 62 | adversity class | contention, duplicate delivery, partial failure (S 44, SR 39-53) | Adversity Class | | a fixed set of kinds |
| 63 | harness, adversity harness | the test machinery that can create the slice's adversity class, and fail (F 233, S 44-49, SR 39-63) | Adversity Harness | | the method defines what it must do; see question 8 |
| 64 | readiness, readiness checklist, readiness gate | the six checks before a slice opens (S 31, SR 1-83) | System Readiness; "Stage 0" a label | | the file's own title; one thing |
| 65 | the close | the moment a slice is closed in the registry with its answers (S 191, SW 179, record 55-57) | Invariant Slice Close | | see question 2 |
| 66 | slice record, the record | one record per slice, written as the stages go (SW 32-69) | Invariant Slice Record | Invariant Slice Record Shape | built on Invariant Slice, whole |
| 67 | escape-hatch hunt | Stage 2's search for paths around the wall (S 114, WE 242) | Escape Hatch Hunt | | built on Escape Hatch, whole |
| 68 | standing guards | three watches named at the close, one per failure mode (S 222-226, SW 206-216) | Standing Guard; each named by the concept Name it watches | | FINDING-813's figures go; no new Name per guard |
| 69 | provisionals, hand-ons | what a slice leaves provisional, and what it hands to later slices (S 192, 210; record 42) | English | | adjective and verb, rewritten as plain phrases |
| 70 | the opening | Stage 1's start, where a question the framing never answered is decided (S 74, SW 47) | English, "Stage 1's start" | | see question 2 |
| 71 | surface | what the guarantees need somewhere to live (S 119); the README as the exports' surface (F 204) | English | | two plain meanings; see question 6 |
| 72 | door | where the adversity arrives (S 72, SW 129) | English | | plain meaning |
| 73 | deviation, sign-off, working defaults, options weighed | (S 216, SW 218, record 88) | English; headings Label | | plain meanings |
| 74 | trusted writer, trust list | a writer the definition trusts (S 115, SW 122) | English | | built in plain words on Trust Assumption |
| | **The Output Shapes** | | | | |
| 75 | registry entry, entry | one slice's entry in the registry (entry 132) | Invariant Slice Entry | Invariant Slice Entry Shape | "registry" dropped: see trigger 4 |
| 76 | rider | a structural condition checked, never battle-tested, whose silent violation voids the evidence (entry 165) | Evidence Precondition | | says what it is; "rider" a figure; the field label goes with it in round 3 |
| 77 | flag, flag riding | the adversity cannot be created the normal way, and what the evidence does instead (S 94-96, entry 167) | Adversity Flag | | names what is flagged |
| 78 | Presumes, Judgment logged, Answered at close, Area, Kills covered | an entry's fields (entry 160-174) | Label | | fields of one entry |
| 79 | possession, collision, case, death | the Kill Shape's words (kill 9-65) | the concept's Names; "case" and "death" English | | "death" is what dies, said plainly in round 3 |
| 80 | `*Say:*` line | the line of real numbers under a kill or a claim (kill 72, record 69) | Label | | a field in its owner |
| 81 | Skeleton, Illustration | an Output Shape's two layers (kill 24, test 32, record 24) | Label | | see question 6 for "skeleton" |
| 82 | structural test | a test that reads the code (test 24) | Structural Wall Check | | see question 9 |

Triggers fired, each taken as proposed:

1. **CBC Framing Reconciliation (row 5).** Built whole, "the
   registry's fold-reconciliation line" is the Invariant Slice
   Registry Fold Reconciliation Line, 6 words, or the Invariant Slice
   Fold Reconciliation Line, 5. Proposed: CBC Framing Reconciliation,
   3: it accounts for every CBC Framing Concern, not only the folds.
2. **The draft line (row 34).** The CBC Framing Export Draft Line, 5
   words. Proposed: English; "a draft line" says it plainly.
3. **The ledgers (row 24).** The Scope Exclusion Enemy Census Ledger,
   5 words. Proposed: no Name for the lists; the items carry the
   Names, and "ledger" goes as a figure.
4. **The Registry Entry Shape (row 75).** The Invariant Slice
   Registry Entry Shape, 5 words. Proposed: the Invariant Slice
   Entry Shape, 4: an entry is an Invariant Slice's, and the registry
   is where every entry stands.
5. **The three lenses (row 20).** "The resource lens" built whole is
   the Resource Enemy Census Probe Lens, 5 words. Proposed: the three
   lenses and their moves are labels inside the Enemy Census Probe
   Lens's entry.

Questions the rule raised, each taken as proposed:

1. **Two meanings of "guarantee".** The concept's System Guarantee is
   a never-event against a named source (`docs/concept/00-cbc.md`);
   cbc-slice's GUARANTEE-n is one of several properties the slice's
   invariant needs, found by attack (S 79-82). Proposed: two Names,
   System Guarantee and Invariant Slice Guarantee.
2. **One name per cbc-slice stage (FINDING-815).** Proposed: the
   stages keep their labels, Stage 1 specify-correctness to Stage 4
   document; "the spec" and "the specification" become the
   Correctness Specification, Stage 1's output; "the close" becomes
   the Invariant Slice Close, the event at Stage 4's end; "the
   opening" becomes "Stage 1's start".
3. **"Definition" as a stage 6 stamp** clashes with System
   Definition, "the definition" in the same files. Proposed: the
   stamps become the labels "theorem" and "contract", since the
   workflow calls a definition contract-shaped.
4. **Labels or Names for parts inside one owner.** Proposed: the
   three lenses and their moves, stage 6's three passes, each
   stage's Exit, Hands down and Residue, an entry's fields, the
   status values, a scope verdict's values, an Output Shape's
   Skeleton and Illustration, and the `*Say:*` line are labels: they
   keep their case where they stand and get no Name.
5. **Figures renamed by what they do (rule 5).** Hostage test, mirror
   test, fence, escape valve, tripwire, rider and ledger. Proposed:
   the plain Names in rows 11, 13, 23, 29, 58, 76 and 24. The other
   way keeps the known word with an owner: System Possession Hostage
   Test, Scope Fence, Decision Tripwire, Evidence Rider. CBC Runs 4
   to 6's records keep the old words either way.
6. **One word, two meanings, in the same files.** "Residue" is stage
   0's banked rejections (FW 120) and the filter's (F 153); "surface"
   is the slices' cut, the code's minimum and the README; "skeleton"
   is a service (SR 21) and an Output Shape's layer. Proposed: the
   residue filter becomes the CBC Framing Export Filter and Residue
   stays a label; "slice surface" becomes the Invariant Slice
   Registry and "surface" stays English; "skeleton" stays English
   and Skeleton a label.
7. **Whether "evidence" is a Name.** The method gives it a narrow
   meaning: a passing test that creates the adversity ("No evidence,
   no closed slice", S 11). Proposed: English, its plain meaning
   proof; the Names are Evidence Test and Evidence Criterion.
8. **Harness, ground and bootstrap.** The method defines what the
   ground and the harness must be (FW 172-190, SR 39-63), so Runtime
   Ground and Adversity Harness are this group's; the stack's group
   names how its Agent Skills build them. "The bootstrap" (F 231, SR
   6) is the stack's cbc-bootstrap Agent Skill's work, and goes to
   the stack's group with FINDING-832's "system bootstrapped".
9. **A structural test and the wall's own check.** The Evidence Test
   Shape lists "a structural test, which reads the code" (test 24);
   cbc-slice's wall's own check "reads the wall where it is defined"
   (S 170). Proposed: one thing, the Structural Wall Check; the
   other way is two Names, the second the Code Rule Test.
10. **The briefing is the Run Briefing.** The container's entry is
    "the text that names the problem this project builds, read at
    framing and committed unchanged", the file cbc-framing commits at
    `docs/system/framing/briefing.md`. Proposed: one thing, written
    by the shared Name, CBC Run Briefing once commit 14 renames it.

Existing Names whose base this group changes:

- **The Slice-Record Shape** (so in `docs/glossary.md`; the file
  titles it the Slice Record Shape, `shapes/slice-record.md` line 5):
  the Invariant Slice Record Shape, 4 words.
- **The Registry Entry Shape:** whole, the Invariant Slice Registry
  Entry Shape, 5 words, a trigger; proposed the Invariant Slice Entry
  Shape, 4 words (trigger 4).
- **The Evidence Test Shape:** unchanged, 3 words; its base, Evidence
  Test, is row 50.

**DECISION-19's Names table: the stack's group.** Proposed
2026-10-31 from the Stack Group's files under
`delivery/spring-postgres/.claude/skills/`, under writing rule 9 as
it stands after ADR-0078's decision 12: a Name built on another
carries it whole, and past 4 words, every word counted, a shorter
true one is looked for; a hyphenated word counts as one. "English"
means the word stays lowercase, its plain meaning ours; a technical
term whose plain technical meaning is ours (Testcontainers, Flyway,
a role, a migration, a schema) is English. "Label" means a label
inside its owner, keeping its case, never a Name. "One thing" means
the word is another word for a thing that already has a Name, and is
rewritten to it. The concept's and the method's Names are in
`delivery/method/docs/glossary/method.md`, the shared ones in
`delivery/container/docs/glossary/container.md`, and are not
repeated. Files: B `cbc-bootstrap/SKILL.md`, AS
`cbc-bootstrap/references/app-structure.md`, BW
`cbc-bootstrap/references/spring-boot-walkthrough.md`, HR
`cbc-bootstrap/references/spring-harness-reference.md`, PC
`cbc-bootstrap/references/spring-pom-convention.md`, I
`infra-establish/SKILL.md`, EW
`infra-establish/references/establishment-walk.md`, RS
`infra-establish/references/postgres-role-split.md`, PW
`infra-establish/references/postgres-setup-walkthrough.md`, V
`infra-serve/SKILL.md`. Judged by the reviewer, 2026-10-31: every row and question's proposal taken.

| # | Word today | What it means (file:line) | Proposed | Built on it | Why |
|---|---|---|---|---|---|
| | **The cbc-bootstrap Agent Skill** | | | | |
| 1 | the bootstrap, bootstrap (as the work) | the work between CBC Framing and the first Invariant Slice: the stack settled, an empty running skeleton on the Runtime Ground, the Adversity Harness proven on one adversity (B 1-12; F 231, SR 6) | CBC Bootstrap | rows 3 to 8 | owner first, as CBC Framing; the method's table sent it here |
| 2 | system bootstrapped | the CBC Bootstrap's one exit (B 9, HR 3) | One thing: the CBC Bootstrap's end; "Exit test" a label | | a milestone of the work, not a thing of its own (FINDING-832) |
| 3 | requirements document, `bootstrap-requirements.md`, the requirements | Stage 2's contract: identity, capabilities, constraints, the ground's facts, the evidence owed, the exclusions (B 109-131, 197) | CBC Bootstrap Requirements | | built on row 1, whole |
| 4 | the harness's one proven adversity | the one Adversity Class the Adversity Harness is proven on at the CBC Bootstrap, read from the framing's own words (B 66-79) | CBC Bootstrap Adversity Class | | built on row 1 and the Adversity Class, whole; 4 words |
| 5 | probe, probe endpoint, contention probe, the probe pair | the scaffolding endpoint and test that prove the Adversity Harness creates the CBC Bootstrap Adversity Class; both die at the first Invariant Slice (B 98, 187; BW 184-196; HR 286-424) | CBC Bootstrap Probe; its endpoint and its test labels | | built on row 1, whole; "probe" alone clashes with the Enemy Census Probe |
| 6 | step plan | Stage 3's ordered plan, five steps, each one change with its verification and commit (B 133-147) | CBC Bootstrap Step Plan | | built on row 1, whole; 4 words; kept apart from the shared Plan Step |
| 7 | the exclusions | what the CBC Bootstrap does not build, each with its why (B 97-106, 186) | CBC Bootstrap Exclusion | | built on row 1, whole; "exclusion" alone now reads as the Scope Exclusion |
| 8 | the stack evaluation, the stack decision | Stage 1's choice of the stack by fluency and audience (B 59-65, BW 21) | English | | plain words, defined where they stand |
| 9 | initialization identity | group, artifact, base package, packaging, language version (B 81-83, 190) | Build Coordinates | | "identity" means a database login everywhere else; see question 2 |
| 10 | runtime identity, the runtime role, runtime | the database role the running application connects as, and nothing else (B 64, 86, 92; RS 32; HR 133) | Label: the `runtime` role | | a role name inside the Database Role Split, row 33; see question 2 |
| 11 | migrations home, one home | the one directory holding migrations, empty at the CBC Bootstrap (B 65, 89, 94; HR 128-161) | English: "the migrations directory" | | "home" is a fact's home elsewhere; see question 3 |
| 12 | zero-applied assertion, migration-path test, `MigrationPathIT` | the test that proves the migration path runs and applied none at the CBC Bootstrap (B 89; HR 41, 200-284) | Migration Path Test | | HR §3's own title; "migration" English |
| 13 | harness, evidence harness, the harness bases | the Adversity Harness as this stack builds it (B 4, 66, 87; HR 1-41) | One thing: Adversity Harness | | the method's Name |
| 14 | the database base, the evidence tier | the harness's two layered test bases, `DatabaseIT` and `WebDatabaseIT` (HR 39-40, 45, 162-199) | Label: by class name | | parts inside one owner; "tier" has three senses (FINDING-852) |
| 15 | the ground, established ground | the Runtime Ground as stood up and verified (B 2, 42, 49; I 9-14) | One thing: Runtime Ground | | the method's Name |
| 16 | the skeleton, empty-but-running skeleton | the running application with no business behavior, wired to the Runtime Ground (B 3, 46; BW 35) | English | | as the method's table left "skeleton"; a walking skeleton is technical English |
| 17 | capability, capability set | what the system must be able to do at the CBC Bootstrap, typically four (B 84-91; PC 21) | English | | plain meaning; the list is the CBC Bootstrap Requirements' §2 |
| 18 | constraint (in the CBC Bootstrap) | a rule the code must keep, cited against the Infrastructure Contract (B 92-96) | English | | plain meaning; the ground's own is row 26 |
| 19 | the log, the project's log, the CBC Run's own log | where a decision is recorded (B 62; AS 8, 63, 67; BW 23; HR 415) | English: "an ADR" | | FINDING-919: a CBC Run records decisions as ADRs |
| 20 | executor | whoever writes the application code (AS 107; HR 23, 427, 470) | One thing: CBC Run | | FINDING-850 |
| 21 | the builder | who reads the CBC Bootstrap Requirements and the Infrastructure Contract to build (B 61, 110; I 89) | English | | plain meaning |
| 22 | certify, certified | Stage 5's check against the delivered state, member by member (B 172-200) | English | | plain meaning |
| 23 | Exit test, exit records, Bound facts, Outcomes it realizes, Variation points | headings and closing parts inside their files (B 194, 215; HR 121, 442) | Label | | parts inside one owner |
| 24 | problem area | what one package holds: everything that area needs (AS 40) | One thing: Responsibility Area | | see question 4 |
| 25 | package-by-feature, classic layered, hexagonal, vertical slice, modular monolith | named architecture styles (AS 22, 85-100) | English | | technical English; see question 5 for "vertical slice" |
| | **The infra-establish and infra-serve Agent Skills** | | | | |
| 26 | Execution Environment, the environment decision | the local runtime host for infrastructure (EW 162; I 65; EW 21) | Execution Environment | | the walk's own Name (FINDING-896); the lowercase uses take it |
| 27 | Infrastructure Service, the service set | a capability provided to the system (EW 164; I 72) | Infrastructure Service | rows 28 to 30 | the walk's own Name (FINDING-896) |
| 28 | Infrastructure Service Constraint, constraint | a requirement or limit put on an Infrastructure Service, each naming its enforcement (EW 165; I 78) | Infrastructure Service Constraint | | the walk's own Name; 3 words |
| 29 | not-provisioned list, exclusion | a service refused, with its why, in Stage 2's evaluation (I 74-77; V 26) | Infrastructure Service Exclusion; the list English | | built on row 27, whole; the items carry the Name, as the method's ledgers |
| 30 | re-entry | a service added, changed or removed on an established Runtime Ground, by the same need-led evaluation as one logged decision (V 1-30; I) | Infrastructure Service Re-entry | | built on row 27, whole; 3 words |
| 31 | the establishment, the walk, establishment walk | infra-establish's work, Stage 0 to Stage 7 (I 9-90; EW 1) | Infrastructure Establishment; the walk's sections Agent Skill Stages | row 32 | owner first; FINDING-897: "Stage 5" everywhere |
| 32 | establishment log | `docs/infrastructure/establishment-log.md`, kept only by a repo without records (I 114, 124; V 21) | Infrastructure Establishment Log | | built on row 31, whole; 4 words |
| 33 | role split, authority split, authority model | database authority as a grant-enforced property: `migrator` owns structure, `runtime` writes data (RS 1-45; HR 133; BW) | Database Role Split | | RS's title; "authority" see question 6 |
| 34 | `migrator`, `runtime`, structure authority, data authority | the Database Role Split's two roles (RS 26, 32) | Label | | role names in backticks |
| 35 | bootstrap identity | the admin login that runs the setup once and owns the database, never wired in (RS 42; PW 161) | Database Setup Identity | | "bootstrap" would mean the CBC Bootstrap; see question 1 |
| 36 | bootstrap SQL | `infrastructure/bootstrap.sql`, the Database Role Split made real (PW 58; HR 128) | Label: by its path | | a file; see question 1 |
| 37 | catalog check | real state queried against the model's claims, the expected result beside each query (I 83; PW 110) | Catalog Check | | the Stage 5 gate's own name |
| 38 | behavioral check | the Infrastructure Service Constraint attempted and watched being refused, live (I 84; PW 117) | Behavioral Check | | its pair; "both ways" is the two together |
| 39 | verify suite, verification suite | `infrastructure/verify-database-model.sql` (I 120; PW 73) | Label: by its path | | a file |
| 40 | infrastructure contract | the builder-facing manual: identities, reachability, refusals, how schema changes are made (I 89, 140; V) | Infrastructure Contract | | used as a document |
| 41 | operator manual | the human's stand-up-and-use manual, written from the lived setup (I 89, 148; B 43) | Operator Manual | | used as a document; not a Convention Manual |
| 42 | lived default, rebuttable default | the choice a stack reference makes unless a demand or an environment fact defeats it: podman local containers, compose-driven; package-by-feature (I 1; EW 37; AS 20; V 44) | Stack Default | | "lived" is a coined adjective (FINDING-916); see question 7 |
| 43 | standing knowledge, governing knowledge | a reference already written, used as the Stack Default (V 44; EW 79-116) | English: "the reference" | | FINDING-892 |
| 44 | enforcement mechanism | what makes an Infrastructure Service Constraint hold: the database's grants, a config, a Structural Wall (I 78-81) | English | | plain meaning |
| 45 | lever | what the evidence does to the ground: start several instances, kill one, freeze the store (I 68; EW 31-36) | English, rewritten as FINDING-882 proposes | | a figure; proven where the Adversity Harness is built |
| 46 | witness read | reading the stored state from outside (PW 172) | One thing: State Witness Reading | | the method's Name |
| 47 | the definition, the intent, the registry, framing artifacts | (I 27-36; EW 8-18) | One thing: System Definition, CBC Framing Intent, Invariant Slice Registry, CBC Framing Export | | the concept's Names |
| 48 | door, real door | where the adversity arrives (B 85, 217; BW 190-222; HR 42-486) | English | | as the method's table row 72 |
| 49 | lived, unlived, honestly empty, proof of life, world is up, decision surface, receipt, seam, two-seat, load-bearing | figures and coined adjectives (FINDING-830, 834, 844, 913 to 918) | English, rewritten as each finding proposes | | not Names; "receipt" and "seat" would read as Receipt Branch and Convention Seat |
| 50 | stand up, reset path, grant boundaries, project-named schema, test companion, earning reason | (I; PW 142; RS 46, 55; PC 20-24) | English | | technical or plain meanings |

Triggers fired:

None. The longest Names are 4 words: the CBC Bootstrap Adversity
Class, the CBC Bootstrap Step Plan and the Infrastructure
Establishment Log.

Questions the rule raised, each taken as proposed:

1. **Two meanings of "bootstrap".** The cbc-bootstrap Agent Skill's
   work (row 1) and the database's one-time setup: the bootstrap SQL
   and the bootstrap identity (rows 35, 36). Proposed: CBC Bootstrap
   for the work; the setup's identity becomes the Database Setup
   Identity, and its file is written by its path. The other way keeps
   "Database Bootstrap Identity", 3 words, with "bootstrap" in two
   senses.
2. **Three meanings of "identity".** A database login (the `runtime`
   role, the Database Setup Identity), and the Maven project's
   coordinates (row 9). Proposed: "identity" stays English for a
   database login; the coordinates become Build Coordinates; the two
   roles are labels by their names.
3. **"Home" for the migrations directory.** One-home calls the place
   a fact lives its home, and a CBC Run reads it so. Proposed:
   English, "the migrations directory".
4. **Whether a "problem area" is a Responsibility Area.** AS 40 puts
   one package per problem area, "the package list reads as the
   problem's table of contents". Proposed: one thing, Responsibility
   Area; the other way is English, a package by feature.
5. **"Vertical slice" beside the Invariant Slice.** AS 94 names an
   architecture style. Proposed: English, written "vertical-slice
   architecture", so "slice" never stands alone there.
6. **Two meanings of "authority".** The concept's: which facts the
   system is the single authority on (System Definition). The
   Database Role Split's: which role may change structure or data.
   Proposed: both English, each defined where it stands; the role
   split's is always written with its role.
7. **"Lived default".** Proposed: the Stack Default, the default a
   stack's references carry; whether a CBC Run has lived it is said
   in plain words. The other way keeps the known word: Lived Default.

Existing Names whose base this group changes:

- None. The shared Stack Overlay and Stack Group are built on
  "stack", which stays English.

**DECISION-19's Names table: the Agent Model's group.** Proposed
2026-10-31, under writing rule 9 as the three groups before it. Three
parts: the Agent Model's own words, `docs/models/agent.md` (AM); the
Names the refinement's decisions gave, DECISION-23 and 32; and the
Names 12c's whole-Name rule renames (ADR-0078, decision 12). "Ours"
or "shared" says which glossary holds the entry: `docs/glossary.md`
only, or also `delivery/container/docs/glossary/container.md`.
FINDING-507's decline reverses: the six channel titles take their
Names, with the rename grep. Judged by the reviewer, 2026-10-31:
every row and question's proposal taken.

| # | Word today | What it means (home) | Proposed | Built on it | Why |
|---|---|---|---|---|---|
| | **The Agent Model's words** | | | | |
| 1 | channel | how text reaches the agent's context window, by when it fires and what it guarantees (AM §4) | English | rows 2 to 7 | its plain meaning, a way a message travels; see question 1 |
| 2 | ambient | entry files loaded at session start (AM §4.1) | Ambient Channel | | the model's word, now a Name; §4.1 retitled |
| 3 | pulled | a file the agent reads because it decided to (AM §4.2) | Pulled Channel | | as row 2 |
| 4 | pushed | text put in context at a moment the agent did not choose (AM §4.3) | Pushed Channel | | as row 2 |
| 5 | told | a human says it in the session (AM §4.4) | Told Channel | | as row 2 |
| 6 | observed | the results of commands the agent runs (AM §4.5) | Observed Channel | | as row 2 |
| 7 | installed | files that work by existing, delivering nothing to the window (AM §4.6) | Installed Channel | | the model counts it the sixth; as row 2 |
| 8 | the gate | enforcement outside the text: a hook, CI, a human review (AM §7) | Enforcement Gate | | "gate" has a second meaning; see question 2 |
| 9 | binding | one tool's mechanisms for the channels and the gate, Layer 2 (AM §10) | Tool Binding | | owner first; §10 retitled *The Tool Bindings* |
| 10 | Layer 1, Layer 2 | the model's vendor-neutral layer and the bindings' layer (AM opening, §10) | Label | | see question 4 |
| 11 | context window, role | everything the agent knows now; the harness's three roles (AM §5) | English | | technical English |
| 12 | write-back | what the agent leaves in the repo (AM §2, §6) | English | | technical English: writing back to the store that lasts |
| 13 | claim, A1, W2, S1, G1 | a behavioural statement with its status and refutation condition; its id (AM §12) | English; the ids Label | | plain meaning; the ids keep their case |
| 14 | the repo | the only durable memory (AM §2) | English | | plain meaning |
| | **The Names the decisions gave** | | | | |
| 15 | entry file | the file a tool loads at session start, `CLAUDE.md` (AM §4.1) | Entry File, shared | | DECISION-23; 107 uses |
| 16 | living text | text that is kept true, as opposed to history (`docs/conventions/facts-in-sync/` §1) | Living Text, shared | | DECISION-23; the container's one-home Agent Rule uses it |
| 17 | receipt branch | the branch a delivery lands on, so the branch is its manifest (ADR-0018) | Receipt Branch, ours | | DECISION-23; see question 3 |
| 18 | the base | the stack-agnostic hygiene files, beside the Stack Overlays (`docs/conventions/repo-hygiene/`) | Hygiene Base, ours | | DECISION-23 |
| 19 | skill | a file under `.claude/skills/<name>/` | Agent Skill | | DECISION-32; entered at commit 4 |
| | **The Names the whole-Name rule renames** | | | | |
| 20 | Run Ask | a line in a CBC Run's backlog addressed to us | CBC Run Ask, shared | | built on CBC Run, whole |
| 21 | Run Reading | us reading a CBC Run since we last did (`docs/conventions/exchange/` §6.3) | CBC Run Reading, ours | | as row 20; see question 5 |
| 22 | Run Birth | a CBC Run's first state | CBC Run Birth, ours | | as row 20 |
| 23 | Run Briefing | the text naming the problem a CBC Run builds | CBC Run Briefing, shared | | as row 20 |
| 24 | Run Hand-off | the text a Newborn Run's agent reads to begin | CBC Run Hand-off, shared | | as row 20 |
| 25 | Newborn Run | a CBC Run at its birth | Newborn CBC Run, ours | | as row 20 |
| 26 | Approach Stage | one phase of an Approach on Trial | Approach on Trial Stage, ours | | built on Approach on Trial, whole; "approach" alone is also Work Approach's |

Questions the rule raised, each taken as proposed:

1. **Whether "channel" is English.** Its meaning here is the plain
   one, a way a message travels, so the six Names are Ambient
   Channel to Installed Channel. The other way is a Name, Agent
   Channel, and the six built on it whole: Ambient Agent Channel, 3
   words each.
2. **Two meanings of "gate".** The Agent Model's is enforcement
   outside the text; a Plan Step's is its exit criteria (`PLAN.md`,
   *Gate*), 67 uses of "the gate" between them. Proposed: two Names,
   Enforcement Gate and Plan Step Gate, the second ours and shared;
   each use is read by hand in round 3's work.
3. **Receipt Branch's home.** ADR-0018 holds the fact and no manual
   does; DECISION-23 said the Exchange Convention gains it. Proposed:
   the exchange manual gains one sentence in this group's glossary
   commit, so the entry points at a living home.
4. **Layer 1 and Layer 2 beside the System Layer and the Refinement
   Layer.** Proposed: labels inside the Agent Model, written "the
   Agent Model's Layer 1" outside it.
5. **The Run family's homes are titles.** Exchange §6.3 *The Run
   Reading* and §6.4 *How a Run Reading closes*, the exchange-reading
   and working-a-reading Agent Rules' titles, and the refinement
   Approach on Trial's §2 *The Approach Stages* hold the old Names.
   Proposed: each retitled in this group's commits, *The CBC Run
   Reading*, *How a CBC Run Reading closes*, *The Approach on Trial
   Stages*, with the rename grep; the other uses wait for round 3's
   work.

**DECISION-20.** Rule 10's reach. Rests: FINDING-303, 368, 379, 380,
454, 471, 472, 507, 517, 537, 596, 665, 666, 826, 827 and 922.
- (a) The rule's letter: numbered sections and parts, in both
  Convention Seats. Outside it: unnumbered headings in skills,
  references and chapters (826, 827, 537); tag-numbered sections,
  READINESS-n and LAYER-n (826, 537); the Agent Model's lowercase
  channel titles, its own words (507); a Conversation Memory part's
  heading, history (596); the refinement's Approach Stage headings,
  §2.1 to §2.10, as a stage heading is (666). A comma that joins a
  gloss is a gloss, so *One cycle, drawn*, *Use, drawn*, *Two Plan
  Steps, not one*, *A convention, not a record*, *Detachable, and kept
  so*, *Down, an idea to an output* and *What it reads, and its words*
  become one phrase each (368, 454, 471, 517, 665). A numbered section
  titled by a fixed heading's words, conventions §2.2 *What it is
  for*, §2.7 and §2.8, is relabelled to stand alone, *The need*, *The
  channel*, *The boundary* (303). An imperative read as a label that
  names its subject stands: *Commit on the word*, *Nothing fetched*,
  *Why it is shaped this way* (379, 380, 472).
- (b) Wider: every heading a Fact Reference can name.
- (c) Narrower: numbered sections only, comma titles as they are.
- Recommended: (a). Under it 303, 368, 454, 471, 517, 665 and 922 are
  fixed, the rest declined.
- Chosen: (a), by the reviewer, 2026-10-30, as recommended. A rule
  the round reads against is not widened mid-round (§2.4, *Reading the
  Finding Kinds*). The rule's reason, that a title is read in every
  reference to it, reaches an unnumbered heading too; the readers
  found references cutting a skill's heading short. Whether rule 10
  widens is for after the round.

**DECISION-21.** Whether rule 9 reaches drawn text. Rests:
FINDING-313, 394, 465, 466, 511, 524, 548, 773 and 798: pictures,
legends, Mermaid labels, a drawing's boxes, a code-block table.
- (a) It reaches every line. A drawing or code block writes the Name
  where its box has room; where it does not, one line above the
  drawing says which short word stands for which Name.
- (b) Drawn text is outside the rule: its words are labels.
- Recommended: (a). A reader of the exchange's legend meets "the run"
  with the same doubt as in prose, and the legend has room.
- Chosen: (a), by the reviewer, 2026-10-30, as recommended. The nine
  findings are fixed: the Name where its box has room, a one-line key
  above the drawing where it has not.

**DECISION-22.** A Markdown mark on a Name at its defining line.
Rests: FINDING-405, 474, 494, 626, 639 and 722; and bold on a coined
label, 718 and 730.
- (a) No mark, as rule 9 says; the glossary's bold is the list's
  form, and the capitals already mark a Name.
- (b) Bold at the one defining line is allowed; the rule gains the
  exception at the round's close.
- Recommended: (a). All eight fixed.
- Chosen: (b), by the reviewer, 2026-10-30, on the agent's changed
  recommendation after the reviewer asked why not. Capitals show a
  word is a Name at every use; bold at the defining sentence shows
  where it is defined, its one home made visible, and a retelling
  does not bold. Checkable: each bold Name is bold once in all living
  text, in the file its glossary entry points at. At the home the bold
  stays: FINDING-405's six, 474, 494, 722. Elsewhere it goes: 626, the
  `commit-plan` skill's Change Set; 639, `exchange-read`'s Delivery
  Pin. 718 and 730 are coined labels, not Names, judged with
  DECISION-19's renames. Rule 9 and its manual gain the line at the
  round's close; the work leaves the home bolds in place.

**DECISION-23.** Lowercase phrases for defined things with no Name.
Rests: FINDING-339 and 367, "the entry file", "the records table", "the
map"; 284, "the chain"; 301 and 364, "registry"; 363 and 503, "the
handbook"; 625, "the working arrangement"; 664, "living text"; 640,
"receipt branch"; 440, "the base".
- (a) English, each, where the English meaning is ours: entry file,
  records table, the map, the chain, registry, the base, working
  arrangement, as the glossary's header says and the pass left them.
  "The handbook" is a proper name, said in plain words once per file
  where first met, "the handbook, the repo this arrangement came
  from, now history (ADR-0038)". "Living text" and "receipt branch"
  have no English meaning and get Names: Living Text, its home
  facts-in-sync §1; Receipt Branch, its home the Exchange Convention,
  which gains the fact from ADR-0018.
- (b) Names for all.
- (c) English for all, "the handbook" introduced in plain words.
- Recommended: (a).
- Chosen: a revised (a), by the reviewer, 2026-10-30, on the agent's
  recommendation judged again by DECISION-19's test, a word a text
  gives a meaning English does not, and a second question, whether
  the word clashes with a Name already held. Names: Entry File, 107
  uses; Living Text, its home facts-in-sync §1; Receipt Branch, its
  home the Exchange Convention, which gains the fact from ADR-0018;
  Hygiene Base, beside Stack Overlay. Plain words, for a clash: "the
  map" written `ARCHITECTURE.md`, beside Local Map; "the chain" said
  as the order the conventions act in, beside Chain Link; "registry"
  outside the slice registry, a trace of the old conventions
  registry, said as the birth entry's list of conventions. English:
  records table, working arrangement. "The handbook" said in plain
  words once per file where first met. The Names enter their glossary
  groups by DECISION-19's shape.

**DECISION-24.** A convention named by its bare hyphenated word.
Rests: FINDING-291, 338, 376, 487, 508, 551, 595, 631, 662 and 678.
The glossary's header says a convention is named by its path in
backticks or by its Name; the pass decided "a label or its Name, never
the bare word" (devlog 2026-10-30), and the writing manual itself
writes "commit-messages' rule".
- (a) The hyphenated folder word is the convention's label and stands
  bare: commit-messages' rule, project-recording's. The header line
  says so: by its label, the folder's word; by its path in backticks;
  or by its Name. A one-word convention, exchange, shapes, writing,
  conventions, retrospective, is only ever its path or its Name,
  since the bare word is English: "the exchange manual", "the shapes
  manual", "the arrangement", "the stack practice" and "the
  conventions manual" change.
- (b) The path in backticks or the Name only, as the header reads
  today: 16 lines in layer 4 alone.
- (c) Backticks on the label.
- Recommended: (a).
- Chosen: a revised option, by the reviewer, 2026-10-30, after asking
  what a convention is (DECISION-32). Three conventions share their
  name with an artifact: commit-messages, commit-plan and
  visual-comparison. Where a label could mean either, the sentence
  writes the kind: "the commit-messages manual" for the top level,
  "the commit-messages Agent Skill" for the skill, as an Agent Rule
  is written; never "approach", which would clash with Work Approach
  and Approach on Trial. Where a label has no clash, the bare
  hyphenated word stands: project-recording's, facts-in-sync's. A
  one-word convention, exchange, shapes, writing, conventions,
  retrospective, is its path or its Name, since the bare word is
  English: "the exchange manual" and the like change. In a shipped
  file "manual" is not written but beside a Fact Reference the CBC Run
  is not asked to follow. Agent Skill is a new Glossary Name; its
  reach, every use of "skill" for the file or only where a label
  clashes, is DECISION-32's design. The glossary's header gains the
  line at the round's close.
- Widened by the reviewer at DECISION-27, 2026-10-30: the kind word is
  written always, not only where a name clashes.

**DECISION-25.** How a Skill Stage or an Approach Stage is written
outside its owner, and an Approach Stage's case. Rests: FINDING-571,
652, 773, 798, 803, 807, 897 and 920.
- (a) "Stage N" inside its owner, and outside it with the owner named,
  "`auto-run`'s Stage 4", as the glossary writes "`cbc-slice`'s Stage
  3"; an Approach Stage the same as a Skill Stage; the rule's "the
  walk's step 3" stays for a walkthrough's numbered steps.
- (b) Lowercase outside the owner, "the framing's stage 3", as the
  rule's examples read.
- Recommended: (a). One case for one kind of thing; the glossary
  already writes it.
- Chosen: (a), by the reviewer, 2026-10-30, as recommended. The
  eight findings are fixed.

**DECISION-26.** Which figures are dead. Rule 5's 109 findings rest on
a reading of each figure; the reviewer decides each word once, here.

| Figure | Findings | Recommended |
|---|---|---|
| rides, ride, riding, for "is in", "goes with" | 287, 366, 569, 610, 632, 683, 713, 912 | fix: the plain verb |
| the front door, for README | 314, 592, 606 | fix at its home, project-recording §1 and §7; `CLAUDE.md`'s rows in both seats and TODO follow |
| projection follows truth; projection, projectable | 324, 564, 699, 886 | fix: "says only what is true"; "derived from" |
| the spine | 315, 556, 642 | fix |
| costume, dressed as, wearing clothes | 295, 359, 538, 612 | fix |
| theatre: the stage not a victim, a third act, acts, movements, scene, film | 329, 464, 530, 737, 791 | fix; the three standing guards' names (813) and the four failure-mode labels (531) stay as the method's words |
| journey: rolling wave, horizon, road, return trip, travels, the walk | 316, 628, 629, 696, 760, 806, 889 | fix |
| debt, bank, park, pays off | 761, 787, 789 | fix |
| graveyard, swamp, lab notebook, distillation, save-point, empties your head | 321, 322, 333, 701, 702 | fix, both seats' Record Stub headers alike |
| swallow, archaeology, binary blob, hedge | 378, 401, 458, 479, 636 | fix |
| floor and ceiling | 294, 613 | fix |
| master, masters, as a verb or a fact's home | 774, 911 | fix: "owns", "home" |
| honest, honestly, of a file | 913 | fix |
| dies, death, of scaffolding | 915 | fix; "born" stays |
| door, the boundary | 910 | keep where it is the concept's word; fix the four other senses |
| lens, stamp, ledger, probe | 790 | keep as the method's words (DECISION-19) |
| load-bearing | 335, 480, 914 | keep: dead in technical English |
| day zero; fighting a notation | 442, 480 | keep: dead, and ADR-0027's own words |
| stands on, holds, carries, lands, fires, harvest, blind, seeded, downstream | not listed | keep |

Recommended: as the table. The rest of rule 5's findings name one
figure each and take the reader's proposal.

Chosen: the table, by the reviewer, 2026-10-30, with two rows
corrected, since both were written before DECISION-19 took (b). The
theatre row's exception, the three standing guards' names (813) and
the four failure-mode labels (531): they stay, and DECISION-19's
design gives them Names. The row "lens, stamp, ledger, probe" (790):
not judged as figures here; they wait for DECISION-19's design, which
names them.

**DECISION-27.** A skill's name in prose. Rests: FINDING-587, 631, 767
and 921: "cbc-slice", "the cbc-slice skill", bare.
- (a) Backticks, `cbc-slice`: a path's last part, written as it is;
  both glossaries do.
- (b) Bare, as a label.
- Recommended: (a).
- Chosen, by the reviewer, 2026-10-30, after the agent had
  recommended declining the four as taste: neither form. A skill is
  written with its kind word, always, as DECISION-24 now reads: "the
  cbc-slice Agent Skill", "the one-home Agent Rule", "the
  commit-messages manual"; a numbered line as "writing rule 9"; a
  path, as a Fact Reference, whenever the sentence points at where a
  fact is written. The four findings are fixed so, and the shape
  reaches every name of an agent part in living text, 166 skill names
  in backticks among them. A form with a slash, /cbc-slice, was taken
  and then dropped for simplicity the same day.

**DECISION-28.** The shipped glossary's missing Names. Rests:
FINDING-644 and 723, Run Reading, used in two shipped texts; 646,
Approach Stage, used in the shipped `approach-drafting.md`.
- (a) Both enter `delivery/container/docs/glossary.md`, one plain
  sentence each from the CBC Run's side.
- (b) The two texts say it in plain words instead.
- Recommended: (a). The CBC Run meets both words as Names.
- Chosen: (a), by the reviewer, 2026-10-30, with a gap the reviewer's
  question found: Approach Stage has no defining home. Our glossary
  points at `approach-drafting.md` §*Stages*, which uses the word and
  never says what one is. So one sentence there defines it, as the
  conventions manual §1.4 defines Skill Stage, in our copy and the
  shipped one, one text; the CBC Run's entry then points at its own
  copy. Run Reading enters the CBC Run's glossary as a follower of
  `docs/conventions/exchange/` §6.3, *The Run Reading*, standing alone,
  since a CBC Run cannot open that home. Both are shared Names, in the
  container's glossary by DECISION-19's shape.

**DECISION-29.** `CBC ADR` citations mid-sentence and in Skill
Templates. Rests: FINDING-924, 20 lines in 18 files; 842.
- (a) A Skill Template, like a Record Stub, cites nothing: its header
  keeps "Skill Template — the Master Copy is in
  correctness-by-construction" without the citation; a citation in a
  skill's or reference's body moves to the file's *Decisions* footer,
  or goes where the footer already lists the ADR. Conventions §1.1
  names the template at the round's close.
- (b) A template header keeps its citation as provenance, and §1.1
  says so.
- Recommended: (a).
- Chosen: a wider (a), by the reviewer, 2026-10-30, on the reviewer's
  point that decision numbers are ours: we need them to change a
  shipped file, and a CBC Run can neither open them nor needs them to
  change its copies. Stripping them at the seed was weighed and not
  taken: a CBC Run's copy equals the Master Copy at its Delivery Pin,
  which every diff of the exchange rests on. Taken instead: shipped
  files carry no decision citation at all, their *Decisions* footers
  included, in the Master Copy itself; the why is reached through the
  Foundation Line, the manual and its ADRs. Our files that never ship
  keep their footers, `ADR-nnnn`. The cost: a grep for an ADR finds
  the manual's section, not the shipped file's; the Foundation Check's
  walk from the manual keeps the link. A design change: the
  conventions manual §1.1, *How a rule is written*, and ADR-0069
  change, built with DECISION-32's design after the decisions.
  FINDING-924 and 842 are fixed by it.
- Reversed by the reviewer at the design's question 10, 2026-10-31,
  ADR-0078: our Master Copies keep their footers, and every delivery
  strips them, in the Pure Seed and in `exchange-deliver`, and before
  `exchange-read` compares. One rule for citing a decision, in
  facts-in-sync §3: a citation in a Work Approach's sentence moves to
  its footer, so the shipped 20 go there and are stripped on the way.

**DECISION-30.** Whether a record's form is held to rules 2 and 3.
Rests: FINDING-605, a record header's comment; 700 and 709, the Record
Stubs' headers, both seats; 692, the playbook's Goal lines; 828, a
skill's description line; 573, the Plan Step Form's close item with
three checks.
- (a) Every line is under the rule. A Goal stays one sentence, as the
  form says, its parts labelled inside it where it has them; a
  description line stays one paragraph, as Claude Code reads it, in
  short sentences; a header comment and a close item are split like
  prose.
- (b) A form's fixed lines stand outside the rule.
- Recommended: (a).
- Chosen: (a), by the reviewer, 2026-10-31, as recommended: the agent
  reads these lines more often than most, so their voice is the one it
  copies. The six findings are fixed within the shape each line keeps.

**DECISION-31.** `ARCHITECTURE.md`'s seven area titles and the
references cut at their dash. Rests: FINDING-285, 341 and 617, and
the pass's decision that kept the titles with their paths. Three
readers found the cut title, *The conventions…*, against rule 6 and
facts-in-sync §3.1, which allows a cut for a numbered rule's bold
lead only.
- (a) The seven titles lose their gloss, the path going to the first
  line of each section; every Fact Reference carries the title whole;
  the rename grep fixes about 30 references.
- (b) The titles stay, and the cut with "…" becomes the settled form
  for a title with a gloss, said in facts-in-sync §3.1.
- Recommended: (a). The pass kept the titles for their paths; the
  readers show the cost lands on every reference.
- Chosen: (a), by the reviewer, 2026-10-31, as recommended. The count
  above was wrong: 15 references in 6 files, not about 30. The seven
  titles lose their gloss, each path going to its section's first
  line; the 15 references carry the title whole; this reverses the
  pass's decision for these seven.

**DECISION-32.** What a convention is. Raised by the reviewer at
DECISION-24, 2026-10-30. Rests: DECISION-24's wording; every text that
names a convention or its artifacts. The Idea-to-Output Model has a
convention as two texts, its manual and its artifacts
(`docs/models/idea-to-output.md` §6.1, *Two texts*), and so spans two
levels of its own chain: the manual is a Canonical Description, a
skill a Work Approach.
- (a) A convention is the manual's level: the way of working, written
  in its manual. Its Agent Skills, Agent Rules and forms are Work
  Approaches made from it, one level down, each pointing up by its
  Foundation Line; a manual points down only in its list *What this
  is made usable as*. A CBC Run holds no convention, only approaches
  made from ours.
- (b) As today: a convention is the manual and its artifacts.
- Chosen: (a), by the reviewer, 2026-10-30. A design change to an Idea
  Model (`.claude/approaches-on-trial/refinement.md` §2.7, *Working
  the findings*): an ADR, the Foundation Check's walk from
  `docs/models/idea-to-output.md` §6 to the conventions manual §1 and
  what stands on them, built with DECISION-19's design after the
  decisions. It also settles Agent Skill as a Name for a skill file,
  beside Agent Rule; its reach is every use, by DECISION-27: 603
  lines in 79 living files say "skill" today, 81 of them inside Skill
  Stage or Skill Template.
- Widened by the reviewer at DECISION-27, 2026-10-30: a convention and
  a Work Approach never share a name. Five do today: commit-messages,
  commit-plan, visual-comparison and retrospective, a manual and an
  Agent Skill each; writing, a manual and an Agent Rule. The design
  chooses which side is renamed. A rule that would choose: a manual is
  named by its subject, an Agent Skill by what it does, as
  exchange-read and exchange-deliver already are. Renaming an Agent
  Skill reaches every CBC Run that holds it; renaming a manual moves
  its folder and every Fact Reference to it, on our side only.
- Narrowed by the reviewer at the design's question 8, 2026-10-31:
  the five shared names stay for now, kept apart by the kind word; a
  new name never repeats one already used, checked by grep, and a new
  Agent Skill takes a verb. The renaming is TODO's "Rename the
  manuals, Agent Skills and Agent Rules that share a name", due when
  the Run Readings of CBC Runs 4, 5 and 6 have closed.

### Met in round 3, of other kinds

Not round 3's kind: a stale line, two texts that disagree, a fact with
no living home, a form slip. Listed so the work can fix them where it
touches the same file, or the last read (§2.9) takes them. Each is a
reader's, as written.

- `docs/conventions/project-recording/README.md` lines 767–769: the §13 note says renumbering "would break those citations"; `docs/conventions/facts-in-sync/` §3.3, *The rename grep*, says a renumbering greps and fixes every Fact Reference in the same commit. The note's reason is stale against that manual; whether §13 keeps its number is a separate question.
- `docs/conventions/conventions/README.md` §3 carries two *Its story* lines (lines 284 and 288, the second inline at a paragraph's end); the manual form asks one italic line per lesson, where it happened.
- `docs/conventions/project-recording/README.md` §8.1 and §8.4 carry the same *Its story* line word for word (lines 562, 593).
- `docs/conventions/project-recording/README.md` line 86: "(§3.3, *Where ADRs live*'s index is the CBC Run's)" uses a Fact Reference as a possessive noun; a form oddity rather than a rule break.
- `.claude/rules/convention-manual.md` line 36 carries "Never intent dressed as evidence" (follows FINDING-295 if the manual changes); `CLAUDE.md` line 28, `delivery/container/.claude/CLAUDE.md` line 51 and `TODO.md` line 495 carry "front door" (follow FINDING-314).
- `docs/conventions/project-recording/README.md` §6 has no first line under its heading, where §2, §3, §4, §5, §7, §8, §9 and §10 each have one; consistency, not a rule.
- `docs/conventions/agent-arrangement/README.md` line 565 calls `delivery/container/.claude/CLAUDE.md` a Record Stub ("The Record Stubs: …"); line 29 says it is "not a Record Stub". Two lines disagree.
- `docs/conventions/agent-arrangement/README.md` line 72 quotes `CLAUDE.md` as "no code, no runs"; `CLAUDE.md` line 7 now reads "no code, no CBC Runs" (FINDING-344).
- `docs/conventions/agent-arrangement/README.md` lines 141–142, "promotion queue": nowhere else in living text; lines 83 and 86, "registry": not in the shipped Decisions Log stub (FINDING-364). Possibly stale.
- `docs/conventions/agent-arrangement/README.md` line 398: "PLAN.md" unmarked beside "`docs/adr/`" in code font.
- `docs/conventions/agent-arrangement/README.md` lines 353–354: two blank lines before §3.8; lines 276 and 367: the *Its story* line runs on from the paragraph without a blank line, unlike every other section.
- `docs/conventions/commit-plan/README.md` §2.7 (lines 109–112), §2.9 (125–126), §2.12 (155–156): the italic line tells the case instead of pointing at its story (`.claude/rules/convention-manual.md`, item 6).
- `docs/conventions/commit-plan/README.md` line 146: a Fact Reference to §2.13, which itself only points at `docs/conventions/commit-messages/` §2.4; a pointer to a pointer.
- `docs/conventions/exchange/README.md` line 189 "the two entry files" vs line 128 "the entry file once" (FINDING-413).
- `docs/conventions/exchange/README.md` lines 133–136: a section's last sentence stands after its *Its story* line; lines 201 and 317: *Its story* mid-paragraph and before the rule it belongs to.
- `docs/conventions/exchange/README.md` line 177 "the bundle": a third word for the staged delivery (FINDING-404).
- `docs/conventions/facts-in-sync/README.md` lines 287–289: "It has happened: CBC Run 3 argued down a clause…" tells a case in the body; line 294 already points at ADR-0034.
- `ARCHITECTURE.md` §1.1, §1.2, §1.3, §2.1–2.4 titles carry a gloss after a dash, outside this list's files (from FINDING-341).
- `docs/conventions/retrospective/README.md` lines 73-74 and `TODO.md` lines 561-567: the Concept Deliverer's seat says the trial runs at the close of the Plan Step that runs the next Run Birth; TODO's open item names CBC Run 5's birth as the trigger; the devlog records CBC Run 5's birth step closed on 2026-10-22 (`devlog/2026-10.md` line 1722) and CBC Run 6 born on 2026-10-29 (line 610). The manual's line is behind events, or the trial was skipped.
- `docs/conventions/retrospective/README.md` line 67: "CBC Run 4's Run Reading" as the trigger for reopening the no-guide choice; the devlog has no reading of CBC Run 4, and CBC Run 5 went through Release and was read on 2026-10-22 (`devlog/2026-10.md` line 1722). Possibly a stale name.
- `docs/conventions/retrospective/README.md` §3 line 129 vs `delivery/container/.claude/skills/apply-retrospective/SKILL.md` lines 65-73: the skill orders commits by five rules; the manual retells three. "Regroup before rewriting", "fix tags before the words around them" and "move a fact to its home before its copy goes" stand only in the skill, a derived file carrying facts its manual lacks.
- `docs/conventions/retrospective/README.md` line 147, "The records table names its moment.": relies on `docs/conventions/project-recording/` §13, *The records table*, with no Fact Reference (one-home rule 2).
- `docs/conventions/shapes/README.md` §4.1 lines 176-179: an italic paragraph tells the case (ADR-0037's third act; CBC Run 3's two looks in `temp/`) in the body rather than pointing at its story (`.claude/rules/convention-manual.md` rule 6: one italic line points).
- `docs/conventions/visual-comparison/README.md` line 71: the *Its story* line shares its line with §2.2's prose; line 58: §2's story line stands under the section heading with no body before §2.1.
- `docs/glossary.md` line 6, "One entry per Name", vs the grouped entries at lines 23, 44, 77, 80 and 207 (two or three Names each).
- `docs/glossary.md` line 73, Run Birth "a CBC Run's first state", vs line 35, the agent "finishes the Run Birth", a procedure. The two entries disagree on what a Run Birth is.
- The three templates' marker lines differ in form: `editorconfig.part` lines 2-3 ("# ----…" on its own line, then "# --- java-spring overlay ---") vs `gitattributes.part` and `gitignore.part` line 2 ("# --- java-spring (Maven) overlay ------…").
- `docs/conventions/writing/README.md` §2 rule 4 (lines 77-79) explains worked examples against definitions; the Agent Rule's rule 4 is numbers against vague words. Not a contradiction, but the why does not say why numbers.
- `concept/00-cbc.md` 92-107: "five practices" (104) counts the list at 92-98 (bounded contexts, SLOs, threat modeling, design-before-code culture, the academic lineage), but 100-103 account for four (threat modeling, bounded contexts, SLOs, formal methods): design-before-code is missing, and "formal methods" stands where "the academic correctness-by-construction lineage" stood.
- `docs/models/agent.md` 5-6 and 265-266 say every claim carries a refutation condition; 4 of the 12 carry none: A1 (279-295), M1 (387-392), M2 (394-398), G1 (402-410).
- "Tests sample; structure forbids." is stated in three chapters: `concept/00-cbc.md` 133, `concept/02-guarantees-and-walls.md` 85-86, `concept/04-cbc-slice.md` 51 — one stance, three homes inside the concept; one-home's question, not Writing's.
- `docs/models/tiers.md` §3.5 facts 1 and 5 (116-117, 126-127) retell §3.4 (105) and §3.3 (96-97), each pair cross-referenced both ways; a reader meets each fact twice in one file.
- `TODO.md` 528-560, "Rewrite the method's texts plain": its trigger says this round's Writing reading of the chapters leaves the item; its ideas (543 the costume, 540-541 the kills, 542 "shape") overlap FINDING-538 and should be re-read when these findings close.
- `ARCHITECTURE.md` line 179: CBC Run 6's state "born 2026-10-29 at `657d372`, on full auto" is behind `TODO.md` lines 38-40, which say it ran through Release (Step 14), closed a Step 15, 254 commits, tag `v0.1.0`.
- `TODO.md` line 182: `auto-run` "drafted and used once, for CBC Run 5"; `PLAN.md` lines 148-149 record its second use, CBC Run 6's birth.
- `TODO.md` lines 567 and 785-786: triggers "the close of the Plan Step that runs CBC Run 5's birth" and "after the Plan Step that runs run 5's birth closes" have fired (CBC Run 5 was born 2026-10-22; PLAN holds CBC Run 6's birth now); the items sit unmarked.
- `TODO.md` line 621 "CBC Run 5's first slice closing" and line 632 "the next birth's Step 3 close": fired (CBC Run 5 through Release; two births since 2026-09-04). Line 1049 "CBC Run 5 meeting an absence guarantee": CBC Run 5 is through Release, so its Run Reading can answer it.
- `TODO.md` line 618 "(the item on `.claude/shapes/`)": no item's first words match; the nearest is the item at line 570, whose Context names `.claude/shapes/` at line 579. The item at line 305 records this kind of slip.
- `PLAN.md` line 235: an item starts lowercase, "- [x] the Exchange Convention says", left by the Names pass's replacement of "The exchange".
- `PLAN.md` lines 361-376: the Refine Plan Step's close has 7 items; the Form (lines 87-104) and the two other Plan Steps have 8. The Approach on Trial dated-note item is missing, though this Plan Step uses three Approaches on Trial.
- `PLAN.md` lines 73-75: the Form's example cites `exchange-birth`, a skill `TODO.md` line 62 says is not yet written, and a CBC Run 5 birth item.
- `TODO.md` lines 572-580: a Context of 9 lines; the header says eight at most.
- `TODO.md` line 761: "an Output Shape for a Skill Templates".
- `ARCHITECTURE.md` line 77: a bullet's continuation line is unindented. Lines 204 and 208: two Stated-in cells wrap the Fact Reference in parentheses where the other rows do not.
- `README.md` lines 26-34: Success criteria 1 to 3 appear met (the walls chapter harvested from CBC Run 3 with `cbc-slice` and `cbc-framing` restated, per `CHANGELOG.md` [Unreleased]; CBC Runs 5 and 6 born from this repo alone) and the section does not say so. Content, not writing.
- `docs/adr/README.md` lines 31-32 and `devlog/README.md` lines 10-11: ragged wraps ("Never edit an / accepted", "fragments / fine"). No rule; noting only.
- `.editorconfig` writes " - " where `.gitattributes` and `.gitignore` write " — " for the same dash.
- `.claude/approaches-on-trial/auto-run.md` (lines 35, 86) and `approach-evaluation.md` (lines 109, 132) each write an Approach Stage in both cases; not my files, behind FINDING-571.
- `.claude/rules/working-a-reading.md` lines 125–126: the *Decisions* line says "checked against its source" where step 4 (line 49) says "its foundation" and the glossary (*Foundation Line*) retires "source".
- `.claude/skills/exchange-read/SKILL.md` line 44: "receipt branch" has no living home; only ADR-0016, 0018 and 0019 (closed) define it. One-home: a fact stated only in history gets a living home before anything retells it.
- `.claude/approaches-on-trial/refinement.md` line 67: a Fact Reference whose title is not in italics, "(`docs/conventions/facts-in-sync/` §1, One home)", unlike every other in the file.
- Header-comment Fact References with a section and no title: `convention-manual.md` line 9, `exchange-reading.md` line 9, `foundation-check.md` line 11, all "docs/conventions/agent-arrangement/ §5.6". `CLAUDE.md`'s comment mixes backticked paths (35, 37) and bare (17).
- `.claude/skills/visual-comparison/SKILL.md` line 118, both copies: the bullet's continuation line starts at column 0, "(§1, *When this fires*) covers this, and was read as", breaking the bullet's indent.
- `.claude/approaches-on-trial/auto-run.md` lines 116–118: "Not known still…" follows the last bullet with no blank line, so it renders inside that bullet.
- `delivery/container/.claude/approaches-on-trial/approach-drafting.md` line 104 "taken here" disagrees with `approach-evaluation.md` lines 80–81, "Not "here", which means the reader's own Convention Seat" (FINDING-648).
- `.claude/approaches-on-trial/refinement.md` lines 182–186, 188–191, 218–220, 273–278, 297–299: lessons' stories told in place, up to three sentences each, where `docs/conventions/conventions/` §2.6, *A lesson taken*, has a manual point at its story in one italic line; whether an Approach on Trial follows the manual's form is the close's question.
- `ARCHITECTURE.md` line 85, heading "1.2 The conventions — `docs/conventions/`": a gloss after a dash (rule 10, Refinement Layer 4); `one-home.md` line 30 points at it (FINDING-617).
- "The front door" has one home, `docs/conventions/project-recording/` §1 (lines 181, 201) and §7 (492, 499); `CLAUDE.md` line 28 and `delivery/container/.claude/CLAUDE.md` line 51 retell it (FINDING-606).
- `delivery/container/docs/glossary.md` lacks Run Reading and Approach Stage, which two shipped texts in this Refinement Layer use (FINDING-644, FINDING-646).
- `.claude/rules/writing.md` lines 70–72: the rule's *Before* example is `working-a-reading.md` step 1 as it still stands (FINDING-619).
- `delivery/container/.claude/skills/apply-retrospective/SKILL.md` lines 83-84, "**Links point at labels,** never section numbers: "SLICE-4 GUARANTEE-2", not "§8"", disagrees with the container's `one-home.md` rule 2 (line 20-21: "its path, section and title in parentheses") and with this skill's own Fact References (lines 120, 133).
- `delivery/container/.claude/skills/retrospective/SKILL.md` lines 113-114, "The Decisions Log gets a "rules in force now" list on top", disagrees with `delivery/container/.claude/decisions.md` lines 3-4, "Append-only, newest last."
- `delivery/container/.claude/skills/retrospective/SKILL.md` lines 116-117, "The Concept Deliverer writes each into the next CBC Run's PLAN at that Plan Step", disagrees with the playbook's lines 82-83, "Questions for one CBC Run alone come in its Run Hand-off, never here", and with the Pure Seed's lines 3-4 and 18-19 (delivers everything, decides nothing; nothing that encodes a prior CBC Run's conclusions).
- `delivery/container/PLAN.md` lines 29-35: the placeholder Plan Steps have no "Now:" line; the Plan Step Form (playbook line 30) has one. A CBC Run "born without one" (line 7) fills a form that differs from the Plan Step Form.
- `delivery/container/.claude/CLAUDE.md` lines 56-57, "every line below passes three tests": the comment sits after the table, so "below" covers only *Local rules*; `retrospective/SKILL.md` lines 109-110 reads the whole file against the tests ("The entry file is read top to bottom").
- `delivery/container/.claude/decisions.md` lines 21-22, "The Delivery Pin is the Concept Deliverer's commit every copy here equals.", retells the glossary's definition (`delivery/container/docs/glossary.md` lines 26-27) and `delivered-copies.md` rule 1 (line 21) with no reference: a second home.
- `delivery/container/docs/glossary.md` lacks "Run Reading", used by `shapes-lifecycle.md` line 93 and `visual-comparison/SKILL.md` line 98 (FINDING-723). "Approach Stage" is used by `approach-drafting.md` line 41 and is also not listed.
- `delivery/container/.claude/rules/delivered-copies.md` lines 29-30, "the entry file was composed once": two entry files are composed (`delivery/README.md` line 26; the Pure Seed lines 21-22).
- `delivery/container/.claude/rules/shapes-lifecycle.md` line 72, "Either of the last three": "either" for three.
- `delivery/container/.claude/decisions.md` lines 35-37 list 11 conventions; `docs/conventions/` holds 12. The `conventions` manual is the one left out, likely on purpose (a CBC Run holds no Convention Manual); worth one word saying so if the list is read as complete.
- `delivery/container/devlog/devlog.md` line 16, "(Step 0: bootstrap)", against the playbook's "Step 0: Bootstrap" (line 138): a label's case differs.
- Saturation's exit is stated in three units: "two consecutive fresh probes finding nothing new" (`cbc-framing/SKILL.md` 81-82), "two consecutive lenses yield zero new facts" (workflow 223-224), "two fresh attacks on the list find nothing new" (`the-whole-system-in-plain.md` 54-55); the worked example ran three probes of one lens each and called two dry probes saturation (77-81). With three lenses in all (workflow 196-210), "two consecutive lenses" and "two probes" are not the same rule.
- `docs/glossary.md` 127 "the Slice-Record Shape" against "Slice Record Shape" at `slice-record.md` 5 and `cbc-slice-workflow.md` 36, 194 (FINDING-822).
- The evidence label's form differs: `evidence-test.md` 46 "SLICE-1 EVIDENCE-2 · GUARANTEE-3 — KILL-3" (a dash before the kill) against `cbc-slice/SKILL.md` 88-89 and 162-163 "SLICE-4 EVIDENCE-3 · GUARANTEE-2 · KILL-12" (a middle dot).
- "evidence-closed" (`cbc-slice/SKILL.md` 189; worked example 259; template 73) against the status value "closed (date, evidence)" (`cbc-framing/SKILL.md` 182; template 18; `registry-entry.md` 72) (FINDING-816).
- Two homes with no Fact Reference between them: the mode's rule "Every "outside" is written ... Silence is the only forbidden channel" at `cbc-framing/SKILL.md` 33-35 and workflow 64-66; "Every field is present; an empty one says "none"" at template 52-53 and `registry-entry.md` 54-56; the status values at `cbc-framing/SKILL.md` 182 and template 17-18; the "Flag riding" slot's guidance said two ways at `registry-entry.md` 42-43 and template 36-40.
- `cbc-framing/SKILL.md` 191 and template 6-7 quote `delivered-copies.md` rule 8's lead short: the lead is "A Skill Template is copied and filled, never edited in place." (FINDING-764).
- `cbc-framing/SKILL.md` 143 "framing verdicts — inline here": "here" means the derivation doc, but the sentence stands in `SKILL.md`.
- `kill.md` 77 "facts FACT-CALLER-1 to FACT-STORE-6" gives a range over tags of four different actors; the six facts are not one sequence by name.
- `cbc-framing/SKILL.md` 107-111 says the CBC Run adds a Glossary Name for each thing framing defines "when framing first uses it"; the CBC Run's glossary header says the first group holds "the Names the delivered skills, rules and shapes are written in", and lists none of the method's terms. The two texts leave the method's words with no home for their Names (FINDING-739).
- `spring-boot-walkthrough.md` 199: "while two real instances still oversell" — a lived CBC Run's problem (overselling) stated as if general; the reader's problem may not be a count.
- `spring-boot-walkthrough.md` 233–235 (*The exit*) and `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 193–195: the same list of exit records in two homes; `spring-boot-walkthrough.md` 146–148 and `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` 165–166: the test-includes rule in two homes.
- `establishment-walk.md` §2 (72–77) and `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` Stage 2 gate (72–77): the same text near verbatim; the contract's section list in three places (`delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` 87–89, 141–146; `establishment-walk.md` 129–134) is Round 2's FINDING-227, left to the TODO item.
- The default-privileges sentence in three homes: `postgres-role-split.md` 79–82, `postgres-setup-walkthrough.md` 64–67, `bootstrap.sql` 59–61.
- `establishment-walk.md` 84: "they are no properties of persisted state" — grammar; "are not properties".
- `spring-pom-convention.md` 51–54: under *What the file does not carry*, two bullets say what the file does carry (`<description>` filled; versions the parent's).
- `bootstrap.sql` 33–39: the template defaults to the prefixed, shared-cluster names while calling the dedicated cluster "the lived normal", whose names are bare; `spring-harness-reference.md`, `.env.example`, `flyway.conf` and `verify-database-model.sql` all carry the prefixed form.
- `testcontainers.properties` 1–8: its header cites CBC ADR-0008 for "the machine's own" where the other seven template headers cite delivered-copies rule 8; a different form for a different destination, said nowhere.

### The read's counts

644 findings, FINDING-282 to 925: the nine readers' 641, three of
them merged into another reader's, and 6 of the agent's from the
items checked first.

- by rule: rule 1: 21; rule 2: 162; rule 3: 67; rule 4: 13; rule 5:
  109; rule 6: 52; rule 7: 29; rule 8: 58; rule 9: 113; rule 10: 16;
  rule 11: 1; of other kinds 3, 2 Agreement and 1 Stale lines;
- by Refinement Layer: 1: 23; 2: 36; 3: 205; 4: 58; 5: 69; 6: 253,
  the Method Group's 92 and the Stack Group's 94 among them;
- by how they stand: 301 checked, 224 resting on the reader, 119
  uncertain;
- known before the readers read, 13: the five of *Met in round 2* still
  true, FINDING-672, 786, 923, 924 and 925; the word, 671; the pass's
  title, 922; the script's six, 299, 586, 607, 657, 690 and 708;
- the Names pass, read against: three Names put where English was
  meant, FINDING-546, 578 and 579; the lowercase Names it missed,
  about 60 in the approaches' dated notes (DECISION-18), 7 elsewhere;
- proposed: each finding carries its reader's proposal, fix, decline
  or a question; the sixteen decisions bind about 330 of them.

Sixteen decisions, DECISION-16 to DECISION-31.

88 things met in passing, of other kinds, listed for the work where
it touches the same file, and for the last read.

### Endings (§2.6)

The reviewer took the endings, 2026-10-31, as the seventeen decisions
leave them, one side of each "or" chosen: where a proposal held an
"or", the fix was taken, as in round 2. Where a finding asked a
question no decision answers, the agent made the call below, and the
reviewer took it. The work names each fixed finding's commit.

- **Fixed, 595,** each in its Refinement Layer: FINDING-282 to 289, 291 to 301, 303 to 334, 336 to 338, 340 to 378, 381 to 404, 406 to 441, 443 to 471, 473, 475 to 479, 481 to 493, 495 to 506, 508, 510 to 530, 532 to 536, 538 to 542, 544 to 567, 569 to 595, 598 to 624, 626 to 654, 656 to 662, 664 to 665, 667 to 717, 719 to 721, 723 to 729, 731 to 738, 740, 742 to 743, 745 to 746, 748 to 774, 776 to 789, 791 to 798, 800 to 807, 809 to 812, 814, 816 to 818, 820 to 822, 824 to 825, 828 to 831, 833 to 841, 843 to 862, 864 to 895, 897 to 909, 911 to 913, 915 to 918, 920 to 923, 925.
- **Fixed by the design of DECISION-19, 29 and 32, 21,** worked once
  it has landed: FINDING-509, 655, 718, 730, 739, 741, 744, 747, 775, 790, 799, 808, 813, 815, 819, 823, 832, 842, 896, 919, 924.
- **Fixed in part, 5:**
  - FINDING-339: Entry File and `ARCHITECTURE.md` fixed; "the records table" stays English, DECISION-23.
  - FINDING-405: the bold stays at the Name's home and goes elsewhere, DECISION-22.
  - FINDING-494: the bold stays at the Name's home and goes elsewhere, DECISION-22.
  - FINDING-531: the title fixed; the four labels stay and get Names by DECISION-19.
  - FINDING-910: "door" stays where it is the boundary; its four other senses fixed, DECISION-26.
- **Declined, 23:**
  - FINDING-290: "consumer" is any project holding a copy, this repo included: English.
  - FINDING-302: a record's short name, PLAN, TODO, ARCHITECTURE, is its label, as a convention's is by DECISION-24.
  - FINDING-335, 442, 480, 914: a dead figure, DECISION-26.
  - FINDING-379 to 380, 472, 507, 666, 826 to 827: outside rule 10 as written, DECISION-20.
  - FINDING-474, 722: the bold is at the Name's home, DECISION-22.
  - FINDING-537, 543: DECISION-17.
  - FINDING-568, 596 to 597: history, DECISION-18.
  - FINDING-625: English, DECISION-23.
  - FINDING-663: no count of 2026-10-17 exists to give.
  - FINDING-863: a summary that says it is one, as one-home rule 3 allows.
- **Moved to TODO:** none. Round 2's findings that DECISION-7 and 8
  moved to the plain-rewrite item, FINDING-206's citations of CBC Run
  3's RETRO, 223, 224, 227 and 228, are worked in this round's layer 6,
  by DECISION-16: the item keeps only what the round leaves.

The agent's calls, where a finding asked a question no decision
answers:
- FINDING-385, fixed: each part leads with its rule, then its why.
- FINDING-404, fixed: Delivery Staging names the delivery as it arrives, as the CBC Run's glossary and exchange §4 use it; the act is "stage a delivery"; our glossary's entry, which says the act, changes.
- FINDING-413, fixed: the two composed entry files named.
- FINDING-419, fixed: "root" said as the Foundation Line's document.
- FINDING-492, fixed: each Idea Model says what it is first, its status after.
- FINDING-509, by the design: the Agent Model's words, ambient, told and the rest, judged by DECISION-19's test in its design, in our glossary's group for Names ours only.
- FINDING-522, fixed: what meets at a Run Birth said in plain words.
- FINDING-525, fixed: "made usable" the verb, lowercase; Made Usable only as the noun.
- FINDING-561, fixed: as FINDING-525.
- FINDING-623, fixed: as sub-lists, the manual first, by DECISION-30's reason.
- FINDING-672, fixed: the four become Skill Stages, each under its heading, as conventions §1.4 says.
- FINDING-738, fixed: said in plain words, or the example dropped.
- FINDING-746, fixed: "stage" there is the Skill Stage, by DECISION-25.
- FINDING-764, fixed: the lead quoted whole, by DECISION-31's reason.
- FINDING-778, fixed: the six as a list.
- FINDING-801, fixed: one short sentence, keeping its label.
- FINDING-822, fixed: the Slice Record Shape, as the Names pass titled it; the glossary's hyphen goes.
- FINDING-916, fixed: in the rewrite, by DECISION-16.

DECISION-23's Rests named FINDING-367 for "registry": that is 364,
and 367 the entry file's; corrected there.

None of the declines is taste alone: each line meets the rule as
written, keeps a decision's word, or is history.

### The work (§2.7)

Each Refinement Layer's fixed findings, with the commits that fixed
them.

- **Layer 1, the conventions manual:** FINDING-282 to 287, 292 to 301,
  303 and 304 in `ab4c2e6`, its old words given their Names there;
  294 and 295 carried to `.claude/rules/convention-manual.md` in
  `839f785`. Already fixed by the design: 288 in `e0714e0`, 289 and
  291 in `39e35b3`, 291's other half already DECISION-24's kind word,
  "the facts-in-sync manual".
- **Layer 2, the project-recording manual:** FINDING-305 to 334 and
  336 to 340 in `eb57bcf`, its old words given their Names there, 339
  in part as its ending says; what retells a replaced phrase carried
  in `f222539` (our records), `454028f` (`CLAUDE.md`) and `2c00ebf`
  (the Record Stubs and the container's Entry File). 335 declined.
- **Layer 3, the other manuals, the models, the concept, the
  glossary:** each file's findings in its commit, its old words given
  their Names there; what follows a file in the commit after it.
  - the Agent Model, FINDING-492 to 506, 508 and 509, `4ee4062`; 507
    declined;
  - the Idea-to-Output Model, 510 to 517, with 492 to 494 there,
    `11389e9`; its two agent-side references, `acbb438`;
  - the Tiers Model, 518 to 529, with 492 to 494 there, `2ccc26a`;
  - the concept's chapters, 530 to 536, 538 to 542, 544 and 545,
    `1f0c17e`; what the method's files retell, `f074544`; 537 and 543
    declined;
  - the writing manual, 483 to 485, `99dbc35`;
  - facts-in-sync, 414 to 434, `5747b32`;
  - agent-arrangement, 343 to 368, `f07d52a`; its Entry File
    references, `c4748c1` and `5a397a7`;
  - commit-messages, 369 to 378, `51a5469`; 379 and 380 declined;
  - commit-plan, 381 to 388, `341107f`;
  - the exchange, 389 to 413, `a60a357`;
  - repo-hygiene and its templates, 435 to 441 and 443, `6d67082`;
    442 declined;
  - retrospective, 444 to 449 and 451 to 456, `7b81e55`; 450 not
    worked, its count needing CBC Run 3's apply guide;
  - shapes, 457 to 471 and 473, `9fb20fd`; 472 and 474 declined;
  - visual-comparison, 475 to 479, 481 and 482, `7a54776`; 480
    declined;
  - the index and the glossary, 341, 342 and 486 to 491, `a575fb5`.
- **Layer 4, `ARCHITECTURE.md`, `README.md` and the records:** each
  record's findings in its commit, the old words of its living text
  given their Names there; history kept its words.
  - `ARCHITECTURE.md`, 546 to 556, `c0eb1e6`; its references in our
    one-home Agent Rule, `ddc07db`, and under `delivery/`, `252293f`;
  - `README.md`, 557 to 563, `943dafe`; 564 fixed in layer 2,
    `f222539`;
  - `PLAN.md`, 570 to 577, `520ab30`;
  - `TODO.md`, 578 to 585, 587 to 590 and 592 to 594, `e5a874b`; 586
    already fixed; 591 not worked, its count needing a reading of
    the 97 uses;
  - `CHANGELOG.md`, 565 to 567 and 569, `5e703d3`, with 566's four
    TODO lines; 568 declined;
  - `devlog/README.md`, `temp/README.md` and `docs/adr/README.md`,
    598 to 603, `c57a713`; 596 and 597 declined.
- **Layer 5, our agent setup:** each kind of agent file's findings in
  its commit, its old words given their Names there; the dated *Uses*
  notes are living, by DECISION-18.
  - `CLAUDE.md` and `CLAUDE.local.md`, 604, 605 and 607, `1275d0f`;
    606 fixed in layer 2, `454028f`;
  - the Agent Rules, 611, 614 to 616 and 618 to 622, `2158499`; 612
    and 613 fixed in layer 1, `839f785`; 617 in layer 4, `ddc07db`;
    623 in the writing manual first, `66abe45`, then ours,
    `e65bd34`; 662's two footers in `1246c85`;
  - the Agent Skills, 624, 626 to 629, 631 to 643, 671 and 672,
    `31156de`; the reference to `exchange-read`'s Stage 3, `683febc`;
  - the Approaches on Trial, 647, 649 to 662, 664, 665 and 667 to 670,
    `1246c85`; the glossary's references to the new §1.1, `80772da`;
    663 and 666 declined;
  - the Decisions Log's header, 608 to 610, `e834a11`.
  630, 644 to 646 and 648 name only the container's copies and are
  layer 6's.
- **Layer 6, `delivery/`, what ships:** each Agent Skill's or file
  family's findings in its commit, its old words given the Names of
  the four Names tables; what follows it in the commit after.
  - the exchange manual and `exchange-deliver`, naming the two
    composed files right, `e2142b3` and `0776127`;
  - the delivery's pages, 673 to 694, `5d562d8`; the
    project-recording manual and `TODO.md` follow the CBC Framing
    Plan Step's title, `6927e66`;
  - the container's records, 695, 697, 698 and 700 to 709,
    `b451eb9`; 696 and 699 fixed in layer 2, `2c00ebf`; our own
    copies and the project-recording manual follow, `cffd879`;
  - the container's agent files, 630, 644 to 646, 648, 710 to 721
    and 723 to 735, `ddd6057`; our approach-drafting and
    visual-comparison follow, `db36e62`, and the agent-arrangement
    manual's seats, `445db69`; 722 declined;
  - the four Output Shapes, 736 to 747, `8a4525b`;
  - cbc-framing's Agent Skill, 748 to 775, `4884a12`;
  - cbc-framing's workflow, 776 to 799, `3be745a`;
  - cbc-framing's references, 800 to 810, `8316ce0`;
  - cbc-slice, 811 to 825, `06a3915`; 826 and 827 declined;
  - cbc-bootstrap's Agent Skill and `app-structure.md`, 828 to 850,
    `c449de0`;
  - cbc-bootstrap's references and templates, 851 to 862 and 864 to
    878, `a6ccf5b`; 863 declined;
  - infra-establish, 879 to 907, `580f7dc`;
  - infra-serve and the items checked across both groups, 908 to
    913, 915 to 923 and 925, `78fe685`; our `.gitignore` follows,
    `4185a49`; 914 declined; 924 fixed by DECISION-29's design,
    `ac34e28`.

## Round 3's close read

All 118 living files read again at `f5dfbbe`, 2026-11-01, against
writing rules 1 to 10 (§2.8), by nine readers as in round 3's read,
A to I, one Refinement Layer or part of one each, each file whole.
The 118 are round 3's 115, with the three delivered Names files
ADR-0078 added. A script swept all 118 first, for the same three
things as before the read: 6 numbered titles past 30 characters or
with a gloss, 47 lowercase spellings of a Name outside history and
outside "made usable", and every Fact Reference's title against its
heading, all of which held. Each reader judged the sweep's lines for
its files.

The agent then checked each finding's first quote against the tree
by script: 350 of 485 matched at the line named, 12 a few lines
away; the 123 the script could not parse were sampled by hand, 7 of
them, and all held. Each finding's mark, changed or not changed in
round 3, is taken from `git blame` on its first line named, against
`00420b9`, where round 3's read was taken.

Found true, so not listed:
- the worked example's two copies are byte-identical;
- `approach-drafting.md` is one text in both Convention Seats;
- every numbered Fact Reference's title lands on its heading.

### Findings

FINDING-926 to 1410. Each keeps its reader's number beside it, and
its reader's proposal; nothing is decided yet.

#### Reader A, Layers 1 and 2: the conventions manual, project-recording

##### `docs/conventions/conventions/README.md`

**FINDING-926.** (A-1) [changed in round 3] rule 9; checked. `docs/conventions/conventions/README.md` *§1, A convention's Work Approaches* (line 49): "is the Idea Model's". The glossary names a particular Idea Model by its name: "the Agent Model, the Tiers Model, the Idea-to-Output Model". "The Idea Model" leaves the reader to work out which one is meant, though the path follows. The sentence can also be read as "a convention is its manual and its Work Approaches", which is DECISION-32's rejected option (b). Proposed: fix: "What a convention is, its manual, with its Work Approaches one level down, is the Idea-to-Output Model's (`docs/models/idea-to-output.md` §6, *A convention*)." Changed.

**FINDING-927.** (A-2) [not changed in round 3] rule 9; checked. *§3, Adding a convention*, step 4 (line 301): "The index's chain, only if the convention acts in sequence". DECISION-23 said "the chain" is to be said as the order the conventions act in, since it clashes with Chain Link. This file's own *What this is made usable as* (line 33) already says it that way. Proposed: fix: "4. Its place in the index's order of the conventions, only if the convention acts in sequence during a piece of work." Unchanged.

**FINDING-928.** (A-3) [changed in round 3] rule 9; checked. *What this does not cover* (lines 336–337): "which paths are the arrangement's". "The arrangement" names the agent-arrangement convention by a short word. DECISION-24 lists "the arrangement" among the forms that change, and DECISION-27 writes a convention with its kind word every time. Proposed: fix: "and which paths the agent-arrangement manual lists". Changed (line 336 rewritten; these words kept).

**FINDING-929.** (A-4) [changed in round 3] rule 3; checked. *§2.2, The need* (lines 208–214): "as evidence. Or as intent marked on trial. … Or as adopted, taken whole from elsewhere". The section names three forms a need can take, joined by "Or as" fragments, so the reader has to count them. The Agent Rule made from this section, `.claude/rules/convention-manual.md` item 2, lists the same three. Proposed: fix: "*What it is for* says the need: the work it makes possible, the failure lived without it, and the trigger. It is stated as one of three:", then a list of three: evidence; intent marked on trial, saying what would make it evidence and when to look again, after which the need is rewritten from what was seen or the convention goes; adopted, saying where it came from and what has been lived under it since. Then: "Never a wish written as evidence." Changed.

**FINDING-930.** (A-5) [changed in round 3] rule 3; checked. *§2.4, The seats* (lines 233–239): "One paragraph when they are alike, a section per Convention Seat when they are not, and "no Convention Seat" said outright when one side has none". The four forms the section can take are packed into two sentences. `.claude/rules/convention-manual.md` item 4 lists them as "One of four:". Proposed: fix: "It takes one of four forms:", then four items: one paragraph when they are alike; a section per Convention Seat when not; "no Convention Seat" said outright when one side has none, so a reader does not hunt for it; a paragraph naming which body sections are whose when the body is already written per Convention Seat, as `docs/conventions/exchange/` does. Changed.

**FINDING-931.** (A-6) [not changed in round 3] rule 2; checked. *§2.7, The channel* (lines 274–275): "Where it reasons from the Agent Model, a Fact Reference to that part (`docs/models/agent.md`)." This sentence has no verb. The parenthesis is also not a Fact Reference, since a Fact Reference gives a section and a title. Proposed: fix: "Where it reasons from the Agent Model, it carries a Fact Reference to the part it rests on, such as (`docs/models/agent.md` §8, *Choosing a channel*)." Changed.

**FINDING-932.** (A-7) [changed in round 3] rule 8; resting on the reader. *What this is made usable as* (lines 28–29): "— a CBC Run's, and this convention's Work Approach there". It is hard to tell what "a CBC Run's" belongs to, or what "there" points at. The next entry (line 32) says only "it points.", and does not say what it points at. Proposed: fix: "— held in a CBC Run, where it is this convention's one Work Approach (§1.3, *The Foundation Line*);" and "it points at each manual." Changed.

**FINDING-933.** (A-8) [not changed in round 3] rule 8; resting on the reader. *§1.3, The Foundation Line* (line 132): "The value carries the relation where it is not derivation." The reader has to work out from the list above that this means the "checked against" and "under" values. Proposed: fix: "Where a file is not derived from what it names, the value says how the two relate: `checked against`, `under`." Unchanged.

**FINDING-934.** (A-9) [not changed in round 3] rule 8; resting on the reader. *§1.3, The Foundation Line* (line 121): "for the stack practice, the concept it was checked against". "The stack practice" is met here with no plain words. The reader has to know it means the Stack Group's files. Proposed: fix: "for the Stack Group's Agent Skills, the stack practice, the concept they were checked against". Question: is "the stack practice" exactly the Stack Group's Agent Skills, or more? Unchanged.

**FINDING-935.** (A-10) [changed in round 3] rule 8; resting on the reader. *§2, The Convention Manual* (lines 191–193): "A section two manuals need becomes the next candidate. A pair recurred is the test an Output Shape is written by". The sentence does not say what the section is a candidate for, and "a pair recurred" has to be decoded. Proposed: fix: "A section that two manuals need becomes a candidate for the list. It is the same test by which an Output Shape is written: a pair of outputs that recur (`docs/conventions/shapes/` §1.2, *How an Output Shape is born*)." Changed.

**FINDING-936.** (A-11) [not changed in round 3] rule 2; resting on the reader. *§2, The Convention Manual* (lines 181–183): "in the order of the parts below, from (§2.1, *The opening statement*) to (§2.9, *Where to look*)". The sentence uses two Fact References as nouns inside it, after two other qualifiers. Proposed: fix: "**The form** is the sections a manual has, each a heading after the opening. They come in the order of §2.1 to §2.9 below." Unchanged.

**FINDING-937.** (A-12) [changed in round 3] rule 2; resting on the reader. *§3, Adding a convention*, step 6 (lines 309–310): "No line in a birth entry's list of conventions, as a CBC Run's Decisions Log holds: the Concept Deliverer receives none (ADR-0042)." The sentence has no verb, and "receives none" leaves the reader to supply "none of what". Proposed: fix: "A CBC Run's Decisions Log lists, in its birth entry, the conventions it received. The Concept Deliverer receives none, so it writes no such line (ADR-0042)." Changed.

**FINDING-938.** (A-13) [changed in round 3] rule 8; resting on the reader. *§1.1, How a rule is written* (line 74): "A decision is cited as one rule says for every text". "One rule" does not say which rule. The reader learns it only from the Fact Reference two lines down. Proposed: fix: "A decision is cited as the facts-in-sync manual says for every text, in both Convention Seats: …". Changed.

**FINDING-939.** (A-14) [not changed in round 3] rule 8; resting on the reader. *§1, A convention's Work Approaches* (lines 67–68): "The reader is an agent in a project, holding a pinned copy". The sentence does not say whose reader. Line 64 says this repo's own Agent Skills and Agent Rules are not copies, so their reader holds no pinned copy. Proposed: fix: "A Work Approach's reader is an agent in a project, opening it at the moment of use. In a CBC Run, that agent holds a pinned copy." Unchanged.

**FINDING-940.** (A-15) [not changed in round 3] rule 2; resting on the reader. *§1.3, The Foundation Line* (lines 110–112): "as a Foundation Line, `foundation:`, in that header's comment. Both Convention Seats, the CBC Run's Record Stubs included." One list item stacks three asides, then ends on a fragment. Proposed: fix: "a record whose header holds its form, such as the Plan Step Form or `TODO.md`'s item form: a `foundation:` line in that header's comment, in both Convention Seats, the CBC Run's Record Stubs included." Unchanged.

**FINDING-941.** (A-16) [not changed in round 3] rule 9; uncertain. *§3, Adding a convention*, step 3 (line 299): "the Decisions Log's Record Stub". The glossary's Record Stub entry says each Record Stub is "named by it: the Plan Stub, the Decisions Log Stub". But no living text outside the glossary uses those Names, so the working practice is "Record Stub" plus its record or path. Also `docs/conventions/project-recording/README.md` lines 238 ("the Record Stub's legend"), 651 ("The plan's Record Stub"), 659–660 ("the Record Stub's placeholders", "the CBC Run's PLAN Record Stub"): 4 more where the particular Record Stub is meant and no path is given. Question: does a particular Record Stub take its Name (Plan Stub, Decisions Log Stub), or does the glossary's example go? If it takes its Name: "the Decisions Log Stub", "the Plan Stub's legend", "The Plan Stub", "the Plan Stub's placeholders". Unchanged.

**FINDING-942.** (A-17) [not changed in round 3] rule 9; uncertain. *§2.4, The seats* (line 228): "### 2.4 The seats". This is a numbered title holding the lowercase word for a Convention Seat, and the glossary's Convention Seat entry points at it. The fixed heading "## The seats", which every manual has, is a label of the form. But this section is numbered, so rule 10 reaches it (DECISION-20), and so does rule 9. Also `docs/conventions/project-recording/README.md` lines 56 ("### The CBC Run's seat"), 65 ("### The Concept Deliverer's seat"), 166 ("*The CBC Run's seat:*") and 187 ("*Our seat:*"): 4 more. Question: is "seat" in the fixed heading, and in the per-seat headings built from it, a label or the Name? If it is the Name: "### 2.4 The Convention Seats", with the rename grep; "The CBC Run's Convention Seat" and so on. Unchanged.

**FINDING-943.** (A-18) [change not traced] rule 6; uncertain. *§3, Adding a convention* (line 315) and *What this does not cover* (line 341): "`CHANGELOG.md`'s standing comment". Every other place, these two files included, calls a record's top comment its "header comment" (one-home's *Not a second home*; `docs/conventions/project-recording/README.md` lines 360, 413, 477, 528, 586, 670, 828). Two words for one thing make the reader ask whether they mean two things. Also `docs/conventions/project-recording/README.md` line 875: 1 more. Proposed: fix: "`CHANGELOG.md`'s header comment", in all 3; or decline if "standing" marks something the header comment is not. Unchanged.

**FINDING-944.** (A-19) [not changed in round 3] rule 3; resting on the reader. *§3, Adding a convention* (line 316): "the PLAN has no per-convention Plan Steps. *Its story: devlog 2026-09-28; …*". Here the story line runs on at the end of a prose paragraph. §2.6 asks for "one italic line", and every other story line in the file stands on its own line. Proposed: fix: move the italic to its own line under the paragraph. Unchanged.

##### `docs/conventions/project-recording/README.md`

**FINDING-945.** (A-20) [changed in round 3] rule 9; checked. *§7.5, When a README changes* (lines 543, 545, 548) and *§9.1, What a playbook is* (line 631): "a Plan Step whose gate makes true", "in lived gates", "The Release Plan Step's gate", "the full sequence of Plan Steps, gates, and". Each lowercase "gate" means a Plan Step Gate. DECISION-19's Agent Model group, question 2, gave "gate" two Names and asked that each use be read by hand. "Lived gates" is also opaque (rule 8). 4 instances. Proposed: fix: "a Plan Step whose Plan Step Gate makes true"; "in Plan Step Gates already in use ("ARCHITECTURE current")"; "The Release Plan Step's Plan Step Gate includes"; "the full sequence of Plan Steps, their Plan Step Gates, and". Changed.

**FINDING-946.** (A-21) [not changed in round 3] rule 5; checked. *§5.4, How an item is written* (line 423): "an idea parked here is not lost"; *§12, Minimum viable set* (line 763): "devlog only (even that pays off)". DECISION-26's row "debt, bank, park, pays off" says fix. 2 instances. Proposed: fix: "an idea written here is not lost"; "devlog only (even that is worth it)". Unchanged.

**FINDING-947.** (A-22) [not changed in round 3] rule 5; resting on the reader. These figures are not in DECISION-26's table: "the raw material for the retrospective and the playbook" (line 228); "Polishing it: it kills the habit." (380); "otherwise they rot" (408); "The cross-project script." (626); "Same checklist spirit as playbooks" (718); "when a struggle crystallizes into a decision" (730, in the drawing, which rule 9 reaches by DECISION-21). The same row ruled the matching figure "the raw material that gets distilled upward" (FINDING-321), and it was fixed. 6 instances. Proposed: fix: "what the retrospective and the playbook are written from"; "Polishing it: the habit stops"; "otherwise they are forgotten"; "The Plan Steps every project of a type starts from."; "A checklist, as a playbook is"; "when a struggle ends in a decision". Changed in part (380 was rewritten with the figure kept); the rest unchanged.

**FINDING-948.** (A-23) [changed in round 3] rule 5; uncertain. *The Concept Deliverer's seat* and on (lines 70, 85, 86, 155, 170, 202, 669, 673, 686): "Lessons fold back at each Plan Step's close", "the evidence its playbook is folded from", "**Fold back:**", "Never folding retrospectives back". "Fold" is a figure for writing lessons into a record, and "folded from" a figure for writing from. The method also gives "fold" a meaning of its own, the Invariant Slice Fold. DECISION-19 fixes a word that has a rival among the delivered Names. 9 instances here, and 32 in living text, the retrospective manual's own Concept Deliverer's seat among them. Question: is "fold back" kept as the convention's dead verb, or said plainly ("lessons are written back into the playbook", "the evidence its playbook is written from") across living text? Changed in part (the Concept Deliverer's seat's list was rewritten with these words kept).

**FINDING-949.** (A-24) [changed in round 3] rule 9; checked. *The Concept Deliverer's seat*, item 1 (line 72): "on trial at the close of the birth Plan Step". "Birth" stands for the CBC Run Birth. The Plan Step meant is the one the retrospective manual calls "the Plan Step that runs the next CBC Run Birth" (`docs/conventions/retrospective/`, *The Concept Deliverer's seat*). Proposed: fix: "on trial at the close of the Plan Step that runs the next CBC Run Birth". Changed (the list was rewritten with these words kept).

**FINDING-950.** (A-25) [not changed in round 3] rule 2; checked. *The Concept Deliverer's seat*, item 5 (lines 108–110): "Its words are a record of their own, `docs/glossary.md`, as a CBC Run's are, and a line known wrong is a TODO known issue". This one sentence holds two unrelated facts: where the glossary is, and what happens to a wrong line. Proposed: fix: "Its words are a record of their own, `docs/glossary.md`, as a CBC Run's are. A line known wrong is a known issue in `TODO.md` (§5, *TODO.md*)." Changed.

**FINDING-951.** (A-26) [not changed in round 3] rule 8; resting on the reader. *The Concept Deliverer's seat*, item 5 (lines 97–106): "**what is stated, and what ships from it** — the pairing, the Idea Models". The five parts are given in new words, not by `ARCHITECTURE.md`'s headings (*Overview*, §1 *What is stated here*, §2 *The delivery and the CBC Runs*, §3 *What must stay true*, §4 *Codemap*), so a reader cannot find them by title. "The pairing" is `ARCHITECTURE.md`'s own word, and it is not explained here. Proposed: fix: name each part by its heading, and say "the pairing" plainly: "each Canonical Description beside what is made from it". Changed.

**FINDING-952.** (A-27) [changed in round 3] rule 8; resting on the reader. *The Concept Deliverer's seat*, item 7 (lines 119–120): "A CBC Run gets it only if it holds here." The reader has to work out that "holds" means "passes its trial". Also *The CBC Run's seat* (lines 61–62): "its lessons reach the playbook when the Concept Deliverer reads it": "it" can be the retrospective or the CBC Run. 2 instances. Proposed: fix: "A CBC Run gets it only if its trial here keeps it (§14, *Conversation Memory*)."; "when the Concept Deliverer reads the CBC Run". Changed.

**FINDING-953.** (A-28) [not changed in round 3] rule 8; resting on the reader. *What it is for* (lines 13–14): "Adopted with the Container Group (ADR-0038, 1d for the README's moment)". An adopted need says where it came from (`docs/conventions/conventions/` §2.2, *The need*), and this line does not say. DECISION-23 asks that the handbook be named in plain words once per file. The text "1d for the README's moment" is also hard to decode. Proposed: fix: "Adopted with the Container Group from the handbook, the repo this arrangement came from, now history (ADR-0038; its decision 1d sets when the README changes)." Unchanged.

**FINDING-954.** (A-29) [changed in round 3] rule 2; resting on the reader. *What this is made usable as* (lines 30–34): "— the one part of the Entry File this convention owns (§13, *The records table*), in a file `docs/conventions/agent-arrangement/` owns: the rule that cannot live inside a record, when to open it." One list item holds four ideas: whose part it is, whose file it sits in, what it holds, and why it is not in a record. Proposed: fix: "— the one part of the Entry File this convention owns (§13, *The records table*). The file is the agent-arrangement manual's. The table holds the one rule a record cannot hold: when to open it." Changed.

**FINDING-955.** (A-30) [changed in round 3] rule 2; resting on the reader. *The Concept Deliverer's seat*, item 4 (lines 81–83, 89–90): "What makes work a Plan Step, and the Plan Step Form, the CBC Run's adapted to this Convention Seat, are under"; "(§3.3, *Where ADRs live*'s index is the CBC Run's)". The first sentence has nested asides. The second folds a Fact Reference into a clause. 2 instances. Proposed: fix: "What makes work a Plan Step, and the Plan Step Form, are under `## The Plan Step Form` at the top of the Concept Deliverer's own `PLAN.md` (ADR-0057). The form is the CBC Run's, adapted to this Convention Seat."; "and no decision index, since `docs/adr/` lists itself. The index in §3.3, *Where ADRs live*, is the CBC Run's." Changed.

**FINDING-956.** (A-31) [changed in round 3] rule 2; checked. *§2.1, What a plan is* (lines 218–221): "The plan of Plan Steps: the whole of the work sketched coarsely, the next 1–2 Plan Steps detailed finely, the detail moving forward as Plan Steps close, each with its exit criteria, its Plan Step Gate, and a live status." This is one sentence with no verb and five parts. "Its exit criteria, its Plan Step Gate" also reads as two things, though the Plan Step Gate is the exit criteria (glossary). Proposed: fix: "A plan is its Plan Steps. The whole of the work is sketched coarsely, and the next 1–2 Plan Steps are detailed finely. The detail moves forward as Plan Steps close. Each Plan Step has a Plan Step Gate, its exit criteria, and a live status." Changed.

**FINDING-957.** (A-32) [not changed in round 3] rule 2; resting on the reader. *§2.4* (lines 237–240), *§3.4* (294–297), *§4.4* (360–362): "In a CBC Run, the Record Stub's legend and the Plan Step Form copied from the playbook at birth, …; in the Concept Deliverer's Convention Seat, `PLAN.md`'s legend and its Plan Step Form." The pattern "In a CBC Run, X; in the Concept Deliverer's Convention Seat, Y" has no verb on either side of the semicolon. The reader has to carry "is the form" over from the sentence before. 3 instances. Proposed: fix: "In a CBC Run, the form is X. In the Concept Deliverer's Convention Seat, it is Y." Changed in part (295 rewritten); 237–240 and 360–362 unchanged.

**FINDING-958.** (A-33) [not changed in round 3] rule 3; checked. *§4.2, Why a devlog* (lines 346–351): "Three payoffs: (1) dead ends are recorded, … — "tried caching …" saves the next attempt; (2) resuming …; (3) it is what the records above it are written from". The three parts are numbered inside one sentence and joined by semicolons and a dash. Proposed: fix: "Three payoffs:", then a list of three, each one item, with the caching example as its own sentence in item 1. Changed in part (349–351).

**FINDING-959.** (A-34) [not changed in round 3] rule 8; resting on the reader. *§5.4, How an item is written* (lines 421, 429–430): "The story is not, because the devlog already holds it."; "tighter, it cut meaning; looser, an item grows back into its story." The first leaves the reader to supply "is not there". The second is two compressed clauses, one of them in the past tense with no event named. 2 instances. Proposed: fix: "The story is not there, because the devlog already holds it."; "When it was capped tighter, it lost meaning. When it is looser, an item grows back into its story." Unchanged.

**FINDING-960.** (A-35) [not changed in round 3] rule 2; checked. *§9.4, How a playbook is written*, item 1 (lines 659–660): "Born without one, the Record Stub's placeholders are filled in place. How is the CBC Run's PLAN Record Stub." In the first sentence "born" attaches to the placeholders, not the CBC Run. The second is a fragment the reader has to rebuild. Proposed: fix: "A CBC Run born without one fills the Plan Stub's placeholders in place. The Plan Stub says how." (Plan Stub per FINDING-941's answer.) Unchanged.

**FINDING-961.** (A-36) [change not traced] rule 6; uncertain. *§6.3, Where the changelog lives* (lines 470–471): "says what at its Framing Plan Step"; *§9.4* (line 674): "The CBC Framing and Release Plan Steps". The playbook titles its Step 1 "CBC Framing" (`delivery/fills/cbc-run-pure-playbook.md`). So "Framing Plan Step" is a third label for that Plan Step, or a different one, since line 470 is about any concept or docs repo. Question: does line 470 mean a CBC Run's CBC Framing Plan Step (then "its CBC Framing Plan Step"), or any repo's framing (then lowercase English, "at its framing")? Changed.

**FINDING-962.** (A-37) [changed in round 3] rule 8; uncertain. *§8.1, What ARCHITECTURE is* (lines 567–568): "A Plan Step's contract, once certified, is history". "Contract" and "certified" are defined nowhere in this file and have no Name. The reader cannot tell what a Plan Step's contract is. Proposed: question: what is meant, a CBC Run's Invariant Slice Record or its Plan Step Gate? Then say it by that Name: "What a closed Plan Step proved is history". Changed.

**FINDING-963.** (A-38) [changed in round 3] rule 9; uncertain. *§8.4, How ARCHITECTURE is written* (line 594): "The why behind a shape is the ADR's"; *§11*'s drawing (line 734): "when the Plan Step changed the system's shape". ADR-0074 listed "shape" among the words with more than one meaning here, and Output Shape is a delivered Name. 2 instances. Proposed: fix: "The why behind a design choice is the ADR's"; "changed the system's structure". Changed.

**FINDING-964.** (A-39) [change not traced] rule 3; resting on the reader. Dashes that set off an aside inside a sentence: line 226 ("at any moment — the three questions"), 277 ("consequences — including the downsides"), 400 ("deferral *explicit* — "we know"), 406 ("when there's a team — same structure"), 643–644 ("the type — the one a project's "Steps from" line names —"), 698 ("too large for an ADR — a multi-page proposal"), 791 ("its path** — and adding a record"), 803 ("not a restatement — it says when to go"). 8 instances. Proposed: fix: end the sentence before the dash, and give the aside a sentence of its own. Changed in part (226 sits in a hunk); the rest unchanged.

**FINDING-965.** (A-40) [not changed in round 3] rule 10; uncertain. *§12* (line 759): "Minimum viable set"; *§13.1* (line 788): "What a row holds"; *§13.2* (line 806): "The table's anti-patterns". Read alone in a Fact Reference, none of the three says what it is about: a set of what, a row of what, which table. Proposed: fix: *The fewest records needed* (26 characters), *What a records table row holds* (30), *Records table anti-patterns* (27), with the rename grep. Unchanged.

**FINDING-966.** (A-41) [changed in round 3] rule 2; resting on the reader. *§13, The records table* (lines 781–783): "The Entry File, the one file loaded before any task, what it may hold and how it stays small, is the agent-arrangement manual's". Two asides sit between the subject and the verb. The second can be read as part of the subject. Proposed: fix: "The Entry File is the one file loaded before any task. What it may hold, and how it stays small, is the agent-arrangement manual's (…)." Changed.

**FINDING-967.** (A-42) [change not traced] rule 9; resting on the reader. Lines 33 ("in a file `docs/conventions/agent-arrangement/` owns"), 254 ("`RETRO.md`, by `docs/conventions/retrospective/`") and 859 ("the failure `docs/conventions/agent-arrangement/` measured, in its *What it is for*"). In each, a path is the doer of a verb. DECISION-27 names a manual with its kind word and keeps a path for a Fact Reference. Line 207 of the same file already writes "the agent-arrangement manual's". 3 instances. Proposed: fix: "in a file the agent-arrangement manual owns"; "`RETRO.md`, under the retrospective manual (`docs/conventions/retrospective/`)"; "the failure the agent-arrangement manual measured (`docs/conventions/agent-arrangement/`, *What it is for*)". Changed in part (858–859); 33 and 254 unchanged.

**FINDING-968.** (A-43) [not changed in round 3] rule 9; uncertain. *§3.3, Where ADRs live* (line 290): "in PLAN.md's Decision index"; *§13.2* (line 809): "It belongs in PLAN.md; the table's row for PLAN.md". This is the path outside backticks, 3 times, where the rest of the file writes `PLAN.md`. The index is also "Decision index" at 290 (the Plan Stub's heading, `## Decision index`) and "decision index" at 89. Proposed: fix: "`PLAN.md`" in all three; "Decision index" at 89, keeping the heading's case. Changed in part (89, 808–810); 290 unchanged.

**FINDING-969.** (A-44) [not changed in round 3] rule 2; resting on the reader. *§1, The records at a glance* (lines 162–164): "How the records feed each other, a picture for each Convention Seat. An arrow says what a record holds for the plan; when a record is opened is each Convention Seat's records table's (§13, *The records table*)." The first sentence has no verb. The second ends on a stacked possessive. Proposed: fix: "Each Convention Seat has a picture of how the records feed each other. An arrow says what a record holds for the plan. When a record is opened is in each Convention Seat's records table (§13, *The records table*)." Unchanged.

#### Reader B, Layer 3: the index and five manuals

##### `docs/conventions/README.md`

**FINDING-970.** (B-1) [not changed in round 3] rule 9; checked.
`docs/conventions/README.md` *The chain* (line 35): "only `commit-plan`". The name stands bare, with no kind word. DECISION-24, as widened, and DECISION-27 require the kind word always: "the commit-plan Agent Skill" or "the commit-plan manual". Also `docs/conventions/README.md` lines 34, 36, 44: 3 more in prose. The drawing's labels at lines 20–22, "visual-comparison", "commit-plan", "commit-messages", are 3 more, since DECISION-21 says rule 9 reaches drawn text and the boxes have room. Proposed: question: which kind word does the chain mean? Recommended: "Agent Skill", since the text says each one "fires" at its moment, and line 44 is the shipped Agent Skill ("a project on another stack can use it unchanged"). So: "only the commit-plan Agent Skill", and box labels "commit-plan Agent Skill" and so on. Unchanged.

**FINDING-971.** (B-2) [not changed in round 3] rule 9; checked.
`docs/conventions/README.md` *The chain* (line 39): "not from this chain". DECISION-23 chose plain words for "the chain", since it clashes with Chain Link: "the order the conventions act in". Also `docs/conventions/README.md` line 12, the heading "## The chain", and line 47, "**What the chain produces**": 2 more. Also `docs/conventions/commit-plan/README.md` line 182, "the index's chain": 1 more (B-3). Proposed: fix: heading "## The order of the conventions"; line 39 "not from this order"; line 47 "**What this order produces**". Unchanged.

**FINDING-972.** (B-3) [not changed in round 3] rule 9; checked.
`docs/conventions/commit-plan/README.md` *What this does not cover* (line 182): "the index's chain". `docs/conventions/README.md` is a Local Map, so "the index" is a second word for a Glossary Name. The line also uses "chain" (B-2). Also `docs/conventions/facts-in-sync/README.md` *Point and derive* (line 111): "another manual, the index": 1 more. Proposed: fix: "the order in the conventions' Local Map, `docs/conventions/README.md`, says which"; and at line 111, "another manual, a Local Map, `ARCHITECTURE.md`". Unchanged.

##### `docs/conventions/agent-arrangement/README.md`

**FINDING-973.** (B-4) [changed in round 3] rule 9; checked.
`docs/conventions/agent-arrangement/README.md` *The CBC Run's seat* (line 55): "the only method work is running `cbc-framing`". The kind word is missing (DECISION-27). The shipped Entry File itself writes "running the cbc-framing Agent Skill". Also line 95: "because `exchange-read` reads them": 1 more. Lines 58 and 80 write "the retrospective's": 2 more, where a one-word convention stands bare (DECISION-24). Proposed: fix:
- line 55: "running the cbc-framing Agent Skill";
- line 95: "because the exchange-read Agent Skill reads them";
- line 58: "the retrospective Agent Skill and the apply-retrospective Agent Skill among them";
- line 80: "not the retrospective manual's Agent Skills".

Changed.

**FINDING-974.** (B-5) [not changed in round 3] rule 9; checked.
`docs/conventions/agent-arrangement/README.md` §2.4, *How the Entry File is written* (line 196): "three the Record Stub's guard comment states". Line 30 says the shipped Entry File is "not a Record Stub". The guard comment is the Entry File's own. Also line 412, "the Record Stub" carries the test; and line 590, "The Record Stubs: `delivery/container/.claude/CLAUDE.md`": 2 more. Round 3's *Met in round 3* list already notes line 590 against line 30. Proposed: fix:
- line 196: "the Entry File's guard comment";
- line 412: "the shipped Entry File carries the test";
- line 590: "The Entry File and the Decisions Log's Record Stub: …".

Unchanged.

**FINDING-975.** (B-6) [not changed in round 3] rule 9; uncertain.
`docs/conventions/agent-arrangement/README.md` §3.4, *`.claude/decisions.md`* (line 330): "own Record Stub." The subject is the Concept Deliverer's Decisions Log. A Record Stub is a shipped file as it is born, and the Concept Deliverer's log is neither. Proposed: fix: "Its rules sit in its header comment." Unchanged.

**FINDING-976.** (B-7) [changed in round 3] rule 9; checked.
`docs/conventions/agent-arrangement/README.md` §5.5, *Agent Skills* (line 503): "in an Agent Skill as in a rule. Our `foundation` lines". The line has two faults:
- "a rule" stands for Agent Rule;
- "`foundation` lines" stands for Foundation Lines.

Also `docs/conventions/facts-in-sync/README.md` §4 step 3 (line 280): "in `foundation` lines": 1 more. Proposed: fix: "in an Agent Skill as in an Agent Rule. Our Foundation Lines are for a reader of the file"; and at line 280, "for its name in Foundation Lines". Changed (503); unchanged (280).

**FINDING-977.** (B-8) [not changed in round 3] rule 5; checked.
`docs/conventions/agent-arrangement/README.md` §4, *Arrangement anti-patterns* (line 424): "**Parking a repeated rule in the operator's file**". DECISION-26's table fixes "park". Proposed: fix: "**Keeping a repeated rule in the operator's file**". Unchanged.

**FINDING-978.** (B-9) [not changed in round 3] rule 6; checked.
`docs/conventions/agent-arrangement/README.md` §4, *Arrangement anti-patterns* (line 406): "**Putting rules in the working-style slot**". §2.4 names this slot *How to work here* (lines 232, 240). "Working-style" is a third word for it. Also line 411: "**Shipping the stance and local-rules slots as empty sections**": 1 more, for *How to work here* and *Local rules*. Proposed: fix: "**Putting rules in the *How to work here* slot**"; and at line 411, "the *How to work here* and *Local rules* slots". Unchanged.

**FINDING-979.** (B-10) [changed in round 3] rule 9; uncertain.
`docs/conventions/agent-arrangement/README.md` §4, *Arrangement anti-patterns* (line 416): "drifts from the source". The glossary's Foundation Line entry retires *source*: it "was a CBC Run's word for the Concept Deliverer, and is not ours". Here the word means the convention's manual. Proposed: fix: "drifts from its manual". Changed.

**FINDING-980.** (B-11) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/agent-arrangement/README.md` §2.6, *The Entry File's size* (line 270): "So the guard and the". This manual never says in plain words what "the guard" is. Also lines 558 and 567: 2 more. Proposed: fix: at line 270, the first use, write "the guard comment, the Entry File's comment that holds the three tests". Changed.

**FINDING-981.** (B-12) [not changed in round 3] rule 3; resting on the reader.
`docs/conventions/agent-arrangement/README.md` *What the difference is* (line 109): "`delivered-copies.md` — how to take a newer copy". One sentence carries both seats' holdings, joined by a dash gloss and a semicolon. Also §3.4 (line 324): "is a comment in the file it governs; the Decisions Log keeps the why": 1 more, three clauses on semicolons. Proposed: fix: "The CBC Run holds the receiver's Agent Rule, `delivered-copies.md`. It says how to take a newer copy without losing its own edits, and what it may do to one meanwhile. The Concept Deliverer holds its Agent Skills and the form of the CBC Run Reading they produce." Line 324 splits the same way, into three sentences. Unchanged (109–110); changed (108, 324).

**FINDING-982.** (B-13) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/agent-arrangement/README.md` §2.2, *Why an Entry File* (line 181): "It earns that by holding only what". The sentence before is about the agent and the files. "It" means the Entry File, three sentences back. Proposed: fix: "The Entry File earns that by holding only what every session needs". Changed.

**FINDING-983.** (B-14) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/agent-arrangement/README.md` §1.3, *Not records* (line 154): "convention that owns the content states the touch". The text does not say which "two sides" are meant. "States the touch" does not say what is written. Proposed: fix: "Where a project fact sits in an arrangement file, the convention that owns the fact states it, and this one holds the file it sits in". Changed.

**FINDING-984.** (B-15) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/agent-arrangement/README.md` §2.4, *How the Entry File is written* (line 250): "be running fails: each has a moment". Three subjects share one singular verb, and the object it fails is left out. Proposed: fix: "A test prerequisite, a migration rule or a service that must be running fails this test: each has a moment". Changed.

**FINDING-985.** (B-16) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/agent-arrangement/README.md` *Why it arrives this way* (line 564): "where it stands, and an Agent Skill fires only on recognising the moment". One sentence chains the case and the reason. "Where it stands" has no clear meaning. Proposed: fix: "Told "remember X", an agent writes X into the Entry File. An Agent Skill would fire only if the agent recognised the moment, and here it does not." Changed.

**FINDING-986.** (B-17) [not changed in round 3] rule 10; uncertain.
`docs/conventions/agent-arrangement/README.md` §5.1 (line 441): "### 5.1 The mapping". The title does not stand alone. In the Fact Reference at line 187, "(§5.1, *The mapping*)", the reader cannot tell what is mapped to what. Proposed: fix: "### 5.1 Channels to mechanisms", 22 characters, with the rename grep. Unchanged.

**FINDING-987.** (B-18) [not changed in round 3] rule 9; uncertain.
`docs/conventions/agent-arrangement/README.md` §3.9 (line 392): "### 3.9 A rule loaded in every session". Here "rule" stands for Agent Rule, inside a numbered title that six or more Fact References carry. "An Agent Rule loaded in every session" is 37 characters, over rule 10's 30. Proposed: question: keep the title, or retitle "An Agent Rule always loaded" (27 characters) with the rename grep. Unchanged.

##### `docs/conventions/commit-messages/README.md`

**FINDING-988.** (B-19) [not changed in round 3] rule 9; checked.
`docs/conventions/commit-messages/README.md` *What it is for* (line 19): "alone with no gate." This is the Agent Model's sense of "gate", which DECISION-19's table (question 2) named Enforcement Gate. Each use of "the gate" was to be read by hand. Proposed: fix: "with no Enforcement Gate." Unchanged.

**FINDING-989.** (B-20) [not changed in round 3] rule 9; checked.
`docs/conventions/commit-messages/README.md` §2.4, *Commit on the word* (line 82): "so the agent stages, shows the diff, and waits". The bare verb has no object. The glossary's Delivery Staging entry says the verb names its object, since git's verb is the same word. Proposed: fix: "so the agent stages the commit, shows the diff, and waits". Unchanged.

**FINDING-990.** (B-21) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/commit-messages/README.md` *What this is made usable as* (line 26): "the `agent` scope, the stop,". This manual never names "the stop" where it states the rule. §2.4 describes the stop without the label. Also line 18, "the stop sentence", and line 117, "the `agent` scope and the stop": 2 more. Proposed: fix: §2.4 gives the label: "…shows the diff, and waits for the word: the stop." Line 18, met first, says "the stop sentence, the rule that the agent waits at each commit". Unchanged (18, 26); changed (117).

**FINDING-991.** (B-22) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/commit-messages/README.md` *The seats* (line 39): "It has one local habit, which scope carries the". It reads as a relative clause. The habit is what the commit's scope signals. Proposed: fix: "It has one local habit: the scope, not the type, carries the signal. It is stated in its own section and not shipped (§3, …)." Changed.

**FINDING-992.** (B-23) [changed in round 3] rule 5; checked.
`docs/conventions/commit-messages/README.md` §3, *The Concept Deliverer's habit* (line 107): "That is the mirror of the". "Mirror" is a figure. Proposed: fix: "It is the other answer done with the scope instead of the type, and not a weaker version of it." Changed.

##### `docs/conventions/commit-plan/README.md`

**FINDING-993.** (B-24) [changed in round 3] rule 9; checked.
`docs/conventions/commit-plan/README.md` §2.6, *What a plan counts* (line 100): "A plan counts commits, never steps." The word stands for Plan Step. The sentence after it quotes "Step" as `PLAN.md`'s word, and that word is now the Name. Proposed: fix: "A plan counts commits, never Plan Steps." Changed.

**FINDING-994.** (B-25) [changed in round 3] rule 8; checked.
`docs/conventions/commit-plan/README.md` §2.11, *Small commits* (line 148): "(§2.13, *The stop at every boundary*)". A same-document reference comes right after "the commit-messages manual's rule". A reader takes it as that manual's §2.13, which does not exist. And this manual's §2.13 only points on. Proposed: fix: "(`docs/conventions/commit-messages/` §2.4, *Commit on the word*)". Changed.

**FINDING-995.** (B-26) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/commit-plan/README.md` §2.8, *Counting subjects* (line 117): "A subject is counted when it is written." What is counted is the subject's characters, against the 50 limit. Nothing in the section says so. Also line 149: "Each small commit is counted": 1 more. Proposed: fix: "A subject's characters are counted against the 50 limit when it is written." Changed.

**FINDING-996.** (B-27) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/commit-plan/README.md` §2.11, *Small commits* (line 144): "Each planned commit landing as one leaves no room to try". A participle phrase is the subject, and "two ways meant" follows on a colon. Proposed: fix: "When each planned commit lands as one, there is no room to try. Trying two ways meant reworking a commit in place." Changed.

**FINDING-997.** (B-28) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/commit-plan/README.md` *What it is for* (line 12): "The failure it answered was lived elsewhere". "Elsewhere" is never named. Then "It is not ours to restate." (line 14) tells the reader nothing they can use (rule 7). Proposed: fix: name the place in plain words, as the agent-arrangement manual does: "lived in the handbook, the repo this convention came from, now history (ADR-0038)". Cut "It is not ours to restate." Changed.

**FINDING-998.** (B-29) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/commit-plan/README.md` §2.10, *The sweep* (line 136): "It reads the text unwrapped." The sentence before is about "a commit's own grep". "It" means the sweep. Proposed: fix: "The sweep reads the text unwrapped." Changed.

**FINDING-999.** (B-30) [changed in round 3] rule 3; resting on the reader.
`docs/conventions/commit-plan/README.md` *Why it arrives this way* (line 168): "its moment is one the agent recognises — work turning". A pair of dashes holds a gloss inside a three-part sentence. Proposed: fix: "An Agent Skill, because the agent recognises its moment: work turning out to need several commits. Nothing in a record would put the plan in front of it then (…)." Changed.

**FINDING-1000.** (B-31) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/commit-plan/README.md` §2.5, *The records commits* (line 94): "Change Set batches record moments". "Record moments" is not defined. "Before its truth exists" (line 95) is not plain. Proposed: fix: "A Change Set gathers the moments its records name. A record's moment can come mid-set, before the fact it records is true." Changed.

##### `docs/conventions/exchange/README.md`

**FINDING-1001.** (B-32) [not changed in round 3] rule 9; checked.
`docs/conventions/exchange/README.md` *What this is made usable as* (line 51): "What `exchange-read` writes". The kind word is missing (DECISION-27). Also:
- line 310, "in `exchange-deliver`";
- line 511, "which its copy in `cbc-slice` follows";
- line 534, "facts-in-sync owns that rule", a convention without its kind word (DECISION-24, widened).

That is 3 more. Proposed: fix:
- line 51: "the exchange-read Agent Skill";
- line 310: "in the exchange-deliver Agent Skill";
- line 511: "in the cbc-slice Agent Skill";
- line 534: "the facts-in-sync manual owns that rule".

Unchanged (51, 511); changed (310, 534).

**FINDING-1002.** (B-33) [not changed in round 3] rule 9; checked.
`docs/conventions/exchange/README.md` §2.5, *One cycle* (lines 149, 153, 154): "pin = X", "read-through = r", "(named in the note, recorded at t)". DECISION-21 covers drawn text:
- a Name goes where its box has room;
- otherwise, one line above the drawing says which short word stands for which Name.

The key below uses the Names, but no line maps "pin" or "read-through" to them. "The note" has room for "Delivery Note". Proposed: fix: "(named in the Delivery Note, recorded at t)". Add one line above the drawing: "pin is the Delivery Pin; read-through is the Read-Through Commit." Unchanged.

**FINDING-1003.** (B-34) [changed in round 3] rule 9; checked.
`docs/conventions/exchange/README.md` §3.4, *One group per file* (line 236): "Staging writes it in." The noun stands with no object, and the glossary says the verb names its object. Proposed: fix: "Staging a delivery writes it in." Changed.

**FINDING-1004.** (B-35) [changed in round 3] rule 3; checked.
`docs/conventions/exchange/README.md` §3.7, *The Delivery Note* (line 281): "which is about our whole tree. A Delivery Note fails to reach when it". The next paragraph runs on inside the third bullet. So a list announced as three claims (line 277) holds a fourth, unrelated idea. Also, "a thin Delivery Note" is a note, not a claim. Proposed: fix: end the bullet at "tree."; a blank line; then "A Delivery Note fails to reach when …" as its own paragraph. The lead becomes "Three kinds of Delivery Note cannot avoid it". Changed.

**FINDING-1005.** (B-36) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/exchange/README.md` *What this is made usable as* (line 41): "read the three things §6.1 names". The section number has no title, and the reader does not hold it. Proposed: fix: "read its Decisions Log, its backlog and the diff of its copies (§6.1, *Reading a CBC Run*)". Changed.

**FINDING-1006.** (B-37) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/exchange/README.md` *What it is for* (line 15): "Not version control: a Delivery Pin is one part of it." The subject of "Not" is missing, and "it" could be the exchange or version control. Proposed: fix: "The exchange is more than version control: a Delivery Pin is only one part of it." Changed.

**FINDING-1007.** (B-38) [changed in round 3] rule 5; resting on the reader.
`docs/conventions/exchange/README.md` §3.1, *Delivery Staging* (line 179): "the CBC Run's tree is checked quiet first". "Quiet" is a figure for a clean tree. Proposed: fix: "checked clean first". Changed.

**FINDING-1008.** (B-39) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/exchange/README.md` §3.7, *The Delivery Note* (line 288): "That is the Told". "That" could be the citation or the prompt. Proposed: fix: "A prompt is the Told Channel's text, so the same holds for it." Changed.

**FINDING-1009.** (B-40) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/exchange/README.md` §5.1, *When a copy may be edited* (line 401): "second condition does not hold it; the other two do." "Hold it" is unclear. It means the condition does not apply. Proposed: fix: "so the second condition does not apply to it; the other two do." Unchanged.

**FINDING-1010.** (B-41) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/exchange/README.md` §5.2, *A finished copy* (line 413): "Plan Step here." Elsewhere in this manual "here" is the Concept Deliverer, as in §6.5, "a Master Copy changes here". In §5.2 it is the CBC Run. Proposed: fix: "by the next Plan Step of this CBC Run". The label *untried here* (line 414) stays, as the CBC Run's own words. Changed.

**FINDING-1011.** (B-42) [not changed in round 3] rule 8; checked.
`docs/conventions/exchange/README.md` §5.4, *One word for the other side* (line 427): "and the shipped Agent Rule says one thing." The sentence does not name the Agent Rule, `delivered-copies.md`, or the "one thing", Concept Deliverer. Proposed: fix: "and the shipped Agent Rule, `delivered-copies.md`, uses that one word." Unchanged (427); the sentence's first half changed (426).

**FINDING-1012.** (B-43) [not changed in round 3] rule 9; uncertain.
`docs/conventions/exchange/README.md` §6.5, *Verdicts* (line 542): "An unverifiable promise is worse than any of the three." "Promise" sits beside the method's Falsifiable Promise. Here it means a verdict that cannot be checked. Proposed: fix: "A verdict that cannot be checked is worse than any of the three." Unchanged.

**FINDING-1013.** (B-44) [changed in round 3] rule 9; uncertain.
`docs/conventions/exchange/README.md` §2.4, *The records' exception* (line 131): "`PLAN`, `TODO`". These are in code font but are not paths. A path is written as it is. Also `docs/conventions/facts-in-sync/README.md` line 20, "four records: PLAN, the": 1 more. Proposed: fix: "`PLAN.md`, `TODO.md` and the devlog"; and "four records: `PLAN.md`, the devlog …". Changed.

##### `docs/conventions/facts-in-sync/README.md`

**FINDING-1014.** (B-45) [not changed in round 3] rule 9; checked.
`docs/conventions/facts-in-sync/README.md` §1, *One home* (line 98): "Each file's header comment is living text." Living Text is a Glossary Name, from DECISION-23, and its home is this section. Also:
- line 206, §3.3: "greps all living text", the second sweep line, 1 more;
- line 100: "gets a living home", 1 more, uncertain: it means a home in Living Text.

Proposed: fix:
- line 98: "is Living Text";
- line 206: "greps all Living Text";
- line 100: "gets a home in Living Text".

§1 also needs its defining sentence (see *Met in passing*). Bold is allowed there (DECISION-22). Unchanged.

**FINDING-1015.** (B-46) [changed in round 3] rule 8; checked.
`docs/conventions/facts-in-sync/README.md` *What it is for* (line 18): "the handbook's Entry File held three disagreeing copies of one rule". This is the file's first "the handbook", with no plain words. DECISION-23 says it is introduced once per file, where first met. Proposed: fix: "the Entry File of the handbook, the repo the arrangement came from, now history (ADR-0038), held three disagreeing copies of one rule". Changed.

**FINDING-1016.** (B-47) [changed in round 3] rule 9; checked.
`docs/conventions/facts-in-sync/README.md` §3.4, *A decision citation* (line 233): "seat can open only its own ADRs". A lowercase "seat" stands for Convention Seat in prose. Also the headings *The CBC Run's seat* and *The Concept Deliverer's seat* (lines 50, 63, and `docs/conventions/agent-arrangement/README.md` lines 49, 69), and their Fact References at lines 35 and 39: uncertain. They sit under the manual form's fixed heading *The seats*. Proposed: fix: "A Convention Seat can open only its own ADRs". Question: do the per-seat headings take "Convention Seat", as in *The CBC Run's Convention Seat*? Changed.

**FINDING-1017.** (B-48) [not changed in round 3] rule 6; checked.
`docs/conventions/facts-in-sync/README.md` §3.1, *What a Fact Reference is* (line 153): "*A skill's template". The example quotes an old bold lead. `delivered-copies.md` rule 8 now reads "An Agent Skill Template is copied and filled, never edited in…". A reference reworded points elsewhere, and this example teaches the form. Proposed: fix: "rule 8, *An Agent Skill Template is…*", 26 characters before the "…". Unchanged.

**FINDING-1018.** (B-49) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/facts-in-sync/README.md` §5, *A disagreement* (line 331): "`convention-lifecycle` on the day it first ran under it". The reader does not hold this retired name. "Argued down" (line 330) is also a figure. Proposed: fix: "CBC Run 3 showed a clause of `convention-lifecycle`, the receiver's protocol then, wrong on the day it first ran under it, and the clause changed". Unchanged.

**FINDING-1019.** (B-50) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/facts-in-sync/README.md` §1, *One home* (line 86): "retelling whose host is itself a Canonical Description". "Host" is not said in plain words. Also §4 step 3 (line 283): "a host that changes for it is walked in": 1 more. Proposed: fix: "a retelling that sits in a Canonical Description sets off that text's Change Walk in turn". Changed (86); unchanged (283).

**FINDING-1020.** (B-51) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/facts-in-sync/README.md` *What it is for* (line 26): "found the One home and Dependencies Finding Kinds". The reader holds neither label. Proposed: fix: "found two Finding Kinds, One home and Dependencies, the checks of a fact's home and of what a text stands on, resting on rules split that way". Changed.

**FINDING-1021.** (B-52) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/facts-in-sync/README.md` §4 step 2 (line 265): "`foundation` per file, the Foundation Line's document, what the whole of it stands on." Three appositives, one after another, describe one thing. Proposed: fix: "Each derived thing names its Canonical Description once, in its one Foundation Line: the document the whole file stands on." Changed.

**FINDING-1022.** (B-53) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/facts-in-sync/README.md` *Why it arrives this way* (line 343): "One home's moment is". The section title is used as the name of an Agent Rule, and it reads as a phrase. Proposed: fix: "The one-home Agent Rule's moment is every text written." Unchanged.

#### Reader C, Layer 3: repo-hygiene, retrospective, shapes, visual-comparison, writing, the glossary

##### `docs/conventions/repo-hygiene/README.md`

**FINDING-1023.** (C-1) [not changed in round 3] rule 5; checked.
`docs/conventions/repo-hygiene/README.md` *What this is made usable as* (line 26): "never travel again." DECISION-26's journey row says to fix "travels" with plain words. Also `docs/conventions/shapes/README.md` 163, 175, 246, 247, 248, 249: 7 more uses on 6 lines ("travels whole", "travels as a copy", "What travels upward", "It travels by being *read*", "What must not travel", "the skeleton travels"). Also `docs/conventions/visual-comparison/README.md` 99: 1 more ("does not travel"). Proposed: fix: "they are never delivered again"; shapes, "is delivered whole", "An Output Shape is delivered as a copy", "What goes upward is a **finding**", "It reaches the Concept Deliverer by being *read*, not by being sent", "What must not be passed on", "the skeleton is passed on"; visual-comparison, "is provisional and is not delivered". Mixed: repo-hygiene 26, shapes 175, 246, 249 and visual-comparison 99 unchanged; shapes 163, 247, 248 changed.

**FINDING-1024.** (C-2) [not changed in round 3] rule 8; checked.
`docs/conventions/repo-hygiene/README.md` §1, *The three files* (line 53): "\"Safe reservations\" — rules fire only on files you touch". This is a coined label in quotes, and no text in the repo defines it. The Hygiene Base's `.editorconfig` explains the same idea with no such name ("When rules fire", "Never on their own"). The cell also chains three parts with a dash, a parenthesis and a semicolon (rule 3). Proposed: fix: "Rules fire only on files you touch, at the moments the file's labels name (`[creating] [typing] [save] [format]`). Untouched files keep their bytes." Unchanged.

**FINDING-1025.** (C-3) [not changed in round 3] rule 5; uncertain.
`docs/conventions/repo-hygiene/README.md` §1, *The three files* (line 52): "Line-ending truth (`* text=auto eol=lf`)". "Truth" stands for the rule the line sets. Proposed: fix: "The line-ending rule (`* text=auto eol=lf`)", or decline if the reviewer reads it as dead. Unchanged.

**FINDING-1026.** (C-4) [changed in round 3] rule 8; uncertain.
`docs/conventions/repo-hygiene/README.md` *What it is for* (line 17): "at the Plan Step that makes the stack true". The reader has to work out which Plan Step "makes the stack true" means. The playbook calls it "Step 4: CBC Bootstrap", and CBC Bootstrap is a Glossary Name in the stack's file. The Hygiene Base's marker lines call the same moment "app bootstrap". Also lines 41, 64-65, 71, 112: 4 more. Proposed: question: should the manual name it "the CBC Bootstrap Plan Step", or keep a phrase that fits any stack? If the phrase stays, say it once in plain words, for example "the Plan Step that first builds the application on its stack". Mixed: lines 17, 65, 71 and 112 changed; 41 and 64 unchanged.

**FINDING-1027.** (C-5) [changed in round 3] rule 2; uncertain.
`docs/conventions/repo-hygiene/README.md` *What it is for* (lines 9-11): "Adopted with the Container Group (ADR-0038); no failure of the Concept Deliverer's is recorded before it." Two ideas are joined by a semicolon. Proposed: fix: "Adopted with the Container Group (ADR-0038). No failure of the Concept Deliverer's is recorded before it." Mixed: lines 9 and 11 changed, 10 unchanged.

##### The hygiene templates

No finding. One copy difference is listed under *Met in passing*.

##### `docs/conventions/retrospective/README.md`

**FINDING-1028.** (C-6) [changed in round 3] rule 8; checked.
`docs/conventions/retrospective/README.md` *What it is for* (line 26): "CBC Run 3 kept both as Agent Skills, and offered them." "Both" has no two-item antecedent: it comes right after a list of three things the retrospective did. The two meant are the look back and the applying of its lessons. Proposed: fix: "CBC Run 3 kept the look back and the applying of its lessons as two Agent Skills, and offered them." Changed.

**FINDING-1029.** (C-7) [changed in round 3] rule 5; checked.
`docs/conventions/retrospective/README.md` §2, *How the look back decides* (line 117): "They are prompts, inside the walk:". DECISION-26's journey row says to fix "the walk". Proposed: fix: "They are prompts, asked while the CBC Run is read part by part:". Changed.

**FINDING-1030.** (C-8) [not changed in round 3] rule 5; checked.
`docs/conventions/retrospective/README.md` §4, *`RETRO.md`* (line 155): "every decision, the experiments, what was parked". DECISION-26's debt row says to fix "park". Proposed: fix: "what was set aside for later". Unchanged.

**FINDING-1031.** (C-9) [not changed in round 3] rule 6; uncertain.
`docs/conventions/retrospective/README.md` §4, *`RETRO.md`* (line 159): "from the note." Within six lines `RETRO.md` is called three things: "`RETRO.md`", "The look back's record" and "the note". Also line 164: 1 more ("the note closing"). The retrospective Agent Skill also says "the note", so the manual may be copying its word. Proposed: fix: "`RETRO.md`" at lines 159 and 164. Unchanged.

**FINDING-1032.** (C-10) [not changed in round 3] rule 2; checked.
`docs/conventions/retrospective/README.md` §3, *How the lessons are applied* (lines 134-135): "**History is never touched,** and the records later Plan Steps were built on change only by a dated revision entry." This misleads on first reading: "the records later Plan Steps" reads as one noun phrase, and the verb, "change", comes late. Proposed: fix: "**History is never touched.** A record that later Plan Steps were built on changes only by a dated revision entry." Unchanged.

**FINDING-1033.** (C-11) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/retrospective/README.md` §3, *How the lessons are applied* (line 136): "A new test was never seen fail." The reason is left for the reader to work out: a test written after the build was never seen to fail, so it proves nothing. Proposed: fix: "A test written now was never seen to fail, so it proves nothing yet." Unchanged.

**FINDING-1034.** (C-12) [changed in round 3] rule 8; uncertain.
`docs/conventions/retrospective/README.md` §3, *How the lessons are applied* (lines 141-142): "README last. The plain-words rewrite goes last." Two things are both "last" within two lines, and the reader cannot tell which comes first. Proposed: question: which goes last? If the rewrite does: "Owners go before the records that summarize them, README last of these. The plain-words rewrite comes after all of them." Changed.

**FINDING-1035.** (C-13) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/retrospective/README.md` *The Concept Deliverer's seat* (lines 87-90): "in place of that item." and "The next Plan Step stands where a CBC Run has its next CBC Run." "That item" points back two sentences to a quoted close line, and the reader must find it. "Stands where" is a figure for "plays the part of". Proposed: fix: "in place of that close line." and "For this repo, its next Plan Step plays the part a next CBC Run plays for a CBC Run." Changed.

**FINDING-1036.** (C-14) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/retrospective/README.md` *The CBC Run's seat* (line 58): "**They get:**". The subject just before is "the reviewer", which is singular. "They" could mean the reviewer and the agent, or the CBC Run. Also line 71: 1 more ("**They get** the CBC Run's records improved"). Proposed: fix: "**The CBC Run gets:**" in both. Changed.

**FINDING-1037.** (C-15) [changed in round 3] rule 8; uncertain.
`docs/conventions/retrospective/README.md` *The CBC Run's seat* (line 64): "each triage row;". "Triage" is the apply-retrospective Agent Skill's Stage 1. The manual uses it twice (lines 64-65 and 71) and never says what it is. Proposed: fix: at first use, "each triage row: a decision marked applied, partly applied, or next CBC Run only;". Changed.

**FINDING-1038.** (C-16) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/retrospective/README.md` *The CBC Run's seat* (line 62): "the next CBC Run's checks, listed for its plan." The retrospective Agent Skill makes these Plan Step Gate items that only the next CBC Run can check. The manual's words do not say so. Proposed: fix: "the Plan Step Gate items only the next CBC Run can check, each with the Plan Step that judges it." Changed.

**FINDING-1039.** (C-17) [changed in round 3] rule 2; checked.
`docs/conventions/retrospective/README.md` *What it is for* (lines 12-14): "so the section's moment never came; the retrospective happened only because the reviewer asked for one." Two ideas are joined by a semicolon, after a sentence that already carries an aside. Proposed: fix: end at "never came." and start a new sentence, "The retrospective happened only because the reviewer asked for one." Changed.

**FINDING-1040.** (C-18) [not changed in round 3] rule 2; resting on the reader.
`docs/conventions/retrospective/README.md` §1, *The two Plan Steps* (lines 97-98): "But a look that changes nothing leaves a CBC Run released with records it has shown could read better." The reader must hold a long object ("a CBC Run released with records it has shown could read better") before the sentence makes sense. Proposed: fix: "But if the look changes nothing, the CBC Run is released with records it has already shown could read better." Unchanged.

##### `docs/conventions/shapes/README.md`

**FINDING-1041.** (C-19) [changed in round 3] rule 9; checked.
`docs/conventions/shapes/README.md` §3, *Where an Output Shape lives* (lines 152-154): "A Structural Wall Backstop \"seen at the red run\", for example, can only be known by looking during the Red Run." Red Run is a Glossary Name (`delivery/method/docs/glossary/method.md`). The same sentence writes it in lowercase inside the quote and with capitals after it. The quote is also stale: the Output Shape now says "seen catching at the Red Run" (`delivery/method/.claude/shapes/slice-record.md` line 89). Proposed: fix: "A Structural Wall Backstop \"seen catching at the Red Run\", for example, can only be known by looking during the Red Run." Changed.

**FINDING-1042.** (C-20) [not changed in round 3] rule 10; checked.
`docs/conventions/shapes/README.md` §5.2 (line 276): "### 5.2 A tick, and a difference". This is two phrases joined by a comma. DECISION-20 made "What it reads, and its words" and "Detachable, and kept so" one phrase each. Proposed: fix: "### 5.2 Ticks and differences". The rename grep finds two Fact References to fix in the same commit: `TODO.md` 215 and 227. Unchanged.

**FINDING-1043.** (C-21) [changed in round 3] rule 9; checked.
`docs/conventions/shapes/README.md` §4, *An Output Shape between repos* (line 168): "a Spring Adversity Harness file's is `spring-postgres/`;". "Spring Adversity Harness" is capitalized like a Name, but neither glossary lists it. The stack's Names table (DECISION-19, row 13) ruled the stack's harness "One thing: Adversity Harness", the method's Name. Proposed: fix: "a file of the stack's Adversity Harness is `spring-postgres/`;". Changed.

**FINDING-1044.** (C-22) [not changed in round 3] rule 9; checked.
`docs/conventions/shapes/README.md` §5.2, *A tick, and a difference* (line 288): "the gate says". This means the Plan Step Gate. A lowercase word is English only, and the section's first sentence writes the Name. Also `docs/glossary.md` 152: 1 more ("read only at the gate"). The container's glossary writes "read only at a Plan Step Gate". Proposed: fix: "the Plan Step Gate says"; and in the glossary, "read only at a Plan Step Gate". Unchanged.

**FINDING-1045.** (C-23) [changed in round 3] rule 9; uncertain.
`docs/conventions/shapes/README.md` *The Concept Deliverer's seat* (lines 55-56): "Two of its own forms, a CBC Run Reading's and a manual's". These are Output Forms, and the manual is a Convention Manual: the glossary's Output Form entry says "A Convention Manual's and a CBC Run Reading's are Agent Rules today". Also `docs/glossary.md` 146 and 221 ("a record's form"), and `docs/conventions/writing/README.md` 147 ("the manual form's fixed headings"): 3 more. Proposed: fix: "Two of its own Output Forms, a CBC Run Reading's and a Convention Manual's"; question for the other three: is "a record's form" a particular Output Form named by its owner, as the entry allows, or should it be the Name? Mixed: shapes 56 and writing 147 changed; glossary 146 and 221 unchanged.

**FINDING-1046.** (C-24) [not changed in round 3] rule 3; checked.
`docs/conventions/shapes/README.md` §1.2, *How an Output Shape is born* (lines 91-95): "**it recurred**, so a pair is the evidence and what they share is the Output Shape; or **it was judged worth keeping**, so one piece was rebuilt". Two ways are chained with a semicolon and "or" in one sentence, after "Two ways one is born". A list shows the count. Proposed: fix: "Two ways one is born, and neither ranks above the other:", then two bullets. Unchanged.

**FINDING-1047.** (C-25) [not changed in round 3] rule 2; checked.
`docs/conventions/shapes/README.md` §2, *What an Output Shape is not* (lines 130-133): "Trial evidence is withheld **in order to stay** undelivered — a derivation that has seen it measures imitation instead of independence, so showing it destroys the measurement." A rule, its reason and its result sit in one sentence across a dash. Also lines 119-120 ("the failure mode it warns about — the material that does not fit gets hidden"), 95-97 ("how work should go — everything measured against it afterwards") and 301-303 ("are not reopened — each looks like"): 3 more. Proposed: fix: one sentence per idea, with no dash; for example "Trial evidence is withheld so that it stays undelivered. A derivation that has seen it measures imitation, not independence. Showing it destroys the measurement." Unchanged.

**FINDING-1048.** (C-26) [not changed in round 3] rule 5; uncertain.
`docs/conventions/shapes/README.md` §2, *What an Output Shape is not* (line 125): "An Output Shape *wants* divergence: that is how it learns". This gives a file wants and learning. Also lines 129-130 ("Their blindness runs opposite ways"), 172 ("that falls out of the groups"), 313 ("that is their force") and 114 ("four near neighbours"): 4 more. Proposed: fix: "An Output Shape expects divergence: a difference is how it gets corrected"; "They are hidden for opposite reasons"; "that follows from the groups"; "that is what makes them work"; "four things easily taken for it"; or decline the ones the reviewer reads as dead. Mixed: lines 114, 125, 129-130 unchanged; 172 and 313 changed.

**FINDING-1049.** (C-27) [changed in round 3] rule 2; checked.
`docs/conventions/shapes/README.md` *Why it arrives this way* (lines 309-311): "The first convention with no Agent Skill: its Work Approach is an Agent Rule, because the moment it serves is an Output Shape being touched, and an Agent Rule loads on the path". Four ideas are chained with a colon, "because" and "and": it is the first such convention, its Work Approach is an Agent Rule, why, and how an Agent Rule loads. Proposed: fix: "The first convention with no Agent Skill. Its Work Approach is an Agent Rule. Its moment is an Output Shape being touched, and an Agent Rule loads on that path (…)." Mixed: lines 309 and 311 changed, 310 unchanged.

**FINDING-1050.** (C-28) [changed in round 3] rule 2; checked.
`docs/conventions/shapes/README.md` *What this is made usable as* (lines 32-34): "held at `.claude/shapes/` and read at a Plan Step Gate, when the Plan Step closes: instances of this convention, each from a CBC Run's lived records, its illustration from the worked example". After the form's path-and-mark lead, five facts follow in one sentence: where, when, what they are, where each came from, and where its illustration came from. Proposed: fix: end after "when the Plan Step closes.", then "Each was written from a CBC Run's records, and carries an illustration from the worked example (§4.2, *An Output Shape's two layers*)." Mixed: lines 32-33 changed, 34 unchanged.

**FINDING-1051.** (C-29) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/shapes/README.md` §4.1, *Nothing fetched* (lines 187-190): "*Named in ADR-0037 as \"a third act of the exchange\", and never built:" The note has no subject, so the reader must guess what was named and never built (a fetch of Output Shapes at the Plan Step Gate). "For it to carry" later in the note has the same gap. Proposed: fix: "*A fetch of Output Shapes at the Plan Step Gate was named in ADR-0037 as \"a third act of the exchange\", and never built: …*". Mixed: lines 187-188 changed, 189-190 unchanged.

**FINDING-1052.** (C-30) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/shapes/README.md` §4.3, *The birth and delivery picture* (lines 236-237): "the difference in the line is the point." The reader has to work out that "the difference" is dashed against solid, meaning read against sent. Also line 242: 1 more ("What is this convention's is where the CBC Run Reading looks"), which puts its point in a clause used as subject. Proposed: fix: "The line is dashed because a CBC Run Reading reads; nothing is sent." and "This convention says where the CBC Run Reading looks: …". Changed.

**FINDING-1053.** (C-31) [not changed in round 3] rule 9; uncertain.
`docs/conventions/shapes/README.md` §4.2, *An Output Shape's two layers* (line 199): "the hand-off to make that possible." CBC Run Hand-off is a Glossary Name. Here the lowercase word means handing an Output Shape to another project, so it fails DECISION-23's test of a clash with a Name already held. Proposed: fix: "when it is handed to another project". Unchanged.

##### `docs/conventions/visual-comparison/README.md`

**FINDING-1054.** (C-32) [not changed in round 3] rule 2; checked.
`docs/conventions/visual-comparison/README.md` *Why it arrives this way* (lines 92-94): "recognises the moment by the question it is facing; no path is touched that a rule could load on, and nothing in a record would bring the method up then." Three ideas are chained with a semicolon and "and". Proposed: fix: "The agent recognises the moment by the question it is facing. No file is touched that a Paths Rule could load on. Nothing in a record would bring the method up then." (The lowercase "a rule" is in FINDING-1060.) Unchanged.

**FINDING-1055.** (C-33) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/visual-comparison/README.md` *What it is for* (lines 16-17): "It asserted the opposite of the rule the procedure existed to keep." The sentence names neither the rule nor the procedure, so the reader must reconstruct both. Proposed: fix: "The arrow said the opposite of the rule it was drawn to show: a CBC Run Reading reads a CBC Run and sends it nothing." Changed.

**FINDING-1056.** (C-34) [changed in round 3] rule 8; checked.
`docs/conventions/visual-comparison/README.md` *What it is for* (line 20): "would have left it out of the set." "The set" appears here before anything says what it is: "The candidate set" is first named in §2.1 (line 64). Line 21 is also a fragment with no subject: "Written as a method the same day, made a convention on 2026-09-19". Proposed: fix: "A method named for diagrams would have left the table out of the candidates. The method was written the same day, and made a convention on 2026-09-19 (ADR-0031)." Mixed: line 20 changed, 21 unchanged.

**FINDING-1057.** (C-35) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/visual-comparison/README.md` §2.4, *The buildable notations* (lines 82-83): "Plain text, rendering on GitHub and in the IDE with no build step, leaves Mermaid and Unicode box drawing." The constraint is the subject of a clause with an aside inside it. It also comes after "the constraint is not aesthetic", which names the constraint before saying it (rule 1). Proposed: fix: "The buildable notations are two. The constraint is plain text that renders on GitHub and in the IDE with no build step, and only Mermaid and Unicode box drawing meet it." Mixed: line 82 changed, 83 unchanged.

**FINDING-1058.** (C-36) [not changed in round 3] rule 7; uncertain.
`docs/conventions/visual-comparison/README.md` §2.4, *The buildable notations* (lines 85-86): "A diagram nobody can read in review is as opaque in a diff as a binary file." This repeats the clause before it: "a committed SVG renders but is not text anyone can read in a diff". Proposed: fix: cut the last sentence; or decline, if the reviewer wants the point said as a rule. Mixed: line 86 changed, 85 unchanged.

**FINDING-1059.** (C-37) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/visual-comparison/README.md` §1, *What a comparison is* (line 45): "The unit is the thing being shown." The reader cannot tell what "the unit" is a unit of. Proposed: fix: "One comparison is made for each thing being shown." Unchanged.

##### `docs/conventions/writing/README.md`

**FINDING-1060.** (C-38) [not changed in round 3] rule 9; checked.
`docs/conventions/writing/README.md` *What it is for* (line 20): "CBC Run 3 wrote a one-page rule". Here, and in "the rule" at lines 22, 66, 70, 73 and 180, the lowercase word means an Agent Rule: CBC Run 3's, then the writing Agent Rule. Line 46 writes the Name ("the Agent Rule states"). That makes 6 uses in this file. Also `docs/conventions/visual-comparison/README.md` 93 ("a rule could load on", a Paths Rule): 1 more. Proposed: fix: "a one-page Agent Rule", "under the Agent Rule", "The Agent Rule applies", "the Agent Rule says outright", "The Agent Rule then names", "why the Agent Rule stays one page"; visual-comparison, "a Paths Rule". Unchanged.

**FINDING-1061.** (C-39) [not changed in round 3] rule 9; checked.
`docs/conventions/writing/README.md` *Why it arrives this way* (line 171): "**A `paths:` list** loads when a file is touched". The glossary names this kind a Paths Rule (`docs/glossary.md`, Agent Rule entry), and FINDING-581 fixed "a `paths:` rule" in `TODO.md` to that Name. A list does not load; the Agent Rule does. The bullet also chains three ideas with commas and "and" (rule 2). Proposed: fix: "**A Paths Rule** loads when a file is touched, after a new one's first draft is written. Chat has no path." Unchanged.

**FINDING-1062.** (C-40) [not changed in round 3] rule 6; checked.
`docs/conventions/writing/README.md` *What it is for* (line 21): "(its RETRO.md, D2)". The retrospective manual now writes the file as "`RETRO.md`" (FINDING-448), so the same reference is written two ways across manuals. Also line 75: 1 more ("(its RETRO.md, D14)"). Proposed: fix: "(its `RETRO.md`, D2)" and "(its `RETRO.md`, D14)". Unchanged.

**FINDING-1063.** (C-41) [changed in round 3] rule 8; resting on the reader.
`docs/conventions/writing/README.md` *The seats* (lines 53-55): "The Concept Deliverer writes under its own: its chat and records. It also covers what CBC Runs read". "It" changes referent, from the Concept Deliverer to its Agent Rule, with no noun to show the change. Proposed: fix: "Its Agent Rule also covers what CBC Runs read". Changed.

**FINDING-1064.** (C-42) [not changed in round 3] rule 2; checked.
`docs/conventions/writing/README.md` §2, rule 9 (lines 131-133): "Its Name goes into the glossary in the commit that first uses it, pointing at the home that defines it, and a word whose English meaning is ours has no Name (rule 6)." Two rules are joined by "and": when a Name is added, and when a word gets no Name. Proposed: fix: end at "defines it.", then "A word whose English meaning is ours has no Name (rule 6)." Unchanged.

**FINDING-1065.** (C-43) [changed in round 3] rule 2; resting on the reader.
`docs/conventions/writing/README.md` §2, rule 9 (line 119): "A count, so a script can find it." This is a fragment with no verb, and the reader must supply "the trigger is". Proposed: fix: "The trigger is a count, so a script can find it." Changed.

**FINDING-1066.** (C-44) [not changed in round 3] rule 2; checked.
`docs/conventions/writing/README.md` §2, rule 11 (lines 153-155): "Markdown has no line width here: a reader meets the text rendered, or in an editor that wraps, and 985 lines in 83 of the 99 living files already run past 72." Three ideas are chained with a colon and "and": the rule, why, and a count. Proposed: fix: "Markdown has no line width here. A reader meets the text rendered, or in an editor that wraps. 985 lines in 83 of the 99 living files already run past 72." Unchanged.

**FINDING-1067.** (C-45) [not changed in round 3] rule 8; resting on the reader.
`docs/conventions/writing/README.md` §1, *What it governs* (lines 74-75): "CBC Run 3 left a specification style for its claims to be judged on plain text first". "Left" can mean dropped or deferred, and "for its claims to be judged" reads as if the claims are being judged. Proposed: fix: "CBC Run 3 put off a specification style until its claims had been judged in plain text (its `RETRO.md`, D14)." Unchanged.

**FINDING-1068.** (C-46) [changed in round 3] rule 3; uncertain.
`docs/conventions/writing/README.md` *What this is made usable as* (lines 35-39): "`delivery/container/docs/glossary/container.md`, the shared Names; `delivery/method/docs/glossary/method.md`, the concept's and the method's; `delivery/spring-postgres/docs/glossary/stack.md`, the stack's." Three files are chained with semicolons inside one bullet. Proposed: fix: a sub-list of three; or decline, since the form keeps one bullet per entry. Changed.

**FINDING-1069.** (C-47) [not changed in round 3] rule 7; uncertain.
`docs/conventions/writing/README.md` §1, *What it governs* (line 62): "How a text reads, never what it says." This repeats the opening statement at line 3 word for word. Proposed: fix: cut, and begin §1 at "It covers every text written"; or decline if the reviewer wants §1 to stand alone in a Fact Reference. Unchanged.

##### `docs/glossary.md`

**FINDING-1070.** (C-48) [not changed in round 3] rule 9; checked.
`docs/glossary.md` *Kinds of text*, Agent Rule entry (line 167): "Rule, the entry file's". Entry File is a Glossary Name (DECISION-23), with an entry ten lines above, and the Fact Reference on the next line writes it capitalized. Proposed: fix: "a Local Rule, the Entry File's". Unchanged.

**FINDING-1071.** (C-49) [not changed in round 3] rule 9; checked.
`docs/glossary.md` *How texts tie*, Foundation Line entry (line 220): "A skill, an Agent Rule, an Output". Agent Skill is a Name, written with its kind every time (DECISION-27, and the glossary's own Agent Skill entry). Proposed: fix: "An Agent Skill, an Agent Rule, an Output Shape". Unchanged.

**FINDING-1072.** (C-50) [not changed in round 3] rule 9; uncertain.
`docs/glossary.md` *Between them*, Pure Seed entry (line 92): "the procedure that gives a CBC Run its birth from". CBC Run Birth is a Name, two entries above, and this lowercase "birth" names the same event, which DECISION-23's test counts as a clash with a Name already held. DECISION-26 keeps "born" as English. Also `docs/glossary.md` 43, `docs/conventions/repo-hygiene/README.md` 40 and 88, `docs/conventions/writing/README.md` 52, `docs/conventions/shapes/README.md` 175, 206 (a title) and 231 (the Mermaid label): 7 more. Proposed: question: is "birth" English, like "born", or the Name? If the Name: "the procedure that makes a CBC Run Birth from this repo alone"; repo-hygiene 88, "The next CBC Run Birth starts corrected"; the idioms "from birth" and "at birth" kept as English. Mixed: glossary 92 unchanged, 43 changed; repo-hygiene 40 unchanged, 88 changed; writing 52 unchanged; shapes 206 changed, 175 and 231 unchanged.

**FINDING-1073.** (C-51) [changed in round 3] rule 3; checked.
`docs/glossary.md` header comment (lines 12-14): "A convention is named by its path in backticks, with its kind word, the exchange manual, or by its Name, the Exchange Convention; never by the bare word." The ways are separated only by commas, and the reader cannot count them: is "with its kind word" a second way, or a condition on the path? The example "the exchange manual" has no backticks, so it reads as a way of its own. Proposed: fix: "A convention is named in one of three ways: by its path in backticks; by its word with its kind word, the exchange manual; or by its Name, the Exchange Convention. Never by the bare word." Changed.

**FINDING-1074.** (C-52) [not changed in round 3] rule 6; uncertain.
`docs/glossary.md` *Kinds of text*, Agent Rule entry (lines 166-168): "a Local Rule, the entry file's (…); a Paths Rule, one loaded by path". Local Rule and Paths Rule are capitalized as Names, and `TODO.md` uses both (lines 176, 601 and 745). Neither has an entry of its own, and the header says "One entry per Name". Proposed: fix: two entries after Agent Rule, each pointing at its home (agent-arrangement §2.4 and §5.6); or a question for the reviewer: are they labels inside the Agent Rule entry? Mixed: lines 166-167 unchanged, 168 changed.

**FINDING-1075.** (C-53) [not changed in round 3] rule 9; uncertain.
`docs/glossary.md` *Kinds of text*, Record Stub entry (line 183): "it: the Plan Stub, the Decisions Log Stub". These two Names are built on Record Stub and Decisions Log but drop "Record", so they do not carry the Name whole (writing rule 9, ADR-0078). No living text uses either. Proposed: fix: drop the two examples ("each named by its record"); or "the Plan Record Stub, the Decisions Log Record Stub", the second at 4 words. Unchanged.

**FINDING-1076.** (C-54) [not changed in round 3] rule 2; resting on the reader.
`docs/glossary.md` *How texts tie*, Chain Link entry (lines 216-217): "Wider than a Fact Reference, which is what one kind of link, points, writes down." The verb "writes down" comes after a nested aside, and "points" stands as a noun between commas. "Link" is also lowercase for the Name. Proposed: fix: "A Fact Reference is narrower: it writes down one kind of Chain Link, points." Unchanged.

**FINDING-1077.** (C-55) [not changed in round 3] rule 8; resting on the reader.
`docs/glossary.md` *Kinds of text*, Output Form entry (lines 146-148): "A particular one is named by its owner: a record's form sits in the record itself, its header comment, the Plan Step Form, a Record Stub's headings." The colon promises names, but the text after it lists where forms sit. Only "the Plan Step Form" is a name. Proposed: fix: "A particular one is named by its owner: the Plan Step Form. A record's Output Form sits in the record itself: its header comment, or a Record Stub's headings." Mixed: lines 146-147 unchanged, 148 changed.

**FINDING-1078.** (C-56) [changed in round 3] rule 8; resting on the reader.
`docs/glossary.md` *Between them*, Delivery Pin entry (lines 57-58): "but for their *Decisions* footers; the other number". "The other number" only makes sense to a reader who has just read the entry above. A glossary entry is often read alone. Proposed: fix: "the second of the two numbers a CBC Run records for a delivery, beside the Read-Through Commit". Mixed: line 57 changed, 58 unchanged.

**FINDING-1079.** (C-57) [not changed in round 3] rule 2; resting on the reader.
`docs/glossary.md` *Kinds of text*, Canonical Description entry (lines 116-118): "Canonical says reference, never correctness: today's understanding, changed only for a reason recorded." "Canonical says reference" is compressed, and the reader must expand it to "the word canonical means it is the reference". Proposed: fix: "\"Canonical\" means the reference, not that it is correct. It is today's understanding, changed only for a reason that is recorded." Unchanged.

**FINDING-1080.** (C-58) [not changed in round 3] rule 5; uncertain.
`docs/glossary.md` *Kinds of text*, Idea Model entry (lines 120-121): "its rules varying by repo, like an interface." This is a comparison the reader has to translate. Proposed: fix: "its rules varying by repo, each repo writing its own Convention Manual for it"; or decline as a plain technical comparison. Unchanged.

##### Across the manuals

**FINDING-1081.** (C-59) [not changed in round 3] rule 9; uncertain.
`docs/conventions/writing/README.md` *What this is made usable as* (line 47): "A change here walks it". The verb stands for running the Change Walk, a Name, on the list. The same sentence ends every manual's list: `docs/conventions/repo-hygiene/README.md` 35, `docs/conventions/retrospective/README.md` 40, `docs/conventions/shapes/README.md` 38 and `docs/conventions/visual-comparison/README.md` 34: 4 more in these files. The form sets it: "It ends with the sentence that a change here walks that list" (`docs/conventions/conventions/` §2.3, *The list of what derives*). Proposed: question: decline as the form's fixed sentence, or change the form and every manual to "A change here runs the Change Walk on it". Unchanged.

#### Reader D, Layer 3: the Idea Models and the concept

##### `docs/models/agent.md`

**FINDING-1082.** (D-1) [not changed in round 3] rule 10; checked. `docs/models/agent.md` *§3* (line 45): "## 3. The components, drawn". A comma gloss in a numbered title counts (DECISION-20). It is the same kind as *One cycle, drawn*, which DECISION-20 fixed, and was missed. "The components" alone would repeat §2's subject. No Fact Reference names the title outside `temp/` and the devlog. Proposed: fix: "## 3. A drawing of the components" (27 characters). unchanged.

**FINDING-1083.** (D-2) [not changed in round 3] rule 10; checked. `docs/models/tiers.md` *§1* (line 17): "## 1. The tiers, drawn". The same comma gloss as FINDING-1082. "The tiers" alone would repeat §2's title. No Fact Reference names it outside `temp/` and the devlog. Proposed: fix: "## 1. A drawing of the tiers". unchanged.

**FINDING-1084.** (D-3) [changed in round 3] rule 10; uncertain. `docs/models/agent.md` *§12.1* (line 286): "### 12.1 On the Ambient Channel". Read alone in a Fact Reference, the title loses its parent, *Claims*. The same applies to §12.2 to §12.8 (*On the Pulled Channel* to *On the Enforcement Gate*) and §12.9 *Scorecard*. Also §2 *Components* (line 37) and §11 *Out of scope* (line 259): neither says of what. 10 more. Proposed: question: does "standing alone" reach a child title that leans on its parent? If yes: "Claims on the Ambient Channel" (29) and so on, "The claims' scorecard", "The agent's components", "What the model leaves out", with the rename grep. changed (§12.1 to §12.4, §12.8 titles); unchanged (the rest).

**FINDING-1085.** (D-4) [changed in round 3] rule 5; resting on the reader. `docs/models/agent.md` *§4.1, Ambient Channel* (lines 95-96): "the Told Channel's diagnostic below, parked rather than fixed". "Parked" is the "debt, bank, park" figure DECISION-26 fixes. The sentence also points "below" with no section. Line 88-89, "An operator's standing file", is not said in plain words either (rule 8). Proposed: fix: "An operator's own file, loaded only in their checkout:" at 88-89; and "Using it again and again for a rule true in any project is the Told Channel's diagnostic (§4.4, *Told Channel*): the missing convention is worked around, not written." changed.

**FINDING-1086.** (D-5) [not changed in round 3] rule 9; checked. `docs/models/agent.md` *§4.6, Installed Channel* (line 152): "only what applies at bootstrap can be delivered this way". "Bootstrap" has a rival among the delivered Names, CBC Bootstrap (`stack.md`); DECISION-19 fixes a word with a rival. The line is also labelled **Costs:** but states a limit, not a cost (rule 3). Proposed: fix: "**Limits:** only what holds from a project's first commit can be delivered this way." unchanged.

**FINDING-1087.** (D-6) [not changed in round 3] rule 2; resting on the reader. `docs/models/agent.md` *§4.6, Installed Channel* (lines 150-151): "the outcome, not the behaviour — the agent does not comply with `.gitignore`, it simply cannot see what git hides." A dash and a comma splice join three ideas. Also 160-162, "`.gitignore` is self-enforcing by mechanism; a Record Stub with its rules in comments is self-enforcing by placement", two parts joined by a semicolon; 163-164, "a record's format travels this way, its timing cannot", a comma splice, with "travels" from DECISION-26's journey row: 2 more. Proposed: fix: "the outcome, not the behaviour. The agent does not comply with `.gitignore`. It cannot see what git hides."; at 160-162, two sentences; at 163-164, "A record's format can be delivered this way. Its timing cannot." unchanged.

**FINDING-1088.** (D-7) [changed in round 3] rule 9; checked. `docs/models/agent.md` *§7, The Enforcement Gate* (line 211): "the Ambient, Pulled or Pushed Channel changes the odds". Two Names are cut to their first word. A Name is written exactly, and line 184 writes them whole. Proposed: fix: "the Ambient Channel, the Pulled Channel or the Pushed Channel changes the odds". changed.

**FINDING-1089.** (D-8) [changed in round 3] rule 1; resting on the reader. `docs/models/agent.md` *§9, Where each convention lands* (line 234): "Shown by each convention's Work Approaches". The section opens on a sentence with no subject, so its point never gets said. Line 236's "the choosing table" is a label the reader has not met (rule 8). Proposed: fix: "Each convention's Work Approaches show where it lands: an Agent Skill for a rule bound to a moment, Record Stubs and Agent Skill Templates for a rule carried in the files a project is born with. The choice rests on the table in §8 (§8, *Choosing a channel*)." changed.

**FINDING-1090.** (D-9) [changed in round 3] rule 2; checked. `docs/models/agent.md` *§10, The Tool Bindings* (line 244): "Layer 1 names capabilities; a Tool Binding names the mechanisms one tool gives each of them: which file…". A semicolon and a colon list hold three ideas. Proposed: fix: "Layer 1 names capabilities. A Tool Binding names the mechanisms one tool gives each of them: which file the Ambient Channel loads, what the Pushed Channel carries, what an Enforcement Gate checks." changed.

**FINDING-1091.** (D-10) [not changed in round 3] rule 8; resting on the reader. `docs/models/agent.md` *§12, Claims* (lines 277-279): "the handbook's history, this repo's, or a CBC Run's. The handbook is the repo that held the working arrangement before this one". The handbook is used first and said one sentence later. Proposed: fix: "Each piece of evidence says where it was seen: this repo's history, a CBC Run's, or the handbook's. The handbook is the repo…", or put the gloss at first use. changed.

**FINDING-1092.** (D-11) [changed in round 3] rule 2; checked. `docs/models/agent.md` *§12.1, A1* (lines 296-298): "In this repo the commit-messages Agent Skill is opened at every commit. So did seven of the eight revisions". "So did" points back to "run over 50 characters" across a sentence about something else, so it reads as "so did [open the Agent Skill]". At 299, "at every Plan Step read" does not say who read. At 300, "(devlog, 2026-09-10 to 09-14)" does not say whose devlog (rule 6). Proposed: fix: "125 of this repo's 233 commits from 2026-09-20 to 09-29 run over 50 characters, though the commit-messages Agent Skill is opened at every commit here. Seven of the eight revisions of commit plans of 2026-09-29 ran over too, the longest at 67."; question: whose devlog, and "at every Plan Step we read". changed.

**FINDING-1093.** (D-12) [changed in round 3] rule 8; resting on the reader. `docs/models/agent.md` *§12.1, A1* (line 301): "**Open question it raises:** unenforced, or mis-set." Two bare adjectives stand for a question the reader has to rebuild. Proposed: fix: "**Open question it raises:** is the limit only unenforced, or set wrong?" changed.

**FINDING-1094.** (D-13) [not changed in round 3] rule 2; resting on the reader. `docs/models/agent.md` *§12.2, P2* (line 336): "`measured` elsewhere, against it, though not on P2 itself —". "Against it" and "not on P2 itself" pull two ways in one lead. At 341-342, "One framework, the vendor's own suite." is a fragment whose point (a weak source) is left unsaid. At 344, "30 points" does not say percentage points: 2 more. Proposed: fix: "`measured` elsewhere, on a nearby question, not P2 itself:"; "Both numbers come from one framework, tested by its vendor's own suite."; "30 percentage points". changed (338-341); unchanged (336-337, 342-344).

**FINDING-1095.** (D-14) [changed in round 3] rule 8; resting on the reader. `docs/models/agent.md` *§12.4, O1* (lines 369-370): "the handbook's three-place hygiene update (its devlog, k)". "k" is an entry label in the handbook's devlog that the reader does not hold, and "three-place hygiene update" packs a sentence into a noun. Also 360-361, "it had kept a member since 2026-09-18", for "it still held a file": 1 more. Proposed: fix: "Earlier, a hygiene change the handbook needed in three places was caught by hand (the handbook's devlog, entry k)."; "and it still held one file, added 2026-09-18". changed.

**FINDING-1096.** (D-15) [not changed in round 3] rule 3; checked. `docs/models/agent.md` *§12.5, W2* (lines 387-392): "a stop … skipped on an instruction the prompt never gave; a checkout opened because…". Two incidents are chained with a semicolon in one item. O1 above gives its three as sub-items. Proposed: fix: two sub-items, one per incident. changed.

**FINDING-1097.** (D-16) [not changed in round 3] rule 2; checked. `docs/models/agent.md` *§12.8, G1* (lines 422-424): "The rule existed in two channels for the whole life of the handbook, no Enforcement Gate existed, and it was broken 15 times." Commas chain three ideas. Proposed: fix: "The rule existed in two channels for the whole life of the handbook. No Enforcement Gate existed. It was broken 15 times." changed.

**FINDING-1098.** (D-17) [changed in round 3] rule 7; resting on the reader. `docs/models/agent.md` *§12.9, Scorecard* (line 440): "Note that the Installed Channel carries no claims." "Note that" adds nothing, and line 154 already says the Installed Channel is "immune to every claim". Proposed: fix: "The Installed Channel carries no claims." changed.

**FINDING-1099.** (D-18) [changed in round 3] rule 2; resting on the reader. `docs/models/agent.md` *§5, The context window* (lines 184-186): "So a rule that rests on a fact of the session — a reviewer is present, a repo is out of bounds — cannot live in a file alone: the file cannot know the session, and the prompt outranks it." Examples in dashes and two reasons after a colon make one sentence of four ideas. Also 97-98, "what must never happen — if it is short.", a condition hung on a list after a dash: 1 more. Proposed: fix: "So a rule that rests on a fact of the session cannot live in a file alone. Such a fact is, for example, that a reviewer is present, or a repo is out of bounds. The file cannot know the session, and the prompt outranks it."; at 97-98, "**Suits:** orientation and routing, kept short: where to look, what kind of repo this is, what must never happen." changed (184); unchanged (185-186, 97-98).

##### `docs/models/idea-to-output.md`

**FINDING-1100.** (D-19) [changed in round 3] rule 8; resting on the reader. `docs/models/idea-to-output.md` *opening* (lines 9-10): "written from one full chain, the agent's, and checked against the concept's and a record's." The reader cannot tell yet which chain "the agent's" is, or which record. Also 187 "The agent's is the worked example.": 1 more. Proposed: fix: "written from one full chain, the Agent Model's (§7, *One chain here*), and checked against the concept's and one record's"; at 187, "The Agent Model's chain is the worked example." changed (9-10); unchanged (187).

**FINDING-1101.** (D-20) [not changed in round 3] rule 9; checked. `docs/models/idea-to-output.md` *§2, The kinds* (line 36): "`docs/models/`: agent, tiers, this one". A particular Idea Model is named by its name (`docs/glossary.md`, *Idea Model*), and the lowercase words are neither its name nor its paths. Proposed: fix: "`docs/models/`: the Agent Model, the Tiers Model, this one". unchanged.

**FINDING-1102.** (D-21) [not changed in round 3] rule 8; resting on the reader. `docs/models/idea-to-output.md` *§3.2, The direction of a link* (line 74): "A reference down is placed upward." It reads as a riddle until the next sentence explains it. Also 69-70, "Sideways is a fact whose home sits beside the line.", a direction used as a subject: 1 more. Proposed: fix: "A link that would point down is fixed by moving its idea up."; "A sideways link points at a fact whose home is at the line's own level." unchanged.

**FINDING-1103.** (D-22) [changed in round 3] rule 8; checked. `docs/models/idea-to-output.md` *§4.2, The upward direction* (lines 111-112): "The Idea Models before this one came from the handbook, the repo that held the working arrangement before this one". One sentence uses "this one" twice for two things: this Idea Model and this repo. Proposed: fix: "The earlier Idea Models came from the handbook, the repo that held the working arrangement before this repo, now history (ADR-0038)." changed.

**FINDING-1104.** (D-23) [not changed in round 3] rule 9; uncertain. `docs/models/idea-to-output.md` *§4.3* (line 124): "### 4.3 After a birth". "Birth" has a rival among our Names, CBC Run Birth. Read alone in a reference (rule 10), the title says a CBC Run's birth, but it means a text written one level up. Also 129, "Birth goes up": 1 more. Proposed: fix: "### 4.3 After the step up" (line 118's own words), and "A new text is written up; afterwards, reliance goes up too."; rename grep (no Fact Reference names it today). unchanged.

**FINDING-1105.** (D-24) [not changed in round 3] rule 5; resting on the reader. `docs/models/idea-to-output.md` *§5, An Idea Model and a concept* (lines 138-139): "only from a mistake lived, and the edit goes home." "Goes home" is a figure for "is sent to the Concept Deliverer", and "a mistake lived" turns the plain order around. Also 179 "only from a mistake lived": 1 more. Proposed: fix: "A CBC Run edits its copy only after a mistake it met, and the Concept Deliverer reads the edit."; the same words at 179. unchanged (139); changed (179).

**FINDING-1106.** (D-25) [not changed in round 3] rule 8; resting on the reader. `docs/models/idea-to-output.md` *§5* (lines 141-142): "What a concept is waits for a second Concept Repo." What waits is an Idea Model of concepts. The sentence leaves the reader to supply that. Proposed: fix: "An Idea Model of what a concept is waits for a second Concept Repo." unchanged.

**FINDING-1107.** (D-26) [not changed in round 3] rule 8; resting on the reader. `docs/models/idea-to-output.md` *§6.2, What a convention asserts* (lines 162-164): "That freedom is the worker's, in one case". "In one case" does not say it means each departure is decided one case at a time. At 167-168, "That convention is one nobody owes anything to: a method filed in the wrong place" leaves the reader to work out why no harm makes it a method: 1 more. Proposed: question: say each in plain words, e.g. "The worker may use that freedom one case at a time, and writes the reason in that project's records." unchanged.

**FINDING-1108.** (D-27) [changed in round 3] rule 8; checked. `docs/models/idea-to-output.md` *§7, One chain here* (lines 190-191): "Their content is the output." "Their" could be the guard and the header, or the two files. The output is the files' entries. Proposed: fix: "What the Entry File and the Decisions Log hold is the output." changed.

**FINDING-1109.** (D-28) [not changed in round 3] rule 8; resting on the reader. `docs/models/idea-to-output.md` *§8, What it does not answer* (lines 199-200): "this repo's conventions, not this Idea Model". The other two items each name a path; this one does not say which convention. Proposed: fix: "— `docs/conventions/facts-in-sync/`, not this Idea Model." unchanged.

##### `docs/models/tiers.md`

**FINDING-1110.** (D-29) [not changed in round 3] rule 9; checked. `docs/models/tiers.md` *§1* (lines 23-24): "mental layer," and "container and execution copies". The drawing names a Concept Repo's two layers by words §2.2 does not use: there they are its Canonical Descriptions and what is made usable. Rule 9 reaches drawn text (DECISION-21). Also 20, "conventions, container, models", for the Container Group and the Idea Models: 1 more. Proposed: fix: the Names where the box has room, "Canonical Descriptions," and "Container Group and made-usable copies"; or one key line above the drawing. unchanged (20, 23); changed (24).

**FINDING-1111.** (D-30) [changed in round 3] rule 8; resting on the reader. `docs/models/tiers.md` *§2.1, The empty top tier* (lines 34-35): "A second repo that needs it copies parts." "A second repo" means a second Concept Repo, and the reader has to guess. At 36-37, "the upward channels" uses "channel" for a flow, in the file that uses the Told Channel: 1 more. Proposed: fix: "A second Concept Repo that needs the method copies parts."; "the upward flows". changed (34-36); unchanged (37).

**FINDING-1112.** (D-31) [changed in round 3] rule 9; checked. `docs/models/tiers.md` *§2.2, Concept Repos* (line 53): "2. What is Made Usable from them:". "Made usable" as the verb is lowercase. Made Usable is capitalized only as the noun (the round's call at FINDING-525), and line 68 writes "made usable". Also 108-109 "what is Made Usable is re-derived": 1 more. Proposed: fix: "What is made usable from them:" and "what is made usable is re-derived". changed.

**FINDING-1113.** (D-32) [changed in round 3] rule 8; resting on the reader. `docs/models/tiers.md` *§2.2* (lines 56-57): "Run Repos never happen here." A repo does not happen. The point is that no Run Repo's work is done in a Concept Repo. Proposed: fix: "No Run Repo's work is done here." unchanged.

**FINDING-1114.** (D-33) [not changed in round 3] rule 3; resting on the reader. `docs/models/tiers.md` *§3.1, Downward delivery* (lines 81-82): "Down is delivery, in two forms. A copy, always pinned at a commit of the tier above, which is what "a concept version" is. And a Delivery Fill:". The two forms are told in a fragment and an "And" sentence. Proposed: fix: a list of two, "1. A copy, always pinned at a commit of the tier above: that pin is what "a concept version" is. 2. A Delivery Fill: …". unchanged.

**FINDING-1115.** (D-34) [changed in round 3] rule 9; checked. `docs/models/tiers.md` *§3.1* (lines 84-85): "it is folded back by name into the playbook that seeded it." "Fold" has a rival among the delivered Names, Invariant Slice Fold. Proposed: fix: "it is merged back by name into the playbook it came from." changed.

**FINDING-1116.** (D-35) [changed in round 3] rule 9; checked. `docs/models/tiers.md` *§3.1* (line 89): "At a Run Birth the two meet." Run Birth is no longer a Name. It became CBC Run Birth (DECISION-19, the Agent Model's group, row 22), and this model speaks of any Run Repo. In the same sentence, "framing" has a rival in CBC Framing, and "neither is a settled agreement" still does not say what agreement would be (rule 8). Proposed: fix: "At a Run Repo's birth the two meet. Both are input to the Run Repo's first decisions, which choose what to keep of them. Neither binds it." changed.

**FINDING-1117.** (D-36) [changed in round 3] rule 7; checked. `docs/models/tiers.md` *§3.2, The Told Channel* (lines 97-99): "That is the Told Channel, unpinned by design" and "It is not a third form of delivery". Both repeat line 95, "The Told Channel is not delivery." At 101, "Nor is a copy the Run Repo has edited" points back past them to "a third form of delivery". At 97, "as an experiment's instrument" is not said in plain words (rule 8). Proposed: fix: "The Told Channel is not delivery, and is unpinned by design (`docs/models/agent.md` §4.4, *Told Channel*). A tier above may hand a Run Repo a warning as session input, after the Run Repo's own work has missed it and is on record. The Run Repo's records say it was told. A Run Repo that leans on it has the Told Channel's diagnostic. A copy the Run Repo has edited between two Delivery Pins is not a form of delivery either (§3.5, …, fact 4)." changed.

**FINDING-1118.** (D-37) [not changed in round 3] rule 2; resting on the reader. `docs/models/tiers.md` *§3.3, Upward harvest* (lines 110-111): "Nothing edits an upstream repo as a side effect of downstream work, in either direction." The sentence names one direction, then says "either". Proposed: fix: "Work in one repo never edits another as a side effect, up or down." unchanged.

**FINDING-1119.** (D-38) [changed in round 3] rule 5; resting on the reader. `docs/models/tiers.md` *§3.4* (line 115): "The Delivery Pin follows the talk, the documents the tiers exchange." "The talk" is a figure for documents, glossed at once. The title at 113 carries it, and 128 cites the title. Proposed: fix: "### 3.4 The Delivery Pin and documents"; "The Delivery Pin follows the documents the tiers exchange."; rename grep: one reference, line 128. unchanged (113); changed (115).

**FINDING-1120.** (D-39) [changed in round 3] rule 4; resting on the reader. `docs/models/tiers.md` *§3.4* (line 119): "That happened once, and it is why the Delivery Pin moves with every Delivery Take". It does not say where or when. Proposed: question: name the CBC Run and the date, or the ADR that records it. changed.

**FINDING-1121.** (D-40) [changed in round 3] rule 8; checked. `docs/models/tiers.md` *§3.5, What holds on every flow* (line 140): "And one number, the Delivery Pin: the commit of the tier above that a delivery's copies equal". The Delivery Pin is used at 101 and throughout §3.4 (113-120), and said in plain words only here. Proposed: fix: say it at §3.4's first line, "The Delivery Pin, the commit of the tier above that a delivery's copies equal, follows …", and keep 140 as the fact. changed.

**FINDING-1122.** (D-41) [not changed in round 3] rule 2; resting on the reader. `docs/models/tiers.md` *§4.2, The dependency rule* (lines 160-162): "A repo lives in exactly one tier; a Concept Repo maintaining its own records, and today its method, is the concepts tier's work, and not a Run Repo's." A semicolon joins two ideas, and the subject (a repo) is said to be "work". Proposed: fix: "A repo lives in exactly one tier. A Concept Repo that keeps its own records, and today its method, does the concepts tier's work, not a Run Repo's." changed (162); unchanged (160-161).

##### `concept/00-cbc.md`

**FINDING-1123.** (D-42) [not changed in round 3] rule 3; resting on the reader. `concept/00-cbc.md` *opening* (lines 3-5): "Read this first; the other chapters deepen it — the Layered System, …". A semicolon and a dash join three parts. Proposed: fix: "*The main document. Read this first. The other chapters go deeper: the Layered System, System Guarantees and Structural Walls, CBC Framing, and the Invariant Slice.*" Editorial. unchanged (3); changed (4-5).

**FINDING-1124.** (D-43) [changed in round 3] rule 9; checked. `concept/00-cbc.md` *The CBC Inversion* (line 40): "Guarantee depth is the visible product;". "Guarantee" stands alone for the System Guarantees. A semicolon also joins a second idea (rule 2). Proposed: fix: "The depth of the System Guarantees is the visible product. Staying small is discipline, not taste." Editorial. changed.

**FINDING-1125.** (D-44) [changed in round 3] rule 7; resting on the reader. `concept/00-cbc.md` (line 60): "## The two components and their pair". The two components are the pair, so the title names one thing twice. At 62, "it lives in the pair" says it with a figure. Proposed: fix: "## The two components"; "The discipline has exactly two components, and is defined by the two together:". Editorial. changed.

**FINDING-1126.** (D-45) [changed in round 3] rule 9; uncertain. `concept/00-cbc.md` *Where it comes from* (line 106): "Threat modeling already thinks in never-events first." "Never-event" is not English. The concept defines the System Never-Event, and this lowercase use stands for threat modeling's version of the same idea. Proposed: fix: "Threat modeling already asks first what must never happen." Editorial. changed.

**FINDING-1127.** (D-46) [changed in round 3] rule 6; checked. `concept/00-cbc.md` *Where it comes from* (line 117): "formal methods enforce but don't say where specifications come from." The list at 102-110 names "the academic correctness-by-construction lineage". The second list at 114-117 calls it "formal methods": one practice under two names. The second list also has four items for "five practices" (120), and design-before-code has none. Proposed: fix: "the correctness-by-construction lineage enforces but doesn't say …" (editorial); question: whether design-before-code gets its gap line (not editorial: it adds a claim). changed.

**FINDING-1128.** (D-47) [changed in round 3] rule 2; resting on the reader. `concept/00-cbc.md` *Where it comes from* (lines 119-122): "These are not five practices but five phases of one derivation, with a single organizing question, …, asked at each phase in that phase's vocabulary." One sentence holds three ideas. Proposed: fix: "These are not five practices but five phases of one derivation. One question organizes them: *what must never happen, and what structure makes it impossible*. Each phase asks it in its own vocabulary." Editorial. changed.

**FINDING-1129.** (D-48) [not changed in round 3] rule 6; uncertain. `concept/00-cbc.md` *What it is not* (line 128): "The method earns its cost". The chapter calls itself "the discipline" everywhere else. "The method" is what the concept becomes (`docs/glossary.md`, *Made Usable*). Proposed: fix: "The discipline earns its cost". Editorial. unchanged.

**FINDING-1130.** (D-49) [not changed in round 3] rule 5; checked. `concept/00-cbc.md` *What it is not* (lines 132-133): "Rigor is *spent*, not applied: the budget goes to the few invariants". This is one of FINDING-532's five figures. The round's ending took its "one word each" fix (§2.6), and this one was left. Proposed: fix: "Rigor is chosen, not applied everywhere: it goes to the few invariants". Editorial. unchanged.

**FINDING-1131.** (D-50) [changed in round 3] rule 5; resting on the reader. `concept/00-cbc.md` *How it fails* (lines 145-146): "bypasses the single enforced code path; the System Guarantee quietly becomes fiction." "Becomes fiction" is a figure, and a semicolon joins the two ideas. The method's glossary says it plainly: "a System Guarantee stops being true". Proposed: fix: "An admin path or raw script goes around the single enforced code path. The System Guarantee stops being true, and nobody sees it." Editorial. changed.

**FINDING-1132.** (D-51) [changed in round 3] rule 2; resting on the reader. `concept/00-cbc.md` *How it fails* (lines 149-150): "Attempting deep rigor before the layers have shrunk the problem — over-theorizing a world that hasn't been bounded yet." A fragment and a dash restatement; the other three items are sentences. Proposed: fix: "Deep rigor is tried before the layers have made the problem small. It theorizes about a world not yet bounded." Editorial. changed (149); unchanged (150).

##### `concept/01-layered-system.md`

**FINDING-1133.** (D-52) [not changed in round 3] rule 9; checked. `concept/01-layered-system.md` *drawing* (line 12): "bounded problems inside one area". In the drawing, "area" stands for Responsibility Area, which the Names table took as a Name because the chapters use "area" with its defined meaning. Rule 9 reaches drawn text (DECISION-21). Also 13 "when areas interact", 17 "each area in LAYER-3-AREAS", 18 "between the areas": 3 more. Proposed: fix: the Name where the line has room ("inside one Responsibility Area", "between the Responsibility Areas"); or one key line above the drawing. Editorial. unchanged.

**FINDING-1134.** (D-53) [not changed in round 3] rule 6; uncertain. `concept/01-layered-system.md` *LAYER-2-SYSTEM* (line 38): "## LAYER-2-SYSTEM — The system of interest". The drawing's label is "System of Interest" (10). The heading writes it in another case and with an article. The same at 21, "The environment" for "Environment" (9), and 65, "Local problems" for "Local Problems" (12): 2 more. The layer titles are labels (the concept's Names table, question 1), and a label is written exactly. Not FINDING-537's gloss question. Proposed: fix: the headings' glosses take the drawing's labels as written. Editorial. unchanged.

**FINDING-1135.** (D-54) [not changed in round 3] rule 5; resting on the reader. `concept/01-layered-system.md` *Two readings to keep apart* (line 98): "description can honestly become a monolith". DECISION-26 fixes "honest, honestly". Proposed: fix: "the same layer description can rightly become a monolith or a set of services", or drop the word. Editorial. unchanged.

**FINDING-1136.** (D-55) [not changed in round 3] rule 2; resting on the reader. `concept/01-layered-system.md` *opening* (line 4): "The layering is not administrative — each layer produces the precondition". A dash joins two ideas. Also in this file 45, 49-50, 92; `concept/02-guarantees-and-walls.md` 3-4 (an aside nested in dashes, "documents are packaging", also rule 5), 16-17, 39, 80, 99; `concept/03-cbc-framing.md` 13; `concept/04-cbc-slice.md` 39-40 (an aside nested in dashes); `concept/00-cbc.md` 129: 12 more. Proposed: fix: a full stop for each dash that joins two clauses; a colon or a list for the asides at 02 3-4, 04 39-40 and 00 129. Editorial. unchanged (01 4, 49, 92; 02 3-4; 04 39-40); changed (the rest).

##### `concept/02-guarantees-and-walls.md`

**FINDING-1137.** (D-56) [changed in round 3] rule 5; resting on the reader. `concept/02-guarantees-and-walls.md` *The described adversary* (lines 25-27): "This is the Falsifiable Promise's opponent; without it the System Guarantees below have nothing to be tested against." "Opponent" is a figure, and a semicolon joins the two ideas. Proposed: fix: "It is what the Falsifiable Promise is defended against. Without it, the System Guarantees below have nothing to be tested against." Editorial. changed.

**FINDING-1138.** (D-57) [changed in round 3] rule 5; resting on the reader. `concept/02-guarantees-and-walls.md` *The System Guarantee Inventory* (line 38): "Small is a feature." The idiom uses "feature" in a chapter where a feature is the product's surface, the thing that comes last. Proposed: fix: "Small is the aim." Editorial. changed.

**FINDING-1139.** (D-58) [not changed in round 3] rule 6; checked. `concept/02-guarantees-and-walls.md` *The ownership map* (lines 49-52): "→ type system / → single validated entry path / … / → code review". The list below names the same ranks differently: 61 "a type error", 62 "a single checked entry path", 68 "a single entry path", 65 "review". One rank, two names each. Proposed: fix: one name per rank in both places, e.g. "type system" and "a single checked entry path" throughout. Editorial. unchanged (49-52); changed (61-68).

**FINDING-1140.** (D-59) [changed in round 3] rule 8; checked. `concept/02-guarantees-and-walls.md` *The ownership map* (lines 72-73): "only where the trust names it the only writer". "The trust" is not said anywhere. It means the assumptions accepted as trust (24-25). Proposed: fix: "only where the assumptions accepted as trust name it the only writer". Editorial. changed.

**FINDING-1141.** (D-60) [not changed in round 3] rule 2; resting on the reader. `concept/02-guarantees-and-walls.md` *The derived surface* (line 86): "The feature set — as an *output*." A fragment opens the section. Proposed: fix: "The feature set comes out of the design, as an *output*." Editorial. unchanged.

**FINDING-1142.** (D-61) [changed in round 3] rule 6; uncertain. `concept/02-guarantees-and-walls.md` *The stance underneath* (line 98): "migrating out of the schema and into a test suite". The chapter's top Structural Wall is "the store's refusal" (47). "The schema" names it by one stack's word. Proposed: fix: "moving out of the store's refusal and into a test suite". Editorial. changed.

##### `concept/03-cbc-framing.md`

**FINDING-1143.** (D-62) [changed in round 3] rule 9; checked. `concept/03-cbc-framing.md` *The derivation order* (lines 27-28): "A candidate promise that is really a feature is rejected." The defined thing is written in lowercase, in the paragraph headed **Choose the Falsifiable Promise**. Proposed: fix: "A candidate Falsifiable Promise that is really a feature is rejected." Editorial. changed.

**FINDING-1144.** (D-63) [changed in round 3] rule 8; checked. `concept/03-cbc-framing.md` *The derivation order* (line 29): "the CBC Framing Intent is overloaded". The CBC Framing Intent is used here and said only at 74-75, "the Falsifiable Promise and the purposes refused". Proposed: fix: "the CBC Framing Intent, the document that states the Falsifiable Promise, is overloaded". Editorial. changed.

**FINDING-1145.** (D-64) [changed in round 3] rule 8; checked. `concept/03-cbc-framing.md` *The derivation order* (line 40): "The Enemy Census collects attackable facts, not generalities." Line 44 then uses Enemy Fact, which the chapter never ties to these words. Proposed: fix: "The Enemy Census collects Enemy Facts, attackable facts, not generalities." Editorial. changed.

**FINDING-1146.** (D-65) [changed in round 3] rule 9; checked. `concept/03-cbc-framing.md` *The derivation order* (line 45): "The output names the *Enemy Collision Kill*". No Markdown mark marks a Name. Only bold at its home is allowed (DECISION-22), and this is italics. Proposed: fix: plain "the Enemy Collision Kill", or bold if this line is its home (the method's glossary points here). Editorial. changed.

**FINDING-1147.** (D-66) [not changed in round 3] rule 8; checked. `concept/03-cbc-framing.md` (line 61): "## Why this order and not the map's". "The map" is not said in the chapter. It means the Layered System's outside-in order (22-23), and "the map" was ruled out beside Local Map (DECISION-23). Proposed: fix: "## Why this order and not the layers'". Editorial. unchanged.

**FINDING-1148.** (D-67) [changed in round 3] rule 9; uncertain. `concept/03-cbc-framing.md` *Why this order and not the map's* (line 67): "The two inversions,". The two order changes are called "inversions", beside the CBC Inversion, which is a different thing. Proposed: fix: "The two changes of order,". Editorial. changed.

**FINDING-1149.** (D-68) [changed in round 3] rule 2; resting on the reader. `concept/03-cbc-framing.md` *opening* (lines 7-8): "This chapter describes *what CBC Framing is*; the procedural detail of running it is deliberately left outside the concept." A semicolon joins two ideas. Also `concept/04-cbc-slice.md` 7-9, the same sentence; `concept/03-cbc-framing.md` 38-39, "Follow one request through its whole life; everything beyond the system's control is an actor.": 2 more. Proposed: fix: a full stop for each semicolon. Editorial. changed.

##### `concept/04-cbc-slice.md`

**FINDING-1150.** (D-69) [changed in round 3] rule 8; checked. `concept/04-cbc-slice.md` *Why the invariant is the unit* (line 17): "reproduces the inversion the discipline exists to avoid". The discipline is an inversion (the CBC Inversion). Here "the inversion" names the order it reverses, so the reader meets the word for both. Proposed: fix: "Cutting work by feature brings back the order the discipline exists to reverse: features first, correctness later." Editorial. changed.

**FINDING-1151.** (D-70) [changed in round 3] rule 6; checked. `concept/04-cbc-slice.md` *The four phases* (lines 34-35): "picked from the enforcement hierarchy". Chapter 02 calls the same list "The Structural Walls, ranked strongest to weakest" and "the ranking". This is a third name. Proposed: fix: "picked from the ranking of Structural Walls, the strongest available". Editorial. changed.

#### Reader E, Layer 4: the records and folder forms

##### ARCHITECTURE.md

**FINDING-1152.** (E-1) [not changed in round 3] rule 9; checked. `ARCHITECTURE.md` header comment (line 6): "The Concept Deliverer's map". DECISION-23 took "the map" for `ARCHITECTURE.md` away, since it clashes with Local Map. Also `ARCHITECTURE.md` 233: "record: this map"; `README.md` 63, the records table: "The map: what is here, what ships, and what must stay true". 3 lines. Proposed: fix: "The Concept Deliverer's `ARCHITECTURE.md`"; "record: this page"; "What is here, what ships, and what must stay true". Unchanged.

**FINDING-1153.** (E-2) [not changed in round 3] rule 9; checked. `ARCHITECTURE.md` Overview (line 53): "is the delivery map's". `delivery/README.md` is a Local Map, and line 129 calls it "the delivery's Local Map". DECISION-23 keeps "map" for the Local Map only. Proposed: fix: "is the delivery's Local Map's". Unchanged.

**FINDING-1154.** (E-3) [changed in round 3] rule 9; checked. `ARCHITECTURE.md` §1, *What is stated here* (line 63): "in the delivery that is it *made usable*". FINDING-561's ending made the verb lowercase with no mark, but the italics are still there. The clause is also hard to read (rule 2). Proposed: fix: "Each is made usable as something in the delivery, and this pairing is what this repo is built around." Changed.

**FINDING-1155.** (E-4) [not changed in round 3] rule 7; checked. `ARCHITECTURE.md` §1.1, *The concept* (line 76-77): "Every copy elsewhere, a CBC Run's `docs/concept/`, is a copy." This says that a copy is a copy. Proposed: fix: "**Canonical here.** The concept's one canonical text is here. A CBC Run's `docs/concept/` holds a copy." Changed (the round split the line; the sentence is older).

**FINDING-1156.** (E-5) [changed in round 3] rule 4; checked. `ARCHITECTURE.md` Overview (line 32): "A few rules must hold across all of it". §3's table has 11 rows. Proposed: fix: "Eleven rules must hold across all of it". Changed.

**FINDING-1157.** (E-6) [changed in round 3] rule 9; checked. `ARCHITECTURE.md` §1.3, *The Idea Models* (line 123-124): "names it in its `foundation` line". The Name is Foundation Line, and line 141 writes it that way. Proposed: fix: "names it in its Foundation Line". Changed.

**FINDING-1158.** (E-7) [changed in round 3] rule 9; checked. Agent Skills and Approaches on Trial are named bare, with no kind word. Conventions §1.5, *Naming a Work Approach*, says "In text, a Work Approach is always written with its kind", and DECISION-27 applies this to every name of an agent part. `ARCHITECTURE.md` §2.1 (line 137): "`cbc-framing` and". Line 216 has the right form: "the commit-messages Agent Skill". Also:
- `ARCHITECTURE.md` 145-146, 213, 217, 220, and codemap 249: 6 more.
- `PLAN.md` 73, 90, 140, 150, 168, 170, 185, 208, 229, 267, 294, 349, 358, 367, 402, 407: 16 lines, plus the title parentheses at 213 and 301.
- `TODO.md` 36, 62, 64, 79, 103, 128, 207, 209, 234, 245, 247, 269, 283, 287, 303, 383, 395, 434, 438, 604, 645, 647, 658, 664, 695, 733, 962, 966, 969, 977, 991, 1083, 1094, 1098, 1191, 1206: about 44 lines.
- `CHANGELOG.md` 31, 33, 43, 58: 4 more.

Six of these are the shared names that DECISION-24 says always need the kind word: `commit-plan` (PLAN 213, 229, 301; TODO 79, 269, 303, 383), `retrospective` (TODO 287) and `visual-comparison` (PLAN 349, 402; TODO 395). Proposed: fix: write the kind word, "the cbc-framing and cbc-slice Agent Skills", "the auto-run Approach on Trial". Give a path as a Fact Reference where the line points at where a fact is written. In the codemap, use a one-line key (DECISION-21). Question: the glossary still writes "`cbc-slice`'s Stage 3", in DECISION-25's form. Does that form stand beside DECISION-27? And does a Plan Step title's parenthesis, a list the Plan Step Form defines, count as a labelled list? Mixed: ARCHITECTURE 137, 145, 249 and PLAN 168, 229 changed; ARCHITECTURE 213, 217, 220 and TODO 36, 62, 79 unchanged.

**FINDING-1159.** (E-8) [changed in round 3] rule 5; checked. "travel" is decided as a figure to fix (DECISION-26, journey row). `ARCHITECTURE.md` §2.4's title (line 162): "What does not travel". Also `ARCHITECTURE.md` 131-132 (the Fact Reference to it), 205 "a line that travels with a file", 212 "which travels with every copy"; `TODO.md` 1260 "The rule cannot travel alone". 5 lines. Proposed: fix: §2.4 becomes *What does not ship*; the rename grep finds only line 132. "a line kept in a file"; "which every copy carries"; "The rule cannot be delivered alone". Changed (ARCHITECTURE); TODO 1260 unchanged.

**FINDING-1160.** (E-9) [changed in round 3] rule 9; uncertain. "the stack practice" points at §2.2, *The Stack Group*: `ARCHITECTURE.md` §2 (line 130): "the method, the stack practice and the". Also `ARCHITECTURE.md` 149 "another stack's practice", 250 codemap "the stack practice (§2.2)"; `CHANGELOG.md` 42 "**The stack practice**"; `TODO.md` 1227 "The practice Agent Skills' bodies", 1233 "the practice Agent Skills' trigger descriptions". 6 lines. Proposed: question: is this the Stack Group, so it takes the Name ("the Stack Group", "the Stack Group's Agent Skills")? Or is it English for what one project taught? Mixed: ARCHITECTURE 130 and TODO 1227, 1233 changed; the rest unchanged.

**FINDING-1161.** (E-10) [not changed in round 3] rule 9; checked. `ARCHITECTURE.md` §3, *What must stay true* (line 213): "which stages only from the Master Copies". Line 214 has "a delivery stages only from `delivery/` and `concept/`". The glossary's Delivery Staging entry says the act is "stage a delivery": the verb names its object. Line 214 makes the delivery the actor. Proposed: fix: "which stages a delivery only from the Master Copies"; "a delivery is staged only from `delivery/` and `concept/`". Unchanged.

**FINDING-1162.** (E-11) [not changed in round 3] rule 9; checked. `ARCHITECTURE.md` §3 (line 219): "the CBC Run's `delivered-copies.md`, rule 1". Also line 220. The glossary's Agent Rule entry names a numbered line by its owner and number, "one-home rule 3", and conventions §1.5 asks for the kind word. Proposed: fix: "the CBC Run's delivered-copies rule 1"; "the CBC Run's delivered-copies Agent Rule". Unchanged.

**FINDING-1163.** (E-12) [changed in round 3] rule 8; resting on the reader. `ARCHITECTURE.md` §2 (line 129-133): "The concept's list of what derives from it is the method, the stack practice and the playbook (…). The chapters carry no such list". The concept has a list, and then its chapters carry none. A reader who does not know where the list is kept reads this as a contradiction. Proposed: fix: "What derives from the concept is the method, the Stack Group and the playbook (…). This list is kept here: the chapters carry none (…)." Changed.

**FINDING-1164.** (E-13) [changed in round 3] rule 8; resting on the reader. `ARCHITECTURE.md` §2.5, *The CBC Runs* (line 198-199): "What each side holds for it is the Exchange Convention's *What this is made usable as*." "it" has nothing to point back at, and the heading has no path. Proposed: fix: "What each side holds for the exchange is the Exchange Convention's (`docs/conventions/exchange/`, *What this is made usable as*)." Changed.

**FINDING-1165.** (E-14) [changed in round 3] rule 8; checked. `ARCHITECTURE.md` §1.2 (line 89): "None of it is CbC". This abbreviation is spelled out nowhere in these files. The repo writes "correctness by construction" (`README.md` 3) and "CBC" inside its Names. Also `TODO.md` 255 "names the CbC concept". 2 lines. Proposed: fix: "None of it is about correctness by construction"; "names this repo's concept". ARCHITECTURE 89 changed; TODO 255 unchanged.

**FINDING-1166.** (E-15) [not changed in round 3] rule 5; uncertain. `ARCHITECTURE.md` §3 (line 215): "A manual never outlives the rule it explains". This is a life figure, next to DECISION-26's "dies, death" row. Proposed: fix: "No manual explains a rule that no longer holds". Unchanged.

**FINDING-1167.** (E-16) [not changed in round 3] rule 8; resting on the reader. `ARCHITECTURE.md` §4, *Codemap* (line 254): "deleted when served". Also `temp/README.md` 15: "once it has served". Neither says when that is. 2 lines. Proposed: fix: "deleted once the work that needed it is done". Unchanged.

**FINDING-1168.** (E-17) [not changed in round 3] rule 9; uncertain. `ARCHITECTURE.md` §1.2 (lines 101, 103, 111, 113, 117): "**conventions** —", "**exchange** —", "**retrospective** —", "**shapes** —", "**writing** —". DECISION-24 says a one-word convention is only ever its path or its Name, since the bare word is English. Here each one is a bold list label, with its path after it. 5 lines. Proposed: question: does the folder word stand as a list label? If not, lead each line with its path. Unchanged.

##### README.md

**FINDING-1169.** (E-18) [changed in round 3] rule 9; checked. `README.md` *What it holds* (line 9-10): "Agent Skills, checklists, templates". These templates are Agent Skill Templates, as `CHANGELOG.md` 44 writes them. Proposed: fix: "Agent Skills with their Agent Skill Templates and checklists, and Output Shapes". Changed.

**FINDING-1170.** (E-19) [not changed in round 3] rule 3; checked. `README.md` header comment (line 75-77): "it arrives when a Plan Step's gate makes it true: the README says only what is already true". Two colons are chained. "a Plan Step's gate" is the Plan Step Gate (rule 9). Proposed: fix: "A missing section is not an omission. It arrives when a Plan Step Gate makes it true, since the README says only what is already true." Changed.

**FINDING-1171.** (E-20) [changed in round 3] rule 9; checked. "the records map" is a coined name for project-recording §1's table. The home calls it *The records at a glance*, and PLAN 303 and 343 say "project-recording's list of the records". DECISION-23 keeps "map" for the Local Map. `README.md` *Project records* (line 70): "is the records map". Also `PLAN.md` 349, 383, 401 and `temp/README.md` 18. 5 lines. Proposed: fix: "project-recording's list of the records". README 70 and temp 18 changed; PLAN unchanged.

**FINDING-1172.** (E-21) [changed in round 3] rule 8; resting on the reader. `README.md` *What it holds* (line 15): "**The Concept Deliverer:** each CBC Run is born from what this repo". The label names the Concept Deliverer, but the sentence never says this repo is it. A reader from outside, who is the one the header comment names, learns the word without learning what it means. Proposed: fix: "**The Concept Deliverer:** this repo is the Concept Deliverer. Each CBC Run is born from what it ships, in a repo of its own, and is read back from here." Changed.

**FINDING-1173.** (E-22) [changed in round 3] rule 5; uncertain. `README.md` *Out of scope* (line 52): "Graduating a CBC Run to its own Concept Repo". This is a school figure, and the Tiers Model does not use the word. Proposed: fix: "Moving a CBC Run into a Concept Repo of its own". Changed.

##### PLAN.md

**FINDING-1174.** (E-23) [not changed in round 3] rule 9; checked. Living Text is a Name (DECISION-23). `PLAN.md` Refine's Goal (line 303): "Living text written before a rule". Also:
- `PLAN.md` 337: "across all living text";
- `TODO.md` 371: "hashes in living text";
- `TODO.md` 376: "living text points at a devlog";
- `TODO.md` 906: "Of 97 uses in living text".

Uncertain: the adjective in `PLAN.md` 326, "every living file", and in the Plan Step Form's close item, `PLAN.md` 91, 186, 268, 368, "No living line in a record". Proposed: fix the five to "Living Text". Question for the adjective: "every file of Living Text"; "No line of Living Text in a record…". Unchanged, all.

**FINDING-1175.** (E-24) [not changed in round 3] rule 9; checked. `PLAN.md` the Plan Step Form, *At the opening* (line 63): "This gate was written before the work started." The Name is Plan Step Gate, and the form writes it in full at lines 53-54. Also `PLAN.md` 149, 227, 313. 4 lines. Proposed: fix: "This Plan Step Gate was written before the work started." Unchanged.

**FINDING-1176.** (E-25) [changed in round 3] rule 9; uncertain. `PLAN.md` the Plan Step Form (line 35): "Now: <the stage this Plan Step is in, one line>". The glossary's Agent Skill Stage entry says "A Plan Step's Now line names the Agent Skill Stage it is in". The form writes "stage" in lowercase. Also `PLAN.md` 45, 47, 66, 75-76, 82, 118, 120-121: 8 more. The form's stages also cover "those of earlier work", which has no Name. Proposed: question: if the Now line's stage is the Agent Skill Stage or Approach on Trial Stage, the Names go in. If it is English for any phase, the glossary's sentence changes. Mixed: 35, 47, 76, 120 changed; 45, 82, 118 unchanged.

**FINDING-1177.** (E-26) [changed in round 3] rule 9; checked. `PLAN.md` Step: Birth CBC Run 6 (line 168): "as `auto-run` Stage 4 lists". DECISION-25's form outside the owner is "`auto-run`'s Stage 4". Line 157, "so this is Stage 1's light read", has no owner either. 2 lines. Proposed: fix: "as `auto-run`'s Stage 4 lists" (or FINDING-1158's kind-word form); "so `auto-run`'s Stage 1 is a light read". Changed.

**FINDING-1178.** (E-27) [changed in round 3] rule 6; checked. `PLAN.md` Refine's Now line (line 306): "read again against rules 1 to 10. Layers 1 to 6 worked". "rules" has no owner, and "Layers" is the Name Refinement Layer cut short. Proposed: fix: "read again against writing rules 1 to 10. Refinement Layers 1 to 6 worked". Changed (f5dfbbe).

**FINDING-1179.** (E-28) [changed in round 3] rule 8; resting on the reader. `PLAN.md` Step: Take CBC Run 5's lessons (line 258): "The rule's *Gates* hold when a CBC Run Reading closes". Line 291 has "by the rule's steps 2 to 8". The rule is the working-a-reading Agent Rule, named only by path in the title. 2 lines. Proposed: fix: "The working-a-reading Agent Rule's *Gates*"; "by working-a-reading steps 2 to 8". 258 changed; 291 unchanged.

**FINDING-1180.** (E-29) [not changed in round 3] rule 6; checked. `PLAN.md` Step: Take CBC Run 5's lessons, Notes (line 289): "CBC Run 5's DECISION-1 was taken in talk". DECISION-1 belongs to our CBC Run Reading of CBC Run 5, as line 216 writes it. "CBC Run 5's" makes it the CBC Run's own. Proposed: fix: "The CBC Run Reading's DECISION-1 was taken in talk". Unchanged.

**FINDING-1181.** (E-30) [not changed in round 3] rule 9; uncertain. "birth" as a noun for a CBC Run Birth. `PLAN.md` (line 169): "What TODO says is due before a birth is settled". Also `TODO.md` 62, 69, 73, 431-432, 694, 747: 7 more. "born" stays (DECISION-26), but the noun names the Name's thing. Proposed: question: is "a birth" English, or the CBC Run Birth? Unchanged.

**FINDING-1182.** (E-31) [not changed in round 3] rule 7; resting on the reader. `PLAN.md` Refine's Notes, stage 1 (line 392-395): "The reviewer confirms the Finding Kinds, their Refinement Rounds, the Refinement Layers, …". The list at lines 409-411, "The reviewer signs:", says the same again for the same moment. Proposed: fix: stage 1 keeps the acts, and the reviewer's part stays only in the list at line 409. Unchanged.

**FINDING-1183.** (E-32) [changed in round 3] rule 8; resting on the reader. `PLAN.md` Step: Birth CBC Run 6's Goal (line 138): "reviewer's checkout CBC Run Briefing". "checkout" is CBC Run 6's own name (`ARCHITECTURE.md` §2.5), and it reads as an English word. "full auto" (lines 135, 138, 167, 177) is defined only in `auto-run`. Proposed: fix: "the reviewer's CBC Run Briefing for `checkout`, CBC Run 6's project". Line 138 changed.

**FINDING-1184.** (E-33) [not changed in round 3] rule 8; resting on the reader. `PLAN.md` Legend (line 10): "stopped (+the Plan Step first)". Proposed: fix: "stopped (+the Plan Step that must come first)". Unchanged.

##### TODO.md

**FINDING-1185.** (E-34) [not changed in round 3] rule 9; checked. `TODO.md` Next, "Decide how work is run by agents" (line 133-134): "the kind of work, the Idea Model, the effort". This is FINDING-578, which the endings list as fixed in `e5a874b`. The line is as it was at 00420b9. The agent's model is meant. Proposed: fix: "the model". Unchanged.

**FINDING-1186.** (E-35) [not changed in round 3] rule 9; checked. `TODO.md` Next, "Decide which ideas here are Idea Models" (line 752): "three Idea Models exist: agent, tiers, idea-to-output". Line 795 has "Idea-to-output has an Idea Model come from". This is FINDING-549, listed as fixed, and both TODO lines are unchanged. 2 lines. Proposed: fix: "the Agent Model, the Tiers Model and the Idea-to-Output Model"; "The Idea-to-Output Model has an Idea Model come from". Unchanged.

**FINDING-1187.** (E-36) [not changed in round 3] rule 9; checked. `TODO.md` Later, "Release concept v2" (line 922-923): "the Plan Step that runs run 5's birth closes". This is one of FINDING-580's lines, listed as fixed. Proposed: fix: "CBC Run 5's birth". Unchanged.

**FINDING-1188.** (E-37) [not changed in round 3] rule 6; checked. Fact References to Conversation Memory sections cut short with "…". DECISION-31's reason applies: a Fact Reference carries its title whole. `TODO.md` (line 97): "§9, *A commit plan's look-back…*". Also lines 115, 236, 447, 673, 830, 881: 6 more. Proposed: fix: the whole title, e.g. "§9, *A commit plan's look-back at the way*", "§21, *A full read for missing fact references*". Unchanged.

**FINDING-1189.** (E-38) [not changed in round 3] rule 6; checked. `TODO.md` Later, "Does the playbook need a convention of its own?" (line 1035-1036): "*What a Output Shape is not*". The heading is *What an Output Shape is not* (`docs/conventions/shapes/README.md` line 112). FINDING-586 fixed the same slip at another line. Proposed: fix: "an". Unchanged.

**FINDING-1190.** (E-39) [changed in round 3] rule 9; checked. "rule" written for Agent Rule. `TODO.md` (line 404): "a manual, an Agent Skill or rule". Also 286 "file, rule, Agent Skill, record, or nothing", 467, 480, 506-507, 587, 589, 593-594, 607: 8 more. Proposed: fix: "Agent Rule", "Agent Rules". 404, 506, 587, 589, 607 changed; 286 changed; 467, 480 unchanged.

**FINDING-1191.** (E-40) [not changed in round 3] rule 9; checked. Entry File in lowercase. `TODO.md` (line 285-286): "ends each: entry file, rule, …". Also 743-744: "its entry file now states only what never changes". 2 lines. Proposed: fix: "Entry File". 286 changed; 743-744 unchanged.

**FINDING-1192.** (E-41) [not changed in round 3] rule 9; checked. The method's and the stack's Names written as bare words:
- `TODO.md` "Watch whether the next Newborn CBC Run…" (line 743-745): "answered the bootstrap half", "At establish it", for CBC Bootstrap and Infrastructure Establishment;
- `TODO.md` 977: "`infra-establish`'s contract", for the Infrastructure Contract;
- `TODO.md` 648: "readiness (600)", for System Readiness;
- `CHANGELOG.md` 37-38: "the registry template or readiness checklist", for the Agent Skill Template `templates/registry.md` and System Readiness's checklist.

5 lines. Proposed: fix: the Names. CHANGELOG 37-38 and TODO 647 changed; the rest unchanged.

**FINDING-1193.** (E-42) [not changed in round 3] rule 9; checked. The refinement's Names in lowercase:
- `TODO.md` (line 383): "its rounds read";
- `TODO.md` 807: "Only the refinement's rounds read";
- `TODO.md` 565: "text round 3 rewrites";
- `TODO.md` 504-505: "a refinement's writing kind", where line 669 writes "Its Writing Finding Kind".

4 lines. Proposed: fix: "its Refinement Rounds"; "Refinement Round 3"; "a refinement's Writing Finding Kind". 565 changed; 383, 504, 807 unchanged.

**FINDING-1194.** (E-43) [changed in round 3] rule 6; checked. `TODO.md` "Rename the manuals…" (line 529-530): "(the refinement's DECISION-24 and 27)". This is FINDING-584's fault: a bare number after the first label. Also line 877, "rule 9's question at the commit", has no owner. 2 lines. Proposed: fix: "DECISION-24 and DECISION-27"; "writing rule 9's question". Changed.

**FINDING-1195.** (E-44) [not changed in round 3] rule 9; checked. `TODO.md` "Make the conventions index a full Local Map" (line 389): "its chain shows only the conventions". DECISION-23 says this "chain" is written as the order the conventions act in, since the Name Chain Link exists beside it. Line 396, "three links, each with its upkeep", means Chain Links. 2 lines. Proposed: fix: "its order shows only the conventions that act in sequence"; "three Chain Links". Unchanged.

**FINDING-1196.** (E-45) [not changed in round 3] rule 9; checked. `TODO.md` (line 392): "The local-map rule now exists". The Name is Local Map, and it has a home in project-recording §8.6. Proposed: fix: "Project-recording's Local Map part now exists". Unchanged.

**FINDING-1197.** (E-46) [changed in round 3] rule 9; checked. `TODO.md` "Decide how work is run by agents" (line 183-184): "the binding, agent-arrangement §5, would hold the mechanics". The Name is Tool Binding, and the Fact Reference lacks its path and title. Proposed: fix: "the Tool Binding (`docs/conventions/agent-arrangement/` §5, *The Claude Code Tool Binding*) would hold the mechanics". Changed.

**FINDING-1198.** (E-47) [not changed in round 3] rule 9; checked. Convention and agent-part names without their kind word (DECISION-24, DECISION-27):
- `TODO.md` (line 169): "both commit-messages':";
- `TODO.md` 435: "the retrospective puts";
- `TODO.md` 1156-1157: "Probably the arrangement's to say", one of the phrases DECISION-24 names to change;
- `TODO.md` 238: "Decide whether approach drafting becomes a convention".

4 lines. Proposed: fix: "both the commit-messages manual's"; "the retrospective Agent Skill puts"; "agent-arrangement's to say"; "whether the approach-drafting Approach on Trial becomes a convention". 1156-1157 changed; 169, 238, 435 unchanged.

**FINDING-1199.** (E-48) [not changed in round 3] rule 9; checked. `TODO.md` "Look again at where a CBC Run learns…" (line 883-884): "how to treat a Skill Template". The Name is Agent Skill Template, carried whole (writing rule 9). Line 898 has "an Output Shape for an Agent Skill Templates", where the article and the plural disagree. 2 lines. Proposed: fix: "an Agent Skill Template"; "(d) an Output Shape for Agent Skill Templates". 884 unchanged; 898 changed.

**FINDING-1200.** (E-49) [changed in round 3] rule 9; checked. `TODO.md` "Decide how a Work Approach and an Output Shape divide…" (line 230-233): "an Agent Skill, an Output Shape and a template", "the registry entry's fields". These are an Agent Skill Template and the Invariant Slice Entry. Proposed: fix: "and an Agent Skill Template"; "the Invariant Slice Entry's fields". Changed.

**FINDING-1201.** (E-50) [not changed in round 3] rule 9; checked. `TODO.md` (line 1000): "its Evidence-Test Shape". The Name is Evidence Test Shape: FINDING-822 took out the hyphen. Proposed: fix: "its Evidence Test Shape". Unchanged.

**FINDING-1202.** (E-51) [not changed in round 3] rule 9; checked. `TODO.md` "Decide whether an overtaken CBC Run Reading…" (line 1121): "ten asks and offers". A CBC Run Ask is a line asking for a verdict on an edit, a file it offers, or a question. Proposed: fix: "ten CBC Run Asks". Unchanged.

**FINDING-1203.** (E-52) [not changed in round 3] rule 9; checked. `TODO.md` (line 1102): "what makes a note land". The item's Context says "our Delivery Notes". Proposed: fix: "what makes a Delivery Note land". Unchanged.

**FINDING-1204.** (E-53) [changed in round 3] rule 9; checked. `TODO.md` (line 1083-1084): "the Spring hygiene parts". These are the Stack Overlay, which line 1091 names. Proposed: fix: "points at the Spring Stack Overlay". Changed.

**FINDING-1205.** (E-54) [not changed in round 3] rule 9; checked. `TODO.md` "Filter a maintainer's Container Group…" (line 1048): "maintainer's container does either". This is the Container Group the title names. Proposed: fix: "so no maintainer's Container Group does either". Unchanged.

**FINDING-1206.** (E-55) [changed in round 3] rule 9; uncertain. `TODO.md` "Read text for its level in the chain" (line 623): "a model holding this repo's own rules". The item's Context names the level as "An Idea Model". Proposed: fix: "an Idea Model holding this repo's own rules". Changed.

**FINDING-1207.** (E-56) [not changed in round 3] rule 5; checked. Figures DECISION-26 decided to fix:
- `TODO.md` (line 314): "TODO sorts by horizon and trigger; within a horizon", the journey row;
- `TODO.md` 1226: "the toolkit's honest scope", the honest row.

Uncertain:
- `TODO.md` 702-703: "from the method's first walk", the journey row, unless "walk 1" is a trial's label (`cbc-derived-claude-walk1.md`);
- `TODO.md` 1062: "not master text", the master row, inside a proposed name.

4 lines. Proposed: fix: "TODO sorts by section, Now, Next and Later, then by trigger; within a section"; "it names the real scope of the Agent Skills"; question for walk and master. 702 changed; the rest unchanged.

**FINDING-1208.** (E-57) [changed in round 3] rule 8; checked. `TODO.md` "Decide whether a receiver needs a rule…" (line 1076): "handbook and CBC Run 3". DECISION-23 says "the handbook" is said in plain words once per file, where it is first met. In TODO the plain words come later, at line 1103-1104. Proposed: fix: move "the handbook, the repo that held the working arrangement before this one," to line 1076. Changed.

**FINDING-1209.** (E-58) [not changed in round 3] rule 3; checked. `TODO.md` Later, "Release concept v2" (line 917-920): "Four items of its own: a CHANGELOG entry for the release; README true for a stranger; …; known issues filed here." Four parts are chained by semicolons, the fault FINDING-589 fixed elsewhere. Proposed: fix: a list of four. Unchanged.

**FINDING-1210.** (E-59) [not changed in round 3] rule 6; resting on the reader. A CBC Run's own name is written two ways. `TODO.md` (line 107-108): "CBC Run 5, event tickets,". Line 415 has "CBC Run 4, safe-reservation-2,". `ARCHITECTURE.md` §2.5 writes `event-tickets` and `safe-reservation-2`, and TODO 36 writes `checkout` in backticks. 2 lines. Proposed: fix: backticks, as in the table. Unchanged.

**FINDING-1211.** (E-60) [not changed in round 3] rule 9; uncertain. "shape" used as English beside Output Shape, which TODO line 656-657 itself warns of. `TODO.md` "Watch whether the worked example anchors…" (line 1164): "could steer a CBC Run toward that shape". Also `TODO.md` 1167, 1168 and `.gitignore` 16, ".env.example is the committed shape". 4 lines. Proposed: fix: "toward that kind of problem"; "another kind"; "a different kind of problem"; "the committed example". 1163-1164 and 1168 changed; 1167 and `.gitignore` unchanged.

**FINDING-1212.** (E-61) [changed in round 3] rule 9; uncertain. "tier" used beside the Tiers Model's tiers. `TODO.md` (line 1237): "a held-insight tier". Also 1241: "ADR-0007 has only the first tier". 2 lines. Proposed: fix: "a held-insight kind"; "only the first kind". 1237 changed; 1241 unchanged.

**FINDING-1213.** (E-62) [not changed in round 3] rule 5; uncertain. "rung" is a ladder figure. The concept's own words are ranking and hierarchy (`concept/02-guarantees-and-walls.md` line 56). `CHANGELOG.md` [Unreleased], Changed (line 50): "The top rung of the". Also `TODO.md` 1183 "Add a rung for System Guarantees" and 1187 "asks for a rung between". 3 lines. Proposed: fix: "The top of the Structural Wall ranking"; "Add a level for System Guarantees held by absence"; "asks for a level between". CHANGELOG 50 and TODO 1183 changed; 1187 unchanged.

**FINDING-1214.** (E-63) [changed in round 3] rule 8; resting on the reader. TODO lines that leave the reader without what they need:
- `TODO.md` (line 853): "a shipped CBC line when our manual changes";
- line 248: "at its Stage 5", where the owner is unclear and line 607 names approach-evaluation's;
- line 1139: "after a CBC Run's apply Plan Step";
- line 1253: "the milestone that fires it";
- line 1026: "*Numbering a section's parts* numbers by form", words left after a title;
- lines 1134, 1146, 1154: "(…, the working draft)", where the form asks who raised it.

8 lines. Proposed: fix: say each plainly, e.g. "a shipped line that retells a manual"; "at `approach-evaluation`'s Stage 5"; drop "numbers by form". 248 and 853 changed; the rest unchanged.

##### CHANGELOG.md

**FINDING-1215.** (E-64) [not changed in round 3] rule 9; checked. `CHANGELOG.md` header comment (line 10-11): "for the pinners: CBC Runs and skills citing a concept version". Line 18-19 has "or a skill derived from it". Line 12, in the same comment, writes "a derived Agent Skill". 2 lines. Proposed: fix: "Agent Skills"; "an Agent Skill". Unchanged.

**FINDING-1216.** (E-65) [changed in round 3] rule 9; checked. `CHANGELOG.md` [Unreleased], Added (line 39-41): "the Output Shapes their Plan Step Gates read: an Invariant Slice Record, an Evidence Test, an Enemy Collision Kill and an Invariant Slice Entry". These name the outputs, not the Output Shapes. The glossary names an Output Shape by its output plus "Shape". Proposed: fix: "the Invariant Slice Record Shape, the Evidence Test Shape, the Enemy Collision Kill Shape and the Invariant Slice Entry Shape". Changed.

##### Hygiene files, folder forms, Conversation Memory

**FINDING-1217.** (E-66) [not changed in round 3] rule 9; checked. `.gitignore` comment (line 2): "# base layer — any repo, from day zero (records-only repos included)". Also `.gitattributes` 2 and `.editorconfig` 16, "this is the base layer". The Name is Hygiene Base (DECISION-23). Our files follow the Master Copies in `delivery/container/`, which say the same, so the fix starts there. 3 lines here, 3 in the Master Copies. Proposed: fix: "# Hygiene Base — any repo, from day zero (…)"; "this is the Hygiene Base". `.gitignore` and `.gitattributes` unchanged; `.editorconfig` 16 changed.

**FINDING-1218.** (E-67) [changed in round 3] rule 9; uncertain. `.editorconfig` comment (line 10): "# Layout conventions (hand-kept - no tool formats this file):". Here "convention" is a defined thing (DECISION-32). The Master Copy reads the same. Proposed: fix: "# Layout rules (…)", in the Master Copy first. Changed.

**FINDING-1219.** (E-68) [not changed in round 3] rule 9; checked. `TODO-CONVERSATION-MEMORY.md` title (line 26): "# TODO's conversation-memory". The Name is Conversation Memory. This is the file's title, not a part heading, so DECISION-18 does not cover it. Proposed: fix: "# TODO's Conversation Memory". Unchanged.

**FINDING-1220.** (E-69) [changed in round 3] rule 8; resting on the reader. `temp/README.md` *A draft* (line 6-9): "a CBC Run Reading written from one". The "one" points back across a list. "an evaluation of this repo while the Change Sets that fix it work through it" never names the refinement's file. Proposed: fix: "a CBC Run Reading of a CBC Run"; "the refinement's file, while the Change Sets that fix what it found are worked". Changed.

**FINDING-1221.** (E-70) [not changed in round 3] rule 5; uncertain. `temp/README.md` (line 3): "a draft on its way somewhere else". Line 6 has "a Delivery Note on its way to a CBC Run". This is a journey figure, next to DECISION-26's journey row. 2 lines. Proposed: fix: "a draft of a text whose home is elsewhere"; "a Delivery Note not yet staged". 3 unchanged; 6 changed.

`devlog/README.md` and `docs/adr/README.md`: no findings.

#### Reader F, Layer 5: our agent setup

**FINDING-1222.** (F-1) [not changed in round 3] rule 9; checked. `.claude/rules/working-a-reading.md` *Governs* (line 14): "**Governs:** what happens between `exchange-read` and". A Work Approach is always written with its kind (`docs/conventions/conventions/` §1.5, *Naming a Work Approach*; DECISION-27). A backticked name alone is neither the kind nor a path. This file has 9 such lines: 14, 15, 75, 108, 110, 113, 114, 121, 123 (`commit-plan`). Also `.claude/rules/exchange-reading.md` 14: 1 more; `.claude/rules/one-home.md` 41 (`cbc-framing`, `cbc-slice`): 1 more; `.claude/skills/exchange-deliver/SKILL.md` 21, 23: 2 more; `.claude/skills/exchange-read/SKILL.md` 11, 100: 2 more; `.claude/approaches-on-trial/approach-evaluation.md` 20, 30, 78, 92, 104 (`approach-drafting`), 114 (`working-a-reading.md`): 6 more; `.claude/approaches-on-trial/auto-run.md` 25, 41 ("the shipped `delivered-copies.md` rule"), 43, 114: 4 more; `.claude/approaches-on-trial/approach-drafting.md` 70 (`approach-evaluation`, both copies): 1 more. 26 lines. `writing.md` line 30's `exchange-read` is an example of a label kept exact, not counted. Proposed: fix: the kind word, "the exchange-read Agent Skill", "the approach-drafting Approach on Trial", "the shipped delivered-copies Agent Rule"; the path where the line points at where a fact is written. Changed 15, unchanged 11.

**FINDING-1223.** (F-2) [not changed in round 3] rule 9; checked. `.claude/rules/foundation-check.md` *A moved section* (line 62): "any file, or moves a fact to a new home, grep all living text for". Living Text is a Glossary Name (DECISION-23; `docs/glossary.md`, *How texts tie*). FINDING-664 named these lines, and its fix reached only `refinement.md`. Also `.claude/rules/one-home.md` 60, "is living text": 1 more; `.claude/skills/commit-plan/SKILL.md` 117–118 and 125, "live text": 2 more, and the same 2 in `delivery/container/.claude/skills/commit-plan/SKILL.md`. Proposed: fix: "grep all Living Text", "is Living Text", "grep Living Text", "from Living Text". Unchanged.

**FINDING-1224.** (F-3) [not changed in round 3] rule 9; uncertain. `.claude/approaches-on-trial/refinement.md` §2.2 *List the files* (line 141): "Every living file falls in exactly one Refinement Layer. When the list finds a". The adjective carries Living Text's meaning, and rule 9 may not reach an adjective made from a Name. Also this file 88, 128; `.claude/approaches-on-trial/model-placing.md` 41, "every living reference"; `.claude/rules/one-home.md` 60, "a living home", the words of facts-in-sync §1. 5 lines. Proposed: question: "every file of Living Text", "every reference in Living Text", or English as it stands. Changed 1 (128), unchanged 4.

**FINDING-1225.** (F-4) [not changed in round 3] rule 9; checked. `.claude/approaches-on-trial/refinement.md` *What this is made usable as* (line 44): "- **its Plan Step in `PLAN.md`**, whose Notes list this page's Approach Stages;". Approach Stage became Approach on Trial Stage (DECISION-19, the Agent Model's group, row 26), and the rename missed this line. The rest of the file uses the new Name. Proposed: fix: "this page's Approach on Trial Stages". Unchanged.

**FINDING-1226.** (F-5) [changed in round 3] rule 9; checked. `.claude/approaches-on-trial/refinement.md` §1.1 *The refinement's words* (line 65): "- **Living Text** — every file but history. History is the". Bold on a Name stands only at its home (DECISION-22). The glossary and DECISION-23 put Living Text's home at facts-in-sync §1, so this is a second definition, in bold, with a scope of its own (`docs/baselines/`, a CBC Run's text in `temp/`). Proposed: question: either this section is the home and the glossary points here, or the bold goes and the line reads as the refinement's scope: "A refinement reads Living Text (`docs/conventions/facts-in-sync/` §1, *One home*), less `docs/baselines/` and a CBC Run's own text in `temp/`." Changed.

**FINDING-1227.** (F-6) [not changed in round 3] rule 9; checked. `.claude/rules/one-home.md` *Governs* (line 8): "rules, comments and config. Where it lives, never how it reads." The list names kinds of file, "manuals, Agent Skills, rules", and "rules" stands for Agent Rules. Also this file's footer 68, "the one-home rule" (DECISION-27: the one-home Agent Rule); `.claude/approaches-on-trial/refinement.md` 23 and footer 395, "writing, and one home per fact", which names two Agent Rules by bare words (DECISION-24: a one-word convention is never its bare word). 4 lines. Proposed: fix: "manuals, Agent Skills, Agent Rules, comments and config"; "the one-home Agent Rule"; "the writing and one-home Agent Rules". Changed 2 (refinement 23, 395), unchanged 2.

**FINDING-1228.** (F-7) [changed in round 3] rule 9; checked. `.claude/rules/writing.md` *The rules*, rule 10 (line 71): "headings, a stage heading and a numbered rule's bold lead are not". The manual says "an Agent Skill Stage heading" (`docs/conventions/writing/` §2, *Why each rule*, rule 10), and DECISION-20 also counts the refinement's Approach on Trial Stage headings. Lowercase "stage" stands for both Names. Also `delivery/container/.claude/rules/writing.md` 69: 1 more. Proposed: fix: "an Agent Skill Stage or Approach on Trial Stage heading", with the manual's rule 10 gaining the second Name. Changed.

**FINDING-1229.** (F-8) [not changed in round 3] rule 9; checked. `.claude/skills/exchange-deliver/SKILL.md` *Stage 2* (line 102): "## Stage 2 — stage and copy across". The glossary's Delivery Staging entry says the verb names its object, "stage a delivery", since git's verb is the same word. Here it has none, and stands beside "Stage 2". Line 106, "If the agent stages, it runs steps 1 and", is the second. 2 lines. Proposed: fix: "## Stage 2 — stage the delivery and copy it across"; "If the agent stages the delivery". Unchanged.

**FINDING-1230.** (F-9) [not changed in round 3] rule 9; checked. `.claude/skills/commit-plan/SKILL.md` §3 *How the commits are split* (line 93): "decisions entry — is a commit of its own, never". The entry is a Decisions Log entry, written in lowercase. Same line in the container's copy. Proposed: fix: "its Decisions Log entry". Unchanged.

**FINDING-1231.** (F-10) [not changed in round 3] rule 9; checked. `.claude/approaches-on-trial/approach-drafting.md` *Stages*, §1 *Open*, step 3 (line 42): "subject is approaches. It holds:". The subject meant is Approaches on Trial, as `approach-drafting` and `approach-evaluation` are about. Same line in the byte-identical shipped copy. Proposed: fix: "only when its subject is Approaches on Trial". Unchanged.

**FINDING-1232.** (F-11) [not changed in round 3] rule 9; uncertain. `.claude/approaches-on-trial/approach-drafting.md` *Not known yet* (line 94): "- **Whether the form holds:** what for, stages, not known, ways". A label inside its owner keeps its case; these words stand for the page's sections *What it is for*, *Stages*, *Not known yet*, *Ways rejected*, *Uses*. Also this file 67, "under the Approach on Trial's uses"; `.claude/approaches-on-trial/approach-evaluation.md` 102, "each Approach on Trial's "settled when""; `.claude/approaches-on-trial/model-placing.md` 72, "changed nothing in its stages"; `.claude/rules/working-a-reading.md` footer 137, "a CBC Run Reading's gates and stages". 5 lines. Proposed: fix: the labels in italics, "*What it is for*, *Stages*, *Not known yet*, *Ways rejected*, *Uses*"; "its *Settled when*"; "its Approach on Trial Stages". Unchanged.

**FINDING-1233.** (F-12) [not changed in round 3] rule 9; uncertain. `.claude/approaches-on-trial/auto-run.md` *What it is for* (line 9): "So that a CBC Run can go from birth to Release with no stop for the". CBC Run Birth is a Name, and "birth" names the same event in lowercase. DECISION-26 kept "born" as a dead figure; it said nothing of the noun. Also this file 4, 34, 56, 59, 96, 101, 103, 111, 133–134: 9 more; `.claude/skills/exchange-deliver/SKILL.md` 42, 153, 200: 3 more; `.claude/rules/one-home.md` 24: 1 more. 14 lines. Proposed: question: is "birth" English beside the Name, as "born" is? If so the glossary entry can say it; if not, "CBC Run 5's CBC Run Birth" and the like. Changed 8, unchanged 6.

**FINDING-1234.** (F-13) [not changed in round 3] rule 9; uncertain. `.claude/skills/visual-comparison/SKILL.md` opening (line 24): "Kind: playbook — copied into a fresh draft each time, never". "Playbook" here is a kind of Agent Skill. Elsewhere "the playbook" is `delivery/fills/cbc-run-pure-playbook.md` (`docs/glossary.md`, Delivery Fill). One word, two meanings. Both copies. Proposed: question: "Kind: an Agent Skill copied into a fresh draft each time, never run in place", or decline as English. Unchanged.

**FINDING-1235.** (F-14) [not changed in round 3] rule 9; uncertain. `CLAUDE.md` *Records*, header comment (line 16): "record's item in the records map". The Fact Reference after it titles the thing *The records at a glance*; "the records map" is ADR-0067's word. DECISION-23 put "the map" into plain words beside Local Map, and the same test may reach this one. Also `.claude/approaches-on-trial/refinement.md` 134, "with the map of the records". Proposed: question: "summarizes the record's item in project-recording's list of the records", or English as it stands. Unchanged.

**FINDING-1236.** (F-15) [not changed in round 3] rule 9; uncertain. `.claude/rules/working-a-reading.md` *Decisions* (line 133): "against its source, and its file read whole". Step 4, which this line summarizes, says "checked against its foundation", and the glossary's Foundation Line entry says *source* is not our word. Proposed: fix: "a taken item checked against its foundation". Unchanged.

**FINDING-1237.** (F-16) [not changed in round 3] rule 5; checked. `.claude/skills/exchange-deliver/SKILL.md` *Stage 1*, step 1 (line 42): "Those are the copies, and only they travel after birth". DECISION-26's journey row fixes "travels". Also `.claude/skills/visual-comparison/SKILL.md` 141, "is provisional and does not travel", and footer 155, "travelling": 2 more; `delivery/container/.claude/skills/visual-comparison/SKILL.md` 142 and 156: 2 more. 5 lines. Proposed: fix: "only they are delivered after birth"; "is provisional and is not delivered"; "provisional and not delivered". Unchanged.

**FINDING-1238.** (F-17) [not changed in round 3] rule 5; checked. `.claude/approaches-on-trial/approach-evaluation.md` *Not known yet* (line 103): "needs a floor of uses.". DECISION-26 fixes "floor and ceiling". 1 line. Proposed: fix: "or placing needs a set number of uses first". Unchanged.

**FINDING-1239.** (F-18) [changed in round 3] rule 5; checked. `.claude/approaches-on-trial/auto-run.md` *Stages*, stage 4 (lines 48–49): "every trouble the CBC Run Briefing names / staged by a test;". "Stage" as a verb for making an adversity happen is the theatre figure FINDING-792 fixed in the method's texts to "create". 1 line. Proposed: fix: "every trouble the CBC Run Briefing names created by a test". Changed.

**FINDING-1240.** (F-19) [not changed in round 3] rule 5; resting on the reader. `.claude/skills/exchange-deliver/SKILL.md` *Stage 2*, step 2 (line 155): "`concept/` is the one path that is not a mirror". "A mirror" stands for "copied to the same path". 1 line. Proposed: fix: "`concept/` is the one path that moves: it lands at `docs/concept/` in the CBC Run". Unchanged.

**FINDING-1241.** (F-20) [not changed in round 3] rule 6; checked. `.claude/rules/convention-manual.md` header comment (lines 8–9): "while a new one is written (docs/conventions/agent-arrangement/ / §5.6); says its form, never its content." A Fact Reference carries path, section and title (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*); this one has no title. Also `.claude/rules/exchange-reading.md` 9 and `.claude/rules/foundation-check.md` 11, the same reference: 2 more. And `.claude/approaches-on-trial/refinement.md` 70, "(`docs/conventions/facts-in-sync/` §1, One home)", a title with no asterisks outside a comment: 1 more. 4 lines. Proposed: fix: "(docs/conventions/agent-arrangement/ §5.6, Rules files)"; "*One home*". Unchanged.

**FINDING-1242.** (F-21) [changed in round 3] rule 6; resting on the reader. `.claude/rules/one-home.md` *The rules*, rule 3 (line 30): "reads it in the owner's place. `ARCHITECTURE.md` does this (§1.2, *The conventions*):". The same-document form (§N, *title*) is used for another document; the path stands outside the parentheses. Also `CLAUDE.md` 3, "(see `docs/models/tiers.md` §2.1, *The empty top tier*, §2.2, *Concept Repos*)": "see" and two sections inside one pair of parentheses, against the one form of §3.1. 2 lines. Proposed: fix: "`ARCHITECTURE.md` does this (`ARCHITECTURE.md` §1.2, *The conventions*)"; "A Concept Repo (`docs/models/tiers.md` §2.2, *Concept Repos*)", with §2.1 in its own parentheses if the line needs it. Changed 1 (one-home 30), unchanged 1.

**FINDING-1243.** (F-22) [not changed in round 3] rule 6; checked. `.claude/rules/foundation-check.md` *The check*, step 3 (line 39): "3. **A Canonical Description changed:** walk what derives from it, as the Change Walk's step 3". The Change Walk is facts-in-sync §4's step 3 ("The greps and these re-reads are the Change Walk"); it has no step 3 of its own. The reference is reworded and points at a step that does not exist. Proposed: fix: "3. **A Canonical Description changed:** run the Change Walk on what derives from it (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 3)." Unchanged.

**FINDING-1244.** (F-23) [not changed in round 3] rule 2; resting on the reader. `.claude/rules/working-a-reading.md` *The steps*, step 4 (lines 51–52): "where a CBC Run's decision says it / lands names a place, never how the CBC Runs lived it." The clause nests a subject inside a subject and cannot be read once. Proposed: fix: "It is checked against what the CBC Runs did, too. A CBC Run's decision names where a change lands, not how the CBC Runs lived with it." Unchanged.

**FINDING-1245.** (F-24) [changed in round 3] rule 2; resting on the reader. `.claude/skills/exchange-read/SKILL.md` *Stage 2* (line 32): "Reading's first line, a new CBC Run Reading's or the open one's,". "…or the open one's, moved, before anything is read" packs two cases and a timing into one sentence. Proposed: fix: "Write it now as the CBC Run Reading's first line, before anything is read. In an open CBC Run Reading, the first line moves to it." Changed.

**FINDING-1246.** (F-25) [not changed in round 3] rule 2; resting on the reader. `.claude/rules/writing.md` header comment (lines 12–14): "Ours, derived from docs/conventions/writing/ like the". A semicolon joins two ideas, and the second runs backward: "how the two differ, that manual's *What this is made usable as* lists". Also `.claude/rules/one-home.md` 14–15, "How the two Convention Seats differ, that manual's *The seats* says.": 1 more; `.claude/rules/convention-manual.md` 10–11, "The why is (docs/conventions/conventions/ §2, The Convention Manual).", a sentence that is only a reference: 1 more. 3 places. Proposed: fix: "Ours is derived from docs/conventions/writing/, as the container's is. That manual's What this is made usable as lists how they differ."; "That manual's *The seats* says how the two differ."; "The why is in docs/conventions/conventions/ (§2, The Convention Manual)." Changed 1 (one-home 15), unchanged 2.

**FINDING-1247.** (F-26) [not changed in round 3] rule 2; resting on the reader. `CLAUDE.md` *Records* table (line 24): "| Starting work, or noticed something not doing it now | What's next; the backlog | TODO.md |". "Noticed something not doing it now" mixes tense and drops its subject. Proposed: fix: "Starting work, or noticing something to do later". Unchanged.

**FINDING-1248.** (F-27) [changed in round 3] rule 2; checked. `.claude/skills/exchange-deliver/SKILL.md` description (line 3): "Use when the reviewer says to deliver — after a CBC Run Reading, or when something a CBC Run holds has changed here — and for a Delivery Note alone". DECISION-30: a description stays one paragraph of short sentences. This sentence holds three cases between a pair of dashes. Also `.claude/skills/visual-comparison/SKILL.md` 3, "Settle how a structure is shown — a picture, a table, a plain list — by writing down", both copies: 1 more. Proposed: fix: "Use when the reviewer says to deliver: after a CBC Run Reading, or when something a CBC Run holds has changed here. Use it too for a Delivery Note alone, when a CBC Run Reading found nothing to send."; "Settle how a structure is shown: a picture, a table or a plain list. Write down what the reader must get, and render every candidate against it." Changed 1 (exchange-deliver), unchanged 1.

**FINDING-1249.** (F-28) [changed in round 3] rule 7; resting on the reader. `.claude/rules/working-a-reading.md` header comment (line 7): "<!-- How this repo works a CBC Run Reading, from the CBC Run Reading to the Delivery Note.". The Name stands twice where one use says it. Also `.claude/approaches-on-trial/auto-run.md` 25, "the CBC Run's CBC Run Reading (`exchange-read`)": 1 more. Proposed: fix: "How this repo works a CBC Run Reading's list, from the written CBC Run Reading to the Delivery Note."; "This is not a CBC Run Reading of it (the exchange-read Agent Skill)". Changed.

**FINDING-1250.** (F-29) [not changed in round 3] rule 7; resting on the reader. `.claude/skills/visual-comparison/SKILL.md` opening (line 11): "build each one, judge it line by line, and let the render decide.". Lines 10–11 give the steps, and the list at 13–18 gives the same four again; §2 then gives six. Both copies. Proposed: fix: keep the list and cut "Write what the reader must get *before* looking at candidates, build each one, judge it line by line, and let the render decide." to "Write what the reader must get before looking at candidates." Changed.

**FINDING-1251.** (F-30) [changed in round 3] rule 3; checked. `.claude/approaches-on-trial/auto-run.md` *Stages*, stage 4 (line 44): "   - how far it may grow or shrink: the CBC Run Briefing's Out, what". The item chains three parts with semicolons (lines 44–49), inside a list whose items already end in semicolons, so the count is hidden. Proposed: fix: a sub-list under "how far it may grow or shrink:", one line each for the Out, the bound on Responsibility Areas and Invariant Slices, and the troubles created by a test. Changed.

**FINDING-1252.** (F-31) [not changed in round 3] rule 3; checked. `.claude/approaches-on-trial/approach-drafting.md` *Uses* (lines 115–116): "trial in `docs/conventions/`. It closed in three pieces: its work / to the file of the refinement, the Concept Deliverer's fixing of its". The three pieces are joined by semicolons, and the first holds a comma gloss, so it reads as four. Both copies. Proposed: fix: "It closed in three pieces:" then a list: "its work, to the refinement's file (the refinement: the Concept Deliverer fixing its own text against its rules); two ideas, to TODO; its way of judging a fix, to the refinement." Changed.

**FINDING-1253.** (F-32) [not changed in round 3] rule 3; resting on the reader. `.claude/skills/commit-messages/SKILL.md` *The agent's own files* (line 105): "commit that touches them is scoped `agent` — `chore(agent)` to add,". A pair of dashes holds a list of parts mid-sentence (105–107). Also, both copies where shipped: `commit-messages/SKILL.md` 21–22; `.claude/skills/commit-plan/SKILL.md` 92–93 and 122–123; `.claude/rules/exchange-reading.md` 14–15; `.claude/rules/working-a-reading.md` 69; `.claude/rules/convention-manual.md` 77–78; `.claude/skills/exchange-deliver/SKILL.md` 89–90: 7 more. 8 sentences. Proposed: fix: a colon and a list, or a sentence per part: "A commit that touches them is scoped `agent`, and touches nothing else. `chore(agent)` adds, installs or updates an Agent Skill or Agent Rule. `docs(agent)` is for a commit plan's lifecycle." The dashes stand on unchanged lines; 4 of the 8 sentences have a changed line. Unchanged.

**FINDING-1254.** (F-33) [not changed in round 3] rule 8; uncertain. `.claude/skills/exchange-deliver/SKILL.md` *Stage 1*, step 9 (line 99): "9. **Commit the Delivery Note last.** The commit after this one is `H`, and". "This one" reads as the last commit before the Delivery Note. *Gates* (line 187) and `docs/conventions/exchange/` §3.1, *Delivery Staging*, name the Delivery Staging by the Delivery Note's own commit. Proposed: fix: "Its commit is `H`, and the Delivery Staging is named by it." Unchanged.

**FINDING-1255.** (F-34) [not changed in round 3] rule 8; resting on the reader. `.claude/skills/exchange-deliver/SKILL.md` *Stage 2*, step 3 (line 170): "   The CBC Run's Agent Rule takes it from there.". Which Agent Rule is not said. Line 198, "The CBC Run's Agent Rule does", is the second. 2 lines. Proposed: fix: "The CBC Run's delivered-copies Agent Rule takes it from there." Unchanged.

**FINDING-1256.** (F-35) [not changed in round 3] rules 5 and 9; checked. `delivery/container/.claude/skills/commit-plan/SKILL.md` §2 *The plan file* (line 59): "- **The list may roll.** Commits near at hand are firm. Commits". ADR-0069: where the two seats agree, the text is the same. The round fixed ours (`31156de`; FINDING-626 to 629, 631, 671; DECISION-22, 24, 26, 27), and `ddd6057` carried none of it to the container. The container still has: bold **Change Set** (9); "set" for Change Set (17, 67, 89, 90, 109, 110, 112, 113, 115, 116, 182, 194); "roll" and "decision horizon" (59–60); "travels the same road" (142); "Small steps" (104, 151, 191); "commit-messages" bare (53, 148, 159, 187); "artifact" (74, 84); "scaffold" (180); "provisional tail" (169, 185). About 30 lines. Explained by seat, and not counted: 95, a path the CBC Run can open, and 148–149, no Fact Reference to our manual. Proposed: fix: carry our wording into the container's copy, with 95 and 148–149 kept for the seat. Unchanged.

#### Reader G, Layer 6: the delivery's pages and the Container Group

##### delivery/README.md

**FINDING-1257.** (G-1) [not changed in round 3] rule 9; checked. `delivery/README.md` §6, *When it lands* (line 94): "Only infra-serve, re-entry, arrives unplanned". It has two faults. The Agent Skill is written without its kind word (DECISION-27). "re-entry" is lowercase where the stack's Name is Infrastructure Service Re-entry. Proposed: fix: "Only the infra-serve Agent Skill, for an Infrastructure Service Re-entry, arrives unplanned". Unchanged.

**FINDING-1258.** (G-2) [changed in round 3] rule 8; resting on the reader. `delivery/README.md` §5, *What a CBC Run does not get* (line 81): "Its own decisions, its own run files and its own versioning". Nothing says what "run files" are. A bare "run" is English, so the phrase names no file kind the reader knows. Proposed: question: which files are meant, the `temp/RUN-n.md` kind? Name them in plain words. Unchanged.

**FINDING-1259.** (G-3) [changed in round 3] rule 8; resting on the reader. `delivery/README.md` §2, *Three ways a file lands* (lines 55–56): "recorded under the container's record rules". Also §4 (lines 76–77): "the standing comments". Neither phrase says what it refers to. The first means the records table and each Record Stub's header comment. The second means the header comments. 1 more. Proposed: fix: "recorded as the container's records table and Record Stub headers say"; "the header comments". Unchanged.

##### delivery/installs/pure-seed.md

**FINDING-1260.** (G-4) [changed in round 3] rule 9; checked. `delivery/installs/pure-seed.md` step 6, after the prompt (line 258): "a reviewer is present *this CBC Run*". The sentence is about one session ("true of this session too"). The Name makes it claim a reviewer for the whole CBC Run. The text looks like a "run" replaced by the Name where it meant "this time". Proposed: fix: "a reviewer is present *in this session*". Unchanged (present at `00420b9`).

**FINDING-1261.** (G-5) [changed in round 3] rule 9; checked. `delivery/installs/pure-seed.md` step 4, after the block (line 183): "This manual delivers what the Master Copy holds". The Pure Seed is a procedure, not a manual. "Manual" here means a Convention Manual. Proposed: fix: "The Pure Seed delivers what the Master Copy holds". Unchanged (the old text had "this manual delivers").

**FINDING-1262.** (G-6) [changed in round 3] rule 9; checked. `delivery/installs/pure-seed.md` closing checklist (line 330): "No Plan Step Gate waits on the briefing to block it". The lowercase "the briefing" stands where the Name CBC Run Briefing is meant (DECISION-19 table row 30). The same sentence then writes the Name. Proposed: fix: "No Plan Step Gate waits on the CBC Run Briefing". Changed.

**FINDING-1263.** (G-7) [not changed in round 3] rule 9; checked. `delivery/installs/pure-seed.md` step 4, shell comment (lines 144–145): "a CBC Run on another stack names method alone and is born with two method Agent Skills, not five". `method` is the loop's directory name, but it is written bare. "Two method Agent Skills, not five" reads as if the method has five. Five is the method and stack together. Proposed: fix: "names `method` alone, and is born with the Method Group's two Agent Skills, not the five of both groups". Changed (Names only).

**FINDING-1264.** (G-8) [changed in round 3] rule 8; resting on the reader. `delivery/installs/pure-seed.md` step 4, after the block (lines 174–175): "Where it began is ADR-0025's, not a number the Newborn CBC Run holds." "It" is the container, and "where it began" is not said in plain words. Proposed: fix: "The container's own history here is ADR-0025's. The Newborn CBC Run holds no commit for it." Unchanged.

**FINDING-1265.** (G-9) [changed in round 3] rule 8; resting on the reader. `delivery/installs/pure-seed.md` step 4, after the block (lines 184–185): "CBC Framing's comment goes in with the Plan Steps." This names a comment the reader has not met. It is the HTML comment under the playbook's Step 1. Proposed: fix: "The comment under the playbook's Step 1, CBC Framing, goes in with the Plan Steps." Changed.

**FINDING-1266.** (G-10) [changed in round 3] rule 5; resting on the reader. `delivery/installs/pure-seed.md` step 4, shell comment (line 149): "# Their footers stay home, as the container's did in step 2." "Stay home" is a figure. The footers are cut off. Proposed: fix: "# Their footers are stripped, as the container's were in step 2." Changed.

**FINDING-1267.** (G-11) [changed in round 3] rule 5; resting on the reader. `delivery/installs/pure-seed.md` step 6, after the prompt (lines 258–260): "A stop written only in a file loses to the harness's pressure to finish". This is personification. Proposed: fix: "A stop written only in a file is skipped when the harness pushes to finish and nothing outside the file says a reviewer is present." Unchanged.

**FINDING-1268.** (G-12) [changed in round 3] rule 2; resting on the reader. `delivery/installs/pure-seed.md` step 6, the prompt (line 228): "Then plan the work as the conventions you were given direct:". The verb comes last, so "direct" first reads as an adjective. The prompt goes to the Newborn CBC Run's agent. Proposed: fix: "Then plan the work the way the delivered Agent Skills and Agent Rules say:". See also *Met in passing*, on "conventions". Unchanged.

##### delivery/fills/cbc-run-pure-playbook.md (lands in the CBC Run's `PLAN.md`)

**FINDING-1269.** (G-13) [changed in round 3] rule 9; checked. `delivery/fills/cbc-run-pure-playbook.md` *The Plan Step Form* (line 50): "the order service's first Invariant Slice, which runs `cbc-slice`". The Agent Skill is written without its kind word (DECISION-27). Also line 156, the Step 1 comment's "(cbc-framing)": 1 more. Proposed: fix: "which runs the cbc-slice Agent Skill"; "(the cbc-framing Agent Skill)". Unchanged.

**FINDING-1270.** (G-14) [not changed in round 3] rule 6; checked. `delivery/fills/cbc-run-pure-playbook.md` *At the close* (line 111): "(`.claude/approaches-on-trial/approach-drafting.md`, its close)". "Its close" is not a section title. The section is *Stages*, §3, *Close*. Proposed: fix: "(`.claude/approaches-on-trial/approach-drafting.md`, *Stages*, §3, *Close*)". Unchanged.

**FINDING-1271.** (G-15) [changed in round 3] rule 8; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` Step 0 (line 145): "Goal: the container exists before content". The CBC Run's glossary has no Container Group, so the reader cannot resolve this. In a CBC Run on this stack, "container" already means a podman container (the stack's Execution Environment). Also `delivery/container/docs/glossary/container.md` line 70, Stack Overlay: "the marked line the container's base carries": 1 more. Proposed: fix: "Goal: the repo, the records and the agent's arrangement exist before any content."; "below the marked line each hygiene file carries". Unchanged (the glossary line moved from the old `docs/glossary.md`).

**FINDING-1272.** (G-16) [not changed in round 3] rule 8; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` *At the opening* (lines 62–63): "a branch not cut cannot be cut afterwards". A branch can be cut at any time. The real point is that work done before the cut is not on the branch. Proposed: fix: "Cheap now, impossible later: work done before the branch is cut is not on it." Unchanged.

**FINDING-1273.** (G-17) [not changed in round 3] rule 8; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` (lines 135–141): "A piece of the way of working put on trial says at which Plan Step's close it is judged" and "A default that does not fit a Plan Step … not a Plan Step cutting a corner". Neither "a piece of the way of working" nor "a default" says what it is. "Cutting a corner" is an idiom (rule 5). Proposed: fix: "A change to how work is done, put on trial, names the Plan Step whose close judges it."; "A playbook item that does not fit a Plan Step is struck there, with its reason. That is a finding about the item, not a Plan Step skipping work." Unchanged.

**FINDING-1274.** (G-18) [not changed in round 3] rule 8; resting on the reader. `delivery/fills/cbc-run-pure-playbook.md` Step 3 (line 179): "Goal: services stood up, constrained to need, verified both ways." "Both ways" means the Catalog Check and the Behavioral Check. Only the infra-establish Agent Skill says so. Proposed: fix: "Goal: the services the Invariant Slices need stood up and constrained, each verified by a Catalog Check and a Behavioral Check." Unchanged.

**FINDING-1275.** (G-19) [changed in round 3] rule 3; uncertain. `delivery/fills/cbc-run-pure-playbook.md` Steps 5..N-3, N-2 and N-1 (lines 194–198, 205–211, 220–224): "Goal: two things are true at each close:" with a bulleted list after it. The Form's Goal is "<one sentence …>" (line 31). DECISION-30 kept a Goal as one sentence with its parts labelled inside it. The round's fix made three Goals into a lead line plus bullets. Proposed: question: is a lead line plus bullets "one sentence, its parts labelled"? If not, write each as one sentence: "Goal: at each close, (1) the Invariant Slice is closed by an Evidence Test that creates its adversity, and (2) the order of the Invariant Slices left is decided again." Changed.

**FINDING-1276.** (G-20) [changed in round 3] rule 8; uncertain. `delivery/fills/cbc-run-pure-playbook.md` Step 1 comment (line 153): "<!-- CBC: this Plan Step opens on the CBC Run Briefing." Nothing in the CBC Run says what the "CBC:" tag on a comment marks. Proposed: question: drop the tag, or say once in `PLAN.md`'s header what it marks. Changed (the tag was kept from "CbC:").

##### The Container Group: records and comments

**FINDING-1277.** (G-21) [change not traced] rule 8; uncertain. 11 lines in 10 shipped files point at the Concept Deliverer's manuals with a "CBC" prefix: `delivery/container/.claude/CLAUDE.md` lines 40 and 60, `README.md` 35, `ARCHITECTURE.md` 9, `CHANGELOG.md` 18, `PLAN.md` 10, `TODO.md` 24, `devlog/devlog.md` 12, `docs/adr/0001-record-architecture-decisions.md` 41, `.claude/decisions.md` 28, and `.claude/rules/delivered-copies.md` 163, "(CBC `docs/conventions/exchange/` §5.8, *Agent Skill Templates*)". The CBC Run cannot open these files. Nothing in its tree says "CBC" is the Concept Deliverer's Repo Tag. The container glossary has no Repo Tag, and `README.md` line 21 shows only `<TAG> ADR-nnnn`. DECISION-3 excepted only `one-home.md` and `writing.md`, and those two say "the Concept Deliverer's" in words. Proposed: question: write "the Concept Deliverer's" before each, as `delivery/container/.claude/rules/writing.md` line 12 does, or decline them as provenance for our Foundation Check. Unchanged; `CLAUDE.md` line 60's title changed.

**FINDING-1278.** (G-22) [not changed in round 3] rule 2; resting on the reader. `delivery/container/.claude/CLAUDE.md`, the three-tests comment (lines 61–62, 66–67): "else it is a convention, stated once, there" and "a fact whose failure is not noticing it". "There" points at nothing. The second phrase cannot be read once. "Convention" is also what a CBC Run does not hold (DECISION-32). Proposed: fix: "1. True of this project and nowhere else. Otherwise it belongs in a delivered Agent Skill or Agent Rule, stated once." and "3. Nothing else would deliver it: a stance, or a fact nobody would notice was missing." Unchanged.

**FINDING-1279.** (G-23) [not changed in round 3] rule 3; checked. `delivery/container/.claude/CLAUDE.md` *Records* comment (lines 37–38): "Three things per row — the moment, what it holds, the path — never the rule itself". The parts are chained with dashes. Also: `delivery/container/docs/adr/0001-record-architecture-decisions.md` lines 8–9, "Significant decisions — what to use, … what a term means — will be made"; `delivery/container/.claude/skills/commit-messages/SKILL.md` lines 20–22, "reads as a command — "fix race in order creation" — and a record as what became true", and lines 105–107, "scoped `agent` — `chore(agent)` to add, … — and touches nothing else"; `delivery/container/.claude/skills/visual-comparison/SKILL.md` line 3, the description, "— a picture, a table, a plain list —". 4 more. Proposed: fix: a colon and a list, or separate sentences. In the description, keep one paragraph of short sentences (DECISION-30). Unchanged.

**FINDING-1280.** (G-24) [not changed in round 3] rule 9; checked. `delivery/container/.claude/decisions.md` header comment (line 3): "The working arrangement's decision log." The lowercase "decision log" stands where the Name Decisions Log, in the container glossary, is meant. Proposed: fix: "The working arrangement's Decisions Log." Unchanged.

**FINDING-1281.** (G-25) [changed in round 3] rule 2; resting on the reader. `delivery/container/PLAN.md` header comment (lines 6–8): "with a playbook's full sequence, a concept's. The playbook itself stays where it came from. Born without one, fill the placeholders in place." "A concept's" hangs off the end. "Born without one" dangles. Proposed: fix: "with the full sequence of Plan Steps from a playbook the Concept Deliverer keeps. The playbook itself is not delivered. A project born without a playbook fills the placeholders in place." Unchanged.

**FINDING-1282.** (G-26) [not changed in round 3] rule 5; checked. `delivery/container/PLAN.md` *Discovered along the way* comment (line 63): "assign to a Plan Step, park in Later, or drop". DECISION-26 rules "park" a figure to fix. Also `delivery/container/.claude/skills/retrospective/SKILL.md` line 93, "is parked to the moment it will exist": 1 more. The *Parked* section label stays, being a label. Proposed: fix: "move to Later"; "waits for the moment it will exist, listed under *Parked*". Unchanged.

**FINDING-1283.** (G-27) [not changed in round 3] rule 9; checked. `delivery/container/PLAN.md` (lines 29, 50): "<first step, e.g. "Bootstrap">" and "<last step, e.g. "Release">". The lowercase "step" stands where Plan Step is meant. The other placeholders say "<next Plan Step>". Proposed: fix: "<first Plan Step, …>", "<last Plan Step, …>". Unchanged.

**FINDING-1284.** (G-28) [not changed in round 3] rule 9; checked. `delivery/container/devlog/devlog.md` first heading (line 16): "(Step 0: bootstrap)". A label keeps its case. The playbook's label is "Step 0: Bootstrap". Round 3 listed this in passing, and it still stands. Proposed: fix: "(Step 0: Bootstrap)". Unchanged.

**FINDING-1285.** (G-29) [changed in round 3] rule 8; resting on the reader. `delivery/container/devlog/devlog.md` header comment (line 5): "Never clean up." It does not say what is never cleaned up. Proposed: fix: "Never rewrite an earlier entry." Unchanged.

**FINDING-1286.** (G-30) [not changed in round 3] rule 5; resting on the reader. `delivery/container/ARCHITECTURE.md` *Overview* comment (line 15): "what kind of system this is, in one breath". Also *Invariants* comment (line 36), "the test that goes red if either went", where "either" has no clear antecedent (rule 8): 1 more. Proposed: fix: cut "in one breath"; "the test that goes red if the computation or the refusal were removed". Unchanged.

**FINDING-1287.** (G-31) [change not traced] rule 9; checked. `delivery/container/.editorconfig` lines 17 and 54, `.gitattributes` line 9, `.gitignore` line 29: "at app bootstrap". The Stack Overlays are appended at CBC Bootstrap, the method's Name and the playbook's Step 4. 4 lines. Proposed: fix: "at CBC Bootstrap". Unchanged (FINDING-708 changed these lines, not this phrase).

**FINDING-1288.** (G-32) [not changed in round 3] rule 9; checked. `delivery/container/.gitignore` (line 16): ".env.example is the committed shape". "Shape" carries the Output Shape meaning. FINDING-923 replaced the same phrase eight lines below. Proposed: fix: ".env.example is the committed counterpart". Unchanged.

**FINDING-1289.** (G-33) [not changed in round 3] rule 6; resting on the reader. `delivery/container/.gitignore` (line 24): "The operator's standing instructions". Every other shipped file calls this person the reviewer (FINDING-711). In the stack's text, "operator" is the reader of the Operator Manual. Proposed: fix: "The reviewer's standing instructions". Unchanged.

##### The Container Group: Agent Rules and the Approach on Trial

**FINDING-1290.** (G-34) [changed in round 3] rule 9; checked. `delivery/container/.claude/rules/delivered-copies.md` rule 4's bold lead (line 75): "**At every Plan Step's close, the CBC Run Asks.**" The old "the Run Asks" was a subject and a verb. With the Name, the lead reads as a noun phrase with no verb, or as the verb "asks" capitalized by mistake. Proposed: fix: "**At every Plan Step's close, the CBC Run writes its CBC Run Asks.**" Changed.

**FINDING-1291.** (G-35) [not changed in round 3] rule 6; resting on the reader. `delivery/container/.claude/rules/delivered-copies.md` rule 5's lead (line 92): "**After the reply, the re-pin: the Delivery Take.**" "Re-pin" is a second word coined for the Name Delivery Take. It stands again at line 129, "gone with the re-pin", and line 140, "the re-pin still lands whole". The title's "re-pinned" (line 12) is the same word. 3 more. Proposed: fix: "**After the reply, the Delivery Take.**"; "gone at the Delivery Take"; "the Delivery Take still copies whole". `temp/README.md` line 13's Fact Reference to the lead follows, by the rename grep. Unchanged.

**FINDING-1292.** (G-36) [not changed in round 3] rule 8; resting on the reader. `delivery/container/.claude/rules/delivered-copies.md` rule 5 (lines 93–94): "a directory named for the hash". It does not say which hash. Also line 122: 1 more. Proposed: fix: "named for the Concept Deliverer's commit", as `temp/README.md` lines 11–12 and the glossary's Delivery Staging say. Unchanged.

**FINDING-1293.** (G-37) [not changed in round 3] rule 2; resting on the reader. `delivery/container/.claude/rules/delivered-copies.md` rule 2 (lines 62–63, 67–68): "so lived work can show one wrong" and "so the second condition does not hold it; the other two do". Neither phrase can be read once. Proposed: fix: "so work in this project can show that a chapter is wrong"; "so the second condition does not apply to it. The first and third do." Unchanged.

**FINDING-1294.** (G-38) [not changed in round 3] rule 9; checked. `delivery/container/.claude/rules/delivered-copies.md` rule 1 (line 29): "(`PLAN`, `TODO`, the devlog, the glossary)". Code font marks a path, and these are not paths. Proposed: fix: "(`PLAN.md`, `TODO.md`, the devlog, the glossary)". Unchanged.

**FINDING-1295.** (G-39) [not changed in round 3] rule 9; checked. `delivery/container/.claude/rules/shapes-lifecycle.md` §3 (line 69): "a delivered one under `delivered-copies.md`". This is neither the part with its kind word (DECISION-27) nor the full path. Also §4 line 87 and §5 line 98: 2 more. Proposed: fix: "under the delivered-copies Agent Rule" at each, or the path `.claude/rules/delivered-copies.md`. Unchanged.

**FINDING-1296.** (G-40) [not changed in round 3] rule 8; uncertain. `delivery/container/.claude/rules/shapes-lifecycle.md` §1 (line 42): "only the source shows that". "Source" means the outputs the Output Shape was written from. The glossary retires "source" as a word. Proposed: fix: "only reading the output itself shows that". Unchanged.

**FINDING-1297.** (G-41) [not changed in round 3] rule 9; checked. `delivery/container/.claude/approaches-on-trial/approach-drafting.md` *Stages*, §3 (line 70): "open `approach-evaluation`". It is written without its kind word (DECISION-27). Also `delivery/container/docs/glossary/container.md` line 73, "drafted by `approach-drafting`": 1 more. Proposed: fix: "open the approach-evaluation Approach on Trial"; "drafted under the approach-drafting Approach on Trial". Unchanged (the glossary line moved from the old `docs/glossary.md`).

**FINDING-1298.** (G-42) [not changed in round 3] rule 9; resting on the reader. `delivery/container/.claude/approaches-on-trial/approach-drafting.md` *Stages*, §1 (lines 41–42, 47): "only when its subject is approaches" and "its uses, empty until the close". Also §3 line 67, "under the Approach on Trial's uses". "Approaches" stands for Approaches on Trial. "Uses" is the *Uses* section label, which `delivered-copies.md` line 66 writes "under its *Uses*". 2 more. Proposed: fix: "only when its subject is Approaches on Trial"; "its *Uses*"; "under the Approach on Trial's *Uses*". Unchanged.

**FINDING-1299.** (G-43) [changed in round 3] rule 8; checked. `delivery/container/.claude/approaches-on-trial/approach-drafting.md` *What it is for* (line 14): "An Agent Skill or a manual written before the work describes a guess." A CBC Run holds no manual. DECISION-24 says a shipped file does not write "manual" except beside a Fact Reference. Proposed: fix: "An Agent Skill written before the work describes a guess." Changed.

**FINDING-1300.** (G-44) [not changed in round 3] rule 8; uncertain. `delivery/container/.claude/approaches-on-trial/approach-drafting.md` *Uses* (lines 115, 122, 129, 131): `docs/conventions/`, `.claude/approaches-on-trial/model-placing.md` and `4fedbb3`. These are paths and a commit in the Concept Deliverer's tree, written as a CBC Run reads its own. Each note's lead names the Concept Deliverer. DECISION-18 (c) keeps what a note says. Proposed: question: prefix "the Concept Deliverer's" to each path, or decline as the note's own words. Unchanged.

##### The Container Group: Agent Skills

**FINDING-1301.** (G-45) [changed in round 3] rule 9; checked. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` description (line 3): "(that is retrospective)". Also `delivery/container/.claude/skills/retrospective/SKILL.md` description (line 3), "that is apply-retrospective, after this": 1 more. Both are written without the kind word (DECISION-27). Proposed: fix: "(that is the retrospective Agent Skill)"; "that is the apply-retrospective Agent Skill, after this". Unchanged.

**FINDING-1302.** (G-46) [not changed in round 3] rule 3; checked. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 2 (line 74): "- regroup before rewriting; fix tags before the words around them;". Two ordering rules sit in one bullet. Proposed: fix: two bullets. Unchanged.

**FINDING-1303.** (G-47) [not changed in round 3] rule 4; resting on the reader. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 3, the stop rule (lines 108–110): "If pass 2 changed only small things, the pass ends. If it changed something real". It sets no measure. Also lines 97–98, "meaning lost, the writing rule, home", three checks given as bare nouns (rule 8): 1 more. Proposed: question: what counts as real, for example a changed fact; fix: "whether meaning was lost, whether the writing rule is met, whether each fact is at its home". Unchanged.

**FINDING-1304.** (G-48) [not changed in round 3] rule 6; resting on the reader. `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 1 (lines 37–38, 49): "**applied**, **partly** (and which part), or **next CBC Run only**" and then "**Apply here**". One status value is written two ways. Proposed: fix: "**Applied**" at line 49. Unchanged.

**FINDING-1305.** (G-49) [changed in round 3] rule 9; resting on the reader. `delivery/container/.claude/skills/retrospective/SKILL.md` Stage 4 (lines 110–111): "the three tests in its guard comment". The Entry File gives the comment no such name. "Guard" collides with the method's Standing Guard. Proposed: fix: "the three tests in the comment above its *Local rules*". Unchanged.

**FINDING-1306.** (G-50) [changed in round 3] rule 8; resting on the reader. `delivery/container/.claude/skills/retrospective/SKILL.md` Stage 3 (lines 103–104): "Dropped: the branch is deleted, and the note's commits move back." It does not say where the commits move. Proposed: fix: "Dropped: the branch is deleted, and the commits to `RETRO.md` made on it are copied back to `retrospective`." Unchanged.

**FINDING-1307.** (G-51) [not changed in round 3] rule 9; uncertain. `delivery/container/.claude/skills/retrospective/SKILL.md` Stage 1 (line 47): "Which approaches were tried and dropped?" "Approach" alone is also Work Approach's word (DECISION-19 table row 26). Proposed: fix: "Which ways of working were tried and dropped?" Unchanged.

**FINDING-1308.** (G-52) [not changed in round 3] rule 9; checked. `delivery/container/.claude/skills/commit-plan/SKILL.md` (line 17): "set's ADR is still Proposed". The lowercase "set" stands where the Name Change Set is meant. It also stands at lines 89, 90, 109, 110, 112, 113, 115 and 116: 8 more. Our copy, `.claude/skills/commit-plan/SKILL.md`, already writes "Change Set" at each, and the shipped copy was not brought along (`31156de`). Also uncertain: the bold "**Change Set**" at line 9, which our copy dropped (FINDING-626). `container.md` makes this Agent Skill the Name's home in a CBC Run, so the bold may stand. Proposed: fix: take our copy's lines. Unchanged.

**FINDING-1309.** (G-53) [not changed in round 3] rule 9; checked. `delivery/container/.claude/skills/commit-plan/SKILL.md` §2 (line 53): "Commit subjects follow commit-messages". The skill is written without its kind word. Also line 148, "The rule is commit-messages' and binds", and line 159, "follows commit-messages too": 2 more, and 1 in the footer. Proposed: fix: "the commit-messages Agent Skill", as our copy has it. Unchanged.

**FINDING-1310.** (G-54) [not changed in round 3] rule 5; checked. `delivery/container/.claude/skills/commit-plan/SKILL.md` §2 (lines 59–60): "**The list may roll.** … past the decision horizon". These are figures DECISION-26's journey row fixes. Also §5 line 142, "travels the same road", and §7 line 169, "tail refined at its boundary": 2 more; footer lines 180 and 185, "scaffold", "provisional tails". Our copy fixed each. Proposed: fix: our copy's words: "**The list may change past a point.** … Commits that a result not yet seen must shape"; "follows the same four steps"; "commit refined at its boundary". Unchanged.

**FINDING-1311.** (G-55) [not changed in round 3] rule 9; checked. `delivery/container/.claude/skills/commit-plan/SKILL.md` §4 table (line 104): "| Small steps |". Also §6 line 151, "**Small steps inside a planned commit": 1 more, and 1 in the footer. The skill's own footer cites ADR-0049, 1: "step" is `PLAN.md`'s. Our copy writes "Small commits". Proposed: fix: "Small commits" at each. Unchanged.

**FINDING-1312.** (G-56) [changed in round 3] rule 8; resting on the reader. `delivery/container/.claude/skills/visual-comparison/SKILL.md` opening (line 20): "What makes it its own method". The Agent Skill calls itself a "method" 5 times: lines 20, 47, 91, 117 and 118. In a CBC Run, "the method" is correctness by construction (`.claude/CLAUDE.md` line 16, "The method is in `docs/concept/`"). 4 more. Proposed: fix: "this Agent Skill" or "the comparison" at each. Our copy is the same. Unchanged.

**FINDING-1313.** (G-57) [not changed in round 3] rule 9; checked. `delivery/container/.claude/skills/visual-comparison/SKILL.md` opening (line 24): "Kind: playbook — copied into a fresh draft each time, never executed in place." In a CBC Run, "the playbook" is the source of its Plan Steps (`PLAN.md`'s "Steps from:"). "Kind:" is a label nothing defines. Proposed: fix: "Its steps are copied into a fresh `temp/` draft each time, never followed in place." Unchanged.

**FINDING-1314.** (G-58) [not changed in round 3] rule 10; checked. `delivery/container/.claude/skills/visual-comparison/SKILL.md` §3 (line 80): "## 3. Gates". This numbered title does not stand alone. "Gate" belongs to two Names, Plan Step Gate and Enforcement Gate, and the section lists the checks a comparison must pass. Proposed: fix: "## 3. The comparison's checks", 26 characters, with the rename grep, in both copies. Unchanged.

**FINDING-1315.** (G-59) [changed in round 3] rule 8; resting on the reader. `delivery/container/.claude/skills/visual-comparison/SKILL.md` §4 (lines 104–105, 113–115): "the rule the procedure existed to keep" and "could not place the operator … the operator is transport, not a place". The CBC Run's reader holds neither "the procedure" nor "the operator". "Transport" is a figure (rule 5). Proposed: fix: "the rule the exchange existed to keep: a CBC Run Reading writes nothing in the CBC Run"; "could not place the reviewer, who works in both repos. The fix was to show the reviewer as what carries text between them, not as a place." Unchanged.

#### Reader H, Layer 6: the Method Group

**FINDING-1316.** (H-1) [not changed in round 3] rule 8; checked. workflow *The order, and why it differs from the presentation* (line 46-47): "the two in the archive this repo came from, and those of CBC Runs 3 to 6." This file ships to a CBC Run. There, "this repo" is the CBC Run's own repo, and that repo came from no archive. The archive has no name and cannot be opened from the CBC Run's tree. Also workflow 449: "The two archive CBC Framings": 1 more. Proposed: fix: "two CBC Framings made before the first CBC Run, and those of CBC Runs 3 to 6"; line 449 "The two CBC Framings made before the first CBC Run". changed.

**FINDING-1317.** (H-2) [not changed in round 3] rule 8; checked. framing SKILL *Each Agent Skill Stage's Exit* (line 96-98): "Either way, they answer who besides the system can write what it stores;". The two ways, trusted or defended, are stated only in the workflow (lines 204-207). In SKILL.md, "either way" points at nothing. The rewrite split it from its old clause. Proposed: fix: "They answer who besides the system can write what it stores, whether that writer is trusted or defended;". changed.

**FINDING-1318.** (H-3) [not changed in round 3] rule 2; checked. framing SKILL *Export and handoff* (line 245-247): "The rest is (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is copied and filled, never edited in place*)." The sentence's object is a parenthesised Fact Reference, and "the rest" names nothing. Also template lines 6-8, the same sentence (its Fact Reference on line 5 also lacks italics on the title); slice workflow 214-215, "Why an Output Shape is read only at the close: (`.claude/rules/shapes-lifecycle.md` §2, ...)", a fragment of the same form: 2 more. Proposed: fix: "How it is used is the delivered-copies Agent Rule's (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is copied and filled, never edited in place*)."; slice workflow: "An Output Shape is read only at the close, for the reasons in `.claude/rules/shapes-lifecycle.md` §2, *Where an Output Shape lives*." changed.

**FINDING-1319.** (H-4) [not changed in round 3] rule 9; checked. glossary *The method's* (line 181-184): "**Correctness Specification** — the cbc-slice Agent Skill's Stage 1 output: … (`.claude/skills/cbc-slice/SKILL.md`)." Slice SKILL first uses the Name at line 83 and never says what it is. The slice workflow defines it, in bold, at lines 108-110: "The output is the **Correctness Specification**: invariant → Invariant Slice Guarantees → Evidence Criteria, plus the Adversity Model." So the entry points at a file that does not define it. Proposed: fix: point the entry at `.claude/skills/cbc-slice/references/cbc-slice-workflow.md`. The slice workflow's bold then stands at its home (see H-6). changed.

**FINDING-1320.** (H-5) [not changed in round 3] rule 9; checked. glossary, entries whose home uses the Name and never says what it is:
- State Witness and State Witness Reading (lines 215-219, home slice SKILL): slice SKILL uses both from line 157 and never defines them. What a State Witness is appears in `.claude/shapes/evidence-test.md` 101-102 ("Read it from where the truth is stored") and in workflow 139.
- Responsibility Area Seam (145-147, home workflow): the workflow uses it at lines 66, 359, 369 and 375, and never says it is the line between two Responsibility Areas.
- Adversity Model (194-196, home slice workflow): named once, at line 110. Its content is described in the outline at 47-49 without the Name.
- Invariant Slice Close (234-236, home slice SKILL): used from line 85. Line 221 says what is done at the close, but no line says what the close is.
- System Refusal (100-102, home framing SKILL): used at 41, 86 and 88 but never defined. The workflow (152-159) reaches it only through the System Refusal Test.
- Adversity Harness (200-202, home `system-readiness.md`): READINESS-4 and READINESS-5 say what it must do, never what it is. Uncertain.
- System Layer (35-37, home `docs/concept/01-layered-system.md`): the chapter defines the five layers but never uses the Name. Uncertain, since the chapter is not this reader's file.

Proposed: fix: one plain defining sentence at each home, in the glossary entry's words. Or, for State Witness, point the entry at `.claude/shapes/evidence-test.md`. glossary lines changed; the homes' lines changed.

**FINDING-1321.** (H-6) [not changed in round 3] rule 9; checked. workflow *The unit* (line 19): "A **CBC Framing** is one Falsifiable Promise". Bold on a Name is allowed only at its home (DECISION-22), and this Name's home is `docs/concept/03-cbc-framing.md`. Also workflow 390 "An **Invariant Slice** is"; slice SKILL 9 "Carry **one Invariant Slice**"; slice workflow 16 "An **Invariant Slice** is" (home `docs/concept/04-cbc-slice.md`): 3 more. Proposed: fix: drop the bold. changed.

**FINDING-1322.** (H-7) [not changed in round 3] rule 9; checked. Script sweep line, confirmed. workflow *Stage 2 — Name the enemies* (line 213-214): "under the label **"The runtime ground"**". The CBC Run copies this label into its System Definition. The label spells the Name Runtime Ground in lowercase, and the worked example's System Definition already writes "The Runtime Ground, beside the Enemy Facts:" (line 99). Also workflow 195, the label **"Trust assumptions — accepted deliberately, not defended"**, and worked example 81, which copies it: 2 more. Proposed: fix: labels "The Runtime Ground" and "Trust Assumptions — accepted deliberately, not defended"; worked example 81 changes to match, in both copies, in the same commit. Workflow lines changed; worked example 81 unchanged.

**FINDING-1323.** (H-8) [not changed in round 3] rule 9; checked. framing SKILL *The derivation order (not the presentation order)* (line 69-71): "becomes a logged revision of LAYER-2-SYSTEM". Row 33 of DECISION-19's table rewrote "logged revision" to the CBC Framing Export Revision. Also workflow 74 "gets a logged revision", 241 "by a dated revision", 324 "becomes a revision of LAYER-2-SYSTEM"; slice SKILL 132 "answered there by a dated revision": 4 more. Proposed: fix: "a CBC Framing Export Revision of LAYER-2-SYSTEM", and the same in each. changed.

**FINDING-1324.** (H-9) [not changed in round 3] rule 9; checked. framing SKILL *The record — the CBC Framing Exports, and one CBC Framing Derivation* (line 148-149): "It carries a draft line at its top until the close." "The close" is lowercase. Here it means CBC Framing's close, but the same files name another close, the Invariant Slice Close. Also framing SKILL 182 "at the close" and 195 "At the close" (CBC Framing's); slice workflow 190 "on what the close wrote down … what a close hands on" and 213-214 "this close … only at the close" (the Invariant Slice Close); template 103 "decided again at each close"; slice SKILL 262 heading "(mention at close)": 7 more. The Output Shapes' fixed heading *What to check at a close* and the field *Answered at close* are labels, so they are not raised. Proposed: fix: "until CBC Framing's close" in the first three; "the Invariant Slice Close" in the rest. changed.

**FINDING-1325.** (H-10) [not changed in round 3] rule 9; checked. "the record" stands for the Invariant Slice Record, which row 66 of DECISION-19's table names. `.claude/shapes/registry-entry.md` *The shape* (line 68-69): "a reference to the record. How the Invariant Slice got there is its record's." Also `evidence-test.md` 61, 83; `registry-entry.md` 53, 96, 100; `slice-record.md` 14, 19, 31 (heading "The record's order"), 215, 217, 227; slice SKILL 16, 95, 229, 230; slice workflow 4, 36, 211 (twice); `system-readiness.md` 29; template 52, 53, 107: 24 more. Proposed: fix: the Name at each use. Or a question for the reviewer: may the bare head noun stand for the Name within the paragraph that just named it? If it may, rule 9 needs that line, and FINDING-1326 and FINDING-1327 follow the answer. mostly changed (`registry-entry.md` 96, 100 and `slice-record.md` 215, 227 unchanged).

**FINDING-1326.** (H-11) [not changed in round 3] rule 9; checked. "the entry" stands for the Invariant Slice Entry (DECISION-19 row 75). slice SKILL *Stage 4 — document* (line 222-224): "The entry went to `in-progress` … The entry gets one line per item". Also `registry-entry.md` 16, 23, 64, 69, 105, 111, 113; framing SKILL 236; `system-readiness.md` 45: 9 more. Proposed: fix, or as FINDING-1325's question. mostly changed (`registry-entry.md` 105, 113 unchanged).

**FINDING-1327.** (H-12) [not changed in round 3] rule 9; checked. "the block" stands for the Invariant Slice Guarantee Block (DECISION-19 row 48). `slice-record.md` *What this document controls* (line 20): "A block this Output Shape accepts". Also `slice-record.md` 25, 27, 38, 54, 58, 166, 178, 179, 196, 219; slice workflow 52 (drawn: "one block per guarantee"), 70, 71, 72: 14 more. Proposed: fix, or as FINDING-1325's question. mostly changed (`slice-record.md` 25, 166 and slice workflow 52 unchanged).

**FINDING-1328.** (H-13) [changed in round 3] rule 9; checked. "promise" in lowercase stands for the Falsifiable Promise (DECISION-19 concept row 11). `the-whole-system-in-plain.md` *The one idea* (line 27-28): "the minimum needed to keep the promises real". There is only one Falsifiable Promise. Also `the-whole-system-in-plain.md` 38, 56, 116; workflow 83, 120, 122 (twice); framing SKILL 41; worked example 18, 47 (table head), 52; `evidence-test.md` 91, the code label `"the promise: %s"`, which is uncertain because it is a string in code: 12 more. Proposed: fix: "the Falsifiable Promise", and "candidate Falsifiable Promises" for the rejected ones. changed, except worked example 47, 52 and `evidence-test.md` 91, unchanged.

**FINDING-1329.** (H-14) [changed in round 3] rule 9; checked. "audience" stands for the Falsifiable Promise Audience (DECISION-19 row 38). workflow *Stage 0 — Choose the Falsifiable Promise* (line 121-122): "would proving it true matter to the named audience?". Also workflow 131, 135; worked example 30, 237; `the-whole-system-in-plain.md` 54: 5 more. Proposed: fix: "the Falsifiable Promise Audience". changed.

**FINDING-1330.** (H-15) [not changed in round 3] rule 9; checked. "guarantee" in lowercase stands for a System Guarantee or an Invariant Slice Guarantee. workflow *Stage 5 — Check between owners* (line 379): "LAYER-4-PROBLEMS's local guarantees". Also `the-whole-system-in-plain.md` 85 "the guarantees" and 91 (heading "who guards each guarantee"); slice workflow 49 and 52 (drawn; DECISION-21 asks a key line where the box has no room), 147 "a contention guarantee", 184 "how deep the guarantees go"; slice workflow 244 "(*invariant / adversity / guarantees / evidence criteria*)", whose "evidence criteria" also writes the Evidence Criterion lowercase and whose four headings do not match the outline's headings (46-66): 7 more. The record's own section labels, "Guarantees" and "The plan, across guarantees", are labels and not raised. Proposed: fix: the Name at each use; at 244, the outline's headings as they stand. changed, except slice workflow 49, 52 and `the-whole-system-in-plain.md` 91, unchanged.

**FINDING-1331.** (H-16) [not changed in round 3] rule 9; checked. "seam" in lowercase stands for the Responsibility Area Seam. workflow *Stage 4 — Sort into owners* (line 360): "A seam named and not drawn". Also workflow 378 "across the seams". Worked example 315, heading "What the example shows about the seams", uses "seams" in another sense: the handoffs between the two Agent Skills. That is a second meaning in the file that names one Responsibility Area Seam (line 246): 2 more. Proposed: fix: "A Responsibility Area Seam named and not drawn", "across the Responsibility Area Seams"; heading "What the example shows about the handoffs". Workflow lines changed; worked example 315 unchanged.

**FINDING-1332.** (H-17) [changed in round 3] rule 9; checked. workflow *Stage 2 — Name the enemies* (line 293): "each Enemy Census Probe's lens, its stamps, and what it found". Two Names are written in lowercase. Also workflow 295 "the saturation claim" (the Enemy Census Saturation); glossary 119-120 "each Enemy Census Probe's lens, stamps and findings": 2 more. "**The resource lens.**" (265) is a label, by trigger 5, and not raised. Proposed: fix: "its Enemy Census Probe Lens, its Enemy Census Probe Stamps"; "the Enemy Census Saturation claim". changed.

**FINDING-1333.** (H-18) [change not traced] rule 9; uncertain. Some words of a Name are used in a second sense. The reader then has to decide which meaning is meant, which is the doubt rule 9 exists to remove:
- "stamps": workflow 394 "one of two stamps" and 403 "the other stamp", for theorem and contract, beside the Enemy Census Probe Stamp;
- "fold": framing SKILL 162 "folded into FACT-CALLER-5", where one candidate fact is merged into another; `registry-entry.md` 93 and worked example 214 "races fold in here", where KILL-2 is merged into SLICE-1, not an Invariant Slice Fold;
- "probed": worked example 194, a Responsibility Area Seam examined, beside the Enemy Census Probe;
- "inversions": workflow 46 "Two inversions", two swaps of order, beside the CBC Inversion;
- "layer": slice workflow 103 "This middle layer is the real work", the Invariant Slice Guarantees, beside System Layer.

Proposed: fix: "one of two labels", "merged into FACT-CALLER-5", "races are merged here", "was examined", "Two swaps of order", "This middle step". Most lines changed; `registry-entry.md` 93 unchanged.

**FINDING-1334.** (H-19) [changed in round 3] rule 9; checked. `registry-entry.md` *The shape* (line 38): "each attack the evidence must stage". "Stage" as a verb sits beside Agent Skill Stage, which FINDING-792 fixed elsewhere. Also line 45 "what cannot be staged the normal way": 1 more. The template's own slots say "generate" (32) and "created" (39). Proposed: fix: "must create", "cannot be created". 38 unchanged, 45 changed.

**FINDING-1335.** (H-20) [not changed in round 3] rule 9; checked. framing SKILL *Export and handoff* (line 204): "names this Agent Skill, a workflow stage, or the CBC Run's arrangement". "A workflow stage" stands for an Agent Skill Stage. Also glossary 176, the Agent Language entry: "a workflow stage": 1 more. Proposed: fix: "an Agent Skill Stage". changed.

**FINDING-1336.** (H-21) [not changed in round 3] rule 9; checked. `kill.md` *The shape* (line 70-72): "says "stopped by" and the Scope Exclusion, or several: "stopped by NOT-OURS-1", "stopped by NOT-OURS-2 and SYSTEM-BOUNDARY-5"". SYSTEM-BOUNDARY-n is a Scope Verdict's tag (workflow 102), so the example calls a Scope Verdict a Scope Exclusion. Also template 85 "+ <deferrals> + <refusals>": its table (95) writes "excluded: NOT-OURS-n", and "refusal" is the System Refusal's word: 1 more. Proposed: fix: "and the Scope Exclusion or Scope Verdict that stops it, or several"; template "+ <deferrals> + <Scope Exclusions>". changed.

**FINDING-1337.** (H-22) [not changed in round 3] rule 9; checked. `kill.md` *Governs* (line 7-8): "written in the System Definition's collisions layer". This is a third name for the layer whose tag is LAYER-4-PROBLEMS (framing SKILL 61, workflow 106). Proposed: fix: "written in the System Definition's LAYER-4-PROBLEMS". changed.

**FINDING-1338.** (H-23) [not changed in round 3] rule 9; checked. slice SKILL *Stage 3 — build* (line 161-162): "record the red from actual output". DECISION-19 row 54 rewrote "the red" to the Red Run. Also line 210 "The red was recorded from actual output.": 1 more. Proposed: fix: "record the Red Run's failure from actual output"; "The Red Run's failure was recorded from actual output." changed.

**FINDING-1339.** (H-24) [not changed in round 3] rule 9; uncertain. template *The Invariant Slice Registry's state* (line 77-78): "New work enters by framing again". This is CBC Framing written as a lowercase verb (DECISION-19 concept row 17). Also template 12 "Framed <date>": 1 more. Proposed: fix: "by a new CBC Framing"; "CBC Framing closed <date>". changed.

**FINDING-1340.** (H-25) [not changed in round 3] rule 9; uncertain. slice SKILL frontmatter (line 3): "close a slice, … or to continue a project that has a slice registry (docs/system/registry.md)". The description's first sentence writes Invariant Slice and Invariant Slice Registry. The trigger list then uses the lowercase words. Proposed: question: are a description's trigger phrases the user's own English, which would stand, as the framing SKILL's "framing, a promise, invariants" does? Or are they the Agent Skill's text, held to rule 9? changed.

**FINDING-1341.** (H-26) [not changed in round 3] rule 9; uncertain. workflow *Stage 3 — Run the Enemy Collisions* (line 347): "The cbc-slice workflow's Stage 1, specify-correctness". Stage 1 belongs to the cbc-slice Agent Skill. DECISION-25 writes a stage outside its owner with that owner named, and DECISION-27 writes the kind word. Also worked example 5 "Part 2 (the cbc-slice workflow)" and 254 "enters the cbc-slice workflow": 2 more. Proposed: fix: "The cbc-slice Agent Skill's Stage 1"; "the cbc-slice Agent Skill". changed.

**FINDING-1342.** (H-27) [not changed in round 3] rule 5; checked. worked example *Stage 0 — Choose the Falsifiable Promise* (line 36-37): "replayed after a swallowed response". DECISION-26's row "swallow, archaeology, binary blob, hedge" fixes the figure. Also worked example 276; `system-readiness.md` 51; `evidence-test.md` 50 "swallow the reply": 3 more. Proposed: fix: "a lost response", "lose the reply". changed, except `evidence-test.md` 50, unchanged.

**FINDING-1343.** (H-28) [not changed in round 3] rule 5; uncertain. framing SKILL, the opening under its title (line 16-17): "A CBC Framing may honestly end in "no project"." DECISION-26 fixes "honest, honestly" said of a file; here it is said of a CBC Framing, a list and a count. Also framing SKILL 273 "an honest status line"; workflow 27 "may honestly end", 305 "named honestly"; `kill.md` 76 "the count stays honest": 4 more. Proposed: fix: drop "honestly" (SKILL 16, workflow 27); "a status line that says what the repo does now"; "named"; "and every pair is counted". changed, except framing SKILL 273, unchanged.

**FINDING-1344.** (H-29) [not changed in round 3] rule 5; uncertain. `evidence-test.md` *The order of its assertions* (line 106-107): "only checks the setup is in place. It owes nothing." "Owes" is a debt figure (DECISION-26 row "debt, bank, park, pays off"). Also `evidence-test.md` 122 "so it owes none"; `slice-record.md` 173 "is owed"; workflow 201 "The block owes one answer"; slice SKILL 197 "still owes a test"; `system-readiness.md` 79 "with READINESS-5 owed there": 5 more. The CBC Run's own writing rule's *After* example also says "owed", which suggests the reviewer may keep the word. Proposed: question: is "owe" dead in English? If not, fix: "It asserts nothing more"; "is needed"; "must answer one question"; "still needs a test"; "with READINESS-5 left to that Stage 3". changed, except `slice-record.md` 173, unchanged.

**FINDING-1345.** (H-30) [not changed in round 3] rule 5; uncertain. `evidence-test.md` *The first line says what the test is* (line 63-64): "and discharges no Enemy Collision Kill". "Discharge" is proof talk for an obligation. The same file says a test "answers" a kill (line 72). Also `evidence-test.md` 176; slice SKILL 196: 2 more. Proposed: fix: "answers no Enemy Collision Kill". changed.

**FINDING-1346.** (H-31) [changed in round 3] rule 5; checked. worked example *Part 2 — SLICE-1 enters the cbc-slice workflow* (line 292): "There is no side door." DECISION-26 keeps "door" only where it means the boundary. A side door is a path around the Structural Wall, which the concept names. Proposed: fix: "There is no Escape Hatch." changed.

**FINDING-1347.** (H-32) [not changed in round 3] rule 5; checked. workflow *Stage 2 — Name the enemies* (line 316): "*censused-and-fenced*". This Scope Verdict value keeps "fence", the figure that DECISION-19 row 23 replaced with Scope Exclusion. The glossary (139) writes "censused and excluded". Proposed: fix: "*censused-and-excluded*", as the glossary has it. changed.

**FINDING-1348.** (H-33) [changed in round 3] rule 5; resting on the reader. framing SKILL *Each Agent Skill Stage's Exit* (line 79-80): "who the claim is sold to". "Sold" is a figure. The workflow (127) and the glossary (94) say "made to". Proposed: fix: "who the Falsifiable Promise is made to". changed.

**FINDING-1349.** (H-34) [not changed in round 3] rule 5; resting on the reader. workflow *Stage 0 — Choose the Falsifiable Promise* (line 139-140): "the State Witness, checkable from outside, on state, never fires;". A State Witness is read; it does not fire. The worked example (38-39) says what is meant: "never above one". Proposed: fix: "the State Witness, read from outside on the stored state, never shows the Falsifiable Promise broken;". changed.

**FINDING-1350.** (H-35) [not changed in round 3] rule 5; resting on the reader. workflow *Stage 2 — Name the enemies* (line 222-224): "It is an Enemy Fact, not a deployment choice, when a line of the Enemy Census races them;". A line does not race; an Enemy Fact makes instances race. Also worked example 102-103 "since no line of the Enemy Census races two of us": 1 more. Proposed: fix: "when an Enemy Fact in the Enemy Census has them race"; "since no Enemy Fact has two instances racing". changed.

**FINDING-1351.** (H-36) [not changed in round 3] rule 5; checked. `evidence-test.md` *Why each rule is there* (line 166-168): "and a Decision Test is never counted as an Enemy Collision Kill." A test is never a kill; what is meant is that it is never counted as answering one. Proposed: fix: "never counted as answering an Enemy Collision Kill." changed.

**FINDING-1352.** (H-37) [changed in round 3] rule 8; resting on the reader. `evidence-test.md` *What this document controls* (line 28-30): "What it leaves out is *What is exempt, and why*." The sentence uses a heading as its object, and "it" stands two sentences from the Output Shape. Also `kill.md` 23-24, the same sentence; `registry-entry.md` 26 "are their own"; `slice-record.md` 22-23 "Every other section is the Invariant Slice's own, as long as it needs": 3 more. Proposed: fix: "What this Output Shape does not govern is listed under *What is exempt, and why*."; "are not this Output Shape's"; "Every other section's content and length are the Invariant Slice's to decide." changed, except the line-30 halves, unchanged.

**FINDING-1353.** (H-38) [not changed in round 3] rule 8; resting on the reader. workflow *The unit* (line 20): "Input: a standing idea, such as a need or a candidate problem." Line 3 says "a raw idea". Line 444 sets "a raw idea" against "an idea already shaped", and line 440 says "a standing idea" again. Framing SKILL 9 says "a standing project idea", while its description says "a raw project idea". The reader cannot tell whether "standing" means raw or shaped. Proposed: question: which is the input? Then one word for it in all five places. changed.

**FINDING-1354.** (H-39) [change not traced] rule 8; resting on the reader. workflow, places where the reader is not given what a word points at:
- 106 "as the concept chapter has them": which chapter;
- 109-110 "A letter is used only for a CBC Framing Concern that does not.": which letter, and how it is given; no example uses one;
- 169 "This is also where the boundary is.": Stage 1 sets the boundary;
- 188 "fails the standard": which standard;
- 341-342 "A System Possession whose every Enemy Fact is used by other Enemy Collision Kills": a System Possession has no Enemy Facts of its own;
- 371-372 "siblings refused at LAYER-2-SYSTEM": the worked example (202) says "sibling systems".

Proposed: fix: "as `docs/concept/01-layered-system.md` has them"; "is called by a letter, A, B and on"; "Stage 1 also sets the boundary."; name the standard or cut the clause; "A System Possession every Enemy Collision Kill of which is shared with another System Possession"; "sibling systems refused at LAYER-2-SYSTEM". changed.

**FINDING-1355.** (H-40) [not changed in round 3] rule 8; resting on the reader. framing SKILL *Export and handoff* (line 291): "System Readiness defines it". "It" has no clear antecedent: the handoff, or the project work between? Also framing SKILL 51 "recorded where the records put sign-offs"; 222-223 "Skipping the order departs from the default: log why." and 279 "logged", neither saying where; 272 "a note that points", not saying at what: 4 more. Proposed: fix: "System Readiness defines what must stand"; "in the record the records table names for sign-offs"; "log why in the Decisions Log" (or wherever the reviewer puts a departure); "a note that points at the method". changed, except 272, unchanged.

**FINDING-1356.** (H-41) [not changed in round 3] rule 8; resting on the reader. template *SLICE-1* slot (line 42-43): "created, or removed with the removal shown." What is removed, the adversity by a contract, is said only in slice SKILL 108-109. Proposed: fix: "created, or the adversity removed by a contract the Correctness Specification adopts, with the removal shown." changed.

**FINDING-1357.** (H-42) [change not traced] rule 8; resting on the reader. Lines the reader must decode:
- slice workflow 192-193 "a counter that over-approximates until a later Invariant Slice ends something";
- slice workflow 212-213 "a judgement the project makes when it makes it", where "it" could be the output or the Output Shape;
- slice SKILL 137 "is scope: refuse it";
- `evidence-test.md` 138-139 "A helper that may be refused returns the answer and asserts nothing. The helper a setup relies on calls it, and asserts.", where the request is refused, not the helper.

Proposed: fix: say what is ended; "when it makes that output"; "is scope beyond this Invariant Slice: refuse it"; "A helper whose request may be refused returns the answer and asserts nothing. A setup helper calls it, and asserts the answer it needs." changed, except `evidence-test.md` 138, unchanged.

**FINDING-1358.** (H-43) [not changed in round 3] rule 8; resting on the reader. worked example *Stage 2 — Name the enemies* (line 108-109): "fifty identical submissions racing at once, the hammering's own count." The hammering test first appears at line 273, in Part 2. At Stage 2 the reader does not yet hold it. Proposed: fix: "the count the evidence will use". changed.

**FINDING-1359.** (H-44) [not changed in round 3] rule 8; uncertain. `the-whole-system-in-plain.md` header (line 3): "No jargon: each Name is given once, beside its plain words." The page breaks its own promise. Falsifiable Promise (13), Structural Wall (15) and CBC Framing Intent (53) come with no plain words at first use. After Responsibility Areas is given at line 41, the page writes "part" and "owner" for them. Proposed: question: may a plain-words summary use plain words for a Name after giving it once, against rule 9? If not, the page writes the Names. Either way, plain words go beside the first use of the three. changed.

**FINDING-1360.** (H-45) [not changed in round 3] rule 8; uncertain. `evidence-test.md`, `kill.md`, `registry-entry.md`, `slice-record.md` frontmatter (line 2): "foundation: practice, under the shapes convention". In a CBC Run, neither "practice" nor "the shapes convention" can be looked up. The container's glossary lists no Foundation Line, and the CBC Run's other delivered files write the bare form ("foundation: the shapes convention", `shapes-lifecycle.md`). The form is our conventions manual's (§1.3), read by our Foundation Check. Proposed: question: is a Foundation Line read by the CBC Run? If it is, the container glossary gains Foundation Line, and "practice" is said in plain words. unchanged.

**FINDING-1361.** (H-46) [not changed in round 3] rule 8; uncertain. workflow *Stage 2 — Name the enemies* (line 241): "Two CBC Runs left it out and wrote it later." The reader cannot open those CBC Runs. Also the *Open (to be settled by CBC Runs)* section (444-454): "all six CBC Framings so far", "CBC Run 5's found two, CBC Run 6's three", "CBC Run 4's is not yet read". The count goes stale at the next CBC Framing, which may be the reader's own: 1 more. Proposed: question: keep the CBC Runs' evidence in a shipped file, with numbers no CBC Run can check? Or move it to our own records and leave the open questions alone. changed.

**FINDING-1362.** (H-47) [not changed in round 3] rule 6; checked. glossary *The concept's* (line 18-20): "**System Guarantee** — … Each is GUARANTEE-n where it is written." Line 185-187 gives the Invariant Slice Guarantee the same tag, "GUARANTEE-n". One tag kind names two Names, and DECISION-19's question 1 made them two Names. Proposed: question: which keeps GUARANTEE-n? In the method's files the tag is always the Invariant Slice Guarantee's. The System Guarantee's line may drop it, or take another tag kind. changed.

**FINDING-1363.** (H-48) [change not traced] rule 8; resting on the reader. glossary, entries that start by counting from the entry above them: 24 "**Escape Hatch** — the second:", 27 "the third", 30 "the fourth", 61 "**System Definition** — the second:", 63 "the third". A glossary entry is looked up alone, and "the second" then points at nothing. Proposed: fix: "the second way the concept fails:", "the second CBC Framing Export:", and so on. changed.

**FINDING-1364.** (H-49) [not changed in round 3] rule 6; resting on the reader. glossary *The method's* (line 186): "found by attacking it, stated without a strategy". Slice SKILL says "with no mechanism in it" (89-90). Two words for one thing. Proposed: fix: "stated without a mechanism". changed.

#### Reader I, Layer 6: the Stack Group

**FINDING-1365.** (I-1) [changed in round 3] rule 10; checked.
`cbc-bootstrap/references/spring-boot-walkthrough.md` *2. Stand the skeleton in the live repo* (line 47): "Stand the skeleton in the live repo". The title has 35 characters. The limit is 30. Proposed: fix: "2. Stand the skeleton" (18). Unchanged.

**FINDING-1366.** (I-2) [changed in round 3] rule 10; checked.
`infra-establish/references/postgres-setup-walkthrough.md` *5. Wire Flyway (config and empty migrations)* (line 110): "Wire Flyway (config and empty migrations)". It has 41 characters, and the parentheses hold a gloss. Proposed: fix: "5. Wire Flyway" (11). Changed.

**FINDING-1367.** (I-3) [not changed in round 3] rule 10; checked.
`infra-establish/references/postgres-setup-walkthrough.md` *7. Verify — both ways, always* (line 136): "Verify — both ways, always". A gloss follows a dash. Proposed: fix: "7. Verify both ways" (16). Unchanged.

**FINDING-1368.** (I-4) [not changed in round 3] rule 10; checked.
`infra-establish/references/postgres-setup-walkthrough.md` *6. Bring it up* (line 122): "Bring it up". Neither title stands alone without its parent heading. "It" names nothing. "Hand off" names no subject, and it reads like the CBC Run Hand-off. Also line 184 "9. Hand off": 1 more. Proposed: fix: "6. Bring the services up" (21); "9. The connection facts" (20), since the section mostly lists them. Unchanged.

**FINDING-1369.** (I-5) [not changed in round 3] rule 10; uncertain.
`infra-establish/references/postgres-setup-walkthrough.md` *1. Declare the service (compose)* (line 43): "Declare the service (compose)". The parentheses add a gloss. Rule 10 names only a gloss after a dash or a colon. Also line 58 "2. Split out credentials (`.env`)": 1 more. Proposed: question: does a parenthesis count as a gloss? If it does, "1. Declare the service" and "2. Split out credentials". Unchanged.

**FINDING-1370.** (I-6) [changed in round 3] rule 9; checked.
`cbc-bootstrap/SKILL.md` *Stage 0* (line 47): "## Stage 0 — System Readiness (refuse if not ready)". System Readiness is "the six checks a system passes before an Invariant Slice opens" (`delivery/method/docs/glossary/method.md`), with its home in cbc-slice's `system-readiness.md`. This Stage 0 runs three other checks, before the CBC Bootstrap. The round changed "readiness check" into the Name. Also `infra-establish/SKILL.md` line 31, "## Stage 0 — System Readiness (before anything else)": 1 more. Proposed: fix: "## Stage 0 — readiness (refuse if not ready)" and "## Stage 0 — readiness (before anything else)", the plain word. Changed.

**FINDING-1371.** (I-7) [changed in round 3] rule 9; checked.
`docs/glossary/stack.md` *CBC Bootstrap Probe* (line 28): "(`.claude/skills/cbc-bootstrap/SKILL.md`)". The entry points at a file that never defines the Name. `cbc-bootstrap/SKILL.md` uses the Probe 6 times but never says it is an endpoint and a test. `spring-boot-walkthrough.md` step 5 says it, and so does `spring-harness-reference.md` §4. Proposed: fix: point at `.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`. Or add one defining sentence to the SKILL's CBC Bootstrap Exclusion 1. Changed.

**FINDING-1372.** (I-8) [changed in round 3] rule 9; checked.
`docs/glossary/stack.md` *Stack Default* (line 87): "(`.claude/skills/infra-establish/SKILL.md`)". `infra-establish/SKILL.md` uses the Name once, in its description, and never defines it. The entry's general sense is in `establishment-walk.md` Stage 1 (lines 49-53). Its "packages by feature" half is in `app-structure.md` *The Stack Default*. Proposed: fix: point at `.claude/skills/infra-establish/references/establishment-walk.md` and `.claude/skills/cbc-bootstrap/references/app-structure.md`. Changed.

**FINDING-1373.** (I-9) [not changed in round 3] rule 9; checked.
`infra-establish/references/postgres-role-split.md` *(opening)* (line 8): "**this model wins.**". "The model" here means the Database Role Split. A CBC Run's reader also holds the Adversity Model, and nothing says which model is meant. Also `postgres-role-split.md` 30, 44, 53, 119, 128, 131: 6 more; `postgres-setup-walkthrough.md` 9, 27, 99, 104: 4 more; `templates/bootstrap.sql` 10, 35, 37: 3 more; `infra-establish/SKILL.md` 98 "the model's claims": 1 more; `docs/glossary/stack.md` 71 "what the model claims": 1 more. Proposed: fix: "the Database Role Split", or its path where a file is meant. Inside `postgres-role-split.md`, use "this reference". Changed, but for role-split 30 and bootstrap.sql 10.

**FINDING-1374.** (I-10) [not changed in round 3] rule 9, rule 5; checked.
`infra-establish/SKILL.md` *(opening)* (line 18): "The exit is the walk's Stage 7". "The walk" is both a figure (DECISION-26, the journey row: fix) and another word for Infrastructure Establishment (DECISION-19, the stack's table, row 31). Also `infra-establish/SKILL.md` 21, 66, 127, 147, 148, 159, 170, 193: 8 more; `establishment-walk.md` 1 (title), 5 "Two projects have walked it", 8, 22, 23, 123, 175, 185: 8 more; `postgres-setup-walkthrough.md` 22 "This walk": 1 more. Proposed: fix: "Infrastructure Establishment's Stage 7"; "the Infrastructure Establishment as done"; the file by its path, `establishment-walk.md`; "This walkthrough". Changed.

**FINDING-1375.** (I-11) [not changed in round 3] rule 9, rule 8; checked.
`cbc-bootstrap/references/spring-harness-reference.md` *(opening)* (line 7): "Three projects built them. The shape below is the third project's, the most corrected." "Project" here means a CBC Run. Lines 19 and 24 of the same file say CBC Run. The ordinals "second" and "third" also assume a numbered list that the reader does not hold. Also `spring-harness-reference.md` 25, 28, 30, 61, 146, 162, 213, 290, 432, 485, 494: 11 more; `infra-establish/SKILL.md` 29; `establishment-walk.md` 5; `postgres-setup-walkthrough.md` 4: 3 more. Proposed: fix: "Three CBC Runs built them. The shape below is the latest one's, the most corrected." Use "the latest CBC Run" for "the third project" and "an earlier CBC Run" for "the second project". Changed.

**FINDING-1376.** (I-12) [not changed in round 3] rule 9; checked.
`infra-establish/SKILL.md` *Records and outputs* (lines 154-155): "the sentence the log's first entry would have held. One CBC Run kept a log beside such records". The log meant here is the Infrastructure Establishment Log. In a repository with records, the decision is an ADR (the stack's table, row 19). Also `establishment-walk.md` 89 "It is one log entry." and 112 "the project's log entry stays"; `infra-serve/SKILL.md` 44 "a log entry, or an ADR": 3 more. Proposed: fix: "the Infrastructure Establishment Log's first entry"; "kept an Infrastructure Establishment Log beside such records"; "It is one ADR, or one Infrastructure Establishment Log entry"; "an Infrastructure Establishment Log entry, or an ADR in a repo with records". Changed.

**FINDING-1377.** (I-13) [not changed in round 3] rule 9; checked.
`infra-establish/SKILL.md` *Records and outputs* (line 151): "The expected results sit in the verify suite and the Operator". The stack's table, row 39, writes this file by its path. Also `infra-establish/SKILL.md` 169; `templates/bootstrap.sql` 38 "the verify suite's role filter"; `postgres-setup-walkthrough.md` 93, the title "4. Land the verification suite": 3 more. Proposed: fix: `infrastructure/postgres/verify-database-model.sql`. The title becomes "4. Land the Catalog Check" (21), since the file's header calls itself the Catalog Check. Changed, but for the setup walkthrough's title.

**FINDING-1378.** (I-14) [not changed in round 3] rule 9; checked.
`infra-establish/SKILL.md` *Stage 0* (line 51): "The facts are added by a dated revision entry". The method's Name for this is CBC Framing Export Revision. Also `establishment-walk.md` 22-23 "a dated revision entry in its LAYER-1-ENVIRONMENT": 1 more. Proposed: fix: "by a CBC Framing Export Revision in LAYER-1-ENVIRONMENT". Changed.

**FINDING-1379.** (I-15) [not changed in round 3] rule 9; checked.
`infra-establish/SKILL.md` *The walk and its Gates* (line 92): "No list of exclusions, no Stage 2.". Line 96 reads: "A constraint without enforcement is a wish." In infra-establish, rows 28 and 29 of the stack's table make these Infrastructure Service Constraint and Infrastructure Service Exclusion. Also `infra-establish/SKILL.md` 27 "which makes the constraint real"; `infra-serve/SKILL.md` 33-34 "the old exclusion's why", "the exclusion stands"; `establishment-walk.md` 106 "its constraint set", 116 "gets its constraints derived fresh", 121 "How a constraint is made real": 6 more. Proposed: fix: "No list of Infrastructure Service Exclusions, no Stage 2."; "An Infrastructure Service Constraint without enforcement is a wish."; the same at each line. Changed.

**FINDING-1380.** (I-16) [not changed in round 3] rule 9; checked.
`infra-establish/SKILL.md` *description* (line 3): "It requires the completed CBC Framing Exports (intent, definition, slice registry)." The three CBC Framing Exports are written in lowercase short forms. Proposed: fix: "(the CBC Framing Intent, the System Definition and the Invariant Slice Registry)". Changed.

**FINDING-1381.** (I-17) [not changed in round 3] rule 9; uncertain.
`cbc-bootstrap/SKILL.md` *description* (line 3): "continue a project that has a completed framing". The same paragraph also says "a completed CBC Framing". "Do NOT use for framing" names the work in lowercase too. Also `infra-establish/SKILL.md` 3, "Do NOT use for framing": 1 more. A description may keep the user's words for triggering, but neither phrase is in quotes. Proposed: fix: "a completed CBC Framing"; "for CBC Framing (the cbc-framing Agent Skill)". Changed.

**FINDING-1382.** (I-18) [changed in round 3] rule 9, rule 8; checked.
`infra-establish/references/establishment-walk.md` *The Names defined here* (line 207): "These three are the Stack Group's:". Stack Group is a Name in our `docs/glossary.md` only. No delivered Names file lists it, so a CBC Run cannot resolve it. Proposed: fix: "These three are the stack's, listed in `docs/glossary/stack.md`:". Changed.

**FINDING-1383.** (I-19) [not changed in round 3] rule 8, rule 9; checked.
`cbc-bootstrap/SKILL.md` *Stage 5* (lines 269-270): "The container's README has no Run or Test section.". "The container" is our Container Group, and the CBC Run's glossaries do not list it. In these files "container" mostly means a podman container: `spring-boot-walkthrough.md` 11, 180 and 185, `postgres-setup-walkthrough.md` 80 and 89. Also `infra-establish/SKILL.md` 139-140 "every project created from the container"; `establishment-walk.md` 198: 2 more. Proposed: fix: "The README this CBC Run was born with has no Run or Test section"; "every CBC Run". Changed.

**FINDING-1384.** (I-20) [not changed in round 3] rule 9; checked.
`infra-establish/references/postgres-setup-walkthrough.md` *9. Hand off* (line 225): "the project's **living Infrastructure Contract:**". By DECISION-22, a Name is bold at its home only, and this Name's home is `infra-establish/SKILL.md`. Also `establishment-walk.md` 140 and 143 "**Catalog Check:**", "**Behavioral Check:**"; `postgres-setup-walkthrough.md` 138 and 145, the same two; `infra-establish/SKILL.md` 9 "**Runtime Ground:**", whose home is `cbc-framing-workflow.md`; `spring-harness-reference.md` 445 "**State Witness,**": 6 more. Proposed: fix: drop the bold. Question on the bold list-item leads that begin with a Name (`cbc-bootstrap/SKILL.md` 45, 51, 54, 83, 103, 126; `infra-serve/SKILL.md` 19, 24, 25; `spring-boot-walkthrough.md` 184, 236, 240; `spring-harness-reference.md` 144, 160, 426, 516): does DECISION-22 reach a lead? Changed.

**FINDING-1385.** (I-21) [not changed in round 3] rule 9; checked.
`infra-establish/references/postgres-role-split.md` *The roles* (line 43): "*the Database Setup Identity:*". This is the Name's home, and it is marked in italics. DECISION-22 allows bold at the home, not another mark. Its sibling items, `migrator` and `runtime`, are bold. Proposed: fix: "**the Database Setup Identity:**". Changed.

**FINDING-1386.** (I-22) [changed in round 3] rule 9; checked.
`infra-establish/references/establishment-walk.md` *Stage 7* (line 191): "The skeleton is". This gives "skeleton" a third meaning: an Agent Skill Template. DECISION-19 (method, question 6) leaves "skeleton" English for the running service, and Skeleton a label for an Output Shape's layer. Also `spring-boot-walkthrough.md` 86 "The config skeleton is an Agent Skill Template": 1 more, uncertain. Proposed: fix: "The Agent Skill Template is"; "The config file is an Agent Skill Template". Changed.

**FINDING-1387.** (I-23) [changed in round 3] rule 9; checked.
`cbc-bootstrap/references/app-structure.md` *The Stack Default* (lines 64-65): "Which test proves which guarantee is the Invariant Slice Record's.". The Invariant Slice Record holds Invariant Slice Guarantees, and here the word is lowercase. Also line 39 in the drawing, "reads the code: a guarantee held by an absence"; `spring-pom-convention.md` 25 "which boundary or guarantee it serves": 2 more. Proposed: fix: "which Invariant Slice Guarantee" in all three. The drawing's line has room. Changed, but for line 39.

**FINDING-1388.** (I-24) [not changed in round 3] rule 9; uncertain.
`infra-establish/references/establishment-walk.md` *Stage 7* (line 199): "because this Gate made it true.". "Gate" stands capitalized alone, and a CBC Run also holds Plan Step Gate. `docs/glossary/stack.md` 75 "the infra-establish Agent Skill's Stage 5 gate" lowercases the label "Stage 5 Gate". Also `infra-establish/SKILL.md` 66, the heading "The walk and its Gates". Proposed: fix: "because the exit test made it true"; the glossary entry writes "Stage 5 Gate", keeping the label's case. Question: may the Stage labels "Stage 1 Gate" to "Stage 6 Gate" stand beside Plan Step Gate? Changed.

**FINDING-1389.** (I-25) [changed in round 3] rule 9; checked.
`infra-serve/SKILL.md` *Hard lines* (line 87): "One logical change per delivery the size of a commit". In a CBC Run, a delivery is the Concept Deliverer's: Delivery Note, Delivery Staging. Also `cbc-bootstrap/SKILL.md` 138 "where a forgotten export becomes a real need", which uses a shell export beside CBC Framing Export: 1 more. `cbc-bootstrap/SKILL.md` 132 "no delivery machinery" is uncertain. Proposed: fix: "6. One logical change per commit, with a commit message drafted for each."; "where a secret nobody exported becomes a real need". Changed.

**FINDING-1390.** (I-26) [not changed in round 3] rule 9; uncertain.
`cbc-bootstrap/references/app-structure.md` *The Stack Default* (line 37): "races, bursts of duplicates, kills". These words are bases of Names, used here in other senses:
- "kills" means killed processes, beside Enemy Collision Kill;
- `cbc-bootstrap/templates/application.yaml` 29, "not just folded into the status", beside Invariant Slice Fold;
- `spring-harness-reference.md` 473, "The `filesystem:` prefix is the invariant; the path is not.", where invariant means the fixed part;
- `spring-harness-reference.md` 223, 275, 297, 299, "the copy", meaning the test database, beside pinned copies;
- `cbc-bootstrap/SKILL.md` 9, "One run, one exit", beside CBC Run.

That is 8 more. Proposed: fix: "killed processes"; "merged into the status"; "is fixed"; "One pass, one exit". Keep "the copy", defined at line 45. Changed, but for application.yaml 29.

**FINDING-1391.** (I-27) [not changed in round 3] rule 9; uncertain.
`cbc-bootstrap/references/spring-harness-reference.md` *1. The database base* (line 99): "MIGRATIONS_HOME". CBC Runs imitate this code, and its identifiers carry words the stack's table changed:
- "home" (row 11): `MIGRATIONS_HOME` here, and `GROUND_BOOTSTRAP_SQL` at line 97;
- "probe" alone (row 5): `GroundProbeController` and `/probe/ground` at 336 and 344, and the role `probe` in `postgres-setup-walkthrough.md` 158-161;
- "bootstrap" for the setup (row 35, question 1): `POSTGRES_BOOTSTRAP_PASSWORD` in `templates/.env.example` 12 and `templates/compose.yaml` 15.

Proposed: question: do the Names reach code identifiers? If they do: `MIGRATIONS_DIRECTORY`, `SETUP_SQL`, `BootstrapProbeController`, the role `no_grant`, `POSTGRES_SETUP_PASSWORD`. Unchanged.

**FINDING-1392.** (I-28) [not changed in round 3] rule 9, rule 8; uncertain.
`cbc-bootstrap/SKILL.md` *The boundary you must keep* (line 29): "under the stack conventions in `references/`". These are references, not conventions. In a CBC Run, "convention" is what arrives in the Decisions Log (the container's records table: "a convention arrives"). Since DECISION-32, a CBC Run holds approaches made from conventions, never conventions. Also `cbc-bootstrap/SKILL.md` 194; `app-structure.md` 22 "the POM convention's"; `spring-boot-walkthrough.md` 66 "The pom is written by the POM convention,"; `spring-pom-convention.md` 1, its title; `spring-harness-reference.md` 527 and 529 "the convention"; `infra-establish/SKILL.md` 135 "The repo's own conventions win.": 7 more. Proposed: fix: "under the stack references in `references/`"; "`spring-pom-convention.md`'s"; "the rule" in the harness reference; "The repo's own records win." The file's name stays, being a path. Changed, but for the pom file's title.

**FINDING-1393.** (I-29) [changed in round 3] rule 6; checked.
`cbc-bootstrap/references/spring-harness-reference.md` *4. The CBC Bootstrap Probe* (line 410): "(variation point 9), never by substring.". This code comment is imitated into a CBC Run's test, where "variation point 9" has no owner. Also `establishment-walk.md` 20 "(Stage 0 in SKILL.md)": a CBC Run holds several SKILL.md files: 1 more. Proposed: fix: "(spring-harness-reference.md, variation point 9)"; "(Stage 0 in `.claude/skills/infra-establish/SKILL.md`)". Unchanged; the establishment-walk line changed.

**FINDING-1394.** (I-30) [not changed in round 3] rule 8; checked.
`cbc-bootstrap/SKILL.md` *Stage 0* (line 57): "and the Runtime Ground's stand-up check is recorded". No "stand-up check" exists in infra-establish. Its Stage 5 records the Catalog Check and the Behavioral Check. Proposed: fix: "and its Catalog Check and Behavioral Check are recorded". Changed.

**FINDING-1395.** (I-31) [not changed in round 3] rule 8; resting on the reader.
`cbc-bootstrap/SKILL.md` *Stage 0* (lines 66-67): "Only a missing member stops; a note goes in the record.". The text never says which members it means, or which record. Proposed: fix: "Record what stood, what was checked and what was noticed, in the devlog's entry for the Plan Step. Only a failed check 1 to 3 stops. Anything else is a note." Changed.

**FINDING-1396.** (I-32) [not changed in round 3] rule 8; resting on the reader.
`cbc-bootstrap/SKILL.md` *Stage 1* (line 137): "The release Plan Step Gate's clean-machine test is". The reader holds no release Plan Step and no clean-machine test from this text. Proposed: fix: "The question comes back at release, when a test on a clean machine shows whether a missing secret matters." Changed.

**FINDING-1397.** (I-33) [not changed in round 3] rule 8; resting on the reader.
`cbc-bootstrap/references/spring-harness-reference.md` *1. The database base* (line 153): "The migrate call plays the **compose one-shot's role** against the". The compose one-shot is described in infra-establish's setup walkthrough, §1, which a cbc-bootstrap reader may not have read. Also line 474 "The credential rule decides the wiring.": no rule has that name: 1 more. Proposed: fix: "The migrate call does here what the `flyway` service in `compose.yaml` does on the Runtime Ground"; "How credentials are handled decides the wiring." Unchanged.

**FINDING-1398.** (I-34) [not changed in round 3] rule 8, rule 5; resting on the reader.
`infra-establish/SKILL.md` *Records and outputs* (lines 166-167): "the stranger's first command finds them there". "The stranger" is a figure the text never explains. Also `establishment-walk.md` 189 and 190; `templates/readme-prerequisites.md` 7: 3 more. Proposed: fix: "the first command of someone new to the repo"; "a new machine". Changed.

**FINDING-1399.** (I-35) [not changed in round 3] rule 8; uncertain.
`infra-establish/references/establishment-walk.md` *(opening)* (line 3): "The method, end to end. It is generic throughout.". In a CBC Run, "the method" is the concept's method: the cbc-framing and cbc-slice Agent Skills. This file is Infrastructure Establishment's stages. Proposed: fix: "Infrastructure Establishment, Stage 0 to Stage 7. It is generic throughout." Changed.

**FINDING-1400.** (I-36) [not changed in round 3] rule 8; resting on the reader.
`cbc-bootstrap/SKILL.md` *Stage 2* (line 145): "Write `bootstrap-requirements.md` in the project's language". The text does not say whether this is the prose language or the programming language. Also `infra-serve/SKILL.md` 86 "Project files are written in the project's language.": 1 more. Proposed: fix: "in the language the project's records are written in". Changed.

**FINDING-1401.** (I-37) [changed in round 3] rule 2; resting on the reader.
`cbc-bootstrap/references/spring-harness-reference.md` *1. The database base* (lines 165-170): "Boot 4 moved Flyway's auto-configuration into its own module; with". This is one sentence of 56 words, joined by a semicolon. Proposed: fix: "Boot 4 moved Flyway's auto-configuration into its own module. With only `flyway-core` and `flyway-database-postgresql` on the test classpath, no auto-configuration runs inside the application context. So the `static` call above is the only migration path in tests." Unchanged.

**FINDING-1402.** (I-38) [not changed in round 3] rule 2; resting on the reader.
`infra-establish/references/postgres-role-split.md` *The roles* (lines 45-46): "it creates the database, and owns it, the two roles, the application schema, and the grants.". It can be read as owning the schema, which is `migrator`'s (line 33). Proposed: fix: "It runs the setup once. It creates the database, the two roles, the application schema and the grants. It owns the database." Changed.

**FINDING-1403.** (I-39) [not changed in round 3] rule 2; resting on the reader.
`cbc-bootstrap/references/spring-boot-walkthrough.md` *5. The adversity created* (lines 286-287): "closed in `finally`, destroyed and then forcibly, none left running on a failed test.". The phrase "destroyed and then forcibly" has no verb for its second half. Proposed: fix: "Instances start before the race. A `finally` block destroys each one, and forcibly if it is still alive. None is left running when a test fails." Changed.

**FINDING-1404.** (I-40) [changed in round 3] rule 2, rule 3; resting on the reader.
`infra-establish/references/establishment-walk.md` *Stage 1* (lines 38-41): "What the evidence must be able to do to the Runtime Ground, start several instances, kill one, freeze the store, is proven where". A list sits inside the subject. Also `postgres-setup-walkthrough.md` 198-199 "Then the Invariant Slices cannot tell whether that reader can write, and must be defended against.": the subject of "must be defended against" is unclear: 1 more. Proposed: fix: "The evidence must be able to start several instances, kill one and freeze the store. Each is proven where the Adversity Harness that does it is built, in the form it does it:"; "...whether that reader can write, so they must defend against one who does." Changed.

**FINDING-1405.** (I-41) [not changed in round 3] rule 3; checked.
`cbc-bootstrap/references/spring-boot-walkthrough.md` *Recall list* (lines 308-309): "`@AutoConfigureTestRestTemplate` required — `RANDOM_PORT` alone provides no `TestRestTemplate` bean.". The list joins its parts with dashes and semicolons. Also items 1 (305-306), 5 (313), 6 (316), 9 (322), 10 (324), 11 (326): 6 more. Proposed: fix: one fact per sentence, for example "`@AutoConfigureTestRestTemplate` is required: `RANDOM_PORT` alone provides no `TestRestTemplate` bean." Unchanged, but for 316 and 324.

**FINDING-1406.** (I-42) [not changed in round 3] rule 3; checked.
`infra-establish/templates/bootstrap.sql` *Purpose* (line 11): "— this file makes it real, and never derives it again.". The template comments join their parts with dashes. Also `bootstrap.sql` 14, 16, 20, 22, 45, 55, 60: 7 more; `templates/.env.example` 7, 21: 2 more; `templates/readme-prerequisites.md` 5 and 11: 2 more; `templates/compose.yaml` 28: 1 more. Proposed: fix: a colon or a full stop at each. Mostly unchanged; bootstrap.sql 11, 14, 45 and 55 and readme-prerequisites 5 changed.

**FINDING-1407.** (I-43) [not changed in round 3] rule 5; checked.
`cbc-bootstrap/templates/readme-run-test.md` *header* (line 5): "Only the material below travels; this header stays with the". DECISION-26's journey row fixes "travels". Also `infra-establish/templates/readme-prerequisites.md` 5: 1 more. Proposed: fix: "Only the material below is merged; this header stays with the Master Copy." Changed.

**FINDING-1408.** (I-44) [not changed in round 3] rule 5; checked.
`cbc-bootstrap/references/spring-harness-reference.md` *What these files are* (line 48): "scaffolding, dies at the first Invariant Slice". DECISION-26 fixes "dies" when it is said of scaffolding. `docs/glossary/stack.md` 27 already says "both go". Proposed: fix: "scaffolding, deleted at the first Invariant Slice". Changed.

**FINDING-1409.** (I-45) [not changed in round 3] rule 5; resting on the reader.
`infra-establish/references/postgres-role-split.md` *The grant boundaries* (line 92): "cannot wear away one migration at a time". The other figures:
- `postgres-setup-walkthrough.md` 87, "cannot wear away";
- `templates/bootstrap.sql` 61, "cannot erode";
- `postgres-role-split.md` 115-116, "rules nothing enforces decay", and 59, "everything hangs off that ownership";
- `spring-boot-walkthrough.md` 142, "A CBC Run lost a long search to the";
- `app-structure.md` 120, "and it earned that";
- `infra-establish/SKILL.md` 57, "plumbing dotfiles".

That is 7 more. Proposed: fix: "cannot stop holding, one migration at a time"; "rules nothing enforces stop being kept"; "everything follows from that ownership"; "A CBC Run searched long for the cause of"; drop "and it earned that"; "hygiene files", the cbc-bootstrap Agent Skill's word. Changed, but for bootstrap.sql 61.

**FINDING-1410.** (I-46) [not changed in round 3] rule 9; checked.
`infra-establish/SKILL.md` *The walk and its Gates* (line 69): "0: ready? → 1: environment → 2: services   → 3: constraints → 4: the reference". DECISION-21 extends rule 9 to drawn text. The drawing's "environment", "services", "constraints" (line 69) and "contract" (line 72) are short forms of Names, and no line above says which Name each stands for. Proposed: fix: one line above the drawing: "environment: the Execution Environment; services: the Infrastructure Services; constraints: the Infrastructure Service Constraints; contract: the Infrastructure Contract and the Operator Manual." Changed (line 69; line 72 unchanged).

### Met at the close read, of other kinds

#### Reader A

- `docs/conventions/conventions/README.md` *What this is made usable as*: §2.3 asks each entry for "the moment it opens at". The Foundation Line entry (28–29) and the index entry (32–35) give none.
- `docs/conventions/conventions/README.md` *Why it arrives this way* (324–326): "in the frontmatter of every shipped Agent Skill and Agent Rule". §1.3 also puts it in this repo's own files, shipped Output Shapes and manuals on an Idea Model, and in a record's header comment, which is not frontmatter.
- `docs/conventions/conventions/README.md` §1.2's frontmatter template (line 90), `foundation: the <name> convention`, fits only a convention's Agent Skill. §1.3 gives method Agent Skills `concept v1` and stack ones `practice, checked against concept v1`.
- `docs/conventions/project-recording/README.md` §13 (784–786): "the only part of the project-recording manual loaded before any task". The records table is in the Entry File, not in the manual. `docs/conventions/conventions/` §2 says a manual is never loaded into an agent.
- `docs/conventions/project-recording/README.md` §3.3 (290) states the PLAN.md Decision index for every repo. Item 4 of *The Concept Deliverer's seat* says the Concept Deliverer has none, and §3.3 does not say the index is the CBC Run's.
- `docs/conventions/project-recording/README.md` §2.4 (252–254), "The look back is not the plan's: `RETRO.md`", is stated for both Convention Seats. Line 154 says the Concept Deliverer has no `RETRO.md`.

Counts: 44 entries: 19 in the conventions manual, 25 in the project-recording manual. By rule: rule 2, 12; rule 3, 5; rule 5, 3; rule 6, 2; rule 8, 11; rule 9, 10; rule 10, 1. By state: 21 changed, 7 changed in part, 16 unchanged. The script sweep's 1 line is not a finding. Met in passing: 6.

#### Reader B

- `docs/conventions/facts-in-sync/README.md` §1: the glossary says Living Text's home is this section. Lines 94–102 use the word but never define it.
- `docs/conventions/facts-in-sync/README.md` line 127 cites claim P1 under `docs/models/agent.md` §4.2, *Pulled Channel*. P1 sits in §12.2, *On the Pulled Channel* (agent.md line 318), as line 179 of the same file cites it.
- `docs/conventions/agent-arrangement/README.md` lines 91–94 and 326 say a CBC Run's birth entry "lists the conventions it holds". DECISION-32 says a CBC Run holds no convention, only Work Approaches made from ours.
- `docs/conventions/agent-arrangement/README.md` line 382: "(the Plan Step Form)" stands as a Fact Reference with no path. The form is in `PLAN.md`.
- `docs/conventions/commit-plan/README.md` §2.7, §2.9 and §2.12 (lines 110–113, 126–127, 158–159): the italic line still tells the case instead of pointing at its story. Round 3's *Met in round 3* listed this, and it still stands.
- `docs/conventions/commit-plan/README.md` §2.10 (lines 136–138): "a manual wraps its prose". Since ADR-0077, Markdown has no line width. The reason holds for older text only.
- `docs/conventions/exchange/README.md` §6.1 (line 479): "the diff of every held copy against its Delivery Pin". The Delivery Pin is our commit, which the CBC Run's diff cannot name. §3.8 (lines 316–317) and the exchange-read Agent Skill compare against the CBC Run's own last delivery commit.
- DECISION-29's reversal says the strip runs "before `exchange-read` compares". `docs/conventions/exchange/README.md` §3.8 says a read needs no strip, and the exchange-read Agent Skill strips nothing. The manual matches the Agent Skill, not the decision's wording.

53 entries. By rule: rule 2, 5; rule 3, 3; rule 5, 3; rule 6, 2; rule 8, 20; rule 9, 19; rule 10, 1. Changed 31, unchanged 22.

#### Reader C

- `docs/conventions/writing/README.md` §1 line 65: "History keeps its words" names three kinds of history. The one-home Agent Rule's *Not a second home* names more: the decisions log entries and Conversation Memory parts, and, by DECISION-18, a released CHANGELOG entry. The two lists disagree.
- `docs/conventions/writing/README.md` line 122 ("none marks a Name") and the writing Agent Rule's rule 9 still forbid bold on a Name. DECISION-22 allows it at the home, and the line is due at the round's close.
- `docs/conventions/writing/README.md` rule 10 (lines 141-149) does not say that a comma gloss counts (DECISION-20). Its list of non-titles names an Agent Skill Stage heading but not an Approach on Trial Stage heading, which DECISION-20 also put outside the rule.
- `docs/conventions/writing/README.md` line 162: the *Its story* line cites "devlog 2026-10-29" twice and does not cite ADR-0078, which changed rule 9. *Where to look* (line 198) names ADR-0053 only.
- `docs/conventions/writing/README.md` line 154: "985 lines in 83 of the 99 living files" is a count from before the round. It is likely stale; not checked.
- `docs/conventions/visual-comparison/README.md` line 53: "Its name is the question, not a candidate: *how is this shown*". The convention and its Agent Skill are named visual-comparison, which names a picture. The claim does not match the name.
- `docs/conventions/shapes/README.md` line 299: "Any change is shown before it is made." has no blank line before it, so Markdown renders it inside the fourth bullet.
- `docs/conventions/shapes/README.md` line 33: "instances of this convention". By DECISION-32 the Output Shapes are Work Approaches made from a convention, not instances of it.
- `docs/conventions/repo-hygiene/templates/java-spring/editorconfig.part` line 3 marks "# --- java-spring Stack Overlay ---". The other two `.part` files mark "# --- java-spring (Maven) Stack Overlay ---…".
- `docs/conventions/repo-hygiene/README.md` says "the Plan Step that makes the stack true". The Hygiene Base's three marker lines say "at app bootstrap". The playbook calls it "Step 4: CBC Bootstrap". These are three wordings for one moment.
- `docs/glossary.md` line 44: Newborn CBC Run runs "until its agent finishes the CBC Run Birth", and `docs/conventions/retrospective/README.md` line 86 says "runs the next CBC Run Birth". The glossary defines CBC Run Birth as "a CBC Run's first state", not an act.

#### Reader D

- `docs/models/agent.md` §10 (line 252): "One mechanism may serve two channels", but its example pairs a channel with the Enforcement Gate, which is not a channel.
- `docs/models/agent.md` G1 (line 423) says the rule was broken 15 times "for the whole life of the handbook". A1 (line 293) counts 15 in the handbook's first 20 commits.
- `docs/models/agent.md` W2 (line 387) cites "three CBC Runs" and gives two incidents.
- `docs/models/agent.md` M2 (line 416) is "`evidenced` (definitional)", while line 275 defines `evidenced` as observed.
- `docs/models/agent.md` §9 (line 234) gives an Agent Skill to "a rule bound to a moment", which §8's table gives to the Pushed Channel. A1 (line 292) calls an Agent Skill the Pulled Channel.
- `docs/models/idea-to-output.md` §2 (line 40): `.claude/shapes/` does not exist in this repo. The Output Shapes are at `delivery/method/.claude/shapes/`.
- `docs/models/tiers.md` §4.2 (line 160), "Downward: only pinned copies", leaves out the Delivery Fill, which §3.1 gives as the second downward form.
- `docs/models/tiers.md` §3.2 (line 102), "an edit goes up", against §3.5 fact 5, "Nothing moves up as files".
- `concept/00-cbc.md` (lines 112-120): "five practices" and "five phases", but the list of gaps has four, and design-before-code has none (D-46).

#### Reader E

- `ARCHITECTURE.md` §2.5: CBC Run 6's state, "born 2026-10-29 at `657d372`, on full auto", is out of date. `TODO.md` 38-39 says it ran through its Release, Step 14, and closed a Step 15.
- `ARCHITECTURE.md` header comment, line 13: "the live CBC Run" is singular, but the table has more than one CBC Run since it was written.
- `README.md` 16: "a repo of its own pinned to a concept version". A CBC Run records a Delivery Pin, a commit (glossary; `TODO.md` 932, "A CBC Run pins a commit"). It is an Agent Skill's Foundation Line that pins a concept version.
- `TODO.md` 537: "ADR-0078 when written". ADR-0078 exists.
- `TODO.md` 1011-1019, "Give the method a glossary": `delivery/method/docs/glossary/method.md` exists now (ADR-0078), so "the method has none" is false.
- `TODO.md` 396-402: the item lists three links, "derives, points, governs". The glossary's Chain Links are four: stands on, points, governs, written from.
- `TODO.md` 694, 747 and 431-432 wait on "the next birth". CBC Runs 5 and 6 have been born since.
- Triggers that look passed:
  - `TODO.md` 95, 113, 185, 198, "CBC Run 5's CBC Run Reading": it exists, `temp/reading-run-5-2026-10-22.md`, per `PLAN.md` 157;
  - `TODO.md` 681 and 922-923, the close of the Plan Step for CBC Run 5's birth;
  - `TODO.md` 736, "CBC Run 5's first Invariant Slice closing": CBC Run 5 is through Release;
  - `TODO.md` 307-308 and 771-772, waiting on Refinement Round 2, which has closed.
- `TODO.md` 818-820: "once the settled form is written there". `docs/conventions/facts-in-sync/` §3.1 now holds the one form.
- `TODO.md` 906-907, "only some say": FINDING-591's count was not worked, so the rule 4 gap stays open.
- `TODO-CONVERSATION-MEMORY.md` §7, §8 and §26: no TODO item and no other living record points at them, though the header says the item's See names each section.
- `devlog/README.md` 9-10, "fragments fine", follows project-recording §4 (its line 364). `.claude/rules/writing.md` *Where it applies* puts every new record line under the rules. The two disagree.
- The glossary's Agent Skill Stage entry and DECISION-25 write "`cbc-slice`'s Stage 3". Conventions §1.5 and DECISION-27 ask for the kind word every time.
- `ARCHITECTURE.md` 78: the list item's second line starts at column 0. It renders by lazy continuation, but in the source it looks like it is outside the list.
- `PLAN.md` 238: the ticked item starts in lowercase, "the Exchange Convention says". All the others start with a capital.

#### Reader F

- `approach-drafting.md`: byte-identical. Its findings, FINDING-1222 (line 70), FINDING-1231, FINDING-1232, FINDING-1252, hold for both.
- `commit-messages/SKILL.md`: identical. FINDING-1253 holds for both.
- `visual-comparison/SKILL.md`: one difference, §5, written for the seat. FINDING-1234, FINDING-1237, FINDING-1248, FINDING-1250 hold for both.
- `commit-plan/SKILL.md`: differs beyond the seat, FINDING-1256.
- `writing.md` and `one-home.md`: every difference is the seat's (examples, the glossary's place, the CBC Run's Fact Reference by id, footers). FINDING-1228 holds for both.

- The round's read said our `commit-plan` differs from the container's only as ADR-0069 allows. Since `31156de` that is no longer true (F-35).
- Living Text's home, facts-in-sync §1 per the glossary and DECISION-23, still writes "living text" in lowercase and never defines it. The only definition, in bold, is `refinement.md` §1.1 (F-5).
- Foundation Line values spell Names in lowercase: `the exchange convention`, `the agent model`, `the tiers model`, `the idea-to-output model`. The form is conventions §1.3's, a question for Refinement Layer 1, not for these files.
- `working-a-reading.md`'s Foundation Line, `practice, under the exchange convention`, uses the form §1.3 gives for an Output Shape, not the one for a convention's Work Approach.
- The Foundation Check's step 1 lists where Foundation Lines sit and says "Only these are checked". It misses the delivered Glossary Names files, `delivery/*/docs/glossary/*.md`, which carry one in their header comment.
- `exchange-read`'s Agent Skill Stage headings capitalize after the dash ("Find where to start"), and `exchange-deliver`'s do not ("write the Delivery Note"). Conventions §1.4's example is lowercase. Both skills number from Stage 1, while §1.4 and the glossary say "numbered from Stage 0".
- `exchange-read`'s opening says "the fourth writes a document", but Stage 2 already writes its first line.
- `exchange-deliver`'s step 6 has no bold lead, while steps 0 to 5 and 7 to 9 do.
- Due at the round's close and not yet in: DECISION-22's home-bold line in writing rule 9 ("no Markdown mark marks a Name" stands bare), and DECISION-18's released CHANGELOG entry in one-home's *Not a second home*.
- `approach-drafting.md`'s "The refinement is open." (both copies) goes stale at the close, as round 3's read already noted.

#### Reader G

- `delivery/container/.claude/skills/commit-plan/SKILL.md` differs from our `.claude/skills/commit-plan/SKILL.md` in 24 hunks. Our copy got the round's fixes in `31156de`, and the shipped one did not (G-52 to G-55). The pair is not a copy kept in step.
- `delivery/container/.claude/decisions.md` lines 39–40, "Their decisions are cited CBC ADR-nnnn": since ADR-0078, every delivery strips the footers. A CBC Run now meets no `CBC ADR-nnnn` in any shipped file, and grep finds none outside the footers.
- `delivery/container/.claude/decisions.md` lines 35–37 ("Conventions: …"), `.claude/CLAUDE.md` line 54 ("a convention arrives", "the conventions held"), and the Pure Seed's prompt and commit subjects (lines 131, 213, 228, 291, "conventions") say a CBC Run holds conventions. DECISION-32 says it holds none, only the Work Approaches made from them.
- `delivery/container/.claude/rules/delivered-copies.md` rule 5 has no Receipt Branch step. `docs/conventions/exchange/` §4, step 3, has the CBC Run cut one, optionally, so step 2's diff is exact. `container.md` has no Receipt Branch entry.
- `delivery/container/.claude/rules/delivered-copies.md` line 21–22: "these copies equal, but for its *Decisions* footers". "Its" has a plural antecedent.
- `delivery/container/.claude/decisions.md` lines 21–22, "The Delivery Pin is the Concept Deliverer's commit every copy here equals", drops "but for its *Decisions* footer", which `container.md` and `delivered-copies.md` rule 1 carry. Round 3 met it as a second home, and it still stands.
- Round 3's in-passing items still stand: `shapes-lifecycle.md` line 73, "Either of the last three"; `apply-retrospective/SKILL.md` lines 88–89, "Links point at labels, never section numbers", against `one-home.md` rule 2; `retrospective/SKILL.md` lines 114–115 ("rules in force now" list on top) against the Decisions Log's "Append-only, newest last"; `retrospective/SKILL.md` line 118 (the Concept Deliverer writes the next CBC Run's `PLAN.md`) against the playbook line 87–88 and the Pure Seed lines 3–4; `PLAN.md`'s placeholder Plan Steps have no "Now:" line; `visual-comparison/SKILL.md` line 127's unindented bullet continuation.
- `delivery/fills/cbc-run-pure-playbook.md` line 192: "## Steps 5..N-3" has no status box, where every other Plan Step heading has one.
- `delivery/fills/cbc-run-pure-playbook.md` line 70, "the stages its Notes list from earlier CBC Runs": a Newborn CBC Run holds nothing from earlier CBC Runs (`delivery/installs/pure-seed.md` line 29).
- `delivery/installs/pure-seed.md` line 158 adds `.claude/skills .claude/shapes docs/glossary` but not `.claude/rules`. Today no file of the Method Group or the Stack Group is under `.claude/rules/`, but `delivery/README.md` lines 33–34 says those groups carry Agent Rules.
- `delivery/installs/pure-seed.md` lines 9–10, "finishes the CBC Run Birth", against the glossary's "a CBC Run's first state". Round 3 met it in passing, and it still stands.

#### Reader H

- Enemy Census Saturation is still stated in three units: framing SKILL 101-102 "two consecutive fresh Enemy Census Probes", workflow 291 "two consecutive ones" (the lenses), `the-whole-system-in-plain.md` 62-63 "two fresh attacks". The glossary (122-124) says Enemy Census Probes.
- The workflow names three Enemy Census Probe Lenses (248-267) but calls the first listing, "actors × the three negations" (244), a lens too, so the count is three or four. The glossary says "the workflow names three".
- The evidence label still differs: `evidence-test.md` 47 and 81 write "· GUARANTEE-3 — KILL-3" with a dash; slice SKILL 97 and 185 write "· GUARANTEE-2 · KILL-12" with a middle dot.
- `kill.md` 83 "FACT-CALLER-1 to FACT-STORE-6": a range over the tags of four different actors.
- `kill.md` 105-108: the illustrated "nothing dies" Enemy Collision Kill starts with NOT-OURS-1, a Scope Exclusion, where the Skeleton (60-61) says it starts with the Enemy Fact.
- When an Output Shape is read: the four Output Shapes' headers say "Read at … Plan Step Gate", while slice workflow 40 says the Invariant Slice Record Shape "is read at the Invariant Slice Close".
- Worked example 247 puts "the CBC Framing Concerns" in LAYER-4-PROBLEMS, while Stage 3 (framing SKILL 61, `kill.md` 8) puts the Enemy Collision Kills there.
- Worked example 115-123 leaves two of the three lists the workflow says the exit leaves (298-317); no Scope Verdicts list, not even an empty one.
- The System Possession Test reads three ways: framing SKILL 85-86 and the glossary 98-99 "could they break the Falsifiable Promise?", workflow 156-157 "… without us being able to stop them?".
- The Structural Wall ladder: slice SKILL 117 "single validated entry path", `the-whole-system-in-plain.md` 97 "single checked entry path"; concept chapter 02 has both (50, 62).
- Slice SKILL 233 says "`ARCHITECTURE.md`'s Invariants table"; slice workflow 201 says "the Invariants section's own comment". The container's `ARCHITECTURE.md` has a section `## Invariants`.
- "judgement" (slice workflow 213) against "judgment" everywhere else ("Judgment logged").
- The workflow's *Open* section (453) says "CBC Run 4's is not yet read", which may be stale against the records.
- The four Output Shapes' "did each have something" (`evidence-test.md` 193, `kill.md` 130, `registry-entry.md` 114, `slice-record.md` 228) asks after the shapes-lifecycle Agent Rule's §3 ending "Each had something". It reads only with the Fact Reference that follows it, which it has.
- No numbered section stands in these 14 files, so rule 10 found nothing.

#### Reader I

- `establishment-walk.md` Stage 4 (lines 123-127) tells a CBC Run to write a new reference beside `postgres-role-split.md`, inside a pinned copy's folder, "so no later project derives it again". `.claude/rules/delivered-copies.md` allows a copy to change only by its rules, and only the Concept Deliverer can carry it to later CBC Runs.
- `establishment-walk.md` 170 says "It is the home of the Runtime Ground's own words", and 206 says "The project's Infrastructure Contract is where it writes its own words". The container's records table puts a CBC Run's own Names in `docs/glossary.md`.
- The Catalog Check checks against three differently named things: "the model's claims" (`infra-establish/SKILL.md` 98), "the reference's claims" (`establishment-walk.md` 141) and "the claims of postgres-role-split.md" (`verify-database-model.sql` 10-11).
- `spring-pom-convention.md` *What the file does not carry* (57-62): two of its three bullets still say what the file does carry, as round 3 met.
- The default-privileges sentence still has three homes: `postgres-role-split.md` 89-94, `postgres-setup-walkthrough.md` 84-87, `bootstrap.sql` 59-61.
- `app-structure.md` 80-83 sends a departure from the Stack Default, which is a reference's choice, to delivered-copies rule 8, which governs Agent Skill Templates. It fits only by analogy.
- `cbc-bootstrap/SKILL.md` 147 says "Both CBC Runs that ran this Agent Skill", while `spring-harness-reference.md` 7 says "Three projects built them". Two or three; the difference is never explained.
- `spring-boot-walkthrough.md` 263 spells "honours", while `establishment-walk.md` 13 spells "honor" and the stack's files spell "behavior".
- `infra-establish/SKILL.md`'s drawing labels Stage 6 "contract", while its Stage 6 Gate asks that both manuals stand.

### The close read's counts

485 findings, FINDING-926 to 1410:
- by reader: A 44, B 53, C 59, D 70, E 70, F 35, G 59, H 49, I 46;
- by rule: 1, 1; 2, 57; 3, 24; 4, 3; 5, 49; 6, 29; 7, 9; 8, 117;
  9, 177; 10, 12; 7 under more than one rule;
- by how they stand: 238 checked, 166 resting on the reader, 81
  uncertain;
- in text round 3 changed: 195; in text it did not: 280; not traced:
  10;
- proposed: 447 fix, 34 a question, 4 another ending;
- met in passing, of other kinds: about 100 lines, below the
  findings.

By cause, as the agent reads them before the endings: the 195 in
changed text were missed at the change; most of the 280 in text not
changed were missed by round 3's read, a few older than a rule the
round changed; the 81 uncertain ask whether the rule reaches them.
Three causes recur across readers, and each wants a decision:
- **copies not carried over:** layer 5 fixed our commit-plan Agent
  Skill, and layer 6 did not carry the fixes to the container's copy,
  24 hunks (FINDING-1256, 1308 to 1311);
- **fixes the endings list as made that never landed:** FINDING-532,
  549, 578 and 580 in part (FINDING-1130, 1185 to 1187);
- **Living Text in lowercase:** FINDING-664's fix reached only
  `refinement.md`. Three Agent Rules, in both seats, still write it
  lowercase (FINDING-1223), and its definition sits in
  `refinement.md`, not at its home (FINDING-1226).
