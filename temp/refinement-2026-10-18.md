<!-- The refinement of this repo, opened 2026-10-18 on
     refinement-2026-10-18. Data only: how this file is made is
     docs/conventions/refinement/ §2. It grows a part at each
     stage, and goes at the close. -->

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
