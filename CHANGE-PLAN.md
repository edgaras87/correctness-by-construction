# Change-plan: cbc-run playbook rebuilt as a full sequence

## Summary — the state after all commits

The bundle's playbook is a complete, self-contained sequence a birth
copies whole: Step 0 Bootstrap, Step 1 Framing, and Step N Release
vendored from the kit's `playbooks/default.md` @ 65dd7ee with a
provenance-and-pin line each, our harvested middles (Define, Ground,
Skeleton & bootstrap, Invariant slices) between them unchanged. An
ADR records who owns which steps: endpoints follow the kit (updated
by refresh against the pin, specialized but never weakened), middles
are CbC's own (changed only by harvest). The install manual carries
the step that was missing under the new model — replacing the
newborn PLAN's STEPS region with this sequence (the sed lives in the
handbook's `installs/default.md`, which a CbC birth replaces with
ours) — and the delivery docs describe copied-whole-at-birth instead
of copied-at-Framing. This repo's own `playbooks/` holds the current
kit base (`default.md`, pinned) instead of the pre-redesign
`TEMPLATE.md`.

Out of scope, staying queued in TODO: the moment-of-need skill steps
(half (a) of the bundle-side item), the re-birth, the handbook
handoff.

## Commits

**1. `docs(agent): add change-plan for playbook rebuild`**
This plan, committed after agreement.

**2. `docs(adr): propose playbook step ownership`**
ADR-0011, Status: Proposed. Decision-first — settled in
conversation (2026-09-01): the playbook ships complete rather than
referencing the kit's steps; endpoints are vendored copies that
follow the kit, middles are owned here. Options rejected:
middles-only file (two masters compose in the newborn — the
ambiguity that caused this set), reference-not-copy (a run's plan
must stand alone). Lands early so the rebuild commits build on a
visible decision.

**3. `docs: refresh playbooks base from the kit`**
`playbooks/TEMPLATE.md` (pre-redesign kit generation, no pin,
untouched since birth commit 1a71e56) is replaced by
`playbooks/default.md` — a pinned copy of the kit's current base @
65dd7ee with a provenance header. One read serves both this and
commit 4; this repo's own machinery lands on the generation the
bundle builds against. Project-scope: `playbooks/` is repo
machinery but not `.claude/`, so no decisions.md entry.

**4. `docs: rebuild cbc-run playbook full-sequence`**
`starter/bundle/cbc-run-playbook.md` becomes the whole sequence on
the kit base: vendored Step 0/1/N each opening with a
provenance+pin comment line; middles inserted between Framing and
Release, content unchanged, renumbered into the sequence; the
"Release additions" section dissolves into the vendored Step N as
added gate items, caveats kept. Version line bumps to v2 with a
dated note (structural rebuild, no new lessons — "Last updated
from project" unchanged). The file must end at Step N: the install
sed copies from the first `## Step` to end-of-file. Exact
specialization wording inside the vendored steps is material-first —
shaped at this commit, reviewed at its boundary.

**5. `docs: teach the birth the whole-playbook copy`**
The delivery docs describe the new model, together (reverting one
alone would leave them contradicting each other):
`installs/cbc.md` gains the STEPS-region replacement step (sed from
the newborn's `playbooks/cbc-run.md`, "Steps from:" line filled),
its step 6 becomes confirmation-not-copy, and the correct-birth
checklist gains the PLAN item; the starter README's table row drops
"copied into PLAN.md at Framing" for copied-whole-at-birth.

**6. `docs: close records for the playbook rebuild`**
The records walk's late arrivals: ADR-0011 flips to Accepted (no
boundary contradicted it), PLAN's decision index gains its line,
TODO retriages the bundle-side item (half (b) done; half (a)
becomes its own Next item), devlog entry with a resume line.
CHANGELOG: no — the mental layer did not change. ARCHITECTURE: no —
the bundle's shape is unchanged, one playbook file either way.
README (root): no — outside-visible truth unchanged.

**7. `docs(agent): close change-plan for playbook rebuild`**
Deletes this file; body records what diverged.

## Decisions taken inside this plan

- Scope is the playbook half only. The user chose "lets do now
  playbook"; the moment-of-need half stays queued rather than
  riding along.
- The TEMPLATE.md refresh joins this set: discovered while planning
  it (the file is a stale ancestor of the exact base this set reads),
  and folding it in costs one commit against a second visit later.
- The manual's missing sed step is treated as a gap-fix, not line
  polish: `pure.md` ends before any playbook is chosen, and the
  handbook's own step-2 sed is in the manual ours replaces — found
  by reading the composition end-to-end while planning.
- Playbook version becomes v2: a run pins "Steps from:
  playbooks/cbc-run.md v<N>", and v1 names the middles-only shape.
- No `.claude/` files change in this set, so no decisions.md entry;
  the agent-scoped commits are exactly the plan's open and close.
