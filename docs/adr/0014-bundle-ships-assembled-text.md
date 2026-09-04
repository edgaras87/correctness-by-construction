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

The bundle ships a CLAUDE.md text file: the CbC section, the
Method row, the stance and local-rule lines, the skill rows —
merged once from the two candidates. The seed merges it into the
kit's CLAUDE.md stub at birth (assembly step 3). No birth derives
it again. The two misses are judged at the merge under ADR-0013:
a fact whose moment of need lives inside a skill stays in the
skill; an every-session fact enters the shipped text.

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
