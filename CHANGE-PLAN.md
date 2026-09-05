# Change-plan: template-whole CLAUDE.md, absorbing the reply

## Summary — the state after all commits

The bundle ships a complete CLAUDE.md template — one file, composed
here from the kit's slim entry file (@ handbook c670fe5: orientation,
records table, guard comment) plus this method's text, filled and
copied whole at birth like every other bundle file. The fragments
file (claude-md-cbc.md) retires; ADR-0015 records the mechanism
change against ADR-0014, whose decision (shipped text, merged once,
no derivation) stands. The install manual's sed keeps the STEPS
markers, matching the canonical answer. The playbook's vendored kit
steps sit at c670fe5 (default.md v2, Framing's projection gate item),
and every stale starter/kit/playbooks/ path is swept to the new home.
The scenario says copy, not merge; the starter README's contract
paragraph names the narrowed assumed surfaces (STEPS region with its
markers, the step/gate idiom, default.md as vendor base — playbooks/
is no kit directory, and CLAUDE.md never entered). After the close,
the next birth runs assembly from these masters, kit pinned at
c670fe5.

## Commits

**1. `fix(starter): install sed keeps the STEPS markers`**
Our installs/cbc.md sed still deletes the whole STEPS region,
markers included, and its checkable-birth line says "no marker
left" — both contradict the handbook's ruling (their 39ddf48: the
markers stay, only what sits between them is swapped, keeping the
region re-runnable). Independent defect fix, first so nothing later
builds on the wrong idiom.

**2. `docs(adr): propose ADR-0015, template ships whole`**
Decision-first — the mechanism was decided in conversation
(2026-09-04, while drafting the handoff) and the reply confirmed the
ground. ADR-0015 amends ADR-0014's delivery only: no merge into the
kit's stub, no slot anchors, a complete template copied whole;
CLAUDE.md stays out of the assumed-surface contract. Context carries
the reply's shape (0032 removed the sections, 0034 the list — the
kit content the template tracks is ~41 lines). ADR-0014 gets a
one-line status pointer. Lands Proposed, flips in step 6.

**3. `feat(starter): re-vendor kit steps at c670fe5`**
cbc-run-playbook.md's vendored steps (0, 1, N) refresh from
default.md v2 — taking the Framing gate item "every step that makes
something true the outside should see names its projection" — and
the vendor headers re-pin. The path sweep ADR-0031 names rides
here, at the refresh it predicted: starter/kit/playbooks/ →
starter/playbooks/ wherever a live reference points (historical ADR
bodies stay as written).

**4. `feat(starter): ship the whole CLAUDE.md template`**
The new bundle file: the kit's entry file at c670fe5 (orientation
fill, records table with the change-plans row, the guard comment)
with the method's text composed in — cbc-section, stance lines,
local rules — and the fill variables the other fills use.
claude-md-cbc.md is deleted; its merge verdicts are history's.
Audit while composing: no handbook ADR citations in the template
body (their new stub rule — a stub cites the project's own sequence
or nothing); the Method row does not return (no list exists; the
registry is the list, and the decisions-bundle-entry fill already
names the method there). Provenance header cites the kit pin and
agent-arrangement. Wording is material-first — the exact shape
emerges at the compose and is reviewed at the boundary.

**5. `docs(starter): scenario and README carry whole-copy`**
The scenario's assembly step rewords: the template lands whole,
copy not merge; the playbook-copy decision below lands in its
step 2/3 text and the fills' "Steps from" line. The starter README
contract paragraph reverts from three claimed surfaces to the
narrowed contract, and the copy table's claude-md-cbc.md row
becomes the template's row.

**6. `docs: records catch up on the reshape`**
CHANGELOG (Unreleased: template-whole delivery, marker-keeping
install, re-vendored steps), TODO (Now item trimmed to what
remains: the next birth), ADR-0015 flips to Accepted with the
boundaries as evidence.

## Decisions taken inside this plan

- **The newborn holds no playbook copy.** Adopting the handbook's
  model (ADR-0031): the steps live in PLAN's STEPS region, plus a
  "Steps from" line naming cbc-run.md, its version and the bundle
  pin; docs/playbooks/ is not seeded. The copy duplicated a pinned
  master it never edits — retro folds into the master, settled
  their side in our direction. The concept copy is not the same
  case and stays: docs/concept/ is read throughout the run; the
  playbook, once mapped, is not. Cost accepted: the newborn is
  less self-contained — reading the procedure's provenance needs
  the pinned master.
- **claude-md-cbc.md is replaced, not kept beside the template.**
  One master for shipped CLAUDE.md text; keeping both would make
  the compose a live dependency inside our own repo. History
  keeps the fragments and their merge verdicts.
- **The Method row dies with the Conventions list.** Nothing
  replaces it in the entry file; the registry entry (birth fills)
  is the one list, which is ADR-0034's point.
- **temp/handbook-handoff-2026-09-04.md is deleted** (untracked,
  gitignored; no commit). Both repos' reply list asks it; delivery
  and reply are done.
