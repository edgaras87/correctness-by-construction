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
| 2 | Dependencies | a retelling where a pointer would do, or a pointer not needed | `docs/conventions/conventions/` §3.1 |
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

Listed by layer, in the order the work takes them. An Agreement
finding sits in its description's layer; which side is wrong is
the reviewer's to decide. "Stands" is §2.4's: checked, resting on
the reader, or uncertain.

#### Layer 1: the conventions manual

**FINDING-1.** Stale lines. Checked. Known.
- Where: `docs/conventions/conventions/README.md`:54-55.
- True: our `.claude/` holds 12 artifacts, 6 skills and 6 rules,
  and the decisions log.
- Text: "this repo, whose own `.claude/` holds ten".
- Ending: fixed, `2bfe201`: no count.

**FINDING-2.** Agreement. Resting on the reader. DECISION-1.
- Where: `docs/conventions/conventions/README.md`:41;
  `.claude/rules/convention-manual.md`:9.
- Rule: a run's first-time work writes a provisional manual at
  `.claude/<name>/manual.md` (`docs/conventions/first-time-work/`,
  the run's seat; the container's skill, step 1.3).
- Text: "A run holds artifacts and writes no manuals." / "a run
  writes no manuals."
- Ending: fixed by ADR-0058 (`a345760`). A run drafts an approach
  on trial, not a manual, so both lines are true; no text changed.

**FINDING-3.** Agreement. Checked.
- Where: `docs/conventions/conventions/README.md`:62-64.
- Rule: our own skills are derived from their manuals, not copied
  (`docs/conventions/agent-arrangement/` §3.1, ADR-0042).
  `docs/conventions/exchange/` §1 and §4 name no copy the deliverer
  holds.
- Text: "the deliverer's own `.claude/skills/` included — is the
  exchange's, `docs/conventions/exchange/` §1 and §4."
- Ending: fixed, `2bfe201`: ours are written here, not copies.

**FINDING-4.** Agreement. Checked. Five places.
- Where: `docs/conventions/conventions/README.md`:216;
  `docs/conventions/exchange/README.md`:38-40, 519-520;
  `docs/conventions/shapes/README.md`:59-60;
  `.claude/rules/exchange-reading.md`:7-8;
  `.claude/rules/convention-manual.md`:7-8.
- Rule: a `paths:` rule loads when a file under its path is read
  with the Read tool, not when one is written
  (`docs/conventions/agent-arrangement/` §3.2; this manual's own
  *Why it arrives this way*).
- Text: "loading while a manual is written"; "loading while a
  reading in `temp/` is written"; "loaded while the file is
  written"; "Loads while one is being written".
- Ending: fixed, `162bfb0` and `98035cd`: all six places say a
  `paths:` rule loads when its file is read.

**FINDING-5.** Stale lines. Uncertain.
- Where: `docs/conventions/conventions/README.md`:229-233.
- True: `5af7355` saw 13 manuals. The redesign's manual, a
  fourteenth, went in `c6a7bcc` 25 minutes before.
- Text: "of the fourteen manuals' opening statements".
- Why uncertain: a dated italic is stale only if it misstates what
  happened, and the count may have been taken before `c6a7bcc`.
- Ending: declined. A dated lesson is wrong only if it misstates
  what happened, and it cannot be shown that the count was taken
  after the redesign's manual went.

**FINDING-6.** Stale lines. Checked.
- Where: `docs/conventions/conventions/README.md`:283-286.
- True: all 13 manuals hold *What this is made usable as*, near
  the top, not at the close.
- Text: "`docs/conventions/exchange/` and `docs/conventions/shapes/`
  close with their lists".
- Ending: fixed, `2bfe201`.

**FINDING-7.** Wiring. Uncertain.
- Where: `docs/conventions/conventions/README.md`:287-289.
- Rule: a path resolves (§3.2). `docs/master.md` went in
  `a337674`.
- Text: "the walk of `docs/master.md` at the exchange plan's
  close".
- Why uncertain: the sentence tells a past event. The path may be
  a name in a story, or a pointer that should read
  `a337674^:docs/master.md`.
- Ending: fixed, `2bfe201`: cited where git keeps it.

**FINDING-8.** Stale lines. Checked.
- Where: `docs/conventions/conventions/README.md`:331-336.
- True: two more chapter changes came from run 3, `86ed0c4`
  (chapter 02) and `41d4fc3` (chapter 01). There are four runs.
- Text: "the concept has bent once … Nothing else from three runs
  has reached a chapter".
- Ending: fixed, `2bfe201`: three bends from four runs, one of
  them making the concept v2 when released.

#### Layer 2: project-recording

**FINDING-9.** Stale lines. Checked.
- Where: `docs/conventions/project-recording/README.md`:14-16.
- True: four runs kept their records under the stubs.
- Text: "three runs kept their records under these stubs".
- Ending: fixed, `f1c02a7`.

**FINDING-10.** Wiring. Checked for the records; resting on the
reader for the stubs.
- Where: `docs/conventions/project-recording/README.md`:22-25,
  38-39.
- Rule: each derived artifact by path from the repo root
  (`.claude/rules/convention-manual.md`, section 3).
- Text: "**The deliverer's own records**, derived from this page
  as the stubs are" names no record. The stubs are bare names
  after "in `delivery/container/`:".
- Ending: fixed, `f1c02a7`: the stubs and our records by path.

**FINDING-11.** Agreement. Checked. Known.
- Where: `docs/conventions/project-recording/README.md`:80-81,
  386, 408-409; `TODO.md`:25; `PLAN.md`:27-28.
- Rule: the seat says what this side does (§3.4), and the form
  derives from it.
- Text, three ways of saying what TODO's Now holds:
  - the seat: "TODO's Now holds what is due while the step is
    open, never the step itself";
  - `TODO.md` and §5.4: "## Now (current plan step)", and "'Now'
    should mirror the current plan step's remaining work";
  - `PLAN.md`: "TODO never repeats the open step", and nothing on
    what Now holds.
- Ending: fixed, `a794f32`: TODO's Now heading says what our seat
  does; §5.4's form stays the run's.

**FINDING-12.** Agreement. Checked. Known.
- Where: `docs/conventions/project-recording/README.md`:203-209;
  `PLAN.md`:110-113.
- Rule: the seat and the step form say one thing about a stopped
  step.
- Text: §2.4, it "resumes where it was instead of starting again"
  and keeps its ticked items. `PLAN.md`: "any stage whose input the
  other step changed runs again", and a ticked item stays "unless
  the other step made it untrue".
- Ending: fixed, `f1c02a7`, to the step form, as lived when the
  refinement resumed.

**FINDING-13.** Agreement. Resting on the reader.
- Where: `docs/conventions/project-recording/README.md`:81-83;
  `PLAN.md`:66-79.
- Rule: `PLAN.md` writes the step's own items first, then checks
  the skills' gates against them; one already met adds nothing.
- Text: the seat, "A step's gate takes the gates of the skills and
  rules it uses … and the rest is written from the form".
- Ending: fixed, `f1c02a7`, to ADR-0057.

**FINDING-14.** Stale lines. Checked.
- Where: `docs/conventions/project-recording/README.md`:196-197.
- True: since `5dbe71f` both legends read "`[!]` blocked (+what
  unblocks) or stopped (+the step first)".
- Text: "`[!]` blocked (+what unblocks it)".
- Ending: fixed, `f1c02a7`.

**FINDING-15.** Agreement. Checked.
- Where: `docs/conventions/project-recording/README.md`:36-37;
  `docs/conventions/agent-arrangement/README.md`:95-97.
- True: our `one-home.md` differs from the container's in its
  scope line (records, manuals, skills, rules, comments and config)
  and in a clause of rule 1 (a convention's subject lives in its
  manual).
- Text: "its examples this repo's", as the only difference.
- Ending: fixed, `f1c02a7` and `a794f32`: four differences named in
  project-recording, agent-arrangement pointing there.

**FINDING-16.** Agreement. Resting on the reader.
- Where: `docs/conventions/project-recording/README.md`:85-87,
  200-201; `delivery/fills/cbc-run-pure-playbook.md`:103-107.
- Text: the seat, "A run keeps its finished steps whole"; §2.4,
  "add a one-line note". The playbook: "the next commit replaces
  the gate with one line".
- Ending: fixed, `f1c02a7`, to the playbook's one closing line.

**FINDING-17.** Agreement. Checked.
- Where: `docs/conventions/project-recording/README.md`:215-217;
  `delivery/fills/cbc-run-pure-playbook.md`:154-162.
- Text: §2.5, the steps "are confirmed at Framing". The playbook
  reads the plan against the framing at Step 2, Identity. Step 1
  has no such item.
- Ending: fixed, `f1c02a7`: confirmed once the problem is framed.

**FINDING-18.** Agreement. Checked.
- Where: `docs/conventions/project-recording/README.md`:678-682;
  `delivery/fills/cbc-run-pure-playbook.md`:21-33;
  `delivery/container/PLAN.md`:3-5, 32-33, 42.
- Text: §9.4, each step keeps "the records expected" and its own
  "Warnings from past runs". The playbook's form has neither: its
  lessons come as "Known already". The PLAN stub keeps `Records:`.
- Ending: fixed, `f1c02a7` and `a794f32`: a playbook step's lessons
  as *Known already*; the stub's form a goal and a gate.

#### Layer 3: the other manuals, the models, the concept

**FINDING-19.** Stale lines. Checked.
- Where: `docs/conventions/agent-arrangement/README.md`:70-77.
- True: our `.claude/` holds four of the run's convention skills
  (`first-time-work` since `d94ec34`), three rules every session
  loads (`foundation-check.md` since `0cae629`), and four rules of
  its own.
- Text: "three of the same convention skills"; "the two rules
  every session loads"; "three rules of its own".
- Ending: fixed, `da7499c`: our `.claude/` named without counts.

**FINDING-20.** Agreement. Checked. Three places.
- Where: `docs/conventions/agent-arrangement/README.md`:49-52;
  `delivery/container/.claude/CLAUDE.md`:27-30;
  `delivery/README.md`:28-32.
- Rule: the pin covers "the skills, rules and shapes under
  `.claude/`, and `docs/concept/`" (`delivered-copies.md` rule 1;
  `docs/conventions/exchange/` §3.2). The decisions log and the
  entry file are the run's own.
- Text: the seat, "everything under `.claude/`"; the entry file
  and the delivery map name skills and rules, not shapes.
- Ending: fixed, `da7499c` and `be2c181`: the run's seat, entry file
  and delivery map name every pinned copy, shapes included.

**FINDING-21.** Agreement and Stale lines. Checked.
- Where: `docs/conventions/commit-messages/README.md`:89-99.
- True: since 2026-10-01, 186 subjects use bare `docs` and 5 use
  `docs(conventions)`; one-area commits use bare `docs`
  (`aba2897`, `ffc6f7c`). `fix(concept)` and `feat(agent)` exist.
  The log holds 1,314 commits.
- Text: "`docs(<area>)` for almost everything … Bare `docs` where
  a commit spans the records generally"; "`feat`/`fix` … all on the
  delivery so far"; "480 commits".
- Ending: fixed, `da7499c`: the habit as the log shows it.

**FINDING-22.** Wiring. Checked. DECISION-2.
- Where: `docs/conventions/exchange/README.md`:20-45.
- Rule: a description lists what derives from it (§3.5 step 1).
  `.claude/rules/working-a-reading.md` carries "practice, under
  the exchange convention".
- Text: the list names four artifacts, not that rule.
- Ending: fixed, `517fc52`, by DECISION-2.

**FINDING-23.** Agreement. Resting on the reader. DECISION-2.
- Where: `docs/conventions/exchange/README.md`:452-455, 530-533.
- Text: "**How the deliverer works a reading**" is sent to
  commit-plan and project-recording, and §6.3 says "the exchange
  says nothing about how". The rule for exactly that stands under
  the exchange.
- Ending: fixed, `517fc52`, by DECISION-2.

**FINDING-24.** Agreement. Resting on the reader.
- Where: `docs/conventions/exchange/README.md`:347-355;
  `delivery/container/TODO.md`:25-39.
- Text: §5.1, the lines live "under one heading kept for them,
  *To the deliverer*". The stub has Now, Next, Later, Known issues,
  and no such heading.
- Ending: fixed, `be2c181`: the stub carries the heading.

**FINDING-25.** Stale lines. Resting on the reader.
- Where: `docs/conventions/first-time-work/README.md`:14.
- True: this repo has lived it twice since it was taken: the
  refinement's manual and the redesign's.
- Text: "Lived three times:". True if it counts only the evidence
  from before the convention.
- Ending: fixed, `a9e8b96`: the manual went. Its uses are
  `approach-drafting`'s now, all four counted (`a0087c5`).

**FINDING-26.** Agreement. Resting on the reader.
- Where: `docs/conventions/first-time-work/README.md`:111-117;
  `.claude/skills/first-time-work/SKILL.md`:18-22.
- Rule: the seats name three differences: where the manual sits,
  what the close makes, who judges it.
- Text: §1 asks the run's second question ("Is it general, or only
  this project's?"). Our skill asks another ("Will a run do it
  too, or only this repo?"), a fourth difference no seat names.
- Ending: fixed, `a0087c5` and `a9e8b96`: one approach serves both
  seats, its one difference marked inline.

**FINDING-27.** Agreement. Checked.
- Where: `docs/conventions/first-time-work/README.md`:140-147;
  `delivery/container/.claude/skills/first-time-work/SKILL.md`:55-65;
  `.claude/skills/first-time-work/SKILL.md`, its close.
- Text: the manual's table has six lasting forms, "A step"
  among them. Both skills offer five, without the step.
- Ending: fixed, `a0087c5` and `a9e8b96`: both skills went. The
  close's forms gave way to the evaluation's endings.

**FINDING-28.** Stale lines. Checked.
- Where: `docs/conventions/refinement/README.md`:176-178.
- True: no kind is called words. Both "words" ideas are Writing
  findings (this file, *Kinds and rounds*).
- Text: "One home and words also need a sweep across files".
- Ending: fixed, `f3060fb`.

**FINDING-29.** Stale lines. Resting on the reader.
- Where: `docs/conventions/refinement/README.md`:301-303.
- True: Wiring adds missing links, and this file fitted it in
  round 1.
- Text: "Adding missing text is the first that may not fit."
- Ending: fixed, `f3060fb`: the known part said, the question kept.

**FINDING-30.** Agreement. Checked.
- Where: `docs/conventions/retrospective/README.md`:73-75.
- True: since `87a9363` the closing item names three places:
  "conventions, the playbook, the concept".
- Text: "'lessons folded back where they came from', which names
  no place and no method."
- Ending: fixed, `da7499c`.

**FINDING-31.** Agreement. Checked. Known.
- Where: `docs/conventions/writing/README.md`:143-147, 153-160,
  197-200; `.claude/rules/writing.md`:28-30.
- Text: the manual defines a coined word "in the project's
  glossary"; our rule, in `ARCHITECTURE.md`'s *The words*. The
  seats name other differences, not this one.
- Ending: fixed, `da7499c`: the writing manual's list names it.

**FINDING-32.** Stale lines. Checked.
- Where: `docs/models/agent.md`:260.
- True: every rule opens with frontmatter since `d5e7e17`. A rule
  is ambient for lack of `paths:` (§10.6 of the same file).
- Text: "`.claude/rules/*.md` without frontmatter".
- Ending: fixed, `da7499c`.

**FINDING-33.** Wiring. Checked for the paths; resting on the
reader for the back-link.
- Where: `docs/conventions/repo-hygiene/README.md`:20-27; the
  three root dotfiles and the container's three.
- Rule: each derived artifact by path
  (`.claude/rules/convention-manual.md`, section 3); each derived
  thing names its description (§3.5 step 2).
- Text: "The three dotfiles at the root of `delivery/container/`".
  No dotfile names the manual.
- Ending: paths fixed, `da7499c`. The back-link declined:
  conventions §3.5 step 2 names how a skill, rule, shape or record
  names its description, and no way for a dotfile.

**FINDING-34.** Wiring. Resting on the reader.
- Where: `concept/` (no list); `ARCHITECTURE.md`:104-131;
  `delivery/fills/cbc-run-pure-playbook.md`:3.
- Rule: a description lists what derives from it (§3.5 step 1).
- Text: the five skills on `concept v1` are listed by name in
  `ARCHITECTURE.md` §2.1 and §2.2. The playbook says "Checked
  against concept v1" and is in neither list.
- Ending: moved to layer 4's work: the list lives in
  `ARCHITECTURE.md`.

**FINDING-35.** Agreement. Resting on the reader. Known.
- Where: the opening statement of each manual.
- Rule: the subject in one sentence (§3.3;
  `.claude/rules/convention-manual.md`, section 1).
- Text: ten break it by this read. More than one sentence:
  agent-arrangement, commit-plan, first-time-work, refinement,
  visual-comparison, writing. One sentence that adds how it works:
  commit-messages, repo-hygiene, retrospective, shapes.
  Project-recording is borderline. The known finding counted nine.
- Ending: fixed, `22b2dca`: eight openings, each the subject in
  one sentence.

**FINDING-36.** Wiring. Checked. DECISION-3.
- Where: about 30 pointers in layers 3, 4 and 6. Among them:
  `docs/conventions/agent-arrangement/README.md`:156, 199, 226,
  231, 262, 335 ("model §10.1"); `docs/models/tiers.md`:89;
  `ARCHITECTURE.md`:243 ("its §3.6"); `PLAN.md`:128, 162, 171,
  205, 210; `TODO.md`:52, 55, 76, 86, 90, 94, 164, 169-173, 228,
  402, 403, 423, 494; `delivery/README.md`:75;
  `delivery/container/.claude/rules/one-home.md`:11-12.
- Rule: a pointer names the file by its path, with the section
  (§3.2), so one grep finds it.
- Text: "project-recording §1", "conventions §3.2", "model
  §10.6". Every number lands on a fitting heading; most name the
  path earlier in the paragraph.
- Narrowed, `f1c02a7`: project-recording's tree pointer moved out of
  the diagram, by path. The rest waits for layers 3, 4 and 6.
- Narrowed, `da7499c`: layer 3's seven pointers by path. Declined:
  commit-plan's "(model §10)", which a dated lesson quotes as it
  stood. The rest waits for layers 4 and 6.

#### Layer 4: `ARCHITECTURE.md`, `README.md`, the records

**FINDING-37.** Stale lines. Checked. DECISION-4.
- Where: `ARCHITECTURE.md`:79-88, 141, 319; `TODO.md`:81-83, 88;
  `.claude/rules/one-home.md`, rule 3.
- True: `docs/conventions/` holds 13 manuals; the 13th is the
  refinement's, on trial.
- Text: "Twelve manuals"; "eleven of the twelve"; "twelve manuals
  and their index"; TODO's "the other eight" and "all twelve";
  one-home's "a phrase for each convention".
- Narrowed by the design change, not ended: `ARCHITECTURE.md`'s
  "eleven" and one-home rule 3 are true again (`a9e8b96`,
  `8e5f093`), and TODO's "the other eight" with them. Left for
  round 1's work: TODO's "all twelve".

**FINDING-38.** Stale lines. Checked.
- Where: `ARCHITECTURE.md`:170-178.
- True: run 4, `safe-reservation-2`, at
  `~/IdeaProjects/cbc-pure-run-4`, born 2026-10-15, through
  Release.
- Text: the runs table ends at run 3.

**FINDING-39.** Agreement. Checked.
- Where: `ARCHITECTURE.md`:233-234.
- Rule: a declined edit "goes, and the need it served goes to the
  run's records" (`docs/conventions/exchange/` §4, step 2).
- Text: "**Declined:** … and the run keeps its edit."

**FINDING-40.** Agreement. Checked.
- Where: `ARCHITECTURE.md`:280-281.
- Rule: four groups ship, each with its masters: method,
  container, a stack practice, the concept
  (`docs/conventions/exchange/` §3.2, §3.3).
- Text: "**The container is the master of every file a run
  receives**".

**FINDING-41.** Agreement. Resting on the reader.
- Where: `ARCHITECTURE.md`:283-285.
- Rule: a change in a derived thing is checked back and decided;
  either side may change (`docs/conventions/conventions/` §3.5
  step 4, §3.6).
- Text: "a rule changed in `delivery/container/` moves its manual
  in the same commit".

**FINDING-42.** Agreement. Resting on the reader.
- Where: `ARCHITECTURE.md`:288-291.
- Rule: a read covers three things: the decisions log, the
  backlog, the diff of every held copy
  (`docs/conventions/exchange/` §6.1). Every read ends with a note
  is §6.6.
- Text: "a reading over two diffs … `docs/conventions/exchange/`
  §6.3 and §6.5".

**FINDING-43.** Agreement. Checked.
- Where: `ARCHITECTURE.md`:353-354.
- Rule: "A note alone, with no files, is still a delivery"
  (`docs/conventions/exchange/` §6.7).
- Text: "**delivery** — files copied whole into a run, with a
  note."

**FINDING-44.** Agreement. Checked.
- Where: `ARCHITECTURE.md`:182-183, 355-357.
- Rule: staging is done "by the reviewer, or by the agent when
  told to" (`docs/conventions/exchange/` §3.1).
- Text: "**staging** — a person copying the delivery"; "Every
  delivery is a person copying files".

**FINDING-45.** Agreement. Checked.
- Where: `ARCHITECTURE.md`:393-395.
- Rule: every skill and rule carries one, shipped or ours; the
  value carries the relation where it is not derivation; records
  carry one in a header comment (`docs/conventions/conventions/`
  §2, §3.5 step 2).
- Text: "**foundation** — the frontmatter line by which a shipped
  file names the description it derives from."

**FINDING-46.** Agreement. Resting on the reader.
- Where: `ARCHITECTURE.md`:398-401.
- Text: "**stage** — one phase of a skill". `PLAN.md`'s step form,
  `working-a-reading.md` and this refinement use it wider.
  `.claude/approaches-on-trial/refinement.md` §3 already names this
  for the refinement's close.

**FINDING-47.** Wiring. Checked.
- Where: `TODO.md`:61.
- True: `docs/conventions/commit-plan/README.md` has §1 and §2.
  §4 is the skill's, `.claude/skills/commit-plan/SKILL.md`.
- Text: "`commit-plan` §4 regroups a set's commits".

**FINDING-48.** Wiring. Uncertain.
- Where: `TODO.md`:574.
- Text: "`concept/02`", for `concept/02-guarantees-and-walls.md`.

**FINDING-49.** Stale lines. Checked.
- Where: `TODO.md`:233-234.
- True: the refinement was `first-time-work`'s first trial here
  (`PLAN.md`), the redesign its second.
- Text: "`first-time-work`'s first trial here".
- Ending: fixed, `0dccf94`.

**FINDING-50.** Stale lines. Checked.
- Where: `TODO.md`:162-184.
- True: the redesign was first-time work here, and closed on
  2026-10-19 with its manual dropped (`c6a7bcc`).
- Text: "Trigger: the next first-time work's close". Whether a
  close that kept nothing fires it is the reviewer's.
- Ending: fixed, `0dccf94`: the item now waits for the first
  evaluation that places a skill or rule.

**FINDING-51.** Stale lines. Checked.
- Where: `TODO.md`:500-507.
- True: `ARCHITECTURE.md` §2.5 names each run's path, since
  `4b9b277`. There are four runs.
- Text: "nothing here names it"; "One run so far".

**FINDING-52.** Stale lines. Checked.
- Where: `TODO.md`:269-271.
- True: the next delivery to run 3 came on 2026-10-18, a note
  alone; the next birth takes the shapes.
- Text: "the next delivery to run 3 is this trigger."

**FINDING-53.** Stale lines. Checked.
- Where: `TODO.md`:433-434.
- True: the manual is 421 lines, the model 466.
- Text: "from about 350 lines to about 600".

**FINDING-54.** Stale lines. Uncertain. DECISION-5.
- Where: `TODO.md`:258, 323, 472-473.
- True: run 4 was born 2026-10-15, by hand from run 3's copies
  and our container.
- Text: "Trigger: before the next birth."; "the next birth's
  Step 3 close."; "a fourth run deriving `.gitignore` by hand."

**FINDING-55.** Agreement. Checked.
- Where: `TODO.md`:27.
- Rule: our `PLAN.md` holds one step, and no upcoming ones
  (project-recording, the deliverer's seat).
- Text: "## Next (upcoming steps — assign each to a step when
  triaged)".

**FINDING-56.** Agreement. Checked.
- Where: `devlog/README.md`:7; `CLAUDE.md`:20.
- Rule: a TODO item's story goes in the devlog when the item is
  added, not at the session's end
  (`docs/conventions/project-recording/` §5.4).
- Text: "2–5 minutes at the end of each session."; "Session
  ending, or a dead end hit".

**FINDING-57.** Wiring. Uncertain.
- Where: `README.md`:51-56; `delivery/container/README.md`:3, 9,
  13-14, 20-26.
- Rule: "Never a relative link" (§3.2).
- Text: "[PLAN.md](PLAN.md)", "[docs/concept/](docs/concept/)".
  Each file sits at its repo's root, so each target is the root
  path, once the stub is in a run.

**FINDING-58.** Wiring. Checked for `PLAN.md` and `TODO.md`;
resting on the reader for the rest. Known.
- Where: headers holding a form, with no `foundation:` line:
  - ours: `PLAN.md`:3-8, 20-22; `TODO.md`:3-23;
    `CHANGELOG.md`:9-20; `.claude/decisions.md`:3-17;
    `CLAUDE.md`:9-13;
  - the run's: `delivery/container/PLAN.md`:3-13, `TODO.md`:3-23,
    `devlog/devlog.md`:3-10, `.claude/decisions.md`:3-27,
    `CHANGELOG.md`:9-16, `.claude/CLAUDE.md`:34-38,
    `docs/adr/0001-record-architecture-decisions.md`:39-40;
    `delivery/fills/cbc-run-pure-playbook.md`:1-8.
- Rule: §3.5 step 2. Some forms are listed by two manuals:
  first-time-work lists the step form's opening item,
  agent-arrangement both entry files and both logs.

#### Layer 5: our agent setup

**FINDING-59.** Agreement. Checked.
- Where: `CLAUDE.md`:21.
- Rule: our `CHANGELOG.md` versions the concept, and "a
  convention's change, or the delivery's, is none" (its comment;
  project-recording, the deliverer's seat).
- Text: "| Shipped something users can see | What changed, for
  users | CHANGELOG.md |".

**FINDING-60.** Agreement. Checked. DECISION-6.
- Where: `.claude/skills/commit-messages/SKILL.md`:129-134;
  `.claude/skills/commit-plan/SKILL.md`:179-191;
  `.claude/skills/visual-comparison/SKILL.md`:30, 102-154.
- Rule: a decision is cited "`CBC ADR-nnnn` in one that ships,
  `ADR-nnnn` in one that stays here"
  (`docs/conventions/conventions/` §2). The three manuals say ours
  is identical to the container's.
- Text: 22 `CBC ADR` citations in files that stay here.
- Ending: fixed, `2bfe201`, by DECISION-6's line in conventions
  §2; the three skills are right as they are.

**FINDING-61.** Agreement. Resting on the reader.
- Where: `.claude/skills/first-time-work/SKILL.md`:16, 24, 37, 45;
  the container's `retrospective` and `apply-retrospective`, the
  same form.
- Rule: "A skill's phases are stages … `## Stage 1 — …`"
  (`docs/conventions/conventions/` §2).
- Text: "## 0. Is it first-time work?", "## 1. Open".

**FINDING-62.** Wiring. Checked.
- Where: `.claude/skills/first-time-work/SKILL.md`:54-55.
- Text: "each in §2's form", bare. It lands on the skill's own §2,
  Work; it means `docs/conventions/conventions/` §2.
- Ending: fixed, `a0087c5`: the skill went.

**FINDING-63.** Wiring. Checked.
- Where: `.claude/rules/foundation-check.md`:37-38.
- Text: "The reviewer decides each (§3.6)", bare. The rule has no
  §3.6; it means `docs/conventions/conventions/` §3.6.

**FINDING-64.** Agreement. Resting on the reader.
- Where: `.claude/rules/convention-manual.md`:66-68.
- Rule: its own section 5, since `d0628b2`: each numbered section
  holds one subject.
- Text: *What this does not fix*: "how the body is divided".

**FINDING-65.** Agreement. Checked.
- Where: `.claude/skills/exchange-deliver/SKILL.md`:154-155.
- Rule: "At birth, every file of each group"
  (`docs/conventions/exchange/` §3.2). Step 2.2 copies only
  `.claude/` skills, rules and shapes.
- Text: "Birth: the same overlay as 2.2 into the newborn's root".

**FINDING-66.** Stale lines. Checked. Both seats.
- Where: `.claude/skills/visual-comparison/SKILL.md`:67-68; the
  container's copy, the same line.
- True: the method ran a third time on 2026-09-30, for the
  codemap, and there the render changed no verdict.
- Text: "Both times this method has run, the render changed a
  verdict".

**FINDING-67.** Stale lines. Resting on the reader. Both seats.
- Where: `.claude/skills/commit-plan/SKILL.md`:91-93; the
  container's copy, the same line.
- True: ADR-0052 decision 5 ended the exposed split; no living
  text uses the word but this.
- Text: "a skill or rule corrected, a convention exposed".

#### Layer 6: `delivery/`, what ships

**FINDING-68.** Agreement. Checked.
- Where: `delivery/container/.claude/rules/delivered-copies.md`:108-113.
- Rule: register in the decisions log, "Then the staging goes"
  (`docs/conventions/exchange/` §4, step 5).
- Text: step 6 removes the staging; step 7 writes the entry.

**FINDING-69.** Agreement. Checked.
- Where: `delivery/container/.claude/rules/delivered-copies.md`:74-79.
- Rule: verdicts are Taken, Declined, Held
  (`docs/conventions/exchange/` §6.5).
- Text: "takes, reshapes or declines each hunk".

**FINDING-70.** Agreement. Resting on the reader.
- Where: `delivery/container/.claude/rules/delivered-copies.md`:93-95.
- Rule: "The diff of each held copy against the pin"
  (`docs/conventions/exchange/` §4, step 2).
- Text: "Diff each held copy against the last delivery entry's
  commit". A run commit, whose bytes equal the pin's; the rule's
  may be the better one.

**FINDING-71.** Agreement. Checked.
- Where: `delivery/container/.claude/rules/shapes-lifecycle.md`:91-95.
- Rule: a run offers its shape by a backlog line, and the reading
  reads it "when a backlog line offers them"
  (`docs/conventions/shapes/`, the run's seat, §4.3;
  `docs/conventions/exchange/` §6.2).
- Text: "The deliverer reads this project's shapes when it reads
  the repository." No backlog line.

**FINDING-72.** Stale lines. Checked.
- Where: `delivery/README.md`:82-86.
- True: since `0a7890c` the playbook has Steps N-2 and N-1, which
  run `retrospective` and `apply-retrospective`.
- Text: "whose middles are the pipeline, cbc-framing to
  infra-establish to cbc-bootstrap to cbc-slice".

**FINDING-73.** Agreement. Checked.
- Where: `delivery/README.md`:25-32.
- Rule: the decisions log went once, at birth
  (`docs/conventions/exchange/` §3.2).
- Text: the three ways a file lands leave out `decisions.md`.

**FINDING-74.** Stale lines. Resting on the reader.
- Where: `delivery/fills/cbc-run-pure-playbook.md`:12-13;
  `delivery/installs/pure-seed.md`:116, 119, 227.
- True: the playbook changed twice after v8 (`f2c489c`,
  `5dbe71f`). After `20dbd61`, v7 gained a note "updated here".
- Text: "Playbook version: v8 (2026-10-16, provisional; run 3's
  retrospective taken, ADR-0055)". No rule says when a version
  moves.

**FINDING-75.** Stale lines. Uncertain.
- Where: `delivery/installs/pure-seed.md`:222-223.
- True: one pin also covers the container's six skills and four
  rules (`delivered-copies.md` rule 1).
- Text: "Every bundle copy byte-identical to its master at the
  subject's pin: the concept chapters, the five skills, the four
  shapes." "Bundle copy" is defined nowhere.

**FINDING-76.** Wiring. Checked.
- Where: `delivery/container/.claude/skills/retrospective/SKILL.md`:95-97.
- True: the skill's section 4 has no item for fixing a line that
  says "now". Wrong since the file was made, `fa7fd41`.
- Text: "The exceptions are in section 4: … and lines that say
  'now' about something no longer true."

**FINDING-77.** Agreement. Resting on the reader.
- Where: `delivery/container/.claude/skills/retrospective/SKILL.md`:113-116.
- Rule: the log is "append-only and dated"
  (`docs/conventions/agent-arrangement/` §3.4; the stub,
  "Append-only, newest last").
- Text: "The decisions log gets a 'rules in force now' list on
  top".

**FINDING-78.** Agreement. Checked. Both seats.
- Where: `delivery/container/.claude/skills/commit-messages/SKILL.md`:103-107;
  ours, the same.
- Rule: the arrangement is a closed list, `CLAUDE.md` and
  `.claude/`; "`COMMIT-PLAN.md` is commit-plan's artifact"
  (`docs/conventions/agent-arrangement/` §1).
- Text: "`CLAUDE.md`, `.claude/` and `COMMIT-PLAN.md` are the
  working arrangement".

**FINDING-79.** Agreement. Checked for `visual-comparison`;
uncertain for the method and the stack.
- Where: `delivery/container/.claude/skills/visual-comparison/SKILL.md`:30,
  101-102, 106, 111, 129, 134;
  `delivery/method/.claude/skills/cbc-framing/SKILL.md`:188;
  `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`:205;
  `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`:152.
- Rule: "Cite no decision mid-sentence", a footer headed
  *Decisions* (`docs/conventions/conventions/` §2). Whether §2
  binds a method or stack skill is not said.
- Text: "In CBC ADR-0028 the table was …"; "(CBC ADR-0027
  decision 2)".

**FINDING-80.** Agreement. Resting on the reader.
- Where: `delivery/container/.claude/CLAUDE.md`:14-30, 67-69.
- Rule: two kinds of content at birth, what the project is and
  the records table; the rest arrives when true
  (`docs/conventions/agent-arrangement/` §2.4).
- Text: at birth, "## Correctness by construction", a stance, and
  "## Local rules" with one rule.

**FINDING-81.** Agreement. Resting on the reader.
- Where: `delivery/method/.claude/skills/cbc-framing/SKILL.md`:202-224.
- Rule: what changes often belongs in PLAN and is linked from the
  README (`docs/conventions/project-recording/` §7.4, §7.6).
- Text: "an honest status line"; "a slice close moves the status
  line".

**FINDING-82.** Agreement. Resting on the reader.
- Where: `delivery/container/README.md`:3-7;
  `delivery/method/.claude/skills/cbc-slice/SKILL.md`:9-12.
- Rule: the test is "the *demonstration that the wall exists*";
  closed means the wall stands and the proof exists
  (`concept/04-cbc-slice.md`, *The proof standard*).
- Text: "closed by a test that creates its adversity"; "the
  adversity-creating test exists and passes." The skill's gates
  agree; these two openings state the test alone.

**FINDING-83.** Agreement. Resting on the reader.
- Where: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`:162-163;
  `references/spring-boot-walkthrough.md`:36-40.
- Rule: an overlay is "appended … below the marked line each base
  file carries" (`docs/conventions/repo-hygiene/` §2, §3).
- Text: "merge plumbing files … (.gitignore grown, .gitattributes
  merged …)". No marker named; `.editorconfig` not mentioned.

**FINDING-84.** Agreement. Checked.
- Where: `delivery/method/.claude/shapes/kill.md`:59-62.
- Rule: a shipped shape's illustration is from the method's
  worked example, "never a run's" (`docs/conventions/shapes/`
  §4.2).
- Text: "\"KILL-1's death, the racers our own instances\"", run
  3's words (`d7f1e23`), in neither worked example.

**FINDING-85.** Stale lines. Checked.
- Where: `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`:113;
  `…/infra-establish/references/establishment-walk.md`:153;
  `…/cbc-bootstrap/SKILL.md`:210.
- True: the kit became the container on 2026-09-19 (`d148ccb`).
- Text: "every kit-born project"; "The kit's README stub".

**FINDING-86.** Stale lines. Checked.
- Where: `delivery/spring-postgres/.claude/skills/infra-establish/templates/verify-database-model.sql`:7.
- True: the walk's parts are stages since `f169d4a`, which missed
  this template.
- Text: "(walk step 5)".

**FINDING-87.** Stale lines. Checked.
- Where: `delivery/method/.claude/skills/cbc-slice/SKILL.md`:68-72;
  `…/cbc-slice/references/cbc-slice-workflow.md`:74-78.
- True: no seed example ships; the phrase came in the archive
  import (`edecd0e`). Stage 0 refuses to start with no framing.
- Text: "(the seed-example case)"; "The seed example's
  invariant".

**FINDING-88.** Stale lines. Checked; resting on the reader that
it is stale, not only unclear.
- Where: `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`:74;
  `…/references/spring-harness-reference.md`:11, 47, 163, 209, 295,
  444, 484; `…/references/spring-boot-walkthrough.md`:41.
- True: the walkthrough's sections are the five steps of Stage 3's
  plan. The skill's Stage 4 is execute, its Stage 5 certify.
- Text: "the stack walkthrough's stage 5"; "(walkthrough, stage
  4)".

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
