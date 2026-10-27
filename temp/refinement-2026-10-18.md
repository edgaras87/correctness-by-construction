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
| 3 | Writing | text older than ADR-0053, against the whole rule | `.claude/rules/writing.md` |

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

By layer, in the order the work takes them. Each says its kind,
how it stands, and the agent's proposed ending.

#### Layer 1: the conventions manual

**FINDING-135.** One home; checked. Two rules say when a section
gets a number. `docs/conventions/conventions/` §3.3 (line 187):
a section "that other text will point at". `docs/conventions/facts-in-sync/`
§3: by form, "whether anything points there yet or not".
`.claude/rules/convention-manual.md` follows facts-in-sync.
Proposed: fix. §3.3 cuts the sentence and points at facts-in-sync §3.
Ending: fixed, `a6a9e03`: §2.5 points at facts-in-sync §3.

**FINDING-136.** Layout; checked. §3.3 lists a manual's parts in one
paragraph of 22 lines. Two parts have numbered subsections (§3.4,
§3.7); five do not. The body and *Where to look*, two of the rule's
nine, are missing. Rests on DECISION-9. Proposed: fix, one numbered
part per section of the form.
Ending: fixed, `a6a9e03` and `2e0caac`: §2.1 to §2.9, the second bringing in what only the rule said.

**FINDING-137.** Layout; checked. §3.3 holds four more subjects:
- the channel, told again in *Why it arrives this way*;
- the open question of a shape, told again in
  `docs/conventions/shapes/`, the deliverer's seat;
- how the form grows;
- two layout rules.
Ending: fixed, `a6a9e03`: the channel and the shape's question point; the layout rule is §2.5.

Proposed: fix. The channel stays in *Why it arrives this way*. The
open question keeps one home. The layout rules get a part of their
own.

**FINDING-138.** Layout; checked. §2 holds three subjects in
unnumbered parts: how a rule is written, the frontmatter with every
kind of file's `foundation` value, and stages. Nine pointers land
on §2, for different parts. Proposed: fix, number them 2.1 to 2.4.
§1's labelled part is left to TODO's "Move conventions §1 to the
idea-to-output model".
Ending: fixed, `a6a9e03`: §1.1 to §1.4.

**FINDING-139.** Lessons; resting on the reader. Three cases sit
undated in the body of the manual that holds §3.7: "The form was
not designed…" (§3.3), "Twice a manual grew seat sections…" (§3.4),
"As the last seven were added…" (§4). Proposed: fix, each a dated
italic or cut.
Ending: fixed, `4252509`: three dated italics.

**FINDING-140.** Lessons; checked. §3 keeps history in its body:
"the sections once numbered 3.1, 3.2, 3.5 and 3.6 moved there".
`docs/conventions/facts-in-sync/` §4: a description states what is
true today. agent-arrangement §3.8 and project-recording §13 put a
kept number in an italic. Proposed: fix, a dated italic. The gap
itself stays (ADR-0065).
Ending: fixed, `a6a9e03`: the sentence cut, with no italic, since DECISION-9 left no gap to explain.

**FINDING-141.** One home; checked. The `foundation` line is told in
four texts: conventions §2 (each kind's value), facts-in-sync §4
step 2 (which files carry it), exchange §3.5 (it travels with a
copy), and `.claude/rules/convention-manual.md`. Exchange §3.5 says
conventions §2 holds the list; *The words* in `ARCHITECTURE.md`
cites both. Proposed: fix. One numbered home for which files carry
it; the others keep their own part and point.
Ending: fixed, `c0a3849` and `5709dc7`: conventions §1.3 is the home.

**FINDING-142.** Dependencies; checked. No rule says whether a
footer's decision line names the section it backs (met in round 1,
item 4). Of our 30 lines in layer 5, 4 do, all in
`visual-comparison`. Proposed: fix, one line in conventions §2: "A
footer line names the section it backs, unless it backs the whole
file." Then edit only the lines that back one section, both copies
alike. Against: a grep for the ADR's number already finds the file.
Ending: fixed, `42fb270`, `5611f5f` and `ab80964`: 57 lines in both seats read; 22 changed.

**FINDING-143.** Dependencies; resting on the reader. "is open
(TODO)" in conventions §3.3 and "(TODO)" in
`docs/conventions/shapes/`, the deliverer's seat, name no item.
Proposed: fix, name it by its first words, "Decide whether our own
forms become shapes".
Ending: fixed, `a6a9e03`: both name the item.

#### Layer 2: project-recording

**FINDING-144.** One home; resting on the reader. How a step opens,
stops and closes is told in project-recording (§2.4 and the
deliverer's seat) and again in `PLAN.md` (its header comment, *The
step form*, and the close). Re-reading the entry file at a close is
also agent-arrangement §2.6. Project-recording §2.4 calls the form
"the playbook's" with no path. Rests on DECISION-11.
Ending: fixed, `cce8e9d` and `583bf8f`: the step form holds how, project-recording what and why; the other records followed in the same plan.

**FINDING-145.** One home; resting on the reader. What each record
holds is told in `CLAUDE.md`'s records table, `README.md`'s "What
it answers" column, `ARCHITECTURE.md`'s codemap and
`temp/README.md`. They differ already. For the devlog, README says
"open questions" and `CLAUDE.md` "a TODO item's story". For the
plan, README says "what *done* means" and `CLAUDE.md` "The step
form, and the open step". README and `CLAUDE.md` also share an
opening phrase, where project-recording §7.6 says "no shared text".
The records map would be a fifth. Rests on DECISION-12.
Ending: fixed, `4f7ad15`, `b20d992`, `6241ff2`, `0a40aea` and `e64c51f`, all but the codemap's part, which waits for layer 4 and TODO's "Decide what kind of text our ARCHITECTURE is". The codemap's part fixed in layer 4, `45e1028`.

**FINDING-146.** Layout; checked. §5.5, conversation-memory, is a
record of its own inside TODO's run of sections. TODO's *When* and
*Anti-patterns* become §5.6 and §5.7. §3.5 does the same inside the
ADRs' run. Proposed: §5.5 fixed, a numbered section of its own,
placed last. Or declined while it is on trial. §3.5 declined: small,
and cited twice.
Ending: fixed, `fa57042`: §14, placed last. §3.5 declined, as the endings say.

**FINDING-147.** Layout; resting on the reader. §7.6, the
anti-patterns, holds "README is the front door for people; the
entry file is the one for agents", which is §7.1's subject.
Proposed: fix, move it.
Ending: fixed, `f6c5153`.

**FINDING-148.** Dependencies; resting on the reader. The `CBC
ADR-nnnn` tag is retold in exchange §3.7 and in `exchange-deliver`
with no fact reference. Its home is project-recording §3.5.
Proposed: fix, add the reference, or cut the clause in the skill.
Ending: fixed, `5f454a1` and `797bb8b`: exchange §3.7 points at §3.5; `exchange-deliver` drops the clause.

#### Layer 3: the other manuals, the models, the concept

**FINDING-149.** Dependencies; checked. agent-arrangement names
project-recording as `one-home.md`'s convention, in §3.2 (line 303),
and in *What the difference is* (line 104). Both `one-home.md` name
facts-in-sync in their `foundation` line, and facts-in-sync lists
them. Proposed: fix, name `docs/conventions/facts-in-sync/`.
Ending: fixed, `d2df7ff` and `c79db64`: §3.2's line went with the container's list; *What the difference is* names facts-in-sync.

**FINDING-150.** Layout; checked. agent-arrangement §3.2 holds three
subjects: the `rules/` directory, the every-session rule, and the
container's four rules. The run's seat lists those four rules too,
and `ARCHITECTURE.md` §2.3 a third time. §3.2's first sentence
retells §5.6. Proposed: fix. The every-session rule takes a
numbered part of its own, placed last. The list stays in the seats.
The first sentence points at §5.6. `ARCHITECTURE.md` §2.3 goes to
TODO's ARCHITECTURE item.
Ending: fixed, `d2df7ff`: the every-session rule is §3.9; §3.2 points at §5.6; the list stays in the seats. `ARCHITECTURE.md` §2.3's list was already an Idea of TODO's ARCHITECTURE item.

**FINDING-151.** Layout; checked. agent-arrangement §1 has two
labelled parts with no numbers, "Detachable, and kept so." and "Not
records.", where §2, §3 and §5 number theirs. Proposed: fix, 1.1 to
1.3. Or declined, if two bold leads are emphasis.
Ending: fixed, `6c5003d`: §1.1 to §1.3.

**FINDING-152.** Lessons; checked. agent-arrangement §2.3 retells
*What it is for*'s case, "one run showed to be a pure rename".
Proposed: fix, cut the clause and point at §5.1.
Ending: fixed, `e2a0d1f`.

**FINDING-153.** Dependencies; checked. agent-arrangement cites
"(model claim M1)" and "(model claim A2, assumed)" with no path.
Their home is `docs/models/agent.md` §12. Proposed: fix.
Ending: fixed, `c79db64`: `docs/models/agent.md` §12.7 and §12.1.

**FINDING-154.** Dependencies; checked. A rule's load limit, that
it arrives after the first draft, is agent-arrangement §5.6. Three
lines point at §3.2 for it: conventions §3.3 and *Why it arrives
this way*, and the exchange. Six state it with no reference: the
exchange, shapes and writing manuals, and the comments of three
rules (`convention-manual.md`, `exchange-reading.md`,
`foundation-check.md`). `TODO.md` points at `.claude/decisions.md`
for it. Proposed: fix, all to §5.6.
Ending: fixed, `3d70b55` and `4fd5673`: every such line names §5.6.

**FINDING-155.** Lessons; checked. Exchange §3.7 holds three rules
only in its dated italic: a verdict is the decision and what the
run owes, nothing else; never describe our own practice; never say
"accepted" for something not decided. `exchange-deliver` states
them, standing on this manual. Proposed: fix. The body states the
three, and the italic keeps the 2026-09-20 case.
Ending: fixed, `c244e6c`.

**FINDING-156.** Lessons; checked. Exchange §6.3's rule, that a
reading asks what the run teaches the worked example, is only in
its italic. `exchange-read` points at §6.3 for it. Proposed: fix,
one sentence in the body.
Ending: fixed, `c244e6c`.

**FINDING-157.** Lessons; resting on the reader. Cases in the
exchange's body, undated: §3.1 "this repo did once, into a run
mid-step", and "*The last delivery was named one commit before its
note was finished.*", whose "last" goes stale; §4 step 4, "a rename
once left the old file standing"; §5.1, "which has happened";
§5.4, "Run 3's text says *source*". Proposed: fix, each a dated
italic or cut. §5.4 may be declined as an example.
Ending: fixed, `c244e6c`: four cases dated by 2026-09-25. §5.4 declined, as the endings say.

**FINDING-158.** Lessons; uncertain. Three italics hold a live
claim, not a case: exchange §3.4 "*One exists. One is owed…*";
repo-hygiene "*How an overlay reaches a run is open.*";
retrospective "*Reopened if…*". An italic reads as history and goes
stale. Proposed: move each live claim into the body, or decline.
Ending: fixed, `dd88bf6`: each claim stands in its body.

**FINDING-159.** Layout; checked. Exchange §3.5, the `foundation`
line, holds "**One pin** for all of it", whose home is §2.2.
Proposed: fix, move it.
Ending: fixed, `ac6db0c`: §2.2.

**FINDING-160.** Layout; checked. The note is told in five sections
of the exchange: §2.5, §3.7, §6.5, §6.6 and §6.7. "A note without
files" is told three times (§2.5, §6.6, §6.7), and "the verdicts go
in the note" twice (§6.5, §6.7). Proposed: fix. §3.7 stays the
note's home. §6.6 holds a note without files, and §2.5 points at
it. §6.7 merges into §6.5.
Ending: fixed, `ac6db0c`: §6.7 merged into §6.5 and §6.6.

**FINDING-161.** One home; checked. Where `concept/` lands in a run
is told in exchange §3.3, "stated here once"; in `exchange-deliver`,
"this is the one line that says so"; and in `delivery/README.md`
§1 and §3. `delivery/installs/pure-seed.md` cites ADR-0036 for it.
`delivery/README.md` and the seed also name two files by bare name.
Proposed: fix. Exchange §3.3 is the home. The skill keeps its
command and cites §3.3. `delivery/README.md` and the seed point at
§3.3 and §3.2, with root paths.
Ending: fixed, `32d28f3` and `1347134`: the map, the seed and the skill point at exchange §3.3. One bare name found and fixed, `00-cbc.md`.

**FINDING-162.** Dependencies; checked but for the last part.
Sections missing or wrong:
- facts-in-sync's run seat points at the exchange with no section
  (§6);
- `CLAUDE.md`'s comment cites agent-arrangement §2.4 for a §2.6
  fact;
- the visual-comparison manual says shapes "states its own rule"
  (§4.3);
- uncertain: shapes and `TODO.md` cite exchange §3.2 and §2.3 for
  "one pin", which is §3.5.

Proposed: fix each.
Ending: fixed, `f7d32ca`, `8c37759` and `ac6db0c`. The visual-comparison line then lost its shapes example in `3907dc0`.

**FINDING-163.** Lessons; checked. Shapes §1 states only in an
italic that when an output opens, extends and closes is its owning
convention's. *What this does not cover* points at §1 for it, and
the shipped `shapes-lifecycle.md` states it. Proposed: fix, move the
rule into the body.
Ending: fixed, `1d03c6d`.

**FINDING-164.** Lessons; checked. Shapes §1's italic ends "a shape
catches a part missing, not a part that lost half its meaning". The
body does not say it. Proposed: fix, one sentence.
Ending: fixed, `1d03c6d`.

**FINDING-165.** Lessons; checked. Shapes §4.3 states only in an
italic that the page's pictures never carry a fact alone. The
visual-comparison manual sends readers here for it. Proposed: fix,
a body sentence.
Ending: fixed, `1d03c6d`.

**FINDING-166.** Layout; checked. Shapes §1 holds two subjects:
what a shape is, and how one is born and written, with a labelled
part, "Before a shape is written…", unnumbered. §4 and §5 number
theirs. Proposed: fix, 1.1 to 1.3.
Ending: fixed, `4eb8a57`: §1.1 to §1.3.

**FINDING-167.** Lessons; checked. Retrospective §3's italic holds
two rules the bullets lack: tests are counted from this run's
reports only; a tool that edits text is checked on what it must not
touch. The shipped `apply-retrospective` states both. Proposed: fix,
two bullets.
Ending: fixed, `01e8715`.

**FINDING-168.** Lessons; checked. Retrospective §1 gives the
reason for the apply step only through run 3. Proposed: fix, state
it in general, and move run 3 to a dated italic.
Ending: fixed, `01e8715`.

**FINDING-169.** One home; checked. Retrospective's run seat says
of the manual's summary "the skills are the source" (line 48). A
manual is what its skills derive from. Proposed: fix, the skills
stand on this manual, and the summary says it is one.
Ending: fixed, `da1049a`.

**FINDING-170.** Layout; resting on the reader. Retrospective's
*Why it arrives this way* retells §1's two-steps reason. Proposed:
fix, point at §1.
Ending: fixed, `da1049a`.

**FINDING-171.** Lessons; checked. Commit-plan §2: "Material-first
is a first-class mode" has one reason only, the seed's third run;
and "a session inside PLAN's Step 10…" sits in the body. The other
bullets put their cases in dated italics. Proposed: fix.
Ending: fixed, `efa463e`.

**FINDING-172.** Layout; checked. The sweep for moved names is split:
facts-in-sync §3 says a commit plan's sweep looks again before its
close and points at commit-plan §2, which states the sweep only in
part; the skill says "before the close"; `foundation-check.md` *A
moved section* is a third telling. TODO's "Decide whether each
seat's copy is written for its seat" notes part of it. Proposed:
fix, the sweep takes a numbered part in commit-plan §2, and the
others point at it.
Ending: fixed, `79bc4a2`: §2.1 to §2.13, the sweep §2.10.

**FINDING-173.** Dependencies; checked. Commit-messages §2's rules,
an agent file never shares a commit and a commit waits for the word,
are named by name and not by path: in `foundation-check.md` step 5,
`PLAN.md` (twice), the commit-plan manual, `TODO.md` and
`working-a-reading.md`. `PLAN.md` and `working-a-reading.md` rely on
them with no reference. Facts-in-sync and the commit-plan manual
give the path with no section. Proposed: fix,
`docs/conventions/commit-messages/` §2.
Ending: fixed, `3b2782b` and `a718c58`.

**FINDING-174.** Lessons; checked. Facts-in-sync §4 tells history in
its body: "The rest ran twice by hand before this was a rule…".
Proposed: fix. The body names what enforces steps 3 to 5 today, and
the history goes to a dated italic.
Ending: fixed, `9a0fe5a`.

**FINDING-175.** Layout; checked. Facts-in-sync §3 holds three
subjects: the fact reference, the numbering of parts, and the grep
when a commit renames. Eight pointers land on §3, for different
parts. The numbering rule's sibling, one subject to a section, is
conventions §3.3. Proposed: fix, number the three. The reviewer
decides whether the numbering rule moves beside conventions §3.3
(FINDING-135).
Ending: fixed, `7fbeccb` and `a9e54e2`: §3.1 to §3.3; the numbering rule stays here.

**FINDING-176.** One home; checked. The concept's bump rule is told
in `ARCHITECTURE.md` §1.1 and in `CHANGELOG.md`'s header comment,
neither citing the other. Three manuals point at ADR-0003 and §1.1.
Facts-in-sync §4 names three targets. Rests on DECISION-14.
Ending: moved to layer 4, its home's layer, since DECISION-14 put the rule in the CHANGELOG's comment (`.claude/approaches-on-trial/refinement.md` §2.7). Decided with layer 3's plan, `cc00ca0`. Fixed in layer 4, `f18f280` and `93fc788`.

**FINDING-177.** Lessons; resting on the reader. The
visual-comparison manual §2, "The render decides", gives as its
reason only the Mermaid case. Proposed: fix, one general reason, or
decline, since the case points back at *What it is for*.
Ending: fixed, `2b9b364`.

**FINDING-178.** One home; resting on the reader. The conventions
index says "nothing here restates one", yet it restates
`commit-plan`'s "plans the commits, not the change",
visual-comparison's boundary, each convention's moment ("fires
when…"), and each domain skill's order. TODO's "Make the
conventions index a full local map" is related. Proposed: fix, keep
who hands to whom. Or TODO, into that item.
Ending: fixed, `dbfe842`.

**FINDING-179.** One home; resting on the reader. Two coined words
are defined in more than one place. "Description": *The words*,
facts-in-sync §4 and `docs/models/idea-to-output.md` §2, which
disagree on which texts are descriptions. "Approach": *The words*,
idea-to-output, and `approach-drafting.md`, which ships, so it keeps
its own. Proposed: "description" to TODO, the ARCHITECTURE item;
"approach" fixed, idea-to-output points at *The words*.
Ending: split. "Approach" fixed, `be9b3a4`: *The words* points at the model §2, the reverse of the proposal, decided with layer 3's plan, `cc00ca0`. "Description" is with TODO's ARCHITECTURE item. "Description" fixed in layer 4, `b71b437`, by ADR-0068 decision 1.

**FINDING-180.** Layout; checked. `docs/models/idea-to-output.md` §3
holds two subjects other text points at, a link and a
disagreement's rule, in bold parts. §4's parts, Down and Up, are
unnumbered, where the tiers model numbers the same pair. Rests on
DECISION-8. Proposed: fix when TODO's "Move conventions §1 to the
idea-to-output model" moves text here.
Ending: fixed, `68e5037` and `c6907c7`: §3.1 to §3.3 and §4.1 to §4.3.

**FINDING-181.** Layout; uncertain. The concept tells "tests sample;
structure forbids" in three chapters (00, 02, 04), and the registry's
reordering in two. Its labelled parts are unnumbered. Proposed:
decline. Chapter 00 is the declared overview, each chapter states
the claim for its own subject, and numbering is TODO's "Number the
concept chapters' sections".
Ending: declined, as the endings say.

**FINDING-182.** Lessons; checked. `docs/models/agent.md` ends a
paragraph "Added 2026-10-24." (line 276), history in a description.
Proposed: fix, cut it.
Ending: fixed, `af2579f`.

**FINDING-183.** Dependencies; resting on the reader. In 8 of the 10
manuals with *Where to look*, every entry repeats a pointer the page
already made. Proposed: decline. The form asks for a list of
landings, and the rule allows "pointers only".
Ending: declined, as the endings say.

#### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

**FINDING-184.** One home; checked. `ARCHITECTURE.md` §2.5 retells
exchange §1 (a run is blind, nothing moves up) and §2.2 (the pin and
the read-through) with a pointer that names no section. The pin is
defined again in *The words*. "Two skills and two rules of ours" is
told in §2.4 and §2.5. *The words* gives "take" and "note" no
pointer. TODO's ARCHITECTURE item carries §2.3 and the counts.
Proposed: fix §2.5's pointers with sections, drop the second pin
and the second "two skills", and point the two words at exchange §4
and §3.7.
Ending: fixed, `06be504` and `1e6870f`: the glossary's take and note point at the exchange; §2.5 keeps the table of runs and points by section; the second pin and "two skills" go.

**FINDING-185.** Dependencies; checked. `ARCHITECTURE.md` (line 270)
says where a manual and the concept are handled differently is "that
manual's *What this does not cover* and ADR-0039". It is
facts-in-sync §4, which the paragraph already names. Proposed: fix,
cut the sentence.
Ending: fixed, `ad21148`: the sentence went with §3.

**FINDING-186.** Dependencies; checked. `ARCHITECTURE.md`'s header
comment cites "(project-recording, the deliverer's seat; ADR-0044)"
by name. Proposed: fix, a root path.
Ending: fixed, `60896d8`.

**FINDING-187.** One home; resting on the reader. `README.md`
retells the tiers model's triggers, "anything general waits on
three" and the garden rule, citing only ADRs. Their home is
`docs/models/tiers.md` §2.1 and §2.2. Proposed: fix, add the fact
reference.
Ending: fixed, `61d74d3`.

**FINDING-188.** Dependencies; checked. `TODO.md` cites sections by
bare name in seven Context lines ("project-recording §4", "shapes
§3", "one-home's rule 5"…). Proposed: fix, root paths.
Ending: fixed, `2e25a85`: six lines; the ARCHITECTURE item's three went with it in this commit.

**FINDING-189.** Dependencies; checked. `TODO.md` points at shapes
§1 for "read at a step's gate only", which is shapes §3. Proposed:
fix.
Ending: fixed in layer 3, `4eb8a57`.

**FINDING-190.** Layout; resting on the reader. `TODO.md` holds the
worked example's two copies as two items: "Decide whether a check
compares the worked example's two copies" and "Deduplicate the
worked example". Proposed: fix, merge with both triggers. Or decline:
two decisions, two triggers.
Ending: fixed, `0923263`.

**FINDING-191.** Dependencies; checked. Record headers retell their
manual with no section reference: `CHANGELOG.md`, `TODO.md`,
`PLAN.md`, `.claude/decisions.md`, and `ARCHITECTURE.md` by name.
Facts-in-sync §4 step 2: "Every line that uses a part of a
document, its root included, carries a fact reference to that
part." Rests on DECISION-10.
Ending: moved to TODO's "Decide how a fact reference is written" (DECISION-10).

**FINDING-192.** Dependencies; checked. `TODO-CONVERSATION-MEMORY.md`
cites sections by bare name in about ten places. Proposed: decline.
A part is never rewritten (project-recording §5.5). Rests on
DECISION-13.
Ending: declined (DECISION-13).

#### Layer 5: our agent setup

**FINDING-193.** One home; checked. `working-a-reading.md` step 8
(line 74) keeps its own list of when the devlog is written: "at a
session's end, at a pause, and when a TODO item is added".
`CLAUDE.md`'s table says "Session ending, a dead end hit, or a TODO
item added". Proposed: fix, point at the records table.
Ending: fixed, `ae425c8`: step 8 points at the records table.

**FINDING-194.** One home; checked. `CLAUDE.local.md` restates
commit-messages' "commit on the word" and commit-plan's stop at
every boundary. agent-arrangement §3.7: it holds settings, never
rules. TODO's "Decide how work is run by agents" carries it.
Proposed: TODO, that item.
Ending: moved to TODO's "Decide how work is run by agents".

**FINDING-195.** One home; checked. Five lines say the seats' copies
are identical, kept true by hand. `approach-drafting.md` is
identical too and has no such line. TODO's "Decide whether each
seat's copy is written for its seat" carries the question.
Proposed: TODO, add `approach-drafting.md` to its list.
Ending: worked by ADR-0069: no text claims a copy the same (`3e61b28`, `e0fd201`), and the run's copy speaks to a run (`fe98cd3`); `approach-drafting.md` stays one text until its evaluation (decision 2).

**FINDING-196.** Dependencies; resting on the reader. Our derived
rules and skills use their own manual with few section references:
`writing.md` 0, `exchange-reading.md` 0, `exchange-deliver` 1,
`exchange-read` 2, `working-a-reading.md` 3, `one-home.md` 4,
`convention-manual.md` 5, `foundation-check.md` 7. Rests on
DECISION-10.
Ending: moved to TODO's "Decide how a fact reference is written" (DECISION-10).

**FINDING-197.** Dependencies; checked. `exchange-reading.md` says
"When it opens, extends and closes is the exchange's" by name. Its
home is exchange §6.3 and §6.4. Proposed: fix.
Ending: fixed, `1fe01db`.

**FINDING-198.** Layout; uncertain. The refinement's §2.5 holds the
order of the layers, which §1, §2.2 and §2.7 point at. Its §2.3
also holds how a fix is judged. Proposed: fix, the layers move to
§2.2, in a commit of its own (approach-drafting, stage 2). The §2.3
part declined.
Ending: fixed, `cb2e5e3`: the layers sit in §2.2. The §2.3 part declined, as the endings say.

#### Layer 6: `delivery/`, what ships

**FINDING-199.** Dependencies; checked. The footers of shipped files
(met in round 1, item 5): 9 footers, 27 lines, 14 distinct ADRs,
all in the container. A run can never open one. Shipped text says
only "the deliverer's to explain". Some name "never-oversold", a
project a run cannot know. Dropping them would change the bytes of
4 identical copies. Proposed: fix, keep them, and add one sentence
to `delivered-copies.md` rule 1: a footer names the decisions a
copy rests on; to go against one, quote it under *To the
deliverer*.
Ending: fixed, `bc1e236`: rule 1 says what a footer is and how a run goes against one; the footers stay.

**FINDING-200.** One home; checked. The playbook's version is told
in four places (met in round 1, item 1): the playbook's line and
three in `pure-seed.md`, none tagged. Proposed: fix, the seed reads
the version from the playbook's line at birth.
Ending: fixed, `4806dd6`: the seed reads the version from the playbook's line.

**FINDING-201.** One home; checked. The seed retells exchange §3.2's
list of pinned copies with counts, untagged (met in round 1, item
2). It agrees today. Proposed: fix, "every pinned copy
(`docs/conventions/exchange/` §3.2)", with no counts. The prompt to
the newborn keeps its counts, and the seed's check compares them
with the tree.
Ending: fixed, `b25d0ef`.

**FINDING-202.** One home; checked. Shipped files retell a deliverer
manual with no fact reference (met in round 1, item 3):
`commit-messages` retells agent-arrangement §1, in both copies;
`commit-plan` says "commit-messages keeps…"; `approach-drafting.md`
says "(`commit-messages`)". Proposed: waits on the run's case
(ADR-0059).
Ending: moved to TODO's "Decide how a fact reference is written", the run's case.

**FINDING-203.** One home; checked. `cbc-bootstrap` and its
walkthrough both say a hygiene file takes its stack overlay below
the marker (met in round 1, item 3). Repo-hygiene §2 says nothing
ships an overlay. TODO's "Decide whether cbc-bootstrap points at the
Spring hygiene parts" carries it. Proposed: TODO, that item.
Ending: moved to TODO's "Decide whether cbc-bootstrap points at the Spring hygiene parts".

**FINDING-204.** One home; checked. The container's entry file
cites `docs/conventions/project-recording/` §13, which a run cannot
open. It retells agent-arrangement §2.4's three tests, and seven
stubs with a `foundation:` line retell project-recording. TODO's
"Decide how a fact reference is written" names them. Proposed:
waits on the run's case, through that item.
Ending: moved to TODO's "Decide how a fact reference is written", the run's case.

**FINDING-205.** Dependencies; checked. The shipped `writing.md`
names "the deliverer's writing manual", which a run cannot open.
Round 1's DECISION-3 excepted only `one-home.md`. Proposed: decline
on the same grounds, and name both rules in the exception.
Ending: declined: round 1's DECISION-3 exception names the shipped `writing.md` beside `one-home.md`.

**FINDING-206.** Dependencies; checked. The playbook cites "run 3's
RETRO Dn" in 12 lines, copied into a run's PLAN at birth. A run
cannot open run 3's RETRO. Its *For run 5 only* rule is stated only
for run 5, and run 5 is born. Proposed: fix in the next playbook
version: the rule in general, "For run <n> only", and the
citations into the playbook's header comment.
Ending: fixed in part, `60efe4a`: the rule for a run-only list stated in general, the version unmoved, a fix being no fold. The RETRO citations moved to TODO's "Rewrite the method's texts plain".

**FINDING-207.** Dependencies; checked. Three template comments
point at files by a name that stops resolving once the template is
copied out (`bootstrap.sql`, `testcontainers.properties`,
`verify-database-model.sql`). Ten template headers tell one fact,
"the filled file is the run's own (CBC ADR-0008)", which no shipped
rule holds. Proposed: fix the three with root paths. The headers:
state the fact once in `delivered-copies.md` rule 1 and point, or
decline as text read at copy time.
Ending: fixed in part, `2ccaa58`: the three comments give full paths. The ten headers declined, read when a template is copied.

**FINDING-208.** One home; checked. The off-template rule is told in
four shipped files, and its only home is ADR-0008, which is history.
Proposed: waits on the run's case. That design must say what a
retelling points at when its only source is history.
Ending: moved to TODO's "Decide how a fact reference is written", the run's case.

**FINDING-209.** One home; checked. `cbc-bootstrap` tells its traps
in two or three files each, with no pointers between them: the
Boot 4 and Testcontainers traps, the missing secret, the
notation-neutral environment, plural instances. The harness
reference says "**Masters nothing.**" (line 10) and "the lived
traps live here" (line 186). Proposed: fix, the walkthrough owns
each trap, and the others point.
Ending: fixed, `d0445c3`: the walkthrough owns each trap, its step 4 and §3.

**FINDING-210.** One home; checked. The harness reference holds an
outcome that its stated home, the walkthrough, lacks: the ground's
authority split held in evidence runs. Proposed: fix, the outcome
moves to the walkthrough's step 4.
Ending: fixed, `944f87d`.

**FINDING-211.** One home; resting on the reader. Skills, shapes and
templates state the same form: the slice record's outline, the
backstop at the red run, a cost's size, the registry entry's
fields, a body asserted by path. TODO's "Decide how an approach and
a shape divide an output" carries the question. Proposed: TODO,
these instances into that item.
Ending: moved to TODO's "Decide how an approach and a shape divide an output".

**FINDING-212.** One home; checked. The worked example's two copies
have no owner. Only `cbc-framing-workflow.md` says they are a pair,
and a run editing `cbc-slice`'s copy meets no line saying the other
follows. Proposed: fix, `cbc-framing`'s copy owns, and
`cbc-slice-workflow.md`'s header says its copy follows.
Ending: fixed, `cd79ba3`: cbc-framing's copy owns.

**FINDING-213.** One home; checked. `delivery/README.md` retells the
playbook's steps with no fact reference. Proposed: fix, point at
the playbook.
Ending: fixed, `8a6a1f7`.

**FINDING-214.** One home; checked. The container's entry file says
the order of questions "is not restated here", then restates it
without "world" (`concept/00-cbc.md` line 31). Proposed: fix, drop
the parenthesis.
Ending: fixed, `c05ae65`.

**FINDING-215.** One home; checked. `delivered-copies.md` says the
deliverer's side "is not here; the run never needs it", then rule 4
tells the deliverer's read and verdicts (exchange §6.1, §6.5). Rule 1
also holds part of rule 2's subject. Proposed: fix, rule 4 keeps
what the run acts on, the three verdicts.
Ending: fixed, `de7b19f`.

**FINDING-216.** One home; checked. Shipped retellings that name
their source in prose: 7 places, among them the container's entry
file, decisions log and `temp/README.md`, `infra-serve`'s "Hard
lines (same as establishment)". Proposed: waits on the run's case;
the list is that design's evidence.
Ending: moved to TODO's "Decide how a fact reference is written", the run's case.

**FINDING-217.** One home; resting on the reader. Shipped retellings
that do not name their source, whose source a run holds:
`infra-establish` lists five of the framing workflow's six runtime
ground lines; `cbc-slice-workflow.md` retells the run's
`ARCHITECTURE.md` Invariants columns; the container's README counts
"five chapters". Proposed: fix, each points.
Ending: fixed, `fcf9622`.

**FINDING-218.** One home; resting on the reader. *The whole system
in plain words* says it is a summary, but names its owners only as
"the detailed docs". Proposed: fix, name them by path.
Ending: fixed, `d9a8595`.

**FINDING-219.** Dependencies; checked. Pointers into another skill
by bare file name: four in `cbc-framing` and `infra-serve`. Within a
skill, 32 `references/…` paths and about 13 bare sibling names.
Proposed: fix the four with root paths. The rest to TODO's "Decide
how a fact reference is written", a form choice over about 45
lines.
Ending: fixed in part, `7583446`: five cross-skill pointers, not four. The paths within a skill moved to TODO's "Decide how a fact reference is written".

**FINDING-220.** Dependencies; checked. Shipped rules named in prose:
"the shapes rule" 8 times, "the delivered-copies rule" 5 times, and
two paths to `shapes-lifecycle.md` without the section they rely on.
Proposed: TODO, the fact-reference item.
Ending: moved to TODO's "Decide how a fact reference is written".

**FINDING-221.** Dependencies; checked. `approach-drafting.md` tells
the run "**At the deliverer:** open `approach-evaluation`". The
line is labelled for the deliverer, and TODO's seat-copy item
carries it. Proposed: decline.
Ending: declined: ADR-0069 decision 2 keeps the file one text for both seats until its evaluation at the refinement's close.

**FINDING-222.** Lessons; checked. The `visual-comparison` skill
states "one obvious answer means a clear answer" only inside a case,
the deliverer's own, and no run is named. Two more cases sit in its
body, and its §4 is a list of cases by design. Rests on
DECISION-7.
Ending: fixed, `206c1e0` and `19142f7`, in both seats.

**FINDING-223.** Lessons; checked. The harness reference states
rules through "passes" a run cannot place: "the third pass evolved
this to…", "the second pass closed it… the third relied on…", and
six more pass names. Variation point 9 tells its own history.
Rests on DECISION-7.
Ending: moved to TODO's "Rewrite the method's texts plain" (DECISION-7).

**FINDING-224.** Lessons; resting on the reader. "Lived" markers in
the stack and method texts, about 18. Some carry a fact the reader
acts on, the version tested on or a trial status. Others tell a
case a fresh run cannot know: "both lived runs", "distilled from a
two-seat discipline". The walkthrough's "Lived realization (once)"
ends in a case line. Rests on DECISION-7.
Ending: moved to TODO's "Rewrite the method's texts plain" (DECISION-7).

**FINDING-225.** Layout; checked. `cbc-slice`'s stages sit at two
heading levels: `## Stage 0`, then `### Stage 1` to `### Stage 4`.
Conventions §2, whose example this skill is, binds it. Proposed:
fix, all at `##`.
Ending: fixed, `4f19dad`: all five stages at `##`, the overview above Stage 0.

**FINDING-226.** Layout; checked. Two shapes, `evidence-test.md` and
`kill.md`, say what they leave out in two sections each. Proposed:
fix, under *What is exempt* only.
Ending: fixed, `494b892`.

**FINDING-227.** Layout; resting on the reader. `cbc-framing`'s
"Export and handoff" holds four subjects; `infra-establish`
describes its two manuals in three places; the worked example lays
out Part 1 by headings and Part 2 by bold leads. Rests on DECISION-8.
Proposed: TODO, the plain rewrite of the method's texts.
Ending: moved to TODO's "Rewrite the method's texts plain" (DECISION-8).

**FINDING-228.** Layout; checked. The walkthrough's §4 has two
labelled parts with no numbers, where §1 to §5 are numbered. The
harness reference's variation point 9 is a decided rule among open
points. Rests on DECISION-8. Proposed: fix, 4.1 and 4.2; point 9
declined.
Ending: moved to TODO's "Rewrite the method's texts plain" (DECISION-8).

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

#### Layer 1: the conventions manual

**FINDING-229.** One home; checked. Conventions §3: "The CHANGELOG
is the concept-version log (ADR-0003) and has no place for a
convention's entry" cites the ADR; the home is `CHANGELOG.md`'s
standing comment (DECISION-14). Not changed. Reopens FINDING-176.
Proposed: fix, point at the comment.
Ending: fixed, `2d1e5bd`.

**FINDING-230.** Dependencies; checked. Conventions §3 step 5 asks
to update `ARCHITECTURE.md` §1.2's count, §2.3's ownership line and
the codemap's count; all three went in layer 4 (`f18f280`,
`1e6870f`, `45e1028`). Not changed; its targets were. Reopens layer
4's rewrite. Proposed: fix, step 5 asks for §1.2's line only.
Ending: fixed, `2d1e5bd`.

#### Layer 2: project-recording

**FINDING-231.** One home; checked. Each record's moment is told in
its *When* (§2.5, §3.6, §4.5, §5.5, §6.5, §7.5) and in the records
table, which §11 rule 3 makes the one place ("a second list here
would be a copy that drifts"). They have drifted: §4.5 "Every
working session, 2–5 minutes", the table "Session ending, a dead
end hit, or a TODO item added". Not changed. Proposed: fix, each
*When* keeps its why and points at §13.
Ending: fixed, `78c51bf`.

**FINDING-232.** One home; resting on the reader. How
conversation-memory is read is told in §14, in the file's header
comment, and in `TODO.md`'s header. §14 has no *How*; layer 2's
forms plan skipped it. Changed (moved, `fa57042`). Reopens
FINDING-144. Proposed: fix, §14 keeps what and why and points at
the header.
Ending: fixed, `78c51bf`.

**FINDING-233.** One home; uncertain. §1, the map, holds two lines
no summary holds: the newcomer's reading order (told again in §8.2
and §8.4), and "Everything is Markdown, in the repo, versioned with
git. That is itself a rule of the convention". ADR-0067: the map is
home to nothing. Changed (§1 rebuilt). Proposed: fix, each line
gets its home outside the map.
Ending: fixed, `78c51bf`.

**FINDING-234.** Layout; resting on the reader. §1 holds the map
and a picture per seat of how the records feed each other; §11 is
"How information flows between records". Changed (§1 rebuilt).
Reopens FINDING-145. Proposed: decline: ADR-0067 decision 2 made
the pictures part of the map's form, and §11 holds the flow's
rules, not a picture.
Ending: declined: the map's pictures are ADR-0067's form.

**FINDING-235.** Layout; checked. §13's "**Anti-pattern.**" is an
unnumbered bold part, where the manual numbers its anti-patterns as
parts eight times (§2.6 to §9.6). Not changed. Proposed: fix, §13.1
and §13.2.
Ending: fixed, `78c51bf`.

**FINDING-236.** Lessons; checked. Three live claims sit in dated
italics: §14's "It is looked at when the third such item is worked,
or at the refinement step's close… If it holds, it reaches runs
through the container; if not, it goes."; exchange §2.4's "The
trigger that would reopen it… It has not happened."; facts-in-sync
§5's "Nothing else from four runs has reached a chapter…", stale
since run 5. Not changed. Reopens FINDING-158. Proposed: fix, each
live part stands in its body; the italic keeps its case.
Ending: fixed, `78c51bf`.

**FINDING-237.** Lessons; resting on the reader. §5.4 gives the cap
on a TODO item's Context a reason only in an italic case: "three
lines cut meaning and lost a fact (ADR-0040)". Not changed.
Proposed: fix, §5.4 states the cap's reason in general.
Ending: fixed, `78c51bf`.

**FINDING-238.** Lessons; checked, but (e) and (f) resting on the
reader. History in descriptions' bodies (`docs/conventions/facts-in-sync/`
§4): (a) project-recording's deliverer seat, "as its first devlog
entry agreed on 2026-08-27"; (b) retrospective §2, "They came from
the plan's old Retrospective section, which the skill replaced";
(c) shapes §2, "a shape was called each of them at some point
before it got its own word"; (d) commit-plan's *Why it arrives this
way*, "it moved to `docs/conventions/commit-messages/` §2 for that
reason"; (e) agent-arrangement, "since ADR-0036"; (f) shapes'
deliverer seat, "since ADR-0057". Not changed. Proposed: fix, each
states today's fact or goes; (e) and (f) become citations.
Ending: fixed, `78c51bf`.

#### Layer 3: the other manuals, the models, the concept

**FINDING-239.** One home; checked. Exchange's *What this is made
usable as* ("loading when a reading in `temp/` is read, not while a
new one is written") and shapes' deliverer seat ("loaded when the
file is read, not while a new one is written") tell when a rule
loads with no fact reference; its home is agent-arrangement §5.6.
Not changed. Reopens FINDING-154. Proposed: fix, each names §5.6.
Ending: fixed, `a2d446d`.

**FINDING-240.** One home; resting on the reader. "Description" is
defined in facts-in-sync §4 and in `docs/models/idea-to-output.md`
§2, neither citing the other. Changed (`b71b437`). Reopens
FINDING-179. Proposed: fix, facts-in-sync §4 cites the model §2.
Ending: fixed, `a2d446d`.

**FINDING-241.** Layout; resting on the reader. Exchange §3.7, the
note's home, now holds the verdicts' wording rules, while §6.5,
*Verdicts*, says "The note carries all of them, in the run's order;
there is no other channel". Changed (`c244e6c`, `ac6db0c`). Reopens
FINDING-155 and 160. Proposed: fix, §3.7 says the note carries
every verdict, in the run's order; §6.5 keeps the three endings and
points at §3.7.
Ending: fixed, `de7238c`.

**FINDING-242.** Lessons; checked. Exchange §3.7's italic holds four
general ways a note fails to reach; only the last is a dated case,
and "the relationship changed under it" stands in no body line.
Changed (`c244e6c`). Reopens FINDING-155. Proposed: fix, the body
names the ways no rule there guards; the italic keeps the
2026-09-20 case.
Ending: fixed, `de7238c`.

**FINDING-243.** Lessons; checked. Exchange §6.2: "That is how a
run's rule for editing copies reached this document." History in
the body; §5.1's italic tells the case. Not changed. Reopens
FINDING-157. Proposed: fix, the sentence goes.
Ending: fixed, `de7238c`.

**FINDING-244.** Dependencies; checked. Exchange §5.4:
"`ARCHITECTURE.md`'s words say deliverer"; the words are
`docs/glossary.md` since `8919dac`. Not changed. Reopens layer 4's
move. Proposed: fix.
Ending: fixed, `de7238c`.

**FINDING-245.** Dependencies; checked. Exchange §6.3:
"`references/worked-example.md` in cbc-framing and cbc-slice", a
path relative to a skill. Changed (`c244e6c`). Reopens FINDING-156.
Proposed: fix, the owner's path,
`delivery/method/.claude/skills/cbc-framing/references/worked-example.md`.
Ending: fixed, `de7238c`.

**FINDING-246.** Dependencies; uncertain. Exchange §6.6's "(§2)"
means §2.2; agent-arrangement §5.5's "`docs/models/agent.md` §4"
means §4.3. Each names the part's parent. Not changed. Proposed:
fix, each names the part.
Ending: fixed, `de7238c` for exchange §6.6 and `a2d446d` for
agent-arrangement §5.5.

**FINDING-247.** Dependencies; checked. Facts-in-sync §2's "the
measured case is `docs/conventions/agent-arrangement/`'s" and
project-recording's *Why it arrives this way*, "the failure
`docs/conventions/agent-arrangement/` measured", mean its *What it
is for* and do not say so. Not changed. Proposed: fix.
Ending: fixed, `a2d446d`.

**FINDING-248.** Lessons; checked. Agent-arrangement §3.2's
"*Empty at birth until 2026-09-23.*" ended the list of the
container's rules, which `d2df7ff` moved out; it now follows "with
one exception, §3.9." Changed. Reopens FINDING-150. Proposed: fix,
it goes.
Ending: fixed, `a2d446d`.

**FINDING-249.** Lessons; checked, the second part resting on the
reader. Agent-arrangement §3.8's italic "Numbered last, so the
sections before it keep the numbers history cites" is false since
§3.9 (`d2df7ff`). Project-recording §13's italic explains its own
number the same way. Changed. Reopens FINDING-150. Proposed: fix,
§3.8's italic goes; §13's declined, true and about its own number.
Ending: fixed in part, `a2d446d`: §3.8's italic. §13's declined,
true and about its own number.

**FINDING-250.** Dependencies; checked. Agent-arrangement's *Why it
arrives this way*: "the comments are dropped on load (§2.6)"; §2.6
tells it again and points at §5.3, its home. Not changed.
Proposed: fix, §5.3.
Ending: fixed, `a2d446d`.

**FINDING-251.** Layout; checked. Repo-hygiene says where an overlay
sits twice: §2, "below the marked line each base file carries", and
§3's first rule, "Overlay content goes below the marker". Changed
in part (`dd88bf6`, §2). Proposed: fix, §3's line goes.
Ending: fixed, `a2d446d`.

**FINDING-252.** Layout; checked. Commit-messages §2 and
visual-comparison §2 are bold-led bullets, the form commit-plan §2
had before `79bc4a2` numbered it; 14 pointers name commit-messages
§2, 8 meaning one bullet and 6 another. Not changed. Reopens
FINDING-172. Rests on DECISION-15.
Ending: moved to TODO's "Write when a bold lead is a part", with
DECISION-15's line.

#### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

**FINDING-253.** One home; checked. `PLAN.md`'s header comment
retells the step's gate and close ("the devlog entry that closes it
names the step and the commit of its ticked gate"), which *The step
form* holds, and has drifted from it ("what diverged from the
plan"). Not changed. Reopens FINDING-144. Proposed: fix, the header
says what the file holds and points at *The step form*.
Ending: fixed, `6c83d84`.

**FINDING-254.** One home; checked. The glossary's "master",
"harvest", "local map", "seats" and "manual" restate their homes
with no fact reference, against the glossary's own header; "master"
has drifted from exchange §1, fact 3 ("— or by the run editing
it"). The index's "A local map (ADR-0045)" cites only the ADR.
Changed (moved, `8919dac`). Reopens FINDING-184. Proposed: fix,
each entry points at its home; the index cites project-recording
§8.6.
Ending: fixed, `6c83d84`.

**FINDING-255.** One home; checked. `ARCHITECTURE.md` §2.1 and §2.2
give the `foundation` values word for word; their home is
conventions §1.3. Changed (`1e6870f`). Reopens FINDING-141.
Proposed: fix, keep "derived from" and "checked against", and cite
§1.3.
Ending: fixed, `6c83d84`.

**FINDING-256.** One home; checked. `ARCHITECTURE.md` §3's row "A
skill never spans two groups, and nothing that needs Spring…" names
ADR-0029 as where it is stated; a closed ADR is history. The first
half lives in exchange §3.4; the second has no living home.
Changed (`dcf7530`). Proposed: fix, cite exchange §3.4; the second
half to TODO's "Decide how a fact reference is written", as
FINDING-208's question.
Ending: fixed in part, `6c83d84`: the row cites exchange §3.4. The
second half moved to TODO's "Decide how a fact reference is
written".

**FINDING-257.** Dependencies; checked. `ARCHITECTURE.md` §2.5 cites
the exchange's "(§1)", "(§2.2)", "(§4)" and "(§6)" bare, in a page
with its own §1, §2.2 and §4. Changed (`1e6870f`). Proposed: fix,
each with the exchange's path.
Ending: fixed, `6c83d84`.

**FINDING-258.** Dependencies; checked. `README.md` ("see
docs/models/tiers.md") and `CLAUDE.md` ("see docs/models/tiers.md")
name no section. Changed in part (`cf61def`, `0a40aea`). Reopens
FINDING-187. Proposed: fix, §2.1 and §2.2.
Ending: fixed, `6c83d84` for `README.md` and `1c6c35c` for
`CLAUDE.md`.

**FINDING-259.** Dependencies; checked. `TODO.md`'s direction item:
"Idea-to-output §2's table names `.claude/shapes/`", by bare name.
Changed (`b2c843b`). Reopens FINDING-188. Proposed: fix.
Ending: fixed, `6c83d84`.

**FINDING-260.** Dependencies; checked. `TODO.md`'s hygiene item
splits a path into two code spans, "`docs/conventions/`
`repo-hygiene/templates/java-spring/`", which no grep finds. Not
changed. Proposed: fix, one span.
Ending: fixed, `6c83d84`.

**FINDING-261.** Dependencies; checked. `TODO.md`: the agents item's
"a stop at each boundary (`commit-plan`)", which is commit-messages
§2's stop (commit-plan §2.13), and the line-width item's
"(`commit-messages`)". Changed in part (`3b2782b`). Reopens
FINDING-173. Proposed: fix, root paths.
Ending: fixed, `6c83d84`.

#### Layer 5: our agent setup

**FINDING-262.** Dependencies; checked. The refinement's §1:
"History is the devlog, closed ADRs and commit bodies
(`.claude/rules/one-home.md`)"; the home is
`docs/conventions/facts-in-sync/` §1. Not changed. Proposed: fix.
Ending: fixed, `1c6c35c`.

**FINDING-263.** Dependencies; checked. Our `commit-plan` skill, §3
"commit-messages keeps the two apart" and §6 "The rule is
commit-messages'", name the convention by name. Written for our
seat (ADR-0069). Not changed. Reopens FINDING-173. Proposed: fix,
`docs/conventions/commit-messages/` §2.
Ending: fixed, `1c6c35c`.

**FINDING-264.** Of another kind, Agreement; checked. `CLAUDE.md`'s
records table has no row for `docs/glossary.md`, a record of both
seats since layer 4 (project-recording §1, item 10; §13: adding a
record adds its row). Not changed. Reopens layer 4's `8919dac`.
Proposed: fix.
Ending: fixed, `1c6c35c`.

#### Layer 6: `delivery/`, what ships

**FINDING-265.** Lessons; checked. `visual-comparison`, both seats:
two undated cases in the body, §1's "Once, the table was the best
answer to one requirement and lost on another" and §2 step 5's "In
its first two runs, the render changed a verdict that reasoning had
got wrong". Not changed. Reopens FINDING-222, whose fix stated only
§1's rule. Proposed: fix, each becomes a dated italic or goes, in
both seats.
Ending: fixed, `1c6c35c` in ours and `89b8b35` in the container's:
both cases go, and the manual holds them, dated.

**FINDING-266.** Lessons; checked. `pure-seed.md`'s opening and
`delivery/README.md` §4's row give the reason the entry files arrive
composed only through a case: "runs that derived their own produced
neither the pre-framing guard nor the pin stance". Not changed.
Proposed: fix, the reason stated in general; ADR-0019 keeps the
case.
Ending: fixed, `4fab07b`.

**FINDING-267.** Lessons; uncertain. `delivery/README.md` §4: "The
rest is this repo's, taken from what the runs derived." History in
a local map, which holds relations only (project-recording §8.6).
Not changed. Proposed: fix, the clause goes.
Ending: fixed, `4fab07b`.

**FINDING-268.** Layout; resting on the reader. `visual-comparison`,
both seats: the rule that a candidate set holds a non-picture is
told in §1 and again in §2 step 3. Not changed. Proposed: decline:
step 3 applies §1's rule where it is acted on.
Ending: declined: the step applies §1's rule where it is acted on.

**FINDING-269.** Dependencies; checked. The run's entry file: "read
`00-cbc.md` first", by bare name; `delivery/README.md`'s same clause
got its path in `32d28f3`. Not changed. Reopens FINDING-161.
Proposed: fix, `docs/concept/00-cbc.md`.
Ending: fixed, `89b8b35`.

**FINDING-270.** Dependencies; checked. `delivery/README.md` §2's
"(`pure-seed.md` step 4)" and the seed's check, "identical to
cbc-run-pure-playbook.md", name files bare: the second of
FINDING-161's two names. Changed in part (`4806dd6`). Reopens
FINDING-161. Proposed: fix, root paths.
Ending: fixed, `4fab07b`.

**FINDING-271.** Dependencies; checked. The two workflows' headers,
written by `cd79ba3`, name the other skill's worked example without
a path. Changed. Reopens FINDING-219. Proposed: fix, the run's
paths.
Ending: fixed, `b2368c6`.

**FINDING-272.** Dependencies; resting on the reader. Pointers into
another skill by name: `infra-serve`'s "(infra-establish's Records
and outputs)", `evidence-test.md`'s "cbc-slice's build gate", the
playbook's Release "in the `retrospective` skill's form". Not
changed. Reopens FINDING-219. Proposed: fix, paths.
Ending: fixed, `4fab07b` for the playbook, `b2368c6` for
`evidence-test.md` and `7857b48` for `infra-serve`.

**FINDING-273.** Dependencies; checked. The harness reference's
pointer, "(`spring-boot-walkthrough.md`, step 4, *Traps, exact*,
items 1 and 2)", is ambiguous: step 4 holds two such lists, and the
facts are the second's, under *The harness in the codebase*.
Changed (`d0445c3`). Reopens FINDING-209. Proposed: fix.
Ending: fixed, `7857b48`.

**FINDING-274.** One home; checked. The harness reference §1's
bound facts still tell the Testcontainers 2.x names, the
walkthrough's trap, and hold a fact the walkthrough lacks:
"`flyway-core` alone is not enough on Flyway ≥ 10". The
walkthrough's step 4 points back at the reference's §1 for the Boot
4 engine fact. Not changed. Reopens FINDING-209. Proposed: fix, §1
points as §2 does; the Flyway fact moves to the walkthrough's
traps; the pointer back is re-read.
Ending: fixed, `7857b48`.

**FINDING-275.** Dependencies; checked, `bootstrap.sql` resting on
the reader. `verify-database-model.sql`'s "the role-split model's
claims" and `bootstrap.sql`'s "the role-split reference" name it in
prose. Changed in part (`2ccaa58`). Reopens FINDING-207. Proposed:
fix, its path.
Ending: fixed, `7857b48`.

**FINDING-276.** One home; checked. `cbc-framing-workflow.md`'s
*Tags* and `cbc-slice` Stage 1, item 5, retell writing rule 6's "a
number local to one record carries its owner"; the home is the
run's `writing.md`, rule 6, which the glossary template already
points at. Not changed. Proposed: fix, both point there.
Ending: fixed, `b2368c6`.

**FINDING-277.** One home; checked. `cbc-slice` Stage 4, item 3, "one
row per rule, never a paragraph", retells the ARCHITECTURE stub's
header comment; FINDING-217's fix pointed the workflow's telling,
not this one. Not changed. Proposed: fix, point.
Ending: fixed, `b2368c6`.

**FINDING-278.** One home; resting on the reader. Readiness lists
retell what another skill makes: `system-readiness.md` READINESS-1
against `cbc-framing`'s export list; `cbc-bootstrap` Stage 0 and
`infra-serve` against `infra-establish`'s contract. Not changed.
Proposed: fix, each names what it checks and points at the section
that makes it.
Ending: fixed, `b2368c6` for `system-readiness.md` and `7857b48`
for `cbc-bootstrap` and `infra-serve`.

**FINDING-279.** One home; checked. The playbook's header comment
retells the seed's swap ("At birth, everything from the step form
down replaces the steps…") with no fact reference; the comment stays
here, so our rule applies. Changed in part. Proposed: fix, cite
`delivery/installs/pure-seed.md` step 4.
Ending: fixed, `4fab07b`.

**FINDING-280.** One home; checked. The two retrospective skills'
closes, item 7, retell commit-plan's look back and `-detail` branch,
and disagree: "Merge on the reviewer's word" against "land by
fast-forward", which the playbook's close asks. Not changed.
Proposed: fix, each points at the run's `commit-plan` §4 and §6 and
keeps only its own step; fast-forward.
Ending: fixed, `89b8b35`.

**FINDING-281.** One home; resting on the reader.
`apply-retrospective` Stage 3's records check retells the step
form's closing items, and checks less: not the pairs of copies. Not
changed. Proposed: fix, the skill keeps when the checks run and
points at the step form's closing items.
Ending: fixed, `89b8b35`.

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
