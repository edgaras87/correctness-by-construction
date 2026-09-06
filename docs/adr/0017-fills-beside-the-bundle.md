# 0017. Fills beside the bundle

Date: 2026-09-07
Status: Proposed (opened inside the fills-layout change set per
change-plans §4; flips to Accepted at the set's final records
commit if no boundary contradicts it)

## Context

ADR-0010 drew one structural line inside `starter/`: nothing under
`bundle/` stays home, nothing outside it ships. That held while the
bundle was skills and a scenario. It stopped describing the
contents when the pure seed arrived (ADR-0016): the playbook is
never copied as a file — the seed writes its steps into the kit's
PLAN stub between the STEPS markers, and the newborn edits them in
place from its first session. Then two entry-file templates were
composed and parked in `bundle/` (2026-09-05 and 2026-09-06), each
meant to be written over a kit stub — CLAUDE.md, README.md — whole
from the title line down, headless, the newborn's own from then on.

Three of the bundle's seven members were now text that lands
inside a kit file and is owned by the newborn afterwards; four were
directories the newborn holds as pinned copies, re-copied at a new
pin and never edited (`starter/README.md`'s authoritative-vs-pinned
rule). The copy table said "not copied as a file" three times.
The user named the defect (2026-09-07): the templates do not
travel as documents; they are copied as contents into documents the
kit already put there. The playbook is the same act.

## Options considered

1. **Leave them in `bundle/`, the copy table explaining each.**
   Rejected: the table was already the only thing holding the
   distinction, three rows of prose against a one-line structural
   rule — the file-level ambiguity ADR-0010 was made to remove,
   reintroduced by kind instead of by file.
2. **Move the two templates only; the playbook stays** (it is a
   derived execution with a concept pin, ADR-0011 names its path).
   Rejected, the user's call: a rule true of two members out of
   three is not a rule; the playbook is written into PLAN exactly
   as the templates are written over their stubs.
3. **A third directory, `starter/fills/`, for all three** — chosen.

Name: `fills/`, the word this repo already uses for text that goes
into a kit file (the seed's fill variables; the retired
birth-fills). Not `templates/`: the skills' own `templates/`
directories are copy-and-fill masters that land as new files at a
path the walkthrough names — a different act, and the collision
would be inside the same tree.

## Decision

`starter/` has three directories, one rule each:

- `bundle/` — what the newborn keeps as **pinned copies**: the
  five skills with their references and templates. Copied whole
  to a path the kit does not claim; changed only by copying anew
  at a new pin; a run's surprise comes back as harvest (ADR-0007).
  `concept/` at the root ships under the same rule.
- `fills/` — text the seed **writes into the kit's own files**,
  which the newborn then owns: `cbc-run-pure-playbook.md` (its
  steps into PLAN's STEPS region), `claude-md-template.md` and
  `readme-md-template.md` (their bodies over the kit's two stubs,
  headless from the title line down, ADR-0015). No pin travels
  with a fill beyond the "Steps from" line and the seed commit's
  subject; the newborn edits the text from its first session and
  nothing re-copies it.
- `installs/` — the manuals. Stays home, with `starter/README.md`.

ADR-0010's structural sentence is amended to the three-way form:
nothing under `bundle/` or `fills/` stays home; `bundle/` lands as
files, `fills/` lands as text inside kit files; everything else
under `starter/` stays. Its other decisions stand.

What this ADR does not decide: whether the two templates are ever
delivered. The pure seed writes only the playbook (ADR-0016); the
templates stay parked. A semi-pure install that writes them over
the kit's stubs is a delivery decision — it reopens the overlay's
"no non-additive act" and CLAUDE.md's absence from the assumed
surfaces (starter/README.md's contract) — and gets its own ADR
when designed. This one only puts the three where that decision
can find them.

## Consequences

Good: the structural rule is again readable from the tree — a
correct copy of `bundle/` is a directory diff; the three fills sit
together as the only things a seed writes into kit files; the
semi-pure design starts from a layout that already says what a
fill is.
Bad: paths in historical records go stale — accepted, history is
not rewritten; this ADR carries the mapping
(`starter/bundle/{cbc-run-pure-playbook,claude-md-template,readme-md-template}.md`
→ `starter/fills/`). The pure seed manual's playbook path and the
two frozen baselines' forward pointers change with the move.
