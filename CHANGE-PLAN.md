# Change-plan: gather the bundle under starter/

## Summary — the state after all commits

The repo carries the handbook-mirroring delivery layout: starter/
holds a describing README (bundle description, the contract from our
side, the harvest flow), installs/cbc.md (the birth manual — the
former Birth section, peer of the handbook's installs/default.md),
and bundle/ with everything that ships — five skills, the snippet,
the playbook, birth-scenario.md. concept/ stays at the root and
ships from there; the copy rule is two wholesale directories. The
stay-home/ships boundary is structural (nothing stays home inside
bundle/), resolving the parked boundary-asymmetry TODO item.
executions/ no longer exists. ADR-0010 records the decision,
amending ADR-0004; ARCHITECTURE's codemap and component text match
the tree; historical records (closed PLAN steps, old ADR bodies,
devlog) keep their old paths — the ADR carries the mapping.

Records walk: ADR yes (0010, Proposed at open, Accepted in the final
records commit); ARCHITECTURE yes (shape changed — rides the move
commit, revert-coherent); TODO yes (path sweep, item closures);
devlog yes; CHANGELOG no (no concept bump — layout is not the mental
layer); root README no (it names no paths; the front door is
unchanged); decisions.md no (no arrangement change).

## Commits

**1. `docs(adr): propose starter layout for the bundle`**
ADR-0010, Status: Proposed — decision-first, the decision settled in
conversation. The gather-vs-evict fork, the mirror rationale (the
reply's peer-manual line), concept/ at root with the two-directory
copy rule. Rejected: the evict shape (delivery/ beside untouched
content dirs), the full gather (method/ absorbing concept/), a
gathering boundary exempting concept/ (leaky by construction).
Amends ADR-0004; a pointer line lands in 0004's header.

**2. `docs: gather the bundle under starter/`**
The move itself, one coherent change: git mv of the skills, snippet,
playbook, and birth-scenario.md into starter/bundle/; the old
bundle README split into starter/README.md (describe, contract,
harvest, the in-trial paragraph) and starter/installs/cbc.md (the
Birth section); internal cross-references updated in the moved
files (birth-scenario.md's pointers to the table and Birth steps).
ARCHITECTURE's codemap and executions component rewritten to the
new tree in the same commit — reverting the move without it would
leave the shape record describing a tree that exists again, and
vice versa.

**3. `docs: retriage TODO for the starter layout`**
The boundary-asymmetry Later item closes (resolved by this set, its
trigger arrived as the symmetry argument). Live path references
sweep to the new tree (the re-birth and bundle-side items). The
queued handoff item gains the FYI: our bundle now mirrors the
starter shape, making the peer-manual line true in both directions.

**4. `docs: close records for the starter layout`**
The devlog entry, and ADR-0010 flips Proposed → Accepted — the
final records commit, per the injected convention; never the close
commit.

## Decisions taken inside this plan

- ARCHITECTURE rides the move commit rather than standing alone:
  the revert test binds them.
- Historical records keep old paths untouched (closed PLAN steps,
  prior devlog entries, ADR-0004/0007/0008 bodies). ADR-0004 gets
  only an amended-by pointer line, not a rewrite.
- Manual filename cbc.md: the handbook names its manuals by role
  (pure, default); a concept names its own by the concept. Cheap to
  rename if the composition ever wants role-naming.
- The snippet moves as-is; its fate stays the trial's question, not
  this set's.
