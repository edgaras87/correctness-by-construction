# Change-plan: snippet withdrawn, arrangement derived at birth

## Summary — the state after all commits

The bundle no longer ships cbc-startup-snippet.md, and no birth
merges a pre-written section into the newborn's CLAUDE.md. The
newborn derives its own arrangement instead: the walk starts by
reading `concept/`, then the agent fills CLAUDE.md, README, and the
stubs itself, then the plan, then the skills. The snippet stays in
this repo as a held baseline — it was written from theory before
any birth, and the first walked birth's derived CLAUDE.md section
is compared against it; stay, replace, or merge is decided at the
trial's close with that evidence. The overlay contract tightens
from "touches one kit file (CLAUDE.md, by append)" to touching no
kit file at all. The birth scenario is rewritten around this order
and also absorbs two pending fixes (the stale manual-step pointer,
the playbook-sed placement); TODO gains the rebuild-script note.

## Commits

**1. `docs(agent): add change-plan for snippet withdrawal`**
This plan, committed after agreement.

**2. `docs(adr): propose deriving the arrangement at birth`**
ADR-0012, Status: Proposed. Decision-first — settled in
conversation (2026-09-02): the snippet is the bundle's last
theory-only artifact; withdrawing it turns it into a hypothesis
with an experiment (the same blind-comparison pattern as the v1
baseline), matches the kit's native model (the agent fills its own
stubs), tests `concept/`'s legibility directly, and zeroes the
overlay's kit-file touches. Rejected: keep shipping it (a guess
delivered as if earned); delete it (loses the comparison the
decision needs); scenario-only withdrawal (the manual would still
merge what the bundle no longer carries).

**3. `docs: withdraw the snippet from the bundle`**
One coherent change — the bundle stops carrying it and every
delivery doc stops saying it does: git mv to
`docs/baselines/cbc-startup-snippet.md` with a header line
(withheld 2026-09-02, comparison point the first walked birth,
fate at trial close); starter README loses the copy-table row and
the contract paragraph drops the CLAUDE.md-append clause; the
install manual loses the merge step (renumber, checklist item
becomes "CLAUDE.md's CbC section is the newborn's own, derived at
Step 0"); the playbook's Step 0 (CbC) comment reworded off "the
merged section", one dated provenance line, no version bump
(structure unchanged, no lesson folded).

**4. `docs: reorder the birth scenario around derivation`**
The scenario draft rewritten: seed keeps kit birth + bundle copy +
birth entry (no merge step); the walk becomes concept-first —
read `concept/`, derive and fill CLAUDE.md / README / stubs, then
the map (playbook sed into PLAN, placed here provisionally), then
the skills (grouping the newborn's change-plan's call), then the
records; briefing last and outside, unchanged. The stale
"steps 3–4" pointer fixed against the renumbered manual. The
order is marked provisional — the first walk tests it; the
snippet open point in the trial protocol is rewritten to the
compare-then-decide form.

**5. `docs: close records for the snippet withdrawal`**
ADR-0012 flips to Accepted; PLAN's decision index gains its line;
ARCHITECTURE updated where the shape changed (executions component
no longer lists the snippet, codemap gains `docs/baselines/`);
TODO — the prebuilt-stub item gains the rebuild-script variant
(staleness objection dissolved; script-vs-walked-commits decided
at trial close), snippet mentions retriaged; devlog entry with
resume line. CHANGELOG: no (mental layer unchanged). Root README:
no.

**6. `docs(agent): close change-plan for snippet withdrawal`**
Deletes this file; body records what diverged.

## Decisions taken inside this plan

- The withdrawal is unconditional, not scenario-only: the manual is
  the procedure of record, and it cannot keep merging a file the
  bundle no longer ships. Both procedures now derive.
- Baseline home is `docs/baselines/` — stay-home by location
  (ADR-0010's structural rule: outside `starter/bundle/` nothing
  ships), named for its role, room for later held baselines (the
  two-tier-harvest TODO idea points the same way).
- The walk order lands as the draft's proposal, explicitly
  provisional — the user called it an example; the first walk is
  the test, per the scenario's own trial protocol.
- The two pending scenario fixes and the TODO script note ride
  this set: same files, same boundary, three fewer standalone
  commits later.
