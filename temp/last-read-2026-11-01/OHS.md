# OHS — One home, what ships

Reader OHS. Finding Kind: One home. Files: the 62 of layer 6, at `70404e1`, each read whole; the worked example once (`cmp` shows the two copies byte-identical). Then a grep across the 62 for each fact seen twice.

Rule read first: `delivery/container/.claude/rules/one-home.md` whole, `.claude/rules/one-home.md`, and `docs/conventions/facts-in-sync/` §1, *One home*, and *The CBC Run's seat*. In a CBC Run, a retelling carries its source's id or its path, section and title. Without either it is a second home (container one-home rule 2). A summary names its owner (rule 3).

15 findings: 8 checked, 6 resting on the reader, 1 uncertain.

Line numbers are at `70404e1`. "Round 2's close read" is `d37a08f`, the last read of One home. Where a pair already stood there, `git show d37a08f:<path>` was checked.

---

## Container: the shipped glossary

### OHS-1

- **Where:** `delivery/container/docs/glossary/container.md`, the entries, lines 19-21 and 24-25.
- **Quote:** `- **Delivery Pin** — the Concept Deliverer's commit every delivered`
- **The rule:** a retelling carries its source's id or its path, section and title; without either it is a second home (`delivery/container/.claude/rules/one-home.md`, rule 2). The glossary's own header asks for "its owner where it has one".
- **What the text says:** the entries for Delivery Pin and Read-Through Commit define both numbers. `delivered-copies.md` rule 1 (lines 21-24) defines the same two, in bold, as their home. The glossary entries name no owner. The two tellings already differ: the glossary says the Delivery Pin is "kept in the Decisions Log's last delivery entry"; rule 1 says it is "taken from the Delivery Staging's name". The Delivery Take entry on line 32, by contrast, names `.claude/rules/delivered-copies.md`.
- **Stands:** checked.
- **Why it was missed:** missed at a change. The file came in at `3630ed9` (ADR-0078). The check that should have caught it is writing rule 9's "pointing at the text that defines it", or ADR-0079's bold check ("bold once ... in the file its glossary entry points at").
- **Proposed:** fix: each entry ends with its owner, "(`.claude/rules/delivered-copies.md`, rule 1)".

### OHS-2

- **Where:** `delivery/container/docs/glossary/container.md`, line 82; `delivery/container/PLAN.md`, *Legend*, line 22.
- **Quote:** `- **Plan Step Gate** — a Plan Step's exit criteria: facts that can be`
- **The rule:** as OHS-1.
- **What the text says:** the Record Stub's legend defines the Plan Step Gate in bold: "**Plan Step Gate** = exit criteria: verifiable facts, not intentions. A Plan Step is done only when every Plan Step Gate item is true." The Pure Seed's fill replaces only the text between the STEPS markers, so the legend stays in every CBC Run. The glossary retells it with no owner. Our own glossary's twin names one ("the Plan Step Form in our `PLAN.md`").
- **Stands:** checked.
- **Why it was missed:** missed at a change, `df74a6b` ("shared Names renamed and entered"). The same checks as OHS-1 apply. The bold script hit on `PLAN.md` line 22 went to the Writing readers as a rule 9 question, not as a home question.
- **Proposed:** fix: the entry ends "(`PLAN.md`, *Legend*)".

### OHS-3

- **Where:** `delivery/container/docs/glossary/container.md`, lines 29-31, 35-37, 66-67.
- **Quote:** `- **Delivery Staging** — a delivery as it arrives in `temp/`: a`
- **The rule:** as OHS-1.
- **What the text says:** OHS-1's pattern, for three more entries whose fact is stated in a shipped file:
  - Delivery Staging: `delivered-copies.md` rule 5 (lines 92-97), and `temp/README.md` lines 11-14;
  - CBC Run Ask: `delivered-copies.md` rule 4 (lines 75-90);
  - Agent Skill Template, "never edited in place": `delivered-copies.md` rule 8 (line 157).

  None carries a bold defining line there, so these rest on whether that rule is the text that defines them.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change, `3630ed9` and `df74a6b`. Same checks as OHS-1.
- **Proposed:** fix: each entry names its rule, as the Delivery Take entry does.

## Method: Output Shapes against the Agent Skills

### OHS-4

- **Where:** `delivery/method/.claude/shapes/slice-record.md`, *The Invariant Slice Record's order*, lines 31-54.
- **Quote:** `## The Invariant Slice Record's order`
- **The rule:** as OHS-1. A copy is a follower and carries a Fact Reference to its home (`docs/conventions/facts-in-sync/` §1, *One home*).
- **What the text says:** the ten sections of an Invariant Slice Record, in order, and the sentence "What spans every Invariant Slice Guarantee has its own section. What belongs to one is in its Invariant Slice Guarantee Block, and nowhere else." (line 53). `cbc-slice-workflow.md`, *The Invariant Slice Record's outline* (lines 33-73), holds the same ten sections and the same sentence (line 69). The cbc-slice Agent Skill names the workflow's outline as the home (SKILL lines 28-32). The workflow points at the Output Shape (line 39). The Output Shape never points back.
- **Stands:** checked.
- **Why it was missed:** the pair stood at `d37a08f` ("The record's order", "The slice's record — its outline"), so round 2's close read missed it. Round 3 reworded both, in `06a3915` and `8a4525b`/`6e1d55e`, and kept both tellings.
- **Proposed:** fix: the Output Shape's section opens with "The order is the cbc-slice workflow's (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The Invariant Slice Record's outline*)." It keeps its list as the follower its *What to check at a close* reads against.

### OHS-5

- **Where:** `delivery/method/.claude/shapes/registry-entry.md`, *The shape*, lines 58-63.
- **Quote:** `- **Every field is present.** An empty one says "none" (or`
- **The rule:** as OHS-1.
- **What the text says:** the Output Shape lists the Invariant Slice Entry's ten fields and the rule "every field is present". The Agent Skill Template `templates/registry.md` gives the same ten fields (lines 29-55) and the same rule (lines 57-58). Neither points at the other. The status values are stated in `cbc-framing/SKILL.md` outcome 2 (line 233) and in the template (lines 19-20). The Output Shape's "one of the Invariant Slice Registry's status values" (line 62) names neither. The two field lists already differ in their guidance. The template's *Adversity to create* says "from the Enemy Census in LAYER-1-ENVIRONMENT, not invented". The Output Shape's says "with the Enemy Fact it comes from".
- **Stands:** checked.
- **Why it was missed:** older than round 2's close read. Both lines date from 2026-10-15 (`6cfd7ad`, `b7d3448`), and round 2's close read missed them. Round 3's read met it in passing (*Met in round 3, of other kinds*) and left it for this read.
- **Proposed:** question: which is the Invariant Slice Entry's home? The template is what the CBC Run fills. The Output Shape is what the close reads against. Recommended: the template. The Output Shape's skeleton then cites `.claude/skills/cbc-framing/templates/registry.md`, and the status line cites `.claude/skills/cbc-framing/SKILL.md`, *Export and handoff*.

### OHS-6

- **Where:** `delivery/method/.claude/shapes/evidence-test.md`, *Why each rule is there*, lines 152-154; *What this document controls*, line 25; *What is exempt, and why*, lines 174-177.
- **Quote:** `- **The State Witness before the answer.** A test that fails on a status`
- **The rule:** as OHS-1.
- **What the text says:**
  - The header comment says "When a Red Run counts is the cbc-slice Agent Skill's Stage 3 ... not this Output Shape's" (lines 15-17).
  - Lines 152-154 still retell that rule's reason: a Red Run stopping on a status "has never read the store". `cbc-slice/SKILL.md` Stage 3 (lines 172-175) is its home.
  - The order "State Witness, then the Falsifiable Promise, then the invariant, then exact numbers" is told in the Agent Skill (lines 159-161) and the Output Shape (lines 101-112), with no reference.
  - The Structural Wall Check is defined in the Agent Skill (lines 194-197; the method glossary points there). The Output Shape tells it twice more, two ways: "reads the code" (line 25), and "reads the store's own list of its constraints, or ... sends the store a refusal" (lines 174-176).

  shapes-lifecycle §4 makes an Agent Skill ask for what its Output Shape names, so two tellings are by design. One of them still has to be the follower.
- **Stands:** resting on the reader.
- **Why it was missed:** the reason pair stood at `d37a08f`, so round 2's close read missed it. The Structural Wall Check lines came in at `8a4525b` (round 3's work), missed at that change.
- **Proposed:** fix: line 152's reason and lines 25 and 174 cite `.claude/skills/cbc-slice/SKILL.md`, *Stage 3 — build*. Line 25 takes the Agent Skill's wording.

### OHS-7

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, *The variation points*, item 9, lines 526-541.
- **Quote:** `9. **A body is asserted by path, never by substring.** This file`
- **The rule:** as OHS-1.
- **What the text says:** the harness reference states, as a rule decided by a CBC Run, that a body is asserted by path and never by substring. The Evidence Test Shape states the same rule for every test: "An answer's fields by their path, never by a substring" (`delivery/method/.claude/shapes/evidence-test.md` line 134). Both land in the same CBC Run. Neither points at the other.
- **Stands:** resting on the reader.
- **Why it was missed:** both stood at `d37a08f`, so round 2's close read missed them. They are in two groups, and a per-file read cannot show the pair.
- **Proposed:** fix: item 9 keeps its stack form (the test-support reader, `$.id`) and cites `.claude/shapes/evidence-test.md`, *How its assertions read*, for the rule.

### OHS-8

- **Where:** `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *Stage 2 — why*, lines 129-135.
- **Quote:** `**Why a trusted writer is not walled against.** Any path that goes`
- **The rule:** as OHS-1.
- **What the text says:** the reason a writer who can remove a Structural Wall is trusted, not walled against. `cbc-framing-workflow.md`, *Stage 2 — Name the enemies* (lines 201-211), gives the same reason where the Trust Assumptions are written: "a writer who can remove a Structural Wall cannot be walled against". The cbc-slice copy has no reference.
- **Stands:** resting on the reader. One fact, or a reason each stage needs on its own?
- **Why it was missed:** the pair stood at `d37a08f`, so round 2's close read missed it.
- **Proposed:** fix: the cbc-slice paragraph keeps its first sentence and cites `.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, *Stage 2 — Name the enemies*, for the rest.

## Stack: the cbc-bootstrap Agent Skill and its walkthrough

### OHS-9

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 4 — execute, step by step*, lines 205-211.
- **Quote:** `- Widen the build's test includes, so integration tests run under the`
- **The rule:** as OHS-1.
- **What the text says:** two bullets of Stage 4 retell outcomes the walkthrough states:
  - "extract into it, never overwrite", each hygiene file's Stack Overlay, the README kept (lines 205-208), against `spring-boot-walkthrough.md` step 2 (lines 49-58);
  - the widened test includes (lines 209-211), against step 4 (lines 192-194).

  The harness reference names the walkthrough as the owner of the second ("stated as an outcome in the walkthrough", lines 461-463). The bullet just above points at the walkthrough for "the outcomes and the traps", but it names other items and no step.
- **Stands:** checked.
- **Why it was missed:** the pair stood at `d37a08f`, so round 2's close read missed it. Round 3 rewrote both files (`c449de0`, `a6ccf5b`) and kept both tellings.
- **Proposed:** fix: each bullet ends with its step, "(`.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, step 2)" and "(… step 4)".

### OHS-10

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *The exit*, lines 296-301.
- **Quote:** `The project's records grown: the stack, the run and test commands,`
- **The rule:** as OHS-1.
- **What the text says:** the list of exit records. `cbc-bootstrap/SKILL.md` Stage 5 (lines 246-249) states the same list, as the step the agent runs: run and test commands, the Operator Manual linked, "no business behavior yet" said outright, the CBC Bootstrap Probe's deletion scheduled. The walkthrough's copy names no source.
- **Stands:** checked.
- **Why it was missed:** the pair stood at `d37a08f`, so round 2's close read missed it. Round 3's read met it in passing (*Met in round 3, of other kinds*) and left it for this read.
- **Proposed:** fix: the walkthrough's section points: "The exit records are the cbc-bootstrap Agent Skill's (`.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 5 — certify and close*)."

### OHS-11

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *1. Record the stack decision*, lines 30-39.
- **Quote:** `Before any code, an ADR carries:`
- **The rule:** as OHS-1.
- **What the text says:** what the stack decision's ADR holds. `cbc-bootstrap/SKILL.md` Stage 1 (lines 79-83) says the same, and the two lists differ:
  - the walkthrough adds the application structure;
  - the Agent Skill adds "the app knows one identity, the `runtime` role".

  Neither points at the other.
- **Stands:** resting on the reader.
- **Why it was missed:** both were rewritten at round 3 (`c449de0`, `a6ccf5b`), missed at that change.
- **Proposed:** question: which holds the ADR's contents? Recommended: the Agent Skill's Stage 1, which decides. The walkthrough's §1 keeps its trap and points there.

## Stack: infra-establish's references and infra-serve

### OHS-12

- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, lines 34-36, 72-75, 107-108.
- **Quote:** `The rule: secrets and what varies per machine are variables.`
- **The rule:** as OHS-1.
- **What the text says:** the setup walkthrough says "It owns nothing" and names the Database Role Split as its home. It still retells three rules whose home is `establishment-walk.md`, without a reference:
  - "The canonical command is `podman compose`, whatever provider stands behind it" (line 35), against the walk's Stage 1 (lines 63-64);
  - secrets as variables and decided identities literal (lines 72-75), against the walk's Stage 5 (lines 132-135);
  - expected results as comments beside each query, "so the reader needs no other doc open" (lines 107-108), against the walk's Stage 5 (lines 141-142).
- **Stands:** checked.
- **Why it was missed:** all three pairs stood at `d37a08f`, so round 2's close read missed them. Both files were rewritten at `580f7dc`.
- **Proposed:** fix: each of the three lines cites `.claude/skills/infra-establish/references/establishment-walk.md` and its Stage, or is cut to its Postgres-only part.

### OHS-13

- **Where:** `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`, *Hard lines*, lines 84-85.
- **Quote:** `3. Destructive acts need explicit confirmation.`
- **The rule:** as OHS-1.
- **What the text says:** two working rules: destructive acts need confirmation, and installs on the host are the reviewer's own acts. `infra-establish/SKILL.md`, *The rule for results* (lines 125-127), states both, with no reference either way.
- **Stands:** resting on the reader. Each Agent Skill runs alone and its reader acts on the line in place, but rule 2 still asks for the reference.
- **Why it was missed:** the pair stood at `d37a08f`, so round 2's close read missed it.
- **Proposed:** fix: infra-serve's two lines cite `.claude/skills/infra-establish/SKILL.md`, *The rule for results*.

## Our files under `delivery/`

### OHS-14

- **Where:** `delivery/installs/pure-seed.md`, opening, lines 32-40; `delivery/README.md`, *What the tree does not show*, line 73.
- **Quote:** `container itself. They hold two stances a CBC Run can only receive:`
- **The rule:** give each fact one home; elsewhere, link, or retell with a Fact Reference (`.claude/rules/one-home.md`, rules 1 and 2).
- **What the text says:** both our files state that the two composed files hold two stances a CBC Run can only receive, name the same two stances, and say nothing before the CBC Run Briefing produces them. Each cites ADR-0019, a decision citation, not a Fact Reference to a living home. Neither points at the other.
- **Stands:** checked.
- **Why it was missed:** missed at a change, `5d562d8` ("the delivery's pages meet the rule"). That commit wrote both lines in their present form; at `d37a08f` each said it differently ("the pin stance", "the pre-framing guard"). The check that should have caught it is one-home rule 6, the question at the commit.
- **Proposed:** fix: `delivery/README.md` §4 keeps the fact, as the map of what lands. The Pure Seed's paragraph points: "(`delivery/README.md` §4, *What the tree does not show*)".

### OHS-15

- **Where:** `delivery/container/.claude/skills/apply-retrospective/SKILL.md`, *Stage 1 — triage*, lines 54-55.
- **Quote:** `- **Never** history: devlog entries, closed ADRs, closed Plan Step Gates,`
- **The rule:** as OHS-1. What counts as history in a CBC Run has its home in `delivery/container/.claude/rules/one-home.md`, *Not a second home* (lines 41-45).
- **What the text says:** a second list of what is history: devlog entries, closed ADRs, closed Plan Step Gates, released CHANGELOG versions, migrations, comments. The Agent Rule's list is the devlog, closed ADRs, commit bodies, the Decisions Log's entries and released CHANGELOG entries. The two lists differ, and neither points at the other.
- **Stands:** uncertain. The Agent Skill's list may be read as what an applied row must not touch, which is wider than history.
- **Why it was missed:** the list stood at `d37a08f`, so round 2's close read missed it. The rule unclear: the rule does not say whether a list of "what not to change" is a telling of what history is.
- **Proposed:** question: does the list retell the Agent Rule's history? If so, fix: "**Never** history (`.claude/rules/one-home.md`, *Not a second home*), and with it closed Plan Step Gates and migrations".

---

## Found true, so not listed

- The worked example: byte-identical in `cbc-framing` and `cbc-slice`. The cbc-framing workflow names itself the owner and the cbc-slice workflow the follower. It is the allowed pair.
- Every Agent Skill Template header, and the four Output Shapes' header comments, retell their governing rule with its path: `delivered-copies.md` rule 8, `shapes-lifecycle.md`.
- `the-whole-system-in-plain.md` says it is a summary, names its owners, and says what to do when they disagree (one-home rule 3).
- `cbc-framing/SKILL.md`'s derivation table and Stage Exits, `cbc-slice/SKILL.md`'s Stage 0 list, and `infra-establish/SKILL.md`'s Stage Gates are summaries. Each names its owner at the file's or section's head: the workflow, `system-readiness.md` with the READINESS-n ids, and `establishment-walk.md` ("The full detail of each Agent Skill Stage"). This covers round 3's in-passing item on the Stage 2 Gate.
- The method glossary and the stack glossary: every entry names its owner file.
- `spring-harness-reference.md` says "It owns nothing" and cites the walkthrough step for each outcome.
- The kill shape's illustration, KILL-2 and KILL-4, carries the worked example's ids.
- `cbc-framing-workflow.md` rule 4 now cites the Agent Skill's *The mode*. Round 3's in-passing pair on "Every outside is written" is fixed.
- The retrospective and apply-retrospective Agent Skills' *Land it* items point at the commit-plan Agent Skill and the Plan Step Form.
- Leftovers in this kind, rechecked: G6 (`decisions.md` lines 21-22) and I5 (the default-privileges sentence, three homes) both still stand as listed.

## Met in passing

- FINDING-227's three tellings of the Infrastructure Contract's sections still stand: `infra-establish/SKILL.md` lines 110-111 and 179-189, `establishment-walk.md` lines 158-168, and a fourth at `postgres-setup-walkthrough.md` lines 225-228. DECISION-8 left them to TODO's "Rewrite the method's texts plain". That item's trigger, the refinement's close, is now due.
- `evidence-test.md`'s two descriptions of a Structural Wall Check disagree with each other (lines 25 and 174-176). This is Agreement's kind, and OHS-6 carries it.
- `cbc-slice/SKILL.md` Stage 4 item 2 gives three kinds of *Answered at close* line. `registry-entry.md` (lines 51 and 66-67) and `templates/registry.md` (lines 51-55) give one kind: Adversity Flag or judgment.

## Not read

None. All 62 files were read whole.
