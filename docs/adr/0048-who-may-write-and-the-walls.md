# 0048. Who may write, and the walls

Date: 2026-10-08
Status: Proposed (2026-10-08, under the commit plan for run 3's
edits)

## Context

The walls chapter, `concept/02-guarantees-and-walls.md`, ranks the
walls by who can violate them: database constraint, type system,
single validated entry path, runtime check, code review, hope. Run 3
met two things it does not say, at SL-3 and the review after it, and
sent them as lessons for the chapter, which a run never edits (its
TODO, *To the deliverer*, read 2026-10-08).

- **A wall binds no one who can remove it.** SL-3 defended its
  receipts and units held against scripts holding the ledger's own
  identity, because nothing said whether such writers were trusted.
  The review wrote the answer — trusted, everything else fenced (run
  3's definition, T4; its ADR-0014). Until then its single entry
  path was a wall only in name: "single" held only while nothing
  else wrote. The same gap sits one rung up — a constraint binds
  every code path, never the store's owner, who can drop it.
- **A right withheld is a wall.** Run 3's application identity
  holds no right to change the store's structure, and the server
  refuses it (run 3's ADR-0006, C1); SL-3 weighed the same for
  receipts — the identity's update and delete revoked — and chose a
  trigger for what the revoke cost the ground, not for a weaker
  wall. It is the store's own refusal, as a constraint is, and the
  strongest wall for a rule that an operation never happens. The
  ranking names only the constraint.

The framing half of the same lesson — who besides the system may
write what it stores — is already the described adversary's
"assumptions explicitly accepted as trust", and the framing skill
asks it since `6389120`. The slice skill hunts escape hatches
against that answer since `3758a72`. The chapter they derive from
says neither.

## Options considered

- **Leave the chapter; the skills carry it.** Rejected: a derivation
  that says more than its source about what a wall is, is how the
  two drift apart.
- **One clause on the single-entry-path rung.** Rejected: it fixes
  the rung run 3 met and leaves the reason unsaid; the constraint
  rung has the same gap.
- **A paragraph after the ranking, the ranking unchanged.** Rejected
  by the reviewer: a reader who takes in the ranking alone still
  sees "database constraint", and never meets the withheld right.
- **The paragraph, and the top rung renamed for both refusals** —
  chosen.

## Decision

1. **The top rung is the store's refusal**: a constraint, or a right
   withheld from the identity that writes.
2. **A paragraph after the ranking says who each wall leaves
   unbound**: whoever can remove it. The described adversary says
   who besides the system may write what it stores, trusted or
   defended, and walls are assigned against that answer; a single
   entry path is a wall only where the trust names it the only
   writer. Its wording is settled in the chapter's own commit.
3. **This is substance; the concept's next release is v2**
   (ADR-0003). A plan derived from v1 may hold a single entry path
   as a wall with no trust line naming it, and under this text that
   plan is wrong.
4. **The executions that state the ranking follow it**: `cbc-slice`'s
   SKILL.md and workflow, and `cbc-framing`'s
   `the-whole-system-in-plain.md`.

## Consequences

- CHANGELOG's [Unreleased] carries the change, and names v2.
- Runs take the chapter at their next delivery, in its own commit
  first (ADR-0046); every run's copy of the ranking changes.
- "Use database constraints" in `concept/00-cbc.md` stays: it names
  a technique, not the rung.
- TODO's absence rung stays held. A guarantee held by absence — no
  clock, no state outside the store — is not a right withheld, and
  its trigger, a second run meeting one, has not fired.
