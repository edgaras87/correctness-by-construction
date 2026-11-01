# DES: Dependencies, what ships (layer 6, 62 files)

Reader DES. Finding Kind: Dependencies. Read at `70404e1`, every file of
`lists/ships.txt` whole; the worked example once (`cmp` shows the two
copies byte-identical).

Rule homes read first, whole: `docs/conventions/facts-in-sync/` §1, §2,
§3.1, §3.4, *The CBC Run's seat*; `delivery/container/.claude/rules/one-home.md`
rule 2. Also exchange §3.2, §3.7, §3.8, ADR-0070, ADR-0079, DECISION-1
to 40 and both lists of the agent's calls.

13 findings: 9 checked, 4 resting on the reader, 0 uncertain.

---

**DES-1.** The rule for a shipped reference says one form, and the
shipped lines use another.

- **Where:** `docs/conventions/facts-in-sync/README.md`, §3.1 *What a
  Fact Reference is*, line 179. It weighs against 11 shipped lines in
  10 files: `delivery/container/.claude/CLAUDE.md` 40 and 60,
  `README.md` 35, `ARCHITECTURE.md` 9, `CHANGELOG.md` 18, `PLAN.md` 10,
  `TODO.md` 24, `devlog/devlog.md` 12,
  `docs/adr/0001-record-architecture-decisions.md` 41,
  `.claude/decisions.md` 28, `.claude/rules/delivered-copies.md` 163.
  Also `delivery/container/.claude/rules/one-home.md` 12–13, which
  still writes "(CBC docs/conventions/facts-in-sync/ §1, …)".
- **Quote:** "In a shipped file, a reference to this repo's text leads with CBC"
- **The rule:** §3.1, that same line: a shipped reference to this
  repo's text leads with CBC, the Repo Tag. ADR-0079's lesson: a
  decision that changes what a rule allows is not done until the
  rule says it.
- **What the text says:** DECISION-40 (2026-11-01) changed the 11
  lines from "CBC docs/…" to "the Concept Deliverer's docs/…". §3.1
  still says "leads with CBC". So the 11 lines break the rule as
  written, and `one-home.md` 12–13 keeps the old form. Two forms now
  stand in shipped files.
- **Stands:** checked (§3.1 line 179 and each of the 12 lines read in
  the tree).
- **Why it was missed:** missed at a change. DECISION-40 was fixed in
  `2fca3bf`, `8b6eec0` and `75d77e2`. No commit changed §3.1. The
  same miss ADR-0079 names for DECISION-18 and DECISION-22.
- **Proposed:** question: (a) §3.1 says a shipped reference to this
  repo's text opens with "the Concept Deliverer's", in words, and the
  container's `one-home.md` comment follows; or (b) the 11 lines take
  "CBC" back, and the container's glossary gains the Repo Tag.
  Recommended: (a). It is what DECISION-40 chose, and FINDING-1277's
  reason stands: nothing in a CBC Run says what "CBC" is.

**DES-2.** The method's Agent Skills use parts of the concept and
never say which.

- **Where:** `delivery/method/.claude/skills/cbc-framing/SKILL.md`,
  *The derivation order (not the presentation order)*, line 55. Also
  `cbc-framing/references/cbc-framing-workflow.md` *The order, and
  why it differs from the presentation*, lines 30–54; `cbc-slice/SKILL.md`
  Stage 2, lines 115–118, the Structural Wall ladder.
- **Quote:** "## The derivation order (not the presentation order)"
- **The rule:** `docs/conventions/facts-in-sync/` §3.1: a line that
  relies on a fact written elsewhere carries a Fact Reference. §4
  step 2 and ADR-0070 decision 7: a derived file's lines carry Fact
  References to their foundation too. The concept ships, at
  `docs/concept/`, so such a reference resolves in the CBC Run; it is
  not the case of *The CBC Run's seat*, where a line about our
  manuals stands alone.
- **What the text says:** the section retells
  `concept/03-cbc-framing.md` *The derivation order*, and the cbc-slice
  Agent Skill retells the ladder of `concept/02-guarantees-and-walls.md`
  *The ownership map*. Neither names the chapter. Across the method's
  Agent Skills, references and Output Shapes, `docs/concept/` appears
  in two lines (`the-whole-system-in-plain.md` 4, the workflow 106),
  and no line names a chapter's section. TODO's "Number the concept
  chapters' sections" says the same: "nothing points into a chapter's
  section today".
- **Stands:** checked (grep over `delivery/method/` and
  `delivery/spring-postgres/`).
- **Why it was missed:** older than the rule. ADR-0070 decision 7
  came on 2026-10-27; its rewrite plan named FINDING-202, 204, 216,
  219 and 220, not the method's lines on the concept. DECISION-7 and
  DECISION-8 sent the method's texts to TODO's "Rewrite the method's
  texts plain", which does not name this.
- **Proposed:** question: (a) the method's texts gain one reference
  per section that uses a chapter part (ADR-0072), such as
  (`docs/concept/03-cbc-framing.md`, *The derivation order*), as
  part of "Rewrite the method's texts plain"; the first one fires
  "Number the concept chapters' sections"; or (b) ADR-0070's trigger
  to revisit decision 7 is weighed first, since these files would
  carry a reference on most sections. Recommended: (a), in that item.

**DES-3.** The container's commit-plan retells the stop rule and
names its owner without a reference.

- **Where:** `delivery/container/.claude/skills/commit-plan/SKILL.md`,
  §6 *Review protocol*, lines 147–149.
- **Quote:** "only on the reviewer's word. The rule is the commit-messages Agent Skill's, and binds"
- **The rule:** `delivery/container/.claude/rules/one-home.md` rule 2:
  a retelling carries its source's id, or its path, section and title
  in parentheses. Without it, a retelling is a second home.
- **What the text says:** it retells commit-messages' *Rules*,
  "Commit on the word", and names the owner in prose only. Our copy
  carries `(docs/conventions/commit-messages/ §2.4, *Commit on the
  word*)` there; the container's copy drops it and points nowhere. The
  same file's §3 already points at its own commit-messages Agent
  Skill by path (line 95).
- **Stands:** checked (`diff` of the two copies: this is one of the
  three hunks).
- **Why it was missed:** missed at a change. `15f6e88` (FINDING-202)
  pointed line 95 at the CBC Run's own commit-messages Agent Skill
  and left this line. `cb3f28c` gave our copy its reference, not the
  container's. The Copies script at `075a7ff` counted the hunk as the
  seat's; it is the seat's only in which home it names.
- **Proposed:** fix: "at every commit, not only inside a Change Set
  (`.claude/skills/commit-messages/SKILL.md`, *Rules*)."

**DES-4.** Four lines send the reader to the delivered-copies Agent
Rule by name only.

- **Where:** `delivery/container/.claude/rules/shapes-lifecycle.md`
  §3 line 69, §4 line 87, §5 line 98;
  `delivery/container/.claude/skills/apply-retrospective/SKILL.md`
  Stage 4 item 3, lines 131–133.
- **Quote:** "for that part, it is changed too, under the delivered-copies Agent Rule."
- **The rule:** `docs/conventions/facts-in-sync/` §3.1: a line that
  relies on a fact written elsewhere carries a Fact Reference; a name
  in prose is not one. Container `one-home.md` rule 2.
- **What the text says:** each relies on delivered-copies rule 2 (how
  a delivered copy is edited) or rule 4 (how an edit reaches the
  Concept Deliverer), and names the Agent Rule in words. Every other
  shipped line that names this Agent Rule carries its path and rule,
  such as apply-retrospective 63–64.
- **Stands:** checked.
- **Why it was missed:** missed at a change. In shapes-lifecycle the
  three lines named `delivered-copies.md`, a whole-document
  reference, until `8b6eec0` swapped the path for the Name.
  apply-retrospective 132 was missed at `15f6e88` (FINDING-220),
  which fixed line 63 of the same file. ADR-0070 decision 8's
  question at the commit should have caught both.
- **Proposed:** fix: lines 69 and 87, and apply-retrospective 132,
  add "(`.claude/rules/delivered-copies.md`, rule 2, *A copy may be
  edited in place…*)"; line 98 adds
  "(`.claude/rules/delivered-copies.md`, rule 4, *At every Plan Step's
  close…*)".

**DES-5.** The Invariant Slice Record Shape retells which Agent Skill
Stage writes which part, with no reference.

- **Where:** `delivery/method/.claude/shapes/slice-record.md`, *An
  Invariant Slice Guarantee Block*, lines 58–62.
- **Quote:** "The Invariant Slice Guarantee Block grows by Agent Skill Stage, the cbc-slice Agent Skill's."
- **The rule:** container `one-home.md` rule 2; facts-in-sync §3.1.
- **What the text says:** Stage 1, Stage 2 and Stage 4 and what each
  adds are the cbc-slice Agent Skill's facts, at
  `.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The
  Invariant Slice Record's outline*, which the cbc-slice SKILL.md
  names as that home (lines 30–32). The Output Shape names the owner
  in words and gives no path.
- **Stands:** checked.
- **Why it was missed:** missed at a change: `8a4525b` and `6e1d55e`
  rewrote the lines into Names and Agent Skill Stages, after ADR-0070,
  and added no reference.
- **Proposed:** fix: "The Invariant Slice Guarantee Block grows by
  the cbc-slice Agent Skill's Agent Skill Stages
  (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The
  Invariant Slice Record's outline*)."

**DES-6.** Six lines name an Agent Skill's own file by its bare name.

- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`
  *Deviations*, line 132, and *Records and outputs*, line 198;
  `cbc-bootstrap/references/app-structure.md` line 22;
  `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`
  lines 3–4, "SKILL.md" twice; `infra-establish/templates/bootstrap.sql`
  lines 34 and 38, in a comment the CBC Run keeps in its filled file.
- **Quote:** "another family of constraints, may force departures from `establishment-walk.md` or"
- **The rule:** facts-in-sync §3.1: the path runs from the repo root;
  an Agent Skill names its own files the same way, since two Agent
  Skills may hold a file of the same name (ADR-0070 decision 3).
- **What the text says:** each names a file by its name alone. In a
  filled `bootstrap.sql`, "postgres-role-split.md, Naming across a
  cluster" and "verify-database-model.sql's role filter" no longer
  resolve: FINDING-207's case.
- **Stands:** checked.
- **Why it was missed:** missed at a change, each time at ADR-0070
  decision 8's question:
  - cbc-slice-workflow 3–4: `45d8974` (FINDING-219's 41 paths) left
    them;
  - app-structure 22: `63bb1db` put the file name where "the pom
    convention's" stood;
  - infra-establish 132 and 198: `1f13fee` put the file name where
    "the walk" stood;
  - bootstrap.sql 34: `7857b48`, the day `2ccaa58` fixed the same
    template's other comment; 38: `1f13fee`.
- **Proposed:** fix: each takes its path from the root:
  `.claude/skills/infra-establish/references/establishment-walk.md`;
  `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`;
  `.claude/skills/cbc-slice/SKILL.md`;
  `.claude/skills/infra-establish/references/postgres-role-split.md`;
  `infrastructure/postgres/verify-database-model.sql`.

**DES-7.** Three references to the Plan Step Form lost their path.

- **Where:** `delivery/container/.claude/skills/retrospective/SKILL.md`
  Stage 4 item 7, line 128;
  `delivery/container/.claude/skills/apply-retrospective/SKILL.md`
  Stage 4 item 7, lines 144–145;
  `delivery/container/.claude/approaches-on-trial/approach-drafting.md`
  *Stages*, §1 item 4, lines 51–52.
- **Quote:** "word (the Plan Step Form, *At the close*)."
- **The rule:** facts-in-sync §3.1: a Fact Reference is the address
  of the fact's home, (`<path>`, *<title>*); a name in prose is not
  one. Container `one-home.md` rule 2 for the CBC Run.
- **What the text says:** the reference gives a Name where the path
  goes. The Plan Step Form is `PLAN.md`'s, under its heading *The Plan
  Step Form*, in both Convention Seats; a grep for `PLAN.md` misses
  these lines.
- **Stands:** checked (both `PLAN.md` files hold `## The Plan Step
  Form`; `approach-drafting.md` is one text in both).
- **Why it was missed:** missed at a change: `84d9c41`, the Names
  pass, turned "(`PLAN.md`'s step form, *At the close*)" into "(the
  Plan Step Form, *At the close*)" and dropped the path.
- **Proposed:** fix: "(`PLAN.md`, *The Plan Step Form*, *At the
  close*)" in the two Agent Skills; in approach-drafting, "is the Plan
  Step Form's (`PLAN.md`, *The Plan Step Form*)".

**DES-8.** A Plan Step Gate item retells the commit-messages rule with
no reference.

- **Where:** `delivery/fills/cbc-run-pure-playbook.md`, *The Plan Step
  Form*, *At the close*, line 104.
- **Quote:** "- [ ] No commit straddles agent and project paths."
- **The rule:** container `one-home.md` rule 2 (the line lands in a
  CBC Run's `PLAN.md`); facts-in-sync §3.1.
- **What the text says:** it retells commit-messages' *The agent's own
  files*: a commit that touches them "touches nothing else". The items
  beside it point at their source (line 102 at
  `.claude/rules/writing.md`, line 103 at the commit-messages Agent
  Skill). This one names none.
- **Stands:** resting on the reader (that a Gate item counts as a
  retelling).
- **Why it was missed:** older than the rule: `0cdc50c`, 2026-10-16,
  before ADR-0070.
- **Proposed:** fix: "- [ ] No commit straddles agent and project
  paths (`.claude/skills/commit-messages/SKILL.md`, *The agent's own
  files*)."

**DES-9.** The Pure Seed points at a devlog entry for a fact the Agent
Model holds.

- **Where:** `delivery/installs/pure-seed.md`, the paragraph after the
  prompt, lines 257–260.
- **Quote:** "reviewer is present (devlog 2026-09-06, "the pure seed runs")."
- **The rule:** facts-in-sync §3.1: a Fact Reference has one target,
  the home of the fact its line relies on. §1: history is not a first
  home either.
- **What the text says:** "an agent pressed to finish skips a stop
  written only in a file" is stated in Living Text at
  `docs/models/agent.md` §5, *The context window*: "a rule that rests
  on a fact of the session cannot live in a file alone. Such a fact
  is, for example, that a reviewer is present". The line points at
  the devlog, which is history.
- **Stands:** checked.
- **Why it was missed:** older than the rule (ADR-0070 decision 6);
  kept when `5d562d8` and `a456f4c` rewrote the paragraph.
- **Proposed:** fix: "(`docs/models/agent.md` §5, *The context
  window*)". The devlog entry may stay beside it as the story.

**DES-10.** "A CBC Run on another stack takes no Stack Group" points
at a summary and at an ADR, not at its home.

- **Where:** `delivery/README.md` §5 *What a CBC Run does not get*,
  lines 84–85; `delivery/installs/pure-seed.md` step 4, the comment at
  lines 144–145.
- **Quote:** "also takes no `spring-postgres/` (`ARCHITECTURE.md` §2.2, *The Stack Group*)."
- **The rule:** facts-in-sync §3.1: one target, the fact's home. §2:
  a convention's subject is stated in its manual; `ARCHITECTURE.md`
  points.
- **What the text says:** the fact's home is
  `docs/conventions/exchange/` §3.4, *One group per file*: "a CBC Run
  on another stack takes the Container Group and the Method Group and
  leaves the Stack Group (ADR-0029)". `delivery/README.md` points at
  `ARCHITECTURE.md` §2.2, which restates it. The Pure Seed cites only
  ADR-0029, the why.
- **Stands:** checked.
- **Why it was missed:** `delivery/README.md` 85 is older than the
  one-target line (round 2's rule plan, 2026-10-25); its reference
  dates from `37e4005`. The Pure Seed's comment was rewritten at
  `a456f4c` and kept the bare citation.
- **Proposed:** fix: both lines take "(`docs/conventions/exchange/`
  §3.4, *One group per file*)"; the Pure Seed keeps ADR-0029 beside
  it. That `ARCHITECTURE.md` §2.2 restates the fact is for the One
  home reader of ours.

**DES-11.** The Pure Seed points at "the delivered Agent Skills" for the
commit-scope rule, with no path.

- **Where:** `delivery/installs/pure-seed.md`, after the prompt, lines
  270–272.
- **Quote:** "central data. The commit-scope rule is not restated. It is in the"
- **The rule:** DECISION-3: every pointer in Living Text carries its
  path; facts-in-sync §3.1.
- **What the text says:** the rule is commit-messages' *The agent's
  own files*. The line names "the delivered Agent Skills", plural and
  with no path, so a change to that section finds no line here.
- **Stands:** resting on the reader (whether the line relies on the
  rule or only says the prompt does not).
- **Why it was missed:** missed at a change: `5d562d8` rewrote the
  paragraph, after ADR-0070.
- **Proposed:** fix: "It is the commit-messages Agent Skill's
  (`delivery/container/.claude/skills/commit-messages/SKILL.md`, *The
  agent's own files*), and the prompt only points at it."

**DES-12.** Two shipped lines give a Name in parentheses where a path
goes.

- **Where:** `delivery/fills/cbc-run-pure-playbook.md`, Step 1's
  comment, line 156; `delivery/method/.claude/shapes/evidence-test.md`,
  *How its assertions read*, lines 146–147.
- **Quote:** "(the cbc-framing Agent Skill). The README purpose paragraph and the devlog's"
- **The rule:** facts-in-sync §3.1: a name in prose is not a Fact
  Reference; the form is a path, section and title.
- **What the text says:** the playbook's comment relies on where the
  CBC Run Briefing is committed, the cbc-framing Agent Skill's fact.
  The Output Shape's "(the worked example's Runtime Ground)" relies on
  the worked example's numbers. Both name the source and give no path.
- **Stands:** resting on the reader (a comment and an Illustration
  line may be judged too small to need one).
- **Why it was missed:** older than the rule; the Names pass
  (`a456f4c`, `8a4525b`) rewrote the words and kept the form.
- **Proposed:** fix: "(`.claude/skills/cbc-framing/SKILL.md`, *The
  record…*)"; "(`.claude/skills/cbc-framing/references/worked-example.md`,
  *Stage 2 — Name the enemies…*)".

**DES-13.** The Local Map retells what goes only once, with no
reference, beside a bullet that has one.

- **Where:** `delivery/README.md` §2 *Three ways a file lands*, the
  first bullet, lines 26–29.
- **Quote:** "are the CBC Run's from then on. They are never delivered again."
- **The rule:** `.claude/rules/one-home.md` rule 2: a retelling carries
  a Fact Reference to its source, or it is a second home.
- **What the text says:** what is copied once and never delivered
  again is `docs/conventions/exchange/` §3.2, *What goes*, its last
  paragraph, and §2.4, *The records' exception*. The second bullet
  carries (`docs/conventions/exchange/` §3.2, …); the first carries
  none.
- **Stands:** resting on the reader (whether "where each part lands"
  is the Local Map's own subject).
- **Why it was missed:** missed at a change: `5d562d8` and `a456f4c`
  rewrote the bullet after ADR-0070.
- **Proposed:** fix: end the bullet with "(`docs/conventions/exchange/`
  §2.4, *The records' exception*)".

---

## Found true, so not listed

- Every *Decisions* footer in a shipped Agent Skill, Agent Rule or
  Approach on Trial is the file's last part, under `---`, and the Pure
  Seed's regex strips it in steps 2 and 4. No ADR is cited anywhere
  else in a shipped file but the commit-messages examples and the
  CBC Run's own ADR-0001.
- No Agent Skill Template or Record Stub cites a decision (§3.4 item
  6). Each template header points at delivered-copies rule 8 by path.
- The 11 DECISION-40 lines each name a section with its title, and
  each line says in its own words what the CBC Run needs.
- CBC Run ids are bare (SLICE-1 GUARANTEE-1, READINESS-5, KILL-2), as
  *The CBC Run's seat* allows; cbc-slice's READINESS-1 to 6 retell
  `system-readiness.md` beside their ids.
- Every other line that names delivered-copies or shapes-lifecycle
  carries its path and rule or section; every cross-Agent-Skill pointer runs from the
  root.
- The worked example's copies are byte-identical, and each workflow
  says which owns it.
- The CBC Runs' evidence counts in the workflows (DECISION-40), the
  container's `writing.md` and `one-home.md` naming our manuals
  (DECISION-3), and approach-drafting's line for the Concept Deliverer
  (FINDING-221) are settled.
- `spring-harness-reference.md`'s "(walkthrough, step 4)" lines sit
  under a header that names the walkthrough by path (ADR-0072).

## Met in passing

- `delivery/README.md` line 5: "`ARCHITECTURE.md`'s (§2, *The
  delivery and the CBC Runs*)" uses the same-document form for
  another file. By §3.1 it reads as `delivery/README.md` §2. Wiring.
- 15 shipped references quote a numbered rule's bold lead whole past
  30 characters, such as "*An Agent Skill Template is copied and
  filled, never edited in place*"; §3.1 cuts it to 30 with "…". Two
  more, `cbc-framing-workflow.md` 112 and `cbc-slice/SKILL.md` 96,
  give "rule 6" with no lead. Wiring.
- The leftovers G6 and I5 still stand as written.

## Not read

None.
