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

Collapsed at round 3's close: FINDING-282 to 925, each with its
ending and commit, are in git at `b8c7d99`, this file's
*Findings (§2.5)* under *Round 3: how it reads*. Every fix is in
the text the last read reads, and the commits cite each number.

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
- **Round 3's close read:** FINDING-926 to 1410, under a commit plan
  in the Refinement Layers' order; each file family's findings in its
  commit, what follows it in the commit after.
  - the conventions manual, 926 to 944 with DECISION-39's sentence,
    `0803717`; the convention-manual Agent Rule follows, `22da3ce`;
  - project-recording, 945 to 969, `f435e8d`;
  - the index, agent-arrangement, commit-messages and commit-plan,
    970 to 1000, `103a301`;
  - exchange and facts-in-sync, 1001 to 1022 with DECISION-35's
    sentence, `0cdd102`;
  - repo-hygiene, retrospective, shapes, visual-comparison and the
    writing manual, 1023 to 1069 and 1081, `efb8cef`;
  - the glossary, 1070 to 1080 with DECISION-36, `b379c2d`;
  - the Idea Models, 1082 to 1122, `9fce63c`;
  - the concept's chapters, 1123 to 1151, editorial, with
    DECISION-34's 532, `eefdced`; 1127's second half, a gap line in
    chapter 00, not editorial and open;
  - `ARCHITECTURE.md` and `README.md`, 1152 to 1171, `5d0f5ca`, whose
    body says "1150";
  - `PLAN.md` and `TODO.md`, 1172 to 1212 with DECISION-34's 549, 578
    and 580, `bcf3010`;
  - `CHANGELOG.md`, the Conversation Memory and `temp/README.md`, 1213
    to 1216 and 1219 to 1221, `a6f2a67`; 1217 and 1218 with the
    Master Copies, `2fca3bf`;
  - our Entry File and Agent Rules, F's share of 1222 to 1253,
    `fab7214`; the writing manual's rule 10 follows, `c91c15a`;
  - our Agent Skills and Approaches on Trial, F's other findings to
    1255, `448a16c`;
  - the delivery's pages, 1257 to 1276, `a456f4c`; our `PLAN.md`'s
    form follows, `78d04c3`; 1275 stands, by DECISION-39;
  - the container's records and hygiene files, 1277 to 1289 with
    1211, 1217 and 1218, `2fca3bf`; ours follow, `e39ad66`; 1287
    declined, CBC Bootstrap being the Stack Group's Name;
  - the container's agent files, 1256, 1277's Agent Rule line and
    1290 to 1315, with DECISION-33, `8b6eec0`; ours follow,
    `7319107`;
  - four lines against what was taken, corrected: 1258, 1300, 1303
    and 1313, `75d77e2`; ours follow, `04a06dd`;
  - the Method Group, 1316 to 1364, by file: cbc-framing's
    `ce370e4`; cbc-slice's, with 1320's homes, `5a1fa33`; the
    Output Shapes `6e1d55e`; the glossary and plain-words page
    `60398b1`; 1340 and 1360 stand, by DECISION-37, and 1361 by
    DECISION-40;
  - the Stack Group, 1365 to 1410, by file: cbc-bootstrap's
    `63bb1db`; infra-establish's and infra-serve's `1f13fee`, with
    the Stage 0 quote `ce370e4`'s rename grep missed; the glossary
    `91619d6`; 1391 stands, by DECISION-37.

  Left for the last read: 1384's bold leads that begin with a Name
  and 1388's "Stage n Gate" labels, each a question no decision
  answers; whether writing rule 10 says a parenthesis is a gloss, as
  DECISION-38 decided; the Java label "the promise: %s"; the Pure
  Seed's `git add` without `.claude/rules`; the playbook's "Steps
  5..N-3" with no status box; agent-arrangement §2.4's "a fact whose
  failure is not noticing it".

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

Collapsed at round 3's close: FINDING-926 to 1410, each with its
reader's number, its ending and its commit, are in git at `b8c7d99`,
this file's *Round 3's close read*.

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

### Decisions

Eight decisions, DECISION-33 to DECISION-40, for what recurs or what
a reader asked; then the agent's calls on the single questions.
Every other finding's ending is its reader's proposal, taken by the
reviewer, 2026-11-01, with the decisions and the calls below.

**DECISION-33.** The container's commit-plan Agent Skill. Rests:
FINDING-1256, 1308 to 1311. Layer 5 fixed our copy; layer 6's
`ddd6057` fixed only FINDING-630 in the container's, so the two
differ by 24 hunks. Of the other five pairs, commit-messages and
`approach-drafting.md` are identical, visual-comparison differs in
its §5 as ADR-0069 allows, and `writing.md` and `one-home.md` are
written for their seats.
- (a) The container's copy takes our fixes, hunk by hunk, keeping
  only what ADR-0069 lets a seat's copy say differently.
- (b) Each finding fixed alone.
- Recommended: (a). The findings are one miss, at one boundary, and
  a diff after shows the two agree.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-34.** Fixes the endings list as made that never landed.
Rests: FINDING-1130 (532), 1185 (578), 1186 (549), 1187 (580 in
part).
- (a) Each is made now, and *The work* names its commit; the close
  commit records the miss.
- (b) The endings are corrected to "not fixed", and the four move to
  the last read.
- Recommended: (a). The decisions stand; only the work was short.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-35.** Living Text's home. Rests: FINDING-1223, 1224,
1226, and the lowercase uses in PLAN and TODO. The glossary points
at facts-in-sync §1, which uses the words and never defines them;
`refinement.md` §1.1 defines them in bold.
- (a) Facts-in-sync §1 gains the one defining sentence, bold there;
  `refinement.md` §1.1 keeps its scope and points at it, its bold
  gone; every lowercase use takes the Name.
- (b) `refinement.md` §1.1 becomes the home, and the glossary points
  there.
- Recommended: (a). Living Text is a fact of one-home, used in every
  seat; the refinement only reads it.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-36.** "Birth" beside CBC Run Birth. Rests: FINDING-1072,
1181, 1233, and their other uses. "Born", "at birth" and "from
birth" are English everywhere.
- (a) "Birth" as a noun for the event is the Name, CBC Run Birth;
  "born", "at birth" and "from birth" stay English.
- (b) "Birth" stays English, and the Name is used only where the
  first state itself is meant.
- Recommended: (a). A reader cannot tell "a birth" from the Name,
  and the idioms read as English.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-37.** Where the Names stop. Rests: FINDING-1391, code
identifiers; 1340, a description's trigger phrases; 1360, the
Foundation Line's words in shipped files.
- (a) The Names reach prose and comments, not code identifiers, not
  the user's phrases a description quotes, and not a Foundation
  Line's value, whose form conventions §1.3 sets.
- (b) The Names reach all three.
- Recommended: (a). An identifier is code, a quoted phrase is the
  user's, and a Foundation Line is a field.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-38.** What rule 10's "standing alone" and "gloss" reach.
Rests: FINDING-1084, child titles that lean on their parent, the
Agent Model's §12.1 to 12.4; 1369, a parenthesis after a title;
987, agent-arrangement §3.9.
- (a) A child title stands alone; a parenthesis is a gloss. Each is
  retitled, with the rename grep.
- (b) A child title may lean on its parent's; a parenthesis is not a
  gloss.
- Recommended: (a). Rule 10's own example, *How*, is a title that
  leans on its parent.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-39.** Forms under rules 2 and 3. Rests: FINDING-1275,
the playbook's Goals as a lead line and bullets; 1081, the manual
form's sentence "A change here walks it"; 1359, the plain-words
page's "no jargon".
- (a) A Goal's labelled list is one sentence, as DECISION-30 meant;
  the form's sentence becomes "A change here runs the Change Walk on
  it", in the conventions manual and every manual; the plain-words
  page writes the Names, each beside its plain words at first use.
- (b) Each stays as it stands.
- Recommended: (a). Each keeps the form's shape and meets the rule.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-40.** Shipped text that points home. Rests: FINDING-1277,
11 lines with "CBC docs/conventions/…"; 1300, approach-drafting's
*Uses* paths; 1361, CBC Runs' evidence counts in a shipped workflow.
- (a) "CBC docs/…" becomes "the Concept Deliverer's
  docs/conventions/…" at each; the *Uses* paths take "the Concept
  Deliverer's"; the workflow keeps the count, since the CBC Run
  reads it as why the line is required.
- (b) The pointers go, the counts move to our records.
- Recommended: (a). The pointers serve our Foundation Check, and the
  count says why, which rule 4 asks.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

The agent's calls, on the single questions, each a fix unless said:
- FINDING-962: the Invariant Slice Record; "what a closed Plan Step
  proved is history".
- FINDING-970: "the commit-plan Agent Skill", as the reader
  recommends.
- FINDING-1026: the phrase stays, said once plainly: "the Plan Step
  that first builds the application on its stack".
- FINDING-1034: the plain-words rewrite goes last, as the reader
  proposes.
- FINDING-1107: said in plain words, as proposed.
- FINDING-1120: the ADR that records it, named.
- FINDING-1160: the Stack Group, by its Name.
- FINDING-1168: the paths lead each line.
- FINDING-1176: the Now line names the Agent Skill Stage or Approach
  on Trial Stage; the glossary's sentence stays.
- FINDING-1234: "Kind: an Agent Skill copied into a fresh draft each
  time".
- FINDING-1235: "project-recording's list of the records".
- FINDING-1258: the `temp/RUN-n.md` kind, said plainly.
- FINDING-1276: the tag goes.
- FINDING-1303: "a changed fact", as proposed.
- FINDING-1344: "owe" is not dead; the reader's fixes.
- FINDING-1353: "a standing idea", in all five places.
- FINDING-1362: GUARANTEE-n is the Invariant Slice Guarantee's; the
  System Guarantee's entry drops the tag.

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

### Endings (§2.6)

The reviewer took the eight decisions, DECISION-33 to 40, and the
agent's calls as recommended, 2026-11-01. The work names each fixed
finding's commit (§2.7, *Round 3's close read*).
- **Fixed, 477,** of which 3 in part: FINDING-926 to 1410 but those
  below. 1127's second half, a gap line in concept chapter 00, is
  not editorial and stays open; 1384 and 1388 are fixed where they
  propose, and each asks a question no decision answers.
- **Stand by a decision, 5:** FINDING-1275, a Goal's labelled list
  being one sentence (DECISION-39); 1340, 1360 and 1391, where the
  Names stop (DECISION-37); 1361, the CBC Runs' counts (DECISION-40).
- **Declined, 3:** FINDING-941 and 942, the agent's call: the Record
  Stub's working practice, and a fixed heading's numbered form;
  1287, CBC Bootstrap being the Stack Group's Name while the Hygiene
  Base reaches a CBC Run on any stack.

None of the three declines is taste: each line is true where it
stands. Four lines went against a call already taken and were
corrected (`75d77e2`, `04a06dd`); the close of the commit plan
(`a3a4026`) says how.

Round 3 is closed, and with it the refinement's last Refinement
Round. The last read (§2.9) is next: everything read against every
Finding Kind of the refinement, in one read, with no fixes between.
What is left for it is listed in *The work*, under *Round 3's close
read*, and in *Met at the close read, of other kinds*.

## The last read

### The rules' check (§2.3)

What changed since each Finding Kind was last read against, and the
TODO items that name a rule or its manual, searched 2026-11-01. The
table in *Kinds and rounds* names each rule where it stood on
2026-10-19; each has a home now:

| Kind | Rule now | Last read against | Changed since | Doubt |
|---|---|---|---|---|
| Stale lines | none needed: a false line is wrong | round 1's close read, `9f7e8dd` | nothing | no |
| Wiring | `docs/conventions/conventions/` §1.3, §2.3; `docs/conventions/facts-in-sync/` §3 | `9f7e8dd` | the Foundation Line's one home (`c0a3849`); the Fact Reference's one form (`a5c5a8e`, `a349b92`, `c53eac8`, `f76c045`, ADR-0070); a section may carry one Fact Reference for its lines (`36ea94d`, ADR-0072) | no |
| Agreement | facts-in-sync §4, §5; conventions §2.4 | `9f7e8dd` | the rule moved into facts-in-sync (`e2ad2e4`, ADR-0065) | no |
| One home | `.claude/rules/one-home.md`, on facts-in-sync §1 | round 2's close read, `d37a08f` | history is never a first home (ADR-0070); the Decisions Log and the Conversation Memory named as history (`f3175be`) | yes, one |
| Dependencies | facts-in-sync §2; §3.4, where a decision is cited | `d37a08f` | the citation rule (`39e35b3`, `96a4d82`, ADR-0078) | no |
| Lessons | conventions §2.6 | `d37a08f` | a lesson points at its story (`9f80445`, ADR-0073) | no |
| Layout | conventions §2.5; facts-in-sync §3.2 | `d37a08f` | a bold-led bullet with a paragraph of its own is a part (`aa40496`, DECISION-15) | no |
| Writing | `.claude/rules/writing.md`, on `docs/conventions/writing/` | round 3's close read, `f5dfbbe` | the stage headings named, Agent Skill Stage and Approach on Trial Stage (`c91c15a`) | yes, five |

None of TODO's 66 items doubts a rule's words. Four name a rule and
are due at the refinement's close, the read their evidence:
"Decide whether writing rule 10 reaches unnumbered headings", which
would widen it; "Test Fact References and foundations as a whole",
whose idea (d), a Finding Kind of its own in the last read, is not
taken, by the reviewer, 2026-11-01; "Decide whether a sweep checks one
home after work lands"; and "Decide whether a standing full read
looks for missing Fact References", whose trigger has not come.

Eight doubts came from what Round 3 left for this read: 1 to 4 from
the list in *The work*, under *Round 3's close read*; 5 to 8 from
*Met at the close read, of other kinds*, which the agent read only
after the first four were decided. Six are decisions the rules never
took. Two of them, DECISION-22 and DECISION-18, said their rule
would gain the line at round 3's close, and it did not. How each
ended, all by the reviewer, 2026-11-01, and all in ADR-0079:

1. **Rule 9, bold on a Name** (DECISION-22): in doubt, fixed. A Name
   is bold once, at the line that defines it.
2. **Rule 10, a parenthesis after a title** (DECISION-38): in doubt,
   fixed. It is a gloss.
3. **Rule 9, a list item's bold lead that begins with a Name**
   (FINDING-1384): in doubt, fixed. The bold marks the item, not the
   Name, and stands.
4. **Rule 9, the labels "Stage 1 Gate" to "Stage 6 Gate" beside Plan
   Step Gate** (FINDING-1388): not in doubt. They are labels inside
   their owner, which rule 9 already allows.
5. **Rule 10, a comma that joins a gloss** (DECISION-20): in doubt,
   fixed. It is a gloss; a comma in a list is not.
6. **One home, a released CHANGELOG entry** (DECISION-18): in doubt,
   fixed. It is history.
7. **Rule 9, a Foundation Line's value** (reader F): in doubt, fixed.
   It is written as conventions §1.3 gives it, as a path is.
8. **The writing rule's reach over the devlog,** "fragments fine" in
   `devlog/README.md` and project-recording §4 (reader E): not in
   doubt. The writing rule covers every new record line; the two lines
   are findings for this read.

The fixes, under the commit plan for the rules' fix: the writing
manual `66d8f6e`, ours `212a795`, the container's `0db2038`, for 1 to
3, 5 and 7; facts-in-sync §1 `f028aa8`, ours `71ad729`, the
container's `ae8eb31`, for 6.

The read's input, beside all Living Text: the list in *The work*,
under *Round 3's close read*, and *Met at the close read, of other
kinds*.
