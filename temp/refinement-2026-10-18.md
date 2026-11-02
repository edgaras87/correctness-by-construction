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
is `eec14ca:TODO-CONVERSATION-MEMORY.md` §7.

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
(`eec14ca:TODO-CONVERSATION-MEMORY.md` §7); §4 step 2 was written later.
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
  3's RETRO, 223, 224, 227 and 228, were to be worked in this round's
  layer 6, by DECISION-16. Corrected by the last read (FINDING-1501,
  DECISION-50): 206 went at `7f6e3a8`, before this round, and 224 in
  it; the last read's work fixed 223, 227 and 228.

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

### Files by layer (§2.2)

As at Round 3's close read: 118 files. Since `f5dfbbe` none came in
and none went; `devlog/2026-11.md` is history.

| Layer | Files | Lines |
|---|---|---|
| 1. The conventions manual | 1 | 366 |
| 2. Project-recording | 1 | 898 |
| 3. The other manuals, the models, the concept | 23 | about 4,600 |
| 4. `ARCHITECTURE.md`, `README.md`, the records | 12 | about 3,600 |
| 5. Our agent setup | 19 | 3,649 |
| 6. `delivery/`, what ships | 62: the container 25, the method 14, the stack 20, `README.md`, the playbook, the Pure Seed | 8,570 |

Read by header only, as before: `TODO-CONVERSATION-MEMORY.md`, 1,275
lines, and `.claude/decisions.md`, 1,242 lines, whose entries and
parts are history.

### The read's setup (§2.4)

Nothing is fixed during the read. Three steps, in order.

**1. The leftovers, checked first.** The agent checks each item of
both lists Round 3 left, in *The work* under *Round 3's close read*
and in *Met at the close read, of other kinds*, against the tree.
One still true is listed as a finding under its Finding Kind; one
gone is named with the commit that took it. Readers are given the
result and do not list these again.

**2. The scripts,** run by the agent over all 118 files:

- **Wiring, whole:** every path in backticks resolves; every Fact
  Reference lands on a heading with its number and title; every
  ADR cited exists; every Foundation Line names a convention, an
  Idea Model or a concept version that exists; every manual's *What
  this is made usable as* names each file whose Foundation Line names
  it, and nothing else.
- **Copies:** the worked example in `cbc-framing` and `cbc-slice`
  byte-identical; `approach-drafting.md` one text in both Convention
  Seats; our `commit-messages`, `commit-plan` and `visual-comparison`
  against the container's, every hunk listed for Agreement to judge
  against ADR-0069.
- **Writing, what a script can find:** numbered titles past 30
  characters, or with a dash, colon, comma or parenthesis; Glossary
  Names spelled in lowercase; a bold Name bold more than once, or away
  from the file its glossary entry points at.

A script's hit is a line to judge, not a finding. Each goes to the
reader of its file and Finding Kind.

**3. The readers,** 23, each for one Finding Kind and one part of the
text, side by side, each file whole unless the table says otherwise:

| Finding Kind | Reader | Files |
|---|---|---|
| Stale lines | 1 | layers 1 to 3 (25) |
| Stale lines | 2 | layers 4 and 5 (31) |
| Stale lines | 3 | layer 6: the container, `delivery/README.md`, the playbook, the Pure Seed (28) |
| Stale lines | 4 | layer 6: the method and the stack (34) |
| Agreement | our side | each file with a Foundation Line in layers 3 to 5, beside what it names; each manual's *The seats* beside the files its Convention Seat holds |
| Agreement | the CBC Run's side | layer 6's Agent Skills, Agent Rules, Output Shapes and references beside their manual or the concept; the Record Stubs beside project-recording; our copies of shipped files diffed |
| One home | ours | layers 1 to 5 (56), then a sweep by grep across all 118 |
| One home | what ships | layer 6 (62); the pairs of copies diffed |
| Dependencies | ours | layers 1 to 5 (56) |
| Dependencies | what ships | layer 6 (62) |
| Lessons | ours | layers 1 to 5 (56) |
| Lessons | what ships | layer 6 (62) |
| Layout | ours | the manuals, the models, the concept, `ARCHITECTURE.md`, `README.md` and `.claude/` whole; the other records and the templates by headings |
| Layout | what ships | layer 6's Agent Skills, Agent Rules, Output Shapes and references whole; the Record Stubs and templates by headings |
| Writing | A | layers 1 and 2 (2) |
| Writing | B | layer 3: the index, agent-arrangement, commit-messages, commit-plan, exchange, facts-in-sync (6) |
| Writing | C | layer 3: repo-hygiene and its 3 templates, retrospective, shapes, visual-comparison, writing, `docs/glossary.md` (9) |
| Writing | D | layer 3: the 3 Idea Models, the 5 concept chapters (8) |
| Writing | E | layer 4 (12) |
| Writing | F | layer 5 (19); the container's 4 copies diffed and read with ours |
| Writing | G | layer 6: `delivery/README.md`, the Pure Seed, the playbook, the container but those 4 (24) |
| Writing | H | layer 6: the method (14) |
| Writing | I | layer 6: the stack (20) |

Stale lines takes four readers, as Refinement Round 1 took five:
each line is checked against the tree, the heaviest read of the
eight. Wiring takes none: the scripts read it whole.

**What each reader gets:**

- its Finding Kind's row in *The rules' check*, and the rule's home,
  to read first;
- the rule for a finding (`.claude/approaches-on-trial/refinement.md`
  §2.4, *Reading the Finding Kinds*): a finding names the rule the
  text breaks; text that could read better is not one;
- the decisions taken, in each Refinement Round's *Decisions*, and
  the agent's calls on the single questions, beside them; a line one
  of them settled is not a finding;
- the result of step 1, and the script hits for its files;
- the form of a finding (§2.5, *List the findings*): where, what the
  rule says and the text says, how it stands, and why it was missed.

Readers are read-only, on the model and effort of the session, as
at Round 3's close read. The agent checks each finding's first quote
against the tree by script before listing it, and samples what the
script cannot parse.

### Before the readers

Steps 1 and 2 of the setup, run 2026-11-01 at `075a7ff`.

**Step 1, the leftovers: 78 still stand.** Each item's quoted text
was searched for with lines joined; where it is still in place, the
item stands. Where an item weighs two files against each other, its
quote was checked and its substance rests on the reader who met it.
Four items, in whole or in part, had no quote to search, and are
marked unverified.

- **The work's list, 8:** 5 stand: FINDING-1127's gap line in
  concept chapter 00; the Java label "the promise: %s"; the Pure
  Seed's `git add` without `.claude/rules`; the playbook's "Steps
  5..N-3" with no status box; agent-arrangement's "a fact whose
  failure is not noticing it". 3 ended by ADR-0079: FINDING-1384's
  bold leads, FINDING-1388's Gate labels, and the parenthesis.
- ***Met at the close read, of other kinds*, 99:** 73 stand, 23 are
  gone, and 3 repeat The work's list.

| Reader | Met | Stand | Gone | What went |
|---|---|---|---|---|
| A | 6 | 6 | 0 | |
| B | 8 | 5 | 3 | Living Text is defined in facts-in-sync §1; claim P1 is cited at its section; DECISION-29's wording was not a line of text |
| C | 11 | 8 | 3 | DECISION-22's line and the comma gloss, `66d8f6e`; shapes' "instances" |
| D | 9 | 7 | 1 | the Tiers Model's downward forms name the Delivery Fill; 1 repeats FINDING-1127 |
| E | 15 | 14 | 1 | TODO's "derives, points, governs" |
| F | 15 | 6 | 9 | the five copy statements, found true; our `commit-plan` and the container's now differ in 3 hunks, not 24; Living Text defined; the Foundation Line's value and the two rule lines, ADR-0079 |
| G | 11 | 7 | 2 | the copies' 24 hunks; the playbook's "earlier CBC Runs"; 2 repeat The work's list |
| H | 15 | 12 | 3 | cbc-slice's "single validated entry path"; two lines that were not findings |
| I | 9 | 8 | 1 | the Catalog Check's "the model's claims" |

The 78 are listed with the readers' findings, by Refinement Layer,
when the read's list is written (§2.5). Readers are told each one
and do not list it again.

**Step 2, the scripts.**

- **Wiring:** 236 hits; 233 are the script's own misreads or a CBC
  Run's own paths. 3 are listed:
  - the writing manual's *What this is made usable as* does not name
    `delivery/container/docs/glossary.md`, whose Foundation Line names
    the writing convention: checked;
  - the Decisions footers of `cbc-bootstrap/SKILL.md` and
    `infra-establish/SKILL.md` name `references/…` from the Agent
    Skill's folder, not from the repo root: uncertain, as a footer
    line may only name a file.
- **Copies:** the worked example is byte-identical in both Agent
  Skills; `approach-drafting.md` is one text in both Convention Seats;
  `commit-messages` is identical. `commit-plan` differs in 3 hunks:
  2 are the seat's, and the container's still bolds Change Set, which
  ours dropped at FINDING-626. `visual-comparison` differs in 1
  hunk, the seat's. The hunks go to the Agreement reader of the CBC
  Run's side.
- **Writing:** no numbered title in Living Text breaks rule 10; the
  10 that do are the Conversation Memory's part headings, history.
  48 lowercase spellings of a Name: 43 are the fixed heading or the
  verb "made usable", a Foundation Line's value, or the released
  `[v1]` entry, all allowed; 5 go to their readers. 68 bold Names:
  40 at the home their entry names, 22 list leads; 6 go to their
  readers: `PLAN.md`'s legend and the container's, delivered-copies'
  Delivery Pin and Read-Through Commit, and the worked example's
  paragraph leads, in both copies.

### The readers' reports

The 23 readers' reports, and the two of the Agreement reader's
helpers, are kept in `temp/last-read-2026-11-01/`, one file per
reader by its label: 272 findings, read at `70404e1`. Beside them,
the briefs the readers were given (`_brief.md`, `_writing-brief.md`),
the agent's notes on the leftovers (`_leftovers.md`), and the sweep
scripts with their file list (`_wiring.py`, `_writing.py`,
`_living-layers.tsv`), to run again at the next read. The read's
list (§2.5) is written from them; the folder goes with this file at
the refinement's close.

### The read's list (§2.5)

385 findings, FINDING-1411 to 1795, from four sources:
- **the readers,** 262: their 272 findings, 10 of them merged where two or three readers found one line;
- **the leftovers,** 83: the 78 of *Before the readers*, step 1, one more found to stand, and G7 split into its 5 items;
- **the scripts,** 3: the Wiring candidates;
- **met in passing,** 37: what a reader met of another Finding Kind, and its own reader did not list.

They go by Refinement Round, by the Finding Kinds' rule (§2.1, *Group the Finding Kinds*), then by Refinement Layer and file, in the order the work takes them. A merged finding goes in the earliest Refinement Round of its kinds.

Each entry gives its Finding Kind, how it stands, why it was missed, its source, where, the quote, what the text says, and the proposed ending. The rule each Finding Kind reads against is its row in *The rules' check* above. Each reader's full entry is in its report, `temp/last-read-2026-11-01/`, by the label in parentheses:
- **a reader's label,** such as SL1-1: the reader's finding, its quote checked by script, its proposal the reader's;
- **left A3:** a leftover, by its reader at round 3's close read; its proposal is the agent's;
- **script W1:** a Wiring candidate;
- **met AGO:** met in passing by that reader, not checked by the agent; its proposal is the agent's.

The leftovers and the items met in passing were not traced to a cause; their entries name none.

Two corrections to *Before the readers*, step 1, found by the readers:
- **left E6 stands,** marked gone: the parentheses now split "derives, points, governs", so the joined-line search missed it (SL2);
- **left B5 stands in all three sections,** marked gone at §2.9 and §2.12: those two are listed as LEO-1 and LEO-2 (LEO).

Left E7 and left E8 also gain the lines reader E named and step 1 left out (SL2).

What the merges join:
- **AGO-1, SL2-23, OHO-3:** our one-home Agent Rule's example of what goes;
- **DES-1, SL1-11, WF-11:** facts-in-sync §3.1's "leads with CBC", and the container's last "CBC docs/";
- **AGO-5, SL2-1:** `ARCHITECTURE.md`'s rule on the method's Output Shapes;
- **DEO-8, OHO-1** and **DEO-7, OHO-2:** the archive's fact, pointed at a released entry;
- **SL3-5, AGS-3:** delivered-copies' `paths:` without `docs/glossary/**`;
- **SL1-13, AGO-8:** the retrospective trial's moment;
- **AGS-1, WF-9:** the container's one-home Agent Rule on Living Text.

Lines found by more than one reader in passing are one entry. Met in passing, and already a finding: agent.md's "≤50 chars" (SL1-15), `README.md`'s pinned Output Shapes (SL2-3), project-recording's "four CBC Runs" (SL1-2), `PLAN.md`'s order of stopped Plan Steps (AGO-15), the three kinds of Work Approach (AGO-11), the Structural Wall Check's "reads the code" (SL4-2), the short `bootstrap.sql` path (SL4-3), the *Answered at close* lines (SL4-4), `slice-record.md`'s stage order (DES-5), the Infrastructure Contract's four tellings (LAS-8), and the container glossary's Living Text (AGS-1).

#### Round 1: what is true

##### Layer 1: the conventions manual

`docs/conventions/conventions/README.md`

**FINDING-1411.** Stale lines; resting on the reader, quote checked (left A3). §1.2, line 90: The frontmatter template's `foundation: the <name> convention` fits only a convention's Agent Skill. §1.3 gives method Agent Skills `concept v1`, and stack ones `practice, checked against concept v1`. Proposed: fix: the template points at §1.3 for the value.

**FINDING-1412.** Stale lines; resting on the reader, met in passing (met WA). §3, step 3, line 308; step 6, lines 320–321: "A convention entering or leaving the Container Group"; "lists … the conventions it received". DECISION-32: a CBC Run holds no convention. As left B3. Proposed: fix, with B3 and G3.

**FINDING-1413.** Wiring; resting on the reader, quote checked (left A1). *What this is made usable as*, lines 24–36: §2.3 asks each entry for "the moment it opens at". The Foundation Line entry and the index entry give none. Proposed: fix: each entry names its moment. AGO, in passing, met the same gap in agent-arrangement's third entry.

**FINDING-1414.** Stale lines; checked; missed at a change (SL1-1). `docs/conventions/conventions/README.md`, *What this is made usable as*, line 32: "- **the index, `docs/conventions/README.md`** — it points at each manual. It holds". The index points at each manual. It does not. `docs/conventions/README.md` names only `docs/conventions/conventions/` and `.claude/approaches-on-trial/approach-drafting.md`. It sends the reader to `ARCHITECTURE.md` §1.2 for which conventions there are. The list of manuals left the index at `722357d` (2026-09-30). Why: missed at a change. `0803717` (2026-11-01, "the conventions manual meets the rule again") expanded "it points" to "it points at each manual". The Foundation Check's read of the index beside the change should have caught it. Proposed: fix: "it points at this manual and at `ARCHITECTURE.md` for the rest." Or go back to "it points."

**FINDING-1415.** Wiring; resting on the reader, met in passing (met DEO). line 35; `docs/conventions/README.md` line 8: "`ARCHITECTURE.md`…(§1.2, *The conventions*)" in the same-document form; it lands on the citing file's own §1.2. Proposed: fix: the path inside the parentheses.

**FINDING-1416.** Agreement; resting on the reader; missed at a change (AGO-11). `docs/conventions/conventions/README.md`, §1, *A convention's Work Approaches*, lines 52 to 58: "- Record Stubs and Agent Skill Templates, for rules that sit in the". A Work Approach is one of three: an Agent Skill, an Agent Rule, or "Record Stubs and Agent Skill Templates". Its Idea Model, the Idea-to-Output Model, lists them otherwise: - §1 and §6.1: "Agent Skills, Agent Rules and Output Forms"; - §2, line 38: "an Agent Skill, an Agent Rule, an Approach on Trial, a record's form in its header comment". The model never names an Agent Skill Template. ADR-0078's decision 1 takes the model's words. Which side: unclear. A Record Stub carries a record's Output Form, so that part may only be wording. The Agent Skill Template is the real difference. Why: missed at the design that renamed both (ADR-0078, DECISION-32): the model's §6 and the manual's §1 were walked together, but their lists were not compared. Proposed: question: is an Agent Skill Template a Work Approach? If yes, the model's §2 names it. If not, the manual's third kind reads "Output Forms: a record's form, in its header or its Record Stub".

**FINDING-1417.** Stale lines; resting on the reader, quote checked (left A2). *Why it arrives this way*, line 338: "in the frontmatter of every shipped Agent Skill and Agent Rule". §1.3 also puts the Foundation Line in this repo's own files, in shipped Output Shapes, in manuals on an Idea Model, and in a record's header comment, which is not frontmatter. Proposed: fix: "in every file §1.3 names".

**FINDING-1418.** Wiring; resting on the reader, met in passing (met WA). *Where to look*, line 363: "§1.3, *The Foundation Line*, above" is not a root path, and §2.9 asks for "Fact References only, as root paths". The bullet also joins two addresses with a semicolon. Proposed: fix: the root path, one address a line.

##### Layer 2: project-recording

`docs/conventions/project-recording/README.md`

**FINDING-1419.** Agreement; resting on the reader, quote checked (left A6). §2.4, lines 252–254: "The look back is not the plan's: `RETRO.md`" is stated for both Convention Seats. Item 12, lines 158–159, says the Concept Deliverer has none. Proposed: fix: §2.4 says it is the CBC Run's.

**FINDING-1420.** Agreement; resting on the reader, quote checked (left A5). §3.3, line 296; *The Concept Deliverer's seat*, item 4, lines 91–93: Item 4 now says the §3.3 index is the CBC Run's. §3.3 itself still states `PLAN.md`'s Decision index for every repo. Stands in part (WA, in passing). Proposed: fix: §3.3 says the index is the CBC Run's.

**FINDING-1421.** Agreement; resting on the reader, met in passing (met SL1). §9.3, line 660: A playbook is versioned "with a note of which project last updated it". The playbook's version line names no project. Proposed: fix: one side follows the other.

**FINDING-1422.** Stale lines; resting on the reader, quote checked (left A4). §13, lines 799–801: "the records table, the only part of the project-recording manual loaded before any task". The records table is in the Entry File, not in the manual, and conventions §2 says a manual is never loaded into an agent. Proposed: fix: "the records table, which the Entry File holds and every session loads".

**FINDING-1423.** Agreement; resting on the reader, met in passing (met WA). §13.1, lines 810–813: A row names three things, but the text speaks of "the half that is new" and of a table read "in both directions". FINDING-335 judged only the figure. Proposed: fix: the text matches the row.

**FINDING-1424.** Stale lines; checked; missed at a change (SL1-2). `docs/conventions/project-recording/README.md`, *What it is for*, line 16: "since: four CBC Runs kept their records under these Record Stubs. Every". Four CBC Runs. The count was set on 2026-10-20 (`f1c02a7`). CBC Run 5 was born on 2026-10-21 and ran through Release. CBC Run 6 was born on 2026-10-29 (`ARCHITECTURE.md` §2.5 lists six). The count has not moved since. Why: missed at a change. Neither CBC Run Birth's close checked this count. The Plan Step Form's close item on "now", "today" and "not yet" asks only about lines that mention the Plan Step's subject. Proposed: question: count the CBC Runs that kept records under the Record Stubs (five or six, depending on CBC Run 2, idle since its Step 0), or date the count, "four by 2026-10-20".

**FINDING-1425.** Stale lines; checked; missed at a change (SL1-3). `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 1, line 74: " the next CBC Run Birth". Whether a retrospective serves this repo is on trial at the close of the Plan Step that runs "the next CBC Run Birth". That trigger was the close of CBC Run 5's birth Plan Step: TODO's "Run this repo's retrospective, on trial" names it. The close came on 2026-10-22 without running the trial. The devlog says it "fired" and was left for the reviewer to place (devlog 2026-10-22). Read today, "the next CBC Run Birth" points at CBC Run 6's. That Plan Step is stopped, and nothing ties the trial to it. Why: missed at a change. The close of CBC Run 5's birth fired the trigger, but nothing re-read the two manuals that state it. `f435e8d` (2026-11-01) reworded the line and kept the claim. Proposed: question: where the reviewer places the trial. Then: "is on trial, its close placed by the reviewer (TODO's "Run this repo's retrospective, on trial")". SL1-13 is the same line in the retrospective manual.

**FINDING-1426.** Agreement; checked; missed at a change (AGO-15). `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 4, lines 81 to 82: " work being done now, and below it any Plan Step stopped for it.". A stopped Plan Step sits below the one being worked. In `PLAN.md` the two stopped Plan Steps come first (lines 135 and 213), and the open one, "Refine this repo against its own rules", comes last (line 301). Which side: the seat. `PLAN.md`'s form says nothing of order, so the seat's "below" is the only claim. Why: the seat was written for one stopped Plan Step; a second one was stopped and the order was never read against it. Proposed: fix: "the piece of work being done now, and beside it any Plan Step stopped for it."

**FINDING-1427.** Stale lines; resting on the reader; missed at a change (SL1-4). `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 5, line 96: " invariants and a `src/` codemap. It keeps to about two pages, as §8". Our `ARCHITECTURE.md` keeps to about two pages. ADR-0068 set "about two pages" at about 1,200 words. `ARCHITECTURE.md` is now 2,053 words and 269 lines. Why: missed at a change. The file grew past the measure across its Refinement Round fixes, and no check compares its size with the claim. Proposed: question: is it cut back to the measure, or does the line say "it aims at about two pages"?

**FINDING-1428.** Stale lines; checked; missed at a change (SL1-5). `docs/conventions/project-recording/README.md`, *The Concept Deliverer's seat*, item 6, line 119: " decisions each, a median of 4.5, and a median of 102 lines. Their". The ADRs' median length is 102 lines, and the median number of decisions is 4.5. The figures were written at `eb57bcf` (2026-11-01, 08:46), when there were 78 ADRs. ADR-0079 landed after (`fc97f20`, 19:29). With 79 ADRs, the median length by `wc -l` is 103 lines. A median of an odd number of whole counts cannot be 4.5. Why: missed at a change. Nothing re-reads an undated running count when an ADR is added. Proposed: fix: date the figures, "at 2026-11-01, 78 ADRs: up to 12 numbered decisions each, a median of 4.5, and a median of 102 lines". Or drop the medians and keep "up to 12".

**FINDING-1429.** Stale lines; uncertain; older than the rule (SL1-6). `docs/conventions/project-recording/README.md`, §7.5 *When a README changes*, line 558: "already written so in Plan Step Gates in use ("ARCHITECTURE". Plan Step Gates in use already carry a records item such as "ARCHITECTURE current". No Plan Step Gate in this repo carries it: not the playbook's (its Gate lines are empty), not the PLAN Record Stub's, not our `PLAN.md`'s. The words came from the handbook ("lived gates") and were reworded at `f435e8d`. Why: older text, carried through rewordings. Each rewording kept the claim and did not check it. Proposed: question: name a gate item that exists, such as our close item "`CLAUDE.md` read top to bottom", or drop the example.

**FINDING-1430.** Stale lines; resting on the reader; missed at a change (SL1-7). `docs/conventions/project-recording/README.md`, §9.4 *How a playbook is written*, moment 2, line 678: " authors them. No Agent Skill or Plan Step asks this of a CBC Run yet: the TODO". No Agent Skill or Plan Step asks a CBC Run to confirm its Plan Steps once the problem is framed. The playbook's Step 2 asks it under *Known already*: "the plan is read end to end against the CBC Framing Exports: each later Plan Step still stands as named, or is reworded in place, never kept silently." That line has been there since `51a792e` (2026-10-16, ADR-0055 decision 6). The manual's line came later (`90d1367`, 2026-10-26). Why: missed at a change. `90d1367` wrote it without reading the playbook it describes. Proposed: fix: "The playbook's Step 2 asks part of it: each later Plan Step is read against the CBC Framing Exports and reworded where it no longer fits. The TODO item "Read CBC Run 4 against `dac4dd1`" asks whether CBC Run 4 did it."

**FINDING-1431.** Stale lines; resting on the reader; missed at a change (SL1-8). `docs/conventions/project-recording/README.md`, §14 *Conversation Memory*, line 856: "The trial is judged when the third item is worked with its section". The trial is judged at the third item worked with its section in hand. The devlog records at least three: §1 for the text-division item ("changed the work", 2026-10-24), §18 for the lesson stories and §19 with §23 for the words item (both 2026-10-29). No verdict is recorded in the devlog, TODO, PLAN or the refinement file, and the line still reads as a trigger yet to come. Why: missed at a change. The close of each of those items did not check the trial's trigger. Proposed: question: the reviewer judges the trial now, or the line names the refinement Plan Step's close as the moment, saying the item count has passed.

**FINDING-1432.** Agreement; resting on the reader, met in passing (met WA). *Why it arrives this way*, lines 866–868: A rule read inside `PLAN.md` is cited to the Installed Channel. The glossary says the Installed Channel delivers nothing to the context window. Uncertain. Proposed: question: which channel a rule read inside `PLAN.md` is.

##### Layer 3: the other manuals, the Idea Models, the concept

`concept/00-cbc.md`

**FINDING-1433.** Agreement; resting on the reader, quote checked (left 1127). lines 113–122: The gap line names "five practices" and "five phases", but the list of gaps beside it has four, and design-before-code has none (D-46). FINDING-1127's second half, not editorial, so left open at round 3; reader D met it again. Proposed: question: the line says four gaps, or a fifth gap is named for design-before-code. A concept chapter's fix that is not editorial is a concept change, and goes through the Foundation Check.

`docs/conventions/agent-arrangement/README.md`

**FINDING-1434.** Wiring; resting on the reader, met in passing (met AGO). *What this is made usable as*, third entry: No moment (conventions §2.3). As left A1, in another manual. Proposed: fix, with A1.

**FINDING-1435.** Wiring; resting on the reader, met in passing (met AGO). §2.4, lines 206–208: "two files disagree while both look current" is claim M2, but the Fact Reference names only M1. Proposed: fix: the reference names M2.

**FINDING-1436.** Stale lines; resting on the reader; missed at a change (SL1-9). `docs/conventions/agent-arrangement/README.md`, *The CBC Run's seat*, line 52: "CBC Run receives it. Its Entry File says two things. `docs/concept/". The shipped Entry File says two things: the copies are pinned, and before CBC Framing the only method work is the cbc-framing Agent Skill. Since `3630ed9` (2026-10-31) it also says the delivered words arrive in `docs/glossary/`, and that this project's own are `docs/glossary.md`'s. It also says where the method is. The count was written at `f07d52a` (2026-11-01), after the glossary line. Why: missed at a change. `f07d52a` reworded the line without re-reading `delivery/container/.claude/CLAUDE.md`. Proposed: fix: "Its Entry File says, among other things, that..." Or add the glossary line as a third thing.

**FINDING-1437.** Stale lines; resting on the reader, quote checked (left B3). lines 91–94 and 330: A CBC Run's birth entry "lists the conventions it holds". DECISION-32: a CBC Run holds no convention, only the Work Approaches made from ours. WA, in passing, met the same in conventions §3 steps 3 and 6; G3 and SL3-3 in the container. Proposed: fix, in the words chosen for G3: "lists the Work Approaches it holds".

**FINDING-1438.** Stale lines; checked; older than the rule (SL1-10). `docs/conventions/agent-arrangement/README.md`, §2.4 *How the Entry File is written*, line 233: "heading saves one that fails. The first two are present at birth. The". Of the five kinds of content, the first two are present at birth, and the other three, *Local rules* among them, arrive when they become true. The shipped Entry File has a `## Local rules` section at birth, with one rule: "Nothing before the CBC Run Briefing names the problem." That section has been in the Container Group since `d148ccb` (2026-09-19). Why: older text: the line came with the vendored manual (`9a1637d`, 2026-09-18). It was missed at `d148ccb`, and in Refinement Round 1's Stale lines read. Proposed: fix: "The first two are present at birth, and a CBC Run's Entry File is born with one Local Rule. The others arrive when they become true..."

**FINDING-1439.** Wiring; resting on the reader, quote checked (left B4). line 386: "(the Plan Step Form)" stands as a Fact Reference with no path. The form is in `PLAN.md`. Proposed: fix: "(`PLAN.md`, *The Plan Step Form*)".

`docs/conventions/commit-messages/README.md`

**FINDING-1440.** Wiring; resting on the reader, met in passing (met DEO). lines 15–16: Cites claim A1 at "`docs/models/agent.md` §12, *Claims*". A1 sits in §12.1, *Claims on the Ambient Channel*. Proposed: fix: §12.1 and its title.

`docs/conventions/commit-plan/README.md`

**FINDING-1441.** Stale lines; resting on the reader, quote checked (left B6). §2.10, line 139: "a manual wraps its prose". Since ADR-0077, Markdown has no line width; the reason holds for older text only. Proposed: fix: "a line of older text may be wrapped, so a name broken across two…".

**FINDING-1442.** Agreement; resting on the reader, met in passing (met AGS). §2.1: `COMMIT-PLAN.md` is "not a record" and sits outside project-recording; the shipped commit-messages Agent Skill line 105 says "None is a project record". Project-recording §1 lists it as record 9, and both records tables carry its row. Proposed: question: it is a record, or project-recording §1 marks it as listed but not a record.

**FINDING-1443.** Stale lines; resting on the reader, met in passing (met LEO). §2.9: The case says "CBC Run 3's Step 10 plan"; `489ecf2`, which brought it in, says the SL-3 plan taught it. Not checked further. Proposed: goes with LEO-1, if the case leaves the manual.

`docs/conventions/exchange/README.md`

**FINDING-1444.** Agreement; resting on the reader, met in passing (met AGS). §4, step 2; §6.5: An edit at a Delivery Take has three endings: taken, declined, unanswered. §6.5's fourth verdict, held, has none there, and neither the manual nor delivered-copies says what a held edit becomes when the copy lands whole. Proposed: question: what a held edit becomes at a Delivery Take.

**FINDING-1445.** Agreement; resting on the reader, quote checked (left B7). §6.1, line 487: "the diff of every held copy against its Delivery Pin". The Delivery Pin is our commit, which the CBC Run's diff cannot name. §3.8 and the exchange-read Agent Skill compare against the CBC Run's own last delivery commit. Proposed: fix: "against the commit of its last delivery".

`docs/conventions/facts-in-sync/README.md`

**FINDING-1446.** Agreement; checked; missed at a change (AGO-7). `docs/conventions/facts-in-sync/README.md`, *What this is made usable as*, lines 38 to 41. The same list is in `.claude/rules/one-home.md`, its header comment, lines 11 to 13: " §2, *Point and derive*; §3.1, *What a Fact Reference is*; *The Concept Deliverer's seat*).". Our one-home Agent Rule holds §1, §2, §3.1 and the Concept Deliverer's seat. The Agent Rule's rule 7 holds §3.4, *A decision citation*, and cites it. Rule 4 also uses §3.3 and §4. A change to §3.4 would not find rule 7 by this list. Which side: the list, in both places. Why: missed at a change. `7d060af` (2026-10-31) added rule 7 and did not touch the list or the header comment. The Foundation Check's step 2 opens the manual beside the change. Proposed: fix both lists to add "§3.4, *A decision citation*" (in the comment, "§3.4, A decision citation"). Add §3.3 and §4 if the reviewer counts rule 4's references.

**FINDING-1447.** Dependencies, Stale lines, Writing; checked; missed at a change (DES-1; also SL1-11, WF-11). `docs/conventions/facts-in-sync/README.md`, §3.1 *What a Fact Reference is*, line 179. It weighs against 11 shipped lines in 10 files: `delivery/container/.claude/CLAUDE.md` 40 and 60, `README.md` 35, `ARCHITECTURE.md` 9, `CHANGELOG.md` 18, `PLAN.md` 10, `TODO.md` 24, `devlog/devlog.md` 12, `docs/adr/0001-record-architecture-decisions.md` 41, `.claude/decisions.md` 28, `.claude/rules/delivered-copies.md` 163. Also `delivery/container/.claude/rules/one-home.md` 12–13, which still writes "(CBC docs/conventions/facts-in-sync/ §1, …)": "In a shipped file, a reference to this repo's text leads with CBC". DECISION-40 (2026-11-01) changed the 11 lines from "CBC docs/…" to "the Concept Deliverer's docs/…". §3.1 still says "leads with CBC". So the 11 lines break the rule as written, and `one-home.md` 12–13 keeps the old form. Two forms now stand in shipped files. Why: missed at a change. DECISION-40 was fixed in `2fca3bf`, `8b6eec0` and `75d77e2`. No commit changed §3.1. The same miss ADR-0079 names for DECISION-18 and DECISION-22. SL1-11 (Stale lines): a shipped file's reference to our text leads with CBC. DECISION-40 (2026-11-01) changed that form to "the Concept Deliverer's `docs/conventions/…`", and the fix landed at `8b6eec0` and `2fca3bf`. At `70404e1`, `delivery/` has 0 references that open with "CBC `docs/" and 13 that open with "the Concept Deliverer's `docs/". The manual that states the form was not changed. Its proposal: fix: "In a shipped file, a reference to this repo's text leads with "the Concept Deliverer's" and serves this repo's Change Walk alone." Check line 149 too, the cross-repo example, against what DECISION-40 meant for a shipped file. WF-11 (Writing): "(CBC docs/conventions/facts-in-sync/ §1, One home; The CBC Run's seat)". A CBC Run does not know "CBC" is our Repo Tag. It is the last "CBC docs/" under `delivery/`. Its proposal: fix: drop "CBC": "(docs/conventions/facts-in-sync/ §1, One home; The CBC Run's seat)". The sentence already says "the Concept Deliverer's facts-in-sync manual". Proposed: question: (a) §3.1 says a shipped reference to this repo's text opens with "the Concept Deliverer's", in words, and the container's `one-home.md` comment follows; or (b) the 11 lines take "CBC" back, and the container's glossary gains the Repo Tag. Recommended: (a). It is what DECISION-40 chose, and FINDING-1277's reason stands: nothing in a CBC Run says what "CBC" is.

`docs/conventions/repo-hygiene/README.md`

**FINDING-1448.** Agreement; resting on the reader, quote checked (left C10). line 71: "the Plan Step that makes the stack true". The Hygiene Base's three marker lines say "at app bootstrap"; the playbook calls it "Step 4: CBC Bootstrap". Three wordings for one moment. Proposed: fix: one wording, the playbook's Plan Step by its Name.

**FINDING-1449.** Stale lines; checked; missed at a change (SL1-12). `docs/conventions/repo-hygiene/README.md`, §2 *The template layers*, lines 78 to 79: "Plan Step, Agent Skill or playbook names the append.". No Plan Step, Agent Skill or playbook names the append. The cbc-bootstrap Agent Skill does: "Each hygiene file, `.gitignore`, `.gitattributes` and `.editorconfig`, takes its Stack Overlay below the marked line it carries" (`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, line 205). Its walkthrough lists what each file takes (`spring-boot-walkthrough.md`, lines 50 to 56). The Agent Skill has named the append since `b6ecf85` (2026-10-21). The manual's line was written later, at `dd88bf6` (2026-10-26). "Nothing ships one" still holds: the `.part` files do not ship. Why: missed at a change. `dd88bf6` moved the line out of a dated italic without re-reading the Stack Group. Proposed: fix: "How a Stack Overlay reaches a CBC Run is open: nothing ships one. The cbc-bootstrap Agent Skill names the append, and its walkthrough lists what each file takes, written by the CBC Run itself."

`docs/conventions/repo-hygiene/templates/java-spring/editorconfig.part`

**FINDING-1450.** Agreement; resting on the reader, quote checked (left C9). line 3: Marks "# --- java-spring Stack Overlay ---". The other two `.part` files mark "# --- java-spring (Maven) Stack Overlay ---". Proposed: fix: one marker in all three.

`docs/conventions/retrospective/README.md`

**FINDING-1451.** Stale lines, Agreement; checked; missed at a change (SL1-13; also AGO-8). `docs/conventions/retrospective/README.md`, *The Concept Deliverer's seat*, line 89: "At the close of the Plan Step that runs the next CBC Run Birth, it". The same claim as SL1-3. The trial's trigger was the close of CBC Run 5's birth Plan Step (TODO's "Run this repo's retrospective, on trial"). That close came on 2026-10-22 without the trial (devlog 2026-10-22), and the reviewer has not yet placed it. Why: missed at a change, as SL1-3. `7b81e55` (2026-11-01) reworded the line. AGO-8 (Agreement): at that close, this repo runs both retrospective Agent Skills on itself, "in place of that close line", the line "lessons written back where they came from". Our side holds three different answers: - `PLAN.md`'s open-but-stopped Plan Step "Birth CBC Run 6, on full auto" ran a CBC Run Birth (2026-10-29). Its close items, lines 182 to 201, hold no retrospective, and still hold the close line the trial replaces (line 194). `PLAN.md`'s form says "A trial names the close that judges it." - `TODO.md` line 682 gives CBC Run 5's birth as the trigger, which has passed (that trigger is leftover E8; the disagreement here is the manual against `PLAN.md`). - Written on 2026-11-01, after CBC Run 6's birth, "the next" may mean CBC Run 7's. Its proposal: question: does the trial run at the close of "Birth CBC Run 6, on full auto", or at CBC Run 7's? Then fix whichever side is wrong, and name the Plan Step in both manuals. Proposed: question, with SL1-3: where the reviewer places the trial. The line then names that close.

`docs/conventions/visual-comparison/README.md`

**FINDING-1452.** Agreement; resting on the reader, quote checked (left C6). §1, line 55: "Its name is the question, not a candidate: *how is this shown*". The convention and its Agent Skill are named visual-comparison, which names a picture. Proposed: question: the line says the name is kept for its history, or the claim goes.

`docs/conventions/writing/README.md`

**FINDING-1453.** Wiring; checked (script W1). *What this is made usable as*: The list does not name `delivery/container/docs/glossary.md`, whose Foundation Line names the writing convention. Proposed: fix: the entry, with its moment.

**FINDING-1454.** Agreement; resting on the reader, quote checked (left C1). §1, line 67: "History keeps its words" names three kinds of history. The one-home Agent Rule's *Not a second home* names more: the Decisions Log's entries, the Conversation Memory's parts, and, by ADR-0079, a released CHANGELOG entry. Proposed: fix: point at facts-in-sync §1 for what history is, and drop the list.

**FINDING-1455.** Agreement; resting on the reader; missed at a change (AGO-14). `docs/conventions/writing/README.md`, *The seats*, lines 54 to 56: "commits. The Concept Deliverer writes under its own: its chat and". The Concept Deliverer writes "its chat and records" under its Agent Rule, beside what CBC Runs read and its manuals. The CBC Run's seat names its commits. Our Agent Rule, `.claude/rules/writing.md`, governs "commit messages, comments" as well, and the manual's §1 covers both in every repo. Which side: the seat. Why: the rule check of Refinement Round 3 read the rule, not the seat beside our rule. Proposed: fix: "The Concept Deliverer writes under its own: its chat, its records, its commits and comments."

**FINDING-1456.** Agreement; uncertain; missed at a change (AGO-16). `docs/conventions/writing/README.md`, §2, *Why each rule*, rule 6, lines 96 to 97. Our Agent Rule follows it, `.claude/rules/writing.md` rule 6, line 30 to 31: "Define each Glossary Name once, in plain words, in `docs/glossary.md`.": " cannot check, so each is defined once, in the project's". Each coined word is defined in the project's glossary. The glossary, which derives from this manual, says "the home defines, the entry points" (`docs/glossary.md`, header comment, lines 8 to 9). The manual's own rule 9 says the same as the glossary: a Name goes into the glossary "pointing at the home that defines it". Which side: rule 6, in the manual and in our Agent Rule. It predates ADR-0076, which made the glossary a list of Names. Why: rule 6 was not rewritten when rule 9 was (ADR-0076, ADR-0078). Proposed: question: does rule 6 read "so each has one Glossary Name, listed in the project's glossary with its plain meaning, pointing at the home that defines it"? Our Agent Rule's rule 6 would follow.

**FINDING-1457.** Stale lines; resting on the reader, quote checked (left C5). line 167: "985 lines in 83 of the 99 living files" is a count from before round 3. Likely stale; not checked. Proposed: fix: date the count, "on 2026-10-29".

`docs/glossary.md`

**FINDING-1458.** Agreement; resting on the reader, quote checked (left C11). line 45; `docs/conventions/retrospective/README.md` line 89: "until its agent finishes the CBC Run Birth"; "runs the next CBC Run Birth". The glossary defines CBC Run Birth as a CBC Run's first state, not an act. G11 meets the same in the Pure Seed. Proposed: question, with G11: the entry widens to the event, as DECISION-36 reads "birth" as a noun for the event; or the three lines say "until its agent finishes its first Plan Step".

**FINDING-1459.** Stale lines; checked; missed at a change (SL1-14). `docs/glossary.md`, *Between them*, the Receipt Branch entry, line 74: " named by its Delivery Pin and never merged: the Pure Seed's". A Receipt Branch is named by its Delivery Pin, and the Pure Seed's `birth-seed` is one. `birth-seed` is not named by a Delivery Pin. The Pure Seed puts the Delivery Pin in its commit subjects (`delivery/installs/pure-seed.md`, step 4, line 128). Why: missed at a change. `873663f` (2026-10-31) took "named by the Delivery Pin" from exchange §4, step 3, and added the Pure Seed's branch beside it without checking its name. Proposed: fix: "a branch holding a delivery as it arrived, never merged: the Pure Seed's `birth-seed`, its Delivery Pin in each commit's subject, or one a CBC Run cuts at its Delivery Take, named by the Delivery Pin, so..."

`docs/models/agent.md`

**FINDING-1460.** Agreement; resting on the reader, quote checked (left D2). G1, line 430; A1, line 293: G1 says the rule was broken 15 times "for the whole life of the handbook". A1 counts 15 in the handbook's first 20 commits. Proposed: fix: G1 takes A1's span.

**FINDING-1461.** Agreement; resting on the reader, quote checked (left D3). W2, line 394: Cites "three CBC Runs" and gives two incidents. Proposed: fix: the count matches the incidents given.

**FINDING-1462.** Agreement; resting on the reader, quote checked (left D4). M2, line 423; line 275: M2 is "`evidenced` (definitional)", while line 275 defines `evidenced` as observed. Proposed: question: M2 takes another grade, or line 275 allows a definitional case.

**FINDING-1463.** Agreement; resting on the reader, quote checked (left D5). §9, line 239: Gives an Agent Skill to "a rule bound to a moment", which §8's table gives to the Pushed Channel; A1, line 292, calls an Agent Skill the Pulled Channel. Proposed: question: which channel an Agent Skill is, then the other line follows.

**FINDING-1464.** Agreement; resting on the reader, quote checked (left D1). §10, line 257: "One mechanism may serve two channels", but its example pairs a channel with the Enforcement Gate, which is not a channel. Proposed: fix: an example of two channels, or "a channel and a gate".

**FINDING-1465.** Agreement; uncertain; missed at a change (AGO-9). `docs/models/agent.md`, §4.1, *Ambient Channel*, *Ownership*, line 92: " - stays out of the repo's history;". An operator's own file "stays out of the repo's history". The agent-arrangement manual, which stands on this model and cites this part for the file, says "The Concept Deliverer tracks its own" (§3.7, *`CLAUDE.local.md`*; ADR-0062). This repo's `CLAUDE.local.md` is tracked. Which side: the model, probably. ADR-0062 never weighed it. But an Idea Model's rules may vary by repo (`docs/models/idea-to-output.md` §5, *An Idea Model and a concept*), so this may be an allowed adaptation. Why: missed at a change. `a3fefe1` (2026-10-23) changed agent-arrangement §3.7. The Foundation Check's step 2 opens the Idea Model the manual names. Proposed: question: does §4.1 say "stays out of the repo's history, unless a repo with one operator tracks it"? Or is the difference an adaptation, said in agent-arrangement §3.7?

**FINDING-1466.** Agreement; resting on the reader; older than the rule (AGO-10). `docs/models/agent.md`, §9, *Where each convention lands*, lines 238 to 240: "Each convention's Work Approaches show where it lands: an Agent Skill". A convention lands as an Agent Skill, or as Record Stubs and Agent Skill Templates. The agent-arrangement manual, which stands on it, places a convention's rule in an Agent Rule as well: by path (§3.2, *`.claude/rules/`*), or with no path for a rule of every task (§3.9, *An Agent Rule always loaded*). Six of our Agent Rules and four of the Container Group's land so. Which side: the model. Its list predates the Agent Rules always loaded (ADR-0053). Why: older than ADR-0053. Missed at `9fce63c` (2026-11-01), which rewrote this line; the Foundation Check's step 3 runs the Change Walk on what stands on the model. Proposed: fix: "Each convention's Work Approaches show where it lands: an Agent Skill for a rule bound to a moment, an Agent Rule for a rule bound to a path or to every task, Record Stubs and Agent Skill Templates for a rule carried in the files a project is born with."

**FINDING-1467.** Stale lines; resting on the reader; older than the rule (SL1-15). `docs/models/agent.md`, §12.7 *Claims on summaries*, claim M1, line 414: "- `evidenced` — the commit-messages manual states "≤50 chars, imperative, **no". The commit-messages manual states "≤50 chars, imperative, no period". Our manual states neither. It says "Either mood, in the present tense" (§2.2, ADR-0049). The words now in force are the commit-messages Agent Skill's, "≤50 chars, present tense, no period". The evidence came from the handbook, vendored on 2026-08-27 (`7b049af`), where its manual said it then. Why: older than the change. ADR-0049 changed the mood in our manual, and the claim's tense was not re-read. `4ee4062` (2026-11-01) reworded the line. Proposed: fix: "the handbook's commit-messages manual of the time stated "≤50 chars, imperative, **no period**"."

`docs/models/idea-to-output.md`

**FINDING-1468.** Stale lines; resting on the reader, quote checked (left D6). §2, line 40: `.claude/shapes/` does not exist in this repo. The Output Shapes are at `delivery/method/.claude/shapes/`. Proposed: fix: "a CBC Run's `.claude/shapes/`", or our path.

**FINDING-1469.** Agreement; resting on the reader; older than the rule (AGO-12). `docs/models/idea-to-output.md`, §3.1, *The four Chain Links*, line 61: "A Work Approach stands on a Canonical Description, never on an Idea Model directly.". Every Work Approach stands on a Canonical Description, and §2 counts an Approach on Trial a Work Approach. The conventions manual, which stands on this model, says "An Approach on Trial carries none: it is first-time work, and stands on no Canonical Description until an evaluation places it" (§1.3, *The Foundation Line*, lines 114 to 116). The model's §4.2 agrees with the manual; its §3.1 does not. Which side: the model's §3.1, which is wider than its own §4.2. Why: older than the rule; neither text changed this part since the Approach on Trial was placed (ADR-0058). Proposed: fix: "A placed Work Approach stands on a Canonical Description, never on an Idea Model directly. An Approach on Trial stands on none yet (§4.2, *The upward direction*)."

`docs/models/tiers.md`

**FINDING-1470.** Agreement; resting on the reader, quote checked (left D8). §3.2, line 110: "an edit goes up", against §3.5 fact 5, "Nothing moves up as files". Proposed: fix: "an edit is read from above".

**FINDING-1471.** Agreement; resting on the reader; older than the rule (AGO-13). `docs/models/tiers.md`, §3.1, *Downward delivery*, lines 88 to 89: " what "a concept version" is;". The pin, a commit of the tier above, "is what 'a concept version' is". The exchange manual, which stands on this model, sends the concept's version to ADR-0003 and `CHANGELOG.md`'s comment (*What this does not cover*, line 592). There a concept version is a whole number, v1, moved only by a change that could invalidate a derived Agent Skill. The conventions manual's Foundation Line value is `concept v1` (§1.3). Many Delivery Pins share one concept version. Which side: the Tiers Model. Why: older text, from the handbook's model (`fc0b078`, 2026-09-27). Missed when the exchange took the Tiers Model as its foundation, at the Foundation Check's step 2. Proposed: fix: "a copy, always pinned at a commit of the tier above. The copy also names the concept version it derives from, which the Concept Repo's own log sets;".

**FINDING-1472.** Agreement; resting on the reader; older than the rule (AGO-4). `docs/models/tiers.md`, §3.3, *Upward harvest*, line 114; and §4.2, *The dependency rule*, line 169: "Up is harvest, and only through records: the tier above reads a". The tier above reads only the Run Repo's records ("Upward: only records", line 169). The exchange manual, which stands on it, reads three things, one of them not a record: "the diff of every held copy against its Delivery Pin" (§6.1, *Reading a CBC Run*, line 486). The model's own fact 4 (§3.5) says the same: "the edit is read from above as the diff". A copy is not a record (`docs/conventions/exchange/` §2.4, *The records' exception*: the records are the CBC Run's own, the copies are not). Which side: the Tiers Model's §3.3 and §4.2. Its §3.5 and the exchange agree with each other. Why: older text, from the handbook's model. Missed at `b06dc95`, as AGO-3. Proposed: fix §3.3: "Up is harvest, and only through what the Run Repo committed: its records, and the diff of its copies. The tier above reads them, read-only, and the Run Repo sends nothing." Fix §4.2: "Upward: only records, and the diff of the copies."

**FINDING-1473.** Agreement; checked; missed at a change (AGO-3). `docs/models/tiers.md`, §3.4, *The Delivery Pin and documents*, lines 125 to 129: "it holds wrong. That is why the Delivery Pin moves with every". "every delivery is a document, and its Delivery Pin moves with it", and "the Delivery Pin moves with every Delivery Take". The exchange manual, which stands on this model, says a Delivery Note without files is a take that moves only the Read-Through Commit: §2.5, line 174, "leaves the Delivery Pin where it was"; §6.6, line 562, "the Read-Through Commit moves, the Delivery Pin does not". Which side: the Tiers Model. It is too general: a delivery with no copy changes nothing the pin describes. Why: wrong from its first form, `ba29cb7` (2026-09-30), which cited the exchange for it. The exchange's note-only rule is older, `7c952e6` (2026-09-26). Missed again at `b06dc95` (2026-10-28), when the Tiers Model took the exchange's general facts: the Foundation Check's step 4 lists each disagreement. Proposed: fix: "That is why the Delivery Pin moves with every Delivery Take that brings a copy". Make the same change to "every delivery is a document, and its Delivery Pin moves with it": "every delivery that brings a copy".

##### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

`ARCHITECTURE.md`

**FINDING-1474.** Stale lines; resting on the reader, quote checked (left E1). §2.5, line 189: CBC Run 6's state, "born 2026-10-29 at `657d372`, on full auto", is out of date: `TODO.md` 38–39 says it ran through its Release, Step 14, and closed a Step 15. Proposed: fix: its state now.

**FINDING-1475.** Agreement; resting on the reader, met in passing (met AGO, SL2). §2, lines 130–132: "What derives from the concept is the method, the Stack Group and the playbook", where §2.2 (lines 148–149) says the Stack Group is "Not derived from the concept but checked against it". Proposed: fix: §2's opening follows §2.2.

**FINDING-1476.** Stale lines; resting on the reader, quote checked (left E2). header comment, line 13: "the live CBC Run" is singular; the table has held more than one CBC Run since. Proposed: fix: "the live CBC Runs".

**FINDING-1477.** Agreement; resting on the reader; missed at a change (AGO-6). `ARCHITECTURE.md`, §2, *The delivery and the CBC Runs*, lines 133 to 134: "ship*). This list is kept here: the chapters carry none". The concept's list is kept in `ARCHITECTURE.md`, and cites step 1 for it. Step 1 allows no list kept elsewhere. It excuses only an Idea Model, and the concept is a Canonical Description. The cited home does not say what the line says. Which side: the rule, probably. The concept has no *What this is made usable as*, and ARCHITECTURE has kept its list since `53fda69` (2026-10-21). Step 1 never said so. Why: the line was written against the conventions manual's old §3.5. The rule moved to facts-in-sync (`e2ad2e4`, ADR-0065), and nothing compared the two. Proposed: question: does facts-in-sync §4 step 1 gain "The concept's chapters carry no list: `ARCHITECTURE.md` §2 keeps it"? A Canonical Description may name a record, as long as it does not take a fact from it (§3.1, *What a Fact Reference is*). Or does the concept carry its own list, in `concept/00-cbc.md`?

**FINDING-1478.** Stale lines; resting on the reader; missed at a change (SL2-2). `ARCHITECTURE.md`, §2.1 *The Method Group* (lines 138 to 141), §2.2 *The Stack Group* (146 to 148), §2.3 *The Container Group* (156 to 159), the codemap (line 251) and the drawing (lines 39 to 46): "cbc-slice Agent Skills, under `.claude/skills/`, and the Output Shapes their Plan". Each group is listed by what it holds. None of the lists names the group's delivered Glossary Names file. These are `delivery/method/docs/glossary/method.md`, `delivery/spring-postgres/docs/glossary/stack.md` and `delivery/container/docs/glossary/container.md`. The drawing of a CBC Run's copies has no `docs/glossary/` either. Why: missed at a change. `3630ed9` (2026-10-31) created the three files, and its body says "every list of what is delivered names the three files". ARCHITECTURE's group lists were not among those lists. No Foundation Line ties them to the delivery, so no Change Walk reached them. Proposed: fix: - in §2.1, §2.2 and §2.3, add ", and the Glossary Names it delivers, `docs/glossary/<group>.md`" to each list; - in the codemap, `method/ the cbc-framing and cbc-slice Agent Skills, their Output Shapes and Glossary Names (§2.1)`; - in the drawing, add a `docs/glossary/ copies` row.

**FINDING-1479.** Agreement, Stale lines; checked; missed at a change (AGO-5; also SL2-1). `ARCHITECTURE.md`, §3, *What must stay true*, line 214: "| Every Agent Skill and Output Shape of the method states the concept version it derives from |". Every Output Shape of the method states a concept version, and the home is `docs/conventions/conventions/` §1.3. That section says an Output Shape names "the convention it lives under, `practice, under the shapes convention`". The four Output Shapes under `delivery/method/.claude/shapes/` all carry exactly that, and name no concept version. Only the two Agent Skills carry `concept v1`. Which side: ARCHITECTURE. Why: missed at a change. `c0eb1e6` (2026-11-01, a writing pass) turned "Every execution states the concept version" into this line and widened what it claims. The one-home rule's question at each changed line (rule 6) should have caught it. SL2-1 (Stale lines): every Output Shape of the method states a concept version. Conventions §1.3 says an Output Shape's line names "the convention it lives under, `practice, under the shapes convention`". All four do: `delivery/method/.claude/shapes/*.md`, line 2. No Output Shape states a concept version. Its proposal: fix: `| Every Agent Skill of the method states the concept version it derives from |`. The Output Shapes' line, the convention they live under, needs no row of its own. Proposed: fix: "| Every Agent Skill of the method states the concept version it derives from |".

`PLAN.md`

**FINDING-1480.** Stale lines; resting on the reader; older than the rule (SL2-4). `PLAN.md`, *The Plan Step Form*, *The Plan Step's own items*, lines 73 to 75: "the goal. For the exchange-birth Agent Skill's goal "a project born from this repo". The example gives a goal to the exchange-birth Agent Skill and an item about "CBC Run 5's birth entry". No exchange-birth Agent Skill exists. `TODO.md` line 62 says it is still to be written, its trigger "the CBC Run Birth after CBC Run 6's". CBC Run 5 was born by the Pure Seed on 2026-10-22. Why: older than the events that made it false. It was written 2026-10-17 (`cc3a875`), when CBC Run 5's birth was to run the exchange-birth Agent Skill. Round 3's read met it (refinement file, line 2250), and it was not fixed. Proposed: fix: take the example from a Plan Step that ran: "For Birth CBC Run 6's goal "CBC Run 6 is born from this repo at one Delivery Pin on main", one item is "CBC Run 6's birth entry names one Delivery Pin, ours, and nothing from another repo"."

**FINDING-1481.** Wiring; resting on the reader, met in passing (met DEO). lines 105, 201, 283: "(`.claude/approaches-on-trial/approach-drafting.md`, *Stages*, §3, *Close*)" mixes a title and a number in one address. Proposed: fix: the one form, number then title.

**FINDING-1482.** Stale lines; checked; missed at a change (SL2-5). `PLAN.md`, *Step: Take CBC Run 5's lessons for CBC Run 6*, Goal (lines 215 to 217) and Notes (lines 296 to 297): "Goal: CBC Run 6 can be born from files that carry what CBC Run 5 learned". - The goal is a CBC Run 6 not yet born. CBC Run 6 was born 2026-10-29 (`337788a`), while this Plan Step was stopped, and it has run through its Release (`TODO.md` lines 38 to 40). - The Notes say "then Birth CBC Run 6, on full auto, opens". It opened, and is itself stopped. Why: it became false at CBC Run 6's birth, after the Plan Step stopped. The devlog's Resume of 2026-10-29, later (`devlog/2026-10.md` lines 543 to 545), says "its goal names run 6, so it is rewritten on resume". That fact stands only in history. Proposed: question: rewrite the goal now, for example "CBC Run 5's CBC Run Reading has DECISION-1, DECISION-2 and DECISION-5 settled, and WORK-1 and WORK-3 to WORK-10 ended", and drop the Notes' "then Birth CBC Run 6 … opens"? Or leave it for the resume, with one line in the Plan Step saying so?

**FINDING-1483.** Stale lines; resting on the reader; missed at a change (SL2-6). `PLAN.md`, *Step: Take CBC Run 5's lessons for CBC Run 6*, own items, line 250: "- [ ] The playbook has no line meant for CBC Run 5 only.". Not yet true. It is true. `PLAN.md` lines 164 to 166, in Birth CBC Run 6, tick the same item: "taken here from the stopped Plan Step … (2026-10-29, `7f6e3a8`)". `delivery/fills/cbc-run-pure-playbook.md` names no CBC Run 5. Why: it came true in the other Plan Step on 2026-10-29. Only that Plan Step's copy was ticked. Proposed: fix: `- [x] The playbook has no line meant for CBC Run 5 only: taken by Birth CBC Run 6, on full auto (2026-10-29, `7f6e3a8`).`.

**FINDING-1484.** Stale lines; checked; missed at a change (SL2-7). `PLAN.md`, *Step: Refine this repo against its own rules*, Notes, lines 409 to 412: "made the approach-drafting Approach on Trial, and the first of the". The refinement is the first use of the approach-evaluation Approach on Trial. It is not. `.claude/approaches-on-trial/approach-evaluation.md` *Uses*, line 129 to 130, gives its first use: "`model-placing.md`'s first evaluation, 2026-10-28 … Its first use." Why: it was written 2026-10-20 (`4acf611`), when the refinement's close was to be the first evaluation. It became false on 2026-10-28. `bcf3010` (2026-11-01) reworded it for Names and kept it. Proposed: fix: "- The first use of first-time work on our Convention Seat, which ADR-0058 made the approach-drafting Approach on Trial. The approach-evaluation Approach on Trial was first used on 2026-10-28, for `model-placing.md`. This Plan Step's close judges both."

`README.md`

**FINDING-1485.** Stale lines; checked; missed at a change (SL2-3). `README.md`, the opening list, *What it holds*, lines 9 to 11: "Skill Templates and checklists, and Output Shapes, each pinned to". The Output Shapes are each pinned to the concept version they derive from. They are not: their Foundation Line is `practice, under the shapes convention`. They stand on a convention, not on a concept version. Why: missed at a change. `5d0f5ca` (2026-11-01, Round 3's close-read fix, "README names Agent Skill Templates and Output Shapes") added the Output Shapes to the sentence. It read for Names, not for truth. Proposed: fix: "And what is made usable from it: Agent Skills with their Agent Skill Templates and checklists, each pinned to the concept version it derives from, and the Output Shapes their Plan Step Gates read."

**FINDING-1486.** Stale lines; resting on the reader, quote checked (left E3). line 17: "a repo of its own pinned to a concept version". A CBC Run records a Delivery Pin, a commit; an Agent Skill's Foundation Line pins a concept version. SL2-3 meets a like claim at line 9. Proposed: fix, with SL2-3: "pinned to a commit of this repo".

`temp/README.md`

**FINDING-1487.** Stale lines; resting on the reader, met in passing (met SL2). line 12: A kept file is named by a TODO item or a Plan Step. `temp/run-6-handoff/` is tracked, and none names it. Proposed: question: an item names it, or it goes.

`TODO-CONVERSATION-MEMORY.md`

**FINDING-1488.** Wiring; resting on the reader, quote checked (left E11). §7, §8, §26: No TODO item and no other living record points at them, though the header says the item's See names each section. Proposed: question: each section is named by the item it serves, or marked as having none.

**FINDING-1489.** Stale lines; checked; missed at a change (SL2-21). `TODO-CONVERSATION-MEMORY.md`, header comment, line 21: "Last touched: 2026-10-31.". Last touched 2026-10-31. `a6f2a67` changed the file on 2026-11-01: its title, "TODO's Conversation Memory". Why: missed at a change. `a6f2a67`, a Writing fix, changed the title and not the date. Proposed: fix: `Last touched: 2026-11-01.`.

`TODO.md`

**FINDING-1490.** Stale lines; checked; missed at a change (SL2-8). `TODO.md`, *Next*, "Decide whether a commit plan's look-back also asks if the work could have been done better", Context, lines 87 to 88: "of them, and 2 changed the answer. CBC Run 5 tries it first, from". CBC Run 5 will try it. CBC Run 5 has run through Release and has been read. `temp/reading-run-5-2026-10-22.md` line 152 records the try: "FINDING-9. The look-back on trial: 13 lines, 0 tries". WORK-17 (line 549) gives this item that finding. Why: it became false when CBC Run 5 ran, 2026-10-22. Leftover E8 names this item's trigger (line 95), not this Context line. Proposed: fix: "CBC Run 5 tried it from its CBC Run Hand-off: 13 look-back lines, 0 tries (its CBC Run Reading, FINDING-9)."

**FINDING-1491.** Stale lines; resting on the reader, quote checked (left E8). lines 95, 113, 186, 199, 308, 682, 737, 773–774, 926–927: Triggers that look passed: "CBC Run 5's CBC Run Reading" (95, 113, 186, 199), which exists; the close of the Plan Step for CBC Run 5's birth (682, 926–927), closed 2026-10-22; "CBC Run 5's first Invariant Slice closing" (737); Refinement Round 2 (308, 773–774), closed. SL2 added 773–774 and 926–927, which the leftovers step left out. Proposed: question, item by item: each fired item is worked, re-aimed, or closed.

**FINDING-1492.** Stale lines; checked; missed at a change (SL2-9). `TODO.md`, *Next*, "Decide whether the concept, the conventions and the Approaches on Trial keep examples", Context, line 103: "The method's worked example, 271 lines in both the cbc-framing". 271 lines. Both copies, `delivery/method/.claude/skills/*/references/worked-example.md`, hold 328 lines today. Why: missed at a change. The count was right at `4620995` (2026-10-21). Round 3's rewrites of the file (`8316ce0`, `ce370e4`, 2026-11-01) grew it, and nothing re-reads a count in TODO when the counted file changes. Proposed: fix: "The method's worked example, 328 lines in both the cbc-framing".

**FINDING-1493.** Stale lines; checked; missed at a change (SL2-10). `TODO.md`, *Next*, "Evaluate the auto-run Approach on Trial", Context, line 192: "Context: drafted and used once, for CBC Run 5". Used once. It was used twice. `PLAN.md` line 151 says Birth CBC Run 6 used "the auto-run Approach on Trial, in its second use". The second use's note waits for that Plan Step's close (`PLAN.md` line 199). Why: it became false on 2026-10-29. Round 3's read met it (refinement file, line 2244), and it was not fixed. Proposed: fix: "Context: drafted for CBC Run 5 and used twice, for CBC Runs 5 and 6 (`.claude/approaches-on-trial/auto-run.md`, its use note; CBC Run 6's note waits for its birth Plan Step's close)."

**FINDING-1494.** Stale lines; checked by SL2: marked gone at `075a7ff`, it still stands; the joined-line search missed it, as parentheses now split the three words (left E6). lines 397–403: "three Chain Links, each with its upkeep: derives …, points …, governs …". The glossary (lines 220–222) and `docs/models/idea-to-output.md` §3.1 give four: stands on, points, governs, written from. Proposed: fix: the four Chain Links, by the glossary's words.

**FINDING-1495.** Stale lines; resting on the reader, quote checked (left E7). lines 433, 694–695, 747–748: Three items wait on "the next birth". CBC Runs 5 and 6 have been born since. The leftovers step named line 433 only; SL2 found the other two still stand. Proposed: question, item by item: each names the CBC Run Birth it waits on, or closes.

**FINDING-1496.** Stale lines; resting on the reader, met in passing (met SL1). lines 442–444: "though no Agent Skill or Plan Step asks it" is stale as SL1-7: the playbook's Step 2 asks it. Proposed: fix, with SL1-7.

**FINDING-1497.** Stale lines; checked; missed at a change (SL2-11). `TODO.md`, *Next*, "Decide whether our own forms become Output Shapes", Ideas, lines 479 to 481: "Only `.claude/decisions.md` holds one under another". Among the records, only the Decisions Log holds its form under a convention other than project-recording. `docs/glossary.md`, a record in `CLAUDE.md`'s records table, holds its form under the writing convention (line 23, `foundation: the writing convention`). Why: missed at a change. The line was written 2026-10-23 (`026640d`). `8919dac` (2026-10-27) gave the glossary its own file and its Foundation Line. No Change Walk reaches TODO. Proposed: fix: "Only `.claude/decisions.md` and `docs/glossary.md` hold one under another convention: agent-arrangement and writing."

**FINDING-1498.** Stale lines; checked; missed at a change (SL2-12). `TODO.md`, *Next*, "Rename the manuals, Agent Skills and Agent Rules that share a name", Context line 534 and Ideas line 544: "four of the names ship, so a rename moves every CBC Run's". Four of the five shared names ship, and line 544 says "four ship". All five ship: - `delivery/container/.claude/skills/` holds commit-messages, commit-plan, visual-comparison and retrospective; - `delivery/container/.claude/rules/writing.md` is the writing Agent Rule. Why: never true. The item was written 2026-10-31 (`72d76c7`, `0f91b8b8`). The shipped writing Agent Rule has existed since `83acdfe`, 2026-10-15. Proposed: fix: line 534, "all five names ship, so a rename moves every CBC Run's"; line 544, "hold-retrospective, write-plainly; all five ship, so every CBC".

**FINDING-1499.** Stale lines; resting on the reader, quote checked (left E4). line 538: "ADR-0078 when written". ADR-0078 exists. Proposed: fix: "ADR-0078".

**FINDING-1500.** Stale lines; resting on the reader; missed at a change (SL2-13). `TODO.md`, *Next*, "Read a CBC Run born before the refinement by its needs, not its diff", Context, lines 565 to 566: "item taken would land in text Refinement Round 3 rewrites.". Refinement Round 3 is still to rewrite the text. Round 3 closed at `c6b3635` (`PLAN.md` line 306). Why: written 2026-10-31 (`e7ee475`), before Round 3 closed on 2026-11-01. `bcf3010` reworded it and kept it. Proposed: fix: "The readings come after the refinement, not before: an item taken now could land in text the refinement's last read changes."

**FINDING-1501.** Stale lines; resting on the reader, met in passing (met LES, LAS). lines 642–675, "Rewrite the method's texts plain": The item lists FINDING-223, 224, 227, 228 and 206 as left here by DECISION-7 and DECISION-8. The refinement file's Round 3 *Endings* says round 3's layer 6 worked them, and *The work* names no commit. LES-1 to 18 and LAS-7 to 10 show 223, 224, 227 and 228 not worked; SL2-15 finds 206 and 224 gone. Proposed: question: the item's list and the Endings line are set by what the tree shows.

**FINDING-1502.** Stale lines; checked; missed at a change (SL2-14). `TODO.md`, *Next*, "Rewrite the method's texts plain", Context, lines 646 to 649: "Agent Skill and workflow (`2674c03`). Not yet, about 26,000 words:". The cbc-framing Agent Skill, the stack's Agent Skills, the concept chapters and System Readiness are not plain yet. Refinement Round 3 rewrote all of them against the writing rule. Examples are `1f0c17e` (the chapters), `4884a12` and `ce370e4` (cbc-framing), and `c449de0`, `580f7dc` and `78fe685` (the stack). DECISION-16, chosen (a): "All 188 are worked in layer 6 … the item closes with them, or keeps what the work left". Why: missed at a change. `e5a874b` and `bcf3010` (2026-11-01) reworded this Context for Names after the chapters were rewritten, and `bcf3010` after the method and the stack were too. Round 3 read for Writing only. The item's own trigger, "what Refinement Round 3 did leaves this item", was not acted on at Round 3's close. Proposed: question: by DECISION-16 (a), does the item close now? Or does it keep only what Round 3 left, its Context rewritten to name that?

**FINDING-1503.** Stale lines; checked; missed at a change (SL2-15). `TODO.md`, the same item, Ideas, lines 662 to 669: "citations of CBC Run 3's RETRO.". Refinement Round 2's FINDING-206, "the playbook's 12 citations of CBC Run 3's RETRO", and FINDING-224, "the 'lived' markers", wait in this item. Both are gone: - `7f6e3a8` (2026-10-29) removed exactly 12 RETRO lines from the playbook; its 4 left are the CBC Run's own `RETRO.md`; - grep finds no "lived" in `delivery/method/` or `delivery/spring-postgres/`, gone in Round 3 (`a6ccf5b`, `580f7dc`, `78fe685`). The refinement file's *Moved to TODO* (line 2354 to 2357) says these findings "are worked in this round's layer 6, by DECISION-16: the item keeps only what the round leaves". Why: missed at a change. The item was not trimmed when Round 3 worked these findings. Proposed: fix: drop FINDING-206 and FINDING-224 from the list. Check FINDING-223, 227 and 228 the same way, and drop what Round 3 fixed.

**FINDING-1504.** Stale lines; checked; missed at a change (SL2-16). `TODO.md`, *Next*, "Read what CBC Run 5's first Invariant Slice's Plan Step Gate found against the Evidence Test Shape", Context, lines 733 to 734: "Output Shapes at birth (the item on `.claude/shapes/`). The cbc-slice Agent Skill". It points at an open TODO item on whether a Newborn CBC Run reads its Output Shapes at birth. No such item exists. ADR-0061 (2026-10-21), "A newborn reads its shapes at the gate, not at birth", settled it, and its Context says "TODO held the question since 2026-10-17". The "unless" is decided. Why: it became false at ADR-0061, 2026-10-21. Round 3's read met it (refinement file, line 2247), and it was not fixed. Proposed: fix: "birth, so CBC Run 5 is the first clean one: since ADR-0061 a Newborn CBC Run reads its Output Shapes at the Plan Step Gate, not at birth. The cbc-slice Agent Skill".

**FINDING-1505.** Stale lines; checked; missed at a change (SL2-17). `TODO.md`, *Next*, "Decide whether a standing full read looks for missing Fact References", Context, lines 809 to 811: "close read ran with seven agents and 52 findings.". Round 2's close read ran its Dependencies Finding Kind with seven agents and 52 findings. The refinement file's *Round 2's close read* (lines 808 to 810 and 870 to 873) says otherwise: - the seven readers covered all four of Round 2's Finding Kinds, Dependencies on each side being two of them; - the 52 are all the readers' findings; - Dependencies had 19. Why: never true as written. It came in at `8a81a02` (2026-10-27). Proposed: fix: "repo for it today: their Dependencies Finding Kind, which two of Refinement Round 2's seven close-read agents ran, with 19 findings."

**FINDING-1506.** Stale lines; resting on the reader, quote checked (left E9). lines 819–821: "once the settled form is written there". `docs/conventions/facts-in-sync/` §3.1 now holds the one form. Proposed: fix: the wait goes.

**FINDING-1507.** Stale lines; resting on the reader, quote checked (left E10). lines 906–909: "only some say": FINDING-591's count was not worked, so the rule 4 gap stays open. Proposed: question: the count is taken now, or the line says it was not.

**FINDING-1508.** Stale lines; checked; missed at a change (SL2-18). `TODO.md`, *Later / someday*, "Decide what our CHANGELOG tracks", Context, line 934: "out. Since v1 (2026-08-28), about 1,350 commits added the". About 1,350 commits since v1. `git log --since=2026-08-28` counts 1,802 on main and 2,107 on this branch. Why: a dated count, right at `8042a18` (2026-10-21), never refreshed. Proposed: fix: "out. Since v1 (2026-08-28), about 1,800 commits on main added the". Or drop the number: "most commits since v1 added the".

**FINDING-1509.** Stale lines; uncertain; missed at a change (SL2-20). `TODO.md`, *Later / someday*, the Triggers of "Decide whether the Infrastructure Contract carries a paragraph on the store's facility" (line 989) and "Add a level for System Guarantees held by absence" (line 1197): "Trigger: CBC Run 5 meeting a System Guarantee held by absence.". Both wait for something CBC Run 5 will do. CBC Run 5 has run through Release and has been read. Its CBC Run Reading has no line on either; grep finds no "absence", "facility" or "Infrastructure Contract" in it. So either each trigger fired and was not seen, or it can no longer fire as written. Round 3's read met line 1197 (refinement file, line 2246): "its Run Reading can answer it". Why: the triggers name one CBC Run, now finished. Its reading did not ask them. Proposed: question: re-aim both at "a CBC Run's CBC Run Reading finds …", or ask them at CBC Run 5's remaining work?

**FINDING-1510.** Stale lines; resting on the reader, quote checked (left E5). line 1015, "Give the method a glossary": `delivery/method/docs/glossary/method.md` exists now (ADR-0078), so "the method has none" is false. Proposed: question: the item closes, or keeps what the glossary does not yet do.

**FINDING-1511.** Stale lines; resting on the reader; missed at a change (SL2-19). `TODO.md`, *Later / someday*, "Watch whether the worked example anchors a CBC Run's CBC Framing", Context line 1168 and Trigger lines 1172 to 1173: "Trigger: the next CBC Framing read on a different kind of". The trigger is still to come. CBC Run 5, `event-tickets`, framed a different kind of problem from the example's order service: two areas and a non-empty LAYER-5. Its CBC Run Reading read that framing on 2026-10-22, in *What run 5 teaches the worked example* (`temp/reading-run-5-2026-10-22.md` lines 422 to 445). The Context's "No evidence in three CBC Runs" also predates CBC Runs 4 to 6. Why: the trigger passed at CBC Run 5's Reading, and the item was not re-read then. Proposed: question: has the trigger fired, so that the item is now due with what CBC Run 5's Reading §6.3 found? Or does it wait for CBC Run 6's?

##### Layer 5: our agent setup

`.claude/approaches-on-trial/approach-drafting.md`

**FINDING-1512.** Stale lines; resting on the reader, quote checked (left F15). line 127, both copies: "The refinement is open." goes stale at the refinement's close. Proposed: fix at the refinement's close, in both Convention Seats: the line says what the refinement found.

`.claude/approaches-on-trial/auto-run.md`

**FINDING-1513.** Stale lines; checked; missed at a change (SL2-22). `.claude/approaches-on-trial/auto-run.md`, *Ways rejected*, lines 85 to 88: "makes any CBC Run full-auto. Rejected for now: one full-auto CBC Run has". One full-auto CBC Run has been lived. Three have: - CBC Run 4 (`TODO.md` line 418, "ran on full auto through Release"); - CBC Run 5 (this file's *Uses*); - CBC Run 6 (`TODO.md` lines 38 to 40). Why: written 2026-10-21 (`b1efa42`), before CBC Run 5's birth. It became false on 2026-10-22 and again on 2026-10-29. `e2d66ea` (2026-10-30) reworded it for Names and kept it. Proposed: question: is a rejection's reason Living Text, to be kept true ("three full-auto CBC Runs have been lived, and a shipped Agent Rule would decide for every CBC Run what three have shown")? Or does it say when it was weighed ("when drafted, one full-auto CBC Run had been lived")?

`CLAUDE.local.md`

**FINDING-1514.** Agreement; uncertain; the rule unclear (AGO-17). `CLAUDE.local.md`, line 3: "- Before any commit: stage it, show me the diff, and stop. Commit". The stop at every commit, one commit at a time, no push without the word. That is the commit-messages convention's rule (`docs/conventions/commit-messages/` §2.4, *Commit on the word*). The agent-arrangement manual itself calls it so: "The commit stop is not such a rule" (§3.5, line 344, pointing at §2.4). Line 5 does the same for a Change Set (`commit-plan` §6). But §3.7 also names "how often the agent stops for review" as a setting. Which side: unclear. The manual says both. Why: the rule is unclear: §3.7's example of a setting overlaps a rule another manual owns. Proposed: question: is "stop at every commit" a setting here, or the convention's rule? If a rule, lines 3 to 5 go, or keep only what differs from it. If a setting, §3.7 says the stop is one.

`.claude/rules/convention-manual.md`

**FINDING-1515.** Agreement; resting on the reader, met in passing (met LAO). line 20; conventions §2, lines 182–183: Each of the nine is "a `##` heading", but item 6, "A lesson points at its story", and conventions §2.6 are a rule for the body, not a heading (DECISION-9 counted it among the nine). Proposed: fix: "each a heading, but item 6, a rule for the body".

`.claude/rules/foundation-check.md`

**FINDING-1516.** Agreement; resting on the reader, quote checked (left F10). step 1: Step 1 lists where Foundation Lines sit and says "Only these are checked". It misses the delivered Glossary Names files, `delivery/*/docs/glossary/*.md`, which carry one in their header comment. AGO, in passing: it misses the playbook too, whose Plan Step Form comment carries `foundation: the project-recording convention`. Proposed: fix: step 1 names both, or names "any file whose header comment carries a Foundation Line".

`.claude/rules/one-home.md`

**FINDING-1517.** Agreement; resting on the reader, met in passing (met AGO). rule 7; `docs/conventions/exchange/` §3.8: Both put a *Decisions* footer on an Output Shape. Facts-in-sync §3.4 item 3 says only "A Work Approach", and the Idea-to-Output Model's §2 does not count an Output Shape one. No shipped Output Shape has a footer today. Proposed: question: facts-in-sync §3.4 names the Output Shape, or rule 7 and §3.8 drop it.

**FINDING-1518.** Agreement, Stale lines, One home; checked; missed at a change (AGO-1; also SL2-23, OHO-3). `.claude/rules/one-home.md`, *The rules*, rule 2, line 25: "copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the". After CBC Run Birth, only Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the concept go. Its home, `docs/conventions/exchange/` §3.2, *What goes*, line 205, also lists "each group's Glossary Names, in `docs/glossary/`". The retelling leaves out one of the five things that go. Which side: the Agent Rule. The exchange-deliver Agent Skill stages `docs/glossary/` too. Why: missed at a change. `3630ed9` (2026-10-31) added the Glossary Names to §3.2. The Change Walk's re-read of each retelling that names §3.2 should have caught it. `2158499` (2026-11-01) then edited this very line and kept the old list. SL2-23 (Stale lines): after CBC Run Birth, the copies that go are Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the concept. Exchange §3.2 also lists "each group's Glossary Names, in `docs/glossary/`". So does `.claude/skills/exchange-deliver/SKILL.md`, Stage 1 step 1 and Stage 2 step 2. Its proposal: fix: "copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial, each group's Glossary Names and the". OHO-3 (One home): the rule's example retells what goes after a CBC Run Birth, with its Fact Reference to `docs/conventions/exchange/` §3.2, *What goes*. Since `3630ed9` (2026-10-31), §3.2 also lists "each group's Glossary Names, in `docs/glossary/`". The retelling leaves them out, so the follower no longer matches its home. Its proposal: fix: "After CBC Run Birth, only the copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial, the Glossary Names and the concept (`docs/conventions/exchange/` §3.2, *What goes*)." Proposed: fix: "After CBC Run Birth, only the copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial, the Glossary Names and the concept (`docs/conventions/exchange/` §3.2, *What goes*)."

`.claude/rules/working-a-reading.md`

**FINDING-1519.** Wiring; resting on the reader, quote checked (left F9). line 4: Its Foundation Line, `practice, under the exchange convention`, uses the form conventions §1.3 gives an Output Shape, not the one for a convention's Work Approach. Proposed: fix: `foundation: the exchange convention`.

`.claude/rules/writing.md`

**FINDING-1520.** Agreement; resting on the reader, met in passing (met SL2). *Where it applies*, lines 106–109: "What CBC Runs read" does not name the delivered Glossary Names files. Proposed: fix: the list names them.

`.claude/skills/commit-messages/SKILL.md`

**FINDING-1521.** Agreement; resting on the reader, met in passing (met OHO). *The agent's own files*: `chore(agent)` covers Agent Skills and Agent Rules; the commit-messages manual §3 also puts Approaches on Trial under it. Proposed: fix: the Agent Skill names Approaches on Trial, in both copies.

`.claude/skills/exchange-deliver/SKILL.md`

**FINDING-1522.** Agreement; resting on the reader, met in passing (met OHO). Stage 2, step 2: Copies `.claude/approaches-on-trial/` and `.claude/shapes/` from every group; exchange §3.2 lists Approaches on Trial for the Container Group only, and Output Shapes for the Method Group and the Stack Group. Harmless today. Proposed: fix: the step names what each group ships.

**FINDING-1523.** Agreement; checked; missed at a change (AGO-2). `.claude/skills/exchange-deliver/SKILL.md`, *Stage 1 — write the Delivery Note*, lines 17 to 19. Again at step 7, line 93: "In `temp/note-to-<run>-<date>.md`, told, not delivered: the CBC Run". The Delivery Note is "told, not delivered", and the CBC Run "reads it through the Told Channel, as session input" (`docs/models/tiers.md` §3.2). Its foundation, the exchange manual, says otherwise in three places: - §6.6, line 562: "A Delivery Note alone, with no files, is still a delivery"; - §3.1: the Delivery Note is copied into the CBC Run's `temp/` with the delivery; - §3.7: "in a Delivery Note or in a prompt ... A prompt is the Told Channel's text, so the same holds for it". The prompt is the Told Channel; the Delivery Note is not. The Fact Reference also misses: Tiers Model §3.2 says "The Told Channel is not delivery", a warning handed as session input after the Run Repo's own work missed it. A file staged in `temp/` and read under the delivered-copies Agent Rule is not that. Which side: the Agent Skill. The old wording, "told not delivered", meant only that the Delivery Note is not a pinned copy. Why: missed at a change. `31156de` (2026-11-01, a writing pass) grew "told not delivered" into the Told Channel claim and its Fact Reference. The Foundation Check's step 2 reads the exchange manual beside such a change. Proposed: fix line 17 to 19: "In `temp/note-to-<run>-<date>.md`. It goes down with the delivery, but it is not a copy: the CBC Run reads it at the Delivery Take, and it goes when the take is done (`docs/conventions/exchange/` §4, *The Delivery Take*, step 5)." Fix step 7: "The CBC Run cannot open this repo, and a citation it cannot follow reads as its own."

`.claude/skills/exchange-read/SKILL.md`

**FINDING-1524.** Stale lines; resting on the reader, quote checked (left F12). line 9: "Four Agent Skill Stages, and the fourth writes a document", but Stage 2 already writes the document's first line. Proposed: fix: "and the document is begun at Stage 2 and finished at the fourth".

**FINDING-1525.** Agreement; resting on the reader, quote checked (left F11). Stage headings, lines 15, 23, 35; `.claude/skills/exchange-deliver/SKILL.md` lines 13, 102: Exchange-read capitalizes after the dash ("Find where to start"), exchange-deliver does not ("write the Delivery Note"); conventions §1.4's example is lowercase. Both number from Stage 1, while §1.4 and the glossary say "numbered from Stage 0". Proposed: question: Stage 0 is a rule or only the method's; the case follows §1.4.

##### Layer 6: `delivery/`, what ships

`delivery/container/.claude/decisions.md`

**FINDING-1526.** Agreement; resting on the reader, quote checked (left G6). lines 21–22: "The Delivery Pin is the Concept Deliverer's commit every copy here equals" drops "but for its *Decisions* footer", which `container.md` and delivered-copies rule 1 carry. Proposed: fix: the clause, or a Fact Reference to delivered-copies rule 1 in place of the definition.

**FINDING-1527.** Stale lines; resting on the reader, quote checked (left G3). lines 35–37; `delivery/container/.claude/CLAUDE.md` line 54; `delivery/installs/pure-seed.md` lines 131, 213, 228, 291: "Conventions: …", "a convention arrives", "the conventions held", and the Pure Seed's "conventions" say a CBC Run holds conventions. DECISION-32: it holds none, only the Work Approaches made from them. SL3-3 meets the same in the container's glossary. Proposed: fix, with SL3-3 and B3, in one wording.

**FINDING-1528.** Stale lines; resting on the reader, quote checked (left G2). lines 39–40: "Their decisions are cited CBC ADR-nnnn". Since ADR-0078 every delivery strips the footers, so a CBC Run meets no `CBC ADR-nnnn` in any shipped file. Proposed: fix: the sentence goes, or says the citations stay here.

`delivery/container/.claude/rules/delivered-copies.md`

**FINDING-1529.** Stale lines, Agreement; resting on the reader; missed at a change (SL3-5; also AGS-3). `delivery/container/.claude/rules/delivered-copies.md`, the frontmatter's `paths:` list, lines 2-8 (line 7 quoted): " - "docs/concept/**". The `paths:` list names the delivered places, so the Agent Rule loads when a copy is touched. It omits `docs/glossary/**`. Rule 1 of the same file (lines 26-28) says the delivered Glossary Names in `docs/glossary/` are pinned copies under one Delivery Pin. An edit to `docs/glossary/method.md` loads no rule that says it is a copy. Why: missed at a change. `3630ed9` made the delivered Names pinned copies, and its body says "every list of what is delivered names the three files"; it changed rule 1 and left the `paths:` list. AGS-3 (Agreement): the manual says the Agent Rule loads when a copy is read. The delivered Glossary Names in `docs/glossary/` are pinned copies; the Agent Rule's own rule 1 says so (line 28), as does `container.md`'s header ("changed only as .claude/rules/delivered-copies.md says"). But `paths:` lists `.claude/` folders, `docs/concept/**` and `temp/**`, and not `docs/glossary/**`. An agent editing a delivered glossary file never has the Agent Rule loaded. Its proposal: fix: add ` - "docs/glossary/**"` after line 7. (`docs/glossary.md`, the CBC Run's own record, stays out of the glob.) Proposed: fix: add ` - "docs/glossary/**"` after line 7. The pattern matches the folder only, not the CBC Run's own `docs/glossary.md`.

**FINDING-1530.** Agreement; resting on the reader, quote checked (left G4). rule 5: Rule 5 has no Receipt Branch step. `docs/conventions/exchange/` §4, step 3, has the CBC Run cut one, optionally, so step 2's diff is exact. `container.md` has no Receipt Branch entry. Proposed: question: the Agent Rule gains the step and the glossary the entry, or exchange §4 says the branch is the Concept Deliverer's.

**FINDING-1531.** Agreement; checked; missed at a change (AGS-4). `delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 6, line 119: " 6. **Write one Decisions Log entry** carrying both numbers: the new". The manual's step 5 lists the entry's contents: the date, the Delivery Pin, what came, what was declined and where its need went. It does not name the Read-Through Commit. The Agent Rule's entry carries the Delivery Pin and the Read-Through Commit, and not what came or what was declined. Each side lacks part of the other's list. Which side: both, in part. The manual's §2.2, agent-arrangement §3.4 and the Decisions Log's Record Stub all say every delivery entry carries both numbers, so the manual's step 5 is short of its own §2.2. The Agent Rule drops what came and what was declined, though it says elsewhere (rule 5, after step 7) that "the Decisions Log entry says so" of a declined need. Why: the Read-Through Commit was added to §2.2 and the Agent Rule after step 5 was written; neither change re-read the other list. Proposed: question: one list in both. The recommended form: "One entry: the date, the new Delivery Pin, the Read-Through Commit the Delivery Note names, what came, and each declined edit with where its need went." The manual's step 5 and the Agent Rule's step 6 both take it.

`delivery/container/.claude/rules/one-home.md`

**FINDING-1532.** Agreement; resting on the reader; missed at a change (AGS-2). `delivery/container/.claude/rules/one-home.md`, *Not a second home*, line 43: "History: the devlog, closed ADRs, commit bodies, the entries of". The manual's §1 holds that a fact stated only in history gets a home in Living Text before anything retells it (ADR-0070, decision 6, which is not marked as our seat's only). Our one-home Agent Rule carries it at line 60. The container's *Not a second home* stops at "history is not a second home". A CBC Run keeps a devlog and a Decisions Log, and meets the same risk. Which side: the Agent Rule, unless the fact is meant for our seat only. The manual's *The CBC Run's seat* does not say either way. Why: missed at a change: `a5c5a8e` (ADR-0070) wrote the line into facts-in-sync §1 and ours. The container's copy was not walked for it. Proposed: fix, with AGS-1: add "A fact stated only in history gets a home in Living Text before anything retells it." Or question: is the rule our seat's only? Then facts-in-sync, *The seats*, says so.

**FINDING-1533.** Agreement, Writing; checked; missed at a change (AGS-1; also WF-9). `delivery/container/.claude/rules/one-home.md`, *Not a second home*, line 45: "never updated, so they cannot drift. The Decisions Log's header". The manual says every file's header comment is Living Text, the history files' included. The Agent Rule names only the Decisions Log's header comment. A CBC Run's devlog and CHANGELOG also carry header comments that hold their forms and Foundation Lines; read by the Agent Rule, they are history and never updated. The container's glossary sends Living Text to this section (`container.md` line 52), so the CBC Run's only account of Living Text is the narrow one. Which side: the Agent Rule. Its line predates the manual's sentence. Why: missed at a change. `0cdd102c` wrote the manual's sentence (DECISION-35). Its Foundation Check said "the two one-home Agent Rules, which follow in commit 13". Ours followed at `fab7214`; the container's took only the released-entries line, at `ae8eb31`. The Change Walk of `0cdd102c` should have caught it. WF-9 (Writing): "The Decisions Log's header comment is living text." The Name is written in lowercase. Our copy writes "Living Text". Its proposal: fix: "comment is Living Text." Proposed: fix: lines 45-46 become "never updated, so they cannot drift. **Living Text** is every text but history. Each file's header comment is Living Text, the history files' included." (The bold is the Name's defining line in the CBC Run's seat, where its glossary entry points.)

`delivery/container/.claude/rules/shapes-lifecycle.md`

**FINDING-1534.** Agreement; resting on the reader; missed at a change (AGS-5). `delivery/container/.claude/rules/shapes-lifecycle.md`, §3 *A difference at the close*, line 68: " changes: a project's own with a dated line, a delivered one under". The Agent Rule asks a dated line in a project's own Output Shape when it changes. The manual has no dated line. It says outputs closed before a change are not reopened, and the difference between them records when the Output Shape changed. `61fcc5d` removed the manual's dated lines, about seven places, and kept this one in the Agent Rule. Which side: the Agent Rule, probably. The manual's reason covers both kinds of Output Shape, and the writing of history into a file is what delivered-copies rule 2 forbids for a copy. If a CBC Run's own Output Shape does need a dated line, the manual should say so in its *The CBC Run's seat*. Why: missed at a change: `61fcc5d` (ADR-0052). Its body says a delivered Output Shape changes "under delivered-copies rather than with a dated line", and kept the line for a project's own. ADR-0052 is silent on it. Proposed: question: drop "with a dated line" ("a project's own in place, a delivered one under the delivered-copies Agent Rule"), or the shapes manual names the dated line for a CBC Run's own Output Shapes.

`delivery/container/.claude/rules/writing.md`

**FINDING-1535.** Agreement; resting on the reader; missed at a change (AGS-6). `delivery/container/.claude/rules/writing.md`, rule 10, line 72: " The point goes in the first sentence. A record's fixed headings, an Agent Skill Stage or Approach on Trial Stage heading, and a". The manual says rule 10 holds for numbered sections in both Convention Seats, and exempts three things: the manual form's fixed headings, a stage heading, and a numbered rule's bold lead. The Agent Rule exempts "a record's fixed headings" instead. A CBC Run writes no manual, so the manual's first exemption is empty there; the Agent Rule puts a wider one in its place, which the manual never names. Which side: the manual, probably. The substitution was deliberate ("the headings a run holds among the exemptions"), and it is the CBC Run's equivalent. But it stands nowhere in the Canonical Description. Why: missed at a change: `25b3946`. Its Foundation Check says "the two copies differ in their examples only, as ADR-0069 allows". They also differ in this exemption. Proposed: question: the manual's rule 10 names, for the CBC Run's seat, a record's fixed headings beside the manual form's; or the Agent Rule drops the exemption.

`delivery/container/.claude/skills/apply-retrospective/SKILL.md`

**FINDING-1536.** Agreement; resting on the reader, quote checked (left G7 apply-retrospective). lines 89–90: "Links point at labels, never section numbers", against one-home rule 2, whose Fact Reference carries the section number with its title. Proposed: fix: "Links carry a label and, where there is one, its section number and title".

`delivery/container/.claude/skills/retrospective/SKILL.md`

**FINDING-1537.** Agreement; resting on the reader; missed at a change (AGS-7). `delivery/container/.claude/skills/retrospective/SKILL.md`, *Stage 4 — close*, item 3, line 114: " line naming that decision. The Decisions Log gets a "rules in". The Agent Skill puts a "rules in force now" list on top of the Decisions Log at the retrospective. The manual says the log is append-only and dated, in entries of three parts, and names no such list. The stub says newest last. The retrospective manual, the Agent Skill's own foundation, names no list either. Which side: the manuals. CBC Run 3 and CBC Run 4 each wrote the list at their retrospective (our Decisions Log, 2026-10-17). Practice is the evidence. The fact lives only in the Agent Skill and in history. Why: missed at a change: `d1922c4`. Its Foundation Check read agent-arrangement §3.4 and said "the retrospective skill agrees", without weighing "on top" against "append-only". Proposed: question: agent-arrangement §3.4 (or the retrospective manual §4) gains the list, as the one part of a CBC Run's log not appended, and the stub's header says so; or the list goes to `RETRO.md`.

**FINDING-1538.** Agreement; resting on the reader, quote checked (left G7 retrospective). line 118: The Concept Deliverer writes each lesson into the next CBC Run's PLAN, against the playbook (lines 87–88) and the Pure Seed (lines 3–4), which say the Newborn CBC Run writes its own. Proposed: question: who writes the next CBC Run's Plan Steps.

`delivery/container/docs/glossary/container.md`

**FINDING-1539.** Stale lines; checked; missed at a change (SL3-3). `delivery/container/docs/glossary/container.md`, the Decisions Log entry, line 91: " decisions, the conventions held, and each delivery's Delivery Pin". The Decisions Log holds "the conventions held". Since ADR-0078 (DECISION-32) a convention is its manual, and a CBC Run holds none, only the Work Approaches made from them. Leftover G3 lists the same claim in `decisions.md` 35-37, `.claude/CLAUDE.md` 54 and the Pure Seed, but not this line. Why: missed at a change. `3630ed9` (2026-10-31) moved the entry into this file the same day ADR-0078 was written; the Change Walk from ADR-0078 did not reach it, and Round 3's close read (reader G) listed its siblings and not this one. Proposed: question: fix it in the same words as G3's lines, in the same commit, so the four say one thing.

**FINDING-1540.** Agreement; checked; missed at a change (AGS-8). `delivery/container/docs/glossary/container.md`, entry *Glossary Name*, line 99: " or more words, capitalized, written exactly; what this file lists.". The entry says a Glossary Name is "the name of a thing this project defines ... what this file lists". In `container.md` neither half is true. This file lists the shared Names, which the Concept Deliverer defines. The project's own are `docs/glossary.md`'s, as the file's own header says (line 8-9). Which side: the entry. Why: missed at a change: `3630ed9` moved the entry, word for word, from the CBC Run's glossary record into the pinned copy. Its Change Walk did not re-read the moved entries. Proposed: fix: "- **Glossary Name** — the name of a defined thing: two or more words, capitalized, written exactly; this project's own are listed in `docs/glossary.md`, the delivered ones in `docs/glossary/`."

`delivery/container/PLAN.md`

**FINDING-1541.** Agreement; unverified, no quote to search (left G7 PLAN Now). the placeholder Plan Steps: The placeholder Plan Steps have no "Now:" line, which the Plan Step Form gives. Proposed: fix: each takes its line.

`delivery/installs/pure-seed.md`

**FINDING-1542.** Agreement; resting on the reader, quote checked (left G11). line 9: "finishes the CBC Run Birth", against the glossary's "a CBC Run's first state". As C11. Proposed: question, with C11.

**FINDING-1543.** Stale lines; checked; missed at a change (SL3-2). `delivery/installs/pure-seed.md`, step 4's bold lead, line 123; also line 6 and line 122: "Delivery Pin in the subjects.** One commit per delivery. The subject". One commit per delivery (123); "commit the deliveries there" (122); "Every delivery is a commit on a Receipt Branch" (6). The same file says the CBC Run holds one delivery (line 94, "One Delivery Pin, because the CBC Run holds one delivery"; the prompt, lines 211-212, "one delivery ... in two halves"), and step 4 makes four commits of it (line 290, "Four commits on birth-seed"). Why: missed at a change. The words date from `f9342dd` (2026-09-07), when the seed made "the five deliveries". ADR-0025 and ADR-0036 made the container part of one delivery at one Delivery Pin; lines 94 and 173-175 were brought to that, these three were not. `5d562d8` reworded all three and kept the claim. Proposed: fix: - line 6: "The delivery is committed on a Receipt Branch, `birth-seed`, in four commits. That" - lines 122-123: "**4. Cut the Receipt Branch and commit the delivery there, the Delivery Pin in every subject.** One commit per part of the delivery. The subject"

**FINDING-1544.** Agreement; resting on the reader, quote checked (left git add). line 158: The seed's `git add .claude/skills .claude/shapes docs/glossary` leaves out `.claude/rules`. No Method Group or Stack Group file is under `.claude/rules/` today, but `delivery/README.md` lines 33–34 says those groups carry Agent Rules. Proposed: fix: add `.claude/rules`, so the line holds when a group first ships one.

**FINDING-1545.** Stale lines; resting on the reader; missed at a change (SL3-6). `delivery/installs/pure-seed.md`, step 6's prompt, line 215; also the check after it, lines 290-292: "- then docs/concept/, five method and stack Agent Skills, the". The prompt lists what the second half of the delivery holds: the concept, five Agent Skills, four Output Shapes, the Plan Steps. The third seed commit also adds `docs/glossary/method.md` and `docs/glossary/stack.md` (line 158, `git add ... docs/glossary`). The check at lines 290-292 lists the same commit as "the method and stack Agent Skills with the method's Output Shapes", without them. Why: missed at a change. `3630ed9` created the two files and added `docs/glossary` to line 158. It did not update the prompt or the check, though its body says every list of what is delivered names the three files. Proposed: fix: - line 215-216: "- then docs/concept/, five method and stack Agent Skills, the method's four Output Shapes, their Glossary Names, and the Plan Steps in PLAN." - line 292: "Agent Skills with the method's Output Shapes and their Glossary Names, the Plan Steps into PLAN."

**FINDING-1546.** Stale lines; checked; missed at a change (SL3-1). `delivery/installs/pure-seed.md`, the reader's checklist after step 6 ("What the agent is left to do"), line 329: "- Step 0 closed clean on the Plan Step Gate the container wrote for". The container wrote Step 0's Plan Step Gate. Nothing writes it. The Pure Seed replaces the PLAN Record Stub's placeholder Plan Steps, its Step 0 Gate with them, with the playbook's (`pure-seed.md` lines 161-164). The playbook's Step 0 has an empty `Gate:` (`delivery/fills/cbc-run-pure-playbook.md` line 148), and its Plan Step Form says the Plan Step Gate is written when the Plan Step opens (line 58). So the agent writes Step 0's Gate. Why: missed at a change. Playbook v3 (2026-09-06) stripped Step 0's gates to "derived when this step opens"; the line, then "Step 0 closed clean on its container gates", was already false at `f9342dd`. `5d562d8` reworded it to name the Plan Step Gate and did not check the claim. Round 1's Stale lines read and its close read missed it too. Proposed: fix: "- Step 0 closed clean on the Plan Step Gate the agent wrote when it opened. No Plan Step Gate waits on the CBC Run Briefing: it opens CBC Framing."

`delivery/method/.claude/shapes/evidence-test.md`

**FINDING-1547.** Stale lines; checked; missed at a change (SL4-2). `delivery/method/.claude/shapes/evidence-test.md`, *What this document controls*, line 25: "a Structural Wall Check, which reads the code;". The line says a Structural Wall Check reads the code. Three other texts describe it differently: - the cbc-slice SKILL's Stage 3 step 5, lines 194-197, and the method glossary, lines 225-227: it sends a Structural Wall its refusal directly, or reads it where it is defined; - this Output Shape's own *What is exempt, and why*, lines 174-177: it reads the store's list of its constraints, or sends the store a refusal; - the worked example, lines 301-303: its Structural Wall Check is a second row written straight to the store and refused. None of these reads the code. Why: missed at a change. The line began as "a structural test, which reads the code" (`31d8a78`, 2026-10-15). `8a4525b` (2026-11-01) put the Name Structural Wall Check in its place and kept the old description. Nobody read the Name's glossary entry beside the line. Proposed: fix: "a Structural Wall Check, which sends a Structural Wall its refusal directly or reads it where it is defined, and is not evidence;"

**FINDING-1548.** Agreement; resting on the reader, quote checked (left H3). lines 47 and 81; `cbc-slice/SKILL.md` 97 and 185: The evidence label differs: "· GUARANTEE-3 — KILL-3" with a dash, against "· GUARANTEE-2 · KILL-12" with a middle dot. Proposed: fix: one form; the Output Shape's, as what the close reads against.

**FINDING-1549.** Stale lines; resting on the reader, met in passing (met SL4). line 122: Quotes SLICE-2's invariant as "a retry after a crash ends in one order and one truthful answer". The worked example, lines 218–219, words it "a crash at any point leaves the system where a retry ends in exactly one order and one truthful answer". Proposed: fix: the quote takes the source's words.

`delivery/method/.claude/shapes/kill.md`

**FINDING-1550.** Agreement; checked; known, and deferred to TODO (AGS-10). `delivery/method/.claude/shapes/kill.md`, *The shape*, line 74 (template at 51-56): "- **An Enemy Collision that breaks nothing stays in the list,**". The Output Shape gives a collision where nothing dies a `KILL-<n>` tag. In the concept an Enemy Collision Kill is what dies. Which side: not clear. CBC Run 5 carried such a kill, and TODO.md 653-656 plans to move the worked example toward the Output Shape. Why: known and deferred (devlog 2026-10), waiting for the plain rewrite. Proposed: question: is a collision where nothing dies an Enemy Collision Kill (the concept and glossary widen), or a tried Enemy Collision under another tag (the Output Shape changes)? The worked example, the workflow and the registry template follow.

**FINDING-1551.** Stale lines; resting on the reader, quote checked (left H4). line 83: "FACT-CALLER-1 to FACT-STORE-6": a range over the tags of four different actors. Proposed: fix: list them, or "the FACT tags of the four actors".

**FINDING-1552.** Agreement; resting on the reader, quote checked (left H5). lines 105–108: The illustrated "nothing dies" Enemy Collision Kill starts with NOT-OURS-1, a Scope Exclusion; the Skeleton (60–61) says it starts with the Enemy Fact. AGS-10 asks whether such a collision is a Kill at all. Proposed: decided with AGS-10.

`delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md`

**FINDING-1553.** Wiring; resting on the reader, met in passing (met DES). line 112; `cbc-slice/SKILL.md` line 96; and 15 shipped references: 15 shipped references quote a numbered rule's bold lead whole, past 30 characters, such as "*An Agent Skill Template is copied and filled, never edited in place*"; facts-in-sync §3.1 cuts it to 30 with "…". These two give "rule 6" with no lead at all. Proposed: question: §3.1's cut reaches a rule's bold lead, or a lead is quoted whole.

**FINDING-1554.** Agreement; resting on the reader, quote checked (left H2). lines 244–267: The workflow names three Enemy Census Probe Lenses but calls the first listing, "actors × the three negations", a lens too: three or four. The glossary says "the workflow names three". Proposed: fix: line 244 is not called a lens.

`delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`

**FINDING-1555.** Agreement; resting on the reader; older than the rule (AGS-11). `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *Working one Invariant Slice*, line 85: "- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees, the proof,". The concept's Document phase records what is promised, the Structural Wall, and how it survived. The page swaps the Structural Wall for the Invariant Slice Guarantees. Which side: the page. Why: older than the rule: `edecd0e`, reworded at `8316ce0` and `60398b1`. Proposed: fix: "- **Document:** what is promised, the Structural Wall that holds it, and the proof, readable later."

`delivery/method/.claude/skills/cbc-framing/references/worked-example.md`

**FINDING-1556.** Agreement; unverified, no quote to search (left H8). lines 115–123, both copies: Leaves two of the three lists the workflow (298–317) says the exit leaves; no Scope Verdicts list, not even an empty one. Proposed: fix: an empty Scope Verdicts list, in both copies.

**FINDING-1557.** Agreement; resting on the reader, quote checked (left H7). line 247, both copies: Puts "the CBC Framing Concerns" in LAYER-4-PROBLEMS, while Stage 3 (framing SKILL 61, `kill.md` 8) puts the Enemy Collision Kills there. Proposed: fix: the worked example follows Stage 3, in both copies.

`delivery/method/.claude/skills/cbc-framing/SKILL.md`

**FINDING-1558.** Stale lines; checked; missed at a change (SL4-1). `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*, line 51: "and recorded in the record the records table names for sign-offs. Delegation changes who". The line says a CBC Run's records table names a record for sign-offs. The container's table (`delivery/container/.claude/CLAUDE.md`, *Records*) has 12 rows, and none of them names sign-offs. The same SKILL, in *The record*, line 178, gives CBC Framing's verdicts one home: "inline in the CBC Framing Derivation". So the line points at a row that does not exist. Why: missed at a change. Commit `ce370e4` (2026-11-01) replaced "where the records put sign-offs" with a claim about the records table. Its Foundation Check read concept v1 only. Nothing checked the new claim against the container's records table. Proposed: fix: "and recorded inline in the CBC Framing Derivation, as *The record* says. Delegation changes who"

**FINDING-1559.** Agreement; resting on the reader, met in passing (met LAS). lines 57–65: Gives its Agent Skill Stages no headings, only a code block and the *Each Agent Skill Stage's Exit* list. Conventions §1.4 puts each Agent Skill Stage under its own heading. Proposed: question: §1.4 reaches the method's Agent Skills, or says it does not.

**FINDING-1560.** Agreement; resting on the reader, quote checked (left H9). lines 85–86; glossary 98–99; workflow 156–157: The System Possession Test reads "could they break the Falsifiable Promise?" in two places, and "… without us being able to stop them?" in the workflow. Proposed: fix: the glossary's words in all three.

**FINDING-1561.** Agreement; resting on the reader, quote checked (left H1). lines 101–102; workflow 291; `the-whole-system-in-plain.md` 62–63: Enemy Census Saturation is stated in three units: "two consecutive fresh Enemy Census Probes", "two consecutive ones" (the lenses), "two fresh attacks". The glossary says Enemy Census Probes. Proposed: fix: all three in the glossary's unit.

`delivery/method/.claude/skills/cbc-framing/templates/registry.md`

**FINDING-1562.** Stale lines; resting on the reader; missed at a change (SL4-4). `delivery/method/.claude/skills/cbc-framing/templates/registry.md`, the SLICE-1 entry, *Answered at close*, line 52. The same claim is in `delivery/method/.claude/shapes/registry-entry.md`: - lines 51-53, the shape; - lines 66-67, the skeleton; - lines 111-112, the check, question 4: "Then one line per Adversity Flag or judgment it settled: the answer". The Agent Skill Template and the Invariant Slice Entry Shape say *Answered at close* holds one kind of line: each Adversity Flag or judgment the Invariant Slice settled. The cbc-slice SKILL asks for three kinds: - Stage 4 step 2, lines 227-230: "what the Invariant Slice left provisional; what it hands to later Invariant Slices, by name; each Adversity Flag or judgment it settled"; - Stage 4 Gate 1, lines 248-250: "what it left provisional and what it hands on, one line each". An entry filled by the template and passed by the Output Shape fails the Agent Skill's Gate. Why: missed at a change. The SKILL's three kinds came in with `2674c03`, and the Output Shape with `6cfd7ad`, both on 2026-10-15. The Output Shape was written without being read against Stage 4. The template's slot was never changed. Proposed: question: are provisional items and hand-ons lines under *Answered at close*? Recommended: yes, as the SKILL says. The template's slot, the Output Shape's field, its skeleton bullet and check question 4 then name all three kinds.

`delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`

**FINDING-1563.** Agreement; resting on the reader, quote checked (left H6). line 40: The four Output Shapes' headers say "Read at … Plan Step Gate", while the workflow says the Invariant Slice Record Shape "is read at the Invariant Slice Close". Proposed: fix: one moment, the Output Shape's own.

**FINDING-1564.** Stale lines; resting on the reader, quote checked (left H13). *Open*, line 453: "CBC Run 4's is not yet read" may be stale: CBC Run 4 has been read. Proposed: fix, once checked against the reading of CBC Run 4.

`delivery/method/.claude/skills/cbc-slice/references/system-readiness.md`

**FINDING-1565.** Agreement; resting on the reader, met in passing (met AGS-method). lines 12–15: READINESS-1 asks only for a `chosen-next` Invariant Slice. Slice SKILL 39–42 also asks for the CBC Framing Reconciliation. Proposed: fix: READINESS-1 names both.

`delivery/method/.claude/skills/cbc-slice/SKILL.md`

**FINDING-1566.** Agreement; checked; older than the rule (AGS-9). `delivery/method/.claude/skills/cbc-slice/SKILL.md`, the opening, line 11: "non-negotiable: **the test that creates the adversity exists and". The Agent Skill makes the completion test one thing: the adversity test exists and passes. The concept needs two: the Structural Wall stands, and the proof exists. Which side: the Agent Skill's opening. Its own Stage 2 and Stage 3 Gates already require the Structural Wall. Why: older than the rule; rewrapped at `06a3915`. Proposed: fix: "The completion test is non-negotiable: **the Structural Wall stands, and the test that creates the adversity had its Red Run and passes.**" Or question: left to the TODO item.

**FINDING-1567.** Agreement; resting on the reader, met in passing (met SL4). line 225: The Invariant Slice Entry "went to `in-progress` when the Correctness Specification landed". No Stage 1 step tells the agent to set it. Proposed: fix: Stage 1 gains the step.

**FINDING-1568.** Agreement; resting on the reader, quote checked (left H11). line 233; workflow 201: "`ARCHITECTURE.md`'s Invariants table" against "the Invariants section's own comment". The container's `ARCHITECTURE.md` has a section, `## Invariants`. Proposed: fix: "section" in both.

`delivery/method/docs/glossary/method.md`

**FINDING-1569.** Agreement; resting on the reader, met in passing (met AGS-method, SL4). lines 162–165: The CBC Framing Reconciliation accounts for every CBC Framing Concern. Framing SKILL 238–239 and the template 84–85 say every Enemy Collision Kill. Proposed: fix: one scope, the Agent Skill's.

`delivery/README.md`

**FINDING-1570.** Wiring; resting on the reader, met in passing (met DES). line 5: "`ARCHITECTURE.md`'s (§2, *The delivery and the CBC Runs*)" uses the same-document form for another file. By facts-in-sync §3.1 it reads as `delivery/README.md` §2. Proposed: fix: "(`ARCHITECTURE.md` §2, *The delivery and the CBC Runs*)".

**FINDING-1571.** Stale lines; checked; missed at a change (SL3-4). `delivery/README.md`, §6 *When it lands*, line 90: "that run much later. Each Agent Skill's Stage 0 refuses to start". Every Agent Skill's Stage 0 refuses to start before its inputs exist. True of cbc-slice, cbc-bootstrap, infra-establish and infra-serve. False of the others that copy at birth: - the retrospective and apply-retrospective Agent Skills, for Plan Steps N-2 and N-1: their Stage 0 cuts a branch and opens the work, and checks no input; - the cbc-framing Agent Skill: its Stage 0 chooses the Falsifiable Promise; - commit-messages, commit-plan and visual-comparison: no Stage 0. Why: missed at a change. Before `5d562d8` the line read "Each practice skill's readiness gate refuses to start", which was true of the Stack Group. The rewording to Glossary Names widened "practice skill" to every Agent Skill. Proposed: fix: "that run much later. The Stage 0 of the cbc-slice Agent Skill and of the Stack Group's three Agent Skills refuses to start" (the rest of the sentence as it stands).

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`

**FINDING-1572.** Agreement; resting on the reader, quote checked (left I6). lines 80–83: Sends a departure from the Stack Default, a reference's choice, to delivered-copies rule 8, which governs Agent Skill Templates. It fits only by analogy. Proposed: decided with AGS-15, which weighs the same departure.

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`

**FINDING-1573.** Stale lines; checked; missed at a change (SL4-3). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *4. The Adversity Harness*, *The Adversity Harness in the codebase*, line 186: " `infrastructure/bootstrap.sql` the Runtime Ground uses; ". The line puts the Runtime Ground's `bootstrap.sql` at `infrastructure/bootstrap.sql`. Every other file puts it at `infrastructure/postgres/init/bootstrap.sql`: - the template's own path line (`infra-establish/templates/bootstrap.sql`, line 5); - the compose mount (`compose.yaml`, line 21); - `.env.example`, line 15; - the setup walkthrough's §3, line 79; - `spring-harness-reference.md`'s `DatabaseIT`, line 98, and its javadoc, line 85. A CBC Run that follows this line mounts a file that is not there. Why: missed at a change. `a6ccf5b` (2026-11-01) rewrote "the same bootstrap SQL the ground uses" and added the wrong path. The Wiring script skips a CBC Run's own paths, and the rewrite was not checked against the templates. Proposed: fix: "`infrastructure/postgres/init/bootstrap.sql` the Runtime Ground uses;"

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`

**FINDING-1574.** Agreement; uncertain; older than the rule (AGS-14). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, §4, line 374; with `spring-boot-walkthrough.md` §5, line 240 on: " * Class the first Invariant Slice needs, end to end through the real". The references state contention as the first Invariant Slice's Adversity Class and show only a burst. READINESS-4 asks for the class the Invariant Slice names; the worked example's SLICE-1 is duplicate delivery. Which side: the references, if read as generic. Why: older than the rule; reworded at `a6ccf5b` without reading READINESS-4. Proposed: question: the harness reference gains a variation point, "the probe's test follows the CBC Bootstrap Adversity Class; the burst is the shape for contention".

**FINDING-1575.** Agreement; checked; older than the rule (AGS-13). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, §5, line 452: " demands it, and the method deletes it.". The CBC Bootstrap Probe is said to be demanded and deleted by "the method". No Method Group file names the probe; the demand and the deletion are the cbc-bootstrap Agent Skill's own. Which side: the stack line, written before the Method Group and Stack Group split (`657d6eb`). Why: older than the split (`8ed34e9`); missed again at `a6ccf5b`. Proposed: fix: "the CBC Bootstrap Probe crosses into `main/`, because the CBC Bootstrap needs a door to attack, and the first Invariant Slice deletes it."

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`

**FINDING-1576.** Agreement; resting on the reader, met in passing (met AGS-stack). its close: Never names System Readiness or its sign-off. Framing SKILL lines 291–294 make the sign-off the gate before Invariant Slice work; the CBC Bootstrap's close hands over without asking for it. Proposed: question: the close asks for the sign-off, or the playbook's Step order carries it.

**FINDING-1577.** Agreement; resting on the reader; missed at a change (AGS-12). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, Stage 1, line 75; with `references/app-structure.md` line 76: "- **The stack evaluation.** The deciding inputs are **fluency and". The concept makes each technology choice answerable to the Invariant Slice Registry. The stack evaluation decides on fluency and audience only, and app-structure says the Invariant Slices "rarely tell structures apart", as with the stack. Which side: not clear. The stack side is practice, and a registry may constrain the store, not the language. Why: missed at `211bd0f` (the concept's line, before the Change Walk) and at `c449de0`, whose Foundation Check said they agree. Proposed: question: the stack evaluation adds "the stack must serve the Invariant Slice Registry; among stacks that do, fluency and audience decide", or the concept narrows "each choice" to the choices the Registry can tell apart.

**FINDING-1578.** Agreement; resting on the reader, quote checked (left I7). line 147; `spring-harness-reference.md` line 7: "Both CBC Runs that ran this Agent Skill" against "Three projects built them". The difference is never explained. Proposed: decided with LES-2 and LES-18, which weigh the same counts.

**FINDING-1579.** Wiring; uncertain: a footer line may only name a file (script W2). *Decisions* footer, lines 283–285: Names `references/…` from the Agent Skill's folder, not from the repo root. Proposed: question, with W3: a footer names a file by its root path, or by its name.

`delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`

**FINDING-1580.** Agreement; resting on the reader, quote checked (left I1). Stage 4, lines 123–127: Tells a CBC Run to write a new reference beside `postgres-role-split.md`, inside a pinned copy's folder, "so no later project derives it again". The delivered-copies Agent Rule allows a copy to change only by its rules, and only the Concept Deliverer can carry it to later CBC Runs. Proposed: fix: the reference is written in the CBC Run's own place and offered under *To the deliverer*.

**FINDING-1581.** Agreement; resting on the reader, quote checked (left I2). lines 170 and 206: "It is the home of the Runtime Ground's own words"; "The project's Infrastructure Contract is where it writes its own words". The container's records table puts a CBC Run's own Names in `docs/glossary.md`. Proposed: fix: the words are defined in the Contract and listed in the glossary.

`delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`

**FINDING-1582.** Stale lines; resting on the reader; missed at a change (SL4-5). `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, *4. Land the Catalog Check*, lines 99-105: "It queries the catalog against the Database Role Split's claims:". The list after this line names 4 checks: 1. roles; 2. database and schema owners; 3. schema privileges; 4. default privileges. The template it names, `templates/verify-database-model.sql`, runs 6 sections. Number 6, "Connect privilege — access by grant, never by default", checks `bootstrap.sql`'s REVOKE CONNECT, and the list leaves it out. `postgres-role-split.md`, lines 92-94, makes the connect revoke a claim of the Database Role Split. Why: missed at a change. The list was a run-on sentence of four items before `580f7dc` (2026-11-01), and the template already held section 6 at `657d6eb`. `580f7dc` made the list a numbered one without checking it against the template. Proposed: fix: add a fifth item, "5. who may connect to the database: the two roles by grant, PUBLIC not at all."

**FINDING-1583.** Agreement; resting on the reader, met in passing (met AGS-stack). lines 194–195: A read-only identity is "made at the CBC Bootstrap beside the two". cbc-bootstrap SKILL line 215 sends a missing service or constraint to Infrastructure Establishment, and its app "knows one identity". Proposed: fix: the identity is made at Infrastructure Establishment.

`delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`

**FINDING-1584.** Agreement; resting on the reader, quote checked (left I9). the drawing: Labels Stage 6 "contract", while its Stage 6 Gate asks that both manuals stand. Proposed: fix: the label names both.

**FINDING-1585.** Wiring; uncertain, as W2 (script W3). *Decisions* footer, lines 208–210: Names `references/…` from the Agent Skill's folder, not from the repo root. Proposed: question, with W2.

`delivery/spring-postgres/.claude/skills/infra-establish/templates/verify-database-model.sql`

**FINDING-1586.** Agreement; resting on the reader, met in passing (met AGS-stack). header, lines 10–11: The header says it checks "the claims of postgres-role-split.md". Role-split lines 62–63 claim `public` is stripped of PUBLIC privileges, "enforced, not assumed"; the template does not query it. Proposed: fix: the template gains the query.

`delivery/spring-postgres/docs/glossary/stack.md`

**FINDING-1587.** Agreement; checked; missed at a change (AGS-15). `delivery/spring-postgres/docs/glossary/stack.md`, entry *Stack Default*, line 85: " demand or a fact about the environment defeats it: local containers". The entry says a Stack Default yields only to a demand or an environment fact, and names app-structure as a home. App-structure lets a CBC Run depart for fluency, audience or a stated intent. Which side: the entry. Why: missed at `c66778e`, which read the entry against establishment-walk only. Proposed: fix: name both departures: local containers under podman, run by compose, departed from only when a demand or an environment fact defeats it; packages by feature, departed from by the CBC Run's own deciding inputs.

#### Round 2: where it lives

##### Layer 1: the conventions manual

`docs/conventions/conventions/README.md`

**FINDING-1588.** Dependencies; resting on the reader, met in passing (met LAO). §1.5, lines 157–158: "A sentence that points at where a fact is written gives the path, as a Fact Reference" retells facts-in-sync §3.1 with no Fact Reference. Proposed: fix: the Fact Reference.

**FINDING-1589.** Dependencies; checked; missed at a change (DEO-1). `docs/conventions/conventions/README.md`, §2 *The Convention Manual*, line 176: "Approaches are made usable (`ARCHITECTURE.md` §1, *What is stated here*). It explains and". "the manual is the convention stated, from which its Work Approaches are made usable" points at `ARCHITECTURE.md`, a record. That fact's home is the Idea-to-Output Model §6.1. `ARCHITECTURE.md` §1.2 itself points up to idea-to-output §6 for it. The reference points down, at a summary. Why: missed at a change. `c53eac8` (the reference rewrite, 2026-10-28) wrote it after ADR-0071. The per-commit question should have caught it (one-home rule 6). Proposed: fix: "(`docs/models/idea-to-output.md` §6.1, *The manual's level*)".

**FINDING-1590.** Dependencies; uncertain; older than the rule (DEO-19). `docs/conventions/conventions/README.md`, §3 *Adding a convention*, line 301: "own (`.claude/approaches-on-trial/approach-evaluation.md`). The". "when its evaluation places a piece as a convention of its own" points down at an Approach on Trial. The step it relies on, from an Approach on Trial to a convention, is stated in idea-to-output §4.2 and §4.3. This manual's §1.3 already cites idea-to-output §4.2 for the same placing. Why: older than the rule. `a9e8b961`, 2026-10-20, before ADR-0071. Proposed: question: naming or relying? If relying, use "(`docs/models/idea-to-output.md` §4.2, *The upward direction*)", with the Approach on Trial named in prose.

**FINDING-1591.** One home; checked; missed at a change (OHO-6). `docs/conventions/conventions/` §3 *Adding a convention*, step 6, lines 320–322; and step 3, lines 309–311: "A CBC Run's Decisions Log lists, in its birth entry, the". Step 6 retells that a CBC Run's Decisions Log lists its conventions in its birth entry, and that the Concept Deliverer receives none (ADR-0042). Step 3 retells that a CBC Run holds that list. The home is the agent-arrangement manual, `docs/conventions/agent-arrangement/` §3.4, *`.claude/decisions.md`*, which its own §2.1 already points at. Neither step carries a Fact Reference; ADR-0042 is the why, not the fact's home. Why: missed at a change. `0803717` (2026-11-01) rewrote step 6's sentences; `b00ba18` (2026-10-29) step 3's. Rule 6's question at the commit should have asked where the fact lives. Proposed: fix: step 6's last two sentences become "The Concept Deliverer's Decisions Log lists no conventions, since it receives none (`docs/conventions/agent-arrangement/` §3.4, *`.claude/decisions.md`*)." Step 3's "a CBC Run holds that list, and cannot open this repo's" gains the same Fact Reference.

##### Layer 2: project-recording

`docs/conventions/project-recording/README.md`

**FINDING-1592.** Layout; resting on the reader, met in passing (met OHO). §1, item 12: Retells its own seat's item 1, "Ours has none: lessons are written back at each Plan Step's close", inside one manual. Proposed: fix: item 12 points at the seat.

**FINDING-1593.** Dependencies; resting on the reader; missed at a change (DEO-6). `docs/conventions/project-recording/README.md`, §7.5 *When a README changes*, line 560: "item on every Plan Step Gate: 7 of the playbook's 9 Plan Steps make". The manual's reason rests on a count taken from the playbook, `delivery/fills/cbc-run-pure-playbook.md`, a text below it. The count is neither marked as an example nor pointed at. Why: missed at a change. `eb57bcf` (2026-11-01) rewrote it. The direction rule, ADR-0071, came earlier. Proposed: question: is it a general line ("most of a playbook's Plan Steps make nothing true that the README says"), or a marked example ("Here, for example, 7 of the playbook's 9 Plan Steps…", with the playbook's path named)?

##### Layer 3: the other manuals, the Idea Models, the concept

`concept/01-layered-system.md`

**FINDING-1594.** Dependencies; uncertain; older than the rule (DEO-18). `concept/01-layered-system.md`, *Two readings to keep apart*, line 96. The same pattern is in `concept/03-cbc-framing.md` line 22 and `concept/04-cbc-slice.md` line 35: "belongs to CBC Framing and is described there.". The chapters lean on each other by name. Chapter 01 sends the reader to "CBC Framing" for the derivation order. Chapter 03 retells the Layered System's outside-in order. Chapter 04 uses "the ranking of Structural Walls" from chapter 02. None gives a path. A section with no number can be addressed by its title. Why: older than the rule. `66d28b2`, 2026-08-28. Proposed: question: do the chapters, copied whole as one concept, need Fact References between themselves? If yes, the three lines take (`concept/03-cbc-framing.md`, *The derivation order*), (`concept/01-layered-system.md`, *Two readings to keep apart*) and (`concept/02-guarantees-and-walls.md`, *The ownership map*). Each is a concept change, editorial, and fires that TODO item's trigger.

`docs/conventions/agent-arrangement/README.md`

**FINDING-1595.** Layout; resting on the reader, met in passing (met LAO). §3, and §3.7 line 356: §3 is titled `.claude/`, yet §3.7 opens "Not under `.claude/`, but the arrangement's neighbour", and `CLAUDE.local.md` is not in §1.1's closed list of paths. §3's subject is wider than its title. Proposed: question: §3 is retitled, or §3.7 moves.

**FINDING-1596.** Layout; resting on the reader, met in passing (met OHO). *The seats*; §3.4: Both tell the birth entry's list and ADR-0042, inside one manual. OHO-6 meets the same fact in the conventions manual. Proposed: fix: one of the two points at the other.

`docs/conventions/commit-plan/README.md`

**FINDING-1597.** Lessons; resting on the reader, quote checked (left B5). §2.7, lines 111–114: The italic line still tells the case instead of pointing at its story. The leftovers step marked §2.9 and §2.12 gone; LEO found both still stand, as LEO-1 and LEO-2, listed beside this. Proposed: fix: as LEO-1 proposes for §2.9, a line naming the story.

**FINDING-1598.** Dependencies; resting on the reader; missed at a change (DEO-5). `docs/conventions/commit-plan/README.md`, §2.8 *Counting subjects*, line 118: "A subject's characters are counted against the 50 limit when it is". "the 50 limit" relies on the commit-messages manual's subject limit (§2.1) and does not say where. Why: missed at a change. `103a301` (2026-11-01) rewrote the line. The per-commit question should have caught it. Proposed: fix: "against the subject's 50-character limit (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*)".

**FINDING-1599.** Lessons; checked; missed at a change (LEO-1). `docs/conventions/commit-plan/README.md`, §2.9 *The agent's files*, lines 128–129: "split when it opens. *CBC Run 3's Step 10 plan put two changes under". The section ends with an italic sentence that tells CBC Run 3's case, not a line that points at its story. §2.8 next to it shows the form: "*Its story: devlog 2026-10-08; …*". Why: missed at a change. The case dates from `489ecf2` (2026-10-08). Round 2 accepted it as an italic, which was the rule's form then. When ADR-0073 turned notes into pointers, `ae53ed7` ("the other lessons point at stories") moved only the *dated* notes. This italic has no date, so it stayed. That commit plan counted dated notes, not cases. Round 3's *Met in round 3* listed it, and so did the close read (reader B). Proposed: fix: lines 128–129 become "split when it opens." and then, on its own line, "*Its story: devlog 2026-10-08.*". That entry tells the take ("agent files their own step") but maybe not the case. If it does not, the italic's words are first copied into a devlog entry, as ADR-0073 decision 2 did for the others, and the line names that entry too.

**FINDING-1600.** Lessons; checked; missed at a change (LEO-2). `docs/conventions/commit-plan/README.md`, §2.12 *The look back*, lines 160–161: "CBC Run 3's polish regrouped 36 small commits into 7, after the fact". The section's last line is the case itself, CBC Run 3's count, not a line that points at its story. ADR-0050 tells the case: "regrouped by kind, 36 into 7" (its line 18). Why: missed at a change, as LEO-1: the case dates from `1e50055` (2026-10-15), and `ae53ed7` moved only dated notes. Round 3's met list and the close read's met list both named it. Proposed: fix: "*Its story: ADR-0050.*" replaces lines 160–161.

`docs/conventions/facts-in-sync/README.md`

**FINDING-1601.** Layout; resting on the reader; older than the rule (LAO-2). `docs/conventions/facts-in-sync/README.md`, §1 *One home*, lines 83-108: "- **History is not a second home.** The devlog, closed ADRs, commit". §1 has seven bold-led bullets. Four of them hold paragraphs of 4 to 6 lines, each with its own reason: - "A fact changes at its home"; - "A copy is a follower", which names two cases; - "History is not a second home": "They are never updated, so they cannot drift"; - "History is not a first home either", with its reason and ADR-0070. So they are parts, and they are not numbered. Why: older than the rule. The bold-lead line came in `aa40496`, 2026-10-28. Proposed: fix. Number the seven as `### 1.1` to `### 1.7`, each titled by its bold lead under writing rule 10. "Living Text" becomes *Living Text*. The bullets' text stays word for word. Every pointer to §1 still lands.

**FINDING-1602.** Lessons; uncertain; the rule unclear (LEO-8). `docs/conventions/facts-in-sync/README.md`, §5 *A disagreement*, lines 335–337: "It has happened: CBC Run 3 showed a clause of `convention-lifecycle`,". The general rule is complete above it: "a Canonical Description is downstream of practice". The paragraph that follows is a case offered as evidence. The story line at 343 already names ADR-0034. Why: the rule is unclear where a plain example ends and a case begins. Proposed: question: is "It has happened: …" the short plain example §2.6 allows? If so, it stays. If it is the case, it goes, and the story line at 343 already points at ADR-0034.

**FINDING-1603.** Dependencies; checked; missed at a change (DEO-3). `docs/conventions/facts-in-sync/README.md`, §5 *A disagreement*, line 339: "The concept's meaning has changed once since v1 (`CHANGELOG.md`).". The manual points down at the CHANGELOG, a record, for the claim that the concept changed. The decision that changed it is ADR-0048, which `ARCHITECTURE.md` §1.1 already cites. This line is not DECISION-14's case: that decision covers the bump rule in the CHANGELOG's header comment, not an entry. Why: missed at a change. `5747b32` rewrote the line on 2026-11-01 and kept the pointer. The per-commit question should have caught it. Proposed: fix: "The concept's meaning has changed once since v1 (ADR-0048)."

`docs/conventions/retrospective/README.md`

**FINDING-1604.** Lessons; resting on the reader; older than the rule (LEO-4). `docs/conventions/retrospective/README.md`, *The CBC Run's seat*, lines 78–81: "would drift. CBC Run 3's apply guide restated nearly every rule of its". The general reason is stated: "it would repeat them, and the two would drift". Then the case that taught it stays in the body as a sentence of its own. ADR-0054 tells it: "in run 3 the apply guide restates nearly every rule" (its lines 45–47). The lesson reads clearly without it, so §2.6's allowance for an example does not apply. Why: older than the rule. The text is from `fa7fd41` (2026-10-15), and §2.6 came on 2026-10-18. Then missed at round 2's Lessons read and at `ae53ed7`. Round 3's FINDING-450 read it for rule 4 only. Proposed: fix: cut "CBC Run 3's apply guide restated nearly every rule of its Agent Skill." Then end the paragraph with "*Its story: ADR-0054.*".

**FINDING-1605.** Layout; uncertain; the rule unclear (LAO-6). `docs/conventions/retrospective/README.md`, §2 *How the look back decides* (lines 108-128) and §3 *How the lessons are applied* (lines 134-153): "- **The order of the commits follows influence.** Removing repeats". Each section is a list of bold-led rules. Most items are a rule and one sentence of reason, 2 lines. A few run to 4 sentences, such as this one and "New proof is not this Plan Step's". No item carries a story. The items sit at the line's edge: longer than "a phrase and a line", shorter than LAO-2's paragraphs. Why: the rule is unclear at its edge. "A paragraph of its own" and "a phrase and a line" leave the 2-to-4-sentence item undecided. Proposed: question. (a) Not parts: a rule list keeps bullets, and §3.2 says so ("a rule and its one reason is a list item"). (b) Parts: number both, as `79bc4a2` numbered commit-plan §2, whose §2.2 is two lines. Recommended: (a). The line then gains the words that decide the next case.

`docs/conventions/shapes/README.md`

**FINDING-1606.** Layout; resting on the reader; older than the rule (LAO-4). `docs/conventions/shapes/README.md`, §2 *What an Output Shape is not*, lines 122-140: "- **Not trial evidence.** This is the one that will be got wrong,". Four bold-led bullets of 3 to 7 lines. Each gives its own reason why an Output Shape is not that thing. They are parts left unnumbered. Why: older than the rule (`aa40496`). Proposed: fix. `### 2.1 Not a template` to `### 2.4 Not trial evidence`, the text word for word. The pointers to §2 (*What it is for*, §1's *Its story*, *What this does not cover*) still land.

**FINDING-1607.** Dependencies; checked; older than the rule (DEO-4). `docs/conventions/shapes/README.md`, §4 *An Output Shape between repos*, line 167: "thing it shapes: the same rule by which an Agent Skill belongs to". "the same rule by which an Agent Skill belongs to exactly one group and is delivered whole" retells exchange §3.4 ("An Agent Skill belongs to one group and travels whole"). It carries no Fact Reference. Why: older than the rule. `3590e39`, 2026-09-27, before facts-in-sync existed. Proposed: fix: add "(`docs/conventions/exchange/` §3.4, *One group per file*)" after "delivered whole".

**FINDING-1608.** Lessons; checked; missed at a change (LEO-3). `docs/conventions/shapes/README.md`, §4.1 *Nothing fetched*, lines 192–196: "staged for a Plan Step Gate on its own. *A fetch of Output Shapes at". A five-line italic tells the case: ADR-0037 named a fetch that was never built, and CBC Run 3 looked in `temp/` at two closes. The lesson, "Nothing is staged for a Plan Step Gate on its own", already stands in the body. ADR-0052 tells the case (its line 28: "looked in at two closes"). Why: missed at a change. The case is from `ec64d6a` and `61fcc5d` (2026-09-27 and 2026-10-15). `ae53ed7` moved shapes' dated notes and left this undated one. Round 3's *Met in round 3* listed it. It is not in *Met at the close read* or in the leftovers, so nothing carried it on. Proposed: fix: lines 192–196 become "staged for a Plan Step Gate on its own." and then, on its own line, "*Its story: ADR-0052.*".

**FINDING-1609.** Layout; resting on the reader, quote checked (left C7). line 305: "Any change is shown before it is made." has no blank line before it, so Markdown renders it inside the fourth bullet. Proposed: fix: a blank line before it.

`docs/conventions/visual-comparison/README.md`

**FINDING-1610.** Lessons; resting on the reader; older than the rule (LEO-5). `docs/conventions/visual-comparison/README.md`, §1 *What a comparison is*, line 58: "set. ADR-0028's best answer to one requirement was one of those.". The lesson is stated in general: a name that named a picture would keep the table and the list out of the set. Then the case follows as evidence, in the body. *What it is for* already tells the same case (lines 20–22), and *Where to look* names ADR-0028. Why: older than the rule: `1e5d42e` (2026-09-19). Round 2's FINDING-265 moved this case out of the Agent Skill and "the manual holds them". That read as cover for the body sentence. Then reworded in `7a54776` (round 3) for writing alone. Proposed: fix: cut the sentence. §1 gains "*Its story: ADR-0028.*".

`docs/conventions/writing/README.md`

**FINDING-1611.** Layout; resting on the reader; older than the rule (LAO-3). `docs/conventions/writing/README.md`, §1 *What it governs*, lines 67-77: "- **Plain is the default for every kind of text.** A kind of text". Three bold-led bullets, each a paragraph with its own reason. The third carries a story: "CBC Run 3 put off a specification style … (its `RETRO.md`, D14)". They are parts left unnumbered. Why: older than the rule (`aa40496`). Proposed: fix. `### 1.1 History keeps its words`, `### 1.2 Dense Agent Skills and Agent Rules`, `### 1.3 Plain as the default`, or titles the reviewer prefers. `.claude/rules/writing.md` cites §1 whole, so its references still land.

**FINDING-1612.** Lessons; resting on the reader; older than the rule (LEO-6). `docs/conventions/writing/README.md`, §1 *What it governs*, lines 75–77: "named yet: CBC Run 3 put off a specification style until its claims". The lesson is general: "A kind of text gets another style only when plain has been shown to fall short there." The text then gives CBC Run 3's RETRO D14 as the case, in the body. No ADR or devlog entry here tells it. ADR-0053 does not mention it, and the devlog has no "specification style". Why: older than the rule: `83acdfe` (2026-10-15). It was reworded in `efb8cef` (round 3's close read) for writing alone. Lessons was not read then. Proposed: fix: "None is named yet." stays. The CBC Run 3 clause is copied into a devlog entry, and the bullet ends with "*Its story: devlog <that entry>.*".

**FINDING-1613.** Dependencies; checked; missed at a change (DEO-2). `docs/conventions/writing/README.md`, §2 *Why each rule*, rule 5, line 94: "Skill's phase is an Agent Skill Stage (`docs/glossary.md`).". A manual points at the glossary, a record, for what an Agent Skill's phase is called. The glossary entry is only a pointer. It sends the reader on to the home, `docs/conventions/conventions/` §1.4. Why: missed at a change. `86bbea6` (2026-10-29, Names and labels) added the sentence after ADR-0070 and ADR-0071. The per-commit question should have caught it. Proposed: fix: "(`docs/conventions/conventions/` §1.4, *Agent Skill Stages*)".

**FINDING-1614.** Lessons; resting on the reader, quote checked (left C4). line 175: The *Its story* line cites devlog 2026-10-29 and does not cite ADR-0078, which changed rule 9. *Where to look* names ADR-0053 only. Proposed: fix: the line and *Where to look* name ADR-0078 and ADR-0079.

**FINDING-1615.** Lessons; resting on the reader; older than the rule (LEO-7). `docs/conventions/writing/README.md`, *Why it arrives this way*, lines 186–187, and lines 190–191: "draft loaded on Markdown files, and was dropped for this.". Each rejected channel has its general reason. "A Paths Rule loads when a file is touched, after a new one's first draft is written. Chat has no path." Then comes the case: "CBC Run 3's first draft loaded on Markdown files, and was dropped for this." Lines 190–191 do the same: "held the lesson in CBC Run 3 and did not act." ADR-0053's *Options considered* tells both: "Load them on Markdown paths only" and "Keep the voice in memory or in `CLAUDE.local.md`". Why: older than the rule: `83acdfe` (2026-10-15). Round 2's Lessons read, `ae53ed7` and round 3 reworded it (`86bbea6`, `efb8cef`). None of them moved the case. Proposed: fix: cut "CBC Run 3's first draft loaded on Markdown files, and was dropped for this." Line 190 becomes "**Memory or `CLAUDE.local.md`** holds a lesson the agent does not act on." The list ends with "*Its story: ADR-0053.*".

`docs/models/agent.md`

**FINDING-1616.** Layout; resting on the reader; older than the rule (LAO-5). `docs/models/agent.md`, §5 *The context window*, lines 170-193: "- **Ranked by role above that.** The harness marks three things". Four bold-led bullets. "Undifferentiated within a role" holds a paragraph of its own, its "Consequence". "Ranked by role above that" holds 11 lines with its reason and claim W2. "Finite" and "Ordered, not prioritised" are one line each. Two of the four are parts, so the section is divided into labelled parts. Why: older than the rule (`aa40496`). Proposed: fix. `### 5.1` to `### 5.4`, each titled by its bold lead. The three pointers to §5 (§8's table and closing line, §12.5 W1) still land.

`docs/models/idea-to-output.md`

**FINDING-1617.** One home; uncertain; the rule unclear (OHO-7). `docs/models/idea-to-output.md`, §5 *An Idea Model and a concept*, lines 138–139; and §6.3 *A convention and the concept*, line 179: "only its outputs vary. A CBC Run edits its copy only after a". The Idea Model says a CBC Run edits its concept copy only after a mistake it met, and the Concept Deliverer reads the edit. The Exchange Convention says the same, `docs/conventions/exchange/` §5.6, *Editing a chapter*: "only from a mistake lived in the CBC Run". `ARCHITECTURE.md` §1.1 points at exchange §5.6 as the home. Neither of the two tellings points at the other. The Idea Model cannot point down (`docs/models/idea-to-output.md` §3.2, *The direction of a link*), and the exchange stands on the Tiers Model, not on this one. Why: the rule is unclear on an Idea Model naming this repo's actors. `9fce63c` (2026-11-01) reworded lines 138–139. Proposed: question: (a) the Idea Model's line is general: "A project edits its copy of a concept only from a mistake it met, and the concept's repo reads the edit"; exchange §5.6 points up to it. (b) It is this repo's: the line goes, and §6.3's cell points at §5's general sentence only.

`docs/models/tiers.md`

**FINDING-1618.** Layout; checked; missed at a change (LAO-1). `docs/models/tiers.md`, §3.5 *What holds on every flow*, line 149; and §3.4 *The Delivery Pin and documents*, line 123: "And one number, the Delivery Pin: the commit of the tier above that a". §3.4 is titled with the Delivery Pin and defines it at line 123: "The Delivery Pin, the commit of the tier above that a delivery's copies equal". §3.5 defines it again at line 149 in the same words, with no pointer to §3.4. §3.4 in turn points at §3.5. The five facts do the same. Fact 1 (line 136) retells §3.4's "no tier's agent reads a tier above it". Fact 5 (lines 146-147) retells §3.3's "the Run Repo sends nothing". So the reader meets each of them twice in one file. Why: missed at a change. `b06dc95` (2026-10-28, model-placing) made §3.5 after Refinement Round 2's close read at `d37a08f`. `9fce63c` (2026-11-01) added the definition at line 123. No check at a commit reads an Idea Model's layout: `convention-manual.md` loads only for manuals. Round 3's reader met the facts (*Met in round 3, of other kinds*, the item on `docs/models/tiers.md` §3.5). The leftovers step did not carry that list, so it is listed here. Proposed: question. (a) §3.5 keeps the Delivery Pin's definition, and §3.4 line 123 points at it: "The Delivery Pin (§3.5, *What holds on every flow*) follows the documents the tiers exchange." (b) The closing paragraph of §3.5 moves into §3.4, and exchange §2.2 line 117 takes the new reference. For the five facts, decide with model-placing's open question.

##### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

`ARCHITECTURE.md`

**FINDING-1619.** Layout; unverified, no quote to search (left E14). line 78: The list item's second line starts at column 0. It renders by lazy continuation, but in the source it reads as outside the list. Proposed: fix: indent it.

**FINDING-1620.** One home; checked; missed at a change (OHO-5). `ARCHITECTURE.md`, §2.2 *The Stack Group*, lines 150–152: " another stack takes no `spring-postgres/`; another stack's Agent ". "A CBC Run on another stack takes no `spring-postgres/`" is the home's fact, `docs/conventions/exchange/` §3.4, *One group per file*: "a CBC Run on another stack takes the Container Group and the Method Group and leaves the Stack Group (ADR-0029)". §2.2 retells it with only ADR-0029. Others now take the second telling as the home: `delivery/README.md` §5, lines 84–85, points at `ARCHITECTURE.md` §2.2 for it. `ARCHITECTURE.md`'s own §3 row 9 points at exchange §3.4. Why: missed at a change, reopening Refinement Round 2's FINDING-256, which moved §3's row off ADR-0029 to exchange §3.4 and left §2.2's line. `5d0f5ca` (2026-11-01) reworded the line; rule 6's question at the commit did not catch it. Proposed: fix: "A CBC Run on another stack takes no `spring-postgres/` (`docs/conventions/exchange/` §3.4, *One group per file*); another stack's Agent Skills would be a group beside this one." `delivery/README.md` line 85's Fact Reference then names exchange §3.4 (the ships reader's file; noted here so the pair is fixed together).

**FINDING-1621.** Dependencies, One home; checked; missed at a change (DEO-8; also OHO-1). `ARCHITECTURE.md`, §3 *What must stay true*, line 212: "| The concept is canonical here; the archive it came from is a frozen snapshot, never a source | §1.1, *The concept*; `CHANGELOG.md`'s `[v1]` entry | commit review |". The rule's "Stated in" names a released entry, which is history. The archive half of the rule is stated nowhere else: §1.1 says nothing of the archive. Why: as DEO-7. OHO-1 (One home): the row says where its rule is stated: §1.1 and the `[v1]` entry. §1.1 states only the first half, "canonical here". The second half, "the archive … is a frozen snapshot, never a source", is stated only in `CHANGELOG.md` lines 93 to 95, the released `[v1]` entry. So the row's first home for that half is history. Its proposal: question: where the archive fact's living home is. Recommended: `ARCHITECTURE.md` §1.1 gains one bullet, "**Imported once.** The chapters came from the archive, `system-design-method`, at `fe0075d`; its copy is a frozen snapshot, never a source.", and the row cites §1.1 alone. Or: `README.md`'s success criterion is read as the home, and the row cites it. Proposed: fix with DEO-7: once §1.1 states the archive fact, the cell reads "§1.1, *The concept*".

`README.md`

**FINDING-1622.** Dependencies, One home; checked; missed at a change (DEO-7; also OHO-2). `README.md`, *Out of scope*, line 56: "concept chapters taken from it (`CHANGELOG.md`, *[v1]*).". The README rests on the released `[v1]` entry for where the chapters came from (`system-design-method`). No Living Text states it: `ARCHITECTURE.md` §1.1 does not mention the archive. Why: missed at a change. ADR-0079 made released entries history, in `f028aa8` and `71ad729`. The Change Walk on facts-in-sync §1 did not look for Living Text that rests on a released entry. OHO-2 (One home): which chapters were taken from the archive is pointed at `[v1]`, a released entry. No Living Text states it. Its proposal: fix with OHO-1: the Fact Reference becomes (`ARCHITECTURE.md` §1.1, *The concept*), once §1.1 holds the import. Proposed: question: give the archive fact a Living home, such as `ARCHITECTURE.md` §1.1 *The concept* ("imported from `system-design-method` at `fe0075d`; the archive is a frozen snapshot, never a source"), then point the README there. Fixed with DEO-8.

`TODO.md`

**FINDING-1623.** One home; uncertain; the rule unclear (OHO-8). `TODO.md`, header comment, lines 23–25: "read before the Ideas are weighed. When an item changes, rewrite". TODO's form says a Conversation Memory section named in See is read before the Ideas are weighed. When a section is read is the Conversation Memory's form, its header comment, as `docs/conventions/project-recording/` §14, *Conversation Memory*, names it ("when one is read … is the file's header comment"). `TODO-CONVERSATION-MEMORY.md` lines 16–17 state it. TODO's line names the file in prose, which is not a Fact Reference (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*). Why: the rule is unclear on a fact two records' forms both act on. Proposed: question: TODO's line keeps its words and gains (`TODO-CONVERSATION-MEMORY.md`, its header comment); or it stays, as TODO's own fact, and the Conversation Memory's header points at TODO's.

**FINDING-1624.** One home; checked; missed at a change (OHO-4). `TODO.md`, *Next*, "Unlock the folders locked for CBC Run 6", lines 47–48: " `Read` deny rule does not stop a shell. ". The Context retells what a `Read` deny rule reaches, with no Fact Reference. The home, `docs/conventions/agent-arrangement/` §5.4, *Permission rules*, says a `Read` deny does cover shell file commands such as `cat`, `head` and `sed`, and does not cover `grep -r` or a script. The second home has drifted: "does not stop a shell" is wider than the home. `.claude/approaches-on-trial/auto-run.md` lines 70–72 retell the same fact correctly, with its Fact Reference. Why: missed at a change. `337788a` (2026-10-29) wrote the line, after §5.4 was checked on 2026-10-24. Rule 6 of `.claude/rules/one-home.md`, the question at the commit (ADR-0070), should have asked where the fact lives. Proposed: fix, lines 47–48: "Context: CBC Run 6 must not read another repository, and a `Read` deny rule stops `cat` and `sed` but not `grep -r` or a script (`docs/conventions/agent-arrangement/` §5.4, *Permission rules*). So, before its birth,".

**FINDING-1625.** Dependencies; resting on the reader; missed at a change (DEO-21). `TODO.md`, *Next*, item "Decide how commits cited by hash can still be regrouped", line 371: "its close (`.claude/skills/commit-plan/SKILL.md` §4, *The lifecycle*), and a regroup gives them new hashes. This repo cites". The look back that regroups a Change Set's commits is stated in commit-plan §2.12. The reference names the Agent Skill that applies it. Why: missed at a change. `9435842` (2026-10-30). Proposed: fix: "(`docs/conventions/commit-plan/` §2.12, *The look back*)".

**FINDING-1626.** Dependencies; resting on the reader; missed at a change (DEO-20). `TODO.md`, *Next*, item "Read a CBC Run born before the refinement by its needs, not its diff", line 559: "(`.claude/skills/exchange-read/SKILL.md`, Stage 3, *Read three things*). The". "a CBC Run Reading takes three things" is stated in exchange §6.1. The Agent Skill derives from it and points there itself. Why: missed at a change. `683febc` (2026-11-01) rewrote the line. Proposed: fix: "(`docs/conventions/exchange/` §6.1, *Reading a CBC Run*)".

##### Layer 5: our agent setup

`.claude/approaches-on-trial/refinement.md`

**FINDING-1627.** Layout; uncertain; the rule unclear (LAO-7). `.claude/approaches-on-trial/refinement.md`, §3 *Not known yet*, lines 340-367: "- **Whether a refinement is the second check on text kept true.** The". Ten bold-led bullets. Two carry a dated story of their own, "On 2026-10-19 the reviewer…" and "The reviewer's view, 2026-10-31…". The page uses the manual's numbered form, and §1 and §2 number their parts. Why: the rule is unclear: its reach over an Approach on Trial is not stated. Proposed: question. Does Layout reach an Approach on Trial written in the manual's form? If yes, number §3's ten items as `### 3.1` to `### 3.10`. If no, DECISION-15's naming of it is closed as out of reach. The refinement's close already asks whether an Approach on Trial follows the manual's form (*Met in round 3*, the item on `refinement.md` lines 182-299).

`.claude/decisions.md`

**FINDING-1628.** Dependencies; checked; older than the rule (DEO-13). `.claude/decisions.md`, header comment, line 10: "Division of labor: a standing rule is written as a comment in". Lines 10 to 17 retell agent-arrangement §3.4 almost word for word: the rule sits in the file it governs, the log keeps the why, and "Neither repeats the other". The line's Foundation Line names agent-arrangement, but no Fact Reference is given. Every other record header carries "Why the form is as it is: (…)". This one does not. Why: older than the rule. `3cad065`, 2026-08-27. Proposed: fix: before the Foundation Line, add "Why the form is as it is: (docs/conventions/agent-arrangement/ §3.4, .claude/decisions.md)". In a comment, the title takes no asterisks.

`.claude/rules/convention-manual.md`

**FINDING-1629.** Dependencies; checked; missed at a change (DEO-12). `.claude/rules/convention-manual.md`, *The sections, in this order*, line 26 (items 1 to 4, 8 and 9): "1. **The opening statement.** One bold sentence: the manual's". Items 5, 6 and 7 point at conventions §2.5, §2.6 and §2.7. Items 1 to 4, 8 and 9 restate §2.1, §2.2, §2.3, §2.4, §2.8 and §2.9 with none. The header comment's "(§2, The Convention Manual)" gives the why of the whole file. It is not a section's reference. Why: missed at a change. ADR-0072's rewrite (`ed96ed0`) did not include this file. Proposed: fix: each item gains its part: (§2.1, *The opening statement*), (§2.2, *The need*), (§2.3, *The list of what derives*), (§2.4, *The seats*), (§2.8, *The boundary*), (§2.9, *Where to look*), each with the path `docs/conventions/conventions/`.

`.claude/rules/foundation-check.md`

**FINDING-1630.** Dependencies; resting on the reader; missed at a change (DEO-16). `.claude/rules/foundation-check.md`, *The check*, step 1, line 28 (and line 23): "Canonical Descriptions: `docs/models/`, `docs/conventions/*/README.md`,". The third bullet relies on which texts are Canonical Descriptions, from facts-in-sync §4, the file's own foundation. It carries no reference. The first bullet relies on conventions §1.3 too. Only the second bullet carries that reference, at its end. Why: missed at a change. `ecda44f` (2026-10-30) wrote the bullet after ADR-0070. Proposed: fix: move "(`docs/conventions/conventions/` §1.3, *The Foundation Line*)" to step 1's lead line, covering bullets 1 and 2. Bullet 3 gains "(`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*)".

`.claude/rules/one-home.md`

**FINDING-1631.** Dependencies; resting on the reader; missed at a change (DEO-17). `.claude/rules/one-home.md`, *The rules*, rule 5, line 41: "the worked example sits in the cbc-framing and cbc-slice Agent Skills, and". Where the worked example's two copies sit, and that one follows the other, is stated in exchange §6.3. The rule says it with no reference. Why: missed at a change. `fab7214` (2026-11-01) rewrote the line. The sentence itself dates from `0148ce1` (2026-10-20), before the Fact Reference had a form. Proposed: fix: "…and the two must stay identical (`docs/conventions/exchange/` §6.3, *The CBC Run Reading*)."

`.claude/rules/working-a-reading.md`

**FINDING-1632.** Dependencies; resting on the reader; missed at a change (DEO-14). `.claude/rules/working-a-reading.md`, *The steps*, step 7, line 70: "lands where the Exchange Convention says.". Where each ending lands is exchange §6.5. The step names the convention in prose only. Why: missed at a change, at the reference rewrite of 2026-10-28. It looked for written references, and this line has none to rewrite. Proposed: fix: "It lands where the Exchange Convention says (`docs/conventions/exchange/` §6.5, *Verdicts*)."

`.claude/skills/commit-messages/SKILL.md`

**FINDING-1633.** Dependencies; checked; missed at a change (DEO-9). `.claude/skills/commit-messages/SKILL.md`, the whole file. Quoted at *The agent's own files*, line 104: "CLAUDE.md` and `.claude/` are the working arrangement.". The Agent Skill stands on the commit-messages manual and carries no Fact Reference to any of its parts. A grep finds 0 references. *Format* uses §2.1 and §2.2. *The agent's own files* uses §2.3. *Rules* uses §2.4. This line also relies on agent-arrangement §1.1. Why: missed at a change. ADR-0072's rewrite (`ed96ed0`) gave references to four files only: `writing.md`, `exchange-reading.md`, `exchange-deliver` and `exchange-read`. The other derived files were not walked. Proposed: question: our copy is held identical to the container's (ADR-0069; DECISION-6). Should references land in both, in the form DECISION-40 gives shipped text ("the Concept Deliverer's `docs/conventions/…`")? In ours alone, breaking the identity? Or should §4 step 2 exempt a copy held identical to a shipped Master Copy?

**FINDING-1634.** Layout; checked; older than the rule (LAO-10). `.claude/skills/commit-messages/SKILL.md`, *Rules*, line 117; and *Format*, lines 19-20: "- **The subject alone makes sense** in `git log --oneline`.". *Format* already says the subject "makes sense alone in `git log --oneline`" (line 20). *Rules* states the same rule again as its own bullet. One rule sits in two sections. Why: older than the rule. *Format* gained the clause in `8fa62c6` (2026-10-09), beside the *Rules* bullet from `df9d5ed` (2026-09-17). Refinement Round 2's read passed it. Proposed: fix. Delete line 117. *Format* holds the rule. Make the same change in the container's copy in the same plan, so the two stay identical.

`.claude/skills/commit-plan/SKILL.md`

**FINDING-1635.** Dependencies; checked; missed at a change (DEO-10). `.claude/skills/commit-plan/SKILL.md`, the whole file. Quoted at §4 *The lifecycle*, line 116: "Before the close, sweep for every name the Change Set moved.** When a". The file holds no Fact Reference to its manual. The sweep bullet retells commit-plan §2.10 and facts-in-sync §3.3 with no reference. §3 and §6 carry references only to commit-messages. Why: as DEO-9. ADR-0070's consequences named "both `commit-plan` skills", but ADR-0072's rewrite left this one out. Proposed: question: as DEO-9. Ours differs from the container's by 3 hunks already, so references in ours alone are possible.

**FINDING-1636.** Layout; uncertain; older than the rule (LAO-8). `.claude/skills/commit-plan/SKILL.md`, §6 *Review protocol*, line 151; also §3 *How the commits are split* (lines 74-96) and §4 *The lifecycle* (lines 112-130). `.claude/skills/visual-comparison/SKILL.md`, §4 *What the render has caught* (lines 99-135): "**Small commits inside a planned commit, where the reviewer has". - **commit-plan §6:** a bold label on its own paragraph, the only labelled part of the section. DECISION-15 named it. - **commit-plan §3 and §4:** bold-led bullets of 7 to 10 lines, each with its own reason: "Order follows where the decision lives", "Plan the records commits", and the sweep. - **visual-comparison §4:** five bold-led bullets, each with the case it came from, which is a story. By the line's letter, all are parts left unnumbered in numbered sections. Why: the rule is unclear: whether §3.2's line reaches an Agent Skill's rule bullets is not stated. Both files are older than the line. Proposed: question. (a) The line reaches Agent Skills: number commit-plan §3, §4 and §6 and visual-comparison §4. Copy each change to the container's copy, as ADR-0069 allows. (b) Agent Skills are outside it: §3.2 says that a rule in an Agent Skill stays a bullet. Commit-plan §6's bold label then becomes plain prose, or a paragraph after the first. Recommended: (b). A rule bullet is acted on, not pointed at.

`.claude/skills/exchange-deliver/SKILL.md`

**FINDING-1637.** Layout; unverified, no quote to search (left F13). Stage 1, step 6: Step 6 has no bold lead, while steps 0 to 5 and 7 to 9 do. Proposed: fix: a bold lead.

`.claude/skills/exchange-read/SKILL.md`

**FINDING-1638.** Dependencies; resting on the reader; missed at a change (DEO-15). `.claude/skills/exchange-read/SKILL.md`, *What this does not do*, line 99. Also Stage 1, lines 17 to 21: "the work that follows, where the Exchange Convention says each lands.". Line 99 names the convention in prose for exchange §6.5. Stage 1 retells exchange §2.2: the two numbers, what each is, and that the last delivery entry carries them. It has no reference. The file's one line on §6.1 covers Stage 3, not Stage 1. Why: missed at a change. ADR-0072's rewrite (`ed96ed0`) gave this file references for some sections only. Proposed: fix: line 99 gains (`docs/conventions/exchange/` §6.5, *Verdicts*). Stage 1 opens "Why both numbers are in the CBC Run: (`docs/conventions/exchange/` §2.2, *The CBC Run*)."

`.claude/skills/visual-comparison/SKILL.md`

**FINDING-1639.** Layout; resting on the reader; older than the rule (LAO-9). `.claude/skills/visual-comparison/SKILL.md`, §1 *When this fires*, lines 26-47; and §2 *The comparison's steps*, steps 2 and 3, lines 56-64: "**The candidate set must contain at least one thing that is not a". §1 holds three subjects: - when the Agent Skill fires, and when it does not (lines 28-30 and 43-47); - the rule that the candidate set holds a non-picture (lines 32-35); - which notations are buildable (lines 37-41). The second subject is told again in §2. Step 2 says "whenever the candidate set includes a non-picture, and the set usually should". Step 3 says "List the candidates, including the plain ones". So one subject is spread over two sections, and the step that acts on it is not its home. The manual gives each its own part: `docs/conventions/visual-comparison/` §2.1, *A non-picture in the set*, and §2.4, *The buildable notations*. Why: older than the rule. Lines 32-41 date from September 2026. Layout reached Agent Skills from DECISION-8, 2026-10-25. Refinement Round 2's read passed it. Proposed: fix. Move lines 32-35 into step 3, which then holds the non-picture rule once. Move lines 37-41 into step 4, as what "for real" can build. §1 keeps when it fires. The container's copy follows (one hunk differs today, the seat's).

**FINDING-1640.** Dependencies; checked; missed at a change (DEO-11). `.claude/skills/visual-comparison/SKILL.md`, the whole file. Quoted at §1 *When this fires*, line 32: "The candidate set must contain at least one thing that is not a". §1 restates visual-comparison §2.1 (a non-picture in the set) and §2.4 (the buildable notations). No section carries a Fact Reference to its manual. Why: as DEO-9. Proposed: question: as DEO-9.

##### Layer 6: `delivery/`, what ships

`delivery/container/.claude/rules/shapes-lifecycle.md`

**FINDING-1641.** Dependencies; checked; missed at a change (DES-4). `delivery/container/.claude/rules/shapes-lifecycle.md` §3 line 69, §4 line 87, §5 line 98; `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 4 item 3, lines 131–133: "for that part, it is changed too, under the delivered-copies Agent Rule.". Each relies on delivered-copies rule 2 (how a delivered copy is edited) or rule 4 (how an edit reaches the Concept Deliverer), and names the Agent Rule in words. Every other shipped line that names this Agent Rule carries its path and rule, such as apply-retrospective 63–64. Why: missed at a change. In shapes-lifecycle the three lines named `delivered-copies.md`, a whole-document reference, until `8b6eec0` swapped the path for the Name. apply-retrospective 132 was missed at `15f6e88` (FINDING-220), which fixed line 63 of the same file. ADR-0070 decision 8's question at the commit should have caught both. Proposed: fix: lines 69 and 87, and apply-retrospective 132, add "(`.claude/rules/delivered-copies.md`, rule 2, *A copy may be edited in place…*)"; line 98 adds "(`.claude/rules/delivered-copies.md`, rule 4, *At every Plan Step's close…*)".

`delivery/container/.claude/skills/apply-retrospective/SKILL.md`

**FINDING-1642.** One home; uncertain; the rule unclear (OHS-15). `delivery/container/.claude/skills/apply-retrospective/SKILL.md`, *Stage 1 — triage*, lines 54-55: "- **Never** history: devlog entries, closed ADRs, closed Plan Step Gates,". A second list of what is history: devlog entries, closed ADRs, closed Plan Step Gates, released CHANGELOG versions, migrations, comments. The Agent Rule's list is the devlog, closed ADRs, commit bodies, the Decisions Log's entries and released CHANGELOG entries. The two lists differ, and neither points at the other. Why: the list stood at `d37a08f`, so round 2's close read missed it. The rule unclear: the rule does not say whether a list of "what not to change" is a telling of what history is. Proposed: question: does the list retell the Agent Rule's history? If so, fix: "**Never** history (`.claude/rules/one-home.md`, *Not a second home*), and with it closed Plan Step Gates and migrations".

`delivery/container/.claude/skills/commit-plan/SKILL.md`

**FINDING-1643.** Layout; resting on the reader; older than the rule (LAS-3). `delivery/container/.claude/skills/commit-plan/SKILL.md`, §3 *How the commits are split*, line 81; the same form in §2 (lines 59–70) and §4 (lines 112–130). Our copy, `.claude/skills/commit-plan/SKILL.md`, has the same lines: "- **Order follows where the decision lives.** A decision settled in". §3's four bullets each hold a paragraph with its reason. §2 has two such bullets ("The list may change past a point", "A planned commit may repeat over a series"). §4 has three ("An ADR inside the Change Set opens as Proposed", the sweep, the look back). None is numbered. The commit-plan manual gives the same subjects numbered parts: §2.4 *Material-first*, §2.5 *The records commits*, §2.7 *Inserted and repeated commits*, §2.10 *The sweep*, §2.12 *The look back*. Why: older than the rule's bold-lead line (`aa40496`). Refinement Round 2's Layout reader read this Agent Skill before the line existed. DECISION-15 left the rest to this read. Proposed: question: (a) number §2's, §3's and §4's parts; or (b) cut each bullet to a short item, its reason left to the manual's numbered part. Recommended (b): DECISION-7 reads facts-in-sync §4 as "a derived file applies, it does not explain", and the manual already holds each reason. Both copies change together.

**FINDING-1644.** Dependencies; checked; missed at a change (DES-3). `delivery/container/.claude/skills/commit-plan/SKILL.md`, §6 *Review protocol*, lines 147–149: "only on the reviewer's word. The rule is the commit-messages Agent Skill's, and binds". It retells commit-messages' *Rules*, "Commit on the word", and names the owner in prose only. Our copy carries `(docs/conventions/commit-messages/ §2.4, *Commit on the word*)` there; the container's copy drops it and points nowhere. The same file's §3 already points at its own commit-messages Agent Skill by path (line 95). Why: missed at a change. `15f6e88` (FINDING-202) pointed line 95 at the CBC Run's own commit-messages Agent Skill and left this line. `cb3f28c` gave our copy its reference, not the container's. The Copies script at `075a7ff` counted the hunk as the seat's; it is the seat's only in which home it names. Proposed: fix: "at every commit, not only inside a Change Set (`.claude/skills/commit-messages/SKILL.md`, *Rules*)."

**FINDING-1645.** Layout; resting on the reader; the rule unclear (LAS-4). `delivery/container/.claude/skills/commit-plan/SKILL.md`, §6 *Review protocol*, line 151. Our copy has the same lines: "**Small commits inside a planned commit, where the reviewer has". §6 holds two subjects: the stop at every boundary (147–149), and small commits with the `-detail` branch (151–161), marked by a bold lead. All three pointers into §6 mean the second subject: §4's table row, `retrospective/SKILL.md` line 125 and `apply-retrospective/SKILL.md` line 142. They name it *Review protocol*, since it has no title of its own. The manual splits the two: §2.11 *Small commits*, §2.13 *The stop at every boundary*. Why: the rule is unclear. DECISION-15 named this bold lead as an open question, and §3.2's line speaks only of bullets. Proposed: question: (a) `### 6.1 The stop at each boundary` and `### 6.2 Small commits`, with the three pointers made §6.2 *Small commits*, in both copies of commit-plan and in both retrospective Agent Skills; or (b) small commits become §7, and the anti-patterns §8. Recommended (a): no section renumbers.

`delivery/container/.claude/skills/retrospective/SKILL.md`

**FINDING-1646.** Dependencies; checked; missed at a change (DES-7). `delivery/container/.claude/skills/retrospective/SKILL.md` Stage 4 item 7, line 128; `delivery/container/.claude/skills/apply-retrospective/SKILL.md` Stage 4 item 7, lines 144–145; `delivery/container/.claude/approaches-on-trial/approach-drafting.md` *Stages*, §1 item 4, lines 51–52: "word (the Plan Step Form, *At the close*).". The reference gives a Name where the path goes. The Plan Step Form is `PLAN.md`'s, under its heading *The Plan Step Form*, in both Convention Seats; a grep for `PLAN.md` misses these lines. Why: missed at a change: `84d9c41`, the Names pass, turned "(`PLAN.md`'s step form, *At the close*)" into "(the Plan Step Form, *At the close*)" and dropped the path. Proposed: fix: "(`PLAN.md`, *The Plan Step Form*, *At the close*)" in the two Agent Skills; in approach-drafting, "is the Plan Step Form's (`PLAN.md`, *The Plan Step Form*)".

`delivery/container/.claude/skills/visual-comparison/SKILL.md`

**FINDING-1647.** Layout; resting on the reader; missed at a change (LAS-5). `delivery/container/.claude/skills/visual-comparison/SKILL.md`, §1 *When this fires*, line 32. Our copy has the same lines: "**The candidate set must contain at least one thing that is not a". §1 holds three subjects: when the comparison fires (28–30, 43–47); the rule that the candidate set holds a non-picture (32–35); and which notations a project can build (37–41). The candidate set's rule is told again in §2, step 2 (lines 59–60) and step 3 (62–64). The manual gives each its own part: §2.1 *A non-picture in the set*, §2.4 *The buildable notations*. Why: missed at Refinement Round 2's Layout read, which read layer 6's Agent Skills whole. The lines are from `2505f78` and `b3c35a6`, before it. Proposed: question: (a) the candidate set's rule moves to §2, step 3, as its one home; the buildable notations get a section of their own; §1 keeps when it fires; or (b) §1 is retitled to cover all three. Recommended (a). Both copies change together.

**FINDING-1648.** Layout; resting on the reader; older than the rule (LAS-6). `delivery/container/.claude/skills/visual-comparison/SKILL.md`, §4 *What the render has caught*, line 99. Our copy has the same lines: "- **The dialect built for the job can be the one that fails.**". §4's five entries are bold-led bullets. Each holds a paragraph and the case it came from, as §4's own lead asks. None is numbered. The *Decisions* footer, in both copies, points at one by quoting it: "§4's 'using a dialect is not fighting it'". Why: older than the rule's bold-lead line (`aa40496`). Proposed: fix: `### 4.1` to `### 4.5`, each titled by its subject, in both copies; the footer line points at §4.5.

**FINDING-1649.** Layout; resting on the reader, quote checked (left G7 visual-comparison). line 126: "(§1, *When this fires*) covers this" starts at column 0 inside an indented list item: a lazy continuation. LES met it again in passing. Proposed: fix: indent it, in both copies if ours has it.

`delivery/container/docs/glossary/container.md`

**FINDING-1650.** One home; checked; missed at a change (OHS-1). `delivery/container/docs/glossary/container.md`, the entries, lines 19-21 and 24-25: "- **Delivery Pin** — the Concept Deliverer's commit every delivered". The entries for Delivery Pin and Read-Through Commit define both numbers. `delivered-copies.md` rule 1 (lines 21-24) defines the same two, in bold, as their home. The glossary entries name no owner. The two tellings already differ: the glossary says the Delivery Pin is "kept in the Decisions Log's last delivery entry"; rule 1 says it is "taken from the Delivery Staging's name". The Delivery Take entry on line 32, by contrast, names `.claude/rules/delivered-copies.md`. Why: missed at a change. The file came in at `3630ed9` (ADR-0078). The check that should have caught it is writing rule 9's "pointing at the text that defines it", or ADR-0079's bold check ("bold once ... in the file its glossary entry points at"). Proposed: fix: each entry ends with its owner, "(`.claude/rules/delivered-copies.md`, rule 1)".

**FINDING-1651.** One home; resting on the reader; missed at a change (OHS-3). `delivery/container/docs/glossary/container.md`, lines 29-31, 35-37, 66-67: "- **Delivery Staging** — a delivery as it arrives in `temp/`: a". OHS-1's pattern, for three more entries whose fact is stated in a shipped file: - Delivery Staging: `delivered-copies.md` rule 5 (lines 92-97), and `temp/README.md` lines 11-14; - CBC Run Ask: `delivered-copies.md` rule 4 (lines 75-90); - Agent Skill Template, "never edited in place": `delivered-copies.md` rule 8 (line 157). None carries a bold defining line there, so these rest on whether that rule is the text that defines them. Why: missed at a change, `3630ed9` and `df74a6b`. Same checks as OHS-1. Proposed: fix: each entry names its rule, as the Delivery Take entry does.

**FINDING-1652.** One home; checked; missed at a change (OHS-2). `delivery/container/docs/glossary/container.md`, line 82; `delivery/container/PLAN.md`, *Legend*, line 22: "- **Plan Step Gate** — a Plan Step's exit criteria: facts that can be". The Record Stub's legend defines the Plan Step Gate in bold: "**Plan Step Gate** = exit criteria: verifiable facts, not intentions. A Plan Step is done only when every Plan Step Gate item is true." The Pure Seed's fill replaces only the text between the STEPS markers, so the legend stays in every CBC Run. The glossary retells it with no owner. Our own glossary's twin names one ("the Plan Step Form in our `PLAN.md`"). Why: missed at a change, `df74a6b` ("shared Names renamed and entered"). The same checks as OHS-1 apply. The bold script hit on `PLAN.md` line 22 went to the Writing readers as a rule 9 question, not as a home question. Proposed: fix: the entry ends "(`PLAN.md`, *Legend*)".

`delivery/fills/cbc-run-pure-playbook.md`

**FINDING-1653.** Dependencies; resting on the reader; older than the rule (DES-8). `delivery/fills/cbc-run-pure-playbook.md`, *The Plan Step Form*, *At the close*, line 104: "- [ ] No commit straddles agent and project paths.". It retells commit-messages' *The agent's own files*: a commit that touches them "touches nothing else". The items beside it point at their source (line 102 at `.claude/rules/writing.md`, line 103 at the commit-messages Agent Skill). This one names none. Why: older than the rule: `0cdc50c`, 2026-10-16, before ADR-0070. Proposed: fix: "- [ ] No commit straddles agent and project paths (`.claude/skills/commit-messages/SKILL.md`, *The agent's own files*)."

**FINDING-1654.** Dependencies; resting on the reader; older than the rule (DES-12). `delivery/fills/cbc-run-pure-playbook.md`, Step 1's comment, line 156; `delivery/method/.claude/shapes/evidence-test.md`, *How its assertions read*, lines 146–147: "(the cbc-framing Agent Skill). The README purpose paragraph and the devlog's". The playbook's comment relies on where the CBC Run Briefing is committed, the cbc-framing Agent Skill's fact. The Output Shape's "(the worked example's Runtime Ground)" relies on the worked example's numbers. Both name the source and give no path. Why: older than the rule; the Names pass (`a456f4c`, `8a4525b`) rewrote the words and kept the form. Proposed: fix: "(`.claude/skills/cbc-framing/SKILL.md`, *The record…*)"; "(`.claude/skills/cbc-framing/references/worked-example.md`, *Stage 2 — Name the enemies…*)".

**FINDING-1655.** Layout; resting on the reader, quote checked (left Steps 5..N-3). line 192: "## Steps 5..N-3" has no status box, where every other Plan Step heading has one. Proposed: fix: the heading takes `[ ]`, as the Plan Step Form gives.

`delivery/installs/pure-seed.md`

**FINDING-1656.** One home; checked; missed at a change (OHS-14). `delivery/installs/pure-seed.md`, opening, lines 32-40; `delivery/README.md`, *What the tree does not show*, line 73: "container itself. They hold two stances a CBC Run can only receive:". Both our files state that the two composed files hold two stances a CBC Run can only receive, name the same two stances, and say nothing before the CBC Run Briefing produces them. Each cites ADR-0019, a decision citation, not a Fact Reference to a living home. Neither points at the other. Why: missed at a change, `5d562d8` ("the delivery's pages meet the rule"). That commit wrote both lines in their present form; at `d37a08f` each said it differently ("the pin stance", "the pre-framing guard"). The check that should have caught it is one-home rule 6, the question at the commit. Proposed: fix: `delivery/README.md` §4 keeps the fact, as the map of what lands. The Pure Seed's paragraph points: "(`delivery/README.md` §4, *What the tree does not show*)".

**FINDING-1657.** Dependencies; checked; older than the rule (DES-9). `delivery/installs/pure-seed.md`, the paragraph after the prompt, lines 257–260: "reviewer is present (devlog 2026-09-06, "the pure seed runs").". "an agent pressed to finish skips a stop written only in a file" is stated in Living Text at `docs/models/agent.md` §5, *The context window*: "a rule that rests on a fact of the session cannot live in a file alone. Such a fact is, for example, that a reviewer is present". The line points at the devlog, which is history. Why: older than the rule (ADR-0070 decision 6); kept when `5d562d8` and `a456f4c` rewrote the paragraph. Proposed: fix: "(`docs/models/agent.md` §5, *The context window*)". The devlog entry may stay beside it as the story.

**FINDING-1658.** Dependencies; resting on the reader; missed at a change (DES-11). `delivery/installs/pure-seed.md`, after the prompt, lines 270–272: "central data. The commit-scope rule is not restated. It is in the". The rule is commit-messages' *The agent's own files*. The line names "the delivered Agent Skills", plural and with no path, so a change to that section finds no line here. Why: missed at a change: `5d562d8` rewrote the paragraph, after ADR-0070. Proposed: fix: "It is the commit-messages Agent Skill's (`delivery/container/.claude/skills/commit-messages/SKILL.md`, *The agent's own files*), and the prompt only points at it."

**FINDING-1659.** Layout; uncertain; older than the rule (LAS-12). `delivery/installs/pure-seed.md`, after step 6, line 287; also step 5, lines 201–204: "**A correct Pure Seed is checkable.** Before the agent starts, every". The Pure Seed's numbered steps are its only parts. The seed's check says it runs "before the agent starts", but it stands after step 6, *Start the agent*. After it come the CBC Run Reading's checklist (316–333) and the CBC Run Reading itself (335–338): two more subjects in step 6. Step 5 holds part of the same check (201–204), which the later list points back to: "the check in step 5 lists nothing". Why: older than this read. Refinement Round 2's Layout read did not take this page. Proposed: question: (a) the check becomes step 6, *Check the seed*, holding lines 201–204 and 287–314. Starting the agent becomes step 7, and the CBC Run Reading's checklist closes the page under a label of its own. The one pointer that moves is "step 6's prompt" (line 299). (b) It stays. Recommended (a).

`delivery/method/.claude/shapes/evidence-test.md`

**FINDING-1660.** One home; resting on the reader; missed at a change (OHS-6). `delivery/method/.claude/shapes/evidence-test.md`, *Why each rule is there*, lines 152-154; *What this document controls*, line 25; *What is exempt, and why*, lines 174-177: "- **The State Witness before the answer.** A test that fails on a status". - The header comment says "When a Red Run counts is the cbc-slice Agent Skill's Stage 3 ... not this Output Shape's" (lines 15-17). - Lines 152-154 still retell that rule's reason: a Red Run stopping on a status "has never read the store". `cbc-slice/SKILL.md` Stage 3 (lines 172-175) is its home. - The order "State Witness, then the Falsifiable Promise, then the invariant, then exact numbers" is told in the Agent Skill (lines 159-161) and the Output Shape (lines 101-112), with no reference. - The Structural Wall Check is defined in the Agent Skill (lines 194-197; the method glossary points there). The Output Shape tells it twice more, two ways: "reads the code" (line 25), and "reads the store's own list of its constraints, or ... sends the store a refusal" (lines 174-176). shapes-lifecycle §4 makes an Agent Skill ask for what its Output Shape names, so two tellings are by design. One of them still has to be the follower. Why: the reason pair stood at `d37a08f`, so round 2's close read missed it. The Structural Wall Check lines came in at `8a4525b` (round 3's work), missed at that change. Proposed: fix: line 152's reason and lines 25 and 174 cite `.claude/skills/cbc-slice/SKILL.md`, *Stage 3 — build*. Line 25 takes the Agent Skill's wording.

`delivery/method/.claude/shapes/registry-entry.md`

**FINDING-1661.** One home; checked; older than the rule (OHS-5). `delivery/method/.claude/shapes/registry-entry.md`, *The shape*, lines 58-63: "- **Every field is present.** An empty one says "none" (or". The Output Shape lists the Invariant Slice Entry's ten fields and the rule "every field is present". The Agent Skill Template `templates/registry.md` gives the same ten fields (lines 29-55) and the same rule (lines 57-58). Neither points at the other. The status values are stated in `cbc-framing/SKILL.md` outcome 2 (line 233) and in the template (lines 19-20). The Output Shape's "one of the Invariant Slice Registry's status values" (line 62) names neither. The two field lists already differ in their guidance. The template's *Adversity to create* says "from the Enemy Census in LAYER-1-ENVIRONMENT, not invented". The Output Shape's says "with the Enemy Fact it comes from". Why: older than round 2's close read. Both lines date from 2026-10-15 (`6cfd7ad`, `b7d3448`), and round 2's close read missed them. Round 3's read met it in passing (*Met in round 3, of other kinds*) and left it for this read. Proposed: question: which is the Invariant Slice Entry's home? The template is what the CBC Run fills. The Output Shape is what the close reads against. Recommended: the template. The Output Shape's skeleton then cites `.claude/skills/cbc-framing/templates/registry.md`, and the status line cites `.claude/skills/cbc-framing/SKILL.md`, *Export and handoff*.

`delivery/method/.claude/shapes/slice-record.md`

**FINDING-1662.** One home; checked; missed at a change (OHS-4). `delivery/method/.claude/shapes/slice-record.md`, *The Invariant Slice Record's order*, lines 31-54: "## The Invariant Slice Record's order". The ten sections of an Invariant Slice Record, in order, and the sentence "What spans every Invariant Slice Guarantee has its own section. What belongs to one is in its Invariant Slice Guarantee Block, and nowhere else." (line 53). `cbc-slice-workflow.md`, *The Invariant Slice Record's outline* (lines 33-73), holds the same ten sections and the same sentence (line 69). The cbc-slice Agent Skill names the workflow's outline as the home (SKILL lines 28-32). The workflow points at the Output Shape (line 39). The Output Shape never points back. Why: the pair stood at `d37a08f` ("The record's order", "The slice's record — its outline"), so round 2's close read missed it. Round 3 reworded both, in `06a3915` and `8a4525b`/`6e1d55e`, and kept both tellings. Proposed: fix: the Output Shape's section opens with "The order is the cbc-slice workflow's (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The Invariant Slice Record's outline*)." It keeps its list as the follower its *What to check at a close* reads against.

**FINDING-1663.** Dependencies; checked; missed at a change (DES-5). `delivery/method/.claude/shapes/slice-record.md`, *An Invariant Slice Guarantee Block*, lines 58–62: "The Invariant Slice Guarantee Block grows by Agent Skill Stage, the cbc-slice Agent Skill's.". Stage 1, Stage 2 and Stage 4 and what each adds are the cbc-slice Agent Skill's facts, at `.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The Invariant Slice Record's outline*, which the cbc-slice SKILL.md names as that home (lines 30–32). The Output Shape names the owner in words and gives no path. Why: missed at a change: `8a4525b` and `6e1d55e` rewrote the lines into Names and Agent Skill Stages, after ADR-0070, and added no reference. Proposed: fix: "The Invariant Slice Guarantee Block grows by the cbc-slice Agent Skill's Agent Skill Stages (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The Invariant Slice Record's outline*)."

`delivery/method/.claude/skills/cbc-framing/references/worked-example.md`

**FINDING-1664.** Layout; checked; missed at a change (LAS-9). `delivery/method/.claude/skills/cbc-framing/references/worked-example.md`, *Part 2*, line 256; the copy, `delivery/method/.claude/skills/cbc-slice/references/worked-example.md`, is byte-identical: "**Stage 1, specify-correctness,** takes the Invariant Slice Entry". Part 1 gives each Agent Skill Stage a heading, `## Stage 0 — …` to `## Stage 6 — …`. Part 2's four Agent Skill Stages are bold-led paragraphs (lines 256, 281, 296, 306). This is FINDING-227's third part, still standing. Why: missed at a change, as LAS-7. `8316ce0`, cbc-framing's references in Refinement Round 3, did not work it. Proposed: fix: `## Stage 1 — specify-correctness`, `## Stage 2 — plan`, `## Stage 3 — build`, `## Stage 4 — document` under Part 2, in cbc-framing's copy first, then cbc-slice's word for word.

`delivery/method/.claude/skills/cbc-framing/SKILL.md`

**FINDING-1665.** Dependencies; checked; older than the rule (DES-2). `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *The derivation order (not the presentation order)*, line 55. Also `cbc-framing/references/cbc-framing-workflow.md` *The order, and why it differs from the presentation*, lines 30–54; `cbc-slice/SKILL.md` Stage 2, lines 115–118, the Structural Wall ladder: "## The derivation order (not the presentation order)". The section retells `concept/03-cbc-framing.md` *The derivation order*, and the cbc-slice Agent Skill retells the ladder of `concept/02-guarantees-and-walls.md` *The ownership map*. Neither names the chapter. Across the method's Agent Skills, references and Output Shapes, `docs/concept/` appears in two lines (`the-whole-system-in-plain.md` 4, the workflow 106), and no line names a chapter's section. TODO's "Number the concept chapters' sections" says the same: "nothing points into a chapter's section today". Why: older than the rule. ADR-0070 decision 7 came on 2026-10-27; its rewrite plan named FINDING-202, 204, 216, 219 and 220, not the method's lines on the concept. DECISION-7 and DECISION-8 sent the method's texts to TODO's "Rewrite the method's texts plain", which does not name this. Proposed: question: (a) the method's texts gain one reference per section that uses a chapter part (ADR-0072), such as (`docs/concept/03-cbc-framing.md`, *The derivation order*), as part of "Rewrite the method's texts plain"; the first one fires "Number the concept chapters' sections"; or (b) ADR-0070's trigger to revisit decision 7 is weighed first, since these files would carry a reference on most sections. Recommended: (a), in that item.

**FINDING-1666.** Layout; checked; missed at a change (LAS-7). `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *Export and handoff*, lines 184–294; *The record*, lines 128–182: "## Export and handoff". The section holds 7 subjects: the 3 export files; reading each alone at the close; the CBC Framing Export Filter; the commit order; the Invariant Slice Registry's outcomes and its Agent Skill Template; the exports as living records; the README; and the handoff to the Runtime Ground. The exports' draft line is split across the two sections: added in *The record* (line 148), removed here (195–196). This is FINDING-227's first part, still standing. Why: missed at a change. DECISION-8 moved FINDING-227 to the plain-rewrite item. DECISION-16 put it in Refinement Round 3's layer 6. `4884a12`, cbc-framing's Agent Skill in Round 3, did not work it, and Round 3's endings say it was worked. Proposed: question: split by subject. For example: *The CBC Framing Exports* (files, draft line, reading alone, living records, the filter), *The commit order*, *The Invariant Slice Registry's outcomes*, *The README*, *The handoff*. Or leave it to the plain-rewrite item, which still names it.

`delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`

**FINDING-1667.** One home; resting on the reader; missed at a change (OHS-8). `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *Stage 2 — why*, lines 129-135: "**Why a trusted writer is not walled against.** Any path that goes". The reason a writer who can remove a Structural Wall is trusted, not walled against. `cbc-framing-workflow.md`, *Stage 2 — Name the enemies* (lines 201-211), gives the same reason where the Trust Assumptions are written: "a writer who can remove a Structural Wall cannot be walled against". The cbc-slice copy has no reference. Why: the pair stood at `d37a08f`, so round 2's close read missed it. Proposed: fix: the cbc-slice paragraph keeps its first sentence and cites `.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, *Stage 2 — Name the enemies*, for the rest.

`delivery/README.md`

**FINDING-1668.** Dependencies; resting on the reader; missed at a change (DES-13). `delivery/README.md` §2 *Three ways a file lands*, the first bullet, lines 26–29: "are the CBC Run's from then on. They are never delivered again.". What is copied once and never delivered again is `docs/conventions/exchange/` §3.2, *What goes*, its last paragraph, and §2.4, *The records' exception*. The second bullet carries (`docs/conventions/exchange/` §3.2, …); the first carries none. Why: missed at a change: `5d562d8` and `a456f4c` rewrote the bullet after ADR-0070. Proposed: fix: end the bullet with "(`docs/conventions/exchange/` §2.4, *The records' exception*)".

**FINDING-1669.** Layout; resting on the reader; older than the rule (LAS-1). `delivery/README.md`, §2 *Three ways a file lands*, lines 26–56; quote at line 30: "- **Pinned copies:**". §2 is three bold-led bullets, each a paragraph: the CBC Run's own from birth, pinned copies, Delivery Fills. They are its three parts, unnumbered. The paragraph on Agent Skill Templates (49–51) is about pinned copies, but stands after the third part's table. The paragraph on the method's own files (53–56) is about files the CBC Run writes, not a way a file lands. Why: older than the rule's bold-lead line (`aa40496`, DECISION-15), which left all but 16 named sections to this read. Refinement Round 2's Layout reader read layer 6's Agent Skills, Agent Rules, Output Shapes and references, not this page. Proposed: fix: `### 2.1 Own from birth`, `### 2.2 Pinned copies`, `### 2.3 Delivery Fills`, the Agent Skill Templates paragraph moved into 2.2. Question: where the method's-own-files paragraph goes; recommended §1, *The groups and the tree*, which says where things sit in the tree. `docs/models/tiers.md` line 94 points at §2 and still lands.

**FINDING-1670.** Layout; resting on the reader; older than the rule (LAS-2). `delivery/README.md`, §2 *Three ways a file lands*, line 36: " - the concept, at `docs/concept/". Where the concept lands is §3's subject, *The one exception*. §2's list tells it again, with no pointer. Why: older than this read. Refinement Round 2's Layout read did not take this page (LAS-1). Proposed: fix: ` - the concept (§3, *The one exception*)`.

**FINDING-1671.** Dependencies; checked; older than the rule (DES-10). `delivery/README.md` §5 *What a CBC Run does not get*, lines 84–85; `delivery/installs/pure-seed.md` step 4, the comment at lines 144–145: "also takes no `spring-postgres/` (`ARCHITECTURE.md` §2.2, *The Stack Group*).". The fact's home is `docs/conventions/exchange/` §3.4, *One group per file*: "a CBC Run on another stack takes the Container Group and the Method Group and leaves the Stack Group (ADR-0029)". `delivery/README.md` points at `ARCHITECTURE.md` §2.2, which restates it. The Pure Seed cites only ADR-0029, the why. Why: `delivery/README.md` 85 is older than the one-target line (round 2's rule plan, 2026-10-25); its reference dates from `37e4005`. The Pure Seed's comment was rewritten at `a456f4c` and kept the bare citation. Proposed: fix: both lines take "(`docs/conventions/exchange/` §3.4, *One group per file*)"; the Pure Seed keeps ADR-0029 beside it. That `ARCHITECTURE.md` §2.2 restates the fact is for the One home reader of ours.

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`

**FINDING-1672.** One home; resting on the reader; missed at a change (OHS-11). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *1. Record the stack decision*, lines 30-39: "Before any code, an ADR carries:". What the stack decision's ADR holds. `cbc-bootstrap/SKILL.md` Stage 1 (lines 79-83) says the same, and the two lists differ: - the walkthrough adds the application structure; - the Agent Skill adds "the app knows one identity, the `runtime` role". Neither points at the other. Why: both were rewritten at round 3 (`c449de0`, `a6ccf5b`), missed at that change. Proposed: question: which holds the ADR's contents? Recommended: the Agent Skill's Stage 1, which decides. The walkthrough's §1 keeps its trap and points there.

**FINDING-1673.** Lessons; checked; missed at a change (LES-12). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, §3 *Wire the runtime datasource*, lines 127–130: "CBC Run decided it at release, not at the CBC Bootstrap. It is never". When fail-fast on a missing secret is decided is told as what one CBC Run did. The general rule is already in the cbc-bootstrap Agent Skill's CBC Bootstrap Exclusion 6: "The question comes back at release ... It is decided there, unless this CBC Run decides otherwise by name." Why: missed at a change, `a6ccf5b`. Proposed: fix: "It is decided at the cbc-bootstrap Agent Skill's Stage 1 by name, and may be put off to release there (CBC Bootstrap Exclusion 6). It is never absorbed here."

**FINDING-1674.** Layout; checked; missed at a change (LAS-10). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, §4 *The Adversity Harness*, line 134; also line 164: "### The test runtime (once per machine; the Operator Manual's)". §4 has two parts with headings and no numbers, where §1 to §5 are numbered. The harness reference's three Fact References into it name the part by title and label: "step 4, *The Adversity Harness in the codebase*, *Traps, exact*, item 3" (`spring-harness-reference.md` lines 151–152, 158–159, 207–208). This is FINDING-228, still standing. Why: missed at a change. FINDING-228 was proposed "fix, 4.1 and 4.2", and DECISION-8 moved it to the plain-rewrite item. DECISION-16 put it in Refinement Round 3's layer 6. `63bb1db`, cbc-bootstrap in Round 3, did not work it. Proposed: fix: `### 4.1 The test runtime` and `### 4.2 The harness in code`. Writing rule 10 then applies: the parenthesis goes, and the second title is 37 characters. The three pointers become "step 4.2, *The harness in code*", with the rename grep.

**FINDING-1675.** Lessons; checked; missed at a change (LES-13). `spring-boot-walkthrough.md`, §4 *The Adversity Harness*, *The test runtime*, *Traps, exact*, item 1, lines 141–144: " from the project root. A CBC Run searched long for the cause of the "no". "A CBC Run searched long for the cause" is a story. The fact the reader needs is general: the file is ignored in the project root, and the error it gives names something else. Why: missed at a change, `63bb1db`. Proposed: fix: "`~/.testcontainers.properties` binds **only from `$HOME`,** never from the project root. In the project root it is ignored, and the error, "no valid Docker environment", does not say why."

**FINDING-1676.** Lessons; resting on the reader; missed at a change (LES-14). `spring-boot-walkthrough.md`, §5 *The adversity created*, lines 267–292: "- **Traps met:** none. Three instances, 120 requests at one instant,". - The proof across instances is introduced as "**As one CBC Run built it:**". - It ends with one run's results: "Three instances, 120 requests at one instant, no port collision across runs". That is a count from one event. - Its trial status is already said, once, in the harness reference's variation point 8: "carried here as prose until a second CBC Run builds it". A trial status may stand (ADR-0073 kept one). - The bullets between are practice stated in general. Why: missed at a change, `a6ccf5b`. Proposed: fix: the lead becomes "**How it is built, built once so far:**". The last bullet becomes "**Traps known:** none yet."

**FINDING-1677.** One home; checked; missed at a change (OHS-10). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *The exit*, lines 296-301: "The project's records grown: the stack, the run and test commands,". The list of exit records. `cbc-bootstrap/SKILL.md` Stage 5 (lines 246-249) states the same list, as the step the agent runs: run and test commands, the Operator Manual linked, "no business behavior yet" said outright, the CBC Bootstrap Probe's deletion scheduled. The walkthrough's copy names no source. Why: the pair stood at `d37a08f`, so round 2's close read missed it. Round 3's read met it in passing (*Met in round 3, of other kinds*) and left it for this read. Proposed: fix: the walkthrough's section points: "The exit records are the cbc-bootstrap Agent Skill's (`.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 5 — certify and close*)."

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`

**FINDING-1678.** Layout; resting on the reader, met in passing (met LAS). §1, §2, §3, *Bound facts*: §1's and §3's *Bound facts* are bullets, and §2's are a numbered list. Proposed: fix: one form, with LAS-11.

**FINDING-1679.** Lessons; uncertain; missed at a change (LES-18). provenance counts that open or frame a reference: - `spring-harness-reference.md` line 7; - `cbc-bootstrap/references/app-structure.md` lines 27–28, "One CBC Run used it across nine Invariant Slices"; - `cbc-bootstrap/templates/readme-run-test.md` line 8, "the Spring and Maven shape CBC Runs used"; - `infra-establish/SKILL.md` line 29, "as two CBC Runs confirmed it", and lines 140–142, "Two CBC Runs worked it, and the shape below is theirs"; - `infra-establish/references/establishment-walk.md` lines 4–5, "Two CBC Runs have done it", and line 151, "as CBC Runs did it"; - `infra-establish/references/postgres-setup-walkthrough.md` lines 3–4, "as two CBC Runs did it": "PostgreSQL. Three CBC Runs built them. The shape below is the latest". - Each line says how many CBC Runs a reference or a default came from. None states a rule through a case. - `infra-establish/SKILL.md` lines 134–135 already state the status in general: "The references are written from what CBC Runs did, not rules." - The counts go stale at the next CBC Run that runs the Agent Skill. - Whether a provenance count is a story line, or a trust signal DECISION-40's reason keeps, no decision says. Why: missed at a change, `63bb1db`, `c449de0`, `a6ccf5b`, `580f7dc` and `1f13fee`. Most were "lived" markers (FINDING-224). Proposed: question: keep the counts as the reader's measure of how proven a reference is, or let the one general line in `infra-establish/SKILL.md` stand for all and drop the counts. For example, "the sequence end to end", "What to do, end to end, for one Infrastructure Service.", "The shape below is the most corrected one."

**FINDING-1680.** Lessons; resting on the reader; missed at a change (LES-3). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, opening, *Why code exists here at all*, lines 23–30: "Harness's outcomes, not by the problem. Three CBC Runs produced them". - The reason the five files carry code rests on what happened: "Three CBC Runs produced them almost identically, and each one's only route was reading the earlier CBC Run's source." - The lesson is already stated in general just before: these five are shaped by the stack and the Adversity Harness's outcomes, not by the problem. - "The last CBC Run's source" is a CBC Run the reader cannot place. Why: missed at a change, `63bb1db` (the common cause above). Proposed: fix: "This file carries code so that no CBC Run has to derive these five from another's source. ... It does not hold for these five, which are shaped by the stack and the Adversity Harness's outcomes, not by the problem, so they come out the same in every CBC Run on this stack." Drop the "Three CBC Runs produced them" sentence.

**FINDING-1681.** Lessons; checked; missed at a change (LES-4). `spring-harness-reference.md`, §1 *The database base*, *Outcomes it realizes*, item 3, line 61: "3. the latest CBC Run's correction: **the Database Role Split holds". The outcome is labelled by the CBC Run whose correction it was. The outcome stands without the label. The label is a story line. Why: missed at a change, `63bb1db` (it was "the third pass's" before `a6ccf5b`). This is FINDING-223's residue. Proposed: fix: "3. **the Database Role Split holds in evidence runs.** The container is set up by ..."

**FINDING-1682.** Layout; uncertain; the rule unclear (LAS-11). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, §1 *The database base*, line 139, under "**Bound facts.**" (line 131). The same in §2 to §4, and elsewhere as listed below: "- **The mounted `bootstrap.sql` is the one source.** The Adversity". Labels that recur in every section of one form, and the bold-led bullets under them, each with its own reason. Counted: - the harness reference, "**Bound facts.**" in §1 to §4, then 6, 2 (numbered), 3 and 5 bold-led bullets; §5, 4 more; - the walkthrough, "**Verified:**" and "**Traps:**" in each step, and §5's "**As one CBC Run built it:**" with 6 bold-led bullets; - the setup walkthrough, §9's two bold-led paragraphs (186, 213) and §6's trap (130); - `apply-retrospective/SKILL.md`'s "**How a row is decided:**" (48) and "**The plain pass,**" (95), which DECISION-15 named. I judge these two not parts: they sit inside an Agent Skill Stage, which is a label of its own, not a numbered section (`docs/conventions/conventions/` §1.4, *Agent Skill Stages*). Read as parts, the harness reference's §1 alone needs 6 numbers. Why: the rule is unclear. The line says nothing of a label on its own line or a bold-led paragraph. DECISION-8 kept the stack's texts out of Layout's reach until the plain rewrite. The setup walkthrough's §9 got its second bold-led paragraph in `580f7dc`, after the line stood. Proposed: question: (a) a label that recurs in every section of one form, and the bullets under it, are that form's fixed labels, as an Output Shape's *Skeleton:* is. A bold-led paragraph outside such a form is judged as a bullet is. §3.2 gains that line. (b) Each is a part and is numbered. Recommended (a). Under (a), only the setup walkthrough's §9 and the walkthrough's §5 are left to judge.

**FINDING-1683.** Lessons; checked; missed at a change (LES-5). `spring-harness-reference.md`, §1, *Bound facts*, the Database Role Split bullet, lines 144–149: " Harness run as the container's superuser, an earlier CBC Run's". "an earlier CBC Run's shape" says who once did it this way. The lesson ("proves the round-trip but not the authority") stands without it. Why: missed at a change, `63bb1db` ("the second pass's shape" before). Proposed: fix: "An Adversity Harness run as the container's superuser proves the round-trip but not the authority."

**FINDING-1684.** Lessons; uncertain; missed at a change (LES-11). `spring-harness-reference.md` §1, line 162; §2, lines 213–215; §4, lines 430–434. Also `app-structure.md` *The Stack Default*, lines 53–54: " image. The latest CBC Run ran 12 against the Runtime Ground's 11.". - Each line is an example under a rule stated in general: Flyway's majors may differ; the bases grow only what every test needs; any pool sized to the count satisfies the barrier; a feature starts with as few classes as it needs. - So each meets §2.6 as an example. - But each names the case by a CBC Run the reader cannot place: "The latest CBC Run", "(the latest CBC Run) and virtual threads (an earlier one)", "One feature a CBC Run built". - The brief names a named CBC Run's incident in shipped prose as the candidate. Why: missed at a change, `63bb1db` (§1, §2, §4) and `c449de0` (`app-structure.md`). Proposed: question: keep them as examples, or drop the CBC Run tags and keep the numbers. For example: "Flyway 12 against the Runtime Ground's 11 is fine." "A fixed pool of that size and virtual threads both satisfy it."

**FINDING-1685.** Lessons; checked; missed at a change (LES-6). `spring-harness-reference.md`, §3 *The Migration Path Test*, *Bound facts*, first bullet, lines 287–292: " the first Invariant Slice needs V1, the latest CBC Run changed this". What happens to the assertion when the first migration lands is told as what one CBC Run did. It is FINDING-223's "the third pass evolved this to…", reworded. Why: missed at a change, `63bb1db`. Proposed: fix: "When the first Invariant Slice needs V1, the assertion becomes "count ≥ 1 and none failed": the count changes, the proof does not."

**FINDING-1686.** Lessons; checked; missed at a change (LES-7). `spring-harness-reference.md`, §3, *Bound facts*, the refused DDL bullet, lines 298–302: " CBC Run met this: a copy wired as the right name but without the". The reason for the refused DDL check comes as a case one CBC Run met. The fact that follows is general, so the case clause adds only a story. It was "(lived once)" before `a6ccf5b` (FINDING-224). Why: missed at a change, `a6ccf5b`. Proposed: fix: "**The refused DDL shows the authority, not only the identity.** A copy wired as the right name but without the Database Role Split, the grants missing and `bootstrap.sql` not mounted, passes the identity assertion and fails here, with the Runtime Ground's own message."

**FINDING-1687.** Lessons; uncertain; missed at a change (LES-10). `spring-harness-reference.md`, §6, item 1, lines 467–470, and item 6, lines 493–495. Also `spring-boot-walkthrough.md` §5, line 240: " version.** `postgres:17` here, because the Runtime Grounds CBC Runs". - Two values in the file are justified by what past CBC Runs did. Item 1: "because the Runtime Grounds CBC Runs built were 17". Item 6: "A hundred is what the CBC Runs used". - The walkthrough adds "(one CBC Run used a hundred)". - The lesson is general in each place: the image follows the Runtime Ground's major version, and the request count is free as long as the requests are released together. - DECISION-40's reason, a count read as why a line is required, may or may not reach a value's provenance. Why: missed at a change, `a6ccf5b` (item 1) and `63bb1db` (item 6). Proposed: question: does DECISION-40 reach these? If not, fix: "`postgres:17` here, the illustration's version." "A hundred is this file's number." "(a hundred, say)".

**FINDING-1688.** Lessons; checked; missed at a change (LES-8). `spring-harness-reference.md`, §6 *The variation points*, item 4, lines 482–489: " missing location with a warning. An earlier CBC Run caught it in". The two ways to catch a missing migrations directory are told as which CBC Run did which: "An earlier CBC Run caught it in Flyway config ... The latest relied on the Migration Path Test". It was "The second pass closed it", FINDING-223's text. Why: missed at a change, `63bb1db`. Proposed: fix: "Two ways work: Flyway config (`failOnMissingLocations(true)`), or the Migration Path Test plus a tracked directory. Catching it nowhere leaves the suite green on a clone that cannot migrate."

**FINDING-1689.** Lessons; checked; missed at a change (LES-9). `spring-harness-reference.md`, §6, item 9, lines 526–530: " once left the rule unsaid, so each CBC Run decided by habit.". - The variation point tells its own history: "This file once left the rule unsaid ... One CBC Run met why". - FINDING-223 named this: "Variation point 9 tells its own history." It still does. - The lesson, why a substring fails, is general and stands without the history. Why: missed at a change, `63bb1db` and `a6ccf5b` ("Lived once" before). Proposed: fix: "9. **A body is asserted by path, never by substring.** A substring cannot tell `3` from `30`, cannot say a field exists, and cannot say one is absent. The rule, decided before the first Invariant Slice and held after:"

**FINDING-1690.** One home; resting on the reader; missed at a change (OHS-7). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, *The variation points*, item 9, lines 526-541: "9. **A body is asserted by path, never by substring.** This file". The harness reference states, as a rule decided by a CBC Run, that a body is asserted by path and never by substring. The Evidence Test Shape states the same rule for every test: "An answer's fields by their path, never by a substring" (`delivery/method/.claude/shapes/evidence-test.md` line 134). Both land in the same CBC Run. Neither points at the other. Why: both stood at `d37a08f`, so round 2's close read missed them. They are in two groups, and a per-file read cannot show the pair. Proposed: fix: item 9 keeps its stack form (the test-support reader, `$.id`) and cites `.claude/shapes/evidence-test.md`, *How its assertions read*, for the rule.

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`

**FINDING-1691.** Layout; resting on the reader, quote checked (left I4). *What the file does not carry*, lines 57–62: Two of the three bullets say what the file does carry. Proposed: fix: they move to the section that holds what it carries.

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`

**FINDING-1692.** Lessons; resting on the reader; missed at a change (LES-1). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *The boundary you must keep — WHAT before HOW*, lines 36–39: "This rule was written from a practice with two roles: one decided". The paragraph tells where the rule came from: a practice with two roles. That is an origin story, which a CBC Run never reads (ADR-0073). The lesson in it is general: one agent does both jobs, and the boundary between Agent Skill Stages keeps them apart. It is FINDING-224's "distilled from a two-seat discipline", reworded. Why: missed at a change, `c449de0` (the common cause above). Proposed: fix: "One agent decides both **what** is built, under which constraints, and **how** it is realized in code. The boundary between the Agent Skill Stages keeps the two apart."

**FINDING-1693.** Lessons; uncertain; missed at a change (LES-2). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 2 — write the CBC Bootstrap Requirements*, lines 146–149. Also *Stage 3 — the CBC Bootstrap Step Plan*, line 178: "other manuals. Both CBC Runs that ran this Agent Skill put it at". - The default path is given through a count of past CBC Runs. The count goes stale when the next CBC Run runs this Agent Skill. - Line 178, "The shape CBC Runs have used is five steps", states the plan's shape the same way. - DECISION-40 kept counts like this in the cbc-framing workflow, "since the CBC Run reads it as why the line is required". It is not clear whether its reason reaches a default path or a plan's shape. Why: missed at a change, `c449de0` (line 148) and `a6ccf5b` (line 178). Proposed: question: does DECISION-40's reason reach this? If not, fix: "The usual place is `docs/construction/`." and "The usual shape is five steps (see the walkthrough's steps):".

**FINDING-1694.** One home; checked; missed at a change (OHS-9). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 4 — execute, step by step*, lines 205-211: "- Widen the build's test includes, so integration tests run under the". Two bullets of Stage 4 retell outcomes the walkthrough states: - "extract into it, never overwrite", each hygiene file's Stack Overlay, the README kept (lines 205-208), against `spring-boot-walkthrough.md` step 2 (lines 49-58); - the widened test includes (lines 209-211), against step 4 (lines 192-194). The harness reference names the walkthrough as the owner of the second ("stated as an outcome in the walkthrough", lines 461-463). The bullet just above points at the walkthrough for "the outcomes and the traps", but it names other items and no step. Why: the pair stood at `d37a08f`, so round 2's close read missed it. Round 3 rewrote both files (`c449de0`, `a6ccf5b`) and kept both tellings. Proposed: fix: each bullet ends with its step, "(`.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, step 2)" and "(… step 4)".

`delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md`

**FINDING-1695.** One home; resting on the reader, quote checked (left I5). lines 89–94; `postgres-setup-walkthrough.md` 84–87; `templates/bootstrap.sql` 59–61: The default-privileges sentence has three homes. DES, in passing, confirms it stands. Proposed: fix: role-split is the home; the other two point at it.

`delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`

**FINDING-1696.** One home; checked; missed at a change (OHS-12). `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, lines 34-36, 72-75, 107-108: "The rule: secrets and what varies per machine are variables.". The setup walkthrough says "It owns nothing" and names the Database Role Split as its home. It still retells three rules whose home is `establishment-walk.md`, without a reference: - "The canonical command is `podman compose`, whatever provider stands behind it" (line 35), against the walk's Stage 1 (lines 63-64); - secrets as variables and decided identities literal (lines 72-75), against the walk's Stage 5 (lines 132-135); - expected results as comments beside each query, "so the reader needs no other doc open" (lines 107-108), against the walk's Stage 5 (lines 141-142). Why: all three pairs stood at `d37a08f`, so round 2's close read missed them. Both files were rewritten at `580f7dc`. Proposed: fix: each of the three lines cites `.claude/skills/infra-establish/references/establishment-walk.md` and its Stage, or is cut to its Postgres-only part.

**FINDING-1697.** Lessons; checked; missed at a change (LES-17). `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, §1 *Declare the service*, *Podman notes*, lines 54–56: "- the `name:` pin is a correction a CBC Run made. Without it, the". The pin is introduced as "a correction a CBC Run made". The reason after it is general. Why: missed at a change, `580f7dc`. Proposed: fix: "- the `name:` pin is required. Without it, the volume's identity depends on the directory the file happens to run from."

`delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`

**FINDING-1698.** Lessons; uncertain; missed at a change (LES-15). `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Stage 0 — readiness*, check 2, lines 49–56: " Refusal or verdict. Then the check passes. Two CBC Runs met this,". - "Two CBC Runs met this, the same way both times" is a count. The lesson follows it in general: "A fact CBC Framing left unstated is written where it belongs." - It is the same fact as the cbc-framing workflow's "Two CBC Runs left it out and wrote it later", which DECISION-40 kept as why the line is required. - It was "Lived twice" before `580f7dc` (FINDING-224). Why: missed at a change, `580f7dc`. Proposed: question: does DECISION-40 reach a second telling of the same count? If not, fix: drop "Two CBC Runs met this, the same way both times."

**FINDING-1699.** Dependencies; checked; missed at a change (DES-6). `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` *Deviations*, line 132, and *Records and outputs*, line 198; `cbc-bootstrap/references/app-structure.md` line 22; `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` lines 3–4, "SKILL.md" twice; `infra-establish/templates/bootstrap.sql` lines 34 and 38, in a comment the CBC Run keeps in its filled file: "another family of constraints, may force departures from `establishment-walk.md` or". Each names a file by its name alone. In a filled `bootstrap.sql`, "postgres-role-split.md, Naming across a cluster" and "verify-database-model.sql's role filter" no longer resolve: FINDING-207's case. Why: missed at a change, each time at ADR-0070 decision 8's question: - cbc-slice-workflow 3–4: `45d8974` (FINDING-219's 41 paths) left them; - app-structure 22: `63bb1db` put the file name where "the pom convention's" stood; - infra-establish 132 and 198: `1f13fee` put the file name where "the walk" stood; - bootstrap.sql 34: `7857b48`, the day `2ccaa58` fixed the same template's other comment; 38: `1f13fee`. Proposed: fix: each takes its path from the root: `.claude/skills/infra-establish/references/establishment-walk.md`; `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`; `.claude/skills/cbc-slice/SKILL.md`; `.claude/skills/infra-establish/references/postgres-role-split.md`; `infrastructure/postgres/verify-database-model.sql`.

**FINDING-1700.** Lessons; checked; missed at a change (LES-16). `infra-establish/SKILL.md`, *Records and outputs*, the first bullet's last item, lines 158–161: " would have held. One CBC Run kept an Infrastructure Establishment Log beside such records, and". The only reason given for "no Infrastructure Establishment Log" in a repo with records is one CBC Run's case. It was "Lived once: a log beside" before `580f7dc` (FINDING-224). Why: missed at a change, `580f7dc` and `1f13fee`. Proposed: fix: "An Infrastructure Establishment Log beside such records holds nothing they do not."

**FINDING-1701.** Layout; checked; missed at a change (LAS-8). `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Records and outputs*, line 179; also its Stage 6 Gate (lines 109–113); `references/establishment-walk.md` Stage 6 (158–168); `references/postgres-setup-walkthrough.md` §9 (225–228): " - `infrastructure-contract.md`, the Infrastructure Contract: the". What the Infrastructure Contract holds is told in four places. Two are in one file. The lists differ: the Agent Skill gives 4 items, and the walk gives 5, adding "what Infrastructure Services exist". `infra-serve/SKILL.md` lines 70–73 name *Records and outputs* as the form's home. This is FINDING-227's second part, still standing. Why: missed at a change, as LAS-7. `580f7dc`, infra-establish in Refinement Round 3, did not work it. Proposed: question: one home. Recommended *Records and outputs*, which infra-serve already points at, carrying the walk's fifth item if the reviewer keeps it. The Stage 6 Gate, the walk's Stage 6 and the setup walkthrough's §9 then point at it.

`delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`

**FINDING-1702.** One home; resting on the reader; missed at a change (OHS-13). `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`, *Hard lines*, lines 84-85: "3. Destructive acts need explicit confirmation.". Two working rules: destructive acts need confirmation, and installs on the host are the reviewer's own acts. `infra-establish/SKILL.md`, *The rule for results* (lines 125-127), states both, with no reference either way. Why: the pair stood at `d37a08f`, so round 2's close read missed it. Proposed: fix: infra-serve's two lines cite `.claude/skills/infra-establish/SKILL.md`, *The rule for results*.

#### Round 3: how it reads

##### Layer 1: the conventions manual

`docs/conventions/conventions/README.md`

**FINDING-1703.** Writing, rule 9; checked; missed at a change (WA-1). `docs/conventions/conventions/README.md`, §2.3 *The list of what derives*, lines 224–225: "*What this is made usable as* is the list a change to the page". "the list a change to the page walks". "Walks" is the Change Walk, written as a lowercase verb. The same section's last sentence, line 233, already says "runs the Change Walk on that list". Why: missed at a change. `0803717` worked DECISION-39 in this file, and its sweep for "walk" stopped at the two sentences the decision quoted. Proposed: fix: "*What this is made usable as* is the list the Change Walk runs on when the page changes, placed as the answer to the need. Each entry has:"

**FINDING-1704.** Writing, rule 3; resting on the reader; missed at a change (WA-2). `docs/conventions/conventions/README.md`, §3 *Adding a convention*, lines 326–328: "header comment); the PLAN has no per-convention Plan Steps.". "No CHANGELOG line and no Plan Step." has two parts. Their two reasons follow in one sentence, joined by a semicolon. Why: missed at a change. `0803717` rewrote line 328 for the close read and kept the semicolon. The check that should have caught it is that commit's re-read of its changed lines. Proposed: fix: "No CHANGELOG line and no Plan Step. The CHANGELOG logs the concept's versions, and has no place for a convention's entry (`CHANGELOG.md`'s header comment). The PLAN has no Plan Step per convention."

##### Layer 2: project-recording

`docs/conventions/project-recording/README.md`

**FINDING-1705.** Writing, rule 1; checked; older than the rule (WA-3). `docs/conventions/project-recording/README.md`, §4.4 *How the devlog is written*, lines 375–377: "Written for future-you, not an audience: fragments fine, spelling". It gives devlog entries a style of their own ("fragments fine, spelling irrelevant"). The writing rule names no such style, and rule 2 asks for short sentences. `devlog/README.md`, the devlog form in our Convention Seat, follows this line; that copy is leftover E12. Why: older than the rule. The line dates from `9a1637d` (2026-09-18), and the writing rule from ADR-0053 (2026-10-15). Round 3 read it, and the question of the rule's reach was settled only in ADR-0079. Proposed: fix: "- Written for future-you, not an audience: short plain sentences, as every record is, and honest." The next sentence, about "I don't understand why this works", stays as it is. Fix this line before `devlog/README.md` (E12), since that file follows it. For line 767, question: if "messy" means the voice, write "The devlog may be raw: dead ends, hunches, open questions. ADRs and the playbook must be settled."

**FINDING-1706.** Writing, rule 5; resting on the reader; missed at a change (WA-4). `docs/conventions/project-recording/README.md`, §5.5 *When an item is written*, line 450: "so it stops occupying your head". The reason for adding an item at once is given as a head occupied. Why: missed at a change. `29e3ce0` (Refinement Round 3) changed this line and kept the figure. FINDING-322's fix was not carried to the other lines that use the same figure. Proposed: fix, together with WA-5: "is found, so no one has to remember it (§11, *The flow between records*, rule 3)."

**FINDING-1707.** Writing, rule 6; checked; missed at a change (WA-5). `docs/conventions/project-recording/README.md`, §5.5 *When an item is written*, lines 450–451: "(§11, *The flow between records*, rule 3: moments,". The reference ends "rule 3: moments, not schedules". The rule's bold lead, line 762, is "Update at natural moments, not on a schedule." The tail rewords it inside the address. Why: missed at a change. `29e3ce0` fixed the reference's title and kept the reworded tail. The Wiring script checks the title, not text after the step. Proposed: fix: "(§11, *The flow between records*, rule 3)", in WA-4's line.

**FINDING-1708.** Writing, rule 9; checked; missed at a change (WA-6). `docs/conventions/project-recording/README.md`, §9.4 *How a playbook is written*, line 671: "1. **Birth:** the playbook's Plan Steps fill the plan, and its \"Steps". The first of the playbook's four moments is labelled "Birth", a noun for the event. Why: missed at a change. `f435e8d` worked DECISION-36 in this file: "CBC Run Birth by name" at line 74, and the idioms at 175 and 244. It left this lead. Proposed: fix: "1. **At birth:** the playbook's Plan Steps fill the plan, …". The other three leads stay.

**FINDING-1709.** Writing, rule 3; checked; older than the rule (WA-7). `docs/conventions/project-recording/README.md`, §12 *The fewest records needed*, lines 784–785: "The test for adding any record is always the same: *will someone —". "*will someone — probably future-you — need this answer and be unable to reconstruct it?*" The aside sits between two dashes. Why: older than the rule (`9a1637d`, 2026-09-18). FINDING-964's list of this file's dash asides missed it. Proposed: fix: "*will someone, probably future-you, need this answer and be unable to reconstruct it?*"

##### Layer 3: the other manuals, the Idea Models, the concept

`concept/00-cbc.md`

**FINDING-1710.** Writing, rule 9; uncertain; the rule unclear (WD-6). `concept/00-cbc.md`, *The two components*, line 65; `concept/03-cbc-framing.md`, *The derivation order*, lines 26 and 57: "**The world model — the Layered System.** A containment description of". Three paragraph leads, not list items, hold a Name in bold away from its home. At 00 line 65 it is the Layered System, whose home is chapter 01. At 03 line 26, "**Choose the Falsifiable Promise.**", the home is chapter 01. At 03 line 57, "**Cut into Invariant Slices.**", the home is chapter 04. ADR-0079's reason, that the bold marks the item, fits a paragraph lead as well. Its words name only a list item. The script sent the worked example's paragraph leads to their reader on the same question. Why: the rule is unclear. ADR-0079, 2026-11-01, wrote the exception for list items only. Proposed: question: (a) decision 2 reaches a paragraph's bold lead, and the rule's line says "a bold lead"; the three stand. (b) It does not; the six paragraphs of 03's *The derivation order* and 00's two components become list items, which decision 2 covers. That fix is editorial, and no wording changes. A third way, the bold dropped from the leads, would cost every other step's lead.

`concept/01-layered-system.md`

**FINDING-1711.** Writing, rule 2, 5; resting on the reader; missed at a change (WD-2). `concept/01-layered-system.md`, *LAYER-3-AREAS — Responsibility Areas*, lines 59-60: "owner.** Often the honest answer is a single Responsibility Area — that". A dash joins two clauses, "the answer is a single Responsibility Area" and "that is a confirmed answer, not a gap". The close read fixed this exact form in the same chapter, a dash joining two clauses (FINDING-1136), and "honestly" two sections down (FINDING-1135, "can rightly become"). This line was in neither list. Why: missed at a change. `1f0c17e` rewrote the line. The close read's FINDING-1136 listed the chapter's other dashes (then lines 45, 49-50, 92) and not this one (then line 57). Proposed: fix, editorial: "owner.** Often the right answer is a single Responsibility Area. That is a confirmed answer, not a gap."

`concept/03-cbc-framing.md`

**FINDING-1712.** Writing, rule 9; checked; missed at a change (WD-1). `concept/03-cbc-framing.md`, *The derivation order*, line 54: "is more than one Responsibility Area, examine the seams between them". "the seams between" two Responsibility Areas. The method's glossary defines exactly this thing as the Responsibility Area Seam, "the line between two Responsibility Areas" (`delivery/method/docs/glossary/method.md`, line 145). The same file a CBC Run receives with the concept lists it, so a reader meets the lowercase word beside its Name and must decide which is meant. Why: missed at a change. `1f0c17e` rewrote the line on 2026-11-01, after ADR-0078 had delivered the method's Names, and kept "the seams". The close read's rule 9 check for a word with a rival should have caught it. Proposed: fix, editorial (the same thing, said in plain words): "is more than one Responsibility Area, examine where each two of them meet". Plain words, not the Name, since the Name's home is the method's workflow, below the concept.

**FINDING-1713.** Writing, rule 2; resting on the reader; missed at a change (WD-3). `concept/03-cbc-framing.md`, *The derivation order*, line 59; `concept/04-cbc-slice.md`, *The four phases*, line 35: "Invariant Slice Registry's ordering is an expectation, not a commitment; evidence from". A semicolon joins two ideas: the order is an expectation; evidence may reorder what is left. The same at chapter 04 line 35, "ranking of Structural Walls, the strongest available; choosing a weaker Structural": the Structural Wall is the strongest available; a weaker one needs a stated reason. 2 lines. Why: missed at a change. `1f0c17e` wrote 03 line 59, and `eefdced` rewrote 04 line 35, after FINDING-1149's fix set the form. The close read listed 03's opening and 04's opening, not these. Proposed: fix, editorial: 03, "Invariant Slice Registry's ordering is an expectation, not a commitment. Evidence from built Invariant Slices is allowed to reorder what remains."; 04, "ranking of Structural Walls, the strongest available. Choosing a weaker Structural Wall than possible is a decision that needs a stated reason."

`docs/conventions/agent-arrangement/README.md`

**FINDING-1714.** Writing; resting on the reader, quote checked (left noticing). §2.4, lines 220 and 251: "a fact whose failure is not noticing it" cannot be read once (rule 1, rule 8). WF-1 meets the same words in `CLAUDE.md` lines 43–44. Proposed: fix, with WF-1, in the same words in both: say what goes wrong, "a fact the agent fails by not noticing that it applies".

**FINDING-1715.** Writing, rule 9; checked; missed at a change (WB-2). `docs/conventions/agent-arrangement/README.md` §2.4, *How the Entry File is written*, line 229. Also §3.1 line 298 and §4 line 412: "5. local rules that have no moment.". - line 229, at the Name's home, writes the thing as "local rules"; - line 412, "**A local rule with a moment**", is a rule in that slot, so the Name; - line 298, "a moment-bound local rule the Entry File must not hold", means a rule that is not in the slot. Written lowercase, it reads as the Name it is not. DECISION-23 settles a clash with a Name by plain words. Why: missed at a change: `b379c2d` gave Local Rule its glossary entry, pointing at §2.4. The home's three lines were not given the Name. Rule 9 says the Name goes in with the home that defines it. Proposed: fix: line 229, "5. Local Rules, rules of this project only that have no moment."; line 412, "**A Local Rule with a moment**"; line 298, "for a rule of this project only that has a moment, which the Entry File must not hold".

`docs/conventions/commit-messages/README.md`

**FINDING-1716.** Writing, rule 2; resting on the reader; missed at a change (WB-6). `docs/conventions/commit-messages/README.md`, *What it is for*, lines 17-20: "sentence, the rule that the agent waits at each commit, alone with". "Lived here since: 480 commits under it by 2026-09-19, and CBC Run 3 held forty-four commits on the stop sentence, the rule that the agent waits at each commit, alone with no Enforcement Gate." The inserted gloss splits "the stop sentence" from "alone". "Alone with no Enforcement Gate" now reads as if it belongs to "each commit". Why: missed at a change: `103a301`, the close read's fix, added the gloss inside the sentence. Proposed: fix: "Lived here since: 480 commits under it by 2026-09-19. CBC Run 3 held forty-four commits on the stop sentence alone, with no Enforcement Gate. The stop sentence is the rule that the agent waits at each commit."

`docs/conventions/commit-plan/README.md`

**FINDING-1717.** Writing, rule 5; resting on the reader; missed at a change (WB-4). `docs/conventions/commit-plan/README.md` §1, *What a commit plan is*, line 62. Also §2.4, *Material-first*, line 89: "held. The second kind makes the tail of a plan provisional, and the". The manual says "the tail of a plan" (line 62) and "the provisional tail" (line 89). Both commit-plan Agent Skills dropped the same figure for "provisional commits" (ours `31156de`; the container's on FINDING-1310, as the figures of DECISION-26's journey row). The manual is their foundation and still says "tail". Why: missed at a change: `31156de` changed the derived Agent Skill. The check of a forced change against the manual should have found the manual's word (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 4). Proposed: fix: line 62, "The second kind makes the plan's last commits provisional, and the plan says so."; line 89, "the provisional commits, the revision commit and the Proposed-then-Accepted ADR are the normal course".

`docs/conventions/exchange/README.md`

**FINDING-1718.** Writing, rule 9; checked; older than the rule (WB-1). `docs/conventions/exchange/README.md`, *What this is made usable as*, line 48. Also *What this does not cover*, line 594: "preceded it or not. Birth is a delivery into the root plus the". Line 48 uses "Birth" as a noun for the event, capitalized only because it opens a sentence. Line 594, "**The birth procedure**", uses it the same way. Why: older than the rule (`e22d7f6`, 2026-09-29). Then missed at a change: `b379c2d` worked DECISION-36's "other uses" in the glossary's Pure Seed entry, repo-hygiene and shapes §4.3, and did not grep the exchange manual. Proposed: fix: line 48, "A CBC Run Birth is a delivery into the root plus the Delivery Fills"; line 594, "**How a CBC Run is born**". Question: is "birth entry" the noun DECISION-36 names? If yes, "the entry written at CBC Run Birth" or "the Decisions Log's first entry"; if no, it stands as English.

**FINDING-1719.** Writing, rule 3; resting on the reader; older than the rule (WB-8). `docs/conventions/exchange/README.md` §2.2, *The CBC Run*, lines 99-105. Also §4, *The Delivery Take*, lines 334-337: "Log carrying two numbers — **the Delivery Pin**, the Concept Deliverer's commit its". One sentence opens with a fragment, then a dash, then two numbers, each with its definition, joined by commas. The next sentence adds a second dash. These lines are the home of both Names. Lines 334-337 use the same form: "Nothing in `temp/` is in force until it is copied into place — a staged Agent Skill is a file, not an Agent Skill, and a Plan Step that opens meanwhile runs on the held copy". That is two consequences chained after a dash. Why: older than the rule (`f95dd0d`, 2026-09-25). The pass (`1576044`) changed only its Names. Proposed: fix: "The copies. And one line in its own Decisions Log per Delivery Note, which carries two numbers:", then a list, "**the Delivery Pin**, the Concept Deliverer's commit its copies equal;" and "**the Read-Through Commit**, its own commit the Concept Deliverer last read up to." Then "Its edits since the Delivery Pin need no record of their own. They are the diff against what was delivered, and git holds it." At 334-337: "Nothing in `temp/` is in force until it is copied into place. A staged Agent Skill is a file, not an Agent Skill. A Plan Step that opens meanwhile runs on the held copy."

**FINDING-1720.** Writing, rule 9; uncertain; the rule unclear (WB-9). - `docs/conventions/exchange/README.md` §2.2, *The CBC Run*, line 116; - the same file, *The seats*, lines 68 and 69; - `docs/conventions/commit-messages/README.md` §3, *The Concept Deliverer's habit*, line 96; - `docs/conventions/README.md`, *The order of the conventions*, line 39: "**One Delivery Pin** for everything delivered, as on every flow". - line 116 bolds Delivery Pin a second time in its own home, after line 100; - lines 68 and 69, "**The CBC Run's**" and "**The Concept Deliverer's**", bold two Names away from their home, the Tiers Model; - line 96, "**The Concept Deliverer did not take it**", and line 39, "**Work no Agent Skill or Agent Rule covers**", bold a phrase that holds a Name. None of these is a list item. Each is a paragraph's bold lead or a bold phrase in running prose. The rule's letter allows neither. The script missed them because each bold span holds more than the Name. Why: the rule is unclear. ADR-0079 answered FINDING-1384 for list items only. Proposed: question: does a paragraph's bold lead, or a bold phrase in prose, that holds a Name count as marking the Name? Recommended: yes for line 116, where its home file then shows two bolds for one Name: drop the bold there. For the other four, the reviewer decides. Either the rule names a paragraph's lead beside a list item's, or the bold goes.

**FINDING-1721.** Writing, rule 5; checked; missed at a change (WB-3). `docs/conventions/exchange/README.md` §3.4, *One group per file*, line 231. Also §3.5, *The Foundation Line in a copy*, line 254: "Agent Skill belongs to one group and travels whole, never split". Line 231 says an Agent Skill "travels whole". Line 254 says "the line travels with the copy as a live claim". These are the last two living uses in the repo. The same words were fixed in shapes ("is delivered whole", `efb8cef`) and `ARCHITECTURE.md` ("which every copy carries", `5d0f5ca`). Why: missed at a change: `a60a357`, "the exchange meets the writing rule", 2026-11-01, rewrote both lines after DECISION-26 (2026-10-30) and kept the word. The round 3 close read passed them too. Proposed: fix: line 231, "An Agent Skill belongs to one group and is delivered whole, never split across two."; line 254, "every copy carries the line as a live claim."

**FINDING-1722.** Writing, rule 3, 1; resting on the reader; older than the rule (WB-7). `docs/conventions/exchange/README.md` §3.7, *The Delivery Note*, lines 271-280: "Why it matters to this CBC Run — the part a diff cannot carry. A verdict". The section opens with three fragments in running prose, joined by a dash: what changed, why it matters, and a verdict. Then a fourth, "Nothing that needs our repo to verify:". The reader must work out that these are a Delivery Note's parts, and how many there are. No line says so first. Why: older than the rule (`523798e`, 2026-09-25). The pass (`1576044`) and round 3's two reads changed only its words. Proposed: fix: open with "A Delivery Note says three things:", then a list: - "what changed since the CBC Run's Delivery Pin, so the CBC Run can diff the Delivery Staging against what it holds and find the Delivery Note wrong;" - "why it matters to this CBC Run, the part a diff cannot carry;" - "a verdict on everything the CBC Run addressed to us since we last read it, in the CBC Run's order." The sentences on verdicts and "Nothing that needs our repo to verify" follow as they stand.

`docs/conventions/facts-in-sync/README.md`

**FINDING-1723.** Writing, rule 2; checked; missed at a change (WB-5). `docs/conventions/facts-in-sync/README.md`, *What it is for*, lines 27-30: "Refinement Round 2 found two Finding Kinds, One home and". "Refinement Round 2 found two Finding Kinds, One home and Dependencies, the checks of a fact's home and of what a text stands on, resting on rules split that way, and the rules came here before it read (ADR-0065)." That is two appositives, a participle clause and a second main clause in one sentence. "It" in "before it read" has to be traced back to Refinement Round 2. Why: missed at a change: `0cdd102`, the close read's fix, wrote this sentence. Nothing read it after. Proposed: fix: "Two of Refinement Round 2's Finding Kinds rested on rules split that way. One home checks a fact's home. Dependencies checks what a text stands on. The rules came here before that round read (ADR-0065)."

`docs/conventions/README.md`

**FINDING-1724.** Writing, rule 9, 8; resting on the reader; older than the rule (WB-10). `docs/conventions/README.md`, *The order of the conventions*, lines 50-52: "the records they govern, are not stages of this and fire on their". "The other conventions, and the records they govern, are not stages of this and fire on their own moments." "Stages" means steps of the order, where Agent Skill Stage and Approach on Trial Stage are Names. "This" stands for the order, which the sentence does not name. Why: older than the rule (`722357d`, 2026-09-30). `103a301` renamed "the chain" to "this order" on line 48 and left this line. Proposed: fix: "The other conventions, and the records they govern, are not steps in this order. Each fires at its own moment."

`docs/conventions/shapes/README.md`

**FINDING-1725.** Writing, rule 9, 8; resting on the reader; older than the rule (WC-3). `docs/conventions/shapes/README.md`, *What it is for* line 13; §2, *What an Output Shape is not*, lines 134-138; *What this does not cover*, line 333: "hidden for opposite reasons. Trial evidence is withheld **so that it". "trial evidence" has a meaning of this repo's own: material in `docs/baselines/` withheld from every CBC Run, so that a later derivation can be measured for independence (ADR-0035 decision 6, ADR-0033). The manual uses it at line 13 before saying what it is, and §2 gives the meaning only by contrast with an Output Shape. It has no Glossary Name, and it sits beside two Names it could be taken for: Approach on Trial, and the method's Evidence Test. "A derivation" (line 137) is not said either. Why: the rule is unclear on a phrase made of two English words whose sum is ours. DECISION-23 settled such phrases one by one ("living text", "receipt branch"); this one was not met. Older than ADR-0076's rule 9. Proposed: question: (a) a Glossary Name, such as Trial Evidence, with shapes §2 or a Local Map in `docs/baselines/` as its home; its other living uses, `ARCHITECTURE.md` line 248 and `TODO.md` line 717, follow; or (b) English, said once in plain words at shapes line 13: "material kept in `docs/baselines/` and never shown to a CBC Run, so its work can be measured blind".

`docs/glossary.md`

**FINDING-1726.** Writing, rule 7; resting on the reader; missed at a change (WC-2). `docs/glossary.md`, group *Kinds of text*, the Canonical Description entry, lines 113-120: "reference, not that it is correct. It is today's understanding,". The entry's first lines say a Canonical Description is "how we understand a thing today" and "may be wrong or incomplete". Its last lines say both again: "'Canonical' means the reference, not that it is correct. It is today's understanding". Only "changed only for a reason that is recorded" is new. Why: missed at the change. `a575fb5` split the entry's first sentence into "It may be wrong or incomplete. It is the one that counts regardless."; `b379c2d` reworded the closing sentence in plain words. Neither weighed the two against each other under rule 7. Proposed: fix: lines 118-120 become "they differ at the edges (ADR-0039). It changes only for a reason that is recorded."

**FINDING-1727.** Writing, rule 7; checked; missed at a change (WC-1). `docs/glossary.md`, group *Kinds of text*, the Idea Model entry, lines 121-123: "repo writing its own Convention Manual for it. A repo adapts it in a Convention Manual". The entry says twice, back to back, that a repo adapts an Idea Model in its own Convention Manual. First as a clause: "each repo writing its own Convention Manual for it". Then as a sentence: "A repo adapts it in a Convention Manual". The second adds only the Fact Reference. Why: missed at the change. `b379c2d` ("the glossary meets the rule again", Round 3's close read) replaced the figure "like an interface" with the clause, beside a sentence that already said it. The rule 7 read at that commit's review should have caught it. Proposed: fix: "an idea any repo can adapt, its rules varying by repo. Each repo adapts it in a Convention Manual of its own (`docs/models/idea-to-output.md` §2, *The kinds*, and §5, *An Idea Model and a concept*)."

**FINDING-1728.** Writing; resting on the reader, quote checked (left E13). line 250: The Agent Skill Stage entry writes "`cbc-slice`'s Stage 3". Conventions §1.5 and DECISION-27 ask for the kind word: "the cbc-slice Agent Skill's Stage 3". WF-14 meets the same form in the container's writing rule 9. Proposed: fix, with WF-14: the kind word.

`docs/models/idea-to-output.md`

**FINDING-1729.** Writing, rule 9, 8; checked; missed at a change (WD-4). `docs/models/idea-to-output.md`, §2, *The kinds*, line 38; the Name used at lines 24, 93 and 155: "| Work Approach | how a piece of work is done | an Agent Skill, an Agent Rule, an Approach on Trial, a record's form in its header comment |". `docs/glossary.md`'s Output Form entry points at this section, "(`docs/models/idea-to-output.md` §2, *The kinds*)". §2's table never names an Output Form or says what one is; it writes "a record's form" in lowercase. The model then uses the Name three times, in the drawing (24), §4.1 (93) and §6.1 (155), and nowhere says what it is. A grep finds no defining line in any file under `docs/models/`. Why: missed at a change. `11389e9` (round 3's work, FINDING-513) brought "Output Forms" into lines 24, 93 and 155, and left §2 as it was. FINDING-513 judged "a record's form" fine as the glossary's own wording, but did not check that §2 is the Name's home. The close read did not catch it. Proposed: fix: line 38's last cell, "an Agent Skill, an Agent Rule, an Approach on Trial, an Output Form"; and line 42 opens with one sentence, "An Output Form is how one output is written, read while it is written, such as a record's header comment." It states what the glossary entry already says. As a change to an Idea Model, it runs the Change Walk.

`docs/models/tiers.md`

**FINDING-1730.** Writing, rule 9; resting on the reader; missed at a change (WD-5). `docs/models/tiers.md`, §3.3, *Upward harvest*, line 114; the drawing, line 29: "Up is harvest, and only through records: the tier above reads a". The glossary's Record Harvest entry points here, "(`docs/models/tiers.md` §3.3, *Upward harvest*)". The section defines the thing as "harvest", lowercase, and never writes the Name. The drawing writes "▲ harvest:" too (line 29). Elsewhere a lowercase "harvest" that means this thing was fixed to the Name: FINDING-580, `TODO.md`'s "the harvest discipline"; FINDING-690, the playbook's "Harvest lands here". DECISION-26 keeps "harvest" as a figure, which settles rule 5 only. Line 75's "it is harvested" is a verb, and stays English. Why: missed at a change. `2ccc26a` rewrote line 114 for FINDING-526, which read it for rule 7 only. The close read did not read it for the Name. Proposed: fix: "Up is the Record Harvest, and only through records: the tier above reads a"; line 29, "▲ Record Harvest: a Run Repo's surprises". Question for the title *Upward harvest*: it stays, read as an English direction word, or it is retitled with the Name and the rename grep. Its references include the glossary entry and §3.5 line 147.

##### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

`devlog/README.md`

**FINDING-1731.** Writing; resting on the reader, quote checked (left E12). lines 9–10: "fragments fine", following project-recording §4. The writing rule covers every new record line (ADR-0079, doubt 8). WA-3 meets project-recording's line; WG-2 the container's Record Stub. Proposed: fix, with WA-3 and WG-2: the line goes, or says "short sentences".

`PLAN.md`

**FINDING-1732.** Writing, rule 6; resting on the reader; missed at a change (WE-11). `PLAN.md`, Step: Birth CBC Run 6, own items, line 159: "CBC Run 6's CBC Run Briefing is the reviewer's: checkout, in". A bare "checkout". Line 138 of the same Plan Step writes `checkout`. Why: FINDING-1183 listed line 138 only, and 1210 listed TODO only. Proposed: fix: "is the reviewer's: `checkout`, in".

**FINDING-1733.** Writing, rule 9; resting on the reader; the rule unclear (WE-12). `PLAN.md`, the titles of two Plan Steps, lines 213 and 301: "(`.claude/rules/working-a-reading.md`, `commit-plan`, the Foundation Check)" (213).". The titles list `commit-plan` (213, 301) and `approach-drafting`, `approach-evaluation` and `visual-comparison` (301). These are bare names in backticks: not paths, and with no kind word. Line 135 uses paths and a Name instead. Why: the rule is unclear here. FINDING-1158 asked whether a Plan Step title's parenthesis, a list the Plan Step Form defines, counts as a labelled list. Its ending was "fixed", and no call answered the question. Proposed: question: does the title's list take the kind word, "the commit-plan Agent Skill", or the path? Or does it stand as the form's list?

**FINDING-1734.** Writing; resting on the reader, quote checked (left E15). line 238: The ticked item starts in lowercase, "the Exchange Convention says". All the others start with a capital. Proposed: fix: "The Exchange Convention says".

`README.md`

**FINDING-1735.** Writing, rule 8; resting on the reader; older than the rule (WE-13). `README.md`, *Success criteria*, line 33 (also 38); `ARCHITECTURE.md` §3, *What must stay true*, line 212: "the archive copy is demoted to a historical snapshot." (README 33); "the archive it came from is a frozen snapshot, never a source" (ARCHITECTURE 212).". README is for someone arriving from outside, as its header says. It names "the archive" at 33 and 38. It says what the archive is, "the archive repo, `system-design-method`", only at 55. `ARCHITECTURE.md` never says. Why: README 33 is older than the rule (`8032035`, 2026-08-27), and the round 3 reads did not list it. Proposed: fix: README 33: "the copy in the archive repo, `system-design-method`, is demoted to a historical snapshot"; ARCHITECTURE 212: "the archive repo it came from, `system-design-method`, is a frozen snapshot".

`temp/README.md`

**FINDING-1736.** Writing, rule 8; resting on the reader; missed at a change (WE-5). `temp/README.md`, body, line 15: "once it has served, and git history keeps every version.". "Each is deleted once it has served". It does not say when that is. Why: FINDING-1167 named this line with the codemap's. The codemap was fixed (`ARCHITECTURE.md` 256); this line was not. Proposed: fix: "Each is deleted once the work that needed it is done, and git history keeps every version."

**FINDING-1737.** Writing, rule 9; resting on the reader; missed at a change (WE-1). `temp/README.md`, body, line 18; `TODO.md`, Next, "Decide which ideas here are Idea Models", line 767: "the records map lists" (temp 18); "refinement's DECISION-12 map shows" (TODO 767).". Both lines call project-recording §1 a "map", the word DECISION-23 keeps for the Local Map. Why: temp 18 is FINDING-1171's line. The endings list 1171 as fixed. The line never changed: `c57a713` and `a6f2a67` touched the file, and `fab7214` fixed only `CLAUDE.md` for 1235. TODO 767 was not in 1171's list. No grep for "map" ran at either fix. Proposed: fix: "which project-recording's list of the records names"; TODO 767: "as project-recording's list of the records shows (the refinement's DECISION-12)".

`TODO.md`

**FINDING-1738.** Writing, rule 9; resting on the reader; missed at a change (WE-8). `TODO.md` 40 ("Read CBC Run 6"), 48 ("Unlock the folders"), 682 ("Run this repo's retrospective"), 705 ("Read the frozen CLAUDE template's…"): "Trigger: the close of the Plan Step that runs CBC Run 5's birth." (682).". Four nouns for the event: "Its birth Plan Step" (40), "before its birth" (48), "CBC Run 5's birth" (682), "No birth can judge" (705). Line 927 already writes "CBC Run 5's CBC Run Birth". Why: DECISION-36's fix, `bcf3010`, took only the lines FINDING-1181 listed. No grep for "birth" ran. Line 682 is also leftover E8, as a passed trigger. This finding is about the word. Proposed: fix: "The Plan Step of its CBC Run Birth stopped"; "before its CBC Run Birth"; "CBC Run 5's CBC Run Birth"; "No CBC Run Birth can judge".

**FINDING-1739.** Writing, rule 5; resting on the reader; missed at a change (WE-15). `TODO.md` 703 ("Read the frozen CLAUDE template's…"); 1066 ("Name the discipline…"): "from the method's first" (703); "not master text" (1066).". "the method's first walk", and a proposed name, "lived is evidence, not master text". Why: this is FINDING-1207's question part. Its ending was "fixed", and no call answered either question. "walk 1" may be a trial's label (`docs/baselines/cbc-derived-claude-walk1.md`). Proposed: question: is "walk" a label, so it stands? Is "master" in a quoted proposed name a figure? If both are figures: "from the method's first trial"; "lived is evidence, not text to copy".

**FINDING-1740.** Writing, rule 9; resting on the reader; missed at a change (WE-10). `TODO.md`, Next, "Decide whether a commit plan's look-back…", lines 84-85. Its home is `.claude/approaches-on-trial/auto-run.md` line 48, in Refinement Layer 5: "Real question being what the auto-run Approach on Trial calls one it must not decide" (TODO 85).". Auto-run defines "a Real question, one the CBC Run must not decide alone". It has one capital, and neither glossary lists it (grep). Why: lines 84 and 85 were rewritten at `e5a874b` and `bcf3010` around the word. It was missed at both changes, and the round 3 reads never met it. Proposed: question: give it a Name, with an entry pointing at auto-run.md, or use plain words, "a question the CBC Run must not decide alone", here and at its home.

**FINDING-1741.** Writing, rule 9; resting on the reader; missed at a change (WE-3). `TODO.md`, Next, "Decide whether our own forms become Output Shapes", lines 480-481: "rules: a manual's, a CBC Run Reading's.". "The open forms are those in rules". These are `convention-manual.md` and `exchange-reading.md`, both Agent Rules. Why: FINDING-1190 names line 480 and is listed as fixed. `bcf3010` did not change it. Proposed: fix: "The open forms are those in Agent Rules: a manual's, a CBC Run Reading's."

**FINDING-1742.** Writing, rule 8, 6; resting on the reader; missed at a change (WE-14). `TODO.md`, Next, "Read text for its level in the chain", line 619: "Found at the design's commit 5". "the design" is named nowhere in the item. It is the design of DECISION-19, 29 and 32, ADR-0078. The reader cannot tell which commit 5 is meant. Why: at `af6a3ea`, 2026-10-31, and not listed by round 3's close read. Proposed: fix: "Found at commit 5 of ADR-0078's commit plan".

**FINDING-1743.** Writing, rule 9; resting on the reader; missed at a change (WE-7). `TODO.md`, Next, "Read text for its level in the chain", line 629: "conventions §1 is the item above". A bare "conventions §1". It is the only one in Living Text outside `temp/` (grep). Why: written at `580acdc`, 2026-10-31, after DECISION-24. Missed at that change and by round 3's close read. Proposed: fix: "the conventions manual §1 is the item above".

**FINDING-1744.** Writing, rule 9; resting on the reader; missed at a change (WE-6). `TODO.md`, Next, "Rewrite the method's texts plain", lines 646-647: "the Output Shapes, the cbc-slice Agent Skill's" (646), then "Agent Skill and workflow (`2674c03`)." (647).". "the cbc-slice Agent Skill's Agent Skill and workflow". The line used to say "`cbc-slice`'s skill and workflow", meaning the `SKILL.md` file and its workflow reference. The kind-word replacement doubled the Name. Why: introduced at `bcf3010`, and its diff read missed it. Proposed: fix: "the cbc-slice Agent Skill's `SKILL.md` and workflow".

**FINDING-1745.** Writing, rule 9; resting on the reader; missed at a change (WE-2). `TODO.md`, Next, the item's title, lines 885-886: "how to treat a Skill". "a Skill Template". Why: this is FINDING-1199. Its ending was "fixed", but `bcf3010` changed only line 898. A miss at the fix, the DECISION-34 kind. Proposed: fix: "how to treat an Agent Skill Template". Grep the title's first words first, since a trigger may quote them.

**FINDING-1746.** Writing, rule 8; resting on the reader; missed at a change (WE-4). `TODO.md`, Later: "Name when a CBC Run is read", line 1138; "Decide how CBC Run Readings work…", line 1150; "Say once that a CBC Run Reading's decisions…", line 1158; "Harvest how public docs beyond the README live…", line 1257: "(2026-10-01, the working draft)" (1138); "the milestone that fires it" (1257).". "the working draft" names a deleted draft, not who raised the item (devlog 2026-10-01, later: "The draft is gone"). "The milestone" is never named. Why: these are parts of FINDING-1214. It is listed as fixed, but `bcf3010` changed 248, 853, 1026 and 1139 only. Proposed: question: who raised the three, or else plain words, "(2026-10-01, from the draft of working a reading, now gone)". Which milestone fires the 1257 item: for example, "a CBC Run first writing public docs beyond its README"?

**FINDING-1747.** Writing, rule 9; resting on the reader; missed at a change (WE-9). `TODO.md`, Known issues, line 1275: "The Runtime Ground template". The file meant is the infra-establish Agent Skill's `templates/compose.yaml`, which says `postgres:17` (checked). "Template" is lowercase. FINDING-1169 and 1200 fixed the same word elsewhere. Why: at `e5a874b`, which changed "The ground template" to this. The change took the Name Runtime Ground and left "template". Proposed: fix: "The infra-establish Agent Skill's Agent Skill Template `templates/compose.yaml`".

##### Layer 5: our agent setup

`.claude/approaches-on-trial/auto-run.md`

**FINDING-1748.** Writing, rule 9; checked; missed at a change (WF-5). `.claude/approaches-on-trial/auto-run.md`, *Stages*, step 4, line 48: "is a Real question, one the CBC Run must not decide alone;". "Real question" is capitalized like a Name and given a meaning of its own, but it is in no glossary, and its second word is lowercase. `TODO.md` line 85 cites this file as its home: "a Real question being what the auto-run Approach on Trial calls one". Why: missed at a change: `448a16c` (2026-11-01) wrote the line. Proposed: question: plain words, "past which is a question the CBC Run must not decide alone", with `TODO.md` 85 following; or a Name with a glossary entry pointing here. Recommended: plain words, since the line already defines it in place.

`.claude/approaches-on-trial/model-placing.md`

**FINDING-1749.** Writing, rule 9; checked; missed at a change (WF-4). `.claude/approaches-on-trial/model-placing.md`, *Stages*, step 7, lines 41 to 42: "7. **Grep, then walk.** Grep every reference in Living Text to the facts' old". "then walk what stands on the Idea Model and on the lower text", with a Fact Reference to facts-in-sync §4, the Change Walk's home. The Change Walk is meant and written as a lowercase verb. Why: missed at a change: `448a16c` wrote the bold lead "Grep, then walk." on 2026-11-01, after DECISION-39. Proposed: fix: "7. **Grep, then run the Change Walk.** Grep every reference … (…); then run the Change Walk on what stands on the Idea Model and on the lower text (…)."

`.claude/approaches-on-trial/refinement.md`

**FINDING-1750.** Writing, rule 9; checked; missed at a change (WF-3). `.claude/approaches-on-trial/refinement.md`, *What this is made usable as*, line 47: "What derives from this page is that list. A change here walks it.". The manual form's sentence in its old wording; "walks" names the Change Walk in lowercase. This page keeps the manual form's sections. Why: missed at a change: DECISION-39's work (`103a301`, `0cdd102`, `efb8cef`) swept the manuals; this page is an Approach on Trial with the manual form. Proposed: fix: "What derives from this page is that list. A change here runs the Change Walk on it."

`CLAUDE.md`

**FINDING-1751.** Writing, rule 2, 3; checked; missed at a change (WF-1). `CLAUDE.md`, the second header comment (under *Records*), lines 38 to 44: "1. True of this project and nowhere else — else it is a". "else it is a convention, stated once, there": "there" points at nothing. Line 43 to 44, "a fact whose failure is not noticing it", cannot be read once. Each test chains its reason on with a dash. The container's copy of the same comment was fixed by FINDING-1278 and 1279 (`delivery/container/.claude/CLAUDE.md` lines 60 to 66); ours was not. Why: missed at a change. `fab7214` ("our Entry File and Agent Rules meet the rule again") edited line 42 of this comment and did not carry FINDING-1278's fix. The leftover agent-arrangement §2.4 line ("a fact whose failure is not noticing it", 220) is the source this comment retells; this is its follower in our Entry File, not the same line. Proposed: fix, as the container's: "1. True of this project and nowhere else. Otherwise it belongs in a manual, stated once." / "2. No moment. Otherwise it goes where the moment is: …" / "3. Nothing else would deliver it: a stance, or a fact nobody would notice was missing." Settle it with the agent-arrangement leftover, so the source and this retelling say the same.

**FINDING-1752.** Writing, rule 9; checked; older than the rule (WF-2). `CLAUDE.md`, the same comment, lines 41 to 42; `.claude/rules/foundation-check.md`, header comment, lines 8 to 9, and *Decisions*, line 80: "paths: list for an Agent Rule about one directory.". Three lines spell out the Name's definition instead of writing it: "`.claude/rules/` with a paths: list for an Agent Rule about one directory"; "an Agent Rule with paths: loads only when a file is touched"; "why not an Agent Rule with paths:". Why: `CLAUDE.md` line 42 was missed at a change: `fab7214` (18:03 the same day) rewrote it from "a rule" to "an Agent Rule" after the Name existed. The two foundation-check lines are older than the Name (`ecda44f`, `2158499`); `b379c2d` added the Name without a grep for its definition's wording. Proposed: fix: "or a Paths Rule in `.claude/rules/` for one directory"; "a Paths Rule loads only when a file is touched with the agent's tools"; "why not a Paths Rule, a `CLAUDE.md` line, or a hook now". The container's `delivery/container/.claude/CLAUDE.md` lines 64 to 65 carry the same wording (reader G's file).

`.claude/rules/convention-manual.md`

**FINDING-1753.** Writing, rule 3, 2; resting on the reader; missed at a change (WF-6). `.claude/rules/convention-manual.md`, *The sections, in this order*, item 3, lines 42 to 46: "shipped or the Concept Deliverer's, with the moment it opens at — or". One sentence carries the list's content, its marks, its moment, and, after a dash, the other case, "nothing shipped", and what a repo then holds. Why: missed at a change: `ecda44f` (2026-10-30) rewrote the line and kept the dash. Proposed: fix: "everything derived from the manual, each by path from the repo root, marked shipped or the Concept Deliverer's, with the moment it opens at. When nothing ships: "nothing shipped", and then what a repo holds."

**FINDING-1754.** Writing, rule 3, 2; resting on the reader; missed at a change (WF-7). `.claude/rules/convention-manual.md`, item 7, lines 80 to 82: "Where the reasoning rests on the Agent Model, a Fact Reference to the part it rests on, such as". "…such as (`docs/models/agent.md` §8, …) (`docs/conventions/conventions/` §2.7, …)." Two parentheses stand together. Nothing tells the example from the item's own source, and the sentence has no verb. Why: missed at a change: `839f785` (2026-11-01) added the second parenthesis beside the first. Proposed: fix: "Where the reasoning rests on the Agent Model, it carries a Fact Reference to that part, such as (`docs/models/agent.md` §8, *Choosing a channel*). Why: (`docs/conventions/conventions/` §2.7, *The channel*)."

`.claude/rules/writing.md`

**FINDING-1755.** Writing, rule 9, 6; uncertain; older than the rule (WF-8). `.claude/rules/writing.md`, *The rules*, rule 6, line 30: "exactly: ADR-0052, FINDING-7, WORK-9, `exchange-read`. Define each". The rule's own example of a name written exactly is a bare Agent Skill name in backticks, the form DECISION-27 retired. It is the last backticked Agent Skill name in our agent files. Why: older than the rule (`5c5ac7d`, 2026-10-18); DECISION-27's sweep left it. Proposed: question: keep it as a label, or replace it: "ADR-0052, FINDING-7, WORK-9, the exchange-read Agent Skill".

##### Layer 6: `delivery/`, what ships

`delivery/container/CHANGELOG.md`

**FINDING-1756.** Writing, rule 3; resting on the reader; older than the rule (WG-7). `delivery/container/CHANGELOG.md`, the *Versioning* placeholder, lines 5–7: "[SemVer](https://semver.org/); a Concept Repo versions its concepts;". The placeholder chains three parts with semicolons: "An app releases SemVer; a Concept Repo versions its concepts; CBC Framing decides." Why: missed at a change. The sentence is older than the rule (`e418e9d`, the starter kit), but `b451eb9` edited it ("Framing" to "CBC Framing") and left the chain. Proposed: fix: "Versioning: <what is a version here? An app releases [SemVer](https://semver.org/). A Concept Repo versions its concepts. CBC Framing decides. The answer replaces this placeholder.>"

`delivery/container/.claude/decisions.md`

**FINDING-1757.** Writing, rule 8; resting on the reader; missed at a change (WG-6). `delivery/container/.claude/decisions.md`, header comment, line 27: "fix it before the bootstrap commit.". No text the CBC Run holds defines "the bootstrap commit". The phrase appears nowhere else in the repo. The Pure Seed names "the hygiene commit" and "the seed commits". Step 0 is "Bootstrap", and CBC Bootstrap is a Stack Group Name for a later Plan Step, so a reader can take the phrase three ways. Why: the round 3 reads missed it. The line dates from `c3a737b` (2026-10-21), after the writing rule (ADR-0053), and has not changed since. Proposed: fix: "fix it before this file is first committed."

`delivery/container/.claude/rules/delivered-copies.md`

**FINDING-1758.** Writing, rule 9; uncertain; the rule unclear (WG-5). `delivery/container/.claude/rules/delivered-copies.md`, rule 1, lines 21 and 23. These are script hits: "- the **Delivery Pin:** the Concept Deliverer's commit these copies equal, but for". Delivery Pin, and Read-Through Commit on line 23, are bold. Our glossary points both at `docs/conventions/exchange/` §2.2, which does not bold them. So these are the only bold uses in Living Text outside the glossaries, and they sit away from the home. Each item opens with "the", so the bold does not open the item, and ADR-0079's allowance for a list lead does not reach it as written. DECISION-22 took the same bold out of the exchange-read Agent Skill (FINDING-639). In a CBC Run, though, this Agent Rule is the only text that defines the two numbers, and the container's glossary entries name no home. Why: the rule is unclear. It does not say which line defines a shared Name in a CBC Run when the delivered entry names no home. Proposed: question. Either (a) the bold goes at both lines, as at FINDING-639, recommended because the bold-once check counts our Master Copies; or (b) delivered-copies rule 1 is the CBC Run's defining line, and each item drops its "the" so the bold opens the item: "- **Delivery Pin:** the Concept Deliverer's commit …".

**FINDING-1759.** Writing; resting on the reader, quote checked (left G5). lines 21–22: "these copies equal, but for its *Decisions* footers". "Its" has a plural antecedent. Proposed: fix: "but for their *Decisions* footers".

`delivery/container/.claude/rules/one-home.md`

**FINDING-1760.** Writing, rule 9; checked; missed at a change (WF-12). `delivery/container/.claude/rules/one-home.md`, *The rules*, rule 3, lines 27 to 28: "reads it in the owner's place. An Invariant Slice Registry entry". The thing is written as the registry's Name plus the lowercase word "entry". Why: missed at a change: `ddd6057` wrote it, after the Name was given. Proposed: fix: "reads it in the owner's place. An Invariant Slice Entry does this: it links the Invariant Slice Record it sums up."

**FINDING-1761.** Writing, rule 9; checked; missed at a change (WF-10). `delivery/container/.claude/rules/one-home.md`, *Decisions*, line 52: "- ADR-0053 — the one-home rule loads in every session". "the one-home rule". Our copy's footer, line 68, says "the one-home Agent Rule". Why: missed at a change: `ac34e28` (2026-10-31) wrote it, after DECISION-27; `ddd6057` did not catch it. Proposed: fix: "- ADR-0053 — the one-home Agent Rule loads in every session".

`delivery/container/.claude/rules/shapes-lifecycle.md`

**FINDING-1762.** Writing; resting on the reader, quote checked (left G7 shapes-lifecycle). line 73: "Either of the last three" can name only two. Proposed: fix: "Any of the last three".

`delivery/container/.claude/rules/writing.md`

**FINDING-1763.** Writing, rule 9; checked; missed at a change (WF-14). `delivery/container/.claude/rules/writing.md`, rule 9, line 55: "delivered-copies rule 4", "`cbc-slice`'s Stage 3";". The example writes an Agent Skill in backticks, not with its kind word, as DECISION-27 reads rule 9. It follows the container glossary's Agent Skill Stage entry (line 86), which is left E13's form. Why: written at `ddd6057`; missed at a change. Proposed: question: settle it with left E13, and this example follows.

**FINDING-1764.** Writing, rule 9; checked; missed at a change (WF-13). `delivery/container/.claude/rules/writing.md`, *Before and after*, the After text, line 94. This line is the container's alone: "> red. That Red Run is owed in the build stage.". The example meant to show the rule writes the cbc-slice Agent Skill's Stage 3 as "the build stage", in lowercase. Why: missed at a change: `ddd6057` edited this line ("red run" to "Red Run") and kept "the build stage". Proposed: fix: "That Red Run must happen in Stage 3, build." This also drops "owed", which FINDING-1344's call says is not a dead figure.

`delivery/container/.claude/skills/commit-plan/SKILL.md`

**FINDING-1765.** Writing; uncertain; not traced (WF-15). `delivery/container/.claude/skills/commit-plan/SKILL.md`, line 9. Script hit: "A **Change Set** is a body of work that needs more than one commit.". Change Set is bold. Ours dropped this bold at FINDING-626, by DECISION-22, and DECISION-33 says the container's copy takes our fixes. But the container glossary's Change Set entry (line 93) names the commit-plan Agent Skill as where a CBC Run finds it, so from the CBC Run's side this may be the home. AGS judged the hunk the seat's. Why: not traced. Proposed: question: drop the bold, as DECISION-22 named 626; or keep it as the CBC Run's home of the Name, a seat difference ADR-0069 allows. Recommended by WF: drop it. By AGS: keep it.

`delivery/container/devlog/devlog.md`

**FINDING-1766.** Writing, rule 2; checked; missed at a change (WG-2). `delivery/container/devlog/devlog.md`, header comment, line 5: "For your later self: fragments fine, honesty mandatory. Never rewrite an earlier entry.". The Record Stub tells every CBC Run that its devlog entries may be fragments. The line is also written in fragments. Doubt 8 named only our `devlog/README.md` and project-recording §4, the leftover E12. This is a third place, and it ships. Why: missed at a change. `2fca3bf` edited this line and kept "fragments fine". Doubt 8 was decided later, and it named only our two lines. Proposed: question, decided with E12 and project-recording §4. If they change, this changes too, for example: "Write for your later self: short sentences, honestly. Never rewrite an earlier entry."

`delivery/container/README.md`

**FINDING-1767.** Writing, rule 9; resting on the reader; missed at a change (WG-3). `delivery/container/README.md`, the opening paragraph, line 7: "adversity proves the wall. The problem is not yet chosen. It arrives". The sentence before it names the Structural Wall. This clause then calls it "the wall", a short form of the Name. The method and the concept write a bare "the wall" in prose nowhere else. The 5 bare uses in `delivery/method/` and `concept/` are field labels in an Output Shape. Why: missed at a change. `b451eb9` rewrote this paragraph and gave the first "wall" its Name. The second was left. The round 3 close read at `f5dfbbe` came after `b451eb9` and did not list it. Proposed: fix: "adversity proves the Structural Wall."

**FINDING-1768.** Writing, rule 3; resting on the reader; older than the rule (WG-8). `delivery/container/README.md`, the closing header comment, line 29: "outside. What changes weekly is PLAN.md's; why is the ADRs'; how". Three homes are chained with semicolons: "What changes weekly is PLAN.md's; why is the ADRs'; how it went is the devlog's." Why: missed at a change. The line is older than the rule (`dc3b7db`). `b451eb9` split the chained sentence right after it ("Chained comments split") and left this one. Proposed: fix: "What changes weekly is PLAN.md's. Why is the ADRs'. How it went is the devlog's."

`delivery/fills/cbc-run-pure-playbook.md`

**FINDING-1769.** Writing, rule 9; checked; missed at a change (WG-1). `delivery/fills/cbc-run-pure-playbook.md`, *The Plan Step Form*, the close item on stale words, line 99: "No living line in a record the Plan Step touched, or one that". "living line" means a line of Living Text, written in lowercase. Our `PLAN.md` holds the same item, and it now reads "No line of Living Text in a record the Plan Step touched" (lines 91, and the other Plan Steps' copies). Why: missed at a change. `bcf3010` (DECISION-35's work) fixed the twin line in our `PLAN.md` but not the playbook it was copied from. `a456f4c` then edited the playbook and left the line. The Foundation Check at `bcf3010` should have caught the twin. The script's lowercase sweep looks for "living text", so it never finds "living line". Proposed: fix: "No line of Living Text in a record the Plan Step touched, or one that", as our `PLAN.md` reads.

`delivery/installs/pure-seed.md`

**FINDING-1770.** Writing, rule 9; resting on the reader; missed at a change (WG-4). `delivery/installs/pure-seed.md`, step 4, the seed commits' subjects, lines 159 and 170: "git commit -m "chore: seed — method and stack skills, shapes, pin @ $deliverer_pin". The subjects write Agent Skills as "skills", Output Shapes as "shapes", and Plan Steps as "steps". Line 170 reads `git commit -m "chore: seed — steps into PLAN, cbc-run-pure $playbook_version @ $deliverer_pin"`. Every Newborn CBC Run reads these subjects, because the prompt tells it to read "every seed commit". Step 6's prompt (lines 215–216) and the checklist (lines 290–292) already write the Names. Our own commit subjects use the Names too, for example `fix(delivery): the cbc-slice Agent Skill meets the rule again`. Why: missed at a change. `5d562d8` edited both lines to rename the variable and left the words. The lines sit inside a code block, so a reader may have taken them for code. Proposed: fix: "chore: seed — method and stack Agent Skills, Output Shapes, pin @ $deliverer_pin" and "chore: seed — Plan Steps into PLAN, cbc-run-pure $playbook_version @ $deliverer_pin". The line 131 subject waits on the leftover G3.

`delivery/method/.claude/shapes/evidence-test.md`

**FINDING-1771.** Writing; resting on the reader, quote checked (left Java label). line 91: The assertion label "the promise: %s" names the Falsifiable Promise by a lowercase short form, in code a CBC Run copies. Proposed: question: DECISION-37 keeps Names out of code identifiers; a string label is neither identifier nor prose. Fix it to "the Falsifiable Promise: %s", or let DECISION-37 reach it.

`delivery/method/.claude/shapes/slice-record.md`

**FINDING-1772.** Writing, rule 9; resting on the reader; older than the rule (WH-11). `delivery/method/.claude/shapes/slice-record.md`, *Rules for the parts*, line 201: "- **Blocks are separated by a `---` line.**". "Blocks" is Invariant Slice Guarantee Block cut to its last word. Everywhere else in the file the Name is written whole. Why: the line (`d3ebdff`, 2026-10-29) is older than the Name (DECISION-19's method table, row 48, 2026-10-31). `8a4525b` and `6e1d55e` then worked this Output Shape for the Name and missed this line. Proposed: fix: `- **Invariant Slice Guarantee Blocks are separated by a `---` line.**`.

`delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md`

**FINDING-1773.** Writing, rule 9; resting on the reader; missed at a change (WH-5). `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, *The order, and why it differs from the presentation*, line 51: "Census comes after, and makes the sketches exact.". "the sketches" is the Enemy Sketches of the line before, cut to one lowercase word. In English a sketch is a drawing. The meaning here is the method's. Why: it was missed at a change. `3be745a` rewrote the line from "rough enemy *sketches*" and gave the Name only its first use. Proposed: fix: `Census comes after, and makes the Enemy Sketches exact.`.

**FINDING-1774.** Writing, rule 9; resting on the reader; missed at a change (WH-6). `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, Stage 2, *What the exit leaves behind*, line 300: "- **The Scope Exclusions.** Every exclusion as a numbered line:". "every exclusion" is every Scope Exclusion, written in lowercase in the item that opens with the Name. The next sentences say "A Scope Exclusion". Why: it was missed at a change. `3be745a` rewrote "Every written-out scope exclusion" and dropped the qualifier without putting in the Name. Proposed: fix: `- **The Scope Exclusions.** Every Scope Exclusion as a numbered line:`.

`delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`

**FINDING-1775.** Writing, rule 2; resting on the reader; missed at a change (WH-2). `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, the opening, lines 14 to 16: "System Never-Event, a thing that must never happen, with a Structural Wall, a structure that makes it impossible, proven by a test that". One sentence of 31 words holds three ideas. It answers each System Never-Event with a Structural Wall, glosses both Names inside the sentence, and adds the proving test. The reader has to hold all of it before the sentence makes sense. Why: it was missed at a change. `60398b1` added the two glosses into one existing sentence to meet DECISION-39, and the rule 2 check at that commit did not catch it. Proposed: fix: "It answers each System Never-Event, a thing that must never happen, with a Structural Wall. A Structural Wall is a structure that makes the System Never-Event impossible. A test that creates the attack proves the Structural Wall holds."

**FINDING-1776.** Writing, rule 8; checked; missed at a change (WH-1). `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *Working one Invariant Slice*, line 85: "- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees, the proof,". This is the first and only use of Invariant Slice Guarantee on the page, and no plain words stand beside it. Every other Name on the page has its plain words. Why: it was missed at a change. `60398b1` is the commit that made DECISION-39's fix on this page. The Foundation Check at that commit read only the glossary's words. Proposed: fix: `- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees (the properties the invariant needs, found by attacking it), the proof,`.

**FINDING-1777.** Writing, rule 5; resting on the reader; missed at a change (WH-3). `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *How it fails (watch for these)*, line 107: "path, and the System Guarantee quietly becomes fiction.". "becomes fiction" is a figure for "stops being true". The method's glossary entry for Escape Hatch already says it plainly: "a System Guarantee stops being true" (`delivery/method/docs/glossary/method.md`, line 25). This is not one of the figures DECISION-26 kept. Why: it was missed at a change. `8316ce0` ("cbc-framing's references meet the rule") rewrote this line and kept the figure from the old text. That commit's rule 5 check missed it. Proposed: fix: `path, and the System Guarantee quietly stops being true.`.

`delivery/method/.claude/skills/cbc-framing/references/worked-example.md`

**FINDING-1778.** Writing, rule 6; resting on the reader; missed at a change (WH-9). both copies of the worked example, Stage 2, line 94: "3. Enemy Census Probe 3, quantities at huge (a key reused thousands". Enemy Census Probes 1 and 2 name their Enemy Census Probe Lens by its label. Enemy Census Probe 3 names a move, "quantities at huge", not its lens, "the resource lens" (`cbc-framing-workflow.md` line 265). A reader who maps each probe to a lens finds no label to match. Rule 8 is touched too. Why: it was missed at a change. `8316ce0` wrote the three probes with the labels and left the third without its label. Proposed: fix, in both copies: `3. Enemy Census Probe 3, the resource lens, quantities at huge (a key reused thousands`.

**FINDING-1779.** Writing, rule 9; resting on the reader; missed at a change (WH-8). both copies of the worked example, `delivery/method/.claude/skills/cbc-framing/references/worked-example.md` and `delivery/method/.claude/skills/cbc-slice/references/worked-example.md`, Stage 2, line 97: "Two Enemy Census Probes in a row found nothing new: saturated.". "saturated" stands for Enemy Census Saturation. The line itself gives the method's meaning: two Enemy Census Probes in a row find nothing new. English "saturated" does not mean that. It is the only lowercase form of the word in `delivery/` (checked by grep). Why: it was missed at a change. `8316ce0` wrote the Name "Enemy Census Saturation:" eight lines above, at line 89, and kept "saturated" from `8257301`. Proposed: fix, in both copies: `Two Enemy Census Probes in a row found nothing new: Enemy Census Saturation.`.

**FINDING-1780.** Writing, rule 9; resting on the reader; missed at a change (WH-10). both copies of the worked example, Stage 6, line 228. This is a script hit: "**Invariant Slice Registry:** SLICE-1 `chosen-next`. SLICE-2". The bold span is the Name alone, in a paragraph, not a list item. The Name's home is `docs/concept/03-cbc-framing.md`, so this is a bold Name away from its home. Lines 236, 239 and 249 are numbered list items, so their leads stand under ADR-0079. Line 223, the paragraph above, labels "CBC Framing Reconciliation:" with no bold. Why: it was missed at a change. `8316ce0` wrote the line when DECISION-22 already allowed bold only at a Name's home. Proposed: fix, in both copies: drop the bold, `Invariant Slice Registry: SLICE-1 `chosen-next`. SLICE-2`, as line 223 has it.

`delivery/method/.claude/skills/cbc-framing/SKILL.md`

**FINDING-1781.** Writing, rule 9; uncertain; the rule unclear (WH-12). `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*, the Delegated-Verdict Mode paragraph, lines 48 to 50: "derivation becomes the only review, so its legibility is part of the". "the written derivation" may mean the CBC Framing Derivation, the document Delegated-Verdict Mode leaves as the only review. It may also mean the reasoning as written, the English sense. The Agent Skill uses "derivation" in both senses: "Present your derivation" at line 37, and "derivation order" at line 208. Why: the rule is unclear on a word with both an English sense and a Name. `4884a129` rewrote the line. Proposed: question: is "the written derivation" the CBC Framing Derivation? If it is, fix it to "the CBC Framing Derivation becomes the only review". The same question reaches `delivery/method/.claude/skills/cbc-framing/templates/registry.md` lines 112 and 114, "(derivation wins, recorded)" and "the derivation overrode it". There it seems to mean what CBC Framing derived.

`delivery/method/.claude/skills/cbc-framing/templates/registry.md`

**FINDING-1782.** Writing, rule 9; resting on the reader; older than the rule (WH-7). `delivery/method/.claude/skills/cbc-framing/templates/registry.md`, *CBC Framing Reconciliation*, lines 97 and 101 to 102: "| <…every kill, one row> | | |". The guidance says "every kill". Line 101's example line, "no deferrals; no kill dropped", is text that a CBC Run copies into its own Invariant Slice Registry. Both write Enemy Collision Kill as the lowercase word "kill". The column header "Kill" and the field "Kills covered" are labels inside their owner, so they stand. Why: the lines are older than the rule (`bb51b61`, the starter bundle). Then `8316ce0` and `ce370e4` worked this Agent Skill Template under the rule and missed them. Proposed: fix: line 97 becomes `| <…every Enemy Collision Kill, one row> | | |`. In line 101, "no kill dropped" becomes "no Enemy Collision Kill dropped".

`delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`

**FINDING-1783.** Writing; resting on the reader, quote checked (left H12). line 213: "judgement" against "judgment" everywhere else ("Judgment logged"). Proposed: fix: "judgment".

`delivery/method/docs/glossary/method.md`

**FINDING-1784.** Writing, rule 9; checked; missed at a change (WH-4). `delivery/method/docs/glossary/method.md`, *The method's*, the CBC Framing Derivation entry, line 167: "how each stage of CBC Framing ran, kept for good". "stage" here is the cbc-framing Agent Skill's Agent Skill Stage, written in lowercase. It is the only lowercase "stage" left in the Method Group (checked by grep). Why: it was missed at a change, twice. `c9f6b56` wrote the entry. Then `60398b1` fixed the same word in the Agent Language entry ("stage" became "Skill Stage", FINDING-1335) and left this one. Proposed: fix: `how each Agent Skill Stage of CBC Framing ran, kept for good`.

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`

**FINDING-1785.** Writing, rule 5; resting on the reader; older than the rule (WI-10). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The Stack Default*, line 53; also lines 27-28 "structural depth earned per feature" and line 57 "own complexity earns it": "- **Depth is earned per feature, never stamped.** A feature starts". "earned" and "stamped" say, by figure, that classes are added when a feature needs them and not laid out from a template. FINDING-1409 counted "and it earned that", in this file's line 120, as a figure, and it was dropped. "Stamp" is also the base of a method Name, the Enemy Census Probe Stamp. DECISION-26 judged neither word. Why: older text (`6385564`). FINDING-1409 named a fourth use and not these three. Proposed: question: are "earned" and "stamped" dead figures here? If not: "- **Depth grows per feature, by need, never from a template.**"; lines 27-28 "structural depth added per feature, by need"; line 57 "when that feature's own complexity needs it".

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`

**FINDING-1786.** Writing, rule 8, 6; resting on the reader; missed at a change (WI-6). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *The Adversity Harness in the codebase*, line 172: " would undo step 3's claim. On Boot 4 the engine enters, not Boot's". "step 3" meant this walkthrough's §3, *Wire the runtime datasource*, as it did when the line was first written (`4566cb6`). Now a numbered list ends one line above it, and its item 3 is "run migrations on the Adversity Harness's side". A reader takes "step 3" as that item. The harness reference says the same fact plainly: "it would undo the datasource's claim that the application cannot migrate" (`spring-harness-reference.md` line 155). Why: missed at a change. `a6ccf5b` turned the capabilities into a numbered list under rule 3, and left "step 3" beside its new item 3. Proposed: fix: "would undo step 3's claim, *Wire the runtime datasource*: the application cannot migrate." Or, as the harness reference writes it: "would undo the datasource's claim that the application cannot migrate."

**FINDING-1787.** Writing; resting on the reader, quote checked (left I8). line 263: "honours", while `establishment-walk.md` 13 spells "honor" and the stack's files spell "behavior". Proposed: fix: "honors".

**FINDING-1788.** Writing, rule 3; resting on the reader; missed at a change (WI-7). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *Recall list — the traps compressed*, lines 307-308, 315, 317 and 319: "6. Ryuk stays on under rootless podman on 2.x; `ryuk.disabled` in the". Four items still chain two facts with a semicolon: - item 2: the restclient trap; the `@AutoConfigureTestRestTemplate` trap; - item 6: Ryuk stays on; the old key has no effect; - item 7: no dummy baseline; the history table exists anyway; - item 8: Flyway is the Adversity Harness's only; at runtime scope it undoes the constraint. Why: missed at a change. FINDING-1405 asked for one fact per sentence in this list, named items 2 and 6 among others, and was taken as proposed. `63bb1db` took out the dashes and left the semicolons in items 2 and 6. Items 7 and 8 were not named. Proposed: fix: a full stop at each: "`RestTemplateBuilder`. `@AutoConfigureTestRestTemplate` is required:"; "Ryuk stays on under rootless podman on 2.x. `ryuk.disabled` in the properties file has no effect."; "No dummy baseline migration. The history table is created by a run with no migrations."; "Flyway is the Adversity Harness's only. At runtime scope it undoes the Runtime Ground's constraint."

`delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`

**FINDING-1789.** Writing, rule 9; resting on the reader; older than the rule (WI-5). `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 2 — write the CBC Bootstrap Requirements*, line 153: "- §3 the constraints, each **by reference** to the ADR or contract". "contract" here is the Infrastructure Contract: Stage 1, line 118, says the constraints are "cited against the Infrastructure Contract". The same Agent Skill also uses "the contract" in its English sense, at line 43, for the CBC Bootstrap Requirements. So the reader must decide at each use which one is meant, which is what rule 9 prevents. Why: older text. `c449de0` (round 3's work) reworded the line and kept the word. Round 3's read and its close read did not list it. Proposed: fix: "- §3 the constraints, each **by reference** to the ADR or the Infrastructure Contract"

`delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`

**FINDING-1790.** Writing, rule 8, 9; resting on the reader; missed at a change (WI-4). `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, *Inputs, before Stage 0*, line 20: "is not settled, the step is not ready: stop (Stage 0 in `.claude/skills/infra-establish/SKILL.md`).". "the step" names nothing this file has introduced. The file speaks of Agent Skill Stages and Infrastructure Establishment. In a CBC Run, "step" also reads as the Plan Step that runs this work, a Name written short. Why: missed at a change. `580f7dc` (round 3's work) wrote the line, and round 3's close read did not list it. Proposed: fix: "is not settled, Infrastructure Establishment is not ready: stop (Stage 0 in `.claude/skills/infra-establish/SKILL.md`)."

**FINDING-1791.** Writing, rule 9, 10; resting on the reader; missed at a change (WI-3). `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, the Stage 3 heading, line 93: "## Stage 3 — Name each Infrastructure Service's constraints, the reference first". "each Infrastructure Service's constraints" splits the Name Infrastructure Service Constraint into a possessive and a lowercase word. The section's own first line writes the Name whole. Why: missed at a change. FINDING-1379 wrote the Name whole at the walk's other uses (lines 106, 116, 121), "the same at each line"; `1f13fee` did not reach the heading. No Fact Reference names this heading (grep), so the rename grep has nothing to fix. Proposed: fix: "## Stage 3 — Name the Infrastructure Service Constraints, the reference first"

`delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`

**FINDING-1792.** Writing, rule 9; resting on the reader; missed at a change (WI-2). `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *The Agent Skill Stages and their Gates*, line 76 (drawing), with the key at lines 68-71: " stood up) exclusions) enforcement) recorded)". The box for Stage 2 says "exclusions", the short form of Infrastructure Service Exclusion. The key above the drawing names environment, services, constraints and contract, and not exclusions. Why: missed at a change. `1f13fee` added the key for FINDING-1410, and that finding named only four of the drawing's short words. Proposed: fix: the key reads "In the drawing, environment is the Execution Environment, services the Infrastructure Services, exclusions the Infrastructure Service Exclusions, constraints the Infrastructure Service Constraints, and contract the Infrastructure Contract and the Operator Manual."

`delivery/spring-postgres/.claude/skills/infra-establish/templates/bootstrap.sql`

**FINDING-1793.** Writing, rule 3; resting on the reader; missed at a change (WI-8). template comments in the Stack Group, 7 lines in 5 files: - `infra-establish/templates/bootstrap.sql` lines 30 and 67; - `infra-establish/templates/compose.yaml` line 42; - `infra-establish/templates/flyway.conf` line 5; - `infra-establish/templates/verify-database-model.sql` lines 18 and 85; - `cbc-bootstrap/templates/readme-run-test.md` line 40, a comment in the bash block that lands in a CBC Run's README: "-- Identities, schema, and privilege boundaries only — no tables, no". Each line joins its parts with a dash, and bootstrap.sql 30-31 and readme-run-test.md 40 add a semicolon. FINDING-1406 named the other dashes in these templates, and those are fixed; these 7 were never named. Why: missed by round 3's close read: FINDING-1406's "also" list left these 7 out, and `1f13fee` fixed what it listed. Proposed: fix, a colon or a full stop at each: - bootstrap.sql 30-31: "Identities, schema, and privilege boundaries only. No tables, no application objects: those arrive solely through the migration tool."; - bootstrap.sql 67-69: "search_path: where unqualified names resolve. It is pinned so migrations and application statements land in the governed schema, never in public. It is a default for convenience. The authority boundary is the grants above."; - compose.yaml 42: "# bare name: compose prefixes the pinned project name"; - flyway.conf 5: "# Flyway: the only DDL path, per the CBC Run's Infrastructure Service Constraints."; - verify-database-model.sql 18: "Expected results are comments beside each query, so this file needs no other document open."; - verify-database-model.sql 85: "empty-string role, oid 0) f: bootstrap.sql's REVOKE CONNECT, checked"; - readme-run-test.md 40-42: "# the one standard test command: unit and integration tests together. Integration tests drive a real throwaway PostgreSQL (Testcontainers, rootless podman), so the Runtime Ground does not need to be up".

**FINDING-1794.** Writing, rule 2, 7; resting on the reader; missed at a change (WI-9). `delivery/spring-postgres/.claude/skills/infra-establish/templates/bootstrap.sql`, the comment above `CREATE ROLE`, lines 33-35: "-- cluster, the Database Role Split named above (roles are cluster-wide).". One sentence chains a path, a section title with no mark, a gloss and a parenthesis: "Prefixed names are the shared-cluster case of postgres-role-split.md, Naming across a cluster, the Database Role Split named above (roles are cluster-wide)." "Named above" first pointed back at "the model", the reference named in *Purpose*. Now the line just before names the Database Role Split, so the gloss repeats it. Why: missed at a change. `1f13fee` replaced "the model" by the Name in place (FINDING-1373), and the sentence's shape stayed. Proposed: fix: "-- the two identities of the Database Role Split. Prefixed names are the shared-cluster case, since roles are cluster-wide (postgres-role-split.md, Naming across a cluster)."

`delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`

**FINDING-1795.** Writing, rule 9; resting on the reader; missed at a change (WI-1). `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`, *Stage 0 — the Runtime Ground stands?*, lines 31-32: "Check the original evaluation. If the wanted service is **an". "**an Infrastructure Service Exclusion,**" is bold inside a sentence. It is not a list lead. The Name's home is `infra-establish/SKILL.md` (`docs/glossary/stack.md` line 52), not this file. Why: missed at a change. `78fe685` turned "**on the not-provisioned list**" into the bolded Name, after DECISION-22 had been taken. FINDING-1384 then listed the bold Names away from their homes, and did not list this one. Proposed: fix: "Check the original evaluation. If the wanted service is an Infrastructure Service Exclusion, the new need must answer the old" (bold dropped; line 32's "Infrastructure Service Exclusion,**" loses its closing marks).

### Decisions

Twelve decisions, DECISION-41 to DECISION-52, for what recurs or what needs the reviewer's choice; then the agent's calls on the single questions; then three left to the reviewer alone. The reviewer took the twelve and the calls as recommended, 2026-11-01. Every other finding's ending is its proposal. Where a fix proposal holds an "or", its first option is taken.

**DECISION-41.** Shipped text that points home, after DECISION-40. Rests: FINDING-1447. DECISION-40 changed 11 shipped lines from "CBC docs/…" to "the Concept Deliverer's docs/…". Facts-in-sync §3.1 still says such a line "leads with CBC", and the container's one-home Agent Rule still writes "CBC docs/" across lines 12–13.
- (a) §3.1 says a shipped reference to our text opens with "the Concept Deliverer's"; the container's line follows.
- (b) The 11 lines take "CBC" back, and the container's glossary gains the Repo Tag.
- Recommended: (a). It is what DECISION-40 chose, and nothing in a CBC Run says what "CBC" is.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-42.** Fact References in our copies of shipped Agent Skills. Rests: FINDING-1633, 1635, 1640. Our commit-messages, commit-plan and visual-comparison Agent Skills retell their manuals with no Fact Reference. Each is held identical to the container's copy, but for the seat (ADR-0069). A shipped file may carry a reference to our text: it serves our Change Walk alone, and the line says what the CBC Run needs without it (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- (a) Both copies gain the references, one per section where one covers it (ADR-0072), in the shipped copy in DECISION-41's form.
- (b) Ours alone gains them, and the pair differs by more hunks.
- (c) Facts-in-sync §4 step 2 says a copy held identical to a shipped one keeps the shipped seat's rule: it stands alone, and its Foundation Line names the manual the Change Walk opens.
- Recommended: (a). It is what §3.1 already allows, and (c) would add an exception to avoid it. A reference names the section, where a Foundation Line names only the manual. The container's commit-plan then gains the reference at line 149 that ours has, and one hunk between the copies goes. The agent first recommended (c), reading "a shipped line stands alone" as "it carries no reference"; the reviewer's question found it.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-43.** References into and between the concept chapters. Rests: FINDING-1665, 1594. The method's Agent Skills use parts of the concept and never say which. The chapters name each other by title, with no Fact Reference.
- (a) Both gain references: the method's texts one per section that uses a chapter part, the chapters one per line that leans on another chapter.
- (b) Neither: the concept is copied whole, and the method's Foundation Line, `concept v1`, names it.
- (c) The method's texts gain them, in "Rewrite the method's texts plain", and its first one fires "Number the concept chapters' sections"; the chapters, one Canonical Description copied whole, need none between themselves.
- Recommended: (c). A change to a chapter must find the method lines that use it. Inside one Canonical Description, a title is enough.
- Chosen: (c), by the reviewer, 2026-11-01, as recommended.

**DECISION-44.** Counts of CBC Runs in the stack's text. Rests: FINDING-1693, 1687, 1684, 1679, 1698, 1578; beside them the Lessons findings that tell a case as a story, FINDING-1673, 1675, 1676, 1680, 1681, 1683, 1685, 1686, 1688, 1689, 1692, 1697, 1700. DECISION-40 kept a shipped workflow's count, since the CBC Run reads it as why the line is required. The stack's references give counts too: "Both CBC Runs that ran this Agent Skill", "Three projects built them", "A hundred is what the CBC Runs used".
- (a) DECISION-40 reaches a count that says how proven a line is. Each stays, made true and told once; the two that differ (1578) are explained. A case told as a story, "one CBC Run did this", goes, as the Lessons findings propose.
- (b) The counts go too. The one general line in `infra-establish/SKILL.md` stands for all.
- Recommended: (a). It holds DECISION-40's reason, and a number says how proven a default is, which rule 4 asks.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-45.** Where a bold-led bullet is a part. Rests: FINDING-1636, 1643, 1627, 1682, 1605; and FINDING-1601, 1606, 1611, 1616, 1648, 1669, which propose numbering such bullets. Facts-in-sync §3.2: a bold-led bullet is a part when it holds a paragraph of its own. Readers ask whether that reaches an Agent Skill's rules, an Approach on Trial's list, a manual's rule list, and the labels a form repeats in every section.
- (a) It reaches the manuals, the Idea Models and `delivery/README.md`, where a part is pointed at. A rule in an Agent Skill, an Agent Rule, an Approach on Trial, a reference or a manual's rule list stays a bullet, however long. A label repeated in every section of one form is that form's fixed label. A part that a Fact Reference points at is numbered, in any file. §3.2 gains these lines.
- (b) It reaches every file: each such bullet is numbered.
- Recommended: (a). The numbers are for pointing, so what is pointed at is numbered and a rule that is only acted on stays a bullet. Under (a), FINDING-1601, 1606, 1611, 1616 and 1669 are numbered as proposed, and 1648, in an Agent Skill, stays. FINDING-1645 and 1647 still stand: each is one section that holds two subjects or three, and is fixed as its reader recommends. FINDING-1645's small commits, which three Fact References point at, take a number by the new line.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-46.** A Name in a paragraph's bold lead. Rests: FINDING-1710, 1720, 1780. ADR-0079 lets a list item's bold lead begin with a Name. Concept chapters 00 and 03, the exchange manual and the worked example bold a Name as a paragraph's lead.
- (a) A paragraph's bold lead counts as a list item's: the rule's line says "a bold lead", and the leads stand. A bold Name inside running prose still goes.
- (b) Only a list item's lead. The paragraphs become list items, or lose the bold.
- Recommended: (a). The bold marks the paragraph, as it marks a list item. Under (a), FINDING-1720's line 116, a second bold at the Name's own home, still loses its bold.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-47.** A Name's home in the CBC Run's seat. Rests: FINDING-1758, 1765, 1650. In a CBC Run, the container's glossary points Change Set at the commit-plan Agent Skill and Delivery Pin at delivered-copies rule 1. Those lines bold the Name. Ours do not, because our glossary points at the manuals.
- (a) The CBC Run's home is the file its glossary points at. The bold stays there, a seat difference ADR-0069 allows, and delivered-copies rule 1's items open with the Name. The container's glossary entries point at their homes and stop defining (FINDING-1650).
- (b) The container's copies follow ours, and the bold goes.
- Recommended: (a). Writing rule 9 bolds the defining line, and in a CBC Run that line is the shipped file.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-48.** Trials whose moment has passed. Rests: FINDING-1425, 1451, 1431, 1513. The retrospective trial was set for "the next CBC Run Birth", which has come twice. The Conversation Memory trial was set for its third item, and has had at least three. The auto-run Approach on Trial rejects a way because "one full-auto CBC Run has been lived"; three have.
- (a) Each manual line names the TODO item that holds the trial's trigger, and the trigger is set there, at the reviewer's word. A rejection's reason says when it was weighed.
- (b) Each trial is judged now.
- Recommended: (a). A trigger kept in one place does not go stale in two. Judging a trial is work of its own.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-49.** TODO items whose trigger has passed. Rests: FINDING-1491, 1495, 1507, 1509, 1510, 1511; beside them 1490 and 1493, already fixes. About 14 items wait on CBC Run 5's reading, CBC Run 5's birth close, "the next birth" or Refinement Round 2, and each of these has happened.
- (a) The agent drafts each item's ending, worked, re-aimed with a new trigger, or closed, and the reviewer decides each in one pass. They land in round 1's layer 4.
- (b) Each trigger is re-aimed only, and the items wait for work of their own.
- Recommended: (a). A fired trigger is an item due now. Re-aiming it hides that.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-50.** The method's findings, and "Rewrite the method's texts plain". Rests: FINDING-1501, 1502, 1666, 1559; and the Lessons and Layout findings in layer 6's method and stack. The TODO item's trigger, the refinement's close, is due. It still lists FINDING-206, 223, 224, 227 and 228; the tree shows 223, 224, 227 and 228 not worked, and 206 gone (SL2-15).
- (a) This read's findings are fixed in the refinement, in their Refinement Rounds. The item then keeps only what is left, its Context rewritten from the tree, and round 3's Endings line is corrected.
- (b) The method's and the stack's findings move to the item, and the refinement closes without them.
- Recommended: (a). The refinement is the work the item asked for. Moving the findings would need a second read of the same files.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-51.** A count in Living Text. Rests: FINDING-1424, 1427, 1428, 1457, 1508, 1593. "Four CBC Runs kept their records", "a median of 102 lines", "985 lines in 83 files", "about 1,350 commits since v1": each was true when taken, and nothing updates it. `ARCHITECTURE.md` "keeps to about two pages": ADR-0068 set that at about 1,200 words, and it holds 2,053.
- (a) A count carries the date it was taken, and stays as taken. A measure that is a target says so: "aims at about two pages".
- (b) Each count is brought up to date, and a check at each change keeps it so.
- Recommended: (a). A dated count stays true, and no check exists to keep (b).
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-52.** A collision where nothing dies. Rests: FINDING-1550, 1552. The kill Output Shape gives a tried Enemy Collision that breaks nothing a `KILL-<n>` tag. In the concept and the glossary, an Enemy Collision Kill is what dies. Known, and deferred to the plain rewrite.
- (a) The Output Shape changes: such a collision is listed as tried, under its own tag. The worked example, the workflow and the registry template follow.
- (b) The concept and the glossary widen the Kill to every tried collision.
- Recommended: (a). The concept holds, and the change stays in the method.
- Chosen: (a), by the reviewer, 2026-11-01, as recommended.

**DECISION-53.** One commit plan for each Refinement Round. Rests: the work of all 385 findings. `.claude/approaches-on-trial/refinement.md` §2.7 asks for a commit plan for each Refinement Layer. Every one of the 18 pairs of Refinement Round and Refinement Layer has findings, from 2 to 62, so that is 18 plans and 36 commits that only open and close them.
- (a) One plan for each Refinement Layer, as §2.7 asks.
- (b) One plan for each Refinement Round, its layers in order inside it, each layer's commits split when the layer opens and its endings committed at its end.
- Recommended: (b). The order, sources before what derives from them, and the stop at every commit both stay; 6 commits open and close plans, not 36. Asked by the reviewer, 2026-11-01, after round 1's layer 1 plan was opened (`f92d6b7`).
- Chosen: (b), by the reviewer, 2026-11-01. A departure from §2.7, carried as a lesson for the Approach on Trial at the refinement's close.

**DECISION-54.** The Change Set written from the list. Rests: the work of all 385 findings; it replaces DECISION-53. Under DECISION-53, round 1's plan still went layer by layer, and rounds 2 and 3 after it. 88 files have findings, 61 of them in more than one Refinement Round, so most would be edited two or three times. Only 25 pairs of findings from different Refinement Rounds sit within 4 lines of each other. About 15 facts are shared across files; a Refinement Layer fixes such a fact at its home and its followers layers later, and the repo disagrees with itself between.
- (a) DECISION-53: one plan for each Refinement Round, its Refinement Layers in order.
- (b) One Change Set for all 385, written from the list. The list keeps its order by Refinement Round and Refinement Layer, the order that shows the chains to decide on. The plan takes the list as its input: first each shared fact, its home and all its followers in one commit; then each file once, all its findings in one edit, the 25 close pairs fixed in Refinement Round order inside it. Each commit names its findings; *The work* is written once, from `git log`, at the end.
- Recommended: (b). The repo never disagrees with itself between commits, and no file is opened twice. Commits drop from about 70 to about 33.
- Chosen: (b), by the reviewer, 2026-11-01. The lesson for `.claude/approaches-on-trial/refinement.md` §2.7 at the refinement's close, the reviewer's: Refinement Rounds and Refinement Layers order the read and the list; the Change Set is written from the list, grouped by what each change needs. Where Refinement Rounds order the reads, as in a first refinement, each round's fixes still land before the next round reads, and inside a round the Refinement Layers are the plan's input, not its structure.

The agent's calls, on the single questions, each a fix unless said:
- FINDING-1416: the third kind takes the Idea Model's word, Output Forms, as ADR-0078 decision 1 did; an Agent Skill Template travels inside its Agent Skill.
- FINDING-1429: the example names a gate item that exists.
- FINDING-1432: the line takes the channel the Agent Model's §8 table gives a rule read inside a record, checked at the fix.
- FINDING-1442: `COMMIT-PLAN.md` is listed in project-recording §1 for its moment, and is the agent's file, not a project record; §1 says so.
- FINDING-1452: the line says the name came first and the question is its subject.
- FINDING-1456: rule 6 as proposed, in the manual and both Agent Rules.
- FINDING-1458, 1542: the CBC Run Birth entry widens to the event, as DECISION-36 reads it.
- FINDING-1462: M2 takes the grade the Agent Model defines for a definitional claim, checked at the fix; line 275 stands.
- FINDING-1463: §8's table decides; §9 and A1 follow it.
- FINDING-1465: the difference is an adaptation, said in agent-arrangement §3.7 with a Fact Reference to the model.
- FINDING-1477: facts-in-sync §4 step 1 gains the line that `ARCHITECTURE.md` §2 keeps the concept's list.
- FINDING-1482: the goal is rewritten now, as proposed.
- FINDING-1488: the Conversation Memory's header allows "Item: none".
- FINDING-1514: declined. `CLAUDE.local.md` is the reviewer's own file, and the agent changes it only on their word.
- FINDING-1517: facts-in-sync §3.4 names the Output Shape.
- FINDING-1525: conventions §1.4 says a first stage is Stage 0 only when it checks readiness; the headings take §1.4's case.
- FINDING-1530: delivered-copies rule 5 gains the optional Receipt Branch step, and the container's glossary the entry.
- FINDING-1531, 1534: as recommended; for 1534, "with a dated line" goes.
- FINDING-1535: the manual's rule 10 names a record's fixed headings for the CBC Run's seat.
- FINDING-1537: agent-arrangement §3.4 names the "rules in force now" list as the one part of the log not appended, and the Record Stub's header says so.
- FINDING-1538: the line follows the playbook and the Pure Seed: the Concept Deliverer writes each lesson into the playbook the next CBC Run is born with.
- FINDING-1539: one wording with left G3 and left B3, in one commit.
- FINDING-1553: §3.1 says a numbered rule is cited by its number and its lead, cut at 30 characters with "…", as a title is; the 15 follow, and the 2 without a lead gain one.
- FINDING-1562: yes, as the Agent Skill says; all four places name the three kinds.
- FINDING-1572: follows FINDING-1587's fix.
- FINDING-1574, 1577: as proposed; for 1577, the stack evaluation's first option, so the concept holds.
- FINDING-1576: the playbook's Plan Step order carries the sign-off, and the cbc-bootstrap Agent Skill's close points at it.
- FINDING-1579, 1585: a footer names a file by its root path, as every Fact Reference does.
- FINDING-1590: relying; the Fact Reference to the Idea-to-Output Model §4.2.
- FINDING-1595: §3 is retitled to cover the operator's file, with the rename grep, and §1.1's list names `CLAUDE.local.md`.
- FINDING-1602: the case goes; the story line already points at ADR-0034.
- FINDING-1617: (a), the Idea Model's line is general.
- FINDING-1618: (a), §3.5 keeps the definition.
- FINDING-1621, 1622: the archive's fact gets its home in `ARCHITECTURE.md` §1.1, and the README and the table point there.
- FINDING-1623: the Conversation Memory's header is the home; TODO's line gains the Fact Reference.
- FINDING-1642, 1659, 1661, 1672, 1701: as their readers recommend.
- FINDING-1725: (b), plain words at shapes line 13; no new Name.
- FINDING-1733: the kind word, "the commit-plan Agent Skill".
- FINDING-1739: "walk" stands, a trial's label; "master text" becomes "text to copy".
- FINDING-1740, 1748: plain words, as recommended.
- FINDING-1746: plain words, and the milestone named as proposed.
- FINDING-1755, 1763: the kind word, by DECISION-27, with left E13.
- FINDING-1766: the line changes, with FINDING-1705 and 1731, by ADR-0079's doubt 8.
- FINDING-1771: stands, by DECISION-37: a string in code is code.
- FINDING-1781: line 48 is the CBC Framing Derivation, and is fixed; the template's two lines mean what CBC Framing derived, and stand.
- FINDING-1785: fixed as proposed; the figures are not dead.

Left to the reviewer alone, with no call:
- **FINDING-1433:** the gap line in concept chapter 00, four gaps against five practices. A fix that is not editorial is a concept change.
- **FINDING-1444:** what a held edit becomes at a Delivery Take. It is how the exchange works, not how its text reads.
- **FINDING-1487:** `temp/run-6-handoff/`, tracked and named by no TODO item or Plan Step: an item names it, or it goes.

Decided by the reviewer, 2026-11-01, during the work:
- **FINDING-1444:** a held edit is re-applied on top at a Delivery Take, as an unanswered one is, and stands until a later Delivery Note answers it.
- **FINDING-1433:** (a), with the agent's wording: chapter 00 gains the fifth gap, design-before-code puts the flaw in a document but does not say what the document must hold; a CHANGELOG [Unreleased] entry.
- **FINDING-1432:** (c), the line names both channels: the Record Stub arrives by the Installed Channel, and its rule is read by the Pulled Channel.
- **FINDING-1431,** met at commit 7 with no TODO item to point at: a TODO item, "Judge the Conversation Memory trial", holds it, its trigger the close of the refinement Plan Step (`056d14a`).

Decided by the reviewer, 2026-11-02, during the work:
- **FINDING-1487:** `temp/run-6-handoff/` stays, and the TODO item "Read CBC Run 6" names it.
- **FINDING-1488,** the agent's call reversed at the Foundation Check: project-recording §14 says a section goes with its item, so §7, §8 and §26 go, and the header gains no "Item: none".
- **DECISION-52's tag:** a tried Enemy Collision where nothing dies is `HOLDS-<n>`, numbered on its own.

Decided by the reviewer, 2026-11-02, after the work:
- **The read again is skipped** (`.claude/approaches-on-trial/refinement.md` §2.9, *The last read*), because the reviewer is out of tokens. The refinement closes on this read's work. §2.9 stands as written: this is a one-time departure for budget, not a lesson for the Approach on Trial's evaluation.

### DECISION-49's pass

The ending of each TODO item whose trigger looked passed, drafted by the agent and taken by the reviewer, 2026-11-01. Lines are `TODO.md`'s at `1ce79f9`. CBC Run 5's CBC Run Reading exists; its work waits in the stopped Plan Step "Take CBC Run 5's lessons for CBC Run 6". The TODO edits land with round 1's layer 4.

**Re-aimed at work already planned:**
- **A commit plan's look-back (77):** at CBC Run 5's reading's WORK-17, which gives it FINDING-9 and D18. The Context says what CBC Run 5 did: 13 look-back lines, 0 tries (FINDING-1490).
- **Examples in the concept (99):** at WORK-17, which gives it the worked-example section. "271 lines" becomes 328.
- **How work is run by agents (117):** at WORK-17, which gives it that CBC Run 5 delegated nothing.
- **Evaluate auto-run (190):** at WORK-10's landing, which puts the reading's nine lessons into auto-run. "Used once" becomes "used twice" (FINDING-1493).

**Re-aimed at a new trigger:**
- **Run this repo's retrospective (676):** the refinement Plan Step's close. The two manuals point at this item, by DECISION-48.
- **Release concept v2 (917):** "the reviewer names it, after the refinement's close".
- **The Infrastructure Contract's facility paragraph (981):** "a CBC Run Reading finds a CBC Run writing it unprompted". The Context says CBC Run 5's reading has nothing on it.
- **A level for System Guarantees held by absence (1187):** the same, with the same note.

**Closed:**
- **Give the method a glossary (1015):** `delivery/method/docs/glossary/method.md` does it (ADR-0078). What is left, a stranger meeting the words in the chapters, goes to Release concept v2's README item.
- **Whether the worked example anchors a CBC Run's CBC Framing (1165):** CBC Run 5 framed another kind of problem, two Responsibility Areas and a LAYER-5 not empty (its reading, §4). The second example's idea moves to the examples item.
- **Whether the next Newborn CBC Run adds the ground-must-be-up rule (740):** into "Read CBC Run 6", as one idea: CBC Run 5's and CBC Run 6's Entry Files.
- **CBC Run 5's first Invariant Slice against the Evidence Test Shape (727):** into CBC Run 5's reading, whose FINDING-23 and 30 are what the Plan Step Gate found. Uncertain: whether they cover the whole comparison is checked at the fix.

**Still waiting, wording only:**
- **A sweep for one home (267)** and **which ideas are Idea Models (751):** the trigger becomes "the refinement's close"; Round 2's condition is met.
- **A delivery's path check (685):** the trigger stands; the Context's "the next CBC Run Birth is where they first land" says they landed at CBC Run 5's.
- **Read CBC Run 4 (414):** stands. Line 433 quotes other items' triggers inside a question, so left E7's line 433 is declined.
- **Skill Template (885):** stands. "Only some say" is true, inside an idea, so left E10 is declined.

**To check at the fix:**
- **A standing full read for missing Fact References (803):** `git blame` on the Dependencies findings missed at a change. If any line is newer than 2026-10-27, the trigger has fired, and the item is re-aimed at the refinement's close with those findings as evidence. Its "once the settled form is written" goes either way (left E9).

### The read's counts

385 findings:
- **by Refinement Round:** round 1, 177: Stale lines 75, Wiring 15, Agreement 86, and DES-1's merge; round 2, 115: One home 21, Dependencies 34, Lessons 28, Layout 32; round 3, 93, Writing;
- **by Refinement Layer:** 1, 14; 2, 21; 3, 87; 4, 63; 5, 36; 6, 164;
- **by source:** the readers 262, the leftovers 83, the scripts 3, met in passing 37;
- **proposed:** 284 a fix, 101 a question for the reviewer: 71 the readers', 30 the agent's.

The readers' 262:
- **by how they stand:** 118 checked, 116 resting on the reader, 28 uncertain;
- **by cause:** 192 missed at a change, 54 older than the rule, 14 the rule unclear, 1 known and deferred to TODO, 1 not traced.

By reader, before merges: SL1 15, SL2 23, SL3 6, SL4 5; Agreement, ours 17, what ships 15; One home, ours 8, what ships 15; Dependencies, ours 21, what ships 13; Lessons, ours 8, what ships 18; Layout, ours 10, what ships 12; Writing A 7, B 10, C 3, D 6, E 15, F 15, G 8, H 12, I 10.

### The work (§2.7)

One Change Set, `COMMIT-PLAN.md`, from `f92d6b7` to its close: 385 findings, every one ended. Written from `git log`: each commit, and the findings its body names. A finding named in two commits landed in parts, or a follower carried it to the other side of the agent/docs split.

- `9505824` docs: facts-in-sync's rules take the decisions: 1447, 1517, 1553
- `a998c32` fix(delivery): shipped lines follow facts-in-sync: 1447, 1553
- `25b2b04` docs: writing manual takes the decisions: 1453, 1456, 1535, 1728
- `ae5c1dc` chore(agent): our writing rule follows its manual: 1456, 1520, 1755
- `cc8c927` fix(delivery): container's writing rule follows: 1456, 1535, 1763
- `f2682a3` docs: a CBC Run receives Work Approaches: 1412, 1416, 1437, 1466, 1591, 1596, 1729
- `eb85cce` fix(delivery): the container holds Work Approaches: 1527, 1539
- `7f07dc6` docs: Agent Skill Stages from Stage 0, by §1.4: 1525
- `c3f9e2c` chore(agent): exchange Agent Skills' headings: 1525, 1626
- `027c228` docs: TODO points at the exchange for a reading: 1626
- `f081e65` fix(delivery): container glossary's Agent Skill Stage: 1525
- `576caba` chore(agent): our rules name delivered glossaries: 1516, 1518
- `a763ed1` fix(delivery): delivered-copies covers glossaries: 1529
- `997abe5` docs: records name the delivered glossaries: 1436, 1478
- `7544def` docs: trials point at their TODO items: 1425, 1431, 1451
- `2cbefbe` chore(agent): auto-run's rejection says when: 1513
- `0d3c23a` docs: CBC Run Birth, the event: 1458, 1542
- `9fa370a` fix(delivery): a Name's home in the CBC Run's seat: 1650 to 1652, 1758, 1759, 1765
- `056d14a` docs: TODO holds the Conversation Memory trial: 1431
- `efefb47` chore(agent): held Agent Skills take references: 1633 to 1636, 1639, 1640, 1645, 1649
- `6de7328` fix(delivery): the container's held copies follow: 1634, 1639, 1643 to 1645, 1647 to 1649
- `315f643` docs: exchange's Delivery Take, held and logged: 1444, 1530, 1531
- `89375da` fix(delivery): delivered-copies and its glossary: 1444, 1530, 1531
- `dbf26f3` docs: the rules-in-force list's place: 1537
- `7675552` fix(delivery): retrospective and the Record Stub: 1537, 1538
- `2ae23a1` docs: the devlog in short sentences: 1705, 1731
- `c7d4eec` fix(delivery): the devlog Record Stub follows: 1766
- `c0e133f` docs: a fact the agent misses by not noticing: 1714
- `f194796` chore(agent): our Entry File's three tests: 1751, 1752
- `36af646` docs: "Real question" in plain words: 1740
- `24181bf` chore(agent): auto-run's "Real question", plain: 1748
- `787a212` docs: the conventions manual and the index: 1411, 1413 to 1415, 1417, 1418, 1588 to 1590, 1703, 1704, 1724
- `e32725a` docs: project-recording, its last read findings: 1419 to 1424, 1426 to 1430, 1432, 1592, 1593, 1706 to 1709
- `7cc0aa6` docs: project-recording names both channels: 1432
- `372af7e` docs: three manuals, their last read findings: 1434, 1435, 1438, 1439, 1441 to 1443, 1595, 1597 to 1600, 1715 to 1717
- `dda6f45` docs: exchange and facts-in-sync, last read findings: 1445, 1446, 1601 to 1603, 1718 to 1723
- `807cf10` chore(agent): our files take facts-in-sync's parts: 1446
- `1b744bf` docs: five manuals, their last read findings: 1448 to 1450, 1452, 1454, 1455, 1457, 1604 to 1615, 1725
- `13e4847` fix(delivery): Hygiene Base names the CBC Bootstrap: 1448
- `91d1e5c` docs: the glossary and the Idea Models: 1435, 1459 to 1465, 1467 to 1473, 1616 to 1618, 1726, 1727, 1730
- `5dec14f` docs: the concept's chapters, editorial again: 1433, 1594, 1710 to 1713
- `9a79e8c` docs: chapter 00 names design-before-code's gap: 1433
- `053cdab` docs: two cases point at their story: 1443, 1599, 1612
- `9a22250` docs: ARCHITECTURE and README, last read findings: 1427, 1474 to 1477, 1479, 1485, 1486, 1619 to 1622, 1735
- `51e314b` fix(delivery): the other stack points at exchange: 1620
- `bf94ea2` docs: PLAN, its last read findings: 1480 to 1484, 1732 to 1734
- `9d8ca44` fix(delivery): playbook's Close reference, one form: 1481
- `7af6189` docs: TODO, DECISION-49's pass: 1490 to 1493, 1495, 1504 to 1507, 1509 to 1511, 1625, 1626
- `eec14ca` docs: TODO, its other last read findings: 1494, 1496 to 1503, 1508, 1623 to 1625, 1738, 1739, 1741 to 1747
- `cc2d16b` docs: temp/ and the Conversation Memory: 1487 to 1489, 1736, 1737
- `307e2bf` docs: the manual's form, a rule beside its headings: 1515
- `fddb68d` chore(agent): our rules and log, last read findings: 1514, 1515, 1519, 1628 to 1632, 1753, 1754
- `dc52440` chore(agent): our Agent Skills and trials, last read: 1512, 1521 to 1524, 1627, 1637, 1638, 1749, 1750
- `8871e84` fix(delivery): commit-messages names Approaches on Trial: 1521
- `ea16c1e` fix(delivery): container rules and skills, last read: 1526, 1528, 1532 to 1536, 1641, 1642, 1646, 1759 to 1762, 1764
- `59ef042` chore(agent): approach-drafting points at PLAN.md: 1646
- `e6403b9` fix(delivery): container stubs and glossary, last read: 1540, 1541, 1756, 1757, 1767, 1768
- `eb822da` fix(delivery): Pure Seed, playbook, Local Map, last read: 1421, 1543 to 1546, 1570, 1571, 1653 to 1659, 1668 to 1671, 1769, 1770
- `e97037e` fix(delivery): the method's Output Shapes, last read: 1547 to 1552, 1660 to 1663, 1771, 1772
- `127f617` fix(delivery): a collision where nothing dies, HOLDS: 1550, 1552
- `fffd1c3` fix(delivery): the cbc-framing Agent Skill, last read: 1553 to 1562, 1664 to 1666, 1773 to 1782
- `0f3ce94` fix(delivery): the cbc-slice Agent Skill, last read: 1563 to 1569, 1667, 1783, 1784
- `12735dc` fix(delivery): the cbc-bootstrap Agent Skill, last read: 1572 to 1579, 1587, 1672 to 1694, 1785 to 1789
- `f91f893` fix(delivery): infra Agent Skills, stack glossary, last read: 1572, 1580 to 1587, 1679, 1695 to 1702, 1790 to 1795
- `20bdb4d` docs: TODO's plain rewrite keeps what is left: 1501 to 1503, 1665, 1744
- `d3a154c` docs: FINDING-206 went before Round 3: 1503
- `7a376c5` docs: commit-messages cites claim A1 at §12.1: 1440

Endings:
- **fixed:** 370, FINDING-1776 among them, met by 1555's fix;
- **stand by a decision or a call:** 10: 1594 (DECISION-43); 1605, 1627, 1643, 1648 and 1682 (DECISION-45); 1710 (DECISION-46); 1765 (DECISION-47); 1771 (DECISION-37); 1559 (the agent's call);
- **declined:** 4: 1507 and 1514, as decided; 1519, working-a-reading's Foundation Line already the exchange manual's words; 1564, CBC Run 4 still not read;
- **left for the refinement's close:** 1, FINDING-1512, approach-drafting's "The refinement is open.", in both copies.

Ended by the reviewer during the work: FINDING-1431, 1432, 1433, 1444, 1487, 1488, and DECISION-52's tag (*Decisions*, above).

Departures from the plan:
- **commits added:** 5c, 5d and 19b for rename greps; a follower for each family that crossed the agent/docs split; 32 in two, its DECISION-52 half after the reviewer named the tag; the plain-rewrite item after commit 36, and a correction to it; FINDING-1440, missed at commit 18 and found by this list;
- **commits dropped:** 2b and 8b, their followers already agreeing;
- **findings moved:** 1421 to the playbook's commit; 1759 taken early; 1501 to 1503 and 1744 after commit 36, by DECISION-50; 1572 to commit 36, with 1587; 1665 to TODO's plain-rewrite item, by DECISION-43;
- **calls reversed:** FINDING-1435, declined at commit 18 and fixed at 21; FINDING-1488's call, reversed by the reviewer at the Foundation Check;
- **a commit body wrong:** `bf94ea2` names project-recording "§3" for the Plan Step Form; it is §2.4.
