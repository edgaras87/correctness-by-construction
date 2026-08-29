# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step or weekly. Prune "Later" ruthlessly:
     deleting an idea you'd re-derive anyway costs nothing.
     Rule: inline TODO:/FIXME: comments in code must reference an item here. -->

## Now (current plan step)

- [ ]

## Next (upcoming steps — assign each to a step when triaged)

- [ ]

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
- [ ] Two-tier harvest idea, from safe-reservations' close: its
      flow-back split sure adoptions (landed in the masters) from
      insights held as evidence with a named promotion path (the
      next run's comparison confirms or kills them). ADR-0007 has
      only the first tier. Consider whether a held-insight tier
      earns a place in the harvest discipline — an ADR-0007
      amendment, decided deliberately, not in passing.
- [ ] A define phase lived in safe-reservations between framing and
      bootstrap: project name (under a naming rule), repo name, and
      remote repo description, each decided with verdicts. No skill
      here covers that gap — cbc-bootstrap territory; consider a
      small addition when bootstrap next gets touched.
- [ ] The projection law's deeper lifecycle is unharvested: public
      docs beyond the README, earned by demonstrated substance and
      refreshed at slice closes — cbc-slice-close territory, seen
      in the safe-reservations node's projection model
      (2026-08-30) but never lived by a run of ours. Harvest when
      a run first reaches the milestone that fires it.
- [ ] checkout-system reads the db port as CHECKOUT_DB_PORT while
      its .env.example names POSTGRES_PORT — two env keys for one
      fact, found at template extraction. If it is a defect, fix it
      in the run first, then harvest; the templates carry it as
      lived.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)
