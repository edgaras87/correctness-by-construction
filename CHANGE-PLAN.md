# Change-plan: adopt the app-structure reference

## Summary — the state after all commits

cbc-bootstrap's references gain `app-structure.md`: the application-
structure decision surface. It carries three things and no more —
the **lived default** (package-by-feature, package-private
boundaries, structural depth earned per feature; harvested from
checkout-system's shape, read read-only), the **decision hook**
(structure is decided at the run's bootstrap and recorded in the
run's log with its why, exactly as the stack decision is; the
recorded decision governs all later code, slices included), and the
**vocabulary** of the named alternatives (classic layered;
hexagonal / onion / clean; vertical slice; modular monolith —
Spring Modulith), each in one or two honest lines, each marked
unlived in any run of this concept. Deliberately absent: pros/cons
essays — re-derivable in conversation, and they would stale. The
walkthrough's stage 1 (where the run records its governing
decisions) points at it.

## Commits

**1. `docs(executions): add app-structure reference`**
The doc lands beside the walkthrough with a provenance header: the
default harvested from checkout's lived shape (ADR-0007), the
alternatives' vocabulary authored here (nothing lived to harvest —
said so honestly), the reach-through-the-run's-log rule stated in
one line.

**2. `docs(executions): route walkthrough to app structure`**
Stage 1 ("Record the stack decision") grows the structure decision
beside the stack decision, pointing at the reference; the
walkthrough's header records the re-derivation (ADR-0007
header-as-change-log).

## Decisions taken inside this plan

- **One doc, not two.** The user's recall and the agent's vocabulary
  are the same truth; splitting them would make two masters.
- **Reference side of ADR-0008's boundary** — imitated decision
  surface, nothing to paste or fill. Application code itself stays
  out, per the harness reference's precedent; this doc carries
  names and rules, not source.
- **Home: cbc-bootstrap, reach: the run's log.** The decision is
  made at bootstrap, so the doc lives there; slice work already
  operates under the run's logged decisions, so no cbc-slice
  pointer is added — the doc states its reach in one line instead
  of coupling two skills.
- **Unlived alternatives are named, not endorsed.** Choosing one is
  off-default: logged with its why (a stated practice intent is a
  legitimate deciding input, per the stack decision's own "fluency
  and audience" precedent), expected to harvest.
- **Correction recorded, not rewritten.** The 2026-08-29 devlog
  entry refers to a TODO Later trigger line "parked 2026-08-28"
  that was never actually committed — the claim was made in
  session but no edit happened. The devlog's never-clean-up rule
  stands: the old entry stays as written; the session-close entry
  for this change set records the correction as a new fact. No
  TODO commit exists in this plan for the same reason — there is
  nothing to absorb.
- **No ARCHITECTURE change** — a new file inside an existing
  `references/` directory changes no shape (standing call from the
  Step 6 templates and the harness reference).
