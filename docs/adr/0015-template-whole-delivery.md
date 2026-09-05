# 0015. The shipped text is a whole template, copied not merged

Date: 2026-09-05
Status: Proposed (opened per change-plans §4; flips at the set's
final records commit). Amends ADR-0014's delivery mechanism only —
its decision (shipped text, merged once from the two candidates,
no per-birth derivation) stands.

## Context

ADR-0014 shipped the method's CLAUDE.md text as fragments the seed
merges into the kit's stub at birth. That merge made the stub's
shape a live dependence: the fragments needed the stub's sections
and list to land in, which put CLAUDE.md back on the assumed-surface
list — and the handbook's contract rule says a new surface widens
handbook-side first, so a widening request was owed.

The user's design, decided while drafting the fourth handoff
(2026-09-04): no sockets at all. The bundle ships a complete
CLAUDE.md template instead, and the handoff told the handbook so —
CLAUDE.md will not re-enter the contract.

The reply then proved the ground the same day. The kit's entry file
reshaped three times before their HEAD settled (their ADR-0032: the
empty sections leave; ADR-0033: the entry-file rules move to the new
agent-arrangement convention; ADR-0034: the Conventions list itself
leaves — "the registry is the list"). Every one of those reshapes
would have broken a merge aimed at the old anchors. It also shrank
what a template must track — the entry file is now ~41 lines of
orientation, records table, and guard — killed our Method-row
fragment (no list exists to hold it; the birth entry in
`.claude/decisions.md` is the one list), and added a stub rule the
template must honor: shipped stub text cites the project's own
sequence or nothing, never a handbook ADR.

## Options considered

1. **Keep the merge (ADR-0014 as written) and ask for the
   widening.** Rejected: the dependence is the defect, not the
   missing permission — the stub reshaped three times in one day,
   and each would have been a breaking change under any anchor
   scheme.
2. **Fragments with declared slot anchors ("sockets").** Rejected,
   the user's call: the same live dependence with more machinery to
   maintain on both sides.
3. **A complete template, composed once here, copied whole.**
   Taken.

## Decision

The bundle ships `starter/bundle/claude-md-template.md`: a complete
CLAUDE.md, composed once in this repo from the kit's entry file at
the pinned handbook commit (orientation fill, records table, guard
comment) with the method's text in place (the CbC section, the
stance lines, the local rules). It carries fill variables like the
other fills and is copied whole at birth — the newborn's CLAUDE.md
is this file, filled; the kit's stub is not merged into, and no
section anchor is assumed.

The fragments file (`claude-md-cbc.md`) retires; its merge verdicts
stay in history. The template's provenance header pins both sources
— the handbook commit and this repo's — and names the handbook's
agent-arrangement convention as the rules the kit half answers to.

ADR-0014's write-clause paragraph is overtaken: the overlay's one
non-additive act is no longer an edit inside a kit file but the
substitution of a composed entry file for the stub. The
assumed-surface contract stays where the handoff left it — the
STEPS region with its markers and the step/gate idiom (the
playbooks/ directory left the kit by their ADR-0031).

## Consequences

Good: zero live dependence on the stub's shape — the day of three
reshapes cost us nothing, which is the design working.

Good: the seed gets simpler and more checkable — one copy like
every other bundle file, verifiable against the template modulo
fills, instead of a merge whose result no single master shows.

Cost: the template duplicates kit content, so a re-pin must re-run
the compose against the kit's entry file and re-verify — the
pinned-copy staleness every bundle file carries, now covering kit
text too. What to track shrank with their reshape, and
agent-arrangement §2's tests now say what may enter.

Bad: two masters feed one file — a kit fix and a method fix both
land here, and the provenance header is what keeps the halves
attributable.
