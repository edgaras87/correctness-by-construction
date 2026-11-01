# SL4: Stale lines, the method and the stack (34 files)

Reader SL4. Finding Kind: Stale lines. Tree at `70404e1`. All 34 files read whole. The worked example was read once: `cmp` shows the two copies are byte-identical.

Five findings: 3 checked, 2 resting on the reader, 0 uncertain.

## Findings

### SL4-1

- **Where:** `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*, line 51.
- **Quote:** `and recorded in the record the records table names for sign-offs. Delegation changes who`
- **The rule:** a false line is wrong. No rule is needed.
- **What the text says:** the line says a CBC Run's records table names a record for sign-offs. The container's table (`delivery/container/.claude/CLAUDE.md`, *Records*) has 12 rows, and none of them names sign-offs. The same SKILL, in *The record*, line 178, gives CBC Framing's verdicts one home: "inline in the CBC Framing Derivation". So the line points at a row that does not exist.
- **Stands:** checked.
- **Why it was missed:** missed at a change. Commit `ce370e4` (2026-11-01) replaced "where the records put sign-offs" with a claim about the records table. Its Foundation Check read concept v1 only. Nothing checked the new claim against the container's records table.
- **Proposed:** fix: "and recorded inline in the CBC Framing Derivation, as *The record* says. Delegation changes who"

### SL4-2

- **Where:** `delivery/method/.claude/shapes/evidence-test.md`, *What this document controls*, line 25.
- **Quote:** `a Structural Wall Check, which reads the code;`
- **The rule:** a false line is wrong. No rule is needed.
- **What the text says:** the line says a Structural Wall Check reads the code. Three other texts describe it differently:
  - the cbc-slice SKILL's Stage 3 step 5, lines 194-197, and the method glossary, lines 225-227: it sends a Structural Wall its refusal directly, or reads it where it is defined;
  - this Output Shape's own *What is exempt, and why*, lines 174-177: it reads the store's list of its constraints, or sends the store a refusal;
  - the worked example, lines 301-303: its Structural Wall Check is a second row written straight to the store and refused.

  None of these reads the code.
- **Stands:** checked.
- **Why it was missed:** missed at a change. The line began as "a structural test, which reads the code" (`31d8a78`, 2026-10-15). `8a4525b` (2026-11-01) put the Name Structural Wall Check in its place and kept the old description. Nobody read the Name's glossary entry beside the line.
- **Proposed:** fix: "a Structural Wall Check, which sends a Structural Wall its refusal directly or reads it where it is defined, and is not evidence;"

### SL4-3

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *4. The Adversity Harness*, *The Adversity Harness in the codebase*, line 186.
- **Quote:** `` `infrastructure/bootstrap.sql` the Runtime Ground uses; ``
- **The rule:** a false line is wrong. No rule is needed.
- **What the text says:** the line puts the Runtime Ground's `bootstrap.sql` at `infrastructure/bootstrap.sql`. Every other file puts it at `infrastructure/postgres/init/bootstrap.sql`:
  - the template's own path line (`infra-establish/templates/bootstrap.sql`, line 5);
  - the compose mount (`compose.yaml`, line 21);
  - `.env.example`, line 15;
  - the setup walkthrough's §3, line 79;
  - `spring-harness-reference.md`'s `DatabaseIT`, line 98, and its javadoc, line 85.

  A CBC Run that follows this line mounts a file that is not there.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `a6ccf5b` (2026-11-01) rewrote "the same bootstrap SQL the ground uses" and added the wrong path. The Wiring script skips a CBC Run's own paths, and the rewrite was not checked against the templates.
- **Proposed:** fix: "`infrastructure/postgres/init/bootstrap.sql` the Runtime Ground uses;"

### SL4-4

- **Where:** `delivery/method/.claude/skills/cbc-framing/templates/registry.md`, the SLICE-1 entry, *Answered at close*, line 52. The same claim is in `delivery/method/.claude/shapes/registry-entry.md`:
  - lines 51-53, the shape;
  - lines 66-67, the skeleton;
  - lines 111-112, the check, question 4.
- **Quote:** `Then one line per Adversity Flag or judgment it settled: the answer`
- **The rule:** a false line is wrong. No rule is needed.
- **What the text says:** the Agent Skill Template and the Invariant Slice Entry Shape say *Answered at close* holds one kind of line: each Adversity Flag or judgment the Invariant Slice settled. The cbc-slice SKILL asks for three kinds:
  - Stage 4 step 2, lines 227-230: "what the Invariant Slice left provisional; what it hands to later Invariant Slices, by name; each Adversity Flag or judgment it settled";
  - Stage 4 Gate 1, lines 248-250: "what it left provisional and what it hands on, one line each".

  An entry filled by the template and passed by the Output Shape fails the Agent Skill's Gate.
- **Stands:** resting on the reader, for which side is wrong. Checked that the three files differ.
- **Why it was missed:** missed at a change. The SKILL's three kinds came in with `2674c03`, and the Output Shape with `6cfd7ad`, both on 2026-10-15. The Output Shape was written without being read against Stage 4. The template's slot was never changed.
- **Proposed:** question: are provisional items and hand-ons lines under *Answered at close*? Recommended: yes, as the SKILL says. The template's slot, the Output Shape's field, its skeleton bullet and check question 4 then name all three kinds.

### SL4-5

- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`, *4. Land the Catalog Check*, lines 99-105.
- **Quote:** `It queries the catalog against the Database Role Split's claims:`
- **The rule:** a false line is wrong. No rule is needed.
- **What the text says:** the list after this line names 4 checks:
  1. roles;
  2. database and schema owners;
  3. schema privileges;
  4. default privileges.

  The template it names, `templates/verify-database-model.sql`, runs 6 sections. Number 6, "Connect privilege — access by grant, never by default", checks `bootstrap.sql`'s REVOKE CONNECT, and the list leaves it out. `postgres-role-split.md`, lines 92-94, makes the connect revoke a claim of the Database Role Split.
- **Stands:** resting on the reader, on whether a partial list reads as the whole. Checked: the template has 6 sections and the list has 4 items.
- **Why it was missed:** missed at a change. The list was a run-on sentence of four items before `580f7dc` (2026-11-01), and the template already held section 6 at `657d6eb`. `580f7dc` made the list a numbered one without checking it against the template.
- **Proposed:** fix: add a fifth item, "5. who may connect to the database: the two roles by grant, PUBLIC not at all."

## Found true, so not listed

- Every Fact Reference into the container lands, with its number and title:
  - `delivered-copies.md` rule 8, *An Agent Skill Template is copied and filled, never edited in place*;
  - `shapes-lifecycle.md` §1, §2 and §3;
  - `writing.md` rule 6.
- The workflows' sections that the SKILLs cite exist: *The Invariant Slice Record's outline*, *Standing Guards*, *Export and handoff*, *The mode — non-negotiable* and *Records and outputs*.
- The method glossary's homes exist. Concept chapters 00 to 04 exist, and chapter 00's *How it fails* lists the four failures in the glossary's order. The counts hold:
  - System Readiness has 6 checks;
  - there are 4 Enemy Census Audit questions and 3 Enemy Census Probe Stamps;
  - there are 3 Standing Guards.
- The worked example agrees with itself, and with the Output Shapes' illustrations:
  - 6 Enemy Facts, 3 System Possessions, 3 System Refusals and 3 Scope Exclusions;
  - 6 Enemy Collision Kills become 2 Invariant Slices and 1 Invariant Slice Fold;
  - KILL-2 and KILL-4 are word for word as in `kill.md`;
  - SLICE-1's entry, GUARANTEE-1 and EVIDENCE-1 to EVIDENCE-3 match `registry-entry.md` and `slice-record.md`;
  - fifty racers and ten thousand orders match the Runtime Ground.
- cbc-bootstrap's 5 Plan Steps match the walkthrough's §1 to §5. The SKILL's "the walkthrough's step 3" and "step 5" land on the secret trap and the cross-process proof. The harness reference's variation points 8 and 9 exist, and so do the walkthrough's trap items 1 to 4.
- The image versions agree: `postgres:17` and `flyway:11` in `compose.yaml`, as the harness reference says. The localdev literals agree across `.env.example`, `bootstrap.sql` and `DatabaseIT`.
- The container's `README.md` has no Prerequisites, Run or Test section. Its hygiene files carry the Stack Overlay marker. Its `ARCHITECTURE.md` has *Components* and *Invariants*. Its records table sends "what an Invariant Slice may rely on" to `ARCHITECTURE.md`.
- ADR-0008 and ADR-0013, cited in the footers, exist.
- The cbc-framing workflow's counts of CBC Framings and Responsibility Areas match what commit `3be745a` says it took from our records.

## Met in passing

- `evidence-test.md` line 122 quotes SLICE-2's invariant as "a retry after a crash ends in one order and one truthful answer". The worked example, lines 218-219, words it "a crash at any point leaves the system where a retry ends in exactly one order and one truthful answer". The meaning is close, but the quote is not the source's words.
- The leftover list marks I3, the Catalog Check named three ways, as gone. That holds in substance: the three names, "the Database Role Split's claims", "the reference's claims" and "the claims of postgres-role-split.md", now all point at one file.
- `cbc-slice/SKILL.md` line 225 says the Invariant Slice Entry "went to `in-progress` when the Correctness Specification landed". No Stage 1 step tells the agent to set it.

## Not read

None.
