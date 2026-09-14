# 0021. cbc-slice gains a stack reference beside its stack-free skill

Date: 2026-09-14
Status: Proposed (opened at the SL-1 harvest change-plan's second
commit, per change-plans §4; flips at the set's final records
commit once the reference's shape has held)

## Context

cbc-slice carries its WHAT/HOW seam in words: "zero mechanisms" at
Stage 1, then the plan and the build where "implementation judgment
is yours". Nothing beside it says what a slice looks like on any
stack. cbc-bootstrap, the skill one step earlier, has three stack
references — the walkthrough, the harness reference, the pom
convention — each on one model: imitated, never pasted; every
artifact stating the outcome it realizes, with variation points, so
a reader can reject the artifact and keep the outcome (ADR-0008
placed them inside the skill).

Run 3 (never-oversold, the pure seed's third birth) closed SL-1 on
2026-09-14 and re-derived the Spring shape of a slice from nothing:
the naive-then-wall commit split with the evidence run red on the
working tree before the wall's commit; the witness read over plain
JDBC from outside every instance, with a sampler for "in every
readable state"; the one-statement admit with the store's row count
as the decision; value types at the door; bodies asserted by JSON
path; the absence guarantees held by rules on the compiled classes,
each shown to fire on a plant. Each of those cost the run a
decision, one of them a dead end (a text search over the source,
replaced by ArchUnit before the commit). Its hand-off asks for a
`references/spring-slice-reference.md` by name and says what it must
not be: a second skill.

## Options considered

1. **A second skill, stack-bound** — cbc-slice-spring beside
   cbc-slice. Rejected: the unit is one invariant end to end and the
   completion test is single; two skills put a seam where the method
   has none, and a run would have to choose between them at every
   slice.
2. **Stack text inside SKILL.md** — a Spring section after Stage 3.
   Rejected: the skill stays stack-free so a run on another stack
   copies it whole; a stack paragraph in the skill is the first
   thing such a run has to cut, and the pin then differs from the
   master for a reason that is not the method's.
3. **A reference on cbc-bootstrap's model** — one file under
   `references/`, pinned to concept v1, provenance from run 3's SL-1
   read read-only, each artifact with the outcome it realizes and
   its variation points; SKILL.md carries one pointer line marked as
   one stack's reading. Chosen: it is the shape the bundle already
   uses for stack knowledge, and it lets a run on another stack write
   its own reference beside this one without touching the skill.
4. **Nothing — the slice record in run 3 is the reference.** A run
   reads its predecessor's `docs/construction/sl-1-*.md`. Rejected:
   a run reads only its own repo (the tier rule); what a run cannot
   reach, the bundle carries.

## Decision

Option 3. cbc-slice gains `references/spring-slice-reference.md`,
written from run 3's SL-1 as lived, on the harness reference's
model. The SKILL stays stack-free; its one new line points at the
reference as a Spring reading of the build stage, to be imitated,
never pasted. A run on another stack writes its own reference at
the same address pattern and hands it back; the skill is not
touched for it.

## Consequences

Good: the next Spring run does not re-derive six decisions and one
dead end; the reference is where a contention slice is legible in
the bundle without a written-not-lived worked example; the bundle's
one model for stack knowledge holds across both practice skills.
Accepted costs: the reference is lived once — every section is a
variation point until a second run confirms or replaces it, and the
header says so; a reader of SKILL.md now sees a stack name in a
stack-free file, one line, marked; the twin worked-example note
stays as it is, since the example is not this reference's job.
