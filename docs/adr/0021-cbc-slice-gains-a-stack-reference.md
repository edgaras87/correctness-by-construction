# 0021. A Spring slice reference, held here and handed after the build

Date: 2026-09-14
Status: Accepted (2026-09-15, at the set's final records commit;
opened Proposed per change-plans §4 and revised at the boundary
before the reference landed — the decision turned from shipped in
the bundle to held here, the user's design. The held reference is
in place at docs/baselines/spring-slice-reference.md, 8383932;
cbc-slice unchanged for it; the first comparison waits on run 3's
SL-2 close)

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
3. **A reference on cbc-bootstrap's model, shipped in the bundle** —
   one file under the skill's `references/`, pinned to concept v1,
   provenance from run 3's SL-1 read read-only, each artifact with
   the outcome it realizes and its variation points; SKILL.md
   carrying one pointer line. The first decision here, 2026-09-14,
   and staged that way. Rejected 2026-09-15 at the boundary: a file
   of working code inside the skill is a lookup, and the skill's own
   teaching is that walls are chosen by comparison, never looked up.
   Moving the pointer to Stage 3 and opening the file with "read
   after the plan is signed" was tried in the staging; asked whether
   that stops an agent reading it early, the honest answer was no —
   a prose guard is the "code review" rung of the skill's own
   hierarchy, and the only wall left was the Stage 2 comparison in
   front of the signer. The exposure is removed instead (option 5).
4. **Nothing — the slice record in run 3 is the reference.** A run
   reads its predecessor's `docs/construction/sl-1-*.md`. Rejected:
   a run reads only its own repo (the tier rule); what a run cannot
   reach, it is handed.
5. **The reference held here and handed after the build** — the
   user's design. The file lives beside frozen v2 under
   `docs/baselines/`, blind to newborns: the pure seed copies the
   bundle, and this is not in it. A run derives its build with no
   reference in hand. After the build is on record, at the slice
   close and before the reading here, the reference is handed to the
   run as session input — told, unpinned, the gates experiment's
   designed exception to the tier rule — and the run compares its
   shapes against it section by section. Chosen: the run's
   derivation is uninfluenced, the reference improves by comparison
   rather than by copying, and the reading here gains a second
   measured category beside the gates — which shapes a run
   re-derives unaided, which it derives weaker, which it beats.

## Decision

Option 5. `docs/baselines/spring-slice-reference.md`, written from
run 3's SL-1 as lived, on the harness reference's model, opening
with the protocol it is handed under. Nothing in cbc-slice points at
it; the skill stays stack-free and unchanged for it.

The protocol:

- **The moment.** After the run's build is on record — the close
  commit on the step's branch — and before the fast-forward to main,
  which waits on the reviewer's word. Not at the plan sign-off:
  handed after the plan but before the build, it would still shape
  the build. Before the merge rather than after it, so a build the
  comparison finds weaker can be redone on a fresh branch from the
  same main instead of refined on top; the run's branch rule
  already lets a restart rename the old branch and cut a new one.
  The run's agent cannot know the moment is for this — it is blind
  to the reference — so its close says only that the step is closed
  on its branch and the fast-forward waits; what the reviewer holds
  against the step is compared then.
- **The channel.** One line of session input in the run, after the
  close is committed: here is a reference from an earlier run's
  build; compare your shapes against it section by section; for
  each, say which is stronger and why; record the verdict. The file
  is not copied into the run's tree.
- **The verdict, per shape**, recorded in the run's devlog and its
  decisions log: the run's is stronger — the run keeps it and files
  a hand-off; the reference's is stronger — the run adopts it as a
  recorded revision with its reason, a refinement commit if the
  build changes; equal or incomparable — a variation point.
- **The update.** Each verdict the reading here confirms lands in
  the reference with one dated harvest line naming the run that
  earned it (ADR-0007). The reference is a lived best, never a
  master.
- **A second derivation**, when the reviewer wants one: the first
  branch is moved out of the local repo — bundled to a file outside
  it and deleted locally, since a branch left in place, local or
  remote-tracking, is readable — a fresh session cuts a new branch
  from the same main and runs the slice again; both are restored
  for the comparison, and one reaches main. The chosen branch gains
  one commit before the merge naming the rival and the verdict; the
  other is kept as the bundle. The cost is the slice's work twice,
  spent only where the reviewer chooses.
- **The first moment** is run 3's SL-2 close. Run 3 is the
  reference's source, so SL-1 has nothing to compare.

## Consequences

Good: a run's build is derived clean, and the reference cannot
become the answer before the plan's comparison has happened; the
reference improves only by a lived comparison, each change traced
to the run that earned it; the reading here measures the reference
the way the gates reading measures the playbook. Accepted costs: a
run that derives a weaker shape has already built it and pays a
refinement commit; the next Spring run gets the six shapes and the
dead end only after it has met them itself — which is the point; a
comparison session per slice close is the reviewer's time; one more
held document to keep current. The reference is lived once — every
section is a variation point until a comparison confirms or
replaces it, and the header says so. The twin worked-example note
stays as it is; the example is not this reference's job.
