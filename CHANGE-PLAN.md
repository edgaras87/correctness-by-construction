# Change-plan: harvest run 3's SL-1 into cbc-slice

## Summary — the state after all commits

Seven findings from run 3's Step 5 (read 2026-09-14, TODO Now) land
in the cbc-slice masters, one in the cbc-bootstrap harness reference
and one clause in the cbc-framing registry template, each in the
run's own wording, one dated harvest line per change per file (CBC
ADR-0007), the pins untouched — runs re-pin on their own act. After
the set: Stage 0 says how the first slice answers R5 and the build
stage owns "red before green"; Stage 1 names what the first slice
births that the framing cannot carry and Stage 2 owns the surface at
its minimum; Stage 2 puts the owner candidates in front of the
signer as a comparison; Stage 1 exits only when every flag on the
registry row is answered by name; Stage 4 flips the row to
`in-progress` at the specification and closes it naming the
provisionals and what the slice hands on; the harness reference
states the body-assertion convention as a variation point; and a
Spring slice reference exists — **held here, not shipped in the
bundle** (ADR-0021 as revised at this set's boundary): a run derives
its build uninfluenced, and the reference is handed over as session
input after the build is on record, for a comparison whose verdict
improves the reference or the run. Two of run 3's hand-offs
are not taken: the absence rung (a concept question, TODO Later)
and the contract wording (the run's own document). Nothing in
`concept/` moves: no CHANGELOG entry, no concept version.

## Commits

**1. `docs(agent): add change-plan for the run 3 SL-1 harvest`**
This plan.

**2. `docs(adr): cbc-slice gains a stack reference`**
ADR-0021, Status: Proposed — the decision settled at the reading,
recorded before the file it governs. Context: the skill carries its
WHAT/HOW seam in words and no stack reference beside it, where
cbc-bootstrap has three; run 3 re-derived the Spring shape of a
slice from nothing and asked for the reference by name. Options: a
second skill (rejected — the unit is one invariant end to end and
the completion test is single); stack text inside SKILL.md
(rejected — the skill stays stack-free so a run on another stack
copies it whole); a reference on cbc-bootstrap's model, imitated
never pasted, each artifact stating the outcome it realizes with
variation points (chosen). Flips to Accepted in commit 10, once
the reference's shape has held.

**3. `docs(starter): the first slice answers R5 in its build`**
references/system-readiness.md R5: at the first slice there is no
wall to break, so R5 is answered in the build — the naive version
committed first, the wall its own diff, the evidence run red on the
working tree before the wall's commit, recorded from actual output.
SKILL.md Stage 0's R5 line says the same in one clause, and Stage 3
gains the gate in the run's words: red before green, the same tests
unchanged. references/cbc-slice-workflow.md Stage 3 carries it too.
Harvest lines in all three.

**4. `docs(starter): the first slice births more than its invariant`**
SKILL.md Stage 1 and the workflow's Stage 1: beside the invariant
and adversity taken as written, the "birth whats" the framing
cannot carry — the schema, the first migration, the door and its
conventions, how the aggregate comes to exist at all — named and
decided at the opening, as records, never absorbed (run 3: two ADRs
before the specification). Stage 2 in both files owns "the surface
at its minimum": only what the guarantees need somewhere to live,
and nothing beyond. The worked example stays duplicate-delivery — a
contention twin waits for a second lived contention slice. Harvest
lines in SKILL.md (second, same set) and the workflow (second, same
set).

**5. `docs(starter): the owner candidates in front of the signer`**
SKILL.md Stage 2 and the workflow's Stage 2: the plan presents the
candidate owners for a guarantee as a comparison the reviewer can
weigh — each face, how it holds the guarantee, its cost — with a
recommendation, the way an ADR presents options. Run 3's plan named
four rejected faces in one paragraph after the choice and the
reviewer read past it; the sign-off is real only if the
alternatives were in front of the signer. Harvest lines in both
(third, same set).

**6. `docs(starter): every flag on the registry row is answered`**
SKILL.md Stage 1's exit and the workflow's Stage 1 exit: a flag on
the registry row ("named here so the slice inherits the warning")
is answered by name in the specification — staged as its own
evidence, or removed by a definition with the removal shown (run 3:
FC3 removed kill 10; G4 showed kill 9 has no interval).
cbc-framing's templates/registry.md flag-riding placeholder gains
the one clause that says the slice answers it by name. Harvest
lines in SKILL.md and the workflow (fourth, same set) and the
template.

**7. `docs(starter): the close is more than a status`**
SKILL.md Stage 4 and the workflow's Stage 4: the row flips to
`in-progress` when the specification lands, the first
project-visible work; the close names the provisionals and what the
slice hands to later slices by name, and re-decides the ordering
with its reason — the step that makes concept 04's "a built slice
may teach that the next is wrong or split" true in the registry.
Harvest lines in both (fifth, same set).

**8. `docs(starter): bodies asserted by path, never by substring`**
cbc-bootstrap's references/spring-harness-reference.md: how the
evidence asserts on a body is a stack convention the reference left
unsaid, so each run decided by habit — run 3 went substring first
and replaced it mid-slice by JSON path, since a substring cannot
tell 3 from 30 or say a field exists. A variation point: by path for
a shape, by type when a shared API contract exists, never by
substring; the contention probe's own `.contains` line annotated to
say it is the identity witness, not the pattern. Harvest line in
the reference.

**9. `docs(adr): the slice reference is held, not shipped`**
ADR-0021, still Proposed, revised at the boundary before the
reference lands: the decision becomes a reference **held in this
repo and handed to a run as session input after its build is on
record**, never copied at birth — so a run derives its build
uninfluenced, and the comparison decides which shape is stronger.
The bundle placement (the previous option 3) moves to the rejected
options with its reason: a file of working code inside the skill is
a lookup, and a prose guard against opening it early is the "code
review" rung of the skill's own hierarchy. The rejected "nothing"
option's tier-rule reasoning is kept: the handed document is the
gates experiment's designed exception — told, unpinned, after the
derivation is recorded. The protocol in the ADR: the moment (the
slice close, before the reading here), the channel (one line of
session input), the verdict (per shape — the run's stronger, the
reference's stronger, or a variation point — recorded in the run's
devlog and decisions log), and the update (a harvest line here per
change the comparison earned).

**10. `docs: a Spring slice reference, held for the comparison`**
*(provisional — the split of its sections is decided when the
material is in hand; the intent is firm)*
docs/baselines/spring-slice-reference.md beside frozen v2, on the
harness reference's model: a header pinned to concept v1 and
provenance from run 3's SL-1 read read-only, opening with the
protocol it is handed under; each artifact stating the outcome it
realizes, with variation points, so a reader can reject the
artifact and keep the outcome. From what run 3 lived: the
naive-then-wall commit split and the red run; the witness over
plain JDBC from outside every instance, with the sampler for "in
every readable state"; the one-statement admit with the row count
as the decision; value types at the door; bodies by path; the
absence rung as bytecode rules with one plant per rule. Nothing in
the skill points at it.

**11. `docs: records for the run 3 SL-1 harvest`**
ADR-0021 flips to Accepted with the held reference in place as its
evidence; PLAN's decision index gains its line; TODO Now's harvest
item closes with the commit per fix; the gates-experiment item in
TODO gains the build comparison as a second reading category, with
its first moment named — run 3's SL-2 close; ARCHITECTURE's codemap
gains the baselines row if it lacks one; the devlog entry for the
set. The registry-template and harness-reference changes need no
row anywhere — templates and references live inside their skill
(CBC ADR-0008), and no codemap lists them.

**12. `docs(agent): close change-plan for the run 3 SL-1 harvest`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Seven of nine bundle hand-offs, and why not the other two.** The
  absence rung would add a level to the enforcement hierarchy, which
  concept/02 states as well as both cbc-slice files — a concept
  change with an ADR and the version question, filed in TODO Later
  with a second-run trigger, not smuggled in as a bundle line. The
  contract's "in its own specification" is run 3's own contract
  document; no infra-establish master names faces. It goes back to
  the run.
- **The ADR before the reference, Proposed until the shape held.**
  Decision-first, since the decision was settled at the reading;
  the reference's split is the one thing only the material can
  show, so commit 10 is the provisional step and commit 11 flips the
  status.
- **Held, not shipped (revised 2026-09-15, the user's design at
  commit 9's boundary).** The reference was planned into the bundle
  with a pointer in the skill. Staged that way, the question was
  whether a prose guard stops an agent reading it before the plan is
  signed; it does not, and the honest answer was that the Stage 2
  comparison and the sign-off are the only wall. The user's design
  removes the exposure instead: the run never has the file, derives
  its build clean, and gets the reference after — the gates
  experiment's own protocol, applied to the build. Cost accepted: a
  run that derives weaker has already built it and pays a refinement
  commit; the next Spring run gets nothing for free, which is the
  point.
- **Prose now, diffs later.** Run 3 has decided (staged, 2026-09-14)
  to edit its skill copies in place under guards and hand diffs.
  This set harvests the ten prose items it filed before that
  decision; the run is told at its Step 6 opening which items the
  master took, so its in-place edits do not repeat them. The first
  diff that arrives is read hunk by hunk against the master as it
  stands after this set.
- **One harvest line per change per file, in the tagged form**, as
  the last two sets did; a file touched by several commits carries
  one line per commit, "same set" after the first.
- **The worked example untouched.** A contention twin is a written
  example nobody lived; the reference in commit 9 is where run 3's
  contention slice is legible, and that is enough until a second
  contention slice is lived.
