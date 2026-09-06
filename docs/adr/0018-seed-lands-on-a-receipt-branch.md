# 0018. The seed lands on a receipt branch

Date: 2026-09-07
Status: Proposed (opened inside the receipt-branch change set per
change-plans §4; flips to Accepted at the set's final records
commit if no boundary contradicts it)

## Context

The pure seed (ADR-0016) delivers five commits on main — hygiene,
kit remainder, concept, skills, the playbook's steps — and the
newborn's agent starts from there. The manual says why: the
history is the manifest, the delivered/authored split exact in
one log. Runs 1 and 2 were seeded that way.

Three things pressed against it, all on record.

The experiment's own statement of what it measures. The pure-seed
item (TODO, fifth revision) names the measured object as assembly
judgment: "the sequence chosen and justified (entrance doc first?
records when, adapted how far? skills whole or split by source?)".
A seed committed on main has already answered the last of those
and removed the sequence question for every delivered file — the
agent inherits five commits and opens its change-plan on top. Run
2's plan chose an order for eight commits of its own; it never
chose one for the thirty files that arrived.

Run 2's known issue. Its TODO records that the kit-remainder seed
commit straddles agent-side paths (`.claude/`, CLAUDE.md) and
project records, accepted "because it predates the arrangement it
violates and rewriting shared history is not this run's to do".
The seed put a violation of the newborn's own commit rule into the
newborn's main log, and the newborn could only note it.

The lived precedent. cbc-newborn-v1 (2026-09-02) seeded on a
receipt branch, `birth-seed`, cut from the hygiene root and never
merged, with main's worktree restored to the same content
untracked; the devlog records the user wanting "the seed
inspectable in git — per-step diffs, deletable — without polluting
main's log", and reading the two histories as "what arrived" and
"how it was understood". The pure seed dropped the branch for
log-exactness; this ADR weighs that against the three above.

The semi-pure install now in view (TODO) adds one delivery — the
two entry-file fills over the kit's stubs. If it alone took the
branch, a pure run and a semi-pure run would differ in two ways
at once.

## Options considered

1. **Seed on main, as today.** Exact manifest in one log.
   Rejected: it decides the one thing the experiment says it
   measures, and it ships a straddling commit the newborn's own
   rule forbids.
2. **One squash commit on main.** Same straddle in one commit, and
   the agent still has no sequence to choose. Rejected.
3. **Receipt branch, main's worktree untracked** — chosen. The
   branch is the manifest (five commits, pins in the subjects,
   deletable, never merged); main's first commit after hygiene is
   the agent's; the delivered/authored split is exact across two
   logs instead of one.

## Decision

The seed commits on a branch named `birth-seed`, cut from the
kit's hygiene commit, one commit per delivery with the pin in the
subject, never merged. Main stays at the hygiene root; after the
seed, the branch tip's tree is restored into main's worktree
untracked, byte-identical, so `git status` on main lists every
delivered file and main's log holds nothing but hygiene.

The pins reach the agent through the firing prompt, one line: the
seed arrived on branch birth-seed, pins in its subjects, main's
worktree holds the same files untracked. Nothing is written into
main for it — the prompt is the session channel, and a branch that
is deletable and never merged is session-shaped truth.

This is the shape for every seed from here: the pure install as
revised in this set, and the semi-pure install when designed, which
adds one commit to the same branch and otherwise differs in
nothing. Runs 1 and 2 keep their shape as history; readings against
them state the difference.

pure-seed.md's "five commits on main, no other branch" is amended
accordingly; ADR-0016's adoption of the pure shape stands, its
delivery mechanics changed in this one respect.

## Consequences

Good: the agent's first act on main is choosing what to commit and
in what order — the measured object measured; no straddling commit
enters main; the branch is a per-step manifest you can diff and
delete; the pure and semi-pure seeds differ by exactly one commit.
Bad: the manifest is no longer in the log the agent works in — one
prompt line and a branch switch stand between the agent and the
pins; a careless `git add -A` on main commits thirty delivered
files in one go, which is a real outcome the reading records
rather than a failure the seed prevents; runs 1 and 2 are a
different shape from every run after them.
