# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step. Prune "Later" ruthlessly: deleting an
     idea you'd re-derive anyway costs nothing.
     Rule: an inline TODO:/FIXME: anywhere in the work must reference an
     item here. -->

## Now (current plan step)

- [x] DONE 2026-09-15, change-plan 0205a7d..close — seven fixes,
      one revision at the boundary (124744c): (1) R5 in the first
      slice's build, the Stage 3 gate reworded at the boundary
      from a process to the outcome — each test seen red with its
      wall absent, three ways named (9886800); (2) the whats the
      framing does not carry and the surface at its minimum
      (7dfd90d); (3) the owner candidates in front of the signer
      (ec51460); (5) every flag answered by name, the template's
      clause (70900fc); (6) the close more than a status (304119b);
      (4) bodies by path, variation point 9 (df75f6c); (7) the
      Spring slice reference — NOT in the bundle: the user's design
      at commit 9's boundary holds it at docs/baselines/, handed to
      a run after its build is on record, ADR-0021 revised then
      accepted (8017028, 8383932); the skill carries no pointer.
      Original item: Harvest run 3's SL-1 into cbc-slice
      (2026-09-14, read from its TODO's ten hand-offs, its slice
      record, devlog and delivered files; seven confirmed at the
      master; one change-plan, harvest lines per CBC ADR-0007,
      pinned copies untouched until a re-pin). The seven: (1) R5 at the first
      slice — system-readiness.md's R5 presumes a wall to break;
      SKILL.md's Stage 0 says the first slice answers it in the
      build: the naive version committed first, the wall its own
      diff, the evidence run red on the working tree before the
      wall's commit, recorded from actual output; "red before
      green" the build stage's own gate. (2) The birth whats —
      Stage 1 names what the first slice births that the framing
      cannot carry (the schema, the first migration, the door and
      its conventions, how the aggregate comes to exist), and
      Stage 2 owns "the surface at its minimum". The worked
      example stays duplicate-delivery; a contention twin is not
      written ahead of a second lived contention slice. (3) Stage
      2 presents the owner candidates as a comparison the signer
      weighs — each face, how it holds the guarantee, its cost —
      with a recommendation, the way an ADR presents options.
      (4) The harness reference states the body-assertion
      convention as a variation point: by path for a shape, by
      type when a shared API contract exists, never by substring;
      its own contention probe's `.contains` line reworked or
      annotated. (5) Stage 1 exit item: every flag on the
      registry row is answered by name — staged as its own
      evidence, or removed by a definition with the removal
      shown. (6) Stage 4: the row flips to `in-progress` when the
      specification lands; the close names the provisionals and
      what the slice hands to later slices by name — the step that
      makes concept 04's "a built slice may teach that the next is
      wrong or split" true in the registry. (7) A
      `references/spring-slice-reference.md` on the bootstrap's
      model — imitated never pasted, each artifact stating the
      outcome it realizes with variation points — from what run 3
      lived: the naive-then-wall split and the red run, the
      witness over plain JDBC from outside every instance with the
      sampler, the one-statement admit with the row count as the
      decision, value types at the door, bodies by path, the
      absence rung as bytecode rules. An ADR first: cbc-slice
      gains a stack reference, the SKILL stays stack-free (CBC
      ADR-0008's model). Not taken: the absence rung in the
      enforcement hierarchy (a concept question — Later); the
      contract's "in its own specification" wording (run 3's own
      document, not the master's — the run's to fix). Told to the
      run at its Step 6 opening, the user's way: which of its ten
      items the master took, so its in-place edits (its
      2026-09-14 decision) need not repeat them.
- [x] DONE 2026-09-12, change-plan 7652e2c..close — nine fixes
      after the run's own re-read added one and retargeted one
      (df39fbe), in the run's wording, one harvest line per change
      per file (CBC ADR-0007), pins untouched: the Ryuk trap and
      template true for Testcontainers 2.x (7531281); Stage 2
      naming no directory (2a74d1c); the machinery proof across
      processes — Stage 1 reading the instance count, stage 5's
      condition and lived realization, variation point 8 in prose
      (d20d0a6); the missing secret — stage 3's trap and recall
      11, Stage 1's fail-fast exclusion, the README template's
      symptom line (3727c59); the Boot 4 Flyway split (c5ecf97);
      the refusal test in the miniature, as code, lived once
      (3d82e33); the application template reading POSTGRES_PORT
      (9bdd33a); the rename trap saying when it bites (57f2fd7);
      the entry-file fill stating no current state, with a
      standing comment — fix 8 retargeted from the skill's Stage 5
      to the fill on the run's answer (cde0e97). Run 3's copies
      stay at their pin; a re-pin is its act. Original item:
      Harvest run 3's Step 4 into cbc-bootstrap (2026-09-12,
      read from its TODO's two hand-offs, its devlog and its
      delivered files; every finding confirmed at the master; one
      change-plan, harvest lines per CBC ADR-0007, pinned copies
      untouched until a re-pin). Seven fixes: (1) the Ryuk trap is
      stale on Testcontainers 2.x — checked against the 2.0.5 jar:
      the properties file reads only ryuk.container.image |
      privileged | timeout, the disable switch is the environment
      variable TESTCONTAINERS_RYUK_DISABLED, and Ryuk reaped both
      throwaways within seconds under rootless podman 5.8.
      templates/testcontainers.properties loses the inert
      `ryuk.disabled` line; the walkthrough's stage 4 trap 2 and
      recall item 6 read "if Ryuk fails on your host, the
      variable in the environment", not a properties line. (2)
      SKILL.md Stage 2 names `internal/construction/…`, a
      directory neither lived run has — both put the document at
      docs/construction/ beside the builder's manuals; the stage
      says "at the path the project's records choose" and names
      no directory. (3) The reference's concurrency probe is
      single-process; run 3's definition named plural instances
      (F17, the intent's done-line), so the machinery proof had
      to cross the process boundary: the store lifted out of the
      database base into its own holder (container + migration),
      the base keeping only the datasource override; a process
      helper forking the build's own output — `target/classes`
      plus the runtime classpath the dependency plugin writes at
      process-test-classes — with the three environment facts a
      real instance gets and no test-scope code inside; the probe
      answering its pid beside the identity; the race asserting
      the pids served are exactly the instances started and
      reading the witness from the store while they run. The
      walkthrough's stage 5 gains the condition (when L1 says
      plural instances, the proof is across processes) and the
      pom convention the plugin's earning reason; the reference
      carries the shape as a variation point, its "two bases, not
      three" line qualified. (4) A missing secret does not stop
      the app: Boot's binding leaves an unresolvable placeholder
      as the literal, the app starts with it as the password, and
      only health (`db` DOWN) tells; the store logs the failed
      authentication. Stage 3's "Fact:" paragraph gains it, and
      templates/readme-run-test.md's Run section gains the
      symptom line run 3 wrote. Whether to refuse to start is a
      *what* — run 3 decided it at release; the trap says decide,
      never absorb. (5) The Boot 4 Flyway split: with only
      `flyway-core` (+ the postgresql module) on the test
      classpath, no Flyway auto-configuration runs in the app
      context — the harness's own call is the only migration path
      in tests; a bound fact for the reference's §1. (6)
      templates/application.yaml reads `${<PROJECT>_DB_PORT:5432}`
      while the .env template names POSTGRES_PORT; run 3 lived one
      key — the template reads POSTGRES_PORT (closes the checkout
      two-keys item in Later). (7) Initializr on Boot 4 already
      emits `webmvc` and the `-test` companions; stage 2's rename
      trap bites only when a pom is written or translated by hand
      — one clause. (8) The entry file's opening line: run 3 left
      "no code yet" standing after the bootstrap — the watch item
      under Later holds the evidence. Decided 2026-09-12, the
      user's call: the skill carries it, so the next run does it
      unprompted. Stage 5's exit-records paragraph names the
      entry file's orientation beside the README projection: a
      line that states the system's state is made true at this
      close, "no code yet" being false now. The kit owns the
      file's shape, not its opening line's truth, so this stays
      on our side; noted for the sixth handoff. Whether
      infra-establish's close wants the same clause is decided at
      the harvest boundary, not assumed.
- [-] SKIPPED for run 3, 2026-09-11 (see the note at the end;
      held for the next run). Original item:
      Hand-back to run 3 at the Step 2 opening (2026-09-10, the
      gates experiment's protocol): one line of session input,
      told after its Step 1 derivation is on record — confirm the
      middle steps against the framed problem, the plan read
      end-to-end once (frozen v2's Framing item the derived gate
      missed; the run's Step 3 and 4 TODO items show the reading
      happened without the gate). Nothing else from v2 goes
      back: the sweeper is moot under v4, the entry-file
      retirement was done unasked. The line, for the prompt after
      its cut-the-branch and derive-the-gate instructions (no ADR
      numbers, paths, or vocabulary of this repo — the temp/ rule):
      "One item for Step 2's gate, or its notes, as you judge: now
      that the problem is framed, confirm the middle steps of the
      plan against it — read the plan end to end once and say
      whether each step still stands as named, and where the
      framing changed a step's shape. A step that no longer fits
      is reworded there, not silently kept."
      (2026-09-11, read at the Step 2 and Step 3 boundaries: no
      trace in the run — neither derived gate carries a
      middle-steps item, no devlog line, no plan-wide reading
      recorded. Checked 2026-09-11 in the run's session
      transcripts, read-only: the wording appears in none of the
      nine; Step 2 opened on "So what next? is it step 2?" and
      nothing else. Never told. Decided the same day, the user's
      call: not told to run 3 at all — the moment was Step 2's,
      the run is two steps past it, and its Step 1 reading showed
      the re-read happening unasked (its Step 3 and 4 items filed
      from the framing), so a forced reading at Step 4 would
      measure little. The line waits for the next pure-seed run's
      Step 2 opening — the clean test of the told channel — or
      for playbook v6 to write the item back as a gate, whichever
      the readings earn first. Item closed here; the line itself
      stays above for that use.)
- [x] DONE 2026-09-11, change-plan c6dbd68..close — all six, in
      the run's wording, one harvest line per change per file
      (CBC ADR-0007), pins untouched: the records section states
      the log-less shape as the default for a repo with records
      and the layout both runs used, the log for a repo without
      records now under docs/ beside the manuals (user's
      correction at the boundary), infra-serve reading the ground's
      record wherever it lives (e1a7c06); Stage 0's check 2 and the
      walk's inputs name the return trip (8e92316); cbc-framing's
      census gains "The runtime ground" beside the trust list
      (a3c0792); the walkthrough's two traps (2118bb6); query 6
      and the probe-role refusal (b06fac5); the naming-case
      comments in both SQL templates (56beb8c). Run
      3's copies stay at their pin; a re-pin is its act. Original
      item:
      Harvest run 3's Step 3 into infra-establish and cbc-framing
      (2026-09-11, read from its TODO's two hand-offs and its
      devlog; every finding confirmed at the master; one
      change-plan, harvest lines per ADR-0007, pinned copies
      untouched until a re-pin). Six fixes: (1) records-and-
      outputs — in a repo with records the shape is no
      establishment log: decisions as ADRs, the walk as lived in
      the devlog, expected results in the verify suite and the
      operator manual; compose.yaml and the env files at the
      root, the runnable ground under infrastructure/, the
      manuals under docs/. Both lived runs used that layout
      (checkout-system docs/infra/, run 3 docs/infrastructure/)
      and the skill's default paths match neither; they differ
      only on the log — checkout-system kept it, run 3 withdrew
      it at the reviewer's question. The section's last line
      sends the mapping note to "the log's first entry", which
      the log-less shape lacks — say where it goes (run 3: the
      environment ADR). (2) Stage 0's check 2 says "if the
      definition has no environment facts, the framing isn't
      finished" and "any check fails → stop"; both runs that hit
      it took the return trip instead — a dated revision entry in
      the definition, the framing's own revision rule, one commit
      (checkout-system d25ff48, run 3 44f256d). Name that remedy
      for check 2; the stop stays for the other two. (3)
      cbc-framing — the census never asks for the runtime ground
      (L1 is "the world"; no reference names the machine, plural
      instances, the store as a service, the clock) while
      infra-establish's Stage 0 requires the definition to carry
      it: a mismatch between two skills of this bundle. The
      workflow's L1 (or the worked example) gains a runtime-ground
      block, asked at framing. (4) postgres-setup-walkthrough —
      two traps lived, neither in the reference: the image runs
      the bootstrap against a temporary server and restarts, so
      the health check can report healthy in that window and the
      first query fails with "the database system is shutting
      down" — pg_isready plus one real query is the honest up;
      and a host without a psql client reads the witness through
      a client container on the host network. (5) templates/
      verify-database-model.sql verifies C1, C2, C4, C5 and
      leaves C3, the CONNECT revoke, unchecked; run 3 added query
      6 (has_database_privilege for both roles and PUBLIC as
      0::oid) because C3 claims it — the template gains it. (6)
      the bootstrap and verify templates hardcode <project>_
      prefixed roles and a LIKE filter, while the role-split
      reference makes the prefix conditional on a shared cluster;
      run 3 took bare names on its dedicated cluster and rewrote
      the filter as an explicit IN list — a comment at the
      template's role names naming the case it ships.
- [x] DONE 2026-09-10, change-plan da5c95f..close — two of the
      three, plus one the run never filed: the registry template's
      opening line in project voice (2d57b01), its reconciliation
      line as a table under an L4-is-the-master sentence (bb51b61,
      the reviewer's own touch-ups in run 3, 79344c5 and 827d123),
      the export order said as the commits' with the file ending
      L1→L5 (dd481ea), the residue filter refusing agent language
      (the run's rule, now the skill's). The twin hand-off was
      already harvested 2026-09-07, both headers narrowed to the
      path line — the 5bdcf71 reading miscounted it as open; run
      3's copies are stale at their pin and its two TODO items are
      its own to close at a re-pin. Original item:
      Harvest run 3's three cbc-framing hand-offs into the bundle
      master (2026-09-10, read from its TODO, all three confirmed
      here): the registry template's opening line puts the
      skill's name, step number and delegation slot into a
      project artifact — the run's rule from it, exports carry no
      agent language, is the fix's shape; SKILL.md's export
      section says the definition grows "L2 → L1 → L4 → L3 → L5,
      one lived state per commit" and was read as append — say the
      commits carry the derivation and the file ends in the
      workflow's order L1→L5; the worked-example twins claim
      byte-identity and differ in line 3, the provenance path
      (diff confirms it in starter/bundle/ too — resolved
      2026-09-17: both headers are gone and the two files are
      byte-identical, checked by diff, and ARCHITECTURE carries
      the fact). One change-plan,
      pinned copies in the runs untouched until a re-pin.

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
      log). (2026-09-07, superseded by ADR-0018: from the next
      seed the deliveries commit on the receipt branch
      birth-seed and main holds them untracked — the agent's
      first commit on main is its own, so the sequence and split
      are measured for every delivered file, not only the
      agent's additions. Runs 1 and 2 were seeded on main; a
      reading against them says so.)
      Reading is this repo's act, read-only, recorded here.
      2026-09-05: cbc-newborn moved to archive/cbc-newborn-v1
      (user's act, both branches intact) — the walk-1 comparison
      source for this experiment and for the trial.
      (2026-09-06) ADR-0016 takes the verdict this item deferred
      to a trial close: the pure shape is adopted, the assembly
      walk cancelled, the parent playbook deleted — the variant
      is the only playbook. The held briefing is released to the
      pure path: it opens Framing in the pure-born run when the
      user fires it. The item's trial framing above is history.
      (2026-09-06, run 2's Step 0 read: the arrangement converged
      with run 1 on the pre-briefing line and the records table,
      came out thinner on the pin stance and README's method
      pointer, and presumed "backend" as run 1 and the parked
      CLAUDE template did — three of three. Decided the same day:
      keep it — the concept and kit never say backend, the
      skills' description lines do, and their bodies are
      backend-born, so the word names the toolkit, not the
      problem; the README template's "a system" reverted to
      match. Trigger to revisit: the first non-backend run (Later).
      Neither run derived the pre-framing guard.)

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
      (ended with run 2 — ADR-0019 delivers the guard from run 3
      on; two pure runs are its whole evidence: neither invented
      it)
      lives in the pure runs untouched while the assembly path
      keeps its brake. ADR-0014's decision (shipped text, never
      per-birth derivation) stands; its merged content is
      archived pending re-harvest.
      (2026-09-07, rule revised, user's call: a birth template is
      judged by what a run derived at birth, so it harvests at
      the Step 0 reading, not after a full run — the README
      template already did (166bc7e, run 2's opening line); the
      CLAUDE template was read the same way and kept as it stood.
      The three-way reading after the full run still owes the
      frozen-v1 comparison for the stance bullets, which no birth
      can judge.)

- [ ] Playbook gates experiment (2026-09-06, user's design; the
      template freeze's move, one level deeper): the pure
      variant re-cut provisional at v3 (55d3dbb) — middle steps
      keep name, skill pointer, and goal; their gates, records
      lines, and warnings stripped to a derive-at-opening
      instruction — and v2 frozen whole at
      docs/baselines/cbc-run-pure-playbook-v2.md. Three
      decisions, taken consciously: kit steps stay vendored
      whole (their gates are the kit's text, not our harvest);
      warnings stripped for purity even though they are
      underivable paid-for facts; the newborn learns nothing of
      the frozen master. Protocol, riding the reviewer-paced
      prompt: at each step opening the run's agent derives the
      gate and stops at the boundary; here, read-only, derived
      vs frozen v2 is compared, then any missing paid-for
      warning (Boot 4, the faithful-miniature container, one
      test command...) is handed over as session input, after
      the derivation is recorded, never as silent playbook
      text. What it measures: which gates are a cache of the
      skills (re-derived) and which are knowledge only the
      playbook holds (missed) — that answer is the playbook's
      own reason-to-exist, measured. The parent stays procedure
      of record, untouched (2026-09-06, overtaken the same day:
      ADR-0016 deleted the parent — the variant is the only
      playbook, and pure-seed.md the procedure of record). Run 2
      of the pure seed delivers the provisional playbook at a
      new pin and then measures arrangement and gates in one
      run. (2026-09-06, v4 — the user took the strip
      whole-playbook: Bootstrap and Framing lose their vendored
      kit gates and kit comments too, overturning decision one
      above for steps 0 and 1; only Release stays vendored, the
      fixed endpoint. Framing's sweeper item and the two
      projection items now sit only in frozen v2 — hand-back
      candidates at the Framing boundary if the derivation
      misses them. The reading gains a category: kit hygiene an
      agent re-derives unaided vs kit knowledge only the
      vendored text held.) (2026-09-06, seeded: run 2 is
      ~/IdeaProjects/cbc-pure-run-2 — five commits, kit @
      c670fe5, bundle @ 322dd43, v4 steps verified byte-true;
      run 1 at ~/IdeaProjects/cbc-pure-run stays frozen in
      place, the reading's evidence, its pins checkable at
      their recorded path. Fired the same day: Step 0 closed in
      nine commits, reviewer-paced; the Step 0 reading is in the
      devlog (2026-09-06, fifth arc) — the derived gate covers
      v2's three and adds five, each traced to a kit convention,
      so at Step 0 the vendored gates were a cache. Awaits the
      briefing; the Framing boundary is the next reading. Note
      for run 3 onward, 2026-09-07: seeded per ADR-0018 on the
      receipt branch and per ADR-0019 with the entry files
      delivered — its Step 0 differs from run 2's in that the
      agent commits the deliveries itself and meets an
      arrangement it did not write; the gates reading compares
      the derived gate, not the commit count. 2026-09-07, a
      trial rides Step 1 onward: a standing PLAN rule, delivered
      to run 3 as its own commit before the briefing — each step
      starts on its own branch cut from main and ends after its
      gate closes by fast-forward merge, on the reviewer's word;
      a restarted step keeps its old branch renamed. The Step 1
      reading checks four things: the branch cut before the
      step's first commit, the merge fast-forward with main
      linear, the gates reading before the merge, and no
      question the rule made the agent ask. Holds → playbook v6
      preamble; bends → the bend is the finding. Two more trials
      ride the same pre-briefing session (temp/prebriefing-run-3.md,
      rewritten 2026-09-09): an untracked CLAUDE.local.md holding
      the reviewer's pace, and the run's CLAUDE.md under .claude/,
      content untouched (2026-09-09: no longer waiting on a
      reading on our side — the seed's semi-pure step delivers the
      entry file at .claude/CLAUDE.md from the next birth, the
      user's call: a layout preference, mechanically identical
      either way; run 3's move stays the handbook's evidence for
      its own stub, their decision 5). Pre-briefing session read
      2026-09-09: the kit update, the move (pure rename, own
      entry), and the local file (yours, written 09-08, logged
      unquoted) all landed, seven commits on a branch of the
      reviewer's choosing, fast-forwarded; the settings file was
      rejected in the plan, not trialed — so the ask-rule reading
      is dead here and the pace reading changes shape: sentence
      plus local file, no gate. And a channel finding, the
      three-voices lesson once more: the agent read the handbook
      checkout (its devlog says so; its registry cites their
      ADR-0035 five times) — "stay inside this repository" sits in
      the briefing's session section, which had not fired, and the
      run's own §8 names a checkout on disk as the handbook, so the
      convention sent it there. Not this repo: no mention. A
      session rule absent from the session's prompt does not exist
      for that session; every prompt to a run carries it from now
      on. The commit ask rule — a tracked
      .claude/settings.json, the harness stopping every commit at a
      prompt — no longer rides as a trial of ours: the kit ships it
      as the born default since af16eb7, so it reaches run 3 with
      the kit update the same prompt opens with (delivered on a
      receipt branch cut from the seed commit, the first kit update
      anywhere to carry an entry-file comment change — the handbook
      wants to hear how the branch served the compare). The
      handbook withdrew the rule for itself after eleven commits:
      it asked for a word already given, twice on the path where
      the prompt is declined to read the diff first. The reading
      adds: whether the agent stages and shows before the prompt
      bites or walks into it; whether the local file's text stayed
      out of the records; whether the arrivals landed as decisions
      entries and one TODO item; for the move, that the harness
      read the file at the new address (the briefing session's
      first act shows) and the rename stayed pure. Run 3 is the app
      repo for the address question — this repo moved its own
      entry file under .claude/ on 09-07 and back on 09-09
      (8d08cfd), on the handbook's reading that the address means
      something: root for a repo about the arrangement, .claude/
      for one that builds an app. Evidence from the handbook's
      checkout-system reading (2026-09-09), for the retrospective:
      that run delegated every gate to the agent by one decisions
      entry and needed no gate, only the record — the ask rule is
      the reviewed mode's gate, and the other mode shows it needs
      none; and the eight playbook lessons the reading listed as
      the method's all sit in frozen v2 already, absent from the
      live fill by this experiment's design — nothing to add, the
      readings decide what re-enters. Holds → kit stub (the
      address; their decision 5 waits on this reading) or bundle,
      decided at the handbook.)
      (2026-09-10, the Step 1 reading — run 3 closed Framing on
      step-1-framing, 44 commits, fast-forwarded to main before
      this reading, the one bend and ours: the reading was to
      come first. Derived gate, twelve items, vs frozen v2's six:
      the problem statement, success criteria, out-of-scope and
      README projection all covered in the method's form — the
      exports, the intent's six bars, the definition layer by
      layer, the registry on template, the README re-derived per
      the skill's projection table — so those four were a cache
      of cbc-framing and the briefing. Two additions v2 never
      had: verdicts inline and no delegation entry; and Release's
      framing-time decisions written in the exports, derived by
      reading forward into the vendored Release step — a gate
      item earned from another step's text. Missed: the
      middle-steps confirmation against the framed problem (the
      run did file Step 3 and Step 4 TODO items from the framing,
      so the reading happened without the gate saying so) — the
      one hand-back, told at the Step 2 opening (Now item); and
      the projection sweeper, moot under v4 since later gates
      derive at opening — no hand-back. The entry-file
      retirement item was absent from the gate and done anyway:
      the agent widened its last step to the whole post-framing
      entry file when three lines had gone false — a paid-for
      warning re-derived at the moment, not at the gate. The
      four trials held: the branch cut from main before the
      step's first commit, fast-forward, main linear, no question
      the rule made the agent ask; the entry file read at
      .claude/ — the plan targets it by path and the guard it
      held governed the session; the pace, sentence plus local
      file, no gate, the file's text in no record; stay-inside —
      no handbook read this step, the one ADR-0035 mention a
      carry-over line in the run's TODO. Three findings on the
      branch rule for its fold-back: the branch gate item was
      ticked before it was true, since the merge is the
      reviewer's act after the close commit — the rule must say
      how that item closes; the rule is silent on the merged
      branch, which is why step-1-framing still exists (deletion
      is safe, main holds every commit — the user's act); and two
      change-plan revision subjects ran to 54 characters, the
      em-dash form. Held → playbook v6 preamble with those
      three lines.)
      (2026-09-11, the Step 2 and Step 3 readings — both steps
      closed and fast-forwarded before the reading, as at Step
      1. Step 2, derived eight vs frozen v2's three: all three
      covered sharper — the naming rule became a four-point bar
      the run wrote itself, the description derived from the
      intent's why, the rename traced into every record with a
      dated revision entry per export; five additions v2 never
      had — the remote as part of the identity (the run retitled
      the step "Identity (name, description, remote)" at
      opening), the CHANGELOG line, README true for a stranger
      from the remote, the devlog entry, the branch item. v2's
      one warning, scope in the description, re-derived unaided.
      A cache, whole; no hand-back. Step 3, derived eleven vs
      v2's four: all four covered in the skill's form (Stage 0,
      the step gates, the exit test); additions — Stage 0's pass
      recorded, the environment section contemporaneous with its
      facts named, standing knowledge as the rebuttable default,
      no ground file older than its decision, T2's tool named
      and its refusal seen (a project item from the definition's
      trust line, which no playbook could hold), the re-stand
      from the manual alone, README/ARCHITECTURE/records rows.
      v2's two warnings both re-derived: the runtime-ground
      return trip was lived exactly (Stage 0 tripped, L1 revised
      by a dated entry, one commit) — a cache of the skill's
      Stage 0 plus the definition's revision rule; grants as
      authority — a cache of the role-split reference. v2's
      records line, "an establishment log of actual outputs", is
      the one thing refused: opened at the decision, withdrawn a
      commit later at the reviewer's question, the walk in the
      devlog's tables instead — one lived run each way now, so
      the log is a run's shape, not the playbook's. No hand-back;
      the skill-side findings are the harvest item in Now. The
      trials held through both steps: branches cut at the
      previous close commit, tips on main, merged branches kept;
      twenty-six commits, none straddling; the entry file edited
      at .claude/ in two agent commits; the pace in no record;
      no handbook mention in any diff. Two more subjects over 50,
      the em-dash revision form (52, 55). The run answered the
      branch-item finding itself: "ticked on the reviewer's word
      to merge, given at this boundary" — that wording is the
      rule's. Held → playbook v6: Step 2 retitled Identity
      (name, description, remote), the run's own fold-back item;
      the branch item's closing wording. The retitle landed as v6
      the same day (3242c59); the branch item's
      wording stays held with Step 1's three branch-rule lines,
      for the version after run 3's trial verdict.)
      (2026-09-15, a second reading category, the user's design —
      ADR-0021: the build comparison. The Spring slice reference is
      held at docs/baselines/, blind to newborns; after a run's
      slice close is committed on its branch and before the
      fast-forward, the reviewer hands it over as session input and
      the run compares its build shape by shape, the verdicts in
      its devlog and decisions log; the reading here checks each
      verdict and lands the confirmed ones in the reference as
      harvest lines. Measures the reference as the gates reading
      measures the playbook: which shapes a run re-derives unaided,
      which weaker, which it beats. A second derivation before the
      merge is the reviewer's option — the first branch bundled out
      of the local repo, a fresh session on a new branch, both
      restored for the comparison, one merged with a commit naming
      the rival. First moment: run 3's SL-2 close. One line joins
      the held branch-rule lines for the playbook: at the close the
      agent says the step is closed on its branch and the
      fast-forward waits — what the reviewer holds against the step
      is compared then; it names no reference. For run 3, told at
      SL-2's opening or the run's own agent commit.)

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
- [x] CANCELLED 2026-09-06 by ADR-0016: the pure shape is
      adopted and the assembly walk will not happen. The
      briefing — still baseline-blind — is released to the pure
      path and opens Framing in the pure-born run; the
      blind-replication protocol below survives with it (this
      repo still opens run and baseline at phase closes and
      records the deltas here). The rest of this item is
      history.
      Re-birth under the scenario — unblocked 2026-09-03 (the
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
      (2026-09-12, run 3's Step 4 reading — the first answer:
      at bootstrap, no. The entry file's opening line still says
      "the ground stands, no code yet" after the skeleton, the
      harness and seven tests landed; Step 3 had rewritten that
      line, Step 4 edited the file only for the records-table row.
      No stack fact entered either — README carries the stack and
      the one test command, so the guard's third test may keep it
      out; the false line is the miss. At establish, no local rule
      entered; the miss cost nothing visible. The fix is run 3's
      own agent commit. Decided the same day, the user's call:
      cbc-bootstrap's Stage 5 names the entry file's opening line
      beside the README projection (CBC ADR-0013's shape) — fix 8
      of the Step 4 harvest in Now. The kit owns the file's shape;
      its opening line's truth is the run's, and the moment is the
      skill's. Evidence for the sixth handoff.
      Reversed later the same day on run 3's own fix, the user's
      call: the run dropped the state clause outright — a line
      about current state has a moment and stales at every step;
      the entry file states only what never changes, current
      state is PLAN's by the records table. Stronger than making
      the line true at each close, so fix 8 landed in our fill
      (cde0e97): the clause gone, a standing comment beside the
      paragraph saying why. No skill names the entry file. The
      kit's stub carries the same clause, and agent-arrangement's
      test 2 has its instance — both the handbook's, in the sixth
      handoff. The bootstrap half of this watch is answered; the
      establish half stays open for the next run.)
      (2026-09-14, run 3's Step 5 reading: the bootstrap half held
      — the opening paragraph has stated no state since the 09-12
      cut, nothing to go stale through a fifth step; the establish
      half stays open.)

## Next (upcoming steps — assign each to a step when triaged)

- [x] DONE 2026-09-07, ADR-0019 (change-plan 2ca749b..close):
      the semi-pure delivery is pure-seed.md's optional step 4 —
      both fills written over the kit's stubs, headless, one
      commit on birth-seed; run 3 runs with it on. The
      kill-or-justify test below was answered on the justify side
      by run 2's Step 0 reading: the guard and the skills' pin
      stance were missed twice. The reading's object changes: what
      the agent edits in delivered entry files, and whether the
      guard holds through Framing. Original item:
      Semi-pure install scenario (2026-09-06, user's idea, shape
      undecided): a third birth shape between assembly (deleted,
      ADR-0016) and pure — the entry files ship filled
      (claude-md-template.md, readme-md-template.md, both parked
      under starter/fills/ since ADR-0017 — text written over the
      kit's stubs, not files copied) while the rest of the birth
      stays pure. Not
      designed yet; both templates wait for it. What run 2
      contributes before any design: its derived CLAUDE.md and
      README are comparison objects against the parked harvests
      — if derivation keeps producing what the templates hold,
      the shape may never be needed; if it keeps missing
      something, that gap is the install's justification.

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
- [x] DONE 2026-09-11 — replied 2026-09-10, absorbed at ab916a1
      (change-plan bd3b785..close). The answers: decision 5 closed
      on run 3's report — the kit's stub stays at the root, a
      bundle that wants .claude/ renames at birth, as the seed
      does; decision 1 withdrawn — the kit ships no settings file,
      the stop is the commit-messages sentence, and run 3's 44
      commits on sentence plus local file are the only lived
      evidence about the stop; the citation ask taken as a wider
      rule (HANDBOOK ADR-0037): a bare number is the reader's own,
      another repo's decision carries its tag, records that never
      leave stay bare — ours is CBC, the bundle swept, ADR-0020;
      exemplars by role; the born-without sentence in §8; no ADR
      cited below the first step of either playbook; tiers §3
      rewritten from our five, the told channel named as what the
      gates experiment uses, unpinned by design; the three-voices
      report became an agent-model correction (the window carries
      roles, W2) rather than a TODO; the two change-plans practices
      sit in their Step 10 for a read with more runs. Nothing asked
      of run 3. Original item:
      Fifth handoff — DRAFTED 2026-09-10 as
      temp/handbook-handoff-2026-09-10.md (two asks: the copy-
      surviving citation and exemplar forms with the born-without
      sentence for §8; the tiers model's §3 and DRAFT note; one
      report: run 3 through Step 1, decision 5's answer; FYIs:
      the change-plans lessons, the three voices). Delivered by
      the user into a handbook session; the draft is deleted when
      the reply is absorbed. Awaiting: decision 5 and a kit pin if
      the stub moves; the citation form; §3 at a pin. Material as
      it accrued:
      Fifth handoff material, accruing (no trigger set): the
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
      (2026-09-09, the af16eb7 update, §8 friction — three items,
      one pending.) (a) Text that does not survive the copy, two
      forms: every ADR number in the kit's skill copies and the
      models is the handbook's, bare, and the ones below 0020
      collide with this repo's own sequence on other subjects —
      their new stub rule (no handbook citations in a stub) stops
      one step short of the skill copies; a self-qualifying
      citation at the master ("handbook ADR-nnnn") survives
      verbatim copying and can never collide. And artifact-kinds'
      exemplars are written from the handbook's seat (conventions/
      paths, "this repo"); the playbook one was patched to name "a
      concept repo", which a born project has never heard of, and
      points nowhere for either reader — a born project holds no
      playbook copy, ours is a fill. Exemplars by role survive the
      copy ("the playbook your PLAN's Steps-from line names"). (b)
      The requires chain can name a convention a project was born
      without: convention-lifecycle @ af16eb7 requires
      agent-arrangement, and a repo born before it existed has no
      position for it — §8 step 2 reads as "check the copy", and
      there is none; we ran it as a first injection by the
      installed path. Worth one sentence in §8. (c) Run 3's kit
      update, c670fe5 → af16eb7, read 2026-09-09 from the run's
      records: the kit delivered on a receipt branch kit-af16eb7
      (one commit cut from the seed commit, the kit copied over
      it); the agent ran §8 under a change-plan, seven commits,
      project side first so the registry entry named an existing
      commit. What the branch gave the compare, the run's words:
      the whole kit diff at the two pins in one place, and
      compare-first became one git diff per file against the seed
      commit — every copy identical, every overwrite clean. Where
      it fell short: the four placeholder reversions are noise to
      read past; the receipt cannot say which convention a stub
      change belongs to (the starter README's table is not a kit
      file); the why is not in it (ADRs and convention text are
      not kit files) — and the agent went to the handbook checkout
      for both, its own §8 naming "a checkout on disk" as the
      handbook; the entry-file stub diff was carried into the
      living file by hand, comment only. Two things the reading
      adds for the kit's born default: the agent REJECTED the
      settings file, not deferred it, on the handbook's own
      withdrawal (their ADR-0035 read at the checkout) and the
      pace already held by the operator's file and the
      commit-messages sentence — the first born project to read
      the rule's why refused it before running under it once; and
      the hygiene comment's "(if any)" was kept as a recorded local
      edit for the same reason. Run 3 now trials the sentence plus
      the local file with no gate — the case their reply named as
      deciding whether the local copy is dead weight or a band-aid.
      (d) The tiers model, models/tiers.md @ 4fe8083, unchanged at
      af16eb7: its shape holds — three tiers, copies down, records
      up, one tier per repo, the garden paragraph exact — but §3
      was written from zero runs and five have lived it. Five
      refinements, each with evidence: delivery has two forms, the
      pinned copy and the fill the run owns from the seed commit
      on (our ADR-0017; steps in PLAN, the two entry files — folded
      back by name, never re-copied); up is a reading, not a
      sending — the tier above reads the run's records read-only,
      at step boundaries during the run, the run sends nothing,
      and the handbook's checkout review is the same flow one tier
      up, splitting the yield by ownership; one downward channel is
      deliberately not a copy — the gates experiment hands a
      missing warning to the run as session input after the
      derivation is recorded, told, unpinned, a designed exception
      "downward: only pinned copies" would call a violation; tiers
      talk in documents because no tier's agent reads another
      tier's repo (a run reads only its own; a concept repo opens
      a handbook checkout only for the lifecycle update), and the
      pin must follow the talk — our registry lay for two days
      after a reply was absorbed without an entry; vocabulary — the
      "startup snippet" withdrawn 09-02, "pinned at a concept
      version" is a concept-repo commit with each execution naming
      its concept version, and the DRAFT's revise trigger names the
      garden, which has not fired, where "no runs yet" is what
      changed. Ask: revise §3 and the DRAFT note; we re-vendor at
      the new pin.
      (e) Run 3's Step 1, read 2026-09-10: the three pre-briefing
      trials held through a full step — the entry file at .claude/
      read at its address (their decision 5's report: the move is
      a pure rename, the harness follows, nothing else changes);
      the pace as sentence plus local file with no gate, the
      file's text in no record; the branch per step, cut before
      the first commit and fast-forwarded on the word. Two lessons
      for change-plans from the run's own close: name a
      touch-ups-on-reading step from the start (three plan
      revisions each cost a commit before a provisional step named
      them), and a step run as a commit series — draft, one
      revision per reviewer question, verdict — so a question's
      effect is a diff; whether the series shape wants naming in
      change-plans is theirs to decide.

- [ ] Sixth handoff material, accruing (no trigger set):
      (a) run 3's Steps 2 and 3, read 2026-09-11 after the fifth
      draft went: the three trials held through two more steps
      (twenty-six commits, none straddling; the entry file edited
      at .claude/ twice; the pace in no record; no handbook read);
      a change-plan shape worth a line — an outward action, the
      remote created by hand, as a numbered step with no commit,
      so the close body says whether it happened; the em-dash
      revision subject over 50 twice more. (b) The tag rule lived
      on this side, 2026-09-11: 102 bundle citations swept by
      script in one commit, no header line per file (ADR-0020's
      reasoning); the fills' `<TAG>` left literal for the run to
      fill at its naming — whether the kit's stub should say when
      a born project fills it is theirs to read. (c) Run 3's Step 4,
      read 2026-09-12: the trials held a fourth step (fourteen
      commits, none straddling; the entry file at .claude/ once;
      the pace in no record; no handbook read); three subjects
      over 50 again; and the newborn did not update its entry
      file's opening line at bootstrap — the watch item under
      Later holds the evidence. Two fold-backs from it for the
      kit: the CLAUDE.md stub's orientation carries a state
      clause ("nothing to build, no tests, no runtime") that a
      born project rewrites at every step close until it misses
      one — the stub should state only what never changes, with
      current state PLAN's by the records table; and
      agent-arrangement's test 2 gains a lived instance, a line
      with a moment that went where the moment is. Our fill took
      the cut 2026-09-12 (cde0e97).
      (d) Run 3's Step 5, read 2026-09-14: the trials held a fifth
      step (eighteen commits, none straddling; the entry file at
      .claude/ once; the pace in no record; no handbook read, the
      handbook named once as a hand-off's destination); four
      subjects over 50; and run 3's kata hand-off — a personal
      cut-a-kata skill, practice exercises cut from live work,
      lived at SL-1 (three cards cut), graduating after katas in
      two projects — is the handbook's to read. Run 3's
      2026-09-14 decision to edit its skill copies in place under
      guards and hand diffs is the run's arrangement; whether the
      handbook's pinned-copy rule wants the variant is theirs.

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
      (2026-09-07) Closed by ADR-0018: the pure seed adopted B's
      committed manifest and A's clean main at once — the seed
      commits on birth-seed, never merged, main holds the files
      untracked and the agent commits them. The risk note holds
      its shape: the prompt names the branch, and the first
      commit on main is the evidence the reading took.

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

- [ ] Does the worked example anchor a run's framing? Raised
      2026-09-17 by the user, while the header notes were being
      cut: an invented example of a tiny order service, its slice
      an idempotency one, could steer a run toward that shape
      whatever its own problem is. No evidence yet — no record in
      three runs, and run 3 framed over-admission under contention,
      a different problem with a different invariant. One weak
      signal, unresolvable from here: the example and run 3 both
      land on one area, which either means anchoring or means
      small systems have one area. The skill already scopes the
      example to "unsure what a step's output looks like" and the
      example calls itself invented for teaching. Trigger: the next
      framing read on a differently shaped problem — if it still
      lands on one area and an idempotency-flavoured first slice,
      that is the signal. The answer then is a second example on a
      different shape, never deleting the one we have: it is the
      only place in the bundle that shows finished output rather
      than procedure, and Part 2 shows the seam between two skills
      that neither can show alone.

- [ ] Deduplicate the worked example. It is one document shipped
      twice, identical in both skills' references/, so either
      skill's directory stands alone. The cost is 202 duplicated
      lines; the cost of merging is a skill pointing into another
      skill's directory, so cbc-slice could not be installed
      without cbc-framing. Nothing has ever needed that. Since
      2026-09-17 the copies are byte-identical with no headers, so
      diff polices the duplication and nothing can rot silently.
      Trigger: a reason to install one skill without the other.

- [ ] Could a project need its own mould of a bundle skill?
      Raised 2026-09-17 by the user, and deliberately not built
      for. The answer today: a skill is the same for every
      project, and what one project alone needs goes into that
      project's own committed records — its entry file, a gate
      item, an ADR — never into the copy, and never into an
      operator's local file, which belongs to one person on one
      checkout. The gap that could force the question: a declined
      edit the project genuinely needs in the skill's behaviour,
      where a record states it but the agent reads the skill. Run
      3 named the fallback for exactly that and rejected building
      it — an overlay file per skill beside the pinned copy,
      holding project-specific behaviour, at the cost of a second
      file per skill and a prune at every re-pin. Trigger:
      declined-but-needed becoming a pattern rather than a
      possibility.

- [ ] The handbook's invitation, 2026-09-16, not owed and not a
      condition of anything: when we next author or restructure
      something of our own, notice what we had to invent because
      nothing told us — what an artifact must carry, how it is
      written, how explanation is kept apart from instruction.
      None of that ships today and the handbook is deliberately not
      guessing it from its own single instance. Two unfinished
      drafts sit in its temp/, repo-shapes-model-draft.md and
      repo-shapes-gap-list.md; they are thinking, not decisions,
      they bind nothing, and they are ours for the asking. The
      trigger is our next authoring, not a date.

- [ ] Two constraints that bind if we ever restructure our own
      parts, from the same note: whatever we split them into, do
      not call them conventions — that word means method, and
      method has one owner, the handbook. And keep the concept
      beside those parts rather than inside them: the executions
      are derived from the concept, and a repo that reframes itself
      around its executions loses the thing they derive from. Told,
      not delivered; recorded here because the moment it binds is
      one where it would otherwise be forgotten.

- [ ] Concept question from run 3's SL-1 (2026-09-14): a guarantee
      held by absence — no process clock, no state outside the
      store — has no runtime evidence; its wall is a rule on the
      compiled classes (ArchUnit, each rule with a `because`
      naming its guarantee, each shown to fire on a plant). Run 3
      asks for a rung between "single validated entry path" and
      "code review". The hierarchy lives in concept/02 as well as
      both cbc-slice files, so this is a concept change — an ADR
      and the version question (CBC ADR-0003), not a bundle
      harvest. Lived once; a second run meeting an absence
      guarantee is the trigger.

- [ ] A kit-update procedure for a born run, as an install doc
      beside pure-seed.md: the operator block that served once in
      temp/prebriefing-run-3.md — cut a receipt branch kit-<pin>
      from the seed commit carrying the old pin, copy the kit over,
      commit, switch back — with the two things the first run
      taught: guard the `git add -A` against the run's untracked
      files (temp/ nearly rode into the receipt), and say in the
      prompt where the why lives, since the receipt cannot carry it
      and the run's §8 points at a checkout on disk otherwise.
      Every future kit update to a run needs it; the pure seed's
      birth block is the model, and since 2026-09-17 so is
      starter/installs/bundle-update.md, which answers the same
      gap for the bundle — who does what, the copy staged in the
      run's own temp/, the note beside it.

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
- [ ] "Backend" in the skills' description lines (cbc-framing,
      cbc-slice, infra-establish) and both parked entry-file
      templates — kept 2026-09-06: it is the toolkit's honest
      scope, and every run so far is one. At the first
      non-backend run the description lines are where to start;
      the practice skills' bodies (compose, Flyway, Spring Boot)
      are the larger job behind them.
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
- [x] DONE 2026-09-12 (9bdd33a, the Step 4 harvest): the
      application template reads POSTGRES_PORT, the key the env
      and compose templates name. checkout-system's own pair is
      its own to fix. Original item:
      checkout-system reads the db port as CHECKOUT_DB_PORT while
      its .env.example names POSTGRES_PORT — two env keys for one
      fact, found at template extraction. If it is a defect, fix it
      in the run first, then harvest; the templates carry it as
      lived.
      (2026-09-12: run 3 lived one key, POSTGRES_PORT in both
      .env.example and application.yaml — the Step 4 harvest's
      fix 6 aligns the template to it; this item closes with that
      change-plan. checkout-system's own pair is its own to fix.)

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
