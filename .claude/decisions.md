# Agent decisions

<!-- The working arrangement's decision log (handbook ADR-0020,
     provisional). Append-only, newest last. One entry per
     arrangement decision — a skill added or changed, a rule tuned,
     a workflow adopted. Three lines: what, why, what was rejected.

     Division of labor: the standing rule rides as a comment in the
     artifact it governs — this log keeps the why and the rejected
     options, and neither repeats the other. Commit bodies stay
     ordinary commit bodies.

     This file is agent-side: a commit touching it is scoped `agent`
     and touches nothing else (the commit-messages skill carries
     that rule).

     At the project retrospective, read top to bottom: each entry
     graduates to the handbook, stays local, or dies.

     The placeholder on the "@" line below is replaced at copy
     time by the install block in the handbook's manual. It pins
     which handbook state — and so which version of every
     convention — this project was born from (convention-lifecycle
     §2). If that line still shows a placeholder instead of a
     commit hash, the install block was not run from the handbook;
     fix it before the bootstrap commit. -->

- 2026-08-27 Born from the engineering-handbook starter kit
  @ 4fe8083.
  Conventions: project-recording, commit-messages, repo-hygiene,
  artifact-kinds, change-plans.
  Why: handbook defaults.
  Rejected: none — see the handbook's ADRs.

- 2026-08-27 Step 0 commit order: working arrangement installed
  before the project records.
  Why: the arrangement that governs the series belongs on record
  before the work it governs; the agent-scoped commits then sit
  together at the head of the set. Nothing mechanically depends on
  the order.
  Rejected: the kit stub's prescribed order (plan open → project
  records → agent install → plan close). Candidate handbook
  feedback at retrospective: the stub's comment may want updating.

- 2026-08-27 Stub comment discipline: left as delivered, but the
  rule defining it is about to lose its only home.
  Why: the stubs use two comment kinds — fill-comments (marked
  "Fill-comment:", replaced by content) and standing rules (stay
  forever) — yet the only text stating that distinction is PLAN's
  Step 0 bootstrap comment, deleted when Step 0 closes. The
  discipline should also state that comment voice is actor-neutral:
  addressed to whoever edits the record, never to a named agent —
  already true of every stub, but nowhere written. Candidate
  handbook feedback: give both rules a stated home (likely
  project-recording); this repo does not author method (tiers
  model).
  Rejected: defining it locally as a project convention — wrong
  tier. Also rejected: visible text or admonitions instead of
  comments — the rules address the raw-file editor, not the
  rendered reader (agent model: installed, self-enforcing
  delivery).

- 2026-08-27 Commit attribution: agent trailers (Co-Authored-By,
  session link) stripped from this repo's history and disabled
  globally in the agent's settings.
  Why: commits are the author's; whether tool involvement is
  visible in public history is the author's call, and here the
  call is no. Trailers are plain message text — with them gone,
  nothing in git records agent involvement.
  Rejected: keeping the tool default. Candidate handbook feedback:
  the arrangement should state an attribution policy at birth (in
  the kit/install block), so it is decided once instead of
  discovered at the first commit.

- 2026-08-28 CHANGELOG stub repurposed: header and standing comment
  rewritten for the concept-version log role (ADR-0003).
  Why: the kit stub assumes an application repo — SemVer, user-speak
  examples, Deprecated/Security categories. A concept repo's
  changelog users are pinners (run repos, executions citing a
  version), and its versions are concept versions; the stub's rules
  had to be replaced, not filled. Candidate handbook feedback: the
  kit may want per-repo-type CHANGELOG stubs, or a stub that asks
  what a version is here instead of assuming SemVer.
  Rejected: keeping the stub and logging versions elsewhere — two
  version-shaped records where the repo needs one.

- 2026-08-30 The four candidate-handbook-feedback entries above
  graduated: delivered in the first upward handoff (temp/ channel)
  and triaged handbook-side the same day (their change set
  06cc06d..e3e45bd). Outcomes: commit order freed (their fix cites
  the 2026-08-27 entry's reasoning); comment discipline and
  attribution parked in their TODO with leanings; CHANGELOG stub
  parked, leaning one-stub-that-asks. Graduation ahead of the
  retrospective, at the user's call — the birth from the manual
  needed the kit bug fixed first, and the ledger items rode along.
  Rejected: holding them for a retrospective this endless repo will
  not have (the fold-back-at-gate-closes practice, devlog
  2026-08-27, applied to the ledger for the first time).

- 2026-09-01 change-plans convention updated in place from the
  handbook @ 65dd7ee (their ADR-0027): rolling commit lists,
  material-first step order, records steps planned by walking the
  records table, in-set ADRs Proposed by default; requires gains
  project-recording. First live-repo convention injection —
  procedure hand-supplied in their return item 11, deliberately
  unwritten on their side; our friction notes are the payload they
  asked back.
  Why: the vendored copy was stale against the convention now
  governing our own change sets; the next set would have been
  planned under superseded rules.
  Rejected: waiting for the next birth (births refresh kit copies,
  not a live repo's); re-deriving the changes locally (wrong tier —
  the handbook authors method, we consume it pinned).

- 2026-09-03 Convention injected: convention-lifecycle @ f9371e4
  (their ADR-0030; ships in the kit since ADR-0023's condition
  landed). Sixth convention here; first injection run under
  written §8 — the procedure our 2026-09-01 friction notes built.
  Friction gathered for the next handoff: our CLAUDE.md deleted
  the kit's placeholder line (as the stub permits), so "row at the
  placeholder line" had no anchor — row landed at the list's end
  per §8's own reading, which differs from where the kit stub
  places this convention's row (before Hygiene); born and injected
  repos will disagree on row order.
  Why: taken now, not at leisure — the re-birth's newborn holds
  six conventions, and this repo running §8 first hands the newborn
  a procedure with two lived runs behind it.
  Rejected: waiting for the re-birth (the reply's "not urgent") —
  our own arrangement would sit behind the kit we deliver on.

- 2026-09-03 Convention updated: artifact-kinds @ f9371e4 (was
  @ 4fe8083, the birth pin). One drift line: the playbook kind's
  exemplar, starter/kit/playbooks/TEMPLATE.md → playbooks/default.md
  (their ADR-0028 trail). Caught by §8 step 2's chain-currency
  check while injecting convention-lifecycle, whose requires names
  artifact-kinds — the reply's missed-check lesson, lived the same
  day it arrived. Compare-first ran clean: our copy was identical
  to the master at the pin, no local edits, overwrite silent-safe.
  Why: a stale requires-chain member fails the §8 evaluation for
  every future injection.
  Rejected: leaving it (the drift is cosmetic today, but currency
  is now a stated §8 requirement, not a judgment call).

- 2026-09-03 Convention updated: project-recording @ f9371e4 (was
  @ 4fe8083, the birth pin) — the first lived installed-path update
  anywhere, per §8 step 4's by-argument paragraph. Compare ran kit
  stub against kit stub across the span. Findings: PLAN stub drift
  is birth-shape only (STEPS region, ADR-0028 — nothing retrofits
  into a living plan); CHANGELOG stub already answered here,
  specialized past its new placeholder (ADR-0003); README stub's
  closing comment gained the projection rule, carried into our
  README as its own project-side commit (§8 step 3 — sides never
  share a commit). Friction for the next handoff: the by-argument
  paragraph held, but "compare kit stub to kit stub" spans three
  record stubs and the reader must know which records the
  convention ships through — a stub manifest per installed
  convention would make the compare mechanical; and a living
  record that already absorbed the change via a reply reads as
  "nothing to carry", so the update is mostly verification when
  the reply loop is healthy — worth §8 saying so.
  Why: their reply flagged the chain check we missed (change-plans
  requires project-recording); currency is now a §8 requirement.
  Rejected: treating reply absorption as the update (it leaves the
  registry pin stale — the registry would say 4fe8083 while the
  records lived at f9371e4).

- 2026-09-07 CLAUDE.md moved to .claude/CLAUDE.md. Same channel,
  read identically by the harness; every agent-side file now sits
  under .claude/, so the agent/project commit split reads as "under
  .claude/ or not", with no file named beside it.
  Why: the split rule and the records table both listed CLAUDE.md
  as the one agent file outside the agent directory — one location
  removes the exception. This repo trials the shape; the kit stub
  runs receive stays at root until the handbook decides.
  Rejected: moving the run's copy in the same stroke (the kit stub
  is the handbook's; the pure seed still delivers it to root).

- 2026-09-09 Pinned copies updated to the handbook @ af16eb7:
  commit-messages (was @ 4fe8083, the birth pin), change-plans,
  artifact-kinds and convention-lifecycle (were @ f9371e4), and
  the agent model docs/models/agent.md (was @ 4fe8083); tiers.md
  verified identical across the span, pin left as is. Compare-first
  ran clean on all four skills: each identical to the kit copy at
  its pinned hash, no local edits, overwrite silent-safe. What
  moved: the pace rule now the first rule of thumb in
  commit-messages, with the commit stop named a gate (their
  ADR-0035); change-plans §3's gate-item walk and §6 pointing at
  the pace; convention-lifecycle §8's installed-path text lived,
  its step 5 dropping the entry-file row (their ADR-0034), and its
  requires gaining agent-arrangement; artifact-kinds' playbook
  exemplar line; the model's §4 ownership, §7 permission prompt,
  §10 rules directory, comments dropped by the loader (their
  ADR-0036), and the gate row.
  Findings from the pass, each a decision still open: (1) §8
  step 2's chain check fails — convention-lifecycle now requires
  agent-arrangement, which this repo never received (born before
  it existed; run 3 was born with it); its injection is installed
  delivery through the entry file's guard comment and the settings
  file. (2) The entry file's Conventions list, which the lifecycle
  copy now says a project does not keep (their ADR-0034), stands
  here — it goes with the same injection or stays by decision.
  (3) The installed conventions drifted too — repo-hygiene's base
  gained the operator's-file line, project-recording's stubs moved
  f9371e4..af16eb7 — and land project-side, in their own commits
  (§8 step 3). (4) The pin had been lying since 2026-09-07: the
  c670fe5 changes were absorbed through TODO and the reply loop
  with no entry — §8's own warning, lived here. (5) Every ADR
  number inside a pinned copy — the four skills, the two models —
  is the handbook's, and the bare ones below 0020 collide with
  this repo's own sequence on other subjects. Reading rule: a
  citation in a copy resolves at the source, at the hash this
  registry names for that copy, never against docs/adr/ here. The
  copies stay verbatim; the fix belongs at the master (a
  self-qualifying citation survives the copy) and goes up as §8
  friction with the next handoff.
  Why: the reply of 2026-09-08 was written against af16eb7's
  state; a bundle read at the retrospective must hold the text it
  answers, and the registry must name the hash the records are at.
  Rejected: waiting for run 3's Step 1 reading (the reading needs
  the current text on this side); folding the installed drift into
  this commit (sides never share one).

- 2026-09-09 Convention injected: agent-arrangement @ af16eb7 — the
  seventh, the one convention-lifecycle's requires now names that
  this repo was born without (the birth pin predates it). Installed
  delivery through the entry file: the kit stub's two comments at
  the pin replace ours (the records comment; the three-tests guard,
  rules directory named, in place of the SIZE BUDGET comment), the
  table takes the stub's two rows this one lacked (the decisions
  row's wording — the conventions held, with versions; the
  CHANGE-PLAN.md row, change-plans' one ambient line), and the
  Conventions section leaves whole: this registry is the project's
  only list of its conventions (their ADR-0034), and the skills load
  themselves. Orientation lines untouched.
  The entry file returns to the root in the same commit, undoing
  the 2026-09-07 move: the handbook's reading of 09-09 gives the
  address a meaning — root for a repo whose subject is the
  arrangement, .claude/ for one that builds an app — and this repo
  is the first kind; run 3, the second, keeps its trial of the other
  address. The 09-07 entry stands as history, superseded here.
  Comments are edit-time text (their ADR-0036): the guard governs
  every edit of this file and costs no session; the file's ambient
  weight is its table and three lines.
  Why: §8 step 2 makes chain currency a requirement, and the same
  pass checks a member newly required; here the member was absent,
  and the installed compare that updated the other two conventions
  is the same procedure.
  Rejected: .claude/settings.json — the commit ask rule is run 3's
  trial and withdrawn at the handbook; and nothing under starter/
  needs claudeMdExcludes: the harness loads skills only from
  .claude/skills/ and memory only from files named CLAUDE.md, and
  starter/ has neither (this session's skill list is the four kit
  copies). Keeping the Conventions list "for a human": the registry
  serves that reader, with versions. Keeping the .claude/ address
  because run 3 trials it: the trial reads an app repo's shape, and
  this repo's address would not add to that reading.

- 2026-09-09 Convention updated: project-recording @ af16eb7 (was
  @ f9371e4). The installed compare, kit stub against kit stub
  across the span, per §8 step 4's lived text and the "Shipped
  conventions" table: README's closing comment rewritten, TODO's
  header comment, the devlog's split-file line, PLAN's retrospective
  item 6 and its fold-back line — carried into the records
  project-side in 5e2cb69, "carry the stubs' changed comments into
  the records". Not carried: PLAN's birth-shape comments (nothing
  retrofits into a living plan, the 09-03 reading) and the kit's
  first ADR's context wording (ours is an accepted record, not a
  stub). CHANGELOG's comment already said "lands".
  Why: the pin must name the hash the records are at; the carries
  are the stub's rules as they now read.
  Rejected: none — every change was rule text, none a local edit.

- 2026-09-09 Convention updated: repo-hygiene @ af16eb7 (was
  @ 4fe8083, the birth pin). The base .gitignore's two changes
  carried into ours in the same project-side commit: the settings
  comment loses "(if any)", and the operator's-file block arrives —
  CLAUDE.local.md ignored, with the reason that the tool never
  ignores it on its own. .gitattributes and .editorconfig
  unchanged across the span.
  Why: the line is the hygiene base's now (their ADR-0035), and a
  checkout here may hold the operator's file.
  Rejected: none.

- 2026-09-11 Pinned copies updated to the handbook @ ab916a1 (were
  @ af16eb7): the four skill copies — commit-messages, change-plans,
  artifact-kinds, convention-lifecycle — and both models,
  docs/models/agent.md and tiers.md (tiers moves for the first time
  since the birth pin). Compare-first ran clean: each skill copy
  byte-identical to the kit at af16eb7, each model identical below
  its header; no local edits, overwrite silent-safe. What moved:
  every citation in the copies and the models reads HANDBOOK
  ADR-nnnn (their ADR-0037 — a reference to another repo's decision
  carries that repo's tag; a bare number is the reader's own);
  commit-messages' delivery is pushed with no gate, the stop being
  the sentence alone (their ADR-0035, decision 1 withdrawn — the
  kit ships no settings file); change-plans §6 names no settings
  file; convention-lifecycle §6 states the tag rule as the general
  case its stub rule was the special case of, and §8 step 2 says a
  convention required since the pin that the project was born
  without lands as a first injection in the same pass — what this
  repo did on 09-09; artifact-kinds' exemplar lines name their
  document by the role it holds for the reader; the agent model's
  window carries roles — the harness's wiring, the prompt, and tool
  results, weighed in that order, so a rule resting on a fact of the
  session is told every session by design (§5 corrected, §8's row,
  claim W2 evidenced by our three runs); the tiers model's §3
  rewritten from our five in four paragraphs, the told channel named
  for what it is — unpinned by design, not a third form — and the
  DRAFT note re-dated. The chain check (§8 step 2):
  convention-lifecycle requires agent-arrangement, held here @
  af16eb7 by installed delivery; its update at ab916a1 lands by that
  path, project side first, in this change set (CHANGE-PLAN.md,
  commits 5 and 7). The tag rule's project-side consequence — this
  repo's own tag, and the bundle's citations — is a decision of this
  repo, ADR-0020, in the same set.
  Why: the reply of 2026-09-10 was written against ab916a1's state,
  and the registry must name the hash the records are at (§8 step
  4's warning, lived here on 09-07).
  Rejected: none — no copy carried a local edit.

- 2026-09-11 Convention updated: agent-arrangement @ ab916a1 (was
  @ af16eb7). The installed compare, kit stub against kit stub
  across the span: the entry-file stub and the decisions-log stub
  unchanged; the kit's .claude/settings.json deleted — the commit
  gate left the kit (their ADR-0035, decision 1 withdrawn, on run
  3's report that every reader of the note opts out before running
  under it), and §3 now describes the file as one a project adds
  when it needs a gate or an exclude. Nothing lands: this repo
  never held the file (rejected 2026-09-09, the same reading), so
  what was a local rejection is now the kit's own state. The
  starter README's two tables lose the file's rows; no project
  text here named it.
  Why: the pin must name the hash the records are at; the entry
  records that the rejection needs no restating.
  Rejected: none.

- 2026-09-11 Convention updated: project-recording @ ab916a1 (was
  @ af16eb7). The installed compare across the span: one stub
  changed, README's — the decisions row gains "cited from other
  repos as `<TAG> ADR-nnnn`" (their ADR-0037; §3 states the rule,
  §7 names the slot). Carried project-side in 919dc9a with the tag
  filled, CBC (ADR-0020); the README fill follows the stub with
  `<TAG>` literal (aa5a1a5). PLAN, TODO, CHANGELOG, devlog
  and ARCHITECTURE stubs unchanged.
  Why: the row is where a repo declares its tag, and the reply
  asked for the declaration.
  Rejected: none.
  repo-hygiene verified unchanged across af16eb7..ab916a1 (the
  reply says so; the kit's three base files show no diff); pin left
  as is, the tiers precedent of 09-09.

- 2026-09-17 Pinned copies updated to the handbook @ ba7eaa4 (were
  @ ab916a1): the four skill copies — commit-messages, change-plans,
  artifact-kinds, convention-lifecycle — and both models,
  docs/models/agent.md and tiers.md. Compare-first ran clean: each
  skill copy byte-identical to the kit at ab916a1, each model
  identical below its vendoring header; no local edits, overwrite
  silent-safe. Taken under the note of 2026-09-16 in temp/, told not
  delivered, whose three corrections are what let the procedure at
  our pin run at all: step 1 diffs starter/kit/, not
  conventions/<name>/, the kit being the master of everything that
  ships (HANDBOOK ADR-0040); step 2's `delivery` frontmatter field
  is gone and landing is shown by where a file sits; step 4's master
  is starter/kit/.claude/skills/<name>/SKILL.md at the path we
  already hold it, no rename. The old file compared against still
  resolves — `git show ab916a1:conventions/<name>/CONVENTION.md` —
  because the compare is at our pin, not at HEAD: the layout change
  broke the fetch, not the comparison.
  What moved: all four rewritten, not adjusted, roughly two thirds
  of the text gone, each now rules only with its explanation left in
  a handbook page that never ships; convention-lifecycle renumbered
  §1–§8 to §1–§3 (requires-chains, the registry and the hash,
  updating a copy), step numbers inside the update unchanged, so our
  §8 step 4 is its §3 step 4 — citations of the old numbers in this
  log's history are left alone, the handbook fixed only its live
  ones. The rule changes, as against prose: convention-lifecycle §3
  step 4 gains "a project may edit its copy between two pins",
  provisional until one such edit has gone through an update
  (HANDBOOK ADR-0038, from run 3's hand-off of 09-15 — its rules 1–3,
  5, 6 and 7 in the handbook's text, rule 4's cadence reshaped), and
  gains the receipt branch as the compare when a project holds one,
  which we do not; its `requires` drops artifact-kinds, leaving
  change-plans and agent-arrangement, and its description gains the
  trigger "when a copy under .claude/skills/ turns out wrong
  mid-step"; commit-messages names CHANGE-PLAN.md among the agent's
  own files as before, unchanged in substance; change-plans' revert
  exemplar becomes a module and its ARCHITECTURE paragraph, and its
  records walk reads the entry file's table rather than naming
  project-recording; artifact-kinds' exemplars become repo-relative,
  each naming where this repo holds the thing. The models: tiers §3
  says an edited copy is not a third form of delivery — delivery
  comes down, an edit goes up — and that an edited copy's diff
  against its pin is one of the records the tier above reads; both
  models follow the renumbering in their cross-references.
  Why: the registry must name the hash the records are at, and the
  procedure we hold cannot run again until this lands.
  Rejected: none — no copy carried a local edit. Answering run 3's
  ask first (temp/bundle-handoff-2026-09-17.md): the shape it asks
  about is settled one tier up inside this very delivery, so CBC
  ADR-0007 would have been written blind to it; the ask does not
  block run 3, whose Step 6 opens on the copies as they stand.

- 2026-09-17 Convention updated: agent-arrangement @ ba7eaa4 (was
  @ ab916a1). The installed compare, kit stub against kit stub
  across the span: the entry-file stub unchanged; the decisions-log
  stub changed by one line, its cross-reference following the
  renumbering — "convention-lifecycle §7" to "§2", the registry and
  the hash. Carried into this file's own header above, which keeps
  its birth wording and takes only the section number. The
  conventions/ side of both stubs is now a symlink into the kit, so
  the kit is master in fact and not only by the note's word.
  Why: the pin must name the hash the records are at, and a live
  cross-reference to a renumbered section is a reader sent to the
  wrong rule.
  Rejected: none.

- 2026-09-17 Convention updated: project-recording @ ba7eaa4 (was
  @ ab916a1), verified unchanged across the span: of the kit's
  files only the four skills and the decisions-log stub moved, so
  README, PLAN, TODO, devlog, CHANGELOG, ARCHITECTURE and the first
  ADR are all untouched. Nothing lands; the pin moves so the
  registry names the hash the records are at.
  Why: an update absorbed without the pin moving leaves step 2
  reading a stale hash as current — this repo's own lesson of
  2026-09-08.
  Rejected: leaving the pin at ab916a1 on the grounds that nothing
  changed (the tiers precedent of 09-09 did that for repo-hygiene
  and it was right there, the reply being the evidence; here the
  evidence is our own diff over the kit, so the pin moves with it).

- 2026-09-17 Convention updated: repo-hygiene @ ba7eaa4 (was
  @ ab916a1), verified unchanged across the span: the kit's three
  base files — .editorconfig, .gitattributes, .gitignore — show no
  diff. Nothing lands.
  Why: as above.
  Rejected: none.
  Checked and needing nothing: every live citation of a renumbered
  section. convention-lifecycle's live §-references here were the
  header's alone; the two in this log's history are left as they
  were, the handbook's own practice with its own. change-plans kept
  §1–§7 and lost only §8, §9 and its Delivery section, so
  starter/installs/pure-seed.md's "change-plans §6" still names the
  review protocol and is not carried. The ADRs' "per change-plans
  §4" lines are history and stand.

- 2026-09-18 Local rule: a path written in a document of this repo
  is written from the repo root, never relative to the file it
  sits in. In anything this repo ships, the root meant is the
  receiving repo's — a shipped file names `docs/concept/00-cbc.md`,
  never `../concept/`, and never a path of ours.
  Why: found the same day, in the material. The handbook's
  convention manuals cite each other and the repo around them
  relatively; vendored to `docs/conventions/` they were read from
  a different root, and of the four links reaching outside their
  own directory, two dangled — `../../starter/README.md` and
  `../../starter/playbooks/` resolve to `docs/starter/...`, which
  does not exist here — while `../../models/tiers.md` and
  `../../models/agent.md` resolved only because `docs/models/` is
  where we happen to keep them. Two broken, two saved by accident,
  in one copy of one directory. Every artifact this repo makes is
  read from a root other than the one it was written at: the kit,
  the bundle, the fills, the vendored manuals. A relative path is
  a bet that the tree above a file travels with it, and here it
  never does.
  Rejected: fixing the vendored manuals' links — they are
  read-only and correct where they were written, and an edit
  would fork the explanation (ADR-0024 decision 5); the dangle is
  recorded in `docs/conventions.md` as a known consequence
  instead. Also rejected: filesystem-absolute paths, which name
  one person's checkout — `~/PycharmProjects/...` appears in the
  install manuals as an operator's variable and stays there,
  which is a different thing from a path inside a document.

- 2026-09-18 Correction to the entry of 2026-09-17: that entry says
  convention-lifecycle was "renumbered §1–§8 to §1–§3". It was
  §1–§9. Checked at both hashes that matter — the pin it was written
  against, `ab916a1`, and the one never-oversold held, `9e28143` —
  and each has nine numbered sections plus an unnumbered Delivery
  section. The entry's substance stands: the three new sections are
  named correctly, step numbers inside the update are unchanged, and
  §8 step 4 is §3 step 4.
  Why it is recorded rather than edited: this log is append-only, so
  a wrong fact is corrected by a later entry and the original stays
  as it was written. And the error travelled — the note delivered to
  never-oversold on 2026-09-18 repeated "eight sections", and that
  run stated nine in its own entry without flagging it as a
  correction. A receiver quietly fixing our arithmetic is the mildest
  possible way to learn this, and it would not always be.
  What it cost, which is the part worth keeping: the miscount was not
  the reason we missed the fourth stale citation, but it is the same
  mistake one step earlier — we described a renumbering without
  reading the range it covered, and then searched for one number out
  of nine. The procedure fix is in starter/installs/bundle-update.md
  (d209f9c); this entry is the fact.
  Rejected: editing the 09-17 entry in place (append-only, and a
  silently corrected record is worse than a visibly corrected one);
  leaving it, on the grounds that the substance held (the number is
  cited in a live procedure, and a wrong range invites a wrong
  search).
