<!-- Draft — the pure-seed candidate (2026-09-05). A variant of
     cbc-run-playbook.md (v3, this repo — provenance, harvest
     history and the kit-vendor base live in its header), created
     for the pure-seed experiment (starter/installs/pure-seed.md).
     The steps are the parent's except the deltas below; the
     parent is the procedure of record, and harvest lands there
     first. v1 deltas (2026-09-05): the assembly (CbC) Step 0
     comment and the (CbC) gate item's install-manual clause
     dropped — no place in the pure design; and the channel
     split — the kit's first-session comment and the agent-side
     gates leave Step 0 for the firing prompt and the run's own
     change-plan, and the briefing opens Framing as its starting
     input, so Step 0 closes clean, no gate born blocked.
     v2 (2026-09-06): Framing gains the parent's entry-file
     retirement gate item, by re-derivation.
     v3 (2026-09-06, provisional, user's design — the gates
     experiment): the middle steps keep their name, their skill
     pointer, and their goal; their gates, records lines, and
     warnings from past runs are stripped to a derive-at-opening
     instruction, and v2 is frozen whole at
     docs/baselines/cbc-run-pure-playbook-v2.md for the per-step
     derived-vs-frozen reading (the TODO item holds the
     protocol: warnings handed to the run only after each
     derivation is recorded). Kit steps (0, 1, N) stay vendored
     whole — their gates are the kit's text, not this repo's
     harvest. Lifespan: the experiment's reading decides — of
     this file and the parent, the winner stays and the other is
     deleted; until then this file changes only by re-deriving
     from the parent, the v3 strip excepted. -->

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
