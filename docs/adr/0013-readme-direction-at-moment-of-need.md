# 0013. README direction lives at the skills' moments of need

Date: 2026-09-03
Status: Proposed

## Context

The handbook's README stub used to carry Prerequisites/Run/Test as
sections with fill-comments — direction baked into the container,
hedged with "Framing decides" (their ADR-0024). The 2026-08-31
exchange split that: the *when* is convention-tier and landed in
their project-recording (README as a projection record — a section
arrives when a step's gate makes it true; gate items where relevant,
no mandatory doc step per gate; their ADR-0025/0026), and the stub
was slimmed to the adopted rule — container stays, direction goes.

That deletion orphaned the *what*: for a CbC run, nothing anywhere
now says which step makes each section true or what shape the
section takes. The moments are method facts — the ground standing,
the harness being real — so the home is method-tier: this bundle's
skills.

One lived fact shapes the split. checkout-system's Prerequisites
section holds both environment lines (podman, compose provider) and
a stack line (JDK via wrapper) — but at ground time no stack fact
exists to project. Each line arrives when its fact becomes true.

## Options considered

1. Leave it to the newborn's derivation (ADR-0012). Rejected: that
   ADR covers birth-time arrangement, derived in the session that
   reads `concept/`; these sections' moments are mid-run, past any
   session that saw the scenario — direction that must survive to a
   later moment needs a file the moment's work reads, and that file
   is the skill being walked.
2. Gate items in the cbc-run playbook's middle steps. Rejected: the
   adopted projection rule refuses a mandatory doc step per gate;
   the playbook already routes Ground and Skeleton to these skills,
   which is where the work — and so the moment — is lived. The
   middles also change by harvest (ADR-0011), and this is adoption,
   not harvest.
3. Steps in the skills, with the section skeletons as template
   fragments inside each skill (ADR-0008 machinery) — chosen.

## Decision

infra-establish's exit projects the README's **Prerequisites**
section when the ground stands — environment lines only, from
`templates/readme-prerequisites.md`, derived from the operator
manual (a projection, never a second master). cbc-bootstrap's close
projects **Run** and **Test** when the harness is real — plus the
stack's Prerequisites line, whose fact is born there — from
`templates/readme-run-test.md`.

Both fragments are extracted from checkout-system's lived README
(read-only), the same discipline as the skills' seven existing
templates: master copies here, pin and provenance in the header; a
run copies, fills, and the filled section is the run's own
(ADR-0008).

Scope boundary: CLAUDE.md has parallel mid-run moments — the stack
fact at bootstrap, a ground-must-be-up local rule at establish — and
gains nothing here, deliberately. Its stub teaches its own fills
(each section's comment carries the rule), so no direction was
orphaned; and whether the newborn catches those moments unprompted
is the ADR-0012 derivation experiment's data. A watch item rides the
re-birth; evidence decides at trial close.

## Consequences

Good: the orphaned direction has a home that survives to its moment
— the skill open in the session doing the work; a run whose ground
never stands correctly has no Prerequisites section (projection
follows truth); the fragments are lived, not theorized.
Accepted costs: the README's one section now fills from two skills
at two times, so a reader mid-run sees a Prerequisites section
without a stack line — honest, but it can read as incomplete;
infra-serve gains no step, so a later service that changes the
ground's prerequisites must refresh the projection as part of
growing the operator manual — harvested into an explicit step only
if a run shows the miss.
