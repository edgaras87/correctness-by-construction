# 0014. The bundle ships assembled text; the derivation experiment closes

Date: 2026-09-04
Status: Proposed

## Context

ADR-0012 withdrew the startup snippet and made the first birth an
experiment: could a newborn derive its own arrangement from
`concept/` alone? The walk ran (cbc-newborn, 2026-09-03) and
answered yes: the derived CLAUDE.md section (8f167c4) re-derived
the snippet's standing guards in its own words, carried a stronger
pre-stack discipline, and added something the snippet never had —
the records-carry-the-method mapping (README = promise,
Invariants = guarantee inventory, ADRs = refusals, PLAN cut by
invariant). It missed two things: the human sign-off gates (which
live in the skills — ADR-0013's moment-of-need logic cuts both
ways there) and the docs/system/ framing-artifact home with
registry-as-source-of-truth. The comparison is recorded in the
walk-1 reading (devlog 2026-09-03); the derivation is held blind
at docs/baselines/cbc-derived-claude-walk1.md.

The newborn's post-walk sessions then rewrote the scenario as
assembly (cbc-newborn 3b27b46, carried to the master 2026-09-04):
the derivation needed the whole bundle in view and the concept
read first, nothing more — the staged introduction lived only in
the commit log. Per-birth derivation was scaffolding for a
one-time question, and repeating it would give every newborn a
different CLAUDE.md.

## Options considered

1. Keep per-birth derivation. Rejected: the question it answers —
   is the concept legible enough to boot from — is now answered
   and recorded; repetition buys divergence noise, not signal, and
   gives up the uniform arrangement births exist to deliver.
2. Reinstate the snippet as the shipped text. Rejected: it
   predates the kit, lacks the records mapping, and lost the
   comparison everywhere the derivation won.
3. Ship the derivation verbatim, retire the snippet. Rejected:
   the derivation's two misses are real content whose place must
   be judged, not dropped by default.
4. Merge once — each side kept where it won — and freeze the
   result into the bundle as shipped text. Chosen.

## Decision

The bundle ships a CLAUDE.md text file, merged once from the two
candidates and slim by design: a short CbC section (the concept
pointer, the ordering in one line, the pre-framing guard), the
Method conventions row, the stance lines, the local-rule lines.
The seed merges it into the kit's CLAUDE.md stub at birth
(assembly step 3). No birth derives it again.

Slimming happened at the merge review (2026-09-04 boundary), not
in the comparison: the derivation's concept summary is dropped as
a lossy copy beside its master, and its step-routing rows as
redundant with the playbook mapped into PLAN — and fragile, since
framing may renumber the plan. Its records-carry-the-method
mapping — the comparison's best find — ships through the birth
fills instead: each record's fill carries the method's reading of
that record, the kit's records-teach-themselves model.

The two misses are judged under ADR-0013: the sign-off gates stay
in cbc-framing and cbc-slice, the registry rule already lives in
cbc-slice (Stage 0, the close step) — both verified, not assumed.
Only the pre-framing guard enters the shipped text, the one rule
that must hold in sessions where no skill has fired yet.

The shipped text is a derived execution like the rest of the
bundle: header pins the concept version, changes flow back as
harvest from runs, never as per-birth rewrites.

Both baselines stay at docs/baselines/, blind to newborns,
headers annotated: comparison consumed, this ADR the verdict.
ADR-0012 stands as written — this ADR closes its experiment with
the evidence it asked for.

The overlay contract's write clause returns, knowingly: ADR-0012
tightened the overlay to touch no kit file while the text was an
unearned guess. The merge into the kit's CLAUDE.md stub is again
the overlay's one non-additive act — now carrying text earned
from a lived derivation, which was the whole objection.

## Consequences

Good: every newborn boots with the same evidence-earned
arrangement; everything before the briefing is mechanical, which
is what makes the scenario's rebuild script possible; the concept
legibility question has a recorded answer instead of a standing
experiment.
Bad: the convergence metric is given up — one derivation was
observed, never a second to compare it against; and the shipped
text can drift stale against concept revisions. Accepted: the
staleness risk is the same one every bundle file carries and the
same harvest discipline covers it, and a second derivation would
have cost a birth to buy noise the first walk already priced.
