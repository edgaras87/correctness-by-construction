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

- [ ] Make the conventions index a full local map (2026-09-30, the
      reviewer).
      Context: its chain shows only the conventions that act in
      sequence during a piece of work. The other eight relate by what
      they govern, read or describe, stated as about thirty pointers
      across the manuals' *What this does not cover*, and seen
      together nowhere. The local-map rule now exists
      (project-recording §8.6, ADR-0045).
      Ideas:
      - all twelve and how each touches the others, derived from
        those pointers, built by `visual-comparison`.
      - three links, each with its upkeep: derives (conventions
        §3.5, the foundation check), points (one home, a step's
        close), governs (none: a change to a rule that governs
        other text could sweep that text or file the sweep, a rule
        beside §3.5).
      - scenarios as entries into one procedure, the foundation
        check: a manual, a skill or rule, a run's finding. Two
        exits it lacks: the governs sweep, and what must run again
        after.
      Trigger: due — the pair it waited on was made on 2026-09-30.
      See: devlog 2026-09-30, local maps.

- [ ] Decide whether a TODO item's story is written when the item
      is added (2026-10-17, the reviewer).
      Context: TODO's header sends an item's story to that
      session's devlog entry, written at the session's end. By
      then the reasons are cut to a line, and an item added
      mid-session has no See until then. Tried on five items on
      2026-10-17, the refinement first.
      Ideas: TODO's header gains "when the item is added", and
             project-recording says it for both seats.
      Trigger: due — the third item was written this way on
               2026-10-17.
      See: devlog 2026-10-17, the refinement.

## Next (upcoming steps — assign each to a step when triaged)

- [ ] Read run 4 against `dac4dd1`, the run 3 commit it was born
      from (2026-10-15, the reviewer).
      Context: run 4, safe-reservation-2, was born 2026-10-15 by
      hand from run 3's skills, rules and shapes at `dac4dd1` and
      our container at `35edd3f`, and ran on full auto through
      Release. Reading it shows what it changed on top of
      `dac4dd1`, what of run 3's asks it answered, what still has
      to be checked, and what is new. It left twelve lines under
      To the deliverer.
      Ideas: run 3's and run 4's `RETRO.md` read against the
             retrospective skill's form, for a shape (ADR-0054).
      Trigger: run 3's reading closes; in a new session.
      See: `f097695`, the kickoff and the message it took.

- [ ] Decide whether our own forms become shapes, and whether a
      shape's part can be optional (2026-10-17, the reviewer).
      Context: a shape is read at a step's gate only, so the work
      is not shaped by it (`docs/conventions/shapes/` §1). Our own
      forms, a reading's and a manual's, are rules that load while
      the file is written. They kept that place because this repo
      had no steps; since ADR-0057 it has.
      Ideas:
      - the work's rules keep what must hold while working, such as
        numbers never changed; the forms become shapes.
      - a part a shape names may be optional, where the work does
        not always produce it.
      - Known already as questions, a skill's Gates and the
        playbook's lists, answered in a step's own words.
      Trigger: run 4's reading, which reads how run 4 lived run 3's
               shapes.
      See: devlog 2026-10-17, our forms as shapes.

- [ ] Refine this repo against its own rules (2026-10-17, the
      reviewer).
      Context: most of the text predates its rules: writing and
      one-home (ADR-0053), the foundation check (2026-10-17), a
      lesson written in general (conventions §3.7, 2026-10-18). The
      rules guard new and changed text; older text is rewritten in
      work of its own, and this is that work. W8 of the reading of
      run 3 joined it at that reading's close (2026-10-18).
      Ideas:
      - dependencies: a retelling becomes a pointer, and a pointer
        stays only if needed (conventions §3.1).
      - seats: a deliverer seat says how its convention works here,
        nothing more; project-recording's first (the playbook, why
        runs keep steps).
      - plain language: living text older than ADR-0053.
      - stale lines: each one noticed and not fixed where found.
      - one home: facts told in several places, such as how the
        seats differ, told in five (W8).
      - foundations: every `foundation` line read once against its
        manual; the check reads only what changes.
      - lessons: each manual's body read against conventions §3.7;
        a case written as the rule becomes a general statement,
        the case its dated italic. *What it is for* keeps its
        case, since its evidence is one by design.
      - words: "run" as a verb for skills and steps, beside "run"
        the project; say "uses".
      - words: "small steps" in `commit-plan` (ADR-0050), a third
        "step" beside PLAN's and a numbered list's.
      Trigger: the reading of run 3 closes.
      See: devlog 2026-10-17, the refinement.

- [ ] Write a rule that writes a skill or rule from its convention
      (2026-10-17, the reviewer).
      Context: conventions §2 says how a skill or rule is written,
      and nothing puts it in front of the writer: a manual has
      `convention-manual.md`, a skill or rule has no such rule.
      First-time work writes freely, and its output is input: what
      the work needed. The lasting form comes from the conventions
      convention, the manual by §3 and each skill or rule from it
      by §2.
      Ideas:
      - a rule derived from §2, as `convention-manual.md` is from
        §3, on `.claude/skills/`, `.claude/rules/` and `delivery/`.
      - a `paths:` rule loads only on a Read; the commit is the
        other moment (`.claude/decisions.md`, 2026-10-17).
      - first-time work's close hands its output to the rule, in
        both seats.
      - our draft moves out of `docs/conventions/` to be free;
        ADR-0056 put it there, on trial.
      - shipped or ours only: a run writes no conventions, so its
        draft may stay free until a reading rewrites it.
      Trigger: the next first-time work's close, here or offered by
               a run.
      See: devlog 2026-10-17, later, the skill rewrite.

- [ ] Rewrite the method's texts plain (2026-10-17, run 3's RETRO
      D2).
      Context: the agent copies the voice it reads. Run 3's records
      came out in the skills' voice, though "explain plainly" was in
      its memory. Plain already: the rules, the shapes, `cbc-slice`'s
      skill and workflow (`2674c03`). Not yet, about 26,000 words:
      `cbc-framing` (8,500), the stack skills (13,800), the concept
      chapters (3,400), readiness (600). A chapter reworded is a
      concept change, editorial unless a meaning moves.
      Ideas:
      - one commit per file; the worked example's two copies as one.
      - the fenced collisions as "nothing dies" kills, as the kill
        shape asks; the example's kill count and reconciliation move.
      - "invariant-shaped", "contract-shaped": "shape" is a defined
        word now.
      - chapter 02's "scope creep wearing a safety costume".
      Trigger: before run 5's birth, as a step of its own.
      See: devlog 2026-10-17, later, the plain method.

- [ ] Rebuild project-recording §1 as a map of the records, in both
      seats (2026-10-17, the reviewer).
      Context: no one view says which record answers what. §1 draws
      a run's records only, and leaves out RETRO.md, COMMIT-PLAN,
      `docs/system/`, the one-home rule, and records another
      convention owns, such as the decisions log (agent-arrangement
      §3.4). The deliverer's differences are prose under its seat.
      W14 of the reading of run 3 met this three times.
      Ideas:
      - a section of the manual, §1 rebuilt; a file beside it was
        weighed against conventions §3.1.
      - the form chosen by `visual-comparison`: a picture, a table,
        or both.
      - per record: the question it answers, the convention that
        owns it, and how each seat differs.
      Trigger: the refinement item opens; built with it.
      See: devlog 2026-10-17, later, the records map.

- [ ] Decide whether a newborn reads `.claude/shapes/` at birth
      (2026-10-17, the reviewer).
      Context: the seed's prompt says "Read the whole repository
      first, every file", and the method's four shapes are among
      them (ADR-0052; named since `141fa74`). A shape is read at a
      step's gate only, so run 5 would see every shape before its
      first output. Run 5's second slice judges gate-only, and that
      judgement would not be clean.
      Ideas:
      - the prompt leaves `.claude/shapes/` out of its read.
      - left as is, and run 5's gate item says the shapes were read
        at birth.
      Trigger: before run 5's birth, with its item.
      See: devlog 2026-10-17, later, shapes at birth.

- [ ] Birth run 5 from this repo alone, holding one pin, and write
      `exchange-birth` while it runs (2026-09-26, the reviewer; the
      birth itself from Step 10, ADR-0057).
      Context: written from the exchange's manual, as
      `exchange-read` and `exchange-deliver` were, keeping the
      seed's intent — it delivers everything and decides nothing.
      Then deliver §5 points at it, `pure-seed.md` goes, and
      ADR-0016's procedure of record moves. One risk to carry in
      (Variant B, ADR-0018): nothing forces the newborn to read
      what it was given, and the first commit on main is the only
      evidence the reading took.
      Ideas: first-time work on our seat, so a provisional manual,
             `first-time-work`'s first trial here (ADR-0056).
      Trigger: the reviewer names run 5's birth; it opens as a step.
      See: devlog 2026-09-26, evening; and 2026-09-30, night,
      later, where `pure-seed.md` was brought up to date for it.

- [ ] Run this repo's retrospective, on trial (2026-10-17, from
      Step 10's gate).
      Context: `docs/conventions/retrospective/`, the deliverer's
      seat, says what it is: both skills run on this repo, from
      `delivery/container/`, and a verdict on whether we hold them.
      Step 10's gate held it until ADR-0057.
      Trigger: the close of the step that runs run 5's birth.
      See: ADR-0057, decision 4.

- [ ] Ship `temp/` in the container, or stop telling runs to use
      it (2026-09-23).
      Context: `visual-comparison` and `delivered-copies` send a
      newborn to `temp/`, and `exchange-deliver` stages into it; the
      container ships none.
      The exchange manual calls a run's `temp/` untracked, and since
      2026-10-08 a take removes only its staging, because run 3
      keeps its own drafts there; ours is tracked. No shipped text
      says what the folder is for. Ours, `temp/README.md`, is the
      seed.
      Trigger: before the next birth.
      See: devlog 2026-10-08.

- [ ] Decide whether a delivery checks its paths against the run's
      own files (2026-09-30, the reading of run 3).
      Context: our shipped `.claude/rules/shapes-lifecycle.md` sat
      at the path of run 3's own rule, so the take landed ours over
      the run's. `docs/conventions/exchange/` §3.4 checks only that
      no path is claimed by two of our groups, and the take's diff
      (§4) sees that a file differs, not whose it is. Once so far;
      checked by hand at `e6538f6`, where no staged path was new.
      The method's four shapes now sit at run 3's own
      `.claude/shapes/` paths (ADR-0052): the next delivery to run 3
      is this trigger.
      Ideas: in `exchange-deliver`, the staged paths against the
             run's files that are not at its pin.
      Trigger: the next delivery that ships a path new to the run.
      See: devlog 2026-09-30, the delivery to run 3.

- [ ] Read the frozen CLAUDE template's stance bullets against a
      full run's derived entry file (2026-09-06, the user).
      Context: the template's walk-1-era method half is frozen at
      `docs/baselines/claude-md-template-v1.md`. No birth can judge
      the stance bullets — only a run that has framed and built.
      Three ways: the run's `CLAUDE.md`, frozen v1, and
      `cbc-derived-claude-walk1.md`; harvest re-enters the template
      only from that reading, each line traced to the run. Run 3
      skipped its Release (2026-10-15); run 4 released the same
      project, so its entry file is read, run 3's beside it.
      Trigger: run 4's reading.
      See: devlog 2026-09-06 (the template re-cut).

- [ ] Sort `docs/baselines/` by kind (2026-09-23, ADR-0035
      decision 6).
      Context: trial evidence is withheld so a later derivation
      measures independence; a shape is withheld only until a
      gate. A wrong move destroys a measurement that cannot be
      remade, so this is its own reading, not a tidy-up. The
      Spring slice reference opens once, at a run's Release
      (ADR-0033); run 3 skipped its Release, and run 4 had one.
      Trigger: run 4's reading, where the Spring slice reference
               opens.
      See: devlog 2026-09-24.

- [ ] Read what run 5's first slice gate found against the
      evidence-test shape (2026-10-08, the reading of run 3).
      Context: the shape ships with the method since ADR-0052, read
      only at the gate. A newborn writes its first tests without it,
      and its first slice's close reads them against it: the
      differences are the measurement. Run 4 held run 3's shape from
      birth, so run 5 is the first clean one, unless it reads the
      shapes at birth (the item on `.claude/shapes/`). `cbc-slice`
      holds most of its lessons, so tests from the skill alone may
      meet it.
      Trigger: run 5's first slice closing.
      See: devlog 2026-10-08; and 2026-10-10.

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

- [ ] Release concept v1 (2026-10-17, from PLAN's Step N).
      Context: so a stranger, or future-you, can read, cite and copy
      from this repo without the archive. Four items of its own:
      a CHANGELOG entry for the release; README true for a
      stranger; `docs/models/` checked against the repo, since
      `CLAUDE.md` sends a stranger there; known issues filed here.
      PLAN held it until ADR-0057.
      Trigger: the reviewer names it, after the step that runs run
               5's birth closes.
      See: ADR-0057, decision 4.

- [ ] Decide whether a check compares the worked example's two
      copies (2026-10-15, the commit plan for writing rules).
      Context: one-home's rule 5 asks a check where two copies
      cannot be avoided (ADR-0053). The worked example sits in
      `cbc-framing` and `cbc-slice` and must stay identical; it is
      compared by hand at each edit, and was identical on
      2026-10-15.
      Ideas: a diff of the two in `exchange-deliver`'s gates, since
             a delivery is when the copies leave.
      Trigger: the two found different, or the worked example's
               next edit.

- [ ] Decide whether `infra-establish`'s contract carries a paragraph
      on the store's facility (2026-09-17, never-oversold).
      Context: run 3 wrote one at Step 3 — the ways its store makes
      two writers disagree — because the skill is silent on it. We
      held it rather than declined: one instance is not a shape.
      Run 3 says SL-2 did not lean on it; SL-2 faces no race.
      Run 4 rebuilt run 3's problem from run 3's copies, so it
      cannot be the second run.
      Trigger: run 5 reaching the same gap unprompted.
      See: devlog 2026-09-17, later still.

- [ ] Move the skills' `foundation` to concept v2 at the release
      (2026-10-08, ADR-0048).
      Context: the method's skills say `foundation: concept v1`.
      ADR-0048 makes the next release v2, and `cbc-slice` and
      `cbc-framing` already state its ranking.
      Trigger: the release that names v2.

- [ ] Decide whether a rule can be delivered on trial, as a shape
      can (2026-10-08, never-oversold).
      Context: a shape reaches a run but binds nothing until a
      gate reads it (ADR-0052); a rule learned in one run is in
      force in the next from its first step. Run 3 asked after
      offering its evidence-test shape as a rule. Held: the question
      is real only once there is a rule we would deliver that way.
      Run 3's RETRO D4 says a trial names the close that judges it,
      and the step form says so since `0cdc50c`.
      Trigger: a rule we would ship that one run alone has lived.
      See: devlog 2026-10-08.

- [ ] Give the method a glossary (2026-10-08, never-oversold).
      Context: its words are defined where each is first used;
      tripwire, witness, fold, fence and possession appear only in
      the skills, never in the chapters a reader starts from, and
      the wall's own check joins them. Whether a list beside the
      chapters, or a chapter's, is open. Since `fbd1c5e` each run
      starts its own glossary at framing; the method has none.
      Trigger: Release's README item, where a stranger first needs
      the words.

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
      sides drift further from the pin while it waits. Run 3's RETRO
      D24 names one moment: after a run's apply step, so its
      decisions arrive tried. Run 3's next step waited on our note:
      recording the read-through was on its path (2026-10-18).
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
      validated entry path" and "code review". It met it again in
      SL-2 and SL-4, and run 4 rebuilt the same problem from run 3's
      copies, so neither is a second run. The hierarchy lives in
      `concept/02` and both cbc-slice files: a concept change, with
      an ADR and the version question (ADR-0003).
      Trigger: run 5 meeting an absence guarantee.
      See: devlog 2026-09-15; and 2026-10-10.

- [ ] Decide whether the worked example shows a slice that
      inherits its wall (2026-10-10, the reading of run 3).
      Context: run 3's SL-4 built no wall — SL-3's one statement
      already held its invariant — and owed proof only, against its
      own instance killed mid-write and an outcome its caller cannot
      know. The worked example has no such slice and no such
      adversity. One run's slice, so held.
      Trigger: a second run whose slice inherits its wall.
      See: devlog 2026-10-10.

- [ ] Decide whether `cbc-slice` says a red removes the backstop too
      (2026-10-10, the reading of run 3).
      Context: the skill says a wall that already stands is removed on
      the working tree for its red. SL-4's red as signed stayed green:
      the store's check on the units held caught both orders, and the
      evidence went red only with the one transaction and that check
      both gone. Run 3 revised its plan for it and proposed no edit.
      Since `2674c03` the skill asks the red run to note whether each
      backstop was seen or is unproven; removing it is not asked.
      Trigger: a second slice whose red a backstop holds green.
      See: devlog 2026-10-10.

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
