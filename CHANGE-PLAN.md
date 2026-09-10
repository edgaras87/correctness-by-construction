# Change-plan: harvest run 3's framing lessons into cbc-framing

## Summary — the state after all commits

The bundle master of cbc-framing carries what run 3's Step 1 taught
it, in the run's wording, each change logged as a dated harvest
line in the header of the file it touched (ADR-0007). The registry
template opens in project voice — no skill name, no step number,
no delegation slot in a line that lands in a project artifact —
and its fold-reconciliation line is a table, one row per kill, so
"nothing dropped" is checked by counting. The skill's export
section says what the run had to discover: the commits carry the
derivation, the file ends in the workflow's presentation order
L1→L5. Its residue filter widens to the run's rule: an export
carries no agent language. The pin is untouched; run 3's copies
stay as installed until a re-pin. The records here say what
landed, and correct one line of the 2026-09-10 reading: the twin
finding was harvested on 2026-09-07 already, so this set has two
fixes, not three.

## Commits

**1. `docs(agent): add change-plan for the run 3 framing harvest`**
This plan, agreed.

**2. `docs(starter): registry template opens in project voice`**
The template's "Framed <date> (cbc-framing step 6; verdicts …)"
line rewritten so a filled registry reads as the project's own:
the date, whose verdicts, nothing a reader would need the agent's
arrangement to decipher. One harvest line in the template's
header. Run 3's 2ecfed9 is the lived form.

**3. `docs(starter): reconciliation line as a table`**
The template's fold-reconciliation section goes from an arrow list
to one row per kill — what dies, where it lands — with the folds
and the written zero below it, and one sentence above saying the
definition's L4 states every kill and the column is a summary for
counting. Harvest line in the header. Run 3's 79344c5 and 827d123
are the lived form.

**4. `docs(starter): cbc-framing says the file ends L1→L5`**
The export section's "growing L2 → L1 → L4 → L3 → L5, one lived
state per commit" gains its missing half: the commit series
carries the derivation order, the file ends in the workflow's
presentation order — the next run does not append. Harvest line
in the skill's header.

**5. `docs(starter): the residue filter refuses agent language`**
The export section's filter widens from "never references the
derivation doc's machinery" to the run's rule — no skill name, no
workflow step, no arrangement in an export; a reader without the
skills directory must not need it. Harvest line in the skill's
header.

**6. `docs: records for the run 3 framing harvest`**
TODO's harvest item closed as done with the two fixes and the
twin correction; the devlog entry for this session, carrying the
correction to the 2026-09-10 reading (the twin was harvested
2026-09-07; run 3's copy is stale at its pin, its TODO item is the
run's to close at a re-pin).

**7. `docs(agent): close change-plan for the run 3 framing harvest`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Two fixes, not three.** The worked-example twin hand-off is
  already in the master (harvested 2026-09-07, both headers). The
  reading committed at 5bdcf71 counted it as open; step 6 corrects
  the record rather than rewriting history.
- **The table shape is harvested too**, though the run filed no
  hand-off for it: the reviewer asked for it in run 3 on reading
  the arrow list, and the run's plan records the why (checked by
  counting rows). Same discipline as the voice fix — the run's
  lived form, its wording. Strike step 3 if the arrow list should
  stay the template's default.
- **Run 3's copies are not touched.** A harvest lands in the master
  only (ADR-0007); the run re-pins when it chooses. Its two
  hand-off items stay open in its TODO until then.
- **No ADR, no CHANGELOG entry.** Every step applies ADR-0007 and
  ADR-0008; nothing in `concept/` changes, so no concept version
  moves.
