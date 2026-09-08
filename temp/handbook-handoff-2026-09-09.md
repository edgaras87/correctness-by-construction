# Handoff from the handbook — 2026-09-09, the checkout-system review

<!-- Staging copy, tracked in temp/ while it is absorbed; deleted
     once it has served. Substance is on record in the handbook:
     PLAN Step 9's seventh finding, devlog (aq), change-plans §3,
     the seed playbook's v1 header. -->

To the concepts tier. The handbook read the checkout-system run
(`~/IdeaProjects/checkout-system`, 2026-08-27, kit @ 4fe8083 with
your bundle) against its field-test gate. Three things in it are
yours by ownership. Nothing here blocks anything.

## 1. The run's playbook lessons that are the method's

The run folded its retrospective into a v1 of the backend-service
playbook. The handbook kept one warning — one standard test command
from day one — and one lesson graduated to a convention: a change
set that will close a plan gate item names the commit that closes
it (change-plans §3, kit copy follows at your next pin). Everything
else in the run's v1 is CbC-shaped and belongs to the bundle, to
keep or drop against what run 3 already gave you. By a grep of your
bundle, some of it is there already; the rest is listed so the
decision is yours, not ours:

- Ground step (infra-establish): the runtime ground facts must
  already be in the system definition before the step opens — check
  first, log the return trip if not. (Your bundle mentions the
  return trip; confirm it says "check first".)
- Ground step: database authority as grants — role split,
  migrations-only DDL — is cheap at ground time and every later
  immutability wall stood on it.
- Bootstrap step (cbc-bootstrap): make the test container a faithful
  miniature of the ground, same bootstrap SQL and identities, so
  evidence runs under production authority. (Present in your bundle
  by grep.)
- Bootstrap step: the Boot 4 trap — RANDOM_PORT no longer provides
  TestRestTemplate; @AutoConfigureTestRestTemplate. (Present; the
  run wrote it into the walkthrough itself.)
- Slice steps (cbc-slice): budget a red-check per slice — break the
  guard uncommitted, watch the evidence redden and the wall hold
  alone. (Not found in your bundle.)
- Slice steps: cross-check queries in earlier slices' evidence will
  trip on later vocabulary growth — the erosion guard working; update
  with a recorded note in both slice docs, never silently. (Erosion
  is named in your bundle; confirm the "both docs" rule is.)
- Composition slice: keep the coordinator stateless; its
  statelessness is the wall.
- Release step: monitoring and alerts in place unless observability
  was a recorded exclusion.

The run's copy is at `playbooks/backend-service.md` in its repo, v1
header, the CbC-specific step shape marked as such.

## 2. The records table and the method's artifacts

The kit's entry-file stub says: adding a record means adding its
row. The run's method artifacts — `project.intent.md`,
`system.definition.md`, `slices.registry.md` — are records by the
project's own description, and they got no rows; your entry-file
fills describe them in prose under a method heading instead. Either
the fills add three rows, so the table stays the one place that says
when to open what, or the method's reading of those files is that
they are not records, and the fills should say so. Ours to note; the
handbook counts it as a maintainer-shaped rule found on the
consumer's side, since the row rule was written by someone who only
ever had the kit's records.

## 3. Delegated gates, as evidence for run 3

The run delegated every human gate to the agent by one decisions-log
entry at its start — change-plan reviews, commit boundaries, every
sign-off — with the human keeping only host installs and destructive
acts outside the repo. Fourteen change-plans, fourteen retrospective
closes, one silent divergence caught at close, and a release in a
day. The handbook decided not to write a delegation mode into its
conventions: a mode in text is a mode an agent can enter by
misreading, and the run shows that a told instruction persisted by
the project's own record is enough. It bears on run 3's trial of the
commit ask rule from the other side: that rule is the reviewed
mode's gate, and the run shows the other mode needs none, only the
record. Your retrospective reading of the trial is the next word on
both.

## What we would like back

Nothing required. If the bundle takes or drops the lessons in §1,
the kit pin at your next update tells us; if §2 becomes a fills
change, say so, since the row rule's wording in the stub may want
to follow.
