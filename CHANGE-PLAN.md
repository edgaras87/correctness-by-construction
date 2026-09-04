# Change-plan: absorb the assembly rewrite into the bundle

## Summary — the state after all commits

The bundle ships assembled text instead of expecting a per-birth
derivation. The master scenario is the assembly text the first walk
produced; a new bundle file carries the shipped CLAUDE.md CbC
section, merged once from the walk's derivation and the blind
snippet; the birth fills exist in the bundle as templates; the pin
findings the newborn reported are fixed in the masters; and
ADR-0014 records why the ADR-0012 experiment closed. What stays at
trial close, deliberately: the install-manual rewrite, the rebuild
script, and whether the scenario file itself keeps shipping.

## Commits

**1. `docs(starter): rewrite the birth scenario as assembly`**
Carry the newborn's revised copy (cbc-newborn 3b27b46 + 260a39e)
into starter/bundle/birth-scenario.md, re-headered as the master:
provenance line, master paths, the trial-protocol relation kept.
Decision-first anchor — every later step implements what this text
already says.

**2. `docs(adr): add ADR-0014 — the bundle ships assembled text`**
Status: Proposed. Closes the ADR-0012 experiment: the derivation
ran once, served as a review of the concept's clarity, and its
product is merged and frozen — no per-birth derivation. Records
what the comparison found (the misses, the novel mapping) and the
baselines' fate. Proposed until the merge is seen; flips in step 6.

**3. `docs(starter): add the shipped CLAUDE.md text to the bundle`**
The merge, slim by design: fragments for the kit stub — a short
CbC section (concept pointer, the ordering in one parenthetical,
the pre-framing guard), the Method conventions row, the stance
lines, the local-rule lines. Dropped from the derivation: the
concept summary (a summary is a lossy copy; the concept is the
master) and the step-routing rows (PLAN carries the mapping via
the playbook, and hardcoded step numbers lie once framing
renumbers). From the snippet only the pre-framing guard enters —
the registry rule is verified already living in cbc-slice, the
sign-off gates in both skills. ADR-0014's Decision amended to
this shape (it is Proposed, gathering boundary evidence), the
scenario's step-3 fragment list trimmed to match, both baseline
headers annotated, README row and contract paragraph riding
along.

**4. `docs(starter): add the birth fills as templates`**
The problem-agnostic stub fills as bundle templates, drafted from
the newborn's e7a13f9: README purpose paragraph, PLAN title,
ADR-0001, ARCHITECTURE overview, CHANGELOG deferral, TODO
deferrals, devlog birth entry, decisions.md bundle entry.
Variables: name, date, the two pins. Table row rides along.
Absorbs the records-carry-the-method mapping from the derivation:
each record's fill carries the method's reading of that record
(README = promise, ARCHITECTURE Invariants = guarantee inventory,
ADRs = refusals, PLAN cut by invariant) — the rule riding in the
record it governs, the kit's records-teach-themselves model,
instead of a block in CLAUDE.md.

**5. `docs: fix what the walk falsified in the masters`**
cbc-run-playbook.md's Step 0 comment still says concept/ (the
bundle now lands under docs/); the concept chapters' headers call
each copy authoritative — true here, false in a newborn — so the
header gains the pinned-copy variant. Starter README's copy table
updated to the docs/ destinations and the only-the-chosen-playbook
line.

**6. `docs: record the bundle's new shape`**
CHANGELOG entry (the starter is shipped surface), ADR-0014 flipped
to Accepted — the final records commit, once the merge and the
templates are the last evidence in.

## Decisions taken inside this plan

- The install manual (starter/installs/cbc.md) is NOT touched. The
  scenario's own header keeps it the procedure of record until the
  trial-closing ADR, which rewrites it around assembly and writes
  the rebuild script. Mid-set staleness against the new scenario is
  accepted and already flagged by the scenario header.
- The scenario file keeps shipping into newborns for now; "the
  manual is the procedure and the script is the proof" is the
  closing ADR's move, not this set's.
- The baselines (snippet, walk-1 derivation capture) are annotated,
  not deleted, and stay blind to newborns — they are the record of
  the comparison, and history is not cleaned up.
- ADR-0014 is a new ADR, not an edit to ADR-0012: the experiment
  ADR stands as written; its close is a new decision with new
  evidence.
- Revised at the step-3 boundary (2026-09-04, user review): the
  first staged merge froze the derivation on the authority of
  "it won the comparison" without re-auditing it as CLAUDE.md
  text. Against the stub's own rules it restated the concept,
  hardcoded plan step numbers, and imported facts whose homes are
  the skills. Slimmed; the mapping moved to the fills.
