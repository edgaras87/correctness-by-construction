# Reader WI: Writing, the Stack Group

Finding Kind: Writing, rules 1 to 10. Files: the 20 in `lists/wi.txt`,
read whole at `70404e1`; the yaml, sql, properties and conf templates
by their comments. Read first: the Writing row of the last read's
rules' check, `.claude/rules/writing.md`, the writing manual §2,
`refinement.md` §2.4 and §2.5, DECISION-16 to DECISION-40 and both
lists of the agent's calls, ADR-0079, the leftovers, the three
delivered glossaries, and reader I's close-read findings FINDING-1365
to 1410 (in git at `b8c7d99`).

10 findings: 4 checked, 4 resting on the reader, 2 uncertain.

## Findings

**WI-1.** rule 9; checked.
- **Where:** `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md`, *Stage 0 — the Runtime Ground stands?*, lines 31-32.
- **Quote:** "Check the original evaluation. If the wanted service is **an"
- **The rule:** a Name is bold once, at the line that defines it, and nowhere else; a list item's bold lead may begin with one (`.claude/rules/writing.md` rule 9; the container's copy, the one a CBC Run holds, says the same; ADR-0079 decisions 1 and 2).
- **What the text says:** "**an Infrastructure Service Exclusion,**" is bold inside a sentence. It is not a list lead. The Name's home is `infra-establish/SKILL.md` (`docs/glossary/stack.md` line 52), not this file.
- **Why it was missed:** missed at a change. `78fe685` turned "**on the not-provisioned list**" into the bolded Name, after DECISION-22 had been taken. FINDING-1384 then listed the bold Names away from their homes, and did not list this one.
- **Proposed:** fix: "Check the original evaluation. If the wanted service is an Infrastructure Service Exclusion, the new need must answer the old" (bold dropped; line 32's "Infrastructure Service Exclusion,**" loses its closing marks).

**WI-2.** rule 9; checked.
- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *The Agent Skill Stages and their Gates*, line 76 (drawing), with the key at lines 68-71.
- **Quote:** "                 stood up)       exclusions)     enforcement)     recorded)"
- **The rule:** rule 9 reaches drawn text. A drawing writes the Name where its box has room; where it has not, one line above says which short word stands for which Name (DECISION-21).
- **What the text says:** the box for Stage 2 says "exclusions", the short form of Infrastructure Service Exclusion. The key above the drawing names environment, services, constraints and contract, and not exclusions.
- **Why it was missed:** missed at a change. `1f13fee` added the key for FINDING-1410, and that finding named only four of the drawing's short words.
- **Proposed:** fix: the key reads "In the drawing, environment is the Execution Environment, services the Infrastructure Services, exclusions the Infrastructure Service Exclusions, constraints the Infrastructure Service Constraints, and contract the Infrastructure Contract and the Operator Manual."

**WI-3.** rule 9; checked.
- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, the Stage 3 heading, line 93.
- **Quote:** "## Stage 3 — Name each Infrastructure Service's constraints, the reference first"
- **The rule:** a defined thing is written by its Glossary Name, exactly (rule 9). An Agent Skill Stage heading is outside rule 10, not outside rule 9.
- **What the text says:** "each Infrastructure Service's constraints" splits the Name Infrastructure Service Constraint into a possessive and a lowercase word. The section's own first line writes the Name whole.
- **Why it was missed:** missed at a change. FINDING-1379 wrote the Name whole at the walk's other uses (lines 106, 116, 121), "the same at each line"; `1f13fee` did not reach the heading. No Fact Reference names this heading (grep), so the rename grep has nothing to fix.
- **Proposed:** fix: "## Stage 3 — Name the Infrastructure Service Constraints, the reference first"

**WI-4.** rule 8, rule 9; resting on the reader.
- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md`, *Inputs, before Stage 0*, line 20.
- **Quote:** "is not settled, the step is not ready: stop (Stage 0 in `.claude/skills/infra-establish/SKILL.md`)."
- **The rule:** start from what the reader holds (rule 8); a lowercase word is English and only English (rule 9).
- **What the text says:** "the step" names nothing this file has introduced. The file speaks of Agent Skill Stages and Infrastructure Establishment. In a CBC Run, "step" also reads as the Plan Step that runs this work, a Name written short.
- **Why it was missed:** missed at a change. `580f7dc` (round 3's work) wrote the line, and round 3's close read did not list it.
- **Proposed:** fix: "is not settled, Infrastructure Establishment is not ready: stop (Stage 0 in `.claude/skills/infra-establish/SKILL.md`)."

**WI-5.** rule 9; resting on the reader.
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, *Stage 2 — write the CBC Bootstrap Requirements*, line 153.
- **Quote:** "- §3 the constraints, each **by reference** to the ADR or contract"
- **The rule:** a defined thing is written by its Glossary Name; a lowercase word is English and only English (rule 9).
- **What the text says:** "contract" here is the Infrastructure Contract: Stage 1, line 118, says the constraints are "cited against the Infrastructure Contract". The same Agent Skill also uses "the contract" in its English sense, at line 43, for the CBC Bootstrap Requirements. So the reader must decide at each use which one is meant, which is what rule 9 prevents.
- **Why it was missed:** older text. `c449de0` (round 3's work) reworded the line and kept the word. Round 3's read and its close read did not list it.
- **Proposed:** fix: "- §3 the constraints, each **by reference** to the ADR or the Infrastructure Contract"

**WI-6.** rule 8, rule 6; uncertain.
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *The Adversity Harness in the codebase*, line 172.
- **Quote:** "  would undo step 3's claim. On Boot 4 the engine enters, not Boot's"
- **The rule:** start from what the reader holds (rule 8); a number is written so the reader knows its owner (rule 6).
- **What the text says:** "step 3" meant this walkthrough's §3, *Wire the runtime datasource*, as it did when the line was first written (`4566cb6`). Now a numbered list ends one line above it, and its item 3 is "run migrations on the Adversity Harness's side". A reader takes "step 3" as that item. The harness reference says the same fact plainly: "it would undo the datasource's claim that the application cannot migrate" (`spring-harness-reference.md` line 155).
- **Why it was missed:** missed at a change. `a6ccf5b` turned the capabilities into a numbered list under rule 3, and left "step 3" beside its new item 3.
- **Proposed:** fix: "would undo step 3's claim, *Wire the runtime datasource*: the application cannot migrate." Or, as the harness reference writes it: "would undo the datasource's claim that the application cannot migrate."

**WI-7.** rule 3; checked.
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, *Recall list — the traps compressed*, lines 307-308, 315, 317 and 319.
- **Quote:** "6. Ryuk stays on under rootless podman on 2.x; `ryuk.disabled` in the"
- **The rule:** give each part its own line or label; don't chain the parts with dashes and semicolons (rule 3).
- **What the text says:** four items still chain two facts with a semicolon:
  - item 2: the restclient trap; the `@AutoConfigureTestRestTemplate` trap;
  - item 6: Ryuk stays on; the old key has no effect;
  - item 7: no dummy baseline; the history table exists anyway;
  - item 8: Flyway is the Adversity Harness's only; at runtime scope it undoes the constraint.
- **Why it was missed:** missed at a change. FINDING-1405 asked for one fact per sentence in this list, named items 2 and 6 among others, and was taken as proposed. `63bb1db` took out the dashes and left the semicolons in items 2 and 6. Items 7 and 8 were not named.
- **Proposed:** fix: a full stop at each: "`RestTemplateBuilder`. `@AutoConfigureTestRestTemplate` is required:"; "Ryuk stays on under rootless podman on 2.x. `ryuk.disabled` in the properties file has no effect."; "No dummy baseline migration. The history table is created by a run with no migrations."; "Flyway is the Adversity Harness's only. At runtime scope it undoes the Runtime Ground's constraint."

**WI-8.** rule 3; checked.
- **Where:** template comments in the Stack Group, 7 lines in 5 files:
  - `infra-establish/templates/bootstrap.sql` lines 30 and 67;
  - `infra-establish/templates/compose.yaml` line 42;
  - `infra-establish/templates/flyway.conf` line 5;
  - `infra-establish/templates/verify-database-model.sql` lines 18 and 85;
  - `cbc-bootstrap/templates/readme-run-test.md` line 40, a comment in the bash block that lands in a CBC Run's README.
- **Quote:** "--   Identities, schema, and privilege boundaries only — no tables, no"
- **The rule:** don't chain parts with dashes and semicolons (rule 3). The rule covers comments (`.claude/rules/writing.md`, *Governs*), and FINDING-1406's fix, "a colon or a full stop at each", was taken for these templates.
- **What the text says:** each line joins its parts with a dash, and bootstrap.sql 30-31 and readme-run-test.md 40 add a semicolon. FINDING-1406 named the other dashes in these templates, and those are fixed; these 7 were never named.
- **Why it was missed:** missed by round 3's close read: FINDING-1406's "also" list left these 7 out, and `1f13fee` fixed what it listed.
- **Proposed:** fix, a colon or a full stop at each:
  - bootstrap.sql 30-31: "Identities, schema, and privilege boundaries only. No tables, no application objects: those arrive solely through the migration tool.";
  - bootstrap.sql 67-69: "search_path: where unqualified names resolve. It is pinned so migrations and application statements land in the governed schema, never in public. It is a default for convenience. The authority boundary is the grants above.";
  - compose.yaml 42: "# bare name: compose prefixes the pinned project name";
  - flyway.conf 5: "# Flyway: the only DDL path, per the CBC Run's Infrastructure Service Constraints.";
  - verify-database-model.sql 18: "Expected results are comments beside each query, so this file needs no other document open.";
  - verify-database-model.sql 85: "empty-string role, oid 0) f: bootstrap.sql's REVOKE CONNECT, checked";
  - readme-run-test.md 40-42: "# the one standard test command: unit and integration tests together. Integration tests drive a real throwaway PostgreSQL (Testcontainers, rootless podman), so the Runtime Ground does not need to be up".

**WI-9.** rule 2, rule 7; resting on the reader.
- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/templates/bootstrap.sql`, the comment above `CREATE ROLE`, lines 33-35.
- **Quote:** "-- cluster, the Database Role Split named above (roles are cluster-wide)."
- **The rule:** short sentences, one idea each (rule 2); cut what adds nothing (rule 7).
- **What the text says:** one sentence chains a path, a section title with no mark, a gloss and a parenthesis: "Prefixed names are the shared-cluster case of postgres-role-split.md, Naming across a cluster, the Database Role Split named above (roles are cluster-wide)." "Named above" first pointed back at "the model", the reference named in *Purpose*. Now the line just before names the Database Role Split, so the gloss repeats it.
- **Why it was missed:** missed at a change. `1f13fee` replaced "the model" by the Name in place (FINDING-1373), and the sentence's shape stayed.
- **Proposed:** fix: "-- the two identities of the Database Role Split. Prefixed names are the shared-cluster case, since roles are cluster-wide (postgres-role-split.md, Naming across a cluster)."

**WI-10.** rule 5; uncertain.
- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md`, *The Stack Default*, line 53; also lines 27-28 "structural depth earned per feature" and line 57 "own complexity earns it".
- **Quote:** "- **Depth is earned per feature, never stamped.** A feature starts"
- **The rule:** plain words, not metaphor: say what happens (rule 5).
- **What the text says:** "earned" and "stamped" say, by figure, that classes are added when a feature needs them and not laid out from a template. FINDING-1409 counted "and it earned that", in this file's line 120, as a figure, and it was dropped. "Stamp" is also the base of a method Name, the Enemy Census Probe Stamp. DECISION-26 judged neither word.
- **Why it was missed:** older text (`6385564`). FINDING-1409 named a fourth use and not these three.
- **Proposed:** question: are "earned" and "stamped" dead figures here? If not: "- **Depth grows per feature, by need, never from a template.**"; lines 27-28 "structural depth added per feature, by need"; line 57 "when that feature's own complexity needs it".

## Found true, so not listed

- **The script hit,** `infra-establish/SKILL.md` line 3 "infrastructure establishment": it is a quoted user phrase in the description. DECISION-37 keeps the Names out of these phrases. The same goes for "stand up the ground", "the framing is done" and infra-serve's "the new slice needs X".
- **Numbered titles:** all 22 in the 20 files are 30 characters or fewer, one phrase, with no gloss, and stand alone. Glosses after a dash or a parenthesis sit only on unnumbered headings and Agent Skill Stage headings, which DECISION-20 and rule 10 leave out.
- **Bold Names:** away from their homes, only WI-1 is left. The other bold Names are list leads (ADR-0079 decision 2), at their home (Catalog Check, Behavioral Check, Infrastructure Contract and Operator Manual in `infra-establish/SKILL.md`; Stack Default and the three Names in `establishment-walk.md`; the Database Setup Identity), or the glossary's entries.
- **Every capitalized phrase** in the 20 files is a Name in one of the three delivered glossaries, a label or a product name (Spring Modulith, Spring Initializr).
- **FINDING-1365 to 1410's fixes stand in the tree,** but for WI-2, WI-3, WI-7 and WI-8, each a fix that reached part of its lines.
- **Semicolons joining two halves of one contrast** were left, as round 3 and its close read left them: "the order is load-bearing; the commit split is judgment" and others like it, the glossary entries' second clause, and the Agent Skill Template header's "Copy … and fill; the filled file is the CBC Run's own" (DECISION-29's header form).
- "load-bearing", "lands", "door", "honest" of a reason, not of a file: kept by DECISION-26. "the copy" in the harness reference is defined at line 45, as FINDING-1390 kept it.
- The "Gate:" leads in `cbc-bootstrap/SKILL.md` and "The Agent Skill Stages and their Gates": labels inside their owner (ADR-0079, FINDING-1388).
- "Spring pom convention", the reference's title: FINDING-1392's proposal kept the file's name.

## Met in passing

- Leftover I9 (the drawing's Stage 6 says "contract" while its Gate asks for both manuals) looks gone: the key `1f13fee` added says "contract the Infrastructure Contract and the Operator Manual".
- `verify-database-model.sql` lines 36, 63 and 83: the `\echo` headings the operator sees carry a gloss after a dash ("Database ownership — stays above the split"). They are output text, not a numbered section, so no rule I read covers them.
- `docs/glossary/stack.md` header, line 7, chains two facts with a semicolon ("says; a project on another stack holds that stack's file instead"). The method's glossary header has no such clause. It is a semicolon like those left above, so it is not listed.
