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
     derivation is recorded).
     v4 (2026-09-06, provisional, user's design — the strip goes
     whole-playbook): Bootstrap and Framing lose their vendored
     kit gates and kit comments too; every step but Release now
     derives its gate at opening. Release keeps its vendored
     text as the one fixed endpoint, so the kit-refresh rule
     above now reaches only Step N. No new baseline: v2 holds
     every stripped gate whole, kit text included.
     v5 (2026-09-07, harvested from run 3, read-only —
     ~/IdeaProjects/cbc-pure-run-3, its commit da27510 and TODO
     Later item): Release joins the derive-at-opening form — a
     Goal line, the gate derived when the step opens. The kit's
     three gate facts stay vendored inside a "Known already"
     line, so the kit-refresh rule still reaches them and no kit
     gate item is weakened (ADR-0011); the two (CbC) items no
     longer carry checkout-system's recorded exclusions — a
     prior run's conclusion in shipped text, which the pure seed
     excludes on purpose — and read "unless this run's own
     recorded exclusion" instead. The step's kit-provenance
     comment goes with the strip, as Steps 0 and 1's did at v4:
     the pin lives in this header only, and no step ships a path
     the newborn cannot see. v4's "one fixed endpoint" clause is
     superseded by this paragraph. -->

# Playbook: CbC run — pure

Playbook version: v5 (2026-09-07, provisional — Release derives
its gate at opening too, the kit's three facts kept as Known
already, harvested from run 3; v4 2026-09-06, every gate but
Release's derived at step opening; v3 2026-09-06, middle strip;
v2 2026-09-06, retirement gate item; v1 2026-09-05, variant of
cbc-run v3)

## Step 0: Bootstrap                                [~]

Goal: the container exists — repo, records, arrangement — before content.
Gate: derived when this step opens — verifiable facts, from the
goal and the newborn's own records; written into this step before
its work starts.
Notes:

## Step 1: Framing  (cbc-framing)                   [ ]

<!-- CbC: this step opens on the briefing — its starting input,
     the first prompt of project work. The README purpose
     paragraph and the devlog's briefing line land here; names
     given before it are working names. -->

Goal: know what we're building and why, before code.
Gate: derived when this step opens — verifiable facts, from the
goal, the named skill, and the briefing; written into this step
before its work starts.
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

Goal: the system handed to its audience — the promise shipped,
observable, and reversible wherever it deploys.
Gate: derived when this step opens — verifiable facts, from the
goal, the run's records, and the exclusions framing recorded.
Known already: a CHANGELOG entry for the release; README true for
a stranger, its commands verified on a clean machine; known
issues filed in TODO.md. Decided at framing, checked here:
monitoring and alerts in place; deploy and rollback documented and
tried once — each unless this run's own recorded exclusion.
Notes:
