<!-- The CbC run playbook, pure shape — the only playbook:
     ADR-0016 (2026-09-06) adopts pure and retires the parent,
     cbc-run-playbook.md, whose full header lives in git history
     at that path. Provenance, condensed from it: checked against
     concept v1 (ADR-0003, ADR-0005 — practice-born). Middles and
     warnings harvested 2026-08-30 from the two lived runs,
     read-only (ADR-0007, ADR-0009): Ground / Bootstrap / Slices
     / Release and their warnings from checkout-system's
     retro-folded playbook and its PLAN as lived; the Define step
     from safe-reservations log.md Entry 0001. Rebuilt as a full
     sequence on the kit's default.md (ADR-0011); kit steps last
     re-vendored from the handbook's starter/playbooks/default.md
     v2 @ c670fe5. Harvest lands here — the one copy that exists
     (ADR-0007); kit-owned steps (0, 1, N) change only by refresh
     against a new kit pin.
     Born 2026-09-05 as the pure-seed candidate variant
     (starter/installs/pure-seed.md). v1 deltas against the
     parent: the assembly (CbC) Step 0 comment and the (CbC)
     gate item's install-manual clause dropped — no place in the
     pure design; and the channel split — the kit's
     first-session comment and the agent-side gates leave Step 0
     for the firing prompt and the run's own change-plan, and
     the briefing opens Framing as its starting input, so Step 0
     closes clean, no gate born blocked.
     v2 (2026-09-06): Framing gains the entry-file retirement
     gate item.
     v3 (2026-09-06, provisional, user's design — the gates
     experiment): the middle steps keep their name, their skill
     pointer, and their goal; their gates, records lines, and
     warnings from past runs are stripped to a derive-at-opening
     instruction, and v2 is frozen whole at
     docs/baselines/cbc-run-pure-playbook-v2.md for the per-step
     derived-vs-frozen reading (the TODO item holds the
     protocol: warnings handed to the run only after each
     derivation is recorded). -->

# Playbook: CbC run — pure

Playbook version: v3 (2026-09-06, provisional — middle gates
derived at step opening; v2 2026-09-06, retirement gate item;
v1 2026-09-05, variant of cbc-run v3)

## Step 0: Bootstrap                                [~]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; re-cut for the pure design per the header. -->

Goal: the container exists — repo, records, arrangement — before content.
Gate:
- [ ] Repo initialized; hygiene base files present.
- [ ] Every placeholder filled, or explicitly deferred to a named
      step (the stack overlay defers to Framing, which confirms the
      steps that fill or delete it).
- [ ] No fill-comment remains: where a comment says its content
      replaces it, the content is there and the comment is not.
      Every other stub comment is a standing rule — it stays.
Notes:

## Step 1: Framing                                  [ ]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; additions marked (CbC). -->

<!-- CbC: this step opens on the briefing — its starting input,
     the first prompt of project work. The README purpose
     paragraph and the devlog's briefing line land here; names
     given before it are working names. -->

<!-- CbC: these gates are met via the cbc-framing skill — the
     intent, definition, and adversity registry are the problem
     statement, success criteria, and out-of-scope in the method's
     richer form. The middle-steps gate item confirms the step
     sequence, which came whole at birth; each middle step's gate
     is its own — authored when that step opens, as its Gate line
     says. -->

Goal: know what we're building and why, before code.
Gate:
- [ ] One-paragraph problem statement in README.
- [ ] Success criteria written (how we'll know it worked).
- [ ] Out-of-scope list written.
- [ ] Middle steps stand and the plan reads end-to-end once,
      coarsely — the playbook's confirmed against the framed
      problem where a typed one was copied in, written fresh here
      where the project was born on this bare default; birth
      materials brought with the briefing weigh in either way.
- [ ] Every step whose gate makes something true that the outside
      should see names its projection as a gate item — the README
      section, the ARCHITECTURE change. Projection follows truth,
      and the gate is where it is caught.
- [ ] (CbC) Entry-file lines the briefing made false are retired
      in this set; every temporary line still standing names a
      later step as its end.
Notes:

## Step 2: Define (naming)                          [ ]

Goal: the project's public identity decided, not defaulted.
Gate: derived when this step opens — verifiable facts, from the
goal and the run's own records; written into this step before
its work starts.
Notes:

## Step 3: Ground / infrastructure  (infra-establish)    [ ]

Goal: services stood up, constrained to need, verified both ways.
Gate: derived when this step opens — verifiable facts, from the
goal, the named skill, and the registry; written into this step
before its work starts.
Notes:

## Step 4: Skeleton & bootstrap  (cbc-bootstrap)    [ ]

Goal: an empty but buildable, testable, runnable system wired to the
real ground, with the evidence harness proven on one adversity.
Gate: derived when this step opens — verifiable facts, from the
goal, the named skill, and the registry; written into this step
before its work starts.
Notes:

## Steps 5..N-1: Invariant slices  (cbc-slice, one step per stage)

Goal: each registry slice closed by evidence that creates its
adversity; ordering re-decided at each close, never assumed from
the original expectation.
Gate: derived when each stage opens — verifiable facts, from the
goal, the named skill, and the registry; written into the stage
before its work starts.
Notes:

## Step N: Release                                  [ ]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; additions marked (CbC). -->

Gate:
- [ ] CHANGELOG entry for the release.
- [ ] README true for a stranger; any commands verified on a clean
      machine.
- [ ] Known issues filed in TODO.md, not just remembered.
- [ ] (CbC) Monitoring/alerts in place — unless observability was a
      recorded exclusion (it was, for checkout-system's
      correctness-portfolio shape; a deployed service should not
      skip it).
- [ ] (CbC) Deploy/rollback procedure documented and tried once —
      same caveat: locally-runnable-only was a recorded exclusion
      there.
Notes:
