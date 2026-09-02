<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Provenance — archive/cbc/system-design-method
     birth-materials/cbc-startup-snippet.md
     @ fe0075d (imported 2026-08-28, PLAN Step 3). Changes on
     import: none — verbatim below this header.
     Re-derived 2026-08-29: the framing exports' paths — they live
     under docs/system/ as intent.md, definition.md, registry.md
     (cbc-framing's layout re-derivation).
     Withheld from births 2026-09-02 (ADR-0012): out of the bundle,
     held here as a baseline. Written from theory before any birth;
     the comparison point is the first walked birth's derived
     CLAUDE.md section, and stay/retire/merge is decided at that
     trial's close. Blind: not shown to newborns, like the
     safe-reservations-v1 baseline. -->

# CbC startup snippet

*Merge this into the project's agent definition (CLAUDE.md or equivalent).
It carries only the CbC discipline — recording, conventions, and everything
else about how the project runs are the project's own decisions, made
there, not here.*

---

This project follows correctness-driven design (CbC). The concept is in
`concept/` (read `00-cbc.md` first); the two workflows are installed as
skills: `cbc-framing` and `cbc-slice`.

## Method state

- The framing artifacts live under `docs/system/`: `intent.md`,
  `definition.md`, and `registry.md`. The registry is the source of
  truth for what to work next; ordering is re-decided at each slice
  close, never assumed from the original expectation.
- If the framing artifacts do not exist yet, the project is pre-framing:
  the only method work available is running the cbc-framing skill jointly
  with the human. Do not invent artifacts to fill the gap.

## Gates that need the human

- Never start slice work without the cbc-slice skill's Stage 0 readiness
  check. If any of R1–R6 fails, help with bootstrap as ordinary project
  work — do not open Stage 1.
- Stage 1 (correctness spec) and Stage 2 (plan) outputs require explicit
  human sign-off before proceeding. Readiness sign-off is also the
  human's.
- In framing, every step exit, saturation call, and fork resolution is the
  human's verdict — present the derivation, then ask.

## Standing guards (apply in every session, not just slice work)

- A feature request touching state covered by a closed slice: re-check
  that slice's spec before shipping (guarantee erosion guard).
- Any new admin path, script, or migration is checked against the walls
  it might bypass (escape-hatch guard).
- If a guarantee's structural wall is weakened and only its test remains,
  say so — the guarantee has moved from structure to sampling.
- Deviating from a spec, a plan, or a workflow is legal; deviating
  silently is not. Where and how deviations are recorded is the project's
  decision — the discipline only requires that they are.
