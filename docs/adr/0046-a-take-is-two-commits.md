# 0046. A take is two commits

Date: 2026-10-01
Status: Proposed (2026-10-01, under the commit plan for the take's
two commits)

## Context

Two rules a run holds from us met at its take on 2026-10-01.

- **`delivered-copies.md`** says one pin covers every delivered
  copy, the skills and rules under `.claude/` and the chapters under
  `docs/concept/` alike (rule 1), and describes the take as one
  sequence: check, find the run's own edits, copy whole, remove what
  the note says is gone, write one decisions entry (rule 5). It
  says nothing about commits.
- **`commit-messages`**, *The agent's own files*
  (`docs/conventions/commit-messages/`): a commit that touches
  `.claude/` touches nothing else.

Run 3 read one pin as one commit. Its take @ `0000855` put the
`.claude/` copies, the concept chapters and the decisions entry in
one `chore(agent)` commit, and broke the second rule to keep the
first. It asked which gives way, or how the take is split. At its
birth the concept had gone in a commit of its own.

## Options considered

- **An exception in `commit-messages` for a take.** Rejected: a
  rule with an exception cannot be applied without first
  classifying the commit. Our backlog holds the same objection
  against a mood exception for record commits.
- **Two commits, `.claude/` first.** Rejected: the decisions entry
  is under `.claude/`, so it lands in the first commit, which
  claims the new pin while the chapters are still at the old one.
- **Two commits, the concept first.** Neither rule bends, and the
  entry lands where it is true.

## Decision

1. **A take's commits follow `commit-messages`, the chapters'
   commit first.** How each commit is made is that convention's;
   the take adds only the order.
2. **The decisions entry, carrying the pin and the read-through,
   lands in the last commit, where every copy equals the pin.**
   When the run cuts no receipt branch, it is the commit the
   deliverer diffs the copies against at the next read.
3. **`commit-messages` is unchanged.**

## Consequences

- `docs/conventions/exchange/` §4 and the shipped
  `delivered-copies.md` rule 5 say the order and point at
  `commit-messages` for the rest, restating none of it
  (`docs/conventions/conventions/` §3.1).
- `exchange-read` needs no change: the commit of the entry that
  recorded the pin is already its diff base.
- The next note to run 3 answers its ask with this.
