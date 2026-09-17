# Change-plan: the kit comes here

## Summary — the state after all commits

`starter/kit/` holds this repo's copy of the handbook's kit at
`ba7eaa4`, at their path names: thirteen files byte-identical to
the master, three carrying a stated delta, and one line changed in
a fourth. `starter/fills/` is gone — a fill was text written into a
file the kit had already placed, and once we ship the file there is
nothing to write into.

`starter/README.md` carries the delta list beside the set rather
than inside it: what departs from the master, why, and what the pin
claims — derived from `ba7eaa4`, with this delta, last read on this
date (ADR-0023 decision 8). Its contract section is gone; there is
no surface for the handbook to hold still when the shapes are ours.

`pure-seed.md` no longer runs another repo's bash in our shell. Its
step 2 copies `starter/kit/`, its step 4 dissolves — the entry
files arrive in the kit rather than being written over stubs — and
the `sed` that moved `CLAUDE.md` to `.claude/` is gone, because our
kit ships it there.

What this gives us that we did not have: a run born from one place,
holding one pin, updated by one procedure. And an adaptation layer
that is named and listed instead of living inside an install
manual's fourth step.

## Commits

**1. `docs(starter): the kit lands verbatim, thirteen files`**
The untouched thirteen, copied from the handbook at `ba7eaa4` into
`starter/kit/` at their own paths: the four convention skills, the
three hygiene dotfiles, and the record stubs that need nothing from
us — `TODO.md`, `devlog/devlog.md`, `CHANGELOG.md`,
`ARCHITECTURE.md`, `docs/adr/0001`, `.claude/decisions.md`. Its own
step because it is the only one whose correctness is a byte
comparison, and it must be provable as that before anything
diverges from it.

**2. `docs(starter): the three flavoured files, and fills retires`**
`claude-md-template.md` becomes `starter/kit/.claude/CLAUDE.md`,
`readme-md-template.md` becomes `starter/kit/README.md`, and the
playbook's steps land inside `starter/kit/PLAN.md`'s markers. The
provenance headers the fills carried do not travel into the kit — a
shipped file carries instruction only (ADR-0022) — so they become
the raw material of step 3. `starter/fills/` is deleted and
`.claude/decisions.md`'s birth entry gains the second upstream. One
step because the three files and the retired directory are one
change: revert it and the fills are back, whole.

**3. `docs(starter): the delta list, and what the pin claims`**
`starter/README.md` gains the section: the pin, one line per
departure with its reason, the ceiling from ADR-0024, and the
pin's claim in ADR-0023's words. Kept beside the set and never in
it.

**4. `docs(starter): the seed copies our kit`** *(provisional)*
`pure-seed.md` loses its step 2's pointer to the handbook's manual
and its step 4 entirely. Provisional: what the seed becomes is
visible only once the kit is in place, and the step count may
change.

**5. `docs(starter): the delivery docs lose the contract`**
*(provisional)*
`starter/README.md`'s contract section and its two-kinds-of-delivery
table, and `bundle-update.md`, made true for a delivery that
carries its own container. Provisional for the same reason.

**6. `docs: the shape after the kit`**
`ARCHITECTURE.md` — the kit as a component, a codemap row for
`starter/kit/`, the pinning invariant widened — and `README.md` if
the front door no longer describes what this repo ships.

**7. `docs(adr): accept 0023 and 0024, and close Step 8`**
The set's final records commit: both ADRs flip to Accepted, PLAN
Step 8's gate items close naming the commits that closed them, and
anything the work discovered is triaged into TODO.

## Decisions taken inside this plan

**The delta list lives in `starter/README.md`, not in a file of its
own and not in the kit.** The handbook's own rule, which we took
from their repo-shapes draft: only the set is copied, and anything
*about* the set is kept beside it. A delta list inside `starter/kit/`
would travel to every run, which has no use for it.

**Our own `.claude/skills/` does not move.** This repo goes on
taking its four convention copies from the handbook directly, with
the registry and procedure it already runs. Only the bundle gains a
kit. The consequence is two copies of the same four files here, both
pinned to `ba7eaa4` and therefore identical to each other; step 1's
byte comparison is what keeps that true, and a divergence between
them is a finding, not a drift to absorb.

**The order is material-first from step 1 to 5, decision-first at
6 and 7.** The two ADRs are already committed Proposed, so the
decisions that could be made in conversation are made; what is left
— what the seed becomes, what survives in the delivery docs — is
only visible in the material. Steps 4 and 5 are provisional and
will be refined at their boundaries, which is planned refinement,
not divergence.

**No CHANGELOG entry.** It is the concept-version log (ADR-0003) and
the mental layer does not change here.
