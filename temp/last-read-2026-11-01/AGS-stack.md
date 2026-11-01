# AGS-stack: Agreement, the CBC Run's side, the Stack Group

Read at `70404e1`. Four findings: 2 checked, 1 resting on the reader, 1 uncertain.

## Findings

### AGS-S1

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 1 — decide (no mechanism; the reviewer confirms)*, line 75. Also `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The decision rule*, line 76.
- **Quote:** `- **The stack evaluation.** The deciding inputs are **fluency and`
- **The other side:** `concept/03-cbc-framing.md`, *What CBC Framing produces*, line 81: `after CBC Framing, each choice answerable to the Invariant Slice` (the sentence ends on line 82: "Registry it must serve, never the other way around.").
- **The rule:** what derives from a Canonical Description agrees with it, and a disagreement is raised and decided, either side possibly wrong (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*; §5, *A disagreement*). The stack's Agent Skills are checked against concept v1 and must not contradict it (`docs/conventions/conventions/` §1.3, *The Foundation Line*).
- **What the text says:** The concept says each technology choice is answerable to the Invariant Slice Registry. The stack evaluation names only fluency and audience as its deciding inputs, and never checks the stack against the Invariant Slice Registry. app-structure line 76 goes further: "As with the stack, the Invariant Slices rarely tell structures apart." That says the Invariant Slice Registry rarely decides a stack, which is what the concept denies. Infrastructure Establishment does agree: its services are chosen "strictly from the adversity needs of the Invariant Slice Registry". Only the language and framework choice departs.
- **Which side I think is wrong:** not clear. The concept's sentence came in at `211bd0f` (2026-09-06). Its commit body says the CBC Runs recorded "the stack ... against the registry it must serve". The stack Agent Skill, imported earlier, says otherwise, and it is written from practice. Practice is the evidence (§5). The stack side may be the true one: a registry constrains the store, not the language. Then the concept's sentence should say which choices the Invariant Slice Registry decides.
- **Stands:** resting on the reader. Both lines checked in the tree; the reading of "answerable" is mine.
- **Why it was missed:** missed at a change, twice. `211bd0f` changed the concept and asserted the stack's practice without reading the stack Agent Skill (before the Change Walk existed). `c449de0` rewrote the stack evaluation, and its Foundation Check recorded "the Agent Skill against concept v1, they agree".
- **Proposed:** question: which side changes? Either (a) the stack evaluation adds a check: "the stack must serve the Invariant Slice Registry: the store's refusals and the Adversity Classes it names; among stacks that do, fluency and audience decide", and app-structure line 76 drops "As with the stack"; or (b) the concept's sentence narrows "each choice" to the choices the Invariant Slice Registry can tell apart, such as the store and the services.

### AGS-S2

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, *5. What is not in this file*, line 452.
- **Quote:** `  demands it, and the method deletes it.`
- **The other side:** `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md`, its opening note, line 7: `deliberately left open. Standing the system up is project work, not` (the sentence ends "method work.").
- **The rule:** facts-in-sync §4 and §5, as AGS-S1; and the brief's case of a stack text saying the method requires something.
- **What the text says:** The line says the CBC Bootstrap Probe crosses into `main/` "because the method demands it, and the method deletes it". The method demands no probe. System Readiness asks for a skeleton that runs and an Adversity Harness that can create the Invariant Slice's Adversity Class (READINESS-2, READINESS-4), and says standing the system up is project work, not method work. No file of the Method Group names the probe or its deletion (grep of `delivery/method/` for "Probe", "scaffold", "CBC Bootstrap": none but the Enemy Census Probe). The demand and the deletion are the cbc-bootstrap Agent Skill's own (its Stage 1 exclusion 1 and Stage 5 exit records).
- **Which side I think is wrong:** the stack line. "The method" meant the whole practice when the line was written; since the split into the Method Group and the Stack Group it names cbc-framing and cbc-slice.
- **Stands:** checked.
- **Why it was missed:** older than the Group split. The line came in at `8ed34e9` (2026-08-28); the split was `657d6eb` (2026-09-19). Missed again at `a6ccf5b`, which reworded the line and whose Foundation Check said "they agree".
- **Proposed:** fix: "the CBC Bootstrap Probe crosses into `main/`, because the CBC Bootstrap needs a door to attack, and the first Invariant Slice deletes it."

### AGS-S3

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, *4. The CBC Bootstrap Probe*, line 374 (the `ContentionProbeIT` javadoc). With it, `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *5. The adversity created*, line 240 and on.
- **Quote:** ` * Class the first Invariant Slice needs, end to end through the real`
- **The other side:** `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md`, *READINESS-4*, line 46: `Read this Invariant Slice's Invariant Slice Entry. For **the Adversity Class it`. The stack's own SKILL.md line 86 agrees with it: `  first Invariant Slice's shape, such as contention or duplicate`.
- **The rule:** facts-in-sync §4 and §5; the stack's CBC Bootstrap outcome must give what cbc-slice's Stage 0 checks.
- **What the text says:** READINESS-4 requires the Adversity Harness to create the Adversity Class this Invariant Slice names. The cbc-bootstrap SKILL.md reads the CBC Bootstrap Adversity Class from CBC Framing: contention or duplicate delivery. The harness reference says, as a general fact, that contention is "the Adversity Class the first Invariant Slice needs". The walkthrough's step 5, which carries "required outcomes", gives only a burst released at one instant. Neither names a variation point for another class. The method's own worked example has duplicate delivery as SLICE-1's Adversity Class (`delivery/method/.claude/skills/cbc-framing/references/worked-example.md` line 215). A CBC Run that follows the references there proves contention, and READINESS-4 asks for replay and injection.
- **Which side I think is wrong:** the stack's references, if they are read as generic. The javadoc may only be the latest CBC Run's fact, carried in its code.
- **Stands:** uncertain. The references say they are one CBC Run's shape, and the SKILL.md wins over them on a conflict. Whether that is enough is the reviewer's call.
- **Why it was missed:** older than the rule; carried since the import, reworded at `a6ccf5b` without its Foundation Check reading READINESS-4.
- **Proposed:** question: does the harness reference gain a variation point, "the probe's test follows the CBC Bootstrap Adversity Class; the burst is the shape for contention", and the javadoc say "contention, the Adversity Class this CBC Run's first Invariant Slice needed"?

### AGS-S4

- **Where:** `delivery/spring-postgres/docs/glossary/stack.md`, the entry *Stack Default*, line 85.
- **Quote:** `  demand or a fact about the environment defeats it: local containers`
- **The other side:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The decision rule*, line 77: `  the deciding inputs are the CBC Run's own: fluency, audience, and` (the sentence goes on: "a stated intent").
- **The rule:** the glossary's entries agree with the homes they point at (the brief's check for this file; `.claude/rules/writing.md` rule 9 sends each Name to its home).
- **What the text says:** The entry says a Stack Default holds "unless a demand or a fact about the environment defeats it", and names two homes: establishment-walk and app-structure. That is establishment-walk's rule (line 51). app-structure's rule is wider: a CBC Run may depart from the package-by-feature default for fluency, audience or a stated intent, "This CBC Run practices pattern X", with the departure logged. For the second home, the entry states a narrower rule than the home does.
- **Which side I think is wrong:** the glossary entry.
- **Stands:** checked.
- **Why it was missed:** missed at a change: `c66778e`, which wrote the entry. The entry was read against establishment-walk only; the check that should have caught it is reading the entry against each home it names.
- **Proposed:** fix: "**Stack Default** — the choice a stack's references make unless the CBC Run departs from it with a logged reason: local containers under podman, run by compose, departed from only when a demand or a fact about the environment defeats it; packages by feature, departed from by the CBC Run's own deciding inputs (…)."

## Found true, so not listed

- The Structural Wall ranking and "the store's refusal ... a right withheld" (concept 02) agree with the Database Role Split: `runtime` holds no DDL right, so DDL is refused on every path that uses it. The Behavioral Check shows it live.
- Concept 02's "every Structural Wall leaves someone unbound" agrees with postgres-setup-walkthrough §9: the identity people inspect with is decided against the Trust Assumptions, or the Invariant Slices must defend against it.
- Infrastructure Establishment chooses services and the Execution Environment from the Invariant Slice Registry's adversity needs. That agrees with concept 03's "each choice answerable".
- The CBC Framing Exports stay technology-free (concept 03). The Runtime Ground's six lines name "a service", not a store (`cbc-framing-workflow.md` line 225). infra-establish Stage 0 check 2 revises only LAYER-1-ENVIRONMENT facts, and names no store.
- The bootstrap exclusions (no table before its invariant, nothing ahead of need, the probe without business meaning) agree with concept 00's derived, feature-thin surface.
- System Readiness: READINESS-2 (runs, tests green), READINESS-3 (a real store, not mocked: a Testcontainers copy set up by the same `bootstrap.sql`) and READINESS-4 (the first Invariant Slice's class at the CBC Bootstrap, the rest at each Invariant Slice's Stage 0; establishment-walk lines 43-44) agree with the stack's outcomes. READINESS-5 is left to the first Invariant Slice, and the harness reference line 440-446 says the probe cannot fail. That agrees with READINESS-5's second paragraph.
- "The Falsifiable Promise is a property of persisted state" (cbc-bootstrap line 112), and establishment-walk line 99-100's "not properties of persisted state under adversity". Concept 02 makes the Falsifiable Promise a claim about facts the system is the authority on. For a system whose ground is a store, I read this as applying the concept, not contradicting it.
- app-structure line 46, "One package per Responsibility Area", beside the Stack Default "package-by-feature". The concept keeps Responsibility Areas, the ownership partition, apart from features, the derived surface. A system with one Responsibility Area, often the honest answer (concept 01 line 59), would get one package. Not listed: DECISION-19's Names table, question 4, decided that "problem area" is a Responsibility Area (reviewer, 2026-10-31). The reviewer may want to know the concept separates the two.
- The templates agree with what their SKILL.md and references say they hold: `bootstrap.sql` (two roles, schema, connect revoke, default privileges, `search_path` pinned for the runtime role, as `application.yaml`'s comment says); `.env.example` (the four keys of postgres-setup-walkthrough §2); `compose.yaml` (Flyway one-shot behind a profile, `name:` pinned, `:Z`); `flyway.conf` (no credentials); `verify-database-model.sql` (the four checks of postgres-setup-walkthrough §4, and connect); the two README templates.
- The other glossary entries agree with their homes.

## Met in passing

- Stale lines: `spring-boot-walkthrough.md` line 186 says "`infrastructure/bootstrap.sql`". The harness reference (line 98), the templates and postgres-setup-walkthrough §3 say `infrastructure/postgres/init/bootstrap.sql`.
- Stack-internal: `postgres-setup-walkthrough.md` lines 194-195 say a read-only identity is "made at the CBC Bootstrap beside the two". cbc-bootstrap SKILL.md line 215 sends a missing service or constraint to Infrastructure Establishment, and its app "knows one identity".
- Template gap: postgres-role-split line 62-63 claims `public` is stripped of PUBLIC privileges, "enforced, not assumed". `verify-database-model.sql` does not query it, though its header says it checks "the claims of postgres-role-split.md".
- Stack-internal: cbc-bootstrap SKILL.md never names System Readiness or its sign-off. cbc-framing SKILL.md lines 291-294 make the sign-off the gate before Invariant Slice work. The CBC Bootstrap's close hands over without asking for it.

## Not read

None. All assigned files were read whole: the 3 SKILL.md files, the 7 references, the 10 templates, `docs/glossary/stack.md`, concept chapters 00 to 04, and `system-readiness.md`.
