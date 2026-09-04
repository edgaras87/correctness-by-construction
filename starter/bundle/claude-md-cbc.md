<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Provenance — merged once, 2026-09-04 (ADR-0014),
     from the first newborn's derived CLAUDE.md section
     (cbc-newborn 8f167c4, paths as revised by its docs/ layout,
     d7d2817) and the withheld snippet baseline
     (docs/baselines/cbc-startup-snippet.md, ADR-0012).
     Merge verdicts: the stance and local-rule lines survive from
     the derivation verbatim; its concept summary and step-routing
     rows were dropped at the merge review — restatement beside
     the master, and step numbers that lie once framing renumbers
     the plan — not as comparison losses; its records-carry-the-
     method mapping ships through the birth fills instead, each
     rule riding in the record it governs. From the snippet only
     the pre-framing guard enters: the registry rule already lives
     in cbc-slice (Stage 0, the close step), the human sign-off
     gates in cbc-framing and cbc-slice (ADR-0013). No birth
     derives this again.

     Use: assembly step 3 (starter/bundle/birth-scenario.md)
     merges each fragment below into the kit's CLAUDE.md stub at
     the slot its marker names. Shipped text — after birth the
     copy is the newborn's own arrangement, maintained by it;
     improvements flow back here as harvest, never as per-birth
     rewrites. -->

# CLAUDE.md text — the bundle's fragments for the kit stub

<!-- fragment: cbc-section — insert as a top-level section after
     the stub's opening paragraph, before "## Records". -->

## Correctness by construction

The method is in `docs/concept/` — read `00-cbc.md` first; the
other four chapters deepen it. It is not restated here: the order
of questions (promise → guarantees → structure → features → code,
never backwards) lives there, and each record's birth fill carries
the method's reading of that record.

Until the framing artifacts exist (cbc-framing creates them, under
`docs/system/`), the project is pre-framing: the only method work
is running cbc-framing jointly with the human — never invent the
artifacts to fill the gap.

<!-- /fragment -->

<!-- fragment: conventions-row — append at the end of the stub's
     Conventions list. -->

- Method — `docs/concept/` (correctness-by-construction; not a rulebook,
  an ordering of questions)

<!-- /fragment -->

<!-- fragment: stance-lines — the stub's "How to work here"
     section body. -->

- Design conversations before build conversations. Framing runs on
  paper; no language, store, or framework is named before the first
  slice.
- When asked for a feature, ask which guarantee it serves. If none,
  the answer is a recorded refusal, not a quiet yes.
- Name the kill, not the cure: state what dies under an attack before
  choosing a mechanism.
- Prefer the wall over the test. A green test proves the wall was
  there once; only structure makes the attack meaningless.
- Watch for the rot: a feature shipped without re-checking guarantees,
  an admin path around the single entry, guarantees drifting into the
  test suite, theory before the world is bounded.

<!-- /fragment -->

<!-- fragment: local-rules — the stub's "Local rules" section
     body. The first line ships only while the birth-scenario
     trial runs; the trial-closing ADR removes it from this file.
     The second is permanent until the briefing lands, after which
     the newborn may retire it from its copy. -->

- Step 0 here is a trial of `docs/birth-scenario.md`: it is the
  procedure, and every divergence from it is written into the
  devlog, not fixed silently.
- Nothing before the briefing names the problem.

<!-- /fragment -->
