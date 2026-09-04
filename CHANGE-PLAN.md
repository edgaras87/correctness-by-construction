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
The merge itself: a new bundle file with the CbC section, built
from the newborn's derived section (as of aa1e17e, paths per the
docs/ layout) plus what the snippet had and the derivation missed —
judged per ADR-0013's moment-of-need rule, so a miss that lives in
a skill may stay there. Both baseline headers annotated: comparison
consumed. Starter README table row added here (one step with its
listing). Provisional in wording — the merge shapes the file.

**4. `docs(starter): add the birth fills as templates`**
The problem-agnostic stub fills as bundle templates, drafted from
the newborn's e7a13f9: README purpose paragraph, PLAN title,
ADR-0001, ARCHITECTURE overview, CHANGELOG deferral, TODO
deferrals, devlog birth entry, decisions.md bundle entry.
Variables: name, date, the two pins. Table row rides along.
Provisional — may fold into step 3 if the material is small.

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
