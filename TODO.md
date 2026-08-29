# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step or weekly. Prune "Later" ruthlessly:
     deleting an idea you'd re-derive anyway costs nothing.
     Rule: inline TODO:/FIXME: comments in code must reference an item here. -->

## Now (current plan step)

- [ ]

## Next (upcoming steps — assign each to a step when triaged)

- [ ] Framing check, two runs in order: (1) checkout-system's
      framing artifacts vs the cbc-framing skill + concept —
      artifacts exist, process unrecorded (run on auto); (2)
      safe-reservations' framing process vs the workflow, at
      archive .../worksites/safe-reservations/problem-framing-node
      — process recorded jointly, but in the old custom maintenance
      language: distinguish and never adopt, only the framing logic
      counts. Both read-only (ADR-0007); harvest corrections.
- [ ] After both checks: decide the framing record shape — one full
      derivation doc translated at close into the three exports
      (intent, system definition, slice registry), full doc kept as
      archive of the derivation. Hypothesis for now; decide as a
      harvest with both runs' evidence, and check whether
      safe-reservations' multi-doc checkpoints had a reason (e.g.
      resumability) the one-doc shape must preserve. Also settles
      where the working doc lives during "all paper, no repo".
- [ ] After the framing check: safe-reservations' doc-projection
      node — different levels of visibility of project truths — is
      a capability this concept doesn't have; check what it is and
      whether it earns a place here. Same language rule applies.

## Later / someday

- [ ] First lived use of the practice skills in their imported form
      is owed (archive STATUS: they are distillations, exercised as
      agent-driven skills never, as skills-without-agents never) —
      expect corrections; harvest them when they come.
- [ ] Second service family: when a non-PostgreSQL service first
      gets stood up in a run, decide whether it earns its own
      walkthrough beside postgres-setup-walkthrough.md (the test:
      long, sequenced, likely to recur).
- [ ] Trigger descriptions of the practice skills are unoptimized
      (archive STATUS); if they under- or over-fire in runs, the
      descriptions are the knob.
- [ ] The postgres image tag floats: the ground template and the
      harness reference both say postgres:17, so ground and harness
      can pull different minors at different times — noticed while
      discussing the harness reference. If a run ever hits a
      minor-drift surprise, decide whether both should pin tighter
      (full version or digest); until then the shared major is the
      deliberate coupling.
- [ ] The three framing export names (project.intent.md,
      system.definition.md, slices.registry.md) carry the old
      workbench dot-suffix kind-tagging — noticed 2026-08-29 when
      the new derivation doc deliberately got the hyphenated form
      (framing-derivation.md). Decide whether the exports rename to
      match this repo's convention or stay grandfathered as lived
      names; if renaming, the skill's export section, the registry
      template, and checkout's precedent all move together.
- [ ] checkout-system reads the db port as CHECKOUT_DB_PORT while
      its .env.example names POSTGRES_PORT — two env keys for one
      fact, found at template extraction. If it is a defect, fix it
      in the run first, then harvest; the templates carry it as
      lived.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)
