# Agent decisions

<!-- The working arrangement's decision log. Append-only, newest
     last. One entry per arrangement decision — a skill or rule
     added, what one asks changed, a workflow adopted. A fix that
     brings a skill or rule to its manual is no decision: its
     commit body says why. Three lines: what, why, what was
     rejected.

     Division of labor: the standing rule rides as a comment in the
     artifact it governs — this log keeps the why and the rejected
     options, and neither repeats the other. Commit bodies stay
     ordinary commit bodies.

     An entry that follows from an ADR says in a line or two what
     changed in this arrangement, and points at the ADR; it does
     not retell it. -->

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

- 2026-09-19 Deviation from change-plans §4, recorded not repaired:
  ADR-0028 was committed with Status: Accepted at the second commit
  of an eight-commit set. The convention says an ADR inside a set
  opens Proposed and flips in the set's final records commit, and
  §7 lists the early Accepted among its anti-patterns.
  What it cost, which is exactly what the rule predicts: two later
  boundaries changed the ADR. Decision 5 lost one of its three
  arguments when decision 4's home moved from a playbooks/ file to
  a skill, and a later commit added the five requirements the ADR
  had claimed to have and not listed. Neither contradicted it, so
  no record became false — it claimed a settledness it did not have
  for six commits, which is the weaker half of the failure and
  still the one the rule exists to prevent.
  Why it is here as well as in the close commit's body: a close body
  is read once, by whoever was at the close. This log is read top to
  bottom at the retrospective, which is the only place a second
  instance would be recognised as a pattern rather than met as a
  fresh surprise. The close body is the set's retrospective and
  keeps the account of what diverged; this entry is the fact that a
  convention was broken.
  If it recurs it is not a slip. A set whose ADRs are routinely
  settled before its last boundary is either running its ADRs too
  late or its boundaries too loosely, and the answer then is a
  change to one of them, not a third entry.
  Rejected: leaving it in the close body alone, which was the
  recommendation — the convention names that body as the set's
  retrospective, and two records of one event can drift apart. The
  user's call was that a broken rule earns a durable record where
  rules are kept. Also rejected: an entry per change set, which
  would make this log a set index; it is here because a rule was
  broken, not because a set closed.

- 2026-09-19 Three skills of this repo's own, where there was one.
  `format-comparison` split into `visual-comparison` (how a
  structure is shown — a picture, a table, a plain list) and
  `option-comparison` (any choice whose options can be built), and
  `decide-first` was added above both. ADR-0030 holds the reasoning;
  this entry is the arrangement change.
  Why the split rather than a widening: the spine is shared —
  requirements before candidates, every candidate built, judged per
  requirement, recorded in an ADR — but the middle is not. "Render
  them where they will be read" is literal for a picture and a
  figure of speech for a plan, and that act is where the discipline
  lives. A shared spine with different middles is two skills.
  Why `decide-first` at all: a change-plan is a commit plan, and
  nothing in this repo worked out *what* was being changed before
  one was opened. ADR-0029's set is the evidence — planned for six
  commits, landed at twelve, its two most confident steps undone,
  because the question "is a group a directory or a description"
  was never asked out loud.
  The registry is not touched. It lists conventions held at a pin
  (ADR-0028 decision 4), and these three are ours, pinned to
  nothing. Four directories under `.claude/skills/` are convention
  copies and three are native; the distinction is still carried by
  absence — no pin header, no manual, no registry row — which
  ADR-0028 already named as a weak signal and is now weaker at
  three.
  Rejected: registering them anyway, which would make the registry
  two lists under one heading. Also rejected: a draft template for
  `decide-first`, cut because it had never been run (ADR-0030
  decision 3 carries its trigger).

- 2026-09-19 Correction to the entry of 2026-09-18 on relative
  paths: its Rejected clause is no longer true. That entry rejected
  fixing the vendored manuals' links, on the grounds that they are
  read-only and correct where they were written, and said the
  dangle was recorded in `docs/conventions.md` instead. Both halves
  have since gone. The manuals were fixed the next day — four
  outward pointers written from the repo root, nine paths
  repointed, and 66 bare `ADR-nnnn` citations prefixed `HANDBOOK`
  because they were reading as this repo's own decisions — and
  `docs/conventions.md` was deleted, its surviving content folded
  into `docs/conventions/README.md`.
  The rule itself stands and is unchanged: a path in a document of
  this repo is written from the repo root.
  What changed under it was the premise, not the rule. "Read-only"
  came from ADR-0024 decision 5 and was retired by ADR-0025 the
  same week, which made the manuals ours; the entry was written
  against a status that had already lapsed. Worth the correction
  rather than a silent overwrite, because the log is read top to
  bottom at the retrospective and an entry that rejects what was
  later done reads as a reversal nobody noticed.

- 2026-09-19 Convention renamed: change-plans is commit-plan, and
  the four pinned copies are updated to this repo's container @
  478ecdc (were @ ba7eaa4, the handbook). First update taken from
  our own container rather than from the handbook, which ADR-0025
  made possible and nothing had exercised.
  What moved: `.claude/skills/change-plans/` is
  `.claude/skills/commit-plan/`, and `CHANGE-PLAN.md` is
  `COMMIT-PLAN.md`. Two copies were stale in ways the rename
  exposed rather than caused — commit-messages still named
  `CHANGE-PLAN.md` among the agent's own files, and
  convention-lifecycle still said "Is there newer" is answered *in
  the handbook* at `starter/kit/`, where the container has said
  *at the deliverer* since it came here. All four are now
  byte-identical to the container.
  The pin is a commit of this repo, which is new and slightly
  circular: we are the deliverer and a receiver of the same
  artifacts. It resolves cleanly enough — the container is the
  master, `.claude/skills/` holds copies of it, and "is there
  newer" is `git diff 478ecdc..HEAD -- delivery/container` — but
  the convention's language assumes two repos, and a second
  instance should say whether that assumption needs writing down
  or is harmless.
  Rejected: leaving the copies at ba7eaa4 and treating the rename
  as local. A copy at a hash that predates the rename would name a
  convention the container no longer ships, and the registry would
  be recording a fiction.

- 2026-09-19 Conventions injected: decide-first, option-comparison
  and visual-comparison, @ ee244c6 — this repo's container, which is
  also where they were written. Ten conventions held where there
  were seven; seven of the ten ship as skills, the other three as
  stubs. CBC ADR-0031 holds the reasoning.
  The entry of earlier today stands corrected by this one rather
  than by an edit: it said the three were ours, pinned to nothing,
  with no registry entry and no manual, and gave that as the shape
  to mark positively. They now have all three, and the distinction
  it described is gone — `.claude/skills/` holds seven convention
  copies and nothing else.
  A first injection with nothing to inject. convention-lifecycle §3
  takes a copy from the deliverer; here the copy and the original
  are the same file, because these were written in `.claude/skills/`
  and copied outward. The compare-first step is vacuous by
  construction rather than by luck, and is recorded as vacuous so
  the next reader does not take a clean diff for evidence that one
  was run.
  What a re-pin means for them is new and is in bundle-update.md:
  every previous delivery of this group was triggered by taking a
  handbook pin, and three of the seven now change when we change
  them.
  Rejected: registering them at `ba7eaa4` with the other four. That
  hash is the handbook's kit, which never held these files; a pin
  is a claim about where a copy came from, and theirs is here.

- 2026-09-24 `decide-first` discarded. The skill, its manual and the
  master we ship are deleted; `option-comparison` loses the two
  lines that pointed at it. Nine conventions where there were ten.
  Why: three firings, one win. The win was 2026-09-19 and what
  worked in it was one line — *can you say roughly how many commits
  this takes?* — while the seven-step method rode along. The two
  misfires produced a draft covering queued work rather than one
  unsettled shape, and seven ordered questions that were written and
  discarded. What settled that same question instead was a proposed
  ADR corrected while building, which `commit-plan` §4 and §5
  already carry. ADR-0030 recorded the thin evidence at the time:
  built on one clear instance, "thinner evidence than this repo
  usually accepts".
  Rejected: keeping the count line by moving it into `commit-plan`.
  It is a good line and it is not lost — it is in this entry and in
  ADR-0030 — but moving a sentence to keep a discard from feeling
  wasteful is how the thing being discarded grows back. If the
  question is missed in real work, that is the trigger to put it
  somewhere, and then it lands with a firing behind it rather than a
  reluctance.
  Also rejected: replacing it now with the interview shape the
  reviewer described — an agent asking the reviewer questions rather
  than drafting them alone. Not written anywhere yet, deliberately:
  it has never run, which is the mistake this entry is closing.

- 2026-09-24 `option-comparison` discarded; `visual-comparison`
  stays and stays about pictures. The skill, its manual and the
  master we ship are deleted, and the seven places
  `visual-comparison` leaned on it are rewritten so it stands on its
  own. Eight conventions where there were ten this morning.
  Why: it fired once, in the run that created it. Everything its
  findings list knows was learned either there or in a picture
  comparison. The method it carries is good and is not being
  discarded — `visual-comparison` is the same spine and has three
  firings behind it. What is discarded is a second copy of that
  spine, kept for choices that are not about showing something, of
  which one has ever come.
  The split's own test never fired: ADR-0030 decision 10 said that
  if `visual-comparison` never won a comparison whose winner was not
  a picture, the split was decoration and the two should merge back.
  ADR-0032 checked and recorded that it had not. Discarding the
  general half answers that trigger the other way — there is nothing
  to merge back into, because the specialised half was always the
  one doing the work.
  Rejected: merging the general method into `visual-comparison` and
  renaming it. That is the merge ADR-0030 anticipated, and it keeps
  every line while changing the sign on the door. Nothing asked for
  the general scope in five weeks.
  Rejected: moving its two non-picture findings into
  `visual-comparison`. They are in ADR-0030 and in git history. A
  discard that rescues its best parts is not a discard — the same
  call as the count line earlier today.
  Consequence, named rather than hidden: a choice that is not about
  showing something now has no skill. It gets decided and corrected
  while building, which is what `commit-plan` §4 and §5 carry.

- 2026-09-24 `artifact-kinds`: `guide` dropped, two exemplars
  re-anchored. Ten kinds where there were eleven.
  Why the exemplars: the manual's own rule says an exemplar names a
  document by the role it holds *for the reader*, so the word points
  at the right file from our seat and from a born project's. Two did
  not. *concept* and *model* pointed into `docs/conventions/`, which
  never ships — a run opened the vocabulary and read two examples it
  could not see. They now name `§1` of the file itself and the
  reader's own `ARCHITECTURE.md`. Raised by the reviewer asking
  whether a global dictionary misleads when the context changes; it
  did, in exactly this way, and the rule against it was already
  written.
  Why `guide` goes: an advisory how-to, no exemplar in a year, and
  no live text outside this vocabulary reaching for the word. The
  scope rule is the convention's own — a kind earns an entry only
  when its absence has caused someone to reach for the wrong word.
  Rejected: dropping `specification` with it, which is how this
  started. It has no exemplar either, and it is load-bearing:
  `docs/models/shapes.md` §2 defines a shape by what it is not, and
  *could a test verify conformance?* is the line that separates the
  two. A word can be load-bearing without ever being worn, and the
  no-exemplar test does not see that.
  Not done here: our copy is still one entry behind the master —
  the `shape` kind has been in what we ship since 2026-09-23 and has
  never reached us, because we deliver to runs and never to
  ourselves. The drift is named, not fixed.

- 2026-09-24 `artifact-kinds` discarded, and the practice it sat on
  top of becomes the rule instead. The skill, its manual and the
  master we ship go; `commit-plan` loses a `requires` line it never
  used. Seven conventions where there were ten this morning.
  Why: its purpose was that one word means the same thing to both
  parties, and it does not. The reviewer cannot use the definitions
  — "one definition has to fit all, and then I cannot tell what it
  means" — which is the whole job failing, and failing in the worst
  direction, because a word we do not share still reads as agreement
  to me.
  What replaces it was already there. Eight of ten main documents
  open with a block saying what they are and how to read them; the
  vocabulary was a second layer over a practice that works. The rule
  is that block, and two questions it answers — does ignoring this
  owe an explanation, and does it go stale — which is the only axis
  that ever decided anything (force, four citations) and the only
  distinction the records ever turned on.
  It also dissolves this morning's defect rather than patching it: a
  self-describing document needs no exemplar in someone else's repo,
  so a run points at its own.
  Five firings, and four would have gone the same way under a header
  block. The fifth is run 3 having no word for a shape and writing
  "model" plus a paragraph saying model is wrong — under the rule it
  writes what the thing is, and we read that.
  Rejected: keeping it for this repo and no longer shipping it, on
  the evidence that no run in five ever reached for the words. It
  would have kept a vocabulary one of the two readers cannot use.
  Rejected: fixing it instead — dropping the reader-mode axis, which
  has never decided anything, and cutting the file to 84 lines. Both
  were staged and both are dropped; they made an unusable thing
  smaller.

- 2026-09-24 The document rule is a shape, exposed, and this repo's
  first. `.claude/rules/document-header.md`, `paths: **/*.md`.
  Why there: it was written into `CLAUDE.md` first, and both of that
  file's own tests sent it away. Test 2 names `.claude/rules/` with a
  `paths:` list as the home for a rule that has a moment, and writing
  a document is the moment. Test 3 asks whether anything else would
  deliver it — a rules file does, automatically, where a line in the
  entry file waits to be read and followed. `CLAUDE.md` is back to
  what it was.
  Why a shape rather than a convention: `shapes-lifecycle` §1 asks
  that a shape be written from work that exists, and this one
  recurred in eight of ten documents before anyone wrote it down.
  §2 puts an exposed shape in `.claude/rules/` — exposed because
  conformance is what is wanted here, not independence.
  This is the first occupant of a directory we have shipped since
  2026-09-23 and never held, and the first test of the rule we wrote
  for other people.
  Rejected: `CLAUDE.md` carrying the rule text, which the reviewer
  asked for and which was staged. A pointer that must be read and
  followed is weaker than a file that loads itself, and the entry
  file is the one place where every added line costs every task.
  Rejected: a convention — manual, skill, shipped copy. That is the
  three-places cost this day has been spent removing.
  Corrected before the commit, on the reviewer's question: the shape
  was written with a "Where this came from" section giving its birth
  and what it replaced. That is provenance in an artifact, which
  ADR-0034 rules out — a comment says how to use a thing or what a
  part is, never what changed — and it duplicated this entry. Cut.
  The dated lines `shapes-lifecycle` §3 wants are a different thing:
  what the shape takes up as it goes, and nothing has yet.

- 2026-09-24 The document-header shape discarded, hours after it
  landed. `.claude/rules/` is empty again and nothing replaces
  `artifact-kinds`.
  Why: the reviewer's reading of the same fact, and it is the better
  one. The shape was justified by having recurred in eight of ten
  documents — but a practice that recurs eight times unprompted is
  holding itself up, and a rule describing it changes nothing except
  adding a file that loads on every `.md` touched. The recurrence
  was evidence against the rule, and it was written down as evidence
  for it.
  Item by item, as the reviewer put it: what a document is, is
  already in the document; who reads it and when is decided when
  there is a reason to decide it; and the other two are specific
  cases that arise rarely enough to be handled when they arise.
  So nothing replaces `artifact-kinds`. That is the answer, not a
  gap waiting for one — five firings in a year, all of them ours,
  and the practice that actually carried the weight was already
  running without either artifact.
  Rejected: keeping it on trial for a few weeks to see whether it
  earns its place. Everything discarded today was kept on exactly
  that reasoning, and the trial never ends by itself.

- 2026-09-26 The exchange's three artifacts of ours arrive: skills
  `exchange-read` and `exchange-deliver` under `.claude/skills/`, and
  the shape `exchange-reading.md` under `.claude/rules/` with
  `paths: temp/reading-*.md`. CBC ADR-0036, Proposed, in the commit
  plan for the exchange.
  Why skills: each has a moment that is a name the reviewer says —
  "read run 3", "deliver" — and a procedure in `installs/` is a
  document nothing loads at any moment, which is what
  `bundle-update.md` was and why its steps were skipped. As skills
  they gained a description naming the trigger and gates saying what
  must be true at the end.
  Why the shape is in `rules/`, not `shapes/`: its moment is a file
  being written, which is what `paths:` is for; `.claude/shapes/` is
  for a shape opened at a gate, and a reading has no gate. Deferred
  twice by the reviewer to "when we move"; this is the move, named
  in the plan for objection. First exposed shape anywhere; first
  occupant of this directory that stayed.
  Why the prefix: a skill called `read` sat beside a tool called
  `Read`; and the exchange is the first convention with more than
  one artifact, so its name on each ties them together in a listing.
  Rejected: a procedure file for our half (nothing loads it); a
  single skill for read, work and deliver (the work between is a
  branch-long activity with no moment to open by name); a `-shape`
  suffix or a `rules/shapes/` subdirectory (the Governs line is the
  marker by the rule we ship, and a subdirectory is a third home
  that rule does not name).
  This commit crosses the agent/project line: three moves from
  `temp/`, kept as renames so history follows the files. `temp/` is
  scratch, not a record, so the split rule's reason is untouched.
  Named in the plan.

- 2026-09-26 `convention-lifecycle` leaves this arrangement. The copy
  under `.claude/skills/` is deleted; the master and the manual left
  the delivery in the previous commit. CBC ADR-0036, Proposed.
  Why: it was the receiver's protocol — how a project takes a newer
  copy without losing its own edits — held by a repo that stopped
  being a receiver at the fork and never once ran it. Our registry
  pinned us to ourselves. Walked all six of its steps: none could
  fire here. Its one rule that applied to us, that this log lists
  the conventions held, is already a row in the entry file's
  records table. Run 3 used it heavily — eight takes, three receipt
  branches, four in-place edits — and that use continues under the
  rule that replaces it on their side, `delivered-copies.md`, built
  from their own text.
  What replaces it here: nothing of the same kind. Our side of the
  exchange is `exchange-read` and `exchange-deliver`, landed two
  commits ago, which do what a deliverer does rather than what a
  receiver does.
  Rejected: keeping the copy as a reference to what runs hold. The
  shipped file is the reference, at `delivery/container/`, and a
  second copy that nothing here can run is the drift we measured on
  09-24 — thirteen lines apart on one skill, six days on another.
  The registry entries from 09-03 through 09-20 that record this
  convention's injections and updates stand as history.

- 2026-09-26 Convention updated: commit-plan, our copy made equal to
  the master at `delivery/container/`, which gained one bullet in §4
  the commit before — the rename sweep before a close. Byte-identical
  after the copy, checked with `cmp`.
  Why: the one lesson in `bundle-update.md` with nowhere else to
  live; the moment it applies is the close of a change set, and this
  is the convention that governs that moment. Our copy follows the
  master by copying whole, the same day, because the drift between
  the two measured on 09-24 came from exactly this not happening.
  Rejected: editing our copy by hand to match. A copy is changed by
  being copied anew, here as in a run.

- 2026-09-26 `exchange-reading.md` loses its lifecycle sentences.
  The manual gained a clause in §6 the previous commit — a reading
  also closes when overtaken — and the derived list was walked. The
  two skills need nothing. The shape turned out to *restate* the
  reading's lifecycle in its first section — revised as items close,
  deleted when the work does, not a commit plan — all of which the
  manual already says. First staged as the same clause added to the
  shape; the reviewer asked what lifecycle has to do with form, and
  it has nothing. A shape says what an output looks like while it
  exists; when it opens and closes is the owning convention's.
  Removed rather than duplicated. The section keeps the path pattern
  and one line saying whose the lifecycle is.
  Why it matters beyond this file: a derived artifact *follows* its
  description, it does not *repeat* it — a copy that repeats is what
  drifts, and the maintenance rule filed this morning must say so
  when it is written. And shapes have no manual yet (`master.md`
  errata #1); when one is written, this is a line for it. Third
  firing of the rule by hand.

- 2026-09-26 Conventions updated: commit-messages, commit-plan,
  visual-comparison — our three copies made equal to the masters at
  `delivery/container/`, which gained a `foundation` field the
  commit before (`d5e7e17`, ADR-0036 decision 7). `cmp`-identical
  after the copy. The field on our own copies says *the
  commit-plan convention* and so on: a claim about what the file
  stands on, true here as in a run, because a copy is the master
  and the master says it.
  Also arrived with the copy: `visual-comparison`'s master had
  gained a lesson on 2026-09-23 — asked for a picture, this method
  is not always what is wanted — that our copy never took, thirteen
  lines apart. The 09-24 drift measurement, closed by copying whole
  rather than by editing the one line the field needed.
  Why: our `.claude/skills/` copies are downstream of the container,
  not beside it (`master.md`, what must stay true). A copy is
  changed by being copied anew, here as in a run.
  Rejected: adding the field to our copies by hand. That would have
  left the thirteen lines, and a hand edit is the drift this entry
  closes.

- 2026-09-27 Convention held: shapes (CBC ADR-0037). What this repo
  holds of it: nothing that loads. The shipped rule fires on
  `.claude/shapes/**`, and this repo has no such directory, no
  steps and no gates, so no copy of it sits here. Our shapes are
  rules with a Governs line under `.claude/rules/`, exposed, which
  is the convention's §4 — `exchange-reading.md` is the one
  instance, the exchange's artifact and this convention's instance
  at once. The reviewer moves a shape; here that means writing one
  or withdrawing it.
  Why no artifact of our own: a file saying only "we hold nothing"
  is the stub ADR-0035 dropped; the manual states our seat instead.
  Rejected: a copy of the shipped rule here for symmetry with the
  three convention skills. Those we run; this we could not, and a
  rule held by the repo it cannot apply to is the fault ADR-0036
  closed for `convention-lifecycle`.

- 2026-09-27 Copies renewed: `commit-messages` and `commit-plan`,
  copied whole from `delivery/container/` at 76f077c. What changed
  in them: the Decisions footers cite `CBC ADR-0038` by the adopted
  claim's letter where they cited `HANDBOOK ADR-nnnn`; no rule
  moved. Diffed before copying: the footers were the only lines
  apart.
  Why: a run holds no handbook, and neither, since ADR-0025, does
  this repo's text; the six decisions are adopted in ADR-0038 so a
  footer cites something its reader can open.
  Rejected: editing the footers in place. A copy is changed by
  being copied anew (the 2026-09-26 entry above).

- 2026-09-28 Convention held: conventions (CBC ADR-0039). What this
  repo holds of it: the shape of a manual,
  `.claude/rules/convention-manual.md`, loading on
  `docs/conventions/*/README.md` — ours, exposed, shipped nowhere,
  born from the pair the exchange and shapes manuals made and the
  boundary section the conventions manual needed. And the rule's
  step 2 applied to our own side: `exchange-read`,
  `exchange-deliver` and `exchange-reading.md` gain
  `foundation: the exchange convention`, which they lacked — the
  exchange manual's claim was about shipped files, and the rule for
  every description makes no such exception.
  Why: a manual written to a shape answers the seats and the
  boundary because the shape asks; the last two manuals grew the
  sections unprompted and the next writer had nothing telling them
  to.
  Rejected: holding the shape until a third manual grew the
  sections. The shapes rule's own test is a pair, and a stricter
  test for our own instance is a rule kept for symmetry.

- 2026-09-29 Derived, not copied (CBC ADR-0042). The three
  convention skills this repo holds — commit-messages, commit-plan,
  visual-comparison — are its own, each derived from its manual,
  and identical to the container's today because the manuals ask
  the same of both seats. No copy is renewed from
  `delivery/container/` again, and none of our skills or rules
  carries a pin: the "copies renewed … at <commit>" entries of
  2026-09-19 and 2026-09-27 are the last of their kind. The
  2026-09-19 entry's open question — whether being "the deliverer
  and a receiver of the same artifacts" needs writing down — is
  answered: it did, and there are two derivations, not a deliverer
  that receives from itself.
  Why: the container is the run's (CBC ADR-0038). Our PLAN and
  entry file already differ from its stubs, and a shared file
  taken for a shared job is how `convention-lifecycle` was held
  here unrun from 2026-09-03 to 09-26.
  Rejected: diverging the three skills to make the split visible —
  a change nobody needs.

- 2026-10-01 Both discards of 2026-09-24 stand, counted again. Run
  3 used both in its writing pass, 2026-09-21..23, which no reading
  had read when they were counted. `decide-first` showed its commit
  count was not yet sayable — the job of the one line its
  2026-09-24 entry credits. `option-comparison` built five wordings
  of one guarantee and caught that its labels were already there —
  a win, its first firing outside the set that made it. That makes
  four firings and two wins for `decide-first`, two and one for
  `option-comparison`.
  Why: the counts move and the reasons do not. `decide-first`'s
  wins are still its one line; `option-comparison` has one win
  outside its making, and one instance is not a method. Settled by
  the reviewer at the reading of 2026-10-01, its D2.
  Rejected: reopening either. Run 3 holds neither now, by its own
  reviewer's word, so a second instance would have to come from a
  run that reaches for the method without the skill.

- 2026-10-01 Working a reading is a rule,
  `.claude/rules/working-a-reading.md`, loading on the reading files
  beside the reading's shape. Placed from `temp/working-a-reading.md`,
  whose header said it lands once it has run twice; it ran three
  readings of run 3. The shape's four process lines moved into it,
  and the shape is form only again.
  Why: the moment it serves is a reading being worked, which is a
  reading file opened — the paths the shape already loads on. The
  shape could not hold it: a shape is form, never content
  (`docs/conventions/shapes/` §1), and this one lost its lifecycle
  once for that reason.
  Rejected: folding it into the shape — the reviewer's first pick,
  withdrawn when the conflict surfaced. A skill between read and
  deliver — it fires only when called, and a reading is worked
  across sessions. Leaving the draft — its own condition was met.

- 2026-10-01 `commit-messages` types a new agent skill or rule
  `chore(agent)`, as installing or updating one already was; ours
  follows the container's, byte-identical.
  Why: `feat` tells a release tool a user-facing capability arrived,
  and a skill under `.claude/` is detachable — no user meets it.
  Our own commits were `chore(agent)` already; the rule we shipped
  said otherwise.
  Rejected: keeping `feat(agent)` and following it here; letting our
  copy differ from the container's (CBC ADR-0042 keeps them
  derived from one manual).
