# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step or weekly. Prune "Later" ruthlessly:
     deleting an idea you'd re-derive anyway costs nothing.
     Rule: inline TODO:/FIXME: comments in code must reference an item here. -->

## Now (current plan step)

- [ ] Pure-seed experiment (2026-09-05, user's design) — separate
      from the trial: NOT walk 2, the assembly birth keeps the
      held briefing and the trial-close ADR still gates on it.
      Shape: the seed delivers material only, committed on main
      (hygiene; kit remainder raw — none of pure.md's fills, the
      TEMPLATE marker left in; concept/; the five skills; the
      playbook — pins in the commit subjects; NO scenario,
      template, fills, or birth entries: nothing that encodes a
      prior run's conclusions). Then one agent session with a
      two-line prompt: finish the birth, Step 0's gates are the
      exit; the problem arrives later as a briefing. No order
      hints — the order chosen is data.
      (2026-09-05, revised three times before firing: the kit
      half runs pure.md by pointer, fills included; the playbook
      is not delivered as a file — the seed inserts its steps
      into PLAN and fills "Steps from:", so the find-the-mapping
      and strip-the-marker observations are deliberately given
      away; and the insert omits the playbook's (CbC) Step 0
      comment — caught at the user's question: it encodes the
      assembly conclusions the experiment withholds and would
      have contaminated the derivation and commit-structure
      measurements. Fourth: that omission is an artifact, not a
      script filter — cbc-run-pure-playbook.md, the CANDIDATE
      SUCCESSOR (user's framing): if the experiment's reading
      goes well the parent is deleted and the variant stays,
      with the assembly artifacts falling at trial close;
      otherwise the variant dies. Until the reading, the parent
      is procedure of record and harvest lands there first.
      Fifth, user's design — the CHANNEL SPLIT: session-scoped
      text belongs to the firing prompt, PLAN to the project.
      The prompt now carries the situation (two sources, why
      split), the task, read-everything, and the expectation of
      a change-plan; the variant's Step 0 is pure container prep
      (agent-side gates out; the briefing moves to Framing as
      its starting input, so Step 0 closes clean — the walk-1
      blocked-gate known-issue dissolves). This deliberately
      re-opens assembly's "no change-plan": in the pure design
      the split is not fixed by us, so the convention fires on
      its own trigger. The measured object is now ASSEMBLY
      JUDGMENT — the sequence chosen and justified (entrance doc
      first? records when, adapted how far? skills whole or
      split by source?) — not discovery from nothing.)
      What it measures: a second independent derivation of the
      arrangement (the convergence point ADR-0014 gave up),
      compared against the first walk's (archived newborn
      8f167c4, held blind at docs/baselines/) and the shipped
      template; whether the agent reconstructs the bundle's
      birth entry from the seed subjects and holds the commit
      split. It
      also live-tests variant B's delivery shape (seed commits
      on main — the delivered/authored split is exact in the
      log).
      Reading is this repo's act, read-only, recorded here.
      2026-09-05: cbc-newborn moved to archive/cbc-newborn-v1
      (user's act, both branches intact) — the walk-1 comparison
      source for this experiment and for the trial.

- [ ] Template three-way reading, after the next full run
      (2026-09-06, user's design): the shipped CLAUDE.md template
      was re-cut fresh at 8e25977 — the walk-1-era method half
      (the five stance bullets, walk-1's derivation; the
      pre-framing guard, the withdrawn snippet's line; both the
      ADR-0014 merge, earned under different skills than today's)
      stripped and frozen whole at
      docs/baselines/claude-md-template-v1.md. After the next
      full run (through framing and build, current skills), read
      three ways: the run's derived CLAUDE.md vs the frozen
      template-v1 vs cbc-derived-claude-walk1.md. Harvest
      re-enters the template only from that reading, each line
      traceable to the run that earned it. The pre-framing guard
      was stripped with the bullets, then restored same day
      (user's call): it is garden-authored — the withdrawn
      snippet's line, no run's text — and the pure seed ships no
      template, so the does-it-invent-protections measurement
      lives in the pure runs untouched while the assembly path
      keeps its brake. ADR-0014's decision (shipped text, never
      per-birth derivation) stands; its merged content is
      archived pending re-harvest.

- [x] DONE 2026-09-05, change-plan opened ff518f7 (its close
      commit ends the set) — all six steps: sed fix, ADR-0015,
      re-vendor @ c670fe5, claude-md-template.md composed (the
      fragments file retired), scenario/README whole-copy, this
      records commit. Two decisions rode in the plan: the newborn
      holds no playbook copy (Steps-from line instead), and the
      temp/ staging file is deleted. What remains is the next
      birth (the re-birth item below).
      Reshape the CLAUDE.md delivery: template-whole, no sockets
      (user's design, 2026-09-04, decided while drafting the
      fourth handoff). The bundle ships a complete CLAUDE.md
      template — composed once here from the kit-stub content
      that is true for every project (records table, conventions
      list) plus claude-md-cbc.md's fragments, variables like the
      other fills — copied whole at birth; no merge into the
      kit's stub, no slot anchors assumed. ADR-0014's decision
      (shipped text, merged once, no derivation) stands; only
      the delivery mechanism changes — record that as a short
      amendment or follow-up ADR. Also revert what step 3 of the
      absorb set claimed: the starter README contract paragraph
      goes back to two assumed surfaces (playbooks/, STEPS
      region), the copy-table rows for claude-md-cbc.md update,
      and assembly step 3 in the scenario rewords (copy, not
      merge). Cost accepted: the template carries kit content, so
      it updates at re-pin like every pinned copy — the
      architecture's normal staleness, traded for zero live
      dependence on their stub's shape.
      (2026-09-05) The reply reshapes this item — absorb, don't
      run ahead of it. The handbook answered with 41 commits
      (HEAD c670fe5, ADR-0031..0034): the kit's CLAUDE.md is now
      ~41 lines — orientation, records table (change-plans row
      added), one guard comment; the empty sections are gone
      (0032) and the Conventions list is gone (0034, "the
      registry is the list") — so the kit content the template
      tracks shrank and our Method-row fragment is dead (the
      birth entry already names the convention). New stub rule:
      no handbook ADR citations in shipped stub text. Playbooks
      left the kit for starter/playbooks/ (0031) — we owe the
      path sweep their ADR names, and the assumed surfaces are
      now the STEPS region + step/gate idiom + default.md as
      vendor base (playbooks/ is no kit directory). default.md
      v2 adds the Framing projection gate item — take it at the
      re-vendor. Retro-fold settled in our direction: lessons
      fold into the playbook where it lives, the master. Their
      model also says a newborn holds NO playbook copy — steps
      in PLAN plus a "Steps from" line — which puts our
      docs/playbooks/ copy in question: decide inside the
      reshape's change-plan. agent-arrangement (0033) is the new
      home for entry-file rules; the template's provenance cites
      it at re-pin. Still ours from the earlier reply: our
      installs/cbc.md sed deletes the markers, and its "no
      marker left" line — both flip to markers-stay. Both repos'
      reply list asks temp/ deleted; delivery is done.
- [x] DONE 2026-09-04, change-plan 1cc3707..2a2e38b — all but the
      trial-close leftovers it names. Absorb the assembly rewrite
      (2026-09-04, from the newborn's
      post-walk sessions, cbc-newborn 3b27b46 + its devlog): carry
      the revised scenario into starter/bundle/birth-scenario.md
      (the trial protocol's own post-walk revision step — the
      newborn's copy is the draft, re-headered for the master);
      run the one-time CLAUDE.md comparison — the walk's derived
      section vs docs/baselines/cbc-startup-snippet.md — merge,
      and freeze the result into the bundle as shipped text, with
      the ADR that closes ADR-0012; add the birth fills as bundle
      files (newborn drafts: e7a13f9 for the stubs, CLAUDE.md as
      of aa1e17e). While in the bundle, fix the pin findings:
      cbc-run.md's Step 0 comment still says concept/ (bundle now
      lands under docs/); the concept chapters' headers call each
      copy authoritative — false in a newborn, needs a variant.
      Stays at trial close: install-manual rewrite, the rebuild
      script, whether the scenario file still ships.
- [ ] Re-birth under the scenario — unblocked 2026-09-03 (the
      moment-of-need set closed; the third reply absorbed
      same-day, so the seed reads the kit @ f9371e4 and the
      newborn holds six conventions — the birth entry names six):
      safe-reservations (born
      2026-08-30, zero project commits) stopped and discarded
      2026-08-31 — the birth design changed under it
      (starter/bundle/birth-scenario.md trial); deleting the born repo
      is the user's act, outside this repo. Surviving, held for
      the re-birth: the briefing (deliberately baseline-blind) —
      the re-birth takes it unchanged, so the scenario's first
      walk is a fair test — and the standing protocol below.
      Standing protocol, owned here, not by the run: the run is a
      blind replication of safe-reservations-v1 (archived) — its
      briefing omits the baseline deliberately so the derivation
      cannot steer by it. This repo opens both repos at phase
      closes (framing, ground, bootstrap, each slice stage),
      records the deltas here, and judges run 1's held insights at
      those readings (their named promotion path). The baseline at
      ~/IdeaProjects/safe-reservations-v1 stays read-only.
      Decided 2026-09-03: born under a placeholder name,
      cbc-newborn — everything pre-briefing is problem-agnostic,
      so the name would claim an identity that does not exist yet,
      and a domain-naming name would leak the problem into the
      Derive step; the briefing brings the name and the rename
      sweep (kit-sanctioned: "names given here may change at
      Framing"). The old ~/IdeaProjects/safe-reservations must be
      gone by the rename moment, not by birth. Placeholder-birth
      is itself a scenario finding — note it at the first walk,
      adopt at the trial-close ADR.
      (2026-09-03) Seed done: cbc-newborn born at 048c15c, one
      hygiene commit plus the deliberately dirty tree, all copies
      verified byte-identical, both birth entries in. The old
      safe-reservations is already deleted — rename precondition
      met. Remains: the walk (a fresh session in the newborn —
      never this repo's), then the briefing.
      (2026-09-04) cbc-newborn STOPS before the briefing — user's
      decision. No further work there; the user archives it later
      for comparison. Its yield is already absorbed: the assembly
      scenario, the shipped text, the fills, ADR-0014. The
      briefing survives unchanged, still baseline-blind, held for
      the NEXT birth — which runs assembly from the current
      masters (receipt branch of six) and is the trial's walk 2.
      The trial-close ADR re-gates on that birth reaching its
      briefing, not on cbc-newborn.
      (2026-09-05) The next birth waits for the reshape set to
      close and pins the kit at the handbook's c670fe5 (their
      full stub pass: slim entry file, README test, Framing
      projection gate, birth block fills all three dates).
- [ ] Watch at the next birth's phase closes (ADR-0013's scope
      boundary; retargeted 2026-09-04, cbc-newborn stopped
      pre-briefing): does the newborn update its own CLAUDE.md at
      the two parallel mid-run moments — the stack fact at
      bootstrap, the ground-must-be-up local rule at establish?
      Its stub teaches both fills; no skill prompts them. The
      ADR-0012 experiment is closed (ADR-0014, text ships), but
      this question survives it: shipped text still leaves mid-run
      fills to the newborn. A costly miss is evidence for a
      harvested skill line.

## Next (upcoming steps — assign each to a step when triaged)

- [ ] Header audiences (2026-09-05, user's question at the
      pure-seed run): a bundle artifact's header has two
      audiences — the garden's mechanics (tiers, harvest, the
      three homes, master-side use notes) and the copy's reader,
      who needs only neutral vendor language: source + version +
      pin, do not edit this copy, changes arrive by re-copy,
      record your surprises in this repo's own records (the run
      never needs the word "harvest" — its half of the contract
      is writing surprises down). Only claude-md-template.md
      separates the two today (header above the copy line); the
      concept chapters mix them — location-neutral by design
      (b90e7d7) but speaking ecosystem vocabulary into a repo
      that may go public or detach its agent side — and the
      playbook's use-comment travelled into the pure-seed copy
      claiming "the newborn holds no copy of this file", with
      bare ADR citations riding along (the citation trap, in a
      header). Skills are fine as-is: agent-side, not public
      docs — user's call. Fix pattern exists: master header
      above a marker, the copy is everything below, checkable as
      identical-below-the-marker. Not urgent — decide the split
      deliberately at the trial-close delivery rework; the
      seeded run-1 copy stays as delivered (its reaction is
      data). Related: observation (c) record-audience
      boundaries; fifth-handoff item below (their stubs face the
      same question).
- [ ] Fifth handoff material, accruing (no trigger set): the
      ADR-citation trap in text that lands inside a newborn —
      playbook steps copied into PLAN carry bare citations that
      read as the newborn's OWN ADR numbers there. Their stub
      rule (no handbook citations, "am" entry) covers stubs, yet
      their default.md v2 Step 0 comment ships "(ADR-0031)" into
      every born PLAN — their line to draw, FYI-shaped. Our side
      fixed 2026-09-05: the (CbC) Step 0 comment's citation
      dropped; audit any future shipped text the same way.
      (2026-09-06, pure-seed run 1) The three-voices problem,
      lived: an agent weighs its harness wiring (finish the
      task) over the firing prompt over repo files — and skills
      are files, the weakest voice. change-plans fired on its
      trigger (plan written, lifecycle held, scopes split), but
      §6's stop-at-every-boundary never did: nothing established
      that a reviewer was present, and a file-level "stop" loses
      to harness-level "finish." Not silent, though — the sharper
      fact: the agent SAW §6, recorded the deviation in its
      plan's decisions, and justified it by an instruction the
      prompt never gave ("this run was instructed to finish
      unattended") — the harness voice heard as the user's.
      Their own Delivery section
      predicted the class ("a convention firing on judgment
      misses exactly when the judgment fails; nothing catches
      the miss") — yet their ambient line covers only the
      plan-writing trigger, not the stop. To hand over: maybe
      define the hierarchy itself in the conventions model, so
      a rule's home channel becomes a delivery decision — forms
      and formats (commit style, lifecycle, artifact shape)
      travel fine as files, but brakes (stop, wait, ask) need a
      stronger voice; a rule resting on a session fact (a
      reviewer is present) cannot live in a file alone — the
      file can at most say "when a reviewer is present," and
      the session must say one is; and for rules that must hold
      even when the agent's judgment fails, mechanical
      enforcement (a hook or permission gate on git commit) is
      a delivery mode to consider beside pushed/ambient. Our
      side fixed 2026-09-06: the pure-seed prompt now
      establishes the reviewer and the staged-step approval
      pace (plan approved before committed, each step staged,
      shown, committed on the reviewer's word).

- [ ] After the absorb change-plan closes, two user observations
      (2026-09-04), raised mid-set and parked deliberately:
      (a) the pure kit's CLAUDE.md stub carries too much — the
      pure/handbook starter split exists, but part of what the
      pure stub ships should migrate to the handbook's own stub,
      leaving pure emptier (handbook-side change: shape it as
      evidence for the fourth handoff, with what our births
      actually used vs overwrote as the data);
      (b) RESOLVED for this repo (2026-09-04): the handbook's
      model set is exactly agent.md + tiers.md and our pinned
      copies are byte-identical with their HEAD (f9371e4) —
      nothing missing, nothing stale. The kit-side question (the
      kit ships no models) was dropped from the handoff by the
      user — closed, not asked;
      (c) record-audience boundaries — what may go in a README vs
      CLAUDE.md vs the internal records. The rule exists (the
      records table: README is the front door, for the outside)
      but slipped twice in one session, both times the same way:
      lived newborn text adopted on provenance authority without
      auditing it against the target record's own rule (the fat
      CLAUDE.md merge, the birth-narrating README fill). Consider
      whether the rule needs a sharper guard, and name the
      discipline: lived is evidence, not master text.

- [ ] Variant B at the birth after this one (user's design,
      2026-09-03): seed delivers AND commits — stub + bundle land
      on main as delivery commits (the birth-seed receipt becoming
      main) — and the newborn continues on top, its commits pure
      fills/edits/derivations. Compare against this run's variant A
      (seed uncommitted, walk commits the introduction) before the
      procedure is fixed: A shows comprehension order in the log,
      B gives a razor authorship split and a trivially scriptable
      seed. Known risk to watch in B: nothing forces the reading —
      the scenario or prompt must still mandate it, and the first
      derivation commit is the only evidence it took. So the
      trial-close ADR after THIS walk adopts provisionally at
      most; the A-vs-B judgment closes after both are lived.
      (2026-09-04) Overtaken by the assembly rewrite (cbc-newborn
      3b27b46): assembly keeps A's clean main — the seed commits
      nothing on the newborn's line — but prescribes the three
      commits and allows a script to make them. A-vs-B dissolves
      into "session or script," decided with the rebuild script
      at trial close. Kept for the risk note: nothing forces the
      reading — still true of assembly, still to watch.

- [x] Fourth handbook handoff — DELIVERED 2026-09-04 (user
      pasted temp/ staging copy), ANSWERED 2026-09-05 at their
      c670fe5. Disposition: the ask was taken further than asked
      — playbooks and "or delete" marks left the kit (ADR-0031),
      then the empty sections (0032, "guard without sections"),
      then the Conventions list itself (0034); the three pure.md
      defects were fixed same-day (39ddf48) plus one they found
      under ours (their own copy command also deleted the STEPS
      markers); retro-fold settled our way — into the master;
      item 4a dissolved with the list. What lands on us rides in
      the Now item above. Accrued data below kept as the record
      of what was sent: the §8 field data from both lived runs
      this absorption performed. Injection round two: the
      placeholder-line anchor can be legally deleted, so "row at
      the placeholder line" needs a fallback, and §8's end-of-list
      answer disagrees with where the kit stub itself seats this
      convention's row (before Hygiene) — born and injected repos
      disagree on row order. Installed path, first run ever (the
      data their reply asked back): the compare wants a
      per-convention manifest of which record stubs a convention
      ships through; a healthy reply loop makes the update mostly
      verification — the pin is the product, worth §8 saying; and
      the trap their missed-check implies, stated: reply
      absorption without a registry entry leaves the pin lying.
      Full detail in the two registry entries (2026-09-03).
      From the seed (2026-09-03), three pure.md findings: the copy
      block assumes the target dir exists (no mkdir step); "seven
      of the kit's seventeen files" is stale (18 now); the install
      block fills the hash but not the birth entry's date
      placeholder.
      From the newborn's post-walk sessions (2026-09-04, its
      devlog): the kit's PLAN Step 0 comment disagrees with the
      assembly shape on three points — "take the briefing",
      "draft CHANGE-PLAN.md", "plan open first"; and the kit PLAN
      stub says fold retro lessons into the local playbook while
      cbc-run.md's header says into the master — kit and bundle
      disagree (the second half is ours to fix, the stub's half
      is theirs to know).
      (2026-09-04, ADR-0014) The CLAUDE.md stub's slots re-enter
      our assumed-surface list — the bundle again merges into the
      stub at birth. Their contract rule says a new surface widens
      handbook-side first; we owe them the widening request.
      OVERTAKEN same day, user's design: no sockets at all — the
      bundle ships a complete CLAUDE.md template instead of
      merging fragments into their stub, so CLAUDE.md never
      re-enters the contract and no widening is asked (the
      handoff says so). The reshape is the Now item below.
      (2026-09-04) The kit ships no models (starter/kit/docs/
      holds only adr/). DROPPED from the handoff, user's call
      same day: not asked, not ours to raise. Kept here only as
      the fact.
      (2026-09-04) Evidence for the user's pure-stub argument
      (the stub carries too much; the pure/handbook split should
      go further): assembly overrode the kit's Step 0 comment on
      all three points; the first method birth deleted both kit
      playbooks post-walk; the stub's teaching comments are
      standing rules every born repo carries forever, by the
      kit's own gate — while the size-budget comment argues
      against exactly that. The stub's filled content is thin;
      the weight is the teaching text.
- [x] Playbook overlap, fires at the next birth (return handoff
      item 6): the kit ships playbooks/backend-service.md, the
      bundle overlays cbc-run.md beside it — the born project holds
      two playbooks and its Framing must know whether to copy from
      one, both, or merge. (2026-09-01) The starter
      redesign likely dissolves this: playbooks now hold full
      sequences, one chosen and copied whole at birth — a CbC
      birth chooses cbc-run.md and the others stay uncopied.
      (2026-09-02) Asserted on our side: ADR-0011 and the install
      manual's step 3 state the choice explicitly. (2026-09-03)
      Their side closed it as overtaken — the two coexist in
      playbooks/ without competing. All that remains is the
      birth's confirmation.
      (2026-09-04) Confirmed and closed: walk 1 landed both kit
      playbooks beside cbc-run.md without competition — then the
      user deleted the kit's two post-walk (that datum feeds the
      pure-stub handoff argument), and assembly now copies the
      chosen playbook alone.

## Later / someday

- [ ] Prebuilt CbC stub — a cache of the birth scenario's output,
      versioned, so a birth becomes one copy plus a briefing with
      a single composite pin. Parked with its trigger: when births
      come faster than harvests. Until then the cache would be
      stale more often than used, and the scenario walks fresh
      from the masters (2026-08-31 discussion; the ADR-0009
      objection weakens when the stub is derived by a written
      scenario, but the staleness cost stands).
      (2026-09-02) Rebuild-script variant, user's proposal: not a
      stored cache but a script replaying the seed fresh from the
      two pins at each birth — no staleness at all, so that
      objection dies for the seed half. What it cannot settle:
      whether the walk's commits belong to a script or to the
      newborn (the derivation experiment, ADR-0012). The trial's
      closing ADR decides how much becomes script — the scenario's
      trial protocol carries the question.
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
- [ ] The define phase's skill-level half is still open: the
      cbc-run playbook now carries Define as a step (2026-08-30,
      ADR-0009 change set), but no skill walks it the way
      cbc-framing walks framing — naming rule, verdict protocol.
      Consider a small addition when cbc-bootstrap next gets
      touched, or when a run's Define step chafes without one.
- [ ] Handbook suggestion, parked with its trigger: an overlay
      marker in the kit PLAN stub's Framing step (the hygiene
      files' append-below-the-marker pattern), so a method bundle
      can add gate items first-class. Propose it if a CbC run's
      Framing ever needs a gate the generic step cannot express,
      or when a second method bundle appears. Until then the
      generic gates are the interface and cbc-framing meets them
      (bundle doc, Birth section).
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

- [ ] Watch the first Step 0 walk for stub-vs-manual overlap
      friction: the kit's PLAN Step 0 comment and the handbook's
      install manual (was starter/README steps 3–7, now
      installs/pure.md) partially restate each other. The user's instinct
      is to slim the stub comment and carry the logic in the first
      prompt; counter-argument on record (2026-08-31 session): the
      prompt doesn't persist across sessions and the manual isn't
      copied — if anything shrinks, it's the manual deferring to
      the stub (stub-teaches-itself, their ADR-0004). If the walk
      shows lived friction either way, it becomes a handoff item
      with evidence.
- [ ] Birth-walker skill for this repo's arrangement: a thin skill
      in .claude/skills/ that reads the two birth manuals at use
      time (starter/installs/cbc.md, which defers to the handbook's
      installs/pure.md) and walks them with review
      stops — never restating the steps (the handbook's ADR-0014
      pointer idiom; a skill body that copies the manual is a
      second master). Trigger: distill it from the first lived
      birth, not before — the manual is unwalked (2026-08-30), and
      the skill should carry what the walk teaches, not
      speculation. Whether the handbook wants its own walker over
      its manual is its call — FYI delivered 2026-08-30; the return
      handoff (item 7) adds: the handbook has its own parked walker
      candidate, and if both ever exist they walk composing manuals
      (kit first, bundle second), so shape them together, not
      derived twice — dual-noted on their birth-skill entry.
      (2026-08-31) starter/bundle/birth-scenario.md is now this skill's
      precursor: the skill distills from the scenario once walks
      stabilize the draft, not from the manuals directly.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)
