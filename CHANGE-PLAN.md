# Change-plan: the semi-pure delivery

## Summary — the state after all commits

The seed manual has one optional delivery, the semi-pure step: a
sixth commit on `birth-seed` that writes the two fills over the
kit's entry stubs — CLAUDE.md and README.md — headless from the
title line down, `<working-name>` filled with the placeholder
directory name. Everything else about the birth stays pure: main
at hygiene, the files untracked, the agent committing them. Run 3
runs with the step on. ADR-0019 records the re-entry ADR-0016
foresaw ("if the pure runs show derivation inadequate"): two runs
derived the entry files unaided and neither produced the
pre-framing guard or the skills' pin stance, so what the templates
hold is delivered from now on, and the reading of a semi-pure run
measures what the agent changes in delivered entry files rather
than what it derives. The starter doc's contract paragraph names
the one non-additive act and why it widens nothing; the fills'
Use lines, ARCHITECTURE, CHANGELOG and the TODO item catch up.

## Commits

**1. `docs(adr): propose ADR-0019, the entry files ship filled`**
Decision-first. Context: run 2's Step 0 reading (both runs missed
the guard and the pin stance; the kill-or-justify test the TODO
item set is answered on the justify side); ADR-0016's own re-entry
clause; ADR-0015's whole-copy, which is what lets the overwrite
assume nothing of the stub. Options: keep deriving; deliver the
CLAUDE body only; deliver both — taken. One commit for both files
on the receipt branch, where the commit split does not bind.
ADR-0016 gets a one-line "amended by" pointer, as ADR-0014 got
from ADR-0015. Lands Proposed, flips in step 4.

**2. `feat(installs): the semi-pure step — entry files from the fills`**
pure-seed.md: an optional step between the deliveries and the
return to main — cut each fill from its title line, fill the name,
write over the stub, one commit with the bundle pin; the prompt's
situation sentence gains a clause naming the delivered entry
files; the checkable list and the excluded list say what changes
when the step is on. Material-first: the cut-and-fill commands are
proven on a scratch repo against the real fills at this boundary
before the manual states them. Header gains its eighth revision
line.

**3. `docs(starter): the fills' rows, Use lines, and the contract carry delivery`**
starter/README.md: the two fills rows say delivered by the
semi-pure step; the contract paragraph's "no non-additive act"
and "CLAUDE.md does not return" become the true statement — one
act, replacing two stubs whole with fills that carry the kit's
half verbatim at the pin, assuming nothing of the stub, so no
surface enters the contract. The two fills' Use lines; ARCHITECTURE's
executions sentence and codemap row ("parked" no longer).

**4. `docs: records catch up, ADR-0019 accepted`**
CHANGELOG Unreleased (the Added lines' "parked" state, a Changed
entry); TODO — the semi-pure item closed into the ADR, the
pure-seed and gates items told run 3 is semi-pure; ADR-0019 flips.

## Decisions taken inside this plan

- **One manual, one switch.** The step is optional inside
  pure-seed.md, not a second manual: the difference between the
  two shapes is one commit, and one file keeps it structural. The
  manual's name stays — "pure" names the seed's nature (delivers,
  decides nothing); the switch delivers two more texts.
- **Both files, one commit.** The user's design. CLAUDE.md is
  agent-side and README project-side, but the commit lands on the
  receipt branch, never merged — the split rule governs the
  newborn's line, and the kit-remainder commit straddles there
  already.
- **Headless, name filled, nothing else.** The seed cuts from the
  title line and fills `<working-name>` with the placeholder
  directory name; no other placeholder exists in either fill.
- **Run 3 is semi-pure.** The reading's object changes with it:
  what the agent edits in the delivered entry files at Step 0,
  and whether the guard holds through Framing.
- **The pre-framing guard leaves the pure-run measurement.** The
  three-way reading item said the does-it-invent-protections
  measurement lived in pure runs; with the guard delivered, that
  measurement ends with run 2. Recorded in step 4.
