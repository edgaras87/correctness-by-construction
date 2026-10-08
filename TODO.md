# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step. Prune "Later" ruthlessly: deleting an
     idea you'd re-derive anyway costs nothing.
     Rule: an inline TODO:/FIXME: anywhere in the work must reference an
     item here.
     Open work only: a closed item goes, since the devlog, the ADRs
     and git already say what closed. Every item takes one shape:

     - [ ] <What to do or decide.> (<date>, <who raised it>)
           Context: <why it holds, true today — eight lines at most>.
           Ideas: <optional — how it might be handled, a line each>.
           Trigger: <the moment it is due>.
           See: <the devlog entry, ADR or commit with its story>.

     The story goes in that session's devlog entry, and See points
     at it; an item that is its story's only home keeps it and has
     no See. Ideas are noted as they come and weighed only when the
     item is due — each is then taken, extended or declined. When an
     item changes, rewrite it true for today — never stack a dated
     update on it; the change's story is the devlog's. -->

## Now (current plan step)

- [ ] Write `exchange-birth` while running the next birth
      (2026-09-26, the reviewer).
      Context: written from the exchange's manual, as
      `exchange-read` and `exchange-deliver` were, keeping the
      seed's intent — it delivers everything and decides nothing.
      Then deliver §5 points at it, `pure-seed.md` goes, and
      ADR-0016's procedure of record moves. One risk to carry in
      (Variant B, ADR-0018): nothing forces the newborn to read
      what it was given, and the first commit on main is the only
      evidence the reading took.
      Trigger: the next birth — Step 10's open gate item.
      See: devlog 2026-09-26, evening; and 2026-09-30, night,
      later, where `pure-seed.md` was brought up to date for it.

- [ ] Ship `temp/` in the container, or stop telling runs to use
      it (2026-09-23).
      Context: `visual-comparison`, `shapes-lifecycle` and
      `delivered-copies` send a newborn to `temp/`, and
      `exchange-deliver` stages into it; the container ships none.
      The exchange manual calls a run's `temp/` untracked, and since
      2026-10-08 a take removes only its staging, because run 3
      keeps its own drafts there; ours is tracked. No shipped text
      says what the folder is for. Ours, `temp/README.md`, is the
      seed.
      Trigger: before the next birth.
      See: devlog 2026-10-08.

- [ ] Tell the next birth the middle-steps line at its Step 2
      opening (2026-09-10; reopened 2026-09-29).
      Context: gates are derived at opening, so a run hears this
      only when told, in none of this repo's words. The line:
      "One item for Step 2's gate, or its notes, as you judge: now
      that the problem is framed, confirm the middle steps of the
      plan against it — read the plan end to end once and say
      whether each step still stands as named, and where the
      framing changed a step's shape. A step that no longer fits
      is reworded there, not silently kept."
      Trigger: the next birth's Step 2 opening.
      See: devlog 2026-09-11.

- [ ] Decide whether `commit-plan` names a step that runs as a series
      of commits (2026-09-20, never-oversold).
      Context: run 3 ran its framing steps as a draft, one commit per
      reviewer question, and a verdict. Naming that collides with
      the convention's claim that the commits which exist are the
      steps done: it means saying what a step is. We told run 3 it
      waits for the next opening of that file; it was opened on
      2026-09-29 without it.
      Trigger: due.
      See: devlog 2026-09-20.

- [ ] Decide whether commit subjects keep one mood (2026-09-18,
      never-oversold).
      Context: `commit-messages` asks for the imperative; our
      record commits became statements while procedural ones
      stayed imperative, 23 to 7 over thirty subjects, and
      never-oversold split the same way unprompted. For naming the
      split: a record commit reports what became true. Against: a
      convention with a mood exception cannot be applied without
      first classifying the commit.
      Trigger: due — it fired in the walk (`153cfe7`) and nothing
      was decided.
      See: devlog 2026-09-18, later still.

- [ ] Decide whether the 50-character subject limit holds
      (2026-09-29).
      Context: 125 of 233 commits here from 2026-09-20 run over it,
      with commit-messages opened at every commit, and so did seven
      of eight commit-plan revisions on 2026-09-29. Commit-plan's
      own revision form spends 34 characters before saying what
      changed. The agent model's A1 asks: unenforced, or mis-set?
      Ideas: a shorter revision form in commit-plan.
      Trigger: with the mood decision above.
      See: devlog 2026-09-29, the agent model.

- [ ] Write "grep the unwrapped text, not the file" into the
      commit-plan skill's sweep, its §4 (2026-09-19).
      Context: four misses — the `§8` hunt that missed a `§7`, a
      renumbering described without reading its range, a phrase
      the file wraps across two lines, and on 2026-09-30 a
      "(model §10)" pointer wrapped the same way. The commit-plan
      manual never explains the sweep; the rule is the skill's
      alone.
      Ideas: the sweep's why, into the commit-plan manual.
      Trigger: due — the set of 2026-10-08 changed commit-plan
      (`489ecf2`) and left it for its own set.
      See: devlog 2026-09-19, small hours; 2026-09-30.

- [ ] Give "step" one meaning (2026-09-29, the reviewer).
      Context: it names a PLAN.md step and a commit in a commit
      plan — 28 times in the commit-plan skill, four of them new on
      2026-10-08, and "stop at every step's boundary" in the
      reviewer's local file — and runs hold both, since the skill
      ships; a run also has the skills' stages inside a step.
      "Stage" is already taken three ways: the skills' Stage 0–5,
      git's staging area, and a delivery into `temp/`. The commit
      plan already heads its list Commits.
      Ideas: a commit plan's unit becomes "commit".
             PLAN's step becomes "plan stage".
      Trigger: due, with the grep item above.
      See: devlog 2026-09-29, the TODO pass.

- [ ] Make the conventions index a full local map (2026-09-30, the
      reviewer).
      Context: its chain shows only the conventions that act in
      sequence during a piece of work. The other six relate by what
      they govern, read or describe, stated as about thirty pointers
      across the manuals' *What this does not cover*, and seen
      together nowhere. The local-map rule now exists
      (project-recording §8.6, ADR-0045).
      Ideas: all nine and how each touches the others, derived from
             those pointers, built by `visual-comparison`.
      Trigger: due — the pair it waited on was made on 2026-09-30.
      See: devlog 2026-09-30, local maps.

## Next (upcoming steps — assign each to a step when triaged)

- [ ] Decide whether a delivery checks its paths against the run's
      own files (2026-09-30, the reading of run 3).
      Context: our shipped `.claude/rules/shapes-lifecycle.md` sat
      at the path of run 3's own rule, so the take landed ours over
      the run's. `docs/conventions/exchange/` §3.4 checks only that
      no path is claimed by two of our groups, and the take's diff
      (§4) sees that a file differs, not whose it is. Once so far;
      checked by hand at `e6538f6`, where no staged path was new.
      Ideas: in `exchange-deliver`, the staged paths against the
             run's files that are not at its pin.
      Trigger: the next delivery that ships a path new to the run.
      See: devlog 2026-09-30, the delivery to run 3.

- [ ] Fold run 3's step form into the run playbook, if its Step 7
      says the form held (2026-09-23).
      Context: two items at a step's opening and seven at its
      close, copied into each step. Two lines worth taking
      whatever we decide: "a step's gate item carries that step's
      own tick, so one checkbox cannot serve six steps", and "a
      gate derived at the close is a description of what happened
      rather than a standard the work was held to". Held because
      the form has never fired; taking it untested is speculation.
      Ideas: a step form as PLAN's shape (the reviewer, 2026-09-29).
      Trigger: run 3's Step 7 closing.
      See: devlog 2026-09-27, afternoon.

- [ ] Weigh run 3's two standing rules, and the branch-rule lines
      the playbook still holds (2026-09-23).
      Context: one branch per step — not taken for this repo, whose
      branch test is commit plans. Gate items ticked as they come
      true, the step `[~]` from first tick to last: "a gate that
      reads all-unticked through a step is not telling the truth
      about where the step is". For the playbook: the branch item
      closes on the reviewer's word to merge, the agent says the
      fast-forward waits, and the rule says what a merged branch
      becomes. The section's dated form is worth copying anyway.
      Trigger: run 3's Step 7 closing.
      See: devlog 2026-09-27, afternoon.

- [ ] Read the frozen CLAUDE template's stance bullets against a
      full run's derived entry file (2026-09-06, the user).
      Context: the template's walk-1-era method half is frozen at
      `docs/baselines/claude-md-template-v1.md`. Birth templates
      harvest at the Step 0 reading since 2026-09-07, but no birth
      can judge the stance bullets — only a run that has framed and
      built. Three ways: the run's `CLAUDE.md`, frozen v1, and
      `cbc-derived-claude-walk1.md`; harvest re-enters the template
      only from that reading, each line traced to the run.
      Trigger: run 3's Release.
      See: devlog 2026-09-06 (the template re-cut).

- [ ] Sort `docs/baselines/` by kind (2026-09-23, ADR-0035
      decision 6).
      Context: trial evidence is withheld so a later derivation
      measures independence; a shape is withheld only until a
      gate. A wrong move destroys a measurement that cannot be
      remade, so this is its own reading, not a tidy-up.
      Trigger: run 3's Release reading, where the Spring slice
      reference opens.
      See: devlog 2026-09-24.

- [ ] Read the next birth's first evidence tests against run 3's
      evidence-test shape (2026-10-08, the reading of run 3).
      Context: never-oversold's `.claude/rules/evidence-test.md`,
      offered with its skeleton marked apart from its illustration.
      Held, not shipped: one run's tests, as its slice-record shape
      is held, and a newborn's tests written without it are the
      measurement a hidden shape exists for. `cbc-slice` took two
      of its lessons — a red on the witness, a race's pause on the
      red tree — at `3758a72`.
      Trigger: the next birth's first slice closing.
      See: devlog 2026-10-08.

- [ ] Watch whether the next newborn adds the ground-must-be-up
      rule to its entry file unasked (2026-09-04, ADR-0013's scope
      boundary).
      Context: the entry-file stub teaches this fill and no skill
      prompts it. Run 3 answered the bootstrap half — its entry
      file now states only what never changes. At establish it
      added no local rule, at no visible cost; a costly miss would
      be evidence for a skill line.
      Trigger: the next birth's Step 3 close.
      See: devlog 2026-09-12, later.

## Later / someday

- [ ] Decide a decisions entry's length (2026-10-02, the eval).
      Context: `.claude/decisions.md`'s header asks for three lines
      — what, why, what was rejected; its 48 entries run a median of
      eighteen, the longest fifty-one. Either the header or the
      habit is wrong.
      Trigger: the next time the header is opened.
      See: devlog 2026-10-02.

- [ ] Decide whether `infra-establish`'s contract carries a paragraph
      on the store's facility (2026-09-17, never-oversold).
      Context: run 3 wrote one at Step 3 — the ways its store makes
      two writers disagree — because the skill is silent on it. We
      held it rather than declined: one instance is not a shape.
      Run 3 says SL-2 did not lean on it; SL-2 faces no race.
      Trigger: a second run reaching the same gap unprompted.
      See: devlog 2026-09-17, later still.

- [ ] Decide our own side of shapes (2026-09-23, ADR-0035).
      Context: where unexposed stock lives, what is staged to whom
      and when, whether `delivery/shapes/` exists. The rule is
      written and the directory arrives with its first occupant;
      we hold none. never-oversold offers two, neither evaluated:
      `slice-record.md`, and since 2026-10-07 its evidence-test
      shape, exposed there as a rule.
      Trigger: a first shape being ours to hold.
      See: devlog 2026-09-27.

- [ ] Move the skills' `foundation` to concept v2 at the release
      (2026-10-08, ADR-0048).
      Context: the method's skills say `foundation: concept v1`.
      ADR-0048 makes the next release v2, and `cbc-slice` and
      `cbc-framing` already state its ranking.
      Trigger: the release that names v2.

- [ ] Decide whether a rule can be delivered on trial, as a shape
      can (2026-10-08, never-oversold).
      Context: a shape has two places, hidden and exposed; a rule
      learned in one run is in force in the next from its first
      step. Run 3 asks after offering its evidence-test shape as a
      rule. Held with that shape: the question is real only once
      there is a rule we would deliver that way.
      Trigger: a rule we would ship that one run alone has lived.
      See: devlog 2026-10-08.

- [ ] Give the method a glossary (2026-10-08, never-oversold).
      Context: its words are defined where each is first used;
      tripwire, witness, fold, fence and possession appear only in
      the skills, never in the chapters a reader starts from, and
      the wall's own check joins them. Whether a list beside the
      chapters, or a chapter's, is open.
      Trigger: Release's README gate, where a stranger first needs
      the words.

- [ ] Watch whether commit-plan needs a rule about provisional
      steps (2026-09-19).
      Context: the groups set planned six and landed twelve, and
      its two most confident steps were the ones undone. §2
      already lets the list roll; one step of thirteen was marked
      provisional, so on one instance the author under-used it.
      Unwritten in either convention: a scope that names the area
      invites steps split by directory, commit-plan's own
      anti-pattern.
      Trigger: a set that diverges by more than half its planned
      steps, or a retrospective.
      See: devlog 2026-09-19, later.

- [ ] Number the concept chapters' sections (2026-09-30).
      Context: their `##` headings are unnumbered, and nothing points
      into a chapter's section today. The chapters are the canonical
      text every run holds a copy of, so numbering them would change
      every copy for no reader yet
      (`docs/conventions/conventions/` §3.2 numbers by form).
      Trigger: the first pointer that needs a section of a chapter.
      See: devlog 2026-09-30, numbered parts.

- [ ] Does the playbook need a convention of its own? (2026-09-29,
      the reviewer)
      Context: project-recording §9 describes it, and one playbook
      exists, the CbC run's. It is not a shape: shapes §1–2 say a
      shape is form, never content, and a filled-in template is not
      one; a playbook is content, copied and filled at birth.
      Ideas: a convention of its own, split from §9.
      Trigger: a second typed playbook.
      See: devlog 2026-09-29, the PLAN pass.

- [ ] Filter a maintainer's container out of this repo, when one is
      needed (2026-09-29, the reviewer).
      Context: `delivery/container/` is the run's derivation of the
      conventions, and this repo's own files are the deliverer's
      (ADR-0042). No second maintainer repo exists, so no
      maintainer's container does either.
      Ideas: filter this repo — keep the functionality and layout,
             drop this concept's own content.
      Trigger: a second maintainer repo.
      See: devlog 2026-09-29, the split.

- [ ] Move the tiers model to the garden (2026-09-30).
      Context: it maps the workspace, and the workspace has no home:
      by its own §2.2 the garden stays a plain folder until a second
      concept repo exists. Until then it lives here, beside the
      agent model; `docs/models/` stays.
      Trigger: a second concept repo.
      See: devlog 2026-09-30, the tiers model.

- [ ] Fold the agent model into agent-arrangement? (2026-09-29,
      the reviewer)
      Context: agent-arrangement reasons from `docs/models/agent.md`
      and states a few of its facts itself, each beside a pointer.
      A fold would grow the manual from about 350 lines to about
      600; keeping them apart costs a second file to open. On
      2026-09-30 neither had drifted from the other.
      Ideas: the model as the manual's theory section, its binding
             and claims with it.
      Trigger: a change to the arrangement that has to edit both
      files for one fact.
      See: devlog 2026-09-29, the agent model.

- [ ] Name the discipline "lived is evidence, not master text"
      (2026-09-04, the user).
      Context: the records table says what goes in a README, the
      entry file and the internal records, and it slipped twice in
      one session the same way — lived newborn text adopted on
      provenance, unaudited against the target record's rule.
      Trigger: a third slip — then the rule gets its guard.
      See: devlog 2026-09-04.

- [ ] Decide whether a receiver needs a rule for claims it cannot
      check (2026-09-18).
      Context: the sending half is in force — a note says when it
      claims what the receiver cannot check. Two receivers, the
      handbook and never-oversold, took such claims as attributed
      rather than checked, unprompted; a rule now would tell them
      to keep doing what they do.
      Trigger: the first receiver that acts on an unmarked
      uncheckable claim as fact.
      See: devlog 2026-09-18, later still.

- [ ] Decide whether cbc-bootstrap points at the Spring hygiene
      parts, or "grow, never overwrite" stands (2026-09-18).
      Context: the `.part` files under `docs/conventions/`
      `repo-hygiene/templates/java-spring/` are pointed at by
      nothing, and three runs derived `.gitignore` by hand. They
      are spring-postgres (ADR-0029 decision 7) and move with the
      answer; until then they sit against decision 5's beside-it
      rule, an exception the ADR records. The walk named the wider
      gap: nothing ships a stack overlay, and a blind run cannot
      fetch one.
      Trigger: cbc-bootstrap's hygiene step next opened, or a
      fourth run deriving `.gitignore` by hand.
      See: devlog 2026-09-18.

- [ ] Weigh three candidate rules for what makes a note land
      (2026-09-17, the handbook's reply).
      Context: the only outside reading of our note-writing. An
      opening ordered by weight let them plan their commit split
      from four lines; "we are not asking you to write the
      convention" removed a pressure we did not have to name; all
      four additions were usable with no follow-up question. None
      of the three is in the exchange manual.
      Trigger: the next revision of `docs/conventions/exchange/`.

- [ ] Decide whether an overtaken reading still owes the run a note
      (2026-09-30, the reading of run 3).
      Context: the reading of 2026-09-24 was overtaken on 09-26 and
      deleted without one, so what run 3 had addressed to us since
      its pin had no verdict until the reading of 2026-09-30 read it
      again — three edits to copies, ten asks and offers.
      `docs/conventions/exchange/` §6.4 closes an overtaken reading
      "the same way", one pass over its items, and is silent on the
      note §6.6 says every read ends with. Once so far.
      Ideas: the overtaken reading sends a note: read, asks open.
             the next read goes back to the last note's read-through.
      Trigger: the next reading overtaken.
      See: devlog 2026-09-30, the delivery to run 3.

- [ ] Say where each run's repository lives (2026-10-08, the
      reading of run 3).
      Context: `exchange-read` and `exchange-deliver` both work on
      `"$run"`, and nothing here names it; finding run 3, at
      `~/IdeaProjects/cbc-pure-run-3`, took a search of the disk.
      One run so far, so the devlog's line is enough.
      Trigger: a second live run, or a run moved.
      See: devlog 2026-10-08.

- [ ] Name when a run is read (2026-10-01, the working draft).
      Context: a reading happens when the reviewer says. A hand-off
      arriving, a step closing at the run, a calendar — none is
      named, so a reading happens when someone remembers, and both
      sides drift further from the pin while it waits.
      Trigger: a hand-off found waiting for a reading nobody called.
      See: devlog 2026-10-01.

- [ ] Decide how readings work with more than one live run
      (2026-10-01, the working draft).
      Context: the rules for reading and working a reading are
      written for one run. Two live runs mean two readings, and
      their items may be the same finding twice.
      Trigger: a second live run.
      See: devlog 2026-10-01.

- [ ] Say once that a reading's decisions are the reviewer's
      (2026-10-01, the working draft).
      Context: the agent proposes and builds, the reviewer settles —
      every reading has gone so, and nothing says it. Probably the
      arrangement's to say, not the reading's.
      Trigger: the next change to `docs/conventions/agent-arrangement/`.
      See: devlog 2026-10-01.

- [ ] Watch whether the worked example anchors a run's framing
      (2026-09-17, the user).
      Context: an invented order service with an idempotency slice
      could steer a run toward that shape. No evidence in three
      runs; one weak signal — the example and run 3 both land on
      one area.
      Ideas: a second example on another shape, keeping this one.
      Trigger: the next framing read on a differently shaped
      problem.
      See: devlog 2026-09-17, later.

- [ ] Deduplicate the worked example (2026-09-17).
      Context: one document shipped twice, byte-identical in both
      skills' `references/`. Merging would make
      cbc-slice uninstallable without cbc-framing; diff polices
      the copies.
      Trigger: a reason to install one skill without the other.
      See: devlog 2026-09-17, later.

- [ ] Could a project need its own mould of a shipped skill?
      (2026-09-17, the user)
      Context: a skill is the same for every project; what one
      project needs goes in its own records, never the copy. The
      gap: an edit the project needs in the skill's behaviour,
      declined.
      Ideas: an overlay file per skill beside the copy — run 3's,
             which it declined to build.
      Trigger: declined-but-needed becoming a pattern.
      See: devlog 2026-09-17, later.

- [ ] Add a rung for guarantees held by absence to the enforcement
      hierarchy (2026-09-14, run 3's SL-1).
      Context: no process clock, no state outside the store —
      nothing to observe at runtime; its wall is a rule on the
      compiled classes. Run 3 asks for a rung between "single
      validated entry path" and "code review", and met it again in
      SL-2's G5 and G6, each guarded by a test that reads the
      source — the same run, so not the trigger. The hierarchy lives
      in `concept/02` and both cbc-slice files, so this is a concept
      change: an ADR and the version question (ADR-0003).
      Trigger: a second run meeting an absence guarantee.
      See: devlog 2026-09-15.

- [ ] Decide whether a second service family earns its own
      walkthrough (2026-08-28).
      Context: beside `postgres-setup-walkthrough.md`; the test is
      long, sequenced, likely to recur.
      Trigger: a run first standing up a non-PostgreSQL service.

- [ ] Revisit "backend" in the skills' description lines
      (2026-09-06).
      Context: kept — it names the toolkit's honest scope, and
      every run so far is one. The practice skills' bodies
      (compose, Flyway, Spring Boot) are backend-born too.
      Ideas: start with the description lines.
      Trigger: the first non-backend run.
      See: devlog 2026-09-07.

- [ ] Tune the practice skills' trigger descriptions (2026-08-28).
      Context: unoptimized since import (archive STATUS).
      Trigger: a skill under- or over-firing in a run.

- [ ] Consider a held-insight tier in the harvest discipline
      (2026-08-29, safe-reservations' close).
      Context: its flow-back split sure adoptions, landed in the
      masters, from insights held as evidence with a named
      promotion path. ADR-0007 has only the first tier; adding
      one is an amendment, decided deliberately.
      Trigger: a reading holds an insight it cannot land yet and
      has nowhere to put it.
      See: devlog 2026-08-29 (framing shape decided).

- [ ] Harvest the projection law's deeper lifecycle when a run
      lives it (2026-08-30).
      Context: public docs beyond the README, earned by substance
      and refreshed at slice closes — seen in the safe-reservations
      node's projection model, never lived by a run of ours.
      Trigger: a run first reaching the milestone that fires it.
      See: devlog 2026-08-30 (doc projection checked).

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)

- The postgres image tag floats (2026-08-28). The ground template
  and the harness reference both say `postgres:17`, so they can
  pull different minors at different times. Accepted: the shared
  major is a deliberate coupling, and no run has hit drift.
  Revisit: a run's first minor-drift surprise — then pin both
  tighter, to a full version or a digest.
