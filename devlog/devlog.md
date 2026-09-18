# Devlog

<!-- Newest entries on top. 2–5 minutes at the end of each session.
     For future-you: fragments fine, honesty mandatory. Never clean up.
     Mark dead ends loudly with "DEAD END:" so they're greppable.
     End every session with a "Resume:" line — cheapest save-point there is.
     When this file gets long, split into devlog/<YYYY-MM>.md per month. -->

## 2026-09-18  (the kit comes here; a compare stops meaning identical)

- The one-chain question was decided and executed in one session,
  which was not the plan when the session opened. Two ADRs and
  thirteen commits: `starter/kit/` now holds the handbook's kit at
  `ba7eaa4`, fourteen of sixteen files verbatim, and the birth no
  longer runs another repo's bash in our shell.
- The session's own idea, and it is the user's: a compare is not
  "are these identical". Between two repos that have both grown the
  question is what either side has learned that the other should
  have, and that question does not care which side moved. That
  dissolved the objection that had blocked the take for a day —
  two masters, so the compare dies — rather than answering it.
- What kept the mechanical half alive was our own history. The pass
  of 2026-09-09 produced five findings that split by instrument:
  two only a reading could find (ADR-number collisions inside
  byte-perfect copies), two only a diff could (the installed drift,
  the pin lying since 09-07 because a change was absorbed through
  conversation with no entry). Neither instrument finds the other's
  findings. So ADR-0023 keeps both: the diffs are evidence, the
  reading decides, and a verdict is written every time including
  "taught nothing".
- ADR-0023 earned itself twice in a day. Ten minutes after it was
  committed its mechanical half found the three fills claiming a
  re-verification made at `ab916a1` while we sit at `ba7eaa4` — the
  09-17 re-pin covered the four skills and the two models and not
  them. Harmless, as it happens: the entry files were unchanged
  across the span. Then during the manuals' copy a byte check
  called sixteen wrong files identical, because both sides were
  read through the same broken step. A check that pulls both sides
  through one broken read confirms nothing, and that is the failure
  ADR-0023 exists to make visible, met on day one.
- The take came in smaller than measured. 16 files, 926 lines;
  thirteen were expected verbatim and fourteen landed, because the
  user chose to keep the playbook a document rather than fold its
  steps into `PLAN.md`. That kept ADR-0011 untouched and playbooks
  a menu, at the cost of the marked-region insert surviving as the
  birth's one genuine merge. The forward reason is Step 9's: a CbC
  project that is not Spring and Postgres wants a different
  sequence.
- Two things were decided and not done, and only a question found
  them. ADR-0024 decision 5 brought the seven manuals here and no
  step of the change-plan did it. And the same decision was written
  without its second half — their manuals explain their artifacts,
  so anything we flavour needs an explanation that is ours. The
  delta list is that explanation today; outgrowing its table is the
  signal the flavour has turned rule-level.
- DEAD END avoided, and the avoidance is worth more than the fix:
  `convention-lifecycle` tells a run to diff the handbook, and a
  one-chain run holds no handbook checkout. Two options were costed
  — flavour their rule, or carry it in our procedure — before
  reading three lines further, where their own paragraph says the
  handbook is "a checkout on disk or the payload a handoff
  carries". Our delivery is that payload. Nothing needed changing.
  The finding that goes up instead is smaller and real: their
  sentence assumes the payload comes from the handbook itself, not
  from an intermediary holding their files at a pin it chose.
- The letter to the handbook was written too early, on an
  instruction I had put in the ADR myself — decision 9, "three
  things go up before the take lands", which contradicted the
  draft's own conclusion that sending first would be two letters
  where one will do. The user caught it. The decision is now
  decision 10, sent after, and the letter is held in `temp/` with
  a block naming what to refresh before it goes.
- `temp/` cleared, and the clearing was a harvest rather than
  housekeeping: the one-chain draft held two things no ADR had —
  the handbook's own ADR-0041 statement of this role, and the back
  door considered and rejected. Both landed before the draft went.
  The sketch that had been steering the work, while declaring it
  bound nothing, graduated into PLAN steps 7 through 10 — which
  also closed a three-week hole where sixteen decisions and three
  seeded runs had no step around them.
- One local rule arrived from the material: paths are written from
  the repo root, never relative to the file. The vendored manuals
  cite relatively; read from a new root, two of their four outward
  links dangled and two resolved only because `docs/models/` is
  where we happen to keep those files. Every artifact this repo
  makes is read from a root other than the one it was written at.
- Parked for Step 9: the handbook keeps Spring hygiene overlay
  parts as templates appended below the base layer's marked line —
  their own skeleton-plus-flavour shape, built once, deliberately,
  in exactly one of sixteen kit files. Our `cbc-bootstrap` points
  at none of it, so three runs have grown by hand what a template
  already held.

Resume: Step 9, the groups — the work kit, the concept and its
skills, and the practice executions shaped by one stack, which the
repo has drawn three times without naming (the derives-from versus
checked-against split, the reference held out of the bundle, six
templates all in one group). It stands whether or not the take had
landed, and the Spring-overlay item waits inside it. Step 10 is the
delivery run that produces the letter's lived numbers; nothing goes
to the handbook before it. Nothing is owed to either side today.

## 2026-09-17, later still  (both documents delivered, both answered; the exchange ran twice on its first day)

- The exchange ADR-0022 decided was exercised in both directions
  within hours of being written, which was not the plan and is the
  best evidence the set produced. Both receivers read a note, read
  their own records, decided for themselves, wrote their verdict
  into their own logs and deleted the paper. Neither repo reached
  into another.
- Run 3 first. The note went into its temp/, and its two commits
  came back accurate on the parts least certain to carry: the seven
  rules taken as written, the channel "declined, and replaced", the
  facility paragraph held with its trigger, and our reason for
  sending no path restated in its own words. It caught two things
  unprompted that the note did not spell out — that its rule 2 now
  adds a dated line to a header block with no counterpart upstream,
  and that its own temp/ is ignored, so it put the record where it
  survives. bundle-update.md gained a paragraph from the second: a
  run's temp/ need not behave like ours, and the decisions entry is
  therefore the whole record rather than a pointer to one.
- The handbook took the trigger as fired — bundle-update.md is
  their ADR-0030's second clause — and then narrowed it rather than
  writing the convention: it now waits on the first live run of
  that manual. Their reason is our own argument turned around, and
  it is right. The thin-note diagnostic is a claim about what a
  receiver does when a note falls short, and no receiver had read a
  note under it; writing the rule now would freeze a prediction.
  They set a guard with it — a third re-park means the answer is
  no, not later — which is the kind of thing worth stealing.
- One correction from them, accepted. Our handoff said run 3
  reached "copied whole" independently. It did not: its handoff of
  09-15 went to both of us, their ADR-0038 came from it, and what
  we read as two arrivals was one with two recipients.
- And the correction's cause is ours, lived the same day. They had
  to work out that our "run 3" is their "never-oversold", got it
  wrong first, and staged the wrong version before catching it. Our
  records say "run 3" a hundred and sixteen times and
  "never-oversold" once — and the only live bridge between the two
  was the bundle's harvest lines, "never-oversold (run 3 of the
  pure seed)", which this session deleted. ADR-0022's cost, on its
  first day, to the party we had just written to. The fix is a
  second rule in temp/README beside its sibling: a document naming
  a third repo gives both names, with the three names written down
  and the condition for the table outgrowing the file.
- Their two repo-shapes drafts arrived with the reply, verbatim and
  deliberately not rewritten against our handoff — "rewriting first
  would have handed you a conclusion instead". Two things in them
  join the next step: bases-not-stubs, what a receiver gets is
  complete as delivered and extended locally; and only-the-set-is-
  copied, anything about the set kept beside it. The second is the
  test for whether the bundle's kit is built right, and starter/
  already has the shape.
- The one to watch, recorded in the draft and not acted on: their
  model §4 states two upstreams as fact — born with the kit, bundle
  on top — and their B3 wants the model folded into the tiers model
  we vendor. Nothing is delivered, so nothing is declined; when it
  arrives we take it whole, as we just told a run to, and a
  disagreement goes up as evidence rather than into the copy. They
  have built the door themselves: their §7 names three refutations
  and one is close to what one-chain would show.
- The one-chain idea itself grew all session and is thinking only.
  What re-reading the material added, against the argument: the
  coupling to the handbook is not a pointer but shared shell state
  across two repos, unpinned; the seed already performs surgery on
  a kit decision it disagrees with and waits for the kit to adopt
  our preference; starter/fills/ is the bundle's kit half-built,
  two files already carrying the kit's text verbatim; and the cost
  nobody had named — runs are the handbook's only field data about
  its kit, and interposing removes it. A sketch holds the order,
  orientational, and says what it does not settle.

Resume: nothing is owed to either side. The handbook asked for one
thing whenever it happens — that bundle-update.md having run for
real, we say what it taught or that it taught nothing — and run 3's
backlog line for us is closed. Next is the sketch's step 2, the
bundle's kit, which is both the answer to the one-chain question
and the message the handbook asked for. Before it: decide whether
every handbook update being evaluated here twice, for ever, is
worth one chain to a run. If it is not, the sketch fails at step 2
and the honest move is writing down why.

## 2026-09-17, later  (the harvest notes leave the bundle; the exchange replaces them)

- Two questions turned out to be one. Run 3's handoff asked whether
  a run may edit its copy of a method skill between two pins, and
  named its channel — our verdict read "as a document or as the
  header line the run sees at its next copy". We asked separately
  whether the skills could be as lean as the handbook just made its
  conventions. The notes the second question removes are the
  channel the first uses; run 3's own registry says so, calling the
  harvest lines "the record of what was taken". ADR-0022 answers
  both: yes to the edit, no to the channel, and the exchange — a
  note and a copy, the same both directions — in place of it.
- DEAD END, and it cost a written commit: a manual per skill under
  starter/manuals/, holding every removed note verbatim. cbc-framing's
  was written, staged and shown before the check ran. `git log
  --follow` on templates/registry.md returns the header's own
  harvest lines as commit subjects — ec8e504, dd481ea, 7531281 are
  three of them word for word — and the commit bodies say more than
  the headers did. ADR-0007 had already listed that shape and
  rejected it, in its own words "a second log for what git history
  and the file itself can already record". The user saw it first
  and asked why we could not just put it in the records. Kept as
  ADR-0022's option 5 rather than deleted, so it is not re-proposed
  in three months.
- The strip: 28 files, 520 lines out, 16 in. The cut is per line,
  not per block — a template header mixes a copy-and-fill
  instruction and a lived trap in with the extraction record, and
  a block rule would have deleted the trap that binds
  testcontainers.properties to $HOME. Every dropped harvest line
  was checked against the body first; each one recorded a change
  the body already carries. The two .sql templates needed the
  boundary placed by hand, their bodies opening with -- comments
  too.
- One thing moved rather than went: the worked-example twin rule —
  the two copies are identical, a change to one lands in both — is
  a standing rule, not a record of a past change, and had no live
  home once the headers went. It is in ARCHITECTURE's executions
  section. With both headers gone the twins are byte-identical, so
  diff now checks what a sentence used to assert, which closes the
  TODO line recording the discrepancy.
- The exchange, the user's design, arrived mid-set and was the best
  turn in it. A note is not a wrapper for a path — it is an
  insight: the sender reads the receiver's records, evaluates, and
  writes where you stand, what changed, why it matters to you, what
  it recommends, told not delivered. We had the worked example
  already: the handbook's note of 09-16, which we verified in the
  material rather than complying with. And the path question
  dissolves — a good note plus the files is complete, so reaching
  for a path is the diagnostic that the note was thin, not
  something to forbid. A run gets a copy in its own temp/, never a
  path: our records hold our readings of the run, and a run that
  can read its own assessment stops being an independent instance.
- Two gaps the set had to fill. starter/installs/bundle-update.md
  did not exist — pure-seed.md covers birth and nothing after it,
  and run 3's one re-pin ran without a written procedure. And the
  handbook's parked exchange item names its trigger as "a second
  endpoint speaking it — a second concept repo, or a run repo
  injecting from a concept"; the second clause is now true, so the
  hand-off went up with four pieces its five points do not reach,
  including that its "the compare survived" narrows again for a
  receiver holding no checkout, whose compare runs against its own
  delivery commit.
- Three questions from the user parked with triggers rather than
  settled: whether the worked example anchors a run's framing (no
  evidence in three runs; one weak signal, both landing on "one
  area", which has two explanations); whether the twin should be
  deduplicated; and whether a project could ever need its own mould
  of a skill, where run 3's rejected overlay is the named fallback.

Resume: the set closes on the word, then main fast-forwards. Then
two documents wait in temp/ for the operator to carry — the
hand-off to the handbook, and the note to run 3, which goes with
run 3's next bundle copy under the new procedure. Nothing is owed
here until one of them is answered, or until run 3's in-place rule
fires for the first time, which neither of us has watched.

## 2026-09-17  (the handbook delivery @ ba7eaa4, taken under a note; run 3's ask parked one set out)

- A note arrived in temp/ on 09-16, told not delivered: the kit
  moved and the update procedure at our pin names three things that
  no longer exist — the directory it diffs, the `delivery`
  frontmatter field it reads, the CONVENTION.md master it copies
  from. Three corrections, applied once, and the problem is gone
  for good because the new procedure does not have it. Taken this
  session: the four skill copies and both models at ba7eaa4,
  compare-first clean on all six, and registry entries for all
  seven conventions.
- The corrections checked out in the material, not only on the
  note's word. conventions/<name>/stubs/*.md at ba7eaa4 are
  symlinks into starter/kit/ — a plain diff calls them different
  and they are 0-line files holding a relative path, which is the
  exact trap correction 1 warns about. And the compare survived the
  layout change: `git show ab916a1:conventions/<name>/CONVENTION.md`
  resolves although the file is gone at HEAD, because the compare
  is at our pin. A layout change breaks the fetch, not the
  comparison — the handbook recorded the same narrowing at da93a88.
- What actually changed, as against two thirds of the text being
  cut: convention-lifecycle §3 step 4 gains "a project may edit its
  copy between two pins" (HANDBOOK ADR-0038, provisional) and the
  receipt branch as the compare where one exists; its `requires`
  drops artifact-kinds; its description gains a mid-step trigger.
  tiers §3 says an edited copy is not a third form of delivery and
  that its diff against the pin is a record the tier above reads.
  The rest is exemplars moving and prose leaving.
- Run 3's handoff arrived 09-17 with one ask: may a run edit its
  copy of a bundle skill between two pins? Parked deliberately for
  the next set. The handbook settled that shape for its own four
  conventions at kit 9e28143, from run 3's own hand-off, and the
  text rides inside this delivery — answering CBC ADR-0007 first
  would have been writing blind to it. The ask does not block run
  3: its Step 6 opens on the copies as they stand.
- Checked before assuming: run 3 is on our latest bundle exactly.
  All 28 files under starter/bundle/ byte-identical to its copies,
  file lists identical, nothing uncommitted or untracked in its
  skill directories, no commit touching them since its re-pin, and
  all five concept chapters identical. Its in-place editing rule is
  live but unexercised — there is no skill diff to harvest, here or
  anywhere, which is what its own handoff says too.
- First branch in this repo: handbook-delivery-ba7eaa4, cut from
  main at 7bbf49a, closing by fast-forward. Not kit-<hash> — that
  spelling means a receipt branch in the procedure being taken, and
  we hold none. On trial for this set; the retrospective decides
  whether it becomes anything.

Resume: the set closes on the word, then main fast-forwards. Next
is run 3's ask — read its unread span a08093d..5a4b548 read-only,
with its staged TODO and .claude/rules/skills-changed-in-place.md,
then answer in CBC ADR-0007 and starter/README.md's Harvest
section: taken, reshaped, declined or held, naming our hash. After
that, whether run 3 is told the kit moved — it is pinned at
9e28143, before the restructure, and will meet the same break with
no note.

## 2026-09-15  (run 3's SL-1 harvested into cbc-slice; the reference held, not shipped)

- The harvest change-plan (0205a7d): six fixes from run 3's SL-1
  into cbc-slice's skill, workflow and readiness reference, the
  framing's registry template and the bootstrap's harness
  reference, each in the run's wording, one dated harvest line per
  change per file (CBC ADR-0007). Two rewordings at boundaries, the
  user's questions: the Stage 3 red gate, staged first as run 3's
  process (naive commit first, the wall its own diff, red before
  the wall's commit), asked whether it over-restricts — it did,
  for a slice whose wall already stands, and for a brownfield first
  slice — and reworded to the outcome only, each test seen red
  with its wall absent, three ways of making it absent named; and
  "never committed" widened to "never lands in history".
- The seventh fix diverged at its boundary (124744c). The Spring
  slice reference was staged into the bundle with a pointer in the
  skill, then the pointer moved to Stage 3 with a read-after-the-
  plan guard; asked whether that stops an agent reading it early,
  the honest answer was no — a prose guard is the code-review rung,
  and the Stage 2 comparison plus the sign-off were the only wall.
  The user's design instead: the reference held here beside frozen
  v2, blind to newborns, handed to a run as session input after its
  build is committed on its branch and before the fast-forward, for
  a comparison shape by shape whose verdicts come back as harvest
  lines — the gates experiment's protocol applied to the build,
  with a second derivation on a fresh branch as the reviewer's
  option. ADR-0021 revised then accepted; the skill carries no
  pointer and is unchanged for it.
- Nothing in concept/ moved: no CHANGELOG entry, no ADR beyond
  0021, no concept version. Run 3's copies stay at their pin; its
  ten items answered at the master or handed back — the absence
  rung waits as a concept question, the contract wording is the
  run's own document.

Resume: the set closes on the word. Then nothing is owed here until
run 3 closes SL-2 on its branch — told at its Step 6 opening which
of its ten items the master took, and the close reminder line; at
its close, before the merge, the first build comparison, and after
the merge the reading, now in two categories. The run's first skill
diff, if its in-place editing produces one, is read hunk by hunk
against the master as it stands after this set.

## 2026-09-14  (run 3's Step 5 read: SL-1; the gates reading; the trials held; ten hand-offs, seven for the bundle)

- Run 3 closed Step 5, SL-1 no over-admission under contention, on
  step-5-sl-1: eighteen commits, 2026-09-12 → 14, cut from the
  Step 4 close (be61f60), fast-forwarded to main before the
  reading. Read read-only. Six guarantees by attack, zero
  mechanisms; the store's check constraint and one conditional
  UPDATE as the wall; both storms red without the wall (22 and 23
  of 20) and green unchanged with it; the adjustment race; the
  one-clock pair; ArchUnit rules for the absence guarantees after
  a text-search dead end; 29 tests under the one command; the run
  on the real ground with V1 applied as `migrator`. The slice
  record is one document in three movements — spec, plan,
  evidence — with dated sign-offs; the registry flips SL-1 closed
  and keeps SL-2 next by a dated revision naming what SL-1 leaves
  it; version 0.1 as a state of the evidence.
- The gates reading, Step 5 — derived twelve vs frozen v2's two:
  both covered, sharper (Stage 0 recorded, the two opening ADRs,
  each stage's exit with the reviewer's sign-off, the probe pair's
  deletion, the records). v2's records line — one doc per slice,
  spec → plan → evidence — re-derived exactly. Of v2's four
  warnings: the red-check re-derived unaided and stronger — not
  break-the-guard-after but red before the wall exists, since R5
  has nothing to break at the first slice's Stage 0; the
  gate-item-to-named-commit mapping not in the gate, the one
  divergence (sub-packages against "one package-private package")
  recorded at the close anyway; the erosion cross-check and the
  composition warnings do not apply to a first slice — untested,
  not missed. No hand-back.
- The four trials held a fifth step: branch cut at the previous
  close, tip on main by fast-forward; eighteen commits, none
  straddling; the entry file edited at .claude/ once, the
  slice-records row; the pace in no record; no handbook read —
  three "handbook" mentions in the diff, all one TODO line naming
  it as the kata skill's destination, the first time the run names
  the handbook as a target. Four subjects over 50 (52, 53, 54, 54).
  The branch item ticked "on the reviewer's word to merge, given
  at this boundary" — the held wording, again.
- Ten hand-offs filed, nine for the bundle, one for the handbook.
  Seven confirmed at the master: R5 at the first slice (the
  readiness reference says drop the constraint or comment the
  guard — neither exists yet); the birth whats (Stage 1 takes only
  the registry's invariant and adversity; nothing names the
  schema, the door, how the aggregate comes to exist; the worked
  example is duplicate-delivery); the owner candidates as a
  comparison the signer weighs (Stage 2 asks for one owner,
  justified, never the rejected faces — the run restated its own
  §7 after the close); body assertion (the harness reference
  itself asserts by substring in its contention probe); what a
  flag demands (the framing template's flag-riding line, cbc-slice
  silent on it); the close as more than a status (the template's
  `in-progress` never used; concept 04's "a built slice may teach
  that the next is wrong or split" has no Stage 4 step making it
  true in the registry); a stack reference beside the stack-free
  skill, on the bootstrap's model — a shape change, an ADR here.
  Two not as stated: the absence rung asks for a new level in the
  enforcement hierarchy, which lives in concept/02 as well as the
  skill — a concept change, ADR and the version question, not a
  bundle harvest; the contract's "in its own specification" is
  run 3's own contract document, not the master's — no
  infra-establish file names faces — so the fix is the run's. The
  kata skill goes to the sixth handoff.
- Run 3 has a staged, uncommitted agent-side decision: its method
  skills may be edited in place under five guards — lived, a
  question or outcome never the run's answer, logged in the
  skill's header and its decisions log, handed to the source as a
  diff against the pin, our verdict back as one line there. The
  concept chapters stay pinned. The run's arrangement to make;
  what changes here is the channel — after these ten prose items,
  hand-offs arrive as hunks. Decided at the reading, the user's
  call: harvest the seven confirmed items now as prose per CBC
  ADR-0007, and tell the run which it need not re-edit; the diff
  channel is read when the first diff arrives.
- The entry-file watch: the bootstrap half held through a fifth
  step — the opening paragraph has stated no state since the 09-12
  cut, nothing to go stale; the establish half stays open for the
  next run. Nothing for the playbook: the slice step's gate
  derives at opening, and the run did that.

Resume: the harvest change-plan for run 3's SL-1 — seven fixes
across cbc-slice's skill, readiness reference and workflow, the
harness reference, and the framing template's flag line; the
stack reference as an ADR; harvest lines per CBC ADR-0007, pinned
copies untouched. The absence rung waits as a concept question in
TODO Later. Run 3 opens Step 6 (SL-2) in the run, the user's way;
back here at its close, or when its first skill diff arrives.

## 2026-09-12, later  (run 3's bootstrap harvested into the bundle; the fill's state clause cut)

- The harvest change-plan (7652e2c): nine fixes from run 3's Step 4
  into cbc-bootstrap's skill, walkthrough, harness reference and
  three templates, and one into the entry-file fill — each in the
  run's wording, one dated harvest line per change per file (CBC
  ADR-0007). Revised once before work began (df39fbe): run 3 had
  re-read the skill after its merge and filed four hand-offs, three
  matching planned fixes and one new — the refusal test in the
  miniature, which enters the reference as code, lived once, since
  its trap (assert on the root cause) is in the three lines' shape;
  the forked-instance shape enters as prose, a variation point,
  until a second run lives it.
- The morning's call on the entry file reversed on the run's own
  fix, the user's word: not "the skill makes the line true at each
  close" but "no state line at all" — the run dropped the clause,
  current state being PLAN's by the records table. So the fix
  landed in our fill, not the skill: the orientation states only
  what never changes, a standing comment beside it says why, and
  the kit's stub with the same clause goes to the handbook through
  the sixth handoff, with agent-arrangement's test 2 gaining its
  instance.
- Verified here rather than taken from the report: the Ryuk key,
  against the Testcontainers 2.0.5 jar — the properties file reads
  only the ryuk.container.* keys; the switch is the environment
  variable.
- Nothing in concept/ moved: no CHANGELOG entry, no ADR, no concept
  version. Runs 1 to 3 hold their copies at their pins; run 3's two
  bootstrap hand-offs and the four from its re-read are all
  answered at the master, its own TODO items its to close at a
  re-pin.

Resume: the set closes on the word. After it, nothing is owed here
until run 3 closes Step 5 (SL-1, cbc-slice), read at its boundary
as the others were — its Stage 0 is where v2's two un-derived
items (the deliberate break, the R1–R6 record) get their reading.
The sixth handoff accrues in TODO with no trigger set; the
establish half of the entry-file watch stays open for the next run.

## 2026-09-12  (run 3's Step 4 read: the bootstrap; the gates reading; the trials held; eight for the bundle)

- Run 3 closed Step 4 Skeleton & bootstrap on step-4-bootstrap,
  fourteen commits, 2026-09-11 → 12, fast-forwarded to main before
  the reading, as the others were. Read read-only. Spring Boot
  4.1.1 on Java 21 by fluency and audience (its ADR-0007), the
  lived default structure after the alternatives were laid out
  (ADR-0008), the harness racing three forked instances of the
  build's own output against one throwaway store (ADR-0009 —
  the one place it left the harness reference, by decision);
  the requirements certified member by member from the delivered
  files; seven tests green from a clean build with nothing
  exported; health UP with the store UP on the real ground as
  `runtime` and no other identity.
- The gates reading, Step 4 — derived sixteen vs frozen v2's
  five: all five covered, most sharper (requirements and ADRs
  before code, the README commands, the overlay below the
  marker). Two of v2's not re-derived, both cbc-slice's Stage 0
  at the next opening — the deliberate break turning the harness
  red (R5) and the R1–R6 readiness record; nothing to hand back.
  v2's three warnings all re-derived unaided: the miniature
  mounts the ground's own bootstrap SQL, surefire widened to
  `*IT`, the Boot 4 test-client annotation on the web base. The
  additions trace to the skill's stages, the definition's
  runtime ground (F17, the intent's own done-line — plural
  instances, never a sequential replay), and SL-1's clock flag.
- The four trials held through the step: branch cut at the Step
  3 close, tip on main by fast-forward, no commit straddling
  agent and project paths, the entry file edited at .claude/
  once, no handbook mention in the diff, the pace in no record.
  Three subjects over 50 (52, 55, 56).
- Seven findings for the bundle, the run's two hand-offs among
  them, each confirmed at the master (TODO Now, one harvest
  change-plan): the Ryuk trap and the properties template are
  stale on Testcontainers 2.x — checked here against the 2.0.5
  jar: the properties file reads only the ryuk.container.* keys,
  the disable switch is the environment variable, and Ryuk
  reaped fine under rootless podman 5.8; Stage 2's `internal/`
  path, which neither lived run used (both: docs/construction/);
  the plural-instance machinery the reference lacks (the store
  lifted out of the base, a process helper, the probe answering
  its pid, the runtime classpath written by the dependency
  plugin so the fork is the real app from the one test command);
  a missing secret does not stop the app — Boot binds the
  unresolved placeholder as the literal, health alone tells; the
  Boot 4 Flyway module split — the engine alone on the test
  classpath runs no auto-configuration; the application
  template's port key against .env.example's POSTGRES_PORT (the
  checkout two-keys item, lived as one key); Initializr on Boot 4
  already emitting the renamed starters.
- One miss in the run, the TODO watch item's answer: the entry
  file's opening line still says "the ground stands, no code
  yet" — Step 3 rewrote that line, Step 4 touched the file only
  for the records row. The fix is the run's own agent commit.
  The user's call at the reading: the skill carries the moment,
  so the next run does it unprompted — cbc-bootstrap's Stage 5
  names the entry file's opening line beside the README
  projection, fix 8 of the harvest. The kit owns the file's
  shape, not that line's truth; noted for the sixth handoff.
- Nothing for the playbook from this step; the branch-rule lines
  still wait on the trial verdict at the run's retrospective.

Resume: the harvest change-plan for run 3's Step 4 — eight fixes
across cbc-bootstrap's skill, walkthrough, reference and three
templates, harvest lines per CBC ADR-0007, pinned copies
untouched. Run 3 opens Step 5 (SL-1, cbc-slice) in the run, the user's
way; back here at its close.

## 2026-09-11, later still  (run 3's ground harvested into the bundle)

- The harvest change-plan (c6dbd68): six fixes from run 3's Step 3
  into infra-establish, infra-serve and cbc-framing, each in the
  run's wording with one dated harvest line per change per file
  (CBC ADR-0007), the first lines written in the tagged form. The
  records section now says what run 3 lived — no establishment log
  in a repo with records; decisions as ADRs, the walk in the devlog,
  expected results in the verify suite and the operator manual, the
  mapping note in the environment ADR — and the layout both runs
  used; one correction at the boundary, the user's: the log a
  record-less repo keeps goes under docs/ beside the manuals, not
  under infrastructure/, which holds only what runs — checkout-
  system had it there already. infra-serve reads the ground's record
  wherever it lives, so a re-entry no longer fails on a log never
  written.
- Stage 0's check 2 names the return trip; the census asks for the
  runtime ground at framing, closing the mismatch between two of our
  own skills; the walkthrough carries the health-check window and
  the client-container witness read; the verify suite checks the
  CONNECT revoke, with the live probe beside it; the SQL templates
  say which naming case they ship. The verify template took three
  harvest lines from this set, one per change, the user's word.
- Nothing in concept/ moved: no CHANGELOG entry, no ADR, no concept
  version. Runs 1 to 3 hold their copies at their pins.

Resume: the set is closed (8379781); after it, playbook v6 landed
with Step 2 retitled Identity (3242c59), the branch-rule lines held
for the version after run 3's trial verdict. The tree is clean, 26
commits today — the reading, the reply absorbed, the harvest, v6.
Nothing is owed here until run 3 closes Step 4 (cbc-bootstrap), read
at its boundary as the others were; the sixth handoff accrues in
TODO with no trigger set. The Step 2 hand-back line was never told
(checked in the run's transcripts, read-only) and is skipped for run
3 by the user's call — the moment was Step 2's, and the run re-read
its plan unasked; it waits for the next run's Step 2 opening, the
clean test of the told channel, or for playbook v6. Runs
1 to 3 hold their copies at their pins; a re-pin, each run's own
act, brings the tagged citations and the six fixes.

## 2026-09-11, later  (the fifth reply absorbed; the kit at ab916a1; the CBC tag)

- The reply arrived this morning, the user's file into temp/,
  committed as delivery (44b5bac) before the plan. Absorbed under a
  change-plan (bd3b785): pinned copies to ab916a1 — the four skill
  copies and both models, compare-first clean, tiers moving for the
  first time since the birth pin; the three installed conventions
  registered at the hash, one carry (README's decisions row);
  repo-hygiene unchanged across the span, pin left.
- What the reply settled: decision 5 closed on run 3's report, the
  kit's stub staying at the root and the seed's rename at birth the
  bundle's own; decision 1 withdrawn outright — the kit ships no
  settings file, and the 09-09 rejection here is now the kit's
  state; the citation ask returned as a rule wider than asked — a
  tag per repo, both directions (HANDBOOK ADR-0037), every
  convention and model now reading HANDBOOK ADR-nnnn; exemplars by
  role; the born-without sentence in §8; the tiers model's §3
  rewritten from our five with the told channel named; the
  three-voices report absorbed as an agent-model correction (the
  window carries roles, W2).
- The tag question decided here, ADR-0020: this repo is CBC. The
  bundle's 102 citations of our decisions — six numbers, all ours —
  swept to CBC ADR-nnnn by script in one commit, verified by grep
  both sides; the collision it ends was lived, run 3's ADR-0003
  against ours in cbc-framing's header. Records, the bundle doc,
  the seed and the fills' headers stay bare; the temp rule for told
  text stands, since a told line is unfollowable either way. No
  header line per file for the sweep — logged once, the user's
  word at the plan.
- The fills re-verified at the pin: the README fill's row gains the
  stub's clause with <TAG> literal; the CLAUDE stub unchanged; the
  playbook's kit steps untouched by default.md's two comment
  changes. PLAN's decision index caught up, ADR-0014 to 0020 — it
  had stopped at 0013. The fifth-handoff item DONE; a sixth opens
  with the post-draft material.

Resume: the two served drafts leave temp/ and the set closes. Then
the harvest change-plan for run 3's Step 3 — six fixes across
infra-establish and cbc-framing, harvest lines now written as CBC
ADR-nnnn. Run 3 opens Step 4 in the run, the user's way; back here
at its close.

## 2026-09-11  (run 3's Steps 2 and 3 read: the identity and the ground; the gates reading twice; the trials held)

- Run 3 closed two steps since the Step 1 reading, both
  fast-forwarded to main before it, as then. Step 2 Identity on
  step-2-define, eight commits, 2026-09-10: named never-oversold by
  ADR-0003, seven candidates against a four-point bar the run wrote
  itself, the working name overturned in so many words, the remote
  created by the reviewer by hand. Step 3 Ground on step-3-ground,
  eighteen commits, 2026-09-10 → 11: PostgreSQL 17 under podman
  compose as the whole service set, eight exclusions each with its
  why, nine constraints each with its enforcement, verified both
  ways from actual output, T2's tool refused live, the clean
  re-stand from the operator manual alone. Read read-only.
- The gates reading, Step 2 — derived eight vs frozen v2's three:
  all three covered sharper, five additions v2 never had (the
  remote as part of the identity, the step retitled at opening;
  CHANGELOG; README true for a stranger from the remote; the devlog
  entry; the branch item). v2's one warning, scope in the
  description, re-derived unaided. A cache, whole; nothing to hand
  back.
- The gates reading, Step 3 — derived eleven vs v2's four: all four
  covered in the skill's form; the additions traced to the skill,
  the definition's trust line (T2's tool named, its refusal seen —
  an item no playbook could hold), and the records. v2's two
  warnings both re-derived: the runtime-ground return trip lived
  exactly as checkout-system's, Stage 0 tripping and L1 revised by a
  dated entry in one commit; grants as authority from the role-split
  reference. v2's records line, "an establishment log of actual
  outputs", is the one thing refused: the log opened at the decision
  and was withdrawn a commit later at the reviewer's question — what
  does it hold that the records do not? — the walk in the devlog's
  tables, decisions in ADRs, expected results in the verify suite and
  the operator manual. checkout-system kept its log; both runs put
  compose.yaml at the root, the runnable ground under
  infrastructure/, the manuals under docs/, and the skill's default
  paths match neither. Nothing to hand back to the run.
- Six findings for the bundle, the run's two hand-offs among them,
  every one confirmed at the master (TODO Now, one harvest
  change-plan): the log-less shape and the layout as the default for
  record-keeping repos, with somewhere for the mapping note to go;
  Stage 0's check 2 naming the return trip instead of "stop";
  cbc-framing's census asking for the runtime ground — the mismatch
  is between two of our own skills; two walkthrough traps (the
  init-time temporary server behind a healthy check; the witness
  read from a host without psql); the verify template's missing C3
  query; the templates' unconditional role prefix against the
  reference's conditional one.
- The hand-back line for Step 2 left no trace in the run: neither
  gate carries a middle-steps item, no devlog line. Whether it was
  told is the user's to say; the TODO item stays open, annotated.
- The four trials held through both steps: each branch cut at the
  previous close commit, tip on main by fast-forward, the merged
  branches kept; twenty-six commits, none straddling agent and
  project paths; the entry file edited at .claude/ in two agent
  commits; the pace in no record, the destructive acts on the
  recorded yes; no handbook mention in any diff. The run answered
  the Step 1 branch-item finding itself — "ticked on the reviewer's
  word to merge, given at this boundary". Two more subjects over 50,
  the em-dash revision form. One change-plan shape new to us: an
  outward action, the remote, as a numbered step with no commit, so
  the close body could say whether it happened.

Resume: the harvest change-plan for run 3's Step 3 — six fixes
across infra-establish and cbc-framing — is the next act here. The
fifth handoff's reply arrived during this reading, the user's act:
temp/handbook-reply-2026-09-10.md, staged, unread here beyond its
headings — it names a new kit pin, ab916a1, and says the commit gate
is gone from the kit. Absorbing it is the next session's first act,
before the harvest. Run 3 opens Step 4 (cbc-bootstrap) in the run,
the user's way; back here at its close.

## 2026-09-10, later  (the run 3 framing harvest into cbc-framing)

- The harvest change-plan (da5c95f), four fixes to the cbc-framing
  master in the run's wording, one dated harvest line per file
  touched (ADR-0007), the pin untouched: the registry template
  opens in project voice; its fold-reconciliation line is a table
  under a sentence naming L4 the master — the reviewer's touch-ups
  in run 3, harvested without a filed hand-off, the plan's one
  decision open to objection; the export section says the order
  is the commits' and the file ends L1→L5; the residue filter
  refuses agent language, run 3's rule.
- Correction to the entry below: the worked-example twin was not
  a third open fix. Both master headers were narrowed on
  2026-09-07 to "only the provenance path differs", from run 3's
  first report of it; the diff I confirmed today is that line, by
  design. Run 3's copies still carry the byte-identical claim at
  their pin, so its TODO item stays open there until a re-pin.
  Two fixes were owed, not three.
- Nothing in concept/ moved: no CHANGELOG entry, no ADR, no
  concept version. Run 3 keeps its installed copies; a re-pin is
  its act, and the hand-back line for its Step 2 opening (TODO
  Now) is unchanged by this set.

- The fifth handoff fired on the user's word, drafted to
  temp/handbook-handoff-2026-09-10.md (2 asks, 1 report, 3 FYIs)
  from TODO's item (a)–(e): run 3's Step 1 report answers their
  decision 5 (the address is a layout preference, mechanically
  identical; we act on their root-vs-app reading) and reports the
  settings file rejected on their own withdrawal, the pace held by
  sentence plus local file; the asks are the copy-surviving forms
  (self-qualifying citations, exemplars by role, §8's born-without
  sentence) and the tiers model's §3 from five runs. One claim
  softened at the draft's check: the pace at every boundary is
  not verifiable from the run's records — every verdict the
  reviewer's is. The user delivers it into a handbook session.

Resume: the change-plan is closed (d12e26c). Run 3's Step 2 is
opened in the run, the user's way — nothing is drafted here for
it; a draft was written and refused. What this repo owes the run
is the one hand-back line in TODO's Now, carried over by the user
in whatever form they choose. Back here: the Step 2 boundary
reading when it closes. The fifth handoff is drafted; its reply is
read in through temp/ when it comes, then the draft goes.

## 2026-09-10  (run 3's Step 1 read: the gates reading at the Framing boundary; the four trials held)

- Run 3 closed Framing: 44 commits on step-1-framing from the
  gate to the change-plan's close, eight of them agent-scoped,
  none straddling; fast-forwarded to main by the user before this
  reading — the one bend in the protocol, ours, the reading was to
  come first. The framing: one promise (reserved never exceeds
  on-hand-count under contention), four possessions, six
  refusals, twenty kills, one area, four slices, SL-1 chosen-next;
  ADR-0002 adopts it; README re-derived last; the entry file's
  three false lines retired in one widened step.
- The gates reading, derived vs frozen v2, in TODO's experiment
  item: v2's four content items were a cache of cbc-framing and
  the briefing; two items derived that v2 never had (verdicts
  inline, no delegation entry; Release's framing-time decisions
  written in the exports — earned by reading forward into the
  vendored Release step); one miss that goes back as session
  input at the Step 2 opening (the middle steps confirmed against
  the framed problem); the sweeper moot under v4; the entry-file
  retirement done unasked, at the moment rather than the gate.
- The four trials held: branch cut before the first commit,
  fast-forward, main linear, no question asked; the entry file
  read at .claude/ (the plan names it by path, the guard held);
  the pace with no gate, the local file's text in no record;
  no handbook read this step. Three fold-back lines for the
  branch rule: the branch gate item can only be ticked in
  anticipation, since the merge follows the close commit; the
  rule says nothing about the merged branch, so step-1-framing
  still stands (deletion is safe, the user's act); two revision
  subjects at 54 characters.
- The run filed three hand-offs to the bundle, all three
  confirmed here and queued as one harvest change-plan: the
  registry template's opening line in agent voice, the export
  section's "growing" read as append, the worked-example twins
  differing in their provenance path. Its rule from the first —
  exports carry no agent language — is the fix's shape. Two
  change-plans lessons for the fifth handoff: a touch-ups-on-
  reading step named from the start; the step as a commit series.
- temp/briefing-run-3.md has served; deleted in the next commit.

Resume: delete the served briefing; then the harvest change-plan
for the three cbc-framing fixes; the hand-back line rides the
Step 2 opening prompt, which the user fires. The fifth handoff
fires on the user's word — five items now.

## 2026-09-09, later  (run 3's pre-briefing session read; the seed's address; the tiers model queued)

- Two user calls after the set closed, both landed: the seed's
  semi-pure step delivers the entry file at .claude/CLAUDE.md from
  the next birth (6672ca6 — a layout preference, mechanically
  identical either way, so no reading was worth waiting for); and
  the tiers model's §3 refinements queued for the fifth handoff
  (817e05b — the shape holds, the flows were written from zero
  runs).
- Run 3's pre-briefing session, read read-only. The kit reached it
  on the receipt branch kit-af16eb7 and the agent ran §8 under a
  change-plan, seven commits, project side before registration;
  the report on the branch is in TODO's fifth-handoff item (c).
  Two findings. The settings file was rejected in the plan, not
  trialed: the agent read the handbook's withdrawal and the pace
  already held by the operator's file, and refused the kit's born
  default before running under it — the ask-rule reading is dead
  in run 3, and the pace reading is now sentence plus local file,
  no gate. And the agent read the handbook checkout to get there:
  the stay-inside rule sat in the briefing's session section, not
  yet fired, and the run's own §8 names a checkout on disk as the
  handbook. The three-voices lesson, third time: a told rule
  exists only in the session it is told to. This repo was not
  read.
- The operator block for the kit update served once and nearly
  swept the run's untracked temp/ into the receipt; a kit-update
  install doc is now a TODO item. The pre-briefing draft is
  deleted in the next commit, served.

Resume: the briefing — a fresh run 3 session, step-1 cut from
main, temp/briefing-run-3.md pasted whole (its session section
carries the stay-inside rule), stop at the first boundary. Then
the Step 1 reading here: derived gate vs frozen v2, hand-backs
after the derivation is recorded, the trials' checks in TODO (the
branch cut before the step's first commit; the harness reading the
entry file at its new address; the pace holding with no gate). The
fifth handoff fires on the user's word — four items and the run 3
report are in.

## 2026-09-09  (session: the reply and the checkout handoff absorbed, kit @ af16eb7, entry file back at root)

- Two documents read in from the handbook: the reply to our 09-08
  handoff (b313498, grown through e5b762d, ebbde21, ac77216 as the
  handbook kept writing) and a new handoff from its checkout-system
  reading (2e05825). The reply: all three model asks taken (the
  pace rule now commit-messages' first rule of thumb; the
  permission prompt a named gate kind; the operator's file ambient
  with an owner), the kit now ships the settings file with the ask
  rule, the address move permitted and waiting on run 3, the local
  file's shipped shape refused for three reasons. Its finding: the
  loader drops every HTML comment from a memory file before it
  reaches the agent — confirmed here, this session's copy of the
  entry file arrived without its three comments. Later sections:
  the rules directory, the guard example dropped, the ask rule
  withdrawn at the handbook after eleven commits, and a 09-09
  reading that gives the address a meaning — root for a repo about
  the arrangement, .claude/ for an app repo. The handoff: eight
  playbook lessons that are the method's (all in frozen v2 already,
  by grep), the records table missing the method's three files, and
  the checkout run's delegated gates as evidence for run 3's trial.
- Run 3, read read-only before anything: it took only the branch
  rule of the four pre-briefing trials (d4e8cdd, 529d830, 34e00cf);
  no settings file, no local file, CLAUDE.md at root, kit still at
  c670fe5.
- The absorption, as a set. First the pinned copies, one commit
  before the plan (6dc8b23): four skills and the agent model to
  af16eb7, compare-first clean on all, and five findings in the
  registry entry — the chain wants agent-arrangement, the entry
  file's Conventions list, the installed drift, the pin lying since
  09-07 (c670fe5 absorbed through TODO, no entry — §8's own
  warning), and the handbook's ADR numbers colliding with ours. The
  user's question on the citations settled the reading rule: a
  number in a copy resolves at the source at the registry's hash,
  never against docs/adr/ here; the copies stay verbatim, the fix
  is the master's. Same for the playbook exemplar line, which
  names "a concept repo" to every born project and points nowhere.
  Then the plan (2ed87c1) and its steps: agent-arrangement injected
  by the installed path, the Conventions section gone, the entry
  file back at the root (8d08cfd — the 09-07 move undone on the
  handbook's reading; run 3, the app repo, keeps its trial); the
  stubs' changed comments carried project-side (5e2cb69), the two
  registry entries (b0bf648), the fills recomposed with one
  docs/system/ row in both templates (da4db7c — one row, the way
  the ADR row covers a directory, the user's call over three), and
  the pre-briefing prompt rewritten (4d45ce0): the kit update opens
  it, delivered on a receipt branch cut from the seed commit so its
  one commit against its parent is the kit at the two pins; the
  settings item goes, the local file and the move stay.
- Decided against, with reasons on record: a settings file here
  (the ask rule is run 3's trial; nothing under starter/ loads —
  the harness reads skills from .claude/skills/ only and memory
  from files named CLAUDE.md only, and starter/ has neither);
  patching citations or exemplars in copies; a project ADR (every
  decision is arrangement or applies theirs).
- The three drafts in temp/ — the 09-08 handoff, its reply, the
  09-09 handoff — are deleted in the next commit, served: their
  substance is in the registry entries, TODO's fifth-handoff item
  (§8 friction: citations, exemplars, the chain naming a
  convention a repo was born without; the run 3 update report
  pending), the gates-experiment item's evidence notes, and this
  entry.

Resume: fire temp/prebriefing-run-3.md — the operator steps above
its line first (the receipt branch kit-af16eb7 from 27db35e), then
the prompt in a run 3 session on main; then a fresh session on
step-1 with temp/briefing-run-3.md. Back here: read run 3's update
(the branch as compare, the entry-file comment carry, the settings
file's arrival), add its report to the fifth-handoff item, and the
Step 1 boundary reading — derived gate vs frozen v2, hand-backs
after the derivation is recorded, the trials' checks in TODO. The
fifth handoff fires on the user's word once the report is in.

## 2026-09-07/08  (session: run 3's Step 0 read, playbook v5, temp/ tracked, four trials for run 3)

- Run 3 (~/IdeaProjects/cbc-pure-run-3, seeded per ADR-0018 and
  ADR-0019: receipt branch of six, entry files delivered filled)
  closed Step 0 and waits on the briefing. The Step 0 reading,
  read-only, every gate item re-checked here:
  - Nine commits above hygiene on main, eight under a change-plan,
    reviewer-paced: plan, kit conventions, concept, records with
    Step 0's gate written in and still open, CbC skills with the
    registry entry, entry file last ("nothing it names may be
    missing when it lands"), close, close plan. The bundle's
    birth entry reconstructed from the seed subjects with pin,
    why, and rejected — fuller than run 2's.
  - Six gate items, all verifiable and all true at the close;
    against run 2's eight: adds the receipt diff and the
    commit-length rule, drops the placeholder and README-true
    items (delivered filled, nothing to check). Both cover frozen
    v2's three. The split held in every commit, unprompted —
    three runs of three.
  - The entry files: untouched, byte-identical to the fills. The
    change-plan says CLAUDE.md was read line by line and passes,
    README "unchanged, its paragraph already true" — read as its
    own to check, not as vendor text. The reading's object under
    ADR-0019 (what the agent edits in delivered entry files) is
    nothing, at Step 0.
  - Two findings the run filed for us: Release's (CbC) items
    carried checkout-system's exclusions; the worked-example twin
    note claimed byte-identical while the path lines differ.
  - One deviation: a ninth commit after the close reshaped the
    vendored Release step in place — outside the change-plan, a
    vendored step edited in the run rather than only filed — with
    a 56-char subject, breaking the run's own gate item six. Not
    a blocker; the reshape was right and is harvested below.
  - Run 3 also wrote a preamble line into PLAN — every step
    derives its gate at opening — a candidate for the playbook's
    own preamble; not taken this session.
- Playbook v5 (a08adfc): Release joins the derive-at-opening form
  from run 3's text — Goal line, the kit's three facts as "Known
  already", the exclusions re-decided per run. The step's
  kit-provenance comment went too, at the user's question: the
  pin lives in the header as for Steps 0 and 1 since v4, and no
  step ships a path the newborn cannot see. The starter README's
  "fixed endpoint" sentence followed.
- Twin note narrowed to identical-below-the-header, a harvest line
  in each (9527a9b); bodies verified identical.
- temp/ is tracked from today (d918991), user's call: drafts on
  their way somewhere — handoffs, replies, briefings being molded
  — so the shaping shows as diffs, deleted once served, never
  records; temp/README.md holds the rule and the no-citations
  rule for anything leaving for a run. The 2026-09-05 handbook
  reply, absorbed and asked deleted by its own header, was deleted
  rather than committed spent.
- The held briefing read against the pure setup: stale in three
  places — the birth-materials paragraph (concept/ not
  docs/concept/, a playbook file that no longer exists, a kit
  playbook the kit no longer ships), the closing "Bootstrap, Step
  0" line, and checkout-system named as lineage with no word on
  whether it may be read. Draft at temp/briefing-run-3.md: the
  paragraph gone, a "This session" close carrying the session
  truths (opens Framing, reviewer present, stay inside), the
  territory saying nothing of checkout-system is needed. Settled
  (258dfcb): the close carries session truths only — "derive the
  gate first" would spoil the gates reading, and nothing done here
  needs applying in run 3 (v5 came from its own PLAN text; the
  twin note is header-only; its Later items stay as written).
- The user asked why "This session" exists at all and whether the
  framing skill fires unprompted. Files can name the reviewer
  role; only the prompt can say the reviewer is here — and "no
  other repo is yours" is a fact about the machine, not the
  project. The skill has three signals (its trigger line, the
  entry file's pre-framing sentence, PLAN's Step 1); if it still
  misses, that is a finding, not a prompt defect.
- A branch per step, user's design: at the step grain, not the
  run (the receipt branch is already the run's restart point, and
  a repeat wants a fresh repo); fast-forward only, so the readings
  see linear history; the merge after the gate closes, on the
  reviewer's word; a restarted step keeps its old branch renamed.
  First drafted into the briefing's close, then pulled back out:
  a process rule riding the briefing is noise for what framing
  consumes, and the rule must be on main before Step 1 cuts its
  branch. Delivered instead as its own pre-briefing commit, on
  trial, TODO note here (5c1845b).
- The rule that would not hold — stage, show, commit on the word
  — traced to its channel: it lived only in change-plans §6, a
  pulled channel that single commits never open. Four channels
  ranked (harness permission → always-loaded text → triggered
  text → prompt); the rhythm is the user's, not the project's, so
  it went global: ~/.claude/settings.json ask rule on git commit
  plus ~/.claude/CLAUDE.md. Restored within the hour — the user
  wants it local, per project, and trialled in run 3 rather than
  set in the handbook.
- CLAUDE.md moved under .claude/ here (ebd1416, 6b2a81c): same
  channel, two addresses; 103 mentions in 26 files, three live —
  the rest are history and the run-facing starter text. The
  pinned split needed no edit; ".claude/" already covers it.
- CLAUDE.local.md, checked against the harness docs: defined by
  not being committed, root only, the init flow ignores it. The
  user's argument for tracking it (the agent split already
  isolates its commits; diffs would show) was good and was
  dropped anyway — trial 3 tests the native mechanism, and if the
  words prove to be project truth they move into the convention
  under an honest name. Kept ignored; the decisions entry in the
  run records that it exists.
- Pre-briefing prompt drafted (temp/prebriefing-run-3.md): four
  trials for run 3 before its briefing — the branch rule, a
  tracked .claude/settings.json with the ask rule, the ignored
  local file with the reviewer's pace, and (2026-09-08) the
  CLAUDE.md move. Each a decisions entry, one TODO Later item,
  agent-split commits. TODO's gates-experiment note carries what
  the Step 1 reading checks for each (bebd91b, b808225).
- 2026-09-08: handoff to the handbook drafted and committed
  (temp/handbook-handoff-2026-09-08.md, e5b99c8): the agent model
  applied to the pace rule — §8's own diagnostic, the fix its
  table names (pushed at commit time plus a gate), the harness
  permission as a gate with no machinery, an ownership note for
  ambient text; the handbook's own CLAUDE.md move; the stub's
  address; two starting templates. Says which asks can wait for
  run 3's Step 1 reading.
- Resume: three drafts in temp/ in order — the pre-briefing prompt
  into a run 3 session on main; then a fresh session on step-1
  with the briefing; the handoff into a handbook session any time.
  Run 3's Step 1 boundary is the next reading: derived gate vs
  frozen v2, hand-backs after the derivation is recorded, plus
  the four trials' checks in TODO. Each draft is deleted once
  served, logged here.

## 2026-09-07  (session: the receipt branch, then the semi-pure delivery)

- Second arc of the day, two change sets back to back, both
  reviewer-paced, no divergence in either.
- The user asked, before semi-pure: should the pure install also
  put its seed commits on a branch before the agent writes its
  change-plan? Yes, and the records said why better than tidiness
  did — the pure experiment names the commit sequence as its
  measured object, and a seed on main had already taken that
  choice away; run 2's straddling-seed known issue; newborn-v1's
  birth-seed as the lived precedent. ADR-0018 and six commits
  (1a6cdbe..fcc4d66): the seed commits on birth-seed, main stays
  at hygiene with the same files untracked, the prompt gains one
  line naming the branch. The restore-and-reset and the check
  command were proven on a scratch repo before the manual stated
  them. Closed the old variant A-vs-B item on the way: B's
  committed manifest and A's clean main, both.
- Then semi-pure. ADR-0016 had foreseen it in one clause — the
  parked template "may re-enter delivery if the pure runs show
  derivation inadequate" — and run 2's reading was that showing:
  two runs, same skills, neither produced the pre-framing guard
  or the skills' pin stance. ADR-0019 and six commits
  (2ca749b..6b63308): one optional step in pure-seed.md, both
  fills cut from the title line, name filled, written over the
  kit's stubs, one commit on the branch. The cut was proven
  against the real fills first — byte-identical from the title
  down, nothing leaking. The starter doc's contract paragraph
  now says why CLAUDE.md stays off the list even though the step
  writes over it: a fill assumes nothing of the stub.
- Judgment calls disclosed and standing: one manual with a
  switch, not two manuals (the difference is one commit, and one
  file keeps that structural); both entry files in one commit on
  the receipt branch, where the newborn's split rule does not
  govern; the manual keeps its name. The plan was staged before
  the ADR in both sets, the convention's order, as in the
  morning's set.
- What run 3 measures changes: not whether the agent derives the
  guard but what it edits in delivered entry files, and whether
  the guard holds through Framing. The does-it-invent-protections
  measurement ended with run 2 — two pure runs are its whole
  evidence, and neither invented it.
- Resume: seed run 3 per pure-seed.md with step 4 on — check the
  branch (six commits, main at hygiene, worktree equal to the
  tip), then fire the agent on main with the semi-pure
  parenthetical. The Step 0 reading of run 3 afterwards, here,
  read-only. Run 2 still waits on its briefing; its Framing
  boundary is the next gates reading.

## 2026-09-07  (session: "backend" kept, run 2 harvested, fills/)

- Opened on the open question from yesterday's Resume: where to
  fix "backend". Traced before deciding: the concept chapters and
  the kit never say it; three skill description lines do, and the
  practice skills' bodies are backend-born. So the word names the
  toolkit, not the problem — kept (4079880). The README template's
  "a system" reverted to match the CLAUDE template, its header
  saying made-and-reverted; a Later item holds the trigger, the
  first non-backend run. Lesson: the reading applied "nothing
  before the briefing names the problem" one level too strictly —
  a run may say what its skills can build.
- Then the templates against run 2's entry files. Opinion given:
  the templates are better for a stranger, run 2's tighter; the
  guard line no run has derived is the template's reason to
  exist. The user overturned the harvest rule with the right
  argument: a birth template is judged by what a run derived at
  birth, so it harvests at the Step 0 reading, not after a full
  run. Staged both templates recomposed; the user kept the old
  CLAUDE whole and took only run 2's opening line for the README
  (166bc7e; two fixes at the staging — trailing spaces, and the
  header claiming a sentence not taken).
- The semi-pure install came into view — the receipt branch from
  newborn-v1 (birth-seed: what arrived; main: how it was
  understood), the five deliveries plus one commit for the two
  templates, then the agent on main with the boot prompt. Four
  things named for its ADR: two variables change at once against
  run 2; it overturns pure-seed's "five commits on main, no other
  branch"; whether the firing prompt names the branch; the
  templates ship headless. Not decided — the user saw a
  prerequisite first.
- The prerequisite, user's finding: the templates do not travel
  as documents, they are written as contents into files the kit
  already put there. The playbook is the same act, and had been
  the copy table's "not copied as a file" all along. ADR-0017 and
  a six-commit change-plan (64151ac..c47055f): starter/fills/ for
  all three, bundle/ = pinned copies, installs/ = manuals; every
  live path swept, the starter doc's one table now two, codemap
  and CHANGELOG current, the three-way reading item's rule
  revised. No divergence; one finding — ADR-0010's structural
  sentence lived only in that ADR, nothing to rewrite elsewhere.
- Judgment call disclosed: the user said "stage the ADR first";
  the convention says the change-plan opens the set, so the plan
  was staged first and the ADR immediately after. Accepted at
  the boundary.
- Resume: the semi-pure install decision — ADR-0018 (receipt
  branch, the two fills written over the kit's stubs headless,
  the contract paragraph's "no non-additive act" reopened, the
  prompt's line about the branch) and a manual beside
  pure-seed.md; then seed run 3. Run 2 still waits on the
  briefing; its Framing boundary is the next gates reading.

## 2026-09-06  (session: run 2 seeded and fired; the Step 0 reading)

- Fifth arc of the day, logged late. Run 2 was seeded per
  pure-seed.md at ~/IdeaProjects/cbc-pure-run-2 (five commits,
  kit @ c670fe5, bundle @ 322dd43, v4 steps byte-true) and
  recorded in TODO (2aac876) but not here — that session closed
  without its entry. The user then fired it: its agent closed
  Step 0 in nine commits, reviewer-paced, and waits on the
  briefing.
- The Step 0 reading, read-only, both runs against the parked
  templates and frozen v2:
  - Nothing went wrong in either. Run 1 (v1, vendored gates)
    closed on the kit's three gates, unattended, and wrote an
    adoption ADR at birth. Run 2 (v4) derived an eight-item gate
    before working, took no ADR (deferred to framing's close),
    and held the commit split from a836439 on.
  - Gates: run 2's derivation covers v2's three and adds five,
    each traceable to a kit convention (skills registered with
    pins, records table resolving, TODO triaged, day-one devlog
    entry, the split checkable in the log). For Step 0 the
    vendored gates were a cache — the experiment's first data
    point. Framing's hand-back candidates stand unchanged.
  - "Backend", three of three: run 1 "a backend", run 2 "one
    backend" and "a backend", the parked CLAUDE template "a
    backend service" — only the README template was corrected to
    "a system". The watch item from the README-template session
    fired: the fix belongs upstream (concept or kit stub), not in
    shipped text. Open — where, not decided this session.
  - Entry files: both runs derived the nothing-to-build-yet line
    unaided; neither derived the pre-framing guard nor a Local
    rules section. Run 2 came out thinner than run 1: pin stance
    for the concept only, README without the start-at-00-cbc
    pointer (its own devlog: "written badly").
  - Run 2 reported three frictions about the bundle; two were
    real and are fixed (da86fdc): the stale slices.registry.md
    name in cbc-framing's header, the pinless skills seed commit.
    The third — the kit-remainder seed commit straddling agent
    and project paths — is pure-seed's `git add -A`, by design;
    noted, not changed.
- Resume: decide where "backend" is fixed; then deliver the
  briefing to run 2 — it opens Framing, and at that boundary the
  derived gate is compared against frozen v2's Step 1, with the
  cbc-framing mapping comment and the retire-entry-lines gate
  handed back if missed.

## 2026-09-06  (session: the README template, and a third shape named)

- Fourth arc of the day. Opened on the run-1 README, read
  against the kit stub it grew from (01147b1 → c3ffda8): the
  fill-comment honored exactly, the temporary paragraph
  exemplary (names its own end, Step 1 — the retirement rule's
  shape before the rule ever reached it), and one flaw — "a
  backend", the same pre-framing presumption the parked CLAUDE
  template carried. Data point worth watching: the seed shipped
  no template, yet the run re-derived the exact presumption the
  template held. If run 2 does it again, the fix belongs in the
  concept or the kit stub, not in shipped text.
- First answer on templating it was no — the kit stub IS the
  reusable template, the run's additions are the derivation. The
  user then named the real frame: a semi-pure install, a third
  birth shape between assembly (deleted) and pure, where the
  entry files ship filled and the rest stays pure. Under that
  frame the answer flips, and the CLAUDE template's parking is
  the precedent, not the objection.
- Composed and parked (c8f1be5):
  starter/bundle/readme-md-template.md, same apparatus as the
  CLAUDE template — kit half verbatim @ c670fe5, fills harvested
  consciously from run-1's derivation with the "backend"
  presumption corrected to "a system", provenance naming the
  harvest as a run's words taken on purpose (the semi-pure
  trade, explicit). Judgment call: TODO item, not ADR — no
  decision exists yet, the install is undesigned and may never
  be; the ADR moment is if it gets designed.
- The TODO item carries the kill-or-justify test: run 2's
  derived entry files vs the parked harvests — derivation
  keeps producing what the templates hold and the shape is
  never needed, or keeps missing something and that gap is the
  install's justification.
- Resume: unchanged — reseed for run 2 (delivers pure v4), or
  the skills reading; the semi-pure design waits on run-2
  evidence either way.

## 2026-09-06  (session: the strip goes whole-playbook — pure v4)

- Third arc of the day, opened on the user's question: why does
  the playbook still have gates, didn't we decide to derive them?
  Answer on record was decision one of the gates experiment — kit
  steps (0, 1, N) stay vendored whole, their gates being the
  kit's text, not our harvest. The user overturned it for steps 0
  and 1: "i want to make it pure" — Bootstrap and Framing lose
  their vendored kit gates and kit comments too, only Release
  stays as the fixed endpoint (bb7d970, playbook v4).
- Judgment calls disclosed and standing: Framing's briefing
  comment kept (channel-split wiring, garden-authored, not kit
  text — without it the newborn doesn't know where the briefing
  lands); Framing's skill pointer moved into the heading to match
  the middles; no new baseline, since frozen v2 already holds
  every stripped gate whole, kit text included.
- What v4 raises the stakes on: Framing's sweeper item and the
  two projection items now live only in frozen v2 — hand-back
  candidates at the Framing boundary if run 2's derivation misses
  them. And the reading gains a category: kit hygiene an agent
  re-derives unaided vs kit knowledge only the vendored text
  held. The TODO experiment item carries the dated note.
- Found at the staging's reference check: ARCHITECTURE's
  executions responsibility line still named the deleted parent
  playbook and birth scenario — the retirement change-plan's
  records walk fixed that section's birth-procedure sentences
  and the codemap but missed its opening line. Caught up as its
  own commit (e99f0c8).
- Resume: reseed for run 2 (pure-seed.md now delivers v4), or
  the skills reading — user's pick, unchanged.

## 2026-09-06  (session: the gates go derivable, the assembly path retires)

- Same session as the entry below, second arc — the experiments
  compounded and then took the decision they were circling.
- The pre-framing guard came back into the template (ea1f6b2), a
  second look at lineage: it is garden-authored (the withdrawn
  snippet's line), not a run's text, so the re-cut's rule never
  barred it — and the pure seed ships no template, so the
  derivation measurement never needed its absence. Lesson worth
  keeping: when stripping by origin, check each line's actual
  author before sweeping by era.
- The gates experiment (user's design, the template freeze's move
  one level deeper): variant frozen at v2 in baselines, re-cut
  provisional at v3 — middles keep name, skill pointer, goal;
  gates, records lines, and warnings stripped to
  derive-at-opening. Three decisions taken consciously: kit
  steps stay vendored whole; warnings stripped for purity (they
  are underivable paid-for facts — the boundary rhythm hands
  them back after each derivation); the newborn learns nothing
  of the frozen master. What it measures, plainly: which gates
  are a cache of the skills and which are playbook-only
  knowledge — the playbook's reason-to-exist, measured.
- Then the user asked "can we discard cbc-run-playbook.md?" and
  the honest answer surfaced the real question: is the assembly
  walk ever going to happen? It is not — ADR-0016, a full
  change-plan (47ad294..f1dfe1a, eight commits, one §5 revision,
  reviewer-paced at every boundary): pure adopted, assembly walk
  cancelled, four artifacts deleted (parent playbook, birth
  scenario, installs/cbc.md, birth-fills), the variant the only
  playbook carrying its own provenance, pure-seed.md the
  procedure of record, the template parked as the three-way
  reading's comparison object, the held briefing released to the
  pure path. The trial closed without its walk — the pure
  evidence answered the trial's question first.
- The one divergence, recorded not silent: the change-plan's
  records walk missed ARCHITECTURE (the shape change fires its
  moment) — caught by a post-sweep reference grep at a boundary,
  revision-committed. The convention's own failure mode, §3's
  "planned, not remembered", lived once more in miniature.
- DEAD END, cheap: staged a compression of the template's header
  (history to TODO) — user rolled it back; the comment stays
  where the editing happens. Second rollback of that shape;
  the pattern is now memory.
- Open: run 2 reseed (fresh pin, v3 steps, reviewer-paced
  prompt, then the gates readings per boundary); the skills are
  the last unread doc-by-doc comparison; the briefing fires in
  the pure-born run whenever the user chooses.
- Resume: reseed for run 2, or read the skills — user's pick.

## 2026-09-06  (session: the pure seed runs, the reading, the template re-cut)

- The pure-seed experiment, designed 09-05 through six recorded
  revisions (the manual's banner keeps them all): material-only
  seed, five commits on main with pins in the subjects, kit born
  per the handbook's pure.md by pointer, the playbook's steps
  into PLAN from a candidate variant (cbc-run-pure), no template,
  no scenario, no fills — the agent finishes the birth blind.
  Each revision converged on a repo principle already held:
  artifact over script filter, channel split (prompt carries the
  session, PLAN the project), briefing as Framing's starting
  input so Step 0 closes clean.
- Run 1 walked (user fired it, ~/IdeaProjects/cbc-pure-run): the
  newborn passed nearly everything. Change-plan fired unprompted,
  eight commits, sequence justified by where each decision lives
  — entrance doc FOURTH, after what it presumes. Commit split
  perfect. Bundle birth entry reconstructed from the seed
  subjects, citing the copy-entry binding, and it re-derived our
  blindness rule as its own rejected option. README stayed a
  front door. ADR-0002 landed Accepted via the marked case,
  argued correctly. THE FINDING: its derived CLAUDE.md is
  minimal — kit table plus orientation plus one pin stance, no
  stances, no guard. Walk-1 fat, template middle, pure run lean:
  derivation follows whatever rule text is present.
- The miss, and the best data of the run: change-plans §6
  (stop at every boundary) never fired. Not silently — the agent
  recorded the deviation and justified it by an instruction the
  prompt never gave ("instructed to finish unattended"): the
  harness's finish-the-task voice, heard as the user's. Named it
  the three-voices problem (harness > prompt > files; skills are
  files): forms travel as files, brakes need a stronger voice.
  Fix shipped: the prompt now establishes the reviewer and the
  staged-step pace (ab4bdf6). Fifth-handoff note accrued.
- Harvest from the reading: the run's promise-line and pin
  stance folded into the template (faa110f); the entry-file
  sweeper gate item into both playbooks — birth-scoped lines
  name their ends, the gates now sweep them (d4af956, variant
  v2, manual synced).
- Then the section-by-section template pass with the user, and
  it ended somewhere unplanned: the stance bullets traced to
  walk-1's derivation (they beat our snippet in the ADR-0014
  merge — a newborn wrote our shipped text), and the user called
  it: text earned under a different arrangement must not ride
  into the next run. Template frozen whole at
  docs/baselines/claude-md-template-v1.md (6ca9edc), live file
  re-cut with no past-run text (8e25977) — stance bullets and
  pre-framing guard out, the guard's exclusion accepted
  knowingly (brakes don't re-derive; the human backstops
  framing). Three-way reading protocol in TODO: next full run's
  derived CLAUDE.md vs template-v1 vs walk-1's baseline.
- The pass also caught the concept lying: "technology enters
  with the first slice" vs the lived ground-then-skeleton order.
  First content change to a concept chapter since import
  (211bd0f): technology arrives after framing, answerable to the
  registry — the inversion kept, the false timestamp dropped.
  A TODO-worthy footnote: the header-compression attempt (moving
  the template header's history to TODO) was rolled back by the
  user — the comment stays where the editing happens.
- Open: the doc-by-doc comparison paused (birth-scenario next,
  then the playbook verdict, then the skills); the variant vs
  parent call waits for trial close; run 2, if walked, uses the
  new reviewer-paced prompt.
- Resume: birth-scenario.md against run 1's eight-planned-commits
  — the three-commits/no-change-plan prescription now has a lived
  counterexample.

## 2026-09-05  (session: the reply lands, the template ships whole)

- The handbook answered the fourth handoff at scale: 41 commits,
  ADR-0031..0034, HEAD c670fe5. The ask taken further than asked —
  playbooks and the "or delete" marks left the kit (0031), then
  the empty sections ("guard without sections", 0032, a third
  shape neither side had proposed), then the Conventions list
  itself (0034, "the registry is the list"). Their entry file is
  ~41 lines of map and guard. The retro-fold disagreement settled
  our way (into the master); item 4a dissolved with the list; a
  new convention, agent-arrangement, now owns the entry-file
  rules. They also found a defect under ours: their own playbook
  copy command deleted the STEPS markers too.
- The reply reshaped the template-whole Now item rather than
  queueing behind it: one change-plan (ff518f7..5819506), six
  steps, no divergence. Our install sed keeps the markers now
  (tested twice in a scratch birth); ADR-0015 records the
  delivery change against ADR-0014; the kit steps re-vendored at
  c670fe5 (cbc-run.md v3, Framing's projection gate item); the
  compose landed claude-md-template.md — kit half diff-verified
  verbatim, method half unchanged from the fragments, the
  fragments file retired; scenario and README carry whole-copy
  and the three-surface contract paragraph narrowed to the real
  three (STEPS region, step/gate idiom, default.md as vendor
  base — CLAUDE.md off the list, as the handoff promised them).
- Two decisions rode in the plan, both held: the newborn holds no
  playbook copy — their ADR-0031's model applied to ourselves,
  steps in PLAN plus a "Steps from:" line, the concept copy
  deliberately kept (read throughout the run; the playbook, once
  mapped, is not) — and the temp/ staging file deleted
  uncommitted, both repos' reply list asking it.
- Found while re-vendoring, now accruing for a fifth handoff: the
  ADR-citation trap. Text copied into a newborn's PLAN carries
  bare citations that read as the newborn's OWN ADR numbers.
  Ours dropped from the (CbC) comment this set; their default.md
  v2 ships "(ADR-0031)" into every born PLAN — their line to
  draw, FYI-shaped.
- Resume: the next birth — assembly from the current masters, kit
  pinned at c670fe5, receipt branch of six, the held briefing
  (~/IdeaProjects/safe-reservation-briefing.md, still
  baseline-blind) as the first prompt after Step 0 closes. It is
  the trial's walk 2, and the trial-close ADR gates on it.

## 2026-09-04  (session: the stop, the fourth handoff drafted, sockets die)

- cbc-newborn stops before the briefing — the user's decision, no
  further work there; archived later for comparison. Its yield was
  already absorbed, so nothing is lost; the briefing survives
  unchanged for the next birth, which runs assembly and is the
  trial's walk 2. TODO retargeted (9915bac).
- The models observation dissolved on inspection: the handbook's
  model set is exactly agent.md + tiers.md and our pinned copies
  are byte-current with their HEAD (f9371e4). The kit-side fact
  (the kit ships no models) was queued as a handoff question and
  then DROPPED by the user — not asked; the fact stays in TODO.
- The fourth handoff drafted to temp/handbook-handoff-2026-09-04.md
  — staging only, deliberately NOT committed (user's call; the
  substance is on record in TODO and here, the file is a paste
  buffer). One ask: pure ships no waiting-slots — empty sections
  are slots waiting for content pure cannot know; a prepared stub
  built on pure owns its own slots; fills (name, intro) stay,
  waiting-slots go entirely. Plus the three pure.md defects, the
  two disagreement FYIs, the earlier rounds' backlog. Delivery is
  the user's act, as before.
- The big design turn, user's, mid-drafting: NO SOCKETS. The
  first draft asked the handbook to stabilize four CLAUDE.md stub
  slots (the contract widening ADR-0014 implied). Killed: the
  bundle will ship a complete CLAUDE.md template instead —
  composed once here from the kit-universal content (records
  table, conventions list) plus the CbC fragments, copied whole
  at birth. No merge into their file, no anchors assumed,
  CLAUDE.md never re-enters the contract; the widening request
  died before being sent. ADR-0014's substance stands (shipped
  text, merged once, no derivation) — only the delivery mechanism
  changes. The reshape is TODO's Now item (22abd6f): template
  file, contract paragraph back to two surfaces, scenario step 3
  reworded copy-not-merge, a short ADR note. Cost accepted:
  the template carries kit content and updates at re-pin — the
  architecture's normal staleness, traded for zero live
  dependence on their stub's shape.
- Resume: user delivers the handoff (then the staging file is
  deleted); the template-whole reshape next in this repo; then
  the next birth — assembly, receipt of six, same briefing.

## 2026-09-04  (session: the absorb set — assembly lands in the masters)

- The change-plan ran open to close in one sitting (1cc3707 →
  2a2e38b), user-reviewed at every boundary. Landed: the master
  scenario is the assembly text (48ce28b); ADR-0014 closes the
  ADR-0012 experiment — merged once, frozen, no per-birth
  derivation; the bundle ships claude-md-cbc.md (four slim
  fragments) and birth-fills.md (eight templates, the records
  mapping distributed into them); the masters the walk falsified
  are fixed (concept headers location-neutral, playbook comments
  on the docs/ layout and ADR-0014, copy table at the docs/
  destinations); CHANGELOG carries it under Unreleased, concept
  stays v1.
- The set's lesson, earned twice: lived is evidence, not master
  text. The first staged merge froze the newborn's derivation on
  the authority of "it won the comparison" — unaudited, it
  restated the concept, hardcoded step numbers, and imported
  facts whose homes are the skills (user caught it; plan revised
  fe0311f, redone slim). Then the README fill shipped the
  newborn's birth narration as the front door — same mode, one
  fragment, caught again at the boundary. Every adoption from a
  run gets audited against the target record's own rule.
- Standing state to know: until the trial-close rewrite, the
  install manual's hardcoded paths disagree with the copy table
  it defers to — the scenario is the only internally consistent
  birth procedure. Flagged inline on the copy table's playbook
  row; the rewrite plus the rebuild script remain the closing
  ADR's work, after the briefing.
- Parked in TODO for after the set, three user observations: the
  pure kit stub may carry too much (handbook-side, fourth
  handoff); this repo holds only two handbook models (agent.md,
  tiers.md) — is our arrangement shaped the handbook's way?; and
  record-audience boundaries (README vs CLAUDE.md vs internal
  records) may need a sharper guard, given the lesson above.
- Also owed to the handbook (TODO, fourth handoff): CLAUDE.md's
  stub slots re-entered our assumed-surface list (ADR-0014) —
  their contract rule wants the widening handbook-side first.
- DEAD END: none in this set; the step-3 rejection was a caught
  divergence, not a dead end — the plan's boundary did its job.
- Resume: the briefing is still the user's act in cbc-newborn,
  unchanged and blocked on nothing here. After it: the trial-close
  ADR (manual rewrite, rebuild script, scenario-copy fate, marker
  line, session-or-script) — and the next birth runs assembly
  from these masters, its receipt branch cut to six.

## 2026-09-04  (session: post-walk read — the scenario becomes assembly)

- Read cbc-newborn again: five commits on main past the pristine
  close (56352d1..2ea3e8a), birth-seed untouched, tree clean,
  Step 0 still standing closed as walked. The corrections came
  not as spoken notes but as lived commits with their own devlog
  entries — the previous entry's pending slot resolves to this
  reading.
- Layout (d7d2817): the bundle material moved under docs/
  (concept, playbook, scenario), the kit's two unused playbooks
  deleted. One commit deliberately crossing the agent/project
  split — their devlog owns it: a layout move splits into a
  dangling pointer either way.
- The big one (3b27b46): the newborn's scenario COPY rewritten as
  assembly. Verdict of the walk, per its rationale: the CLAUDE.md
  derivation needed the whole bundle in view and the concept read
  first — nothing more; the staged introduction lived only in the
  commit log, for a human reader. New shape: seed of six
  mechanical steps (now including the bundle's shipped CLAUDE.md
  text merged into the stub, and the stub fills as templates),
  then exactly three commits under the split (arrangement /
  bundle + records / Step 0 close) by the newborn's first session
  or a script, then the briefing. No per-birth derivation, no
  change-plan, no ladder (their DEAD END, drafted and discarded).
  Receipt branch survives, re-cut to six steps (260a39e). Our
  master at starter/bundle/birth-scenario.md is untouched — the
  freeze held; the carry is now ours to make, and the trial
  protocol's own post-walk revision step is the vehicle.
- Variant B is overtaken, not lost: assembly keeps A's clean main
  (the seed commits nothing on the newborn's line) but prescribes
  the three commits and allows a script to make them — the A-vs-B
  question dissolves into "session or script," parked with the
  rebuild script at trial close.
- The rewrite asserts ADR-0012's close: the two CLAUDE.md
  candidates (the walk's derivation, the blind snippet baseline)
  compared once, merged, frozen into the bundle as shipped text —
  the derivation was a one-time review of the concept's clarity,
  not a birth step, and it does not repeat. The evidence is
  complete (both candidates exist and will not change); the ADR
  is ours to write, here.
- Carry-list received (their devlog, "Carry to the source repo"):
  the scenario revision; the CLAUDE.md merge + freeze; the birth
  fills as bundle files (drafts: e7a13f9 for the stubs, CLAUDE.md
  as of aa1e17e); the rebuild script (trial close); pin findings —
  cbc-run.md's Step 0 comment still says concept/, the concept
  chapters' headers call each copy authoritative (false in a
  newborn), the kit PLAN stub and cbc-run's header disagree on
  where retro lessons fold; handbook finding — the kit's Step 0
  comment disagrees with the assembly shape on three points
  ("take the briefing", "draft CHANGE-PLAN.md", "plan open
  first"). Findings routed to TODO.
- Resume: on the user's word — carry the assembly rewrite into
  the master scenario, then the CLAUDE.md comparison/merge with
  the ADR-0012-close ADR and the birth-fill templates. The
  briefing stays the user's act and does not wait on any of it:
  the newborn's copy is already the revised text.

## 2026-09-03  (session: walk 1 read — the first phase-close reading)

- The walk closed same-day it was seeded. Twelve commits over the
  hygiene root, tree clean, pristine close at cbc-newborn
  @ 56352d1. The log-as-introduction bet paid: read top-down it is
  an introduction — change-plan open → kit arrangement → scenario
  → concept → derive (CLAUDE.md, then stub fills) → map → skills
  in three groups → Step 0 close → change-plan close. The kit's
  Step 0 was met entirely inside the walk, via its own
  change-plan, exactly the step-is-interface relation the
  scenario claims.
- Checklist (install manual's checkable birth): copies all
  byte-identical to the masters at the pin — no bundle file
  edited; both birth entries in; CLAUDE.md's CbC section the
  newborn's own; commit scoping clean throughout (agent files
  never mixed with records); birth-scenario.md kept at root (an
  open point, now answered by the walk: kept). One item fails
  literally: the STEPS markers are still in PLAN — the newborn
  filled the region in place, which the kit marker's own text
  sanctions while our checklist says "no marker left." The two
  documents disagree with each other; the newborn obeyed the
  marker. Ours for the trial close, theirs for the fourth
  handoff. Kept markers also keep the region re-runnable — the
  friendlier outcome.
- The walk reordered the draft, defensibly: the draft says
  Concept first, but the newborn had to introduce the commit
  conventions before it could make any convention-governed
  commit — the draft's order ignores its own bootstrap
  dependency. Arrangement-first is the fix the draft revision
  takes.
- The snippet comparison ran (the derivation is committed, so
  reading it contaminates nothing; the verdict stays with the
  trial-close ADR). The derivation re-derived the snippet's
  standing guards in its own words (erosion, escape-hatch,
  wall-to-test drift — all inside "watch for the rot" and
  "prefer the wall over the test"), and its pre-stack discipline
  is stronger than the snippet's. It missed two things: the
  human sign-off gates (Stage 1/2, framing verdicts — though
  those live in the skills, so ADR-0013's moment-of-need logic
  cuts the other way), and the docs/system/ framing-artifact
  home with registry-as-source-of-truth (an every-session fact,
  weaker excuse). Novel and best: the records-carry-the-method
  mapping (README = promise, Invariants = guarantee inventory,
  ADRs = refusals, PLAN cut by invariant) — the snippet predates
  the kit and never had it. Emerging shape: merge — but decided
  at trial close, and the misses are harvest questions (concept/
  or skills?), not snippet edits.
- The derivation captured to docs/baselines/
  cbc-derived-claude-walk1.md — trial evidence, not a master,
  blind to future newborns like the snippet (imitation is not
  legibility). NOT a snippet v2: if derivation wins the ADR-0012
  question there is no snippet to version — improvements flow to
  concept/ and the skills, and convergence between independent
  derivations is the metric.
- User observations from the review stops: arrived as commits and
  devlog entries in the newborn, not as notes — read in the
  2026-09-04 entry above.
- Resume: user edits the newborn next — ordinary commits, never
  amends, so 56352d1..HEAD stays the correction list (trial data:
  what the walk got wrong by the watcher's judgment). Then the
  briefing, unchanged, as the first project prompt — brings the
  name safe-reservations; old path already clear. Draft revision
  (arrangement-first + the marker line) after the trial's
  readings, trial-close ADR after the briefing settles in.

## 2026-09-03  (session: the seed — cbc-newborn born)

- The seed ran step by step with a review stop at each boundary,
  under the birth scenario's ordering (trial): audit, kit copy,
  hygiene commit, bundle copy, birth entries — stop. cbc-newborn
  exists at exactly one commit (048c15c, hygiene base) plus a
  deliberately dirty tree: "nothing is committed; the walk
  commits it in order." All eight bundle rows verified
  byte-identical to the masters; kit pin filled @ f9371e4; both
  birth entries in .claude/decisions.md (the kit's names six
  conventions — the absorption's prediction lived; the bundle's
  @ 250bbcf, pinned to concept v1). The install manual's second
  lived test, and the scenario seed's first.
- The audit (pure.md step 0) found one bug, ours: starter/README
  counted two template carriers, but cbc-framing's registry
  master (2026-08-29) makes three — fixed before anything copied
  (250bbcf), the fix-upstream-first rule lived. Handbook side
  clean: HEAD still f9371e4 — the state today's absorption
  already verified — and both contract surfaces hold (playbooks/
  with default.md; the STEPS marker region).
- Three manual findings for the fourth handoff, handbook-side,
  none blocking: pure.md's copy block assumes the target dir
  exists but no step creates it (mkdir -p needed first); "seven
  of the kit's seventeen files" is stale — the kit holds 18; and
  the install block fills <handbook-commit> but not the birth
  entry's <YYYY-MM-DD> date — filled by hand here, per cbc.md's
  "mechanical, done at copy time" spirit.
- Noticed in passing: the old ~/IdeaProjects/safe-reservations is
  already gone, so the rename-time precondition is met early.
- The user wanted the seed inspectable in git — per-step diffs,
  deletable — without polluting main's log (the walk's
  introduction). Built as a receipt branch in the newborn:
  birth-seed, from the hygiene root, five commits (kit remainder
  → concept/ → skills → playbook+scenario → birth entries), never
  merged; main's worktree restored to the same content untracked,
  verified file-by-file. Delete anytime, or keep as the birth's
  receipt. Trial evidence for the rebuild-script question: the
  desire to see the seed as commits is an argument the trial-close
  ADR should hear.
- Second trial datum from the user: the instinct to delete the
  kit's playbooks (default.md, backend-service.md) once cbc-run.md
  lands — the born project holds two playbooks it will never use.
  Held, not done: ADR-0011 and their closed overlap item say the
  two coexist, and no kit file changes at copy. The walk may do it
  as the newborn's own recorded decision; otherwise it waits for
  the trial-close ADR.
- Two more trial datums from the user, post-seed. First: reading
  the lived birth, they independently re-derived the scenario's
  seed/walk/briefing split (outside-mechanical, inside-derived,
  handover at the problem) — confirmation the ordering is natural,
  not just written; the boundary is who commits, and the halves
  now mirror the repo's two histories (birth-seed branch = what
  arrived, main's log = how it was understood) — candidate
  vocabulary for the rewritten manual. Second, on the
  rebuild-script question: leaning against a script — the walked
  seed's value was the checking (the audit caught a real bug, the
  review stops caught manual gaps); a script would replay the copy
  but not the verification. Both decided at the trial-close ADR,
  not now.
- Resume: the walk — a FRESH agent session inside
  ~/IdeaProjects/cbc-newborn (never this repo's sessions: they
  know the withheld baseline) reads birth-scenario.md at the
  newborn's root and walks Concept → Derive → Map → Skills →
  Records. This repo watches at phase closes and records
  divergences here (trial protocol). Briefing last, unchanged,
  brings the name safe-reservations.

## 2026-09-03  (session: third reply absorbed, arrangement current)

- The reply came back same-day, everything adopted or answered:
  our friction log is now their convention-lifecycle §8
  (ADR-0030), the naming collision resolved their side —
  installs/default.md is installs/handbook.md (ADR-0029), manuals
  named by bundle, the playbook keeps default — the mirror noted,
  the gate wording deferred with candidate text ready. Handbook
  moved 65dd7ee → f9371e4; the kit's playbooks/ verifiably did not
  move, so our vendored pins stay honest untouched.
- The absorption ran §8 three times in one set, each a first: the
  sixth convention injected by the procedure our own friction
  built (convention-lifecycle, first run of written §8); the
  chain-currency check caught artifact-kinds one line stale —
  their reply's missed-check lesson, lived the same day it
  arrived; and the first installed-path update anywhere ran on
  project-recording — compare kit stub to kit stub, one comment
  carried (the README projection rule), CHANGELOG already
  specialized past its generalization, PLAN drift birth-shape
  only. The registry now pins all three at f9371e4.
- Fresh field data queued for the fourth handoff (no trigger
  set): the placeholder-line anchor can be legally deleted so §8's
  row-position rule needs a fallback — and disagrees with the kit
  stub's own seating; the installed compare wants a per-convention
  stub manifest; a healthy reply loop makes the update mostly
  verification — the pin is the product.
- One plan revision, fired as reserved: the provisional installed-
  update step split when the compare surfaced its one carry —
  planned refinement, the §5 road walked for the first time here.
- Resume: seed cbc-newborn — installs/cbc.md steps 1–4 from here
  (mechanical; stop before anything derivational), kit read
  @ f9371e4, newborn holds six conventions; then the walk goes to
  a fresh session in the newborn (this repo's sessions know the
  withheld baseline); briefing last, unchanged, brings the name
  safe-reservations. Both temp/ copies deleted at this set's
  close.

## 2026-09-03  (session: moment-of-need set — README direction homed)

- The bundle-side work's second half landed (ADR-0013, the set's
  Proposed ADR, flipped Accepted at this close): the direction the
  handbook's stub slimming orphaned — which step makes
  Prerequisites/Run/Test true, and their shape — now lives in the
  skills. infra-establish's step 7 projects Prerequisites when the
  ground stands; cbc-bootstrap's Stage 5 projects Run/Test (and
  the stack's Prerequisites line) when the harness is real. Both
  skeletons extracted from checkout-system's lived README as
  template fragments (ADR-0008 machinery) — the lived file itself
  forced the honest split: its JDK line is stack, not ground, so
  no single skill could own the whole section.
- The user's consultation shaped the set before it opened: does
  CLAUDE.md deserve the same treatment? Answer argued and taken:
  no — its parallel mid-run moments are real (stack fact at
  bootstrap, ground-up rule at establish) but un-orphaned (the
  stub's comments teach its own fills), and pre-empting them would
  contaminate the ADR-0012 derivation experiment one set after we
  built it. Boundary stated in the ADR; watch item in TODO — the
  re-birth's phase closes observe whether the newborn catches
  those moments unprompted.
- Playbook untouched, deliberately: gate items for README sections
  would be the mandatory-doc-step-per-gate pattern the adopted
  rule refuses, and the middles change by harvest (ADR-0011),
  which adoption is not.
- Two queued triggers fired at this close: the handbook handoff
  (four items, TODO Now) and the re-birth are both unblocked.
- The third handoff delivered same-session, the temp/-to-temp/
  channel as before: friction log, naming ask, mirror FYI, gate
  wording — opened with "nothing blocks us" so the reply can be at
  their leisure, closed with the no-action context block (three
  ADRs, contract at two assumptions and zero touches, re-birth
  next).
- Re-birth path decided with the user: born as cbc-newborn, a
  placeholder — the pre-briefing walk is problem-agnostic, so the
  placeholder keeps Derive problem-blind; the briefing brings the
  name and the rename sweep (kit-sanctioned). Also stated as
  protocol: the walk must be a fresh session in the newborn — this
  repo's sessions have read the withheld baseline, so a derivation
  done here would measure memory, not concept/'s legibility. The
  seed alone may run from here (mechanical, precedent 2026-08-30).
- Resume: seed waits on the handbook reply at the user's call —
  the reply may move the kit under us (the naming ask touches
  files the seed copies and our playbook pins), and the first
  birth died of exactly that. When the reply lands: absorb it,
  refresh pins if it moved anything, then seed cbc-newborn
  (installs/cbc.md steps 1–4, stop before anything derivational);
  the walk goes to a fresh session in the newborn; briefing last,
  unchanged, brings the name safe-reservations. Three experiments
  ride the run (walked birth, derived arrangement vs the blind
  snippet baseline, blind replication vs v1), trial readings at
  phase closes, the CLAUDE.md watch item among them. Both temp/
  copies die when the reply is absorbed.

## 2026-09-02  (session: snippet withdrawn, birth derives)

- Same day, second set, from the user's redesign of the birth:
  cbc-startup-snippet.md leaves the bundle (ADR-0012, the set's
  Proposed ADR, flipped Accepted at this close). It was the
  bundle's last theory-only artifact — written in the archive
  before any birth, never checked against a run. Now held blind at
  docs/baselines/; the newborn derives its own CLAUDE.md section,
  README purpose, and stub fills after reading concept/ first, and
  the first walked birth's derived section is compared against the
  baseline at trial close — stay, retire, or merge, on evidence.
  Withdrawal is unconditional: manual and scenario both derive
  (two procedures of record must not disagree about what a birth
  is). The overlay contract dropped to two kit assumptions and
  zero kit-file touches.
- The scenario reordered around it (the user's order, marked
  provisional): Concept → Derive → Map → Skills → Records,
  briefing last unchanged. The playbook sed placed in Map — a
  read introduction over a silent seed fact — first walk decides.
  The known risk, stated in the ADR: the derived arrangement may
  miss the snippet's human-gates and standing guards and the run
  pays live; that outcome is itself the answer, and attribution
  between the two experiments riding one run (walked birth,
  derived arrangement) is argued in the devlog at the boundary
  where a divergence is seen.
- Also this set: the user's rebuild-script idea recorded on the
  prebuilt-stub TODO item — a script replaying the seed fresh
  from the two pins kills the staleness objection; how much of a
  birth becomes script is the trial-close ADR's question now.
- Resume: unchanged queue otherwise — the moment-of-need set
  (skills' README/Run-Test steps, adopted wording only), then the
  re-birth walks the scenario (now: derive experiment included,
  baseline blind), trial readings at phase closes; the handoff
  (four items) rides after the moment-of-need set closes.

## 2026-09-02  (session: cbc-run playbook rebuilt full-sequence)

- The bundle-side work split at the user's "lets do now playbook":
  this set is the playbook half alone (ADR-0011, the set's
  Proposed ADR, flipped Accepted at this close); the moment-of-need
  half stays queued as its own set. Ownership per step: Bootstrap,
  Framing, Release vendored from the kit's playbooks/default.md
  @ 65dd7ee, refreshed against the pin and never weakened; the
  middles are ours, changed only by harvest. cbc-run-playbook.md
  is v2, a full sequence, (CbC)-marked additions only; the old
  Release-additions section dissolved into the vendored Step N.
- En route: playbooks/TEMPLATE.md (pre-redesign generation,
  unpinned since the birth commit) replaced by a pinned copy of
  the kit base, same name as its master — the user asked whether
  to rename; kept default.md because a pinned copy keeps its
  master's name, and the naming collision resolves upstream via
  the queued handoff item.
- The real find of the set, from reading the composition
  end-to-end while planning: the STEPS-region sed lives in the
  handbook's installs/default.md — the manual ours *replaces* — 
  and pure.md ends with a stepless plan, so a CbC birth had no
  step that put the playbook into PLAN.md at all. installs/cbc.md
  now carries the block itself (new step 3, cbc-run hardcoded),
  Framing became confirm-not-copy, checklist and README row
  updated. Constraint worth remembering: the sed takes first
  "## Step" to EOF, so the playbook master must end at Step N.
- At review: all paths in the stay-home docs made repo-rooted
  (user: no relative paths). New handoff item 4 (cosmetic): the
  kit Framing gate's "born on this bare default" clause vendors
  off-context into typed playbooks.
- Resume: the moment-of-need set (infra-establish README step,
  cbc-bootstrap Run/Test step, skeletons as template fragments,
  adopted wording only), then the re-birth; the handoff (now four
  items) rides after the moment-of-need set closes.

## 2026-09-01  (session: bundle gathered under starter/)

- Same day, second set: the delivery layout now mirrors the
  handbook's starter shape (ADR-0010, the set's Proposed ADR,
  flipped Accepted at this close). starter/README.md describes and
  maps, starter/installs/cbc.md is the birth manual — peer of
  their installs/default.md, now also pointing the kit half at
  pure.md — and starter/bundle/ ships whole: five skills, snippet,
  playbook, birth-scenario.md (which joined the copy table it was
  only implicitly in). concept/ stays at the root and ships from
  there: the copy rule is two wholesale directories, and the
  file-level ambiguity ADR-0016 guards against never existed in
  concept/. executions/ is gone; historical records keep the old
  paths, the ADR carries the mapping.
- The fork that got us here: evict (delivery/ beside untouched
  content dirs — cheapest, my recommendation) vs gather (the
  mirror). User chose the mirror for the two-repo birth visit's
  legibility; the full gather (method/ absorbing concept/) and
  the concept/-inside-bundle variant were rejected on identity
  and redundancy grounds. The 2026-08-30 boundary-asymmetry TODO
  item closed resolved — by the symmetry argument, not its
  predicted trigger.
- The naming hazard from the handbook exchange bit here
  immediately: our own contract paragraph cites "the handbook's
  starter/README.md" one line above our own starter/README.md —
  the same-name collision now exists across tiers, more fuel for
  the queued default.md naming handoff item.
- Resume: unchanged queue — the bundle-side set (playbook rebuilt
  full-sequence on playbooks/default.md's base in its new home,
  moment-of-need README steps, the vendored-endpoints Proposed
  ADR), then the re-birth; the handoff (now three items) rides
  after that set closes.

## 2026-09-01  (session: handbook reply absorbed, convention injected)

- The 2026-08-31 handoff came back adopted on both asks (their
  ADR-0025/0026). Projection rule into project-recording as
  proposed — gate items where relevant, README row in the records
  table. The stub rule reworded, and rightly: our
  fillable-at-birth form overshot at truthfully-empty sections
  (How-to-work-here); the adopted form is container stays,
  direction goes. Stubs slimmed, both self-deletion hedges dead,
  CHANGELOG stub fixed en route (our 08-30 item 5 — its trigger,
  the next non-app birth, is our waiting re-birth). Plain-app
  destination for the dropped sections: their seed playbook's
  Skeleton & CI gate — our overlay-applied-inward suggestion,
  taken.
- First live convention injection ever (their return item 11; the
  procedure deliberately unwritten, our friction the field data
  they want back): change-plans overwritten from the handbook
  @ 65dd7ee — rolling commit lists, material-first order, records
  steps planned by walking the records table, in-set ADRs
  Proposed by default — injection entry in decisions.md, README
  row into CLAUDE.md. Friction notes gathered in TODO's handoff
  item. This absorption set was then the first planned under the
  injected rules; the records walk ran at drafting and cleared
  ARCHITECTURE deliberately (shape unchanged, coarse component
  row covers new files).
- default.md ambiguity caught by the user before it bit: two
  same-named starter files meaning opposites — installs/ (the
  handbook's own direction, replaced by our bundle manual in
  composition, never a dependency) vs kit/playbooks/ (the bare
  sequence, our rebuild base). Naming collision queued for the
  next handoff with the reply's own bare-name usage as evidence.
- The playbook independence question argued and settled: the
  rebuilt cbc-run is complete and self-contained — nothing
  references the handbook at use time; the kit endpoint steps it
  carries are vendored with provenance and pin (drift checkable
  against a named commit, harvest routing instant, updates flow
  the handoff channel), specialized never weakened. Declaring
  them fully ours would not cut the coupling — the gates are kit
  facts — only untrack it. Formal decision: the bundle-side
  set's Proposed ADR.
- Their ADR-0028 moved our ground mid-plan: birth docs re-aimed
  at starter/installs/pure.md; the overlay contract's third
  assumption now concrete (STEPS-marker region +
  playbooks/default.md); playbooks hold full sequences copied
  whole at birth, Framing confirms not authors — cbc-run must be
  rebuilt, and the parked playbook-overlap question likely
  dissolves (one playbook chosen at birth).
- Resume: the bundle-side set — reintroduction plus playbook
  rebuild, first set to exercise the new convention's
  Proposed-ADR and provisional-tail machinery — then the
  re-birth: slim kit, new starter, scenario walk, same briefing.
  The next handoff rides when that set closes.

## 2026-08-31  (session: birth-scenario pivot, safe-reservations stopped)

- The birth design changed out from under the newborn:
  safe-reservations (born 2026-08-30, zero project commits) stopped
  and discarded rather than walked under a procedure being replaced.
  Kept: the baseline-blind briefing, the blind-replication protocol
  (TODO Now), the archived v1 baseline. The re-birth takes the same
  briefing — the same problem through the new birth makes the
  scenario's first walk a fair test.
- The pivot: birth as an ordered introduction, not a file operation.
  executions/birth-scenario.md drafted provisional — seed by pointer
  to the handbook manual (no restated steps), a newborn-walked
  introduction (boot → concept → map → records; the log read
  top-down is the introduction) meeting the kit's Step 0 gates the
  way cbc-framing meets Framing's, briefing last and outside.
  Rejected in discussion: a prebuilt stub now (a cache of the
  scenario's output — parked in TODO behind "births come faster
  than harvests"; the ADR-0009 objection weakens when the stub is
  derived by a written scenario, but the staleness cost stands
  while harvests are weekly); scenario-as-skill first (a
  provisional skill automates speculation — the walker distills
  after walks); paste-delivery (prompts don't persist; the scenario
  copies to the newborn's root, birth-in-flight visible from a
  clean clone); editing the handbook manual from here (wrong tier;
  pointer only).
- Deliberately untouched until the trial closes:
  cbc-startup-snippet.md, the Birth section's body (one in-trial
  paragraph added), the cbc-run playbook (different job — the run's
  map, not the birth). The trial closes with an adopt-or-kill ADR,
  which also decides the snippet question.
- A second front opened mid-session, from the user noticing the kit
  stub is not basic enough: Prerequisites/Run/Test are direction,
  not container — delete-after-birth baked into the stub, its own
  fill-comment hedging ("Framing decides", ADR-0024). The split
  that untangled it: the when is convention-tier (README as a
  projection record in project-recording — touched when something
  became true the outside should see; gate items where relevant,
  no mandatory doc step per gate), the what is method-tier
  (walkthrough steps plus template fragments in infra-establish /
  cbc-bootstrap, existing ADR-0008 machinery — no new mechanism
  needed anywhere). Handoff prepped in TODO Now, two items
  composing; bundle-side reintroduction parked in Next until the
  reply.
- Resume: deliver the handoff to the handbook (user-side, under its
  records); after the reply, the bundle-side reintroduction set;
  then the re-birth — slim kit, scenario walk, same briefing.

## 2026-08-30  (session: handoff loop ran, first birth prelude walked)

- The first upward handoff went to the handbook and came back
  answered same-day: TEMPLATE.md fixed at its root
  (project-recording §9 itself still taught copy-whole), Step 0
  middle commit order freed, our three-assumption surface adopted
  as a named contract in the starter manual (two-sided: they state
  what may be assumed, we state what we assume). Absorbed here in
  dc925cc/e90a5ae; the ledger's four feedback entries graduated —
  its first graduation, ahead of the retrospective under the
  fold-back-at-gate-closes practice. Two items came back for our
  backlog: playbook overlap at birth, walker composition.
- The next run decided: safe-reservations, again — a second run at
  the same territory under the standardized arrangement. Old run
  renamed/archived as safe-reservations-v1 (GitHub rename frees
  the name; archive alone does not). Key design call: blind
  replication — the run's briefing deliberately omits the baseline
  so the derivation cannot steer by it; comparison is concept-side
  work at phase closes, deltas recorded here, run 1's held
  insights judged at those readings (b16e86e). The briefing also
  dropped the idempotent-orders mention — the user counts that run
  incomplete and may redo it (if so, third birth: the walker
  skill's candidate first outing).
- Birth prelude walked for the first time, both manuals in
  sequence: kit copy, pin filled (@ e3e45bd, the post-triage
  handbook), marker stripped, hygiene commit 04805d5; bundle
  overlaid — concept/, five skills, playbook to
  playbooks/cbc-run.md, snippet merged into CLAUDE.md with its pin
  comment (title and merge-instruction lines dropped, copy
  deleted). No trap hit; the manuals composed as written. The
  two-playbooks decision (backend-service.md beside cbc-run.md)
  rides into the run's Framing, flagged in the first-session
  prompt.
- Resume: the run's first session takes the briefing and runs
  Step 0 (its own territory). This repo's next work is the phase-
  close comparison readings, the two-playbooks outcome (note on
  both sides), and the walker skill once the walk finishes.

## 2026-08-30  (session: birth delivery decided, playbook harvested)

- The delivery question answered: how CbC reaches a run repo. Two
  births compose — the handbook kit supplies the container, this
  repo's bundle overlays the method (ADR-0009; 1b2dd56 plan →
  ef87a8a ADR → 832809c playbook → 9c813ee manual → f78416f TODO).
  Rejected at the ADR: a pre-baked stub here (second master of
  every kit file — yesterday's projection law applied to the kit,
  plus a sync burden with no mechanism) and delivery-as-edit-
  instructions (the kit's playbooks/ slot already is that
  mechanism). The overlay's coupling is a named surface of three
  assumptions in the birth manual — CLAUDE.md append, playbooks/,
  the step/gate idiom — with the rule that nothing off the list
  may be depended on; a handbook update is a list check, not
  archaeology. Record layering stated the same way: kit owns the
  record system, CbC events are ordinary project events, method
  artifacts live beside the records under docs/system/.
- cbc-run playbook harvested, not authored: Ground / Bootstrap /
  Slices / Release from checkout-system's retro-folded
  backend-service.md v1 in its own wording, warnings intact; the
  Define step (name under a rule, repo name, remote description,
  verdicts) from safe-reservations log Entry 0001. The merged
  sequence is this repo's judgment — the header says which run
  contributed what. Slice waves deliberately not steps: ordering
  stays registry-driven.
- One divergence, revised first-class (649abce): the plan assumed
  the kit TEMPLATE.md's copy-whole-to-PLAN usage; the lived kit is
  middle-steps-only (Bootstrap/Framing/Release in the stub,
  checkout's ADR-0024). The playbook and manual follow the lived
  shape. The kit's own TEMPLATE.md still carries the older usage —
  the handbook's inconsistency, not ours to fix from here.
- Considered and declined: the bundle overriding the stub's Framing
  step. checkout lived framing under the generic gates with zero
  friction — they are the interface, cbc-framing is how they're
  met. The overlay-marker idea (hygiene-files pattern, applied to
  the PLAN stub) parked in TODO with a trigger instead.
- Runs read-only throughout (ADR-0007). User's stated posture for
  what's next: stop overthinking, birth a run, redo what surprises.
- Resume: the birth manual is untested — the next run repo birth is
  its first walk (and the Define step's first kit-born walk).
  Nearest parked items unchanged: two-tier harvest (ADR-0007
  amendment), define-phase skill half, the overlay-marker handbook
  suggestion. Step N: Release still open in PLAN.

## 2026-08-30  (session: doc projection checked, layout re-derived)

- The queued doc-projection check ran, on two versions of the
  material: the safe-reservations node's originals (close/ and
  knowledge/realization/) and the user's latest copies staged in
  temp/. Substantively identical — the newer pair is the rename
  after their masters adopted it, which reads as the law surviving
  review, not changing. The idea in our words: a run repo's README
  (and any later public doc) is derived from internal truth, never
  authored on its own — an independently patched surface is a
  second master, and two masters diverge; refresh is event-driven
  at milestones, growth is by demonstrated substance.
- Harvested the lived core only (3a463e7 plan → 5e88c09 layout →
  3cd695b projection → 5695004 TODO): the derivation table, the
  thin-README-only default at framing close, milestone refresh,
  the residue filter extended to the surface, README last in the
  derivation-order commit story. Refused as unlived: the model's
  plane directories (internal/, public/), the docs-practice
  setting apparatus, per-milestone guides. Evidence the core is
  natural: safe-reservations walked it; checkout's auto run
  converged on nearly the same README shape with no law at all.
- The check knocked over the week's layout decision. The user
  pushed on root placement; on inspection it was an auto run's
  default, never a verdict, and the derivation doc's placement was
  unlived entirely. Re-derived: exports to docs/system/ as
  intent.md, definition.md, registry.md; derivation record nested
  at docs/system/framing/ (plain-named appendix sweeps beside it).
  One directory now does what three name-prefixes were doing — the
  dotted exports and the framing- appendix prefix dissolved, the
  grandfathered-names TODO deleted as moot. The ripple was wider
  than that TODO predicted: cbc-slice's trigger and R1, the
  readiness checklist, the startup snippet, and infra-establish
  all named the old paths — one commit by the revert test.
- checkout-system stays untouched (ADR-0007), its root-level
  dotted exports standing as the old lived state. temp/ holds the
  user's staging copies, theirs to clear.
- Resume: the Next slot is empty. Nearest Later candidates: the
  two-tier harvest question (ADR-0007 amendment) and the define
  phase gap (cbc-bootstrap territory). The new layout and the
  README law await their first lived run.

## 2026-08-29  (session: framing shape decided, run 2 harvested)

- The record-shape decision taken and landed with the run-2 harvest
  as one change set (2095d02 plan → ed5f19b shape → 4131157 intent
  → a607cca probes → f7216b8 ledgers → cd86b76 step-6 passes →
  75cb903 registry → 1a22fbe TODO → 8c51396 close), user reviewing
  at each boundary. The shape: one working record,
  framing-derivation.md at the run repo's root — per-step sections
  split earned/how-it-ran, frozen at their verdicts, decision-free
  appendix files as the escape valve — composed at close into the
  three exports under the residue filter and committed in
  derivation order. Deciding argument for one doc over per-step
  files: the steps compound (each consumes the previous, the earned
  layers stack into one definition), so file boundaries were
  artificial and cost restated-context glue; the verdict-freeze
  rule keeps multi-doc's real virtue. Rewriting turned out to be a
  non-argument — safe-reservations' translation was near-verbatim
  assembly either way.
- One divergence, caught by the user at a boundary review: the
  planned name framing.derivation.md carried the old workbench
  dot-suffix kind-tagging — meta info our headers already carry.
  Revised first-class (90b84c0) to the hyphenated form. The same
  review surfaced that the three export names are themselves dotted
  inheritances; parked in TODO (b8028d1) as a deliberate decision,
  with checkout as the lived precedent either way.
- Parked in TODO from run 2, not landed: the two-tier harvest idea
  (an ADR-0007 question), the define phase gap (cbc-bootstrap
  territory).
- Resume: doc-projection check (the TODO Next item) — the model and
  guide live in the safe-reservations node's close/ and knowledge/;
  same read-only and language rules. The repo's PLAN resume point
  remains Step N (release).

## 2026-08-29  (session: framing check run 2 — safe-reservations read)

- Run 2 of the TODO framing check executed: the safe-reservations
  problem-framing-node read in full, read-only, at
  archive .../worksites/safe-reservations/problem-framing-node. The
  custom maintenance language (walks, labs, forks, flow-back,
  D/F-numbers) identified and ignored throughout; underneath it the
  node is the method's birthplace — our skill is its distillation,
  so the check became "what did the distillation lose."
- Origin fact worth keeping: the walk log records why the
  every-verdict-human rule exists — an informal walk 0 where the
  agent derived competently but the human "did not control the
  process and did not see the decisions being taken." The rule's
  lived origin; checkout later proved recorded delegation workable.
  Both stances now sit in our skill (default + delegated mode).
- Harvest candidates banked (verdicts owed, none landed yet):
  (1) probe machinery as teachable procedure — three lenses
  (assumption hunt / stretched timeline / resource grid), the
  three-stamp rule (new fact · nothing new naming the covering
  line · out of scope written), the audit checklist for verifying
  the framer without re-deriving — born from the user's own demand;
  (2) numbered fences (W-list) for written-out scope, visibly doing
  work at step 3; (3) the "not probed" honest ledger; (4) scope
  verdicts as a named step-2 output, each with recommendation and
  reason; (5) richer intent shape — audience (claim-buyer vs
  consumers), worth-proving, what done demonstrably means;
  (6) registry refinements beyond checkout's — adversity-class
  grouping as headings-never-boundaries, riders whose silent
  violation voids a slice's evidence, evidence-shape flags, the
  written zero; (7) step 6 as three visible passes (sort with a
  because per stamp → pairwise dedupe → folds); (8) a two-tier
  harvest idea (sure adoptions vs held insights with a promotion
  path) beside ADR-0007; (9) a small define phase (project name,
  repo name, repo description, decided with verdicts) between
  framing and bootstrap — currently covered by no skill.
- Evidence for the record-shape decision (TODO item): the lived
  pipeline was per-step pairs (completion = what the step earned,
  pure, verdict-closed, feeds the next step; derivation = how it
  ran, kept for audit) → at close composed into the three exports
  by a written export plan — committed to the project repo in
  derivation order, eight commits, so the project's git history
  tells the derivation story — under a residue filter: no lab
  vocabulary or paths ever project-side, conclusions re-grounded.
  The user's one-doc-translated-at-close idea matches the
  composition half; the open half is whether the working record is
  one growing doc or per-step files.
- Doc-projection confirmed real and separate (model + guide live in
  the node; README derived from internal masters at milestones) —
  stays parked in TODO as its own later check.
- Resume: the record-shape decision (options + recommendation),
  then the harvest change-plan for the banked candidates, then
  doc-projection.

## 2026-08-29  (session: framing check run 1 — checkout harvested)

- The TODO framing-check direction opened (24f9e5f queued it) and
  run 1 of 2 executed: checkout-system's framing artifacts read
  read-only against the cbc-framing skill. Verdict: no violations —
  every per-step gate checkably satisfied, terminology fully ours.
  Five lived-beyond-the-skill findings; four harvested as a
  seven-commit change set (aaad989 plan → bba4755 registry
  template + skill-side outcomes → 01e9422 living exports with
  logged revisions → d87a4ed recorded saturation log → b30e76e
  labeled trust list → c365890 delegated-verdict mode → db06098
  close, no divergence), user reviewing at each boundary.
- The delegation decision, since it changes how future auto runs
  read the skill: human verdicts stay the default; a run may
  delegate only via an explicit decision in its own
  .claude/decisions.md naming the delegation and its cost. A config
  flag was rejected — it would hide a decision that must stay
  visible. The user plans more fully-auto runs; this is the
  sanctioned path.
- Finding 2 deliberately NOT harvested: checkout already splits
  pure exports from derivation record (ADR-0002 carries the kill
  list), but the record is thin — the process itself is lost. Held
  as evidence for the one-derivation-doc-translated-to-three-exports
  decision, parked in TODO until safe-reservations (run 2) is read.
- Resume: framing check run 2 — safe-reservations at
  archive .../worksites/safe-reservations/problem-framing-node,
  read-only, old custom language distinguished and never adopted;
  then the record-shape decision; then the doc-projection node.

## 2026-08-29  (session: app-structure reference adopted)

- Yesterday's parked decision decided: adopt. Four-commit change
  set landed (plan → reference → walkthrough routing → close),
  the user reviewing at each boundary. app-structure.md now sits
  in cbc-bootstrap/references: the lived default authoritative
  (package-by-feature, package-private, depth earned per feature —
  harvested from checkout's nine slices), the decision rule
  (decided at bootstrap, logged with its why; a stated practice
  intent is a legitimate deciding input), and the four named
  alternatives in two lines each, all marked unlived. The
  slice-reach question resolved without coupling skills: the
  decision travels through the run's own log, which slice work
  already operates under; the doc states its reach in one line.
- CORRECTION, recorded as a new fact (the old entry stands —
  never clean up): the previous entry refers to a TODO Later
  trigger line "parked 2026-08-28". That line was never committed
  — the in-session claim was made without the edit actually
  happening; only the postgres tag-drift note (e783a33) was real.
  Nothing existed to absorb; the change-plan and its close carry
  the same statement.
- Standing expectations after this set: the next run tests the
  harness reference on the lived stack line and the default
  structure (one variable at a time); the first run to live an
  alternative structure upgrades its vocabulary entry with a
  harvest line.
- Resume: Step N (release) remains the next PLAN step.

## 2026-08-29  (session: app-structure question opened, undecided)

- Q&A session, no change set. Discussed application structure
  against checkout's lived shape (package-by-feature,
  package-private boundaries, depth earned per feature): classic
  layered, hexagonal/onion/clean, vertical slice, modular monolith
  named and weighed. Two positions reached, neither enacted yet:
  structure is a bootstrap decision recorded like the stack
  decision (default = the lived shape; a named pattern is legal
  when the run's log carries the why — practicing a pattern counts
  as a deciding input if stated); and a short app-structure
  reference in cbc-bootstrap/references likely earns its place —
  decision hook + recall + user↔agent shared vocabulary, NOT a
  patterns survey (pros/cons essays stay re-derivable). If adopted
  it absorbs the TODO Later trigger line parked 2026-08-28.
- The user's closing observation, not to lose: the structure
  choice also shapes how slice work writes code against its
  planned requirements — so the decision's reach is beyond
  bootstrap. Weigh tomorrow whether the reference (or the run-log
  decision it prescribes) needs routing where cbc-slice work sees
  it, not only at bootstrap.
- Resume: decide the app-structure reference — yes/no, its home,
  its pointers (including the slice-side reach above); if yes, run
  it as a change set. Next PLAN step remains Step N (release).

## 2026-08-28  (post-Step 6: the harness reference adopted)

- Two workbench-era docs handed over (temp/, uncommitted, deleted
  after use). The pom convention was superseded — our Step 4 import
  is its cleaned descendant; diffed section by section, nothing to
  take. The harness reference was the find: the stage 4–5 recurring
  artifacts as code, exactly the test-support gap TODO'd in Later.
- ADR-0008's second-run trigger judged fired: the doc itself proves
  two pre-repo passes, checkout-system re-derived the shape a third
  time. Landed as a *reference* (imitated, never pasted) —
  ADR-0008's own boundary, not a rule change. spring-harness-
  reference.md now sits beside the walkthrough, which routes to it
  from stages 4–5.
- The confirmation pass against checkout's bootstrap (read-only,
  d732b53 and 83262b5) corrected the handed doc in five places —
  the load-bearing one: the container as a faithful miniature
  carrying the ground's authority split (bootstrap.sql mounted,
  migrate as migrator, context as runtime, identity asserted);
  the second pass had run the whole harness as the Testcontainers
  superuser. Also: two bases not three; MigrationPathIT joins the
  set; the probe round-trips current_user; the pool is sized to
  the count. The old virtual-threads claim and the
  failOnMissingLocations guard survive as variation points, each
  attributed to the pass that lived it.
- The old maintenance language (genre labels, workbench mastering,
  flow-back, node/seat vocabulary) stripped on import, per the
  standing rule from the earlier archive read: identify, never
  adopt.
- Resume: Step N (release) still next in PLAN.

## 2026-08-28  (post-Step 6: harvest from the archived run)

- On request, read safe-reservations' project-replica (the run that
  predates this repo, in the ai-context-system archive worksite) —
  read-only, fenced to that one directory — and compared it against
  all seven template masters. Verdict: the old run is the templates'
  ancestor, same lineage through checkout-system; every divergence
  bar two was our later decision already. Its own maintenance
  language (worksite/node/replica layout, numbered log entries, the
  internal-masters doctrine) identified and deliberately not
  adopted; the shared ground vocabulary (Execution Environment,
  service constraints) already lives here via infra-establish.
- The two divergences worth keeping harvested as their own change
  set (ADR-0007), four commits, nothing diverged: the verify
  suite's \echo banners and readable object-type names; the runtime
  password key renamed <PROJECT>_RUNTIME_PASSWORD across
  .env.example and application.yaml (one commit — declaring and
  reading sides of one key). The masters now diverge from
  checkout-system's lived key by intent; its copy picks the rename
  up only by copying anew. Non-adopted divergences are named in the
  verify master's harvest line, so the question does not reopen.
- Resume: Step N (release) is still the next PLAN step.

## 2026-08-28  (Step 6: templates from the lived run)

- Step 6 done in one session, nine commits, none diverged. Seven
  copy-and-fill masters now live inside their skills (five under
  infra-establish/templates/, two under cbc-bootstrap/templates/),
  each verified by substituting checkout's identities back in and
  diffing against the lived file — deltas matched the declared
  generalizations exactly. Both walkthroughs shrank to whys, traps,
  and pointers; the bodies live once.
- ADR-0008 got the load-bearing distinctions: templates ride inside
  the skill (self-containment); a fill becomes the run's own file,
  not a pinned copy; fills never harvest back, shape changes do;
  and the boundary rule — imitated content stays an example under
  references/, pasted content becomes a template, application
  source is neither until a second run re-derives the same shape
  (test-support Java parked in TODO Later on that trigger).
- The blind-trust question at review produced the off-template
  rule (assumptions differ → derive from the model, record, expect
  a harvest — never bend a decided constraint to fit a template)
  and the fill-trail line in the handoff. The guards that already
  existed: decisions upstream of templates, Verified: gates
  downstream, harvest loop around it all.
- Second harvest landed en route: the lived .env carries a fourth
  key (runtime application password) the walkthrough predated.
  Extraction also surfaced a run inconsistency (CHECKOUT_DB_PORT
  vs POSTGRES_PORT) — kept as lived in the templates, TODO'd:
  fix in the run first, then harvest.
- Also this session, advisory: close read confirmed
  the-whole-system-in-plain.md agrees with concept v1 (four minor
  compressions noted, no rewrite owed); archive deprecation needs
  no header changes — the headers already deny it authority —
  frozen beats deleted so pins stay checkable; ARCHITECTURE
  invariant now says retired.
- Resume: Step N (Release) — CHANGELOG release entry, README true
  for a stranger, known issues filed in TODO. The harvest-loop
  success criterion was met at Step 5; templates were the last
  authored step.

## 2026-08-28  (Step 5: first harvest)

- The loop the repo exists for ran once, end to end: checkout-
  system lived a Boot 4.1 trap (RANDOM_PORT alone provides no
  TestRestTemplate bean; @AutoConfigureTestRestTemplate required),
  recorded it in its decision log, fixed its own copy — and this
  repo read that record and took the lesson into the authoritative
  spring-boot-walkthrough.md in the run's own wording. Body now
  byte-identical to the run's lived copy. Run repo read, never
  edited. Six commits, none diverged.
- Harvest discipline settled from the lived case (ADR-0007): the
  execution's provenance header is its change log — one dated
  harvest line per change, traveling with every future copy; no
  concept bump for execution-only changes; CHANGELOG stays the
  pure concept-version log; archive visibly stale by design.
  Local rule in the bundle doc's Harvest section; promotion to
  the handbook waits for the garden rule's trigger.
- Worth remembering: the harvest was a two-hunk diff — smaller
  than any plan around it. That is the loop working: the run pays
  the hunt once, everyone downstream inherits it at birth.
- Templates question resolved at plan review: checkout-system's
  lived ground files put extraction past the don't-author-
  speculatively bar, so Step 6 (templates extracted from the
  lived run) was authored at this step's close — templates as
  master, both walkthroughs re-derived to point at them, pom
  excluded by its own convention.
- README success criterion "harvest loop run once end-to-end" is
  now met; noted in PLAN for release time.
- Resume: Step 6 (templates) — draft its change-plan: read
  checkout-system's compose/bootstrap-SQL/verify-suite/env files
  read-only, land them as pinned master templates, re-derive the
  two walkthroughs to keep whys and point at the templates
  (harvest lines record it, ADR-0007).

## 2026-08-28  (Step 4: practice executions land)

- Step 4 done in one session — ten commits, one mid-set revision,
  the change set that proved the boundaries. The pipeline is
  complete: infra-establish (+ absorbed record defaults),
  infra-serve, cbc-bootstrap under executions/ as skills, pinned
  "checked against concept v1" (ADR-0005 — practice-born
  executions get honest pins, not derives-from claims).
- The form debate, worth remembering whole: the archive ships the
  practice phases as skills driven by agent seats. At the commit-3
  boundary the over-engineering question was raised; a ten-file
  skills+agents staging was reverted unlanded. First swing: guides
  + plan-step pointers (P2 — the phases are planned, pointers at
  the moment of need fire). Counter-swing: re-entry is unplanned —
  "we need Redis now" has no plan step waiting, and a guide then
  depends on human memory (P1). Settled: skills minus agents
  (ADR-0006) — one delivery mechanism, triggers covering the
  unplanned case, the never-lived seat layer left behind.
- DEAD END: the guides-shaped revision (drafted, staged, replaced
  at the same boundary before landing). Not wasted — its P2
  reasoning survives in ADR-0006's rejected-options.
- Import fixes finally fired: the archive keeps infra-establish at
  skills/SKILL.md against its own STATUS diagram (unregisterable
  as a named skill) — normalized, recorded in headers; the
  groundskeeper's record-path defaults absorbed into the SKILL as
  a recorded addition.
- STATUS/LAYOUT stayed behind; their open/owed items are in TODO
  Later, joined by the templates idea from review: extract
  copy-and-fill templates (compose, bootstrap SQL, verify suite —
  not the pom) from the next lived run, template as master.
- Plan-prose slip caught at staging: "twelve files" where the
  enumeration said ten. Never landed; retro'd in the close.
- Resume: Step 5 (first harvest) — draft its change-plan: read
  checkout-system's Boot 4.1 testing-trap entry (read-only),
  bring it into spring-boot-walkthrough.md with run provenance,
  decide the post-import change discipline (execution changes vs
  the concept-version log) and the harvest-discipline question.

## 2026-08-28  (Step 3: executions land)

- Step 3 done in one session, seven-commit change set, none
  diverged. The derived layer exists: nine files under
  executions/ (cbc-framing and cbc-slice with their references,
  the startup snippet), each header opening "derives from concept
  v1" plus provenance @ fe0075d. A run can now be born from this
  repo's copies — executions/README.md carries the birth mapping
  and the authoritative-vs-pinned rule.
- Home decision (ADR-0004): executions/ at the repo root as
  content, not .claude/skills/ — this repo never frames or slices
  itself, the skills could only misfire here, and content commits
  would land agent-scoped. Committed the ADR before the placement
  it governs; the pattern read well at review.
- Close-read finding, marked not fixed: the two worked-example.md
  files are byte-identical — bundle design, each installed skill
  self-contained. Twin note in both headers so a change to one
  lands in both. Divergence between them would otherwise be
  invisible (agent model O1).
- Mechanical detail worth keeping: SKILL.md pin headers sit below
  the YAML frontmatter so a verbatim run-repo copy still parses
  as a skill; the pin line names the concept repo so it stays
  self-contained in a copy.
- Step 4's close read surfaced two honest questions now in its
  gate: practice-born executions may not truthfully say "derives
  from concept v1" (they grew from practice), and the archive's
  STATUS/LAYOUT companion docs need a decided fate.
- Resume: Step 4 (practice executions land) — draft its
  change-plan: import infra-establish (+ infra-serve) and
  cbc-bootstrap; decide the pin phrasing and the companion-doc
  fate; update the bundle doc; problem-framer/ stays out.

## 2026-08-28  (Step 2: concept lands)

- Step 2 done in one session, seven-commit change set, none
  diverged. The mental layer exists: five chapters at concept/,
  archive names kept, each verbatim below a provenance header
  pinned to archive fe0075d. Close read found no defects — the
  plan's provision for recorded fixes went unused. Archive concept/
  is now a historical snapshot.
- Versioning: whole-number concept versions over the mental layer
  as a whole (ADR-0003); rejected SemVer (false precision over
  prose), per-chapter versions (no consumer), commits-as-versions
  (indiscriminate). CHANGELOG is the concept-version log, opened
  at v1 = the chapters as imported. Bump rule: could it invalidate
  a derived execution.
- Repurposing the CHANGELOG stub meant replacing its rules, not
  filling them (app-repo assumptions) — fourth handbook-feedback
  entry queued in decisions.md.
- Call worth remembering: chapter provenance headers deliberately
  omit any versioning reference — the import commit landed before
  the scheme was decided, and a forward reference would have
  reverted incoherently. ADR-0003 governs; headers carry
  provenance only.
- ARCHITECTURE de-provisionalized: the Step 0 hunch held. The
  no-version-entry-no-change invariant is named a review-grade
  wall — the repo's own concept says what to think of that.
- Resume: Step 3 (executions land) — draft its change-plan:
  import cbc-framing, cbc-slice, startup snippet pinned to concept
  v1; decide the executions' home (content, not this repo's
  arrangement) and the bundle question (what a run repo copies at
  birth). Consumes docs/models/agent.md.

## 2026-08-28  (Step 1: framing)

- Framing done in one session (spanned midnight; gates closed
  2026-08-28). Six-commit change set: README framed (success
  criteria, out-of-scope, command stubs deleted — no-commands
  resolved on both sides of the agent/project split), middle steps
  authored (Steps 2–5: concept → birth-material executions →
  practice executions → first harvest), Step 1 closed.
- Read the two archive directories for the first time. Findings:
  the concept is mature — five chapters that read as the mental
  layer's seed, and their split answers the one-doc-or-several
  question (several). The executions form a pipeline: cbc-framing
  → infra-establish → cbc-bootstrap → cbc-slice, each refusing to
  run without the previous one's artifacts. The startup snippet
  cleanly separates method from project decisions.
- Finding: agents-from-practice/ holds three executions, not the
  briefed two. The third, problem-framer/, is a framing method
  from an older lab/walk lineage overlapping cbc-framing —
  excluded completely as noise at review, same status as the rest
  of the archive.
- Decisions: import order is dependency order (concept before the
  executions that pin to its version); first harvest gets its own
  early step to prove the loop; no models routing line in
  CLAUDE.md — pointers ride the steps that need them (agent model
  P2); the name held (the material itself says CbC).
- Resume: Step 2 (concept lands) — draft its change-plan: import
  the five chapters with provenance, decide the concept-version
  scheme (v1) and CHANGELOG's role, de-provisionalize
  ARCHITECTURE.

## 2026-08-27  (Step 0: bootstrap)

- Project started. Repo initialized from the starter kit
  (handbook @ 4fe8083).
- Briefing: one repo for one concept being learned — correctness by
  construction, the design principle that correctness is built into
  the structure of a thing rather than tested in afterwards. Working
  name correctness-by-construction ("cbc" in prose); framing may
  rename. The problem: the understanding lives in a head and
  scattered notes and does not improve in any recorded way when
  things are tried. Wanted: one authoritative place for the
  plain-words statement, its rationale, open questions, and a log of
  what changed it and why. Hunches, not decisions: the concept
  splits into a mental layer (the statement itself) and executions
  derived from it — agent skills, checklists, templates — each
  stating which concept version it derives from; runs and
  experiments happen in other repos, pinned to a concept version,
  and their surprises come back here as harvested concept changes,
  after which executions are re-derived. This repo is the middle
  tier of the workspace (handbook → concepts → runs), under
  concept-garden/, a plain folder. Existing material (input to
  Framing, not pre-agreements): a drafted concept statement and two
  workflow executions in ~/PycharmProjects/archive/cbc/
  system-design-method/birth-materials/ (five concept chapters,
  cbc-framing and cbc-slice skills, a startup snippet); two more
  executions from practice in the same repo's agents-from-practice/
  (infrastructure establishment, system bootstrap) — only those two
  directories matter, the rest of that repo is noise. One live run:
  ~/IdeaProjects/checkout-system, born 2026-08-27 with executions
  copied from the archive snapshot; its decisions log already
  records one improvement (a Boot 4.1 testing trap) that the
  archive copy lacks — the first harvest candidate. Whether an
  execution later graduates to its own concept repo is open, with a
  named trigger (the garden rule: a second concept, a rule written
  twice). Done-ish: months from now the concept doc is consulted
  and updated after runs, and at least one derived execution was
  used in a real project.
- Open: what granularity a "concept version" is; whether
  harvest/provenance discipline is local rules or its own
  convention; whether the mental layer is one document or several.
- Session close: Step 0 done — six-commit change set landed as
  planned (plan open → agent install → records → models → step
  close → plan close); three decisions.md entries queued as
  handbook feedback (commit order, stub comment discipline,
  attribution — trailers stripped from history and disabled before
  anything was pushed). Agreed working practice, not yet recorded
  anywhere binding: this repo has no project end, so
  playbook/retrospective fold-back happens at step-gate closes —
  log it as a decisions.md deviation the first time it is
  exercised. Parked for Framing: whether CLAUDE.md gets a models
  routing line (agent model P2 — pointer at the moment of need vs
  ambient), and whether ARCHITECTURE's Components/Invariants/
  Codemap sections fit a docs-only repo (fill with structural
  invariants, or delete).
- Resume: Framing (PLAN Step 1) — read the two archive directories
  (birth-materials/, agents-from-practice/), then problem statement,
  success criteria, out-of-scope, middle steps authored; the archive
  import is project work there and gets its own change-plan.
