# AGS: Agreement, the CBC Run's side

Read at `70404e1`. 15 findings: 8 checked, 6 resting on the reader, 1 uncertain.

How the read was split:
- the container's Agent Rules, Agent Skills and Record Stubs, the delivered glossaries' container file, and the copies' diffs: read by AGS itself;
- the Method Group (AGS-9 to AGS-11) and the Stack Group (AGS-12 to AGS-15): read by two delegated readers on the session's model, each file whole, beside concept v1. Their full reports are `findings/AGS-method.md` and `findings/AGS-stack.md` in this scratchpad. AGS checked each of their first quotes against the tree; all landed.

The rule every finding names: a derived thing agrees with its Canonical Description until a disagreement is raised and decided, and either side may be the wrong one (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; §5, *A disagreement*). A shipped copy may differ from ours only for its Convention Seat (ADR-0069).

## The copies, hunk by hunk

The script's hunks, each judged:

- **commit-plan, line 9:** the container bolds "**Change Set**". The seat's. In a CBC Run, the glossary entry for Change Set (`delivery/container/docs/glossary/container.md` line 93) names the commit-plan Agent Skill as its home. So line 9 is the Name's defining line in that seat, and the container's writing rule 9 allows bold there. Ours dropped the bold at FINDING-626 because our glossary points at the commit-plan manual instead.
- **commit-plan, line 95:** ours points at `docs/conventions/commit-messages/` §2.3; the container's points at `.claude/skills/commit-messages/SKILL.md`, *The agent's own files*. The seat's: a CBC Run cannot open the manual, and the heading exists at line 102 of the container's commit-messages Agent Skill.
- **commit-plan, line 149:** ours carries a Fact Reference to commit-messages §2.4; the container's has none. The seat's: a shipped line that relies on a manual stands alone (`docs/conventions/facts-in-sync/`, *The CBC Run's seat*).
- **visual-comparison, §5:** the seat's. It says the Mermaid trial is the Concept Deliverer's and not delivered, as the manual's *What this does not cover* says.
- **commit-messages and `approach-drafting.md`:** identical.
- **`writing.md` and `one-home.md`:** written per seat. Three differences are not the seat's: AGS-1, AGS-2 and AGS-6.

No hunk is a copy not carried over.

## Findings

### AGS-1

- **Where:** `delivery/container/.claude/rules/one-home.md`, *Not a second home*, line 45.
- **Quote:** `never updated, so they cannot drift. The Decisions Log's header`
- **The other side:** `docs/conventions/facts-in-sync/README.md`, §1 *One home*, line 102: `  change. Each file's header comment is Living Text, the header`
- **The rule:** facts-in-sync §4 step 2 and §5. The container's one-home Agent Rule derives from facts-in-sync §1 and *The CBC Run's seat* (facts-in-sync, *What this is made usable as*).
- **What the text says:** the manual says every file's header comment is Living Text, the history files' included. The Agent Rule names only the Decisions Log's header comment. A CBC Run's devlog and CHANGELOG also carry header comments that hold their forms and Foundation Lines; read by the Agent Rule, they are history and never updated. The container's glossary sends Living Text to this section (`container.md` line 52), so the CBC Run's only account of Living Text is the narrow one.
- **Which side is wrong:** the Agent Rule. Its line predates the manual's sentence.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `0cdd102c` wrote the manual's sentence (DECISION-35). Its Foundation Check said "the two one-home Agent Rules, which follow in commit 13". Ours followed at `fab7214`; the container's took only the released-entries line, at `ae8eb31`. The Change Walk of `0cdd102c` should have caught it.
- **Proposed:** fix: lines 45-46 become "never updated, so they cannot drift. **Living Text** is every text but history. Each file's header comment is Living Text, the history files' included." (The bold is the Name's defining line in the CBC Run's seat, where its glossary entry points.)

### AGS-2

- **Where:** `delivery/container/.claude/rules/one-home.md`, *Not a second home*, line 43.
- **Quote:** `History: the devlog, closed ADRs, commit bodies, the entries of`
- **The other side:** `docs/conventions/facts-in-sync/README.md`, §1, line 104: `- **History is not a first home either.** A fact stated only in`
- **The rule:** facts-in-sync §4 step 2 ("the whole file is re-read: that finds ... a fact gone missing") and §5.
- **What the text says:** the manual's §1 holds that a fact stated only in history gets a home in Living Text before anything retells it (ADR-0070, decision 6, which is not marked as our seat's only). Our one-home Agent Rule carries it at line 60. The container's *Not a second home* stops at "history is not a second home". A CBC Run keeps a devlog and a Decisions Log, and meets the same risk.
- **Which side is wrong:** the Agent Rule, unless the fact is meant for our seat only. The manual's *The CBC Run's seat* does not say either way.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `a5c5a8e` (ADR-0070) wrote the line into facts-in-sync §1 and ours. The container's copy was not walked for it.
- **Proposed:** fix, with AGS-1: add "A fact stated only in history gets a home in Living Text before anything retells it." Or question: is the rule our seat's only? Then facts-in-sync, *The seats*, says so.

### AGS-3

- **Where:** `delivery/container/.claude/rules/delivered-copies.md`, frontmatter `paths:`, line 7.
- **Quote:** `  - "docs/concept/**"`
- **The other side:** `docs/conventions/exchange/README.md`, *What this is made usable as*, line 39: `  loading when a copy or a file in `temp/` is read (§4, *The Delivery Take*; §5, *Editing a copy*).`
- **The rule:** facts-in-sync §4 step 2 and §5.
- **What the text says:** the manual says the Agent Rule loads when a copy is read. The delivered Glossary Names in `docs/glossary/` are pinned copies; the Agent Rule's own rule 1 says so (line 28), as does `container.md`'s header ("changed only as .claude/rules/delivered-copies.md says"). But `paths:` lists `.claude/` folders, `docs/concept/**` and `temp/**`, and not `docs/glossary/**`. An agent editing a delivered glossary file never has the Agent Rule loaded.
- **Which side is wrong:** the frontmatter.
- **Stands:** checked.
- **Why it was missed:** missed at a change: `3630ed9` made the delivered Names pinned copies and added `docs/glossary/` to rule 1, but not to `paths:`. Its Change Walk read the rule's text, not its frontmatter.
- **Proposed:** fix: add `  - "docs/glossary/**"` after line 7. (`docs/glossary.md`, the CBC Run's own record, stays out of the glob.)

### AGS-4

- **Where:** `delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 6, line 119.
- **Quote:** `   6. **Write one Decisions Log entry** carrying both numbers: the new`
- **The other side:** `docs/conventions/exchange/README.md`, §4 *The Delivery Take*, step 5, line 361: `5. **Register.** One line in the CBC Run's Decisions Log: the date, the`
- **The rule:** facts-in-sync §4 step 2 and §5.
- **What the text says:** the manual's step 5 lists the entry's contents: the date, the Delivery Pin, what came, what was declined and where its need went. It does not name the Read-Through Commit. The Agent Rule's entry carries the Delivery Pin and the Read-Through Commit, and not what came or what was declined. Each side lacks part of the other's list.
- **Which side is wrong:** both, in part. The manual's §2.2, agent-arrangement §3.4 and the Decisions Log's Record Stub all say every delivery entry carries both numbers, so the manual's step 5 is short of its own §2.2. The Agent Rule drops what came and what was declined, though it says elsewhere (rule 5, after step 7) that "the Decisions Log entry says so" of a declined need.
- **Stands:** checked (both texts); which side changes rests on the reader.
- **Why it was missed:** the Read-Through Commit was added to §2.2 and the Agent Rule after step 5 was written; neither change re-read the other list.
- **Proposed:** question: one list in both. The recommended form: "One entry: the date, the new Delivery Pin, the Read-Through Commit the Delivery Note names, what came, and each declined edit with where its need went." The manual's step 5 and the Agent Rule's step 6 both take it.

### AGS-5

- **Where:** `delivery/container/.claude/rules/shapes-lifecycle.md`, §3 *A difference at the close*, line 68.
- **Quote:** `  changes: a project's own with a dated line, a delivered one under`
- **The other side:** `docs/conventions/shapes/README.md`, §5.2 *Ticks and differences*, line 309: `between them records when the Output Shape changed.`
- **The rule:** facts-in-sync §4 step 2 and §5.
- **What the text says:** the Agent Rule asks a dated line in a project's own Output Shape when it changes. The manual has no dated line. It says outputs closed before a change are not reopened, and the difference between them records when the Output Shape changed. `61fcc5d` removed the manual's dated lines, about seven places, and kept this one in the Agent Rule.
- **Which side is wrong:** the Agent Rule, probably. The manual's reason covers both kinds of Output Shape, and the writing of history into a file is what delivered-copies rule 2 forbids for a copy. If a CBC Run's own Output Shape does need a dated line, the manual should say so in its *The CBC Run's seat*.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `61fcc5d` (ADR-0052). Its body says a delivered Output Shape changes "under delivered-copies rather than with a dated line", and kept the line for a project's own. ADR-0052 is silent on it.
- **Proposed:** question: drop "with a dated line" ("a project's own in place, a delivered one under the delivered-copies Agent Rule"), or the shapes manual names the dated line for a CBC Run's own Output Shapes.

### AGS-6

- **Where:** `delivery/container/.claude/rules/writing.md`, rule 10, line 72.
- **Quote:** `    The point goes in the first sentence. A record's fixed headings, an Agent Skill Stage or Approach on Trial Stage heading, and a`
- **The other side:** `docs/conventions/writing/README.md`, §2 *Why each rule*, rule 10, line 160: `    Seats. Three are not titles under it: the manual form's fixed`
- **The rule:** facts-in-sync §4 step 2 and §5; ADR-0069 lets a copy differ for its seat, not state a rule its manual does not hold.
- **What the text says:** the manual says rule 10 holds for numbered sections in both Convention Seats, and exempts three things: the manual form's fixed headings, a stage heading, and a numbered rule's bold lead. The Agent Rule exempts "a record's fixed headings" instead. A CBC Run writes no manual, so the manual's first exemption is empty there; the Agent Rule puts a wider one in its place, which the manual never names.
- **Which side is wrong:** the manual, probably. The substitution was deliberate ("the headings a run holds among the exemptions"), and it is the CBC Run's equivalent. But it stands nowhere in the Canonical Description.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `25b3946`. Its Foundation Check says "the two copies differ in their examples only, as ADR-0069 allows". They also differ in this exemption.
- **Proposed:** question: the manual's rule 10 names, for the CBC Run's seat, a record's fixed headings beside the manual form's; or the Agent Rule drops the exemption.

### AGS-7

- **Where:** `delivery/container/.claude/skills/retrospective/SKILL.md`, *Stage 4 — close*, item 3, line 114.
- **Quote:** `   line naming that decision. The Decisions Log gets a "rules in`
- **The other side:** `docs/conventions/agent-arrangement/README.md`, §3.4 *`.claude/decisions.md`*, line 326: `The arrangement's Decisions Log: append-only and dated, each entry in`. The Record Stub agrees: `delivery/container/.claude/decisions.md` line 3, `<!-- The working arrangement's Decisions Log. Append-only, newest`.
- **The rule:** facts-in-sync §4 step 2 and §5. The line uses a fact whose home is agent-arrangement §3.4, the Decisions Log's form.
- **What the text says:** the Agent Skill puts a "rules in force now" list on top of the Decisions Log at the retrospective. The manual says the log is append-only and dated, in entries of three parts, and names no such list. The stub says newest last. The retrospective manual, the Agent Skill's own foundation, names no list either.
- **Which side is wrong:** the manuals. CBC Run 3 and CBC Run 4 each wrote the list at their retrospective (our Decisions Log, 2026-10-17). Practice is the evidence. The fact lives only in the Agent Skill and in history.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `d1922c4`. Its Foundation Check read agent-arrangement §3.4 and said "the retrospective skill agrees", without weighing "on top" against "append-only".
- **Proposed:** question: agent-arrangement §3.4 (or the retrospective manual §4) gains the list, as the one part of a CBC Run's log not appended, and the stub's header says so; or the list goes to `RETRO.md`.

### AGS-8

- **Where:** `delivery/container/docs/glossary/container.md`, entry *Glossary Name*, line 99.
- **Quote:** `  or more words, capitalized, written exactly; what this file lists.`
- **The other side:** `docs/conventions/writing/README.md`, *What this is made usable as*: `docs/glossary.md` is "a record that holds only the Names it defines", and the delivered Names are pinned copies under `docs/glossary/`. The container's writing rule 9 agrees (`delivery/container/.claude/rules/writing.md` line 43: `project's glossary, `docs/glossary.md`, or a delivered file under`).
- **The rule:** facts-in-sync §4 step 2 and §5; the file's Foundation Line names the writing convention.
- **What the text says:** the entry says a Glossary Name is "the name of a thing this project defines ... what this file lists". In `container.md` neither half is true. This file lists the shared Names, which the Concept Deliverer defines. The project's own are `docs/glossary.md`'s, as the file's own header says (line 8-9).
- **Which side is wrong:** the entry.
- **Stands:** checked.
- **Why it was missed:** missed at a change: `3630ed9` moved the entry, word for word, from the CBC Run's glossary record into the pinned copy. Its Change Walk did not re-read the moved entries.
- **Proposed:** fix: "- **Glossary Name** — the name of a defined thing: two or more words, capitalized, written exactly; this project's own are listed in `docs/glossary.md`, the delivered ones in `docs/glossary/`."

### AGS-9 (the Method Group's reader, AGS-M1)

- **Where:** `delivery/method/.claude/skills/cbc-slice/SKILL.md`, the opening, line 11.
- **Quote:** `non-negotiable: **the test that creates the adversity exists and`
- **The other side:** `concept/04-cbc-slice.md` line 22: `Structural Wall stands, the proof exists, and later work is allowed to`; and line 56, a passing test without its Structural Wall is not closed.
- **The rule:** facts-in-sync §4 step 2 and §5.
- **What the text says:** the Agent Skill makes the completion test one thing: the adversity test exists and passes. The concept needs two: the Structural Wall stands, and the proof exists.
- **Which side is wrong:** the Agent Skill's opening. Its own Stage 2 and Stage 3 Gates already require the Structural Wall.
- **Stands:** checked. TODO's "Rewrite the method's texts plain" names the same gap as an idea (TODO.md 659-661), which is not a decision.
- **Why it was missed:** older than the rule; rewrapped at `06a3915`.
- **Proposed:** fix: "The completion test is non-negotiable: **the Structural Wall stands, and the test that creates the adversity had its Red Run and passes.**" Or question: left to the TODO item.

### AGS-10 (the Method Group's reader, AGS-M2)

- **Where:** `delivery/method/.claude/shapes/kill.md`, *The shape*, line 74 (template at 51-56).
- **Quote:** `- **An Enemy Collision that breaks nothing stays in the list,**`
- **The other side:** `concept/03-cbc-framing.md` line 46: `Possession: what dies? The output names the **Enemy Collision Kill**,`. The method glossary (line 77), the worked example (174) and the framing workflow (304) agree with the concept.
- **The rule:** facts-in-sync §4 step 2 and §5.
- **What the text says:** the Output Shape gives a collision where nothing dies a `KILL-<n>` tag. In the concept an Enemy Collision Kill is what dies.
- **Which side is wrong:** not clear. CBC Run 5 carried such a kill, and TODO.md 653-656 plans to move the worked example toward the Output Shape.
- **Stands:** checked (all lines); the side rests on the reader. Not leftover H5, which is about NOT-OURS-1.
- **Why it was missed:** known and deferred (devlog 2026-10), waiting for the plain rewrite.
- **Proposed:** question: is a collision where nothing dies an Enemy Collision Kill (the concept and glossary widen), or a tried Enemy Collision under another tag (the Output Shape changes)? The worked example, the workflow and the registry template follow.

### AGS-11 (the Method Group's reader, AGS-M3)

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *Working one Invariant Slice*, line 85.
- **Quote:** `- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees, the proof,`
- **The other side:** `concept/04-cbc-slice.md` line 47: `what Structural Wall holds it, and how it was shown to survive. The`
- **The rule:** facts-in-sync §4 step 2 and §5. The page says it summarizes the concept and that a disagreement means one is wrong.
- **What the text says:** the concept's Document phase records what is promised, the Structural Wall, and how it survived. The page swaps the Structural Wall for the Invariant Slice Guarantees.
- **Which side is wrong:** the page.
- **Stands:** resting on the reader (a summary may shorten; the reader reads a swap).
- **Why it was missed:** older than the rule: `edecd0e`, reworded at `8316ce0` and `60398b1`.
- **Proposed:** fix: "- **Document:** what is promised, the Structural Wall that holds it, and the proof, readable later."

### AGS-12 (the Stack Group's reader, AGS-S1)

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md`, Stage 1, line 75; with `references/app-structure.md` line 76.
- **Quote:** `- **The stack evaluation.** The deciding inputs are **fluency and`
- **The other side:** `concept/03-cbc-framing.md` line 81: `after CBC Framing, each choice answerable to the Invariant Slice`
- **The rule:** facts-in-sync §4 and §5; conventions §1.3, "checked against".
- **What the text says:** the concept makes each technology choice answerable to the Invariant Slice Registry. The stack evaluation decides on fluency and audience only, and app-structure says the Invariant Slices "rarely tell structures apart", as with the stack.
- **Which side is wrong:** not clear. The stack side is practice, and a registry may constrain the store, not the language.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at `211bd0f` (the concept's line, before the Change Walk) and at `c449de0`, whose Foundation Check said they agree.
- **Proposed:** question: the stack evaluation adds "the stack must serve the Invariant Slice Registry; among stacks that do, fluency and audience decide", or the concept narrows "each choice" to the choices the Registry can tell apart.

### AGS-13 (the Stack Group's reader, AGS-S2)

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, §5, line 452.
- **Quote:** `  demands it, and the method deletes it.`
- **The other side:** `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md` line 7: `deliberately left open. Standing the system up is project work, not`
- **The rule:** facts-in-sync §4 and §5: a stack text that says the method requires something.
- **What the text says:** the CBC Bootstrap Probe is said to be demanded and deleted by "the method". No Method Group file names the probe; the demand and the deletion are the cbc-bootstrap Agent Skill's own.
- **Which side is wrong:** the stack line, written before the Method Group and Stack Group split (`657d6eb`).
- **Stands:** checked.
- **Why it was missed:** older than the split (`8ed34e9`); missed again at `a6ccf5b`.
- **Proposed:** fix: "the CBC Bootstrap Probe crosses into `main/`, because the CBC Bootstrap needs a door to attack, and the first Invariant Slice deletes it."

### AGS-14 (the Stack Group's reader, AGS-S3)

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, §4, line 374; with `spring-boot-walkthrough.md` §5, line 240 on.
- **Quote:** ` * Class the first Invariant Slice needs, end to end through the real`
- **The other side:** `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md`, READINESS-4, line 46: `Read this Invariant Slice's Invariant Slice Entry. For **the Adversity Class it`
- **The rule:** facts-in-sync §4 and §5: the CBC Bootstrap's outcome gives what cbc-slice's Stage 0 checks.
- **What the text says:** the references state contention as the first Invariant Slice's Adversity Class and show only a burst. READINESS-4 asks for the class the Invariant Slice names; the worked example's SLICE-1 is duplicate delivery.
- **Which side is wrong:** the references, if read as generic.
- **Stands:** uncertain. The references say they are one CBC Run's shape, and the SKILL.md wins on a conflict.
- **Why it was missed:** older than the rule; reworded at `a6ccf5b` without reading READINESS-4.
- **Proposed:** question: the harness reference gains a variation point, "the probe's test follows the CBC Bootstrap Adversity Class; the burst is the shape for contention".

### AGS-15 (the Stack Group's reader, AGS-S4)

- **Where:** `delivery/spring-postgres/docs/glossary/stack.md`, entry *Stack Default*, line 85.
- **Quote:** `  demand or a fact about the environment defeats it: local containers`
- **The other side:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md` line 77: `  the deciding inputs are the CBC Run's own: fluency, audience, and`
- **The rule:** facts-in-sync §4 and §5; a glossary entry agrees with the homes it names.
- **What the text says:** the entry says a Stack Default yields only to a demand or an environment fact, and names app-structure as a home. App-structure lets a CBC Run depart for fluency, audience or a stated intent.
- **Which side is wrong:** the entry.
- **Stands:** checked.
- **Why it was missed:** missed at `c66778e`, which read the entry against establishment-walk only.
- **Proposed:** fix: name both departures: local containers under podman, run by compose, departed from only when a demand or an environment fact defeats it; packages by feature, departed from by the CBC Run's own deciding inputs.

## Found true, so not listed

- **delivered-copies against the exchange:** rule 1's Delivery Pin and Read-Through Commit (§2.2); the edit's three conditions (§5.1); the CBC Run Ask at a Plan Step's close under *To the deliverer* (§5.1); a finished copy's "untried here" (§5.2); renaming and deleting (§5.5); a chapter edited only from a lived mistake (§5.6); Agent Skill Templates and off-template (§5.8); the Delivery Take's order (§4). The verdicts match §6.5.
- **shapes-lifecycle against the shapes manual:** the definition, written from work that exists, one place read at the Plan Step Gate, the four endings, an Output Shape naming work, offering one back. All four method Output Shapes open with a Governs line, as the Agent Rule asks.
- **commit-messages, commit-plan, visual-comparison, retrospective and apply-retrospective against their manuals:** the format and limits, the `agent` scope, the stop; the plan file, the split by change, inserted and repeated commits, the sweep, the look back, small commits; the non-picture in the set and the buildable notations; where a lesson lands, the old questions, the Entry File's re-read; the order by influence, history untouched, a fresh reader, tests counted from this CBC Run's reports.
- **The Record Stubs against project-recording:** `PLAN.md` (legend, the STEPS markers, "Discovered along the way", the Decision index, §2.4, §3.3, §9.4); `TODO.md` (§5.3, §5.4); the devlog (§4.3, §4.4); `CHANGELOG.md` (§6.3, §6.4); `ARCHITECTURE.md` (§8.4, §8.6); `README.md` (§7.4, the Repo Tag row); the ADR stub (§3.4); the playbook's Plan Step Form (§2.4, the closed Plan Step's one line in *The seats*, item 4).
- **The Entry File and Decisions Log stubs against agent-arrangement:** the CBC Run's seat (two things the Entry File says; 5 Agent Skills, 4 Agent Rules, 1 Approach on Trial); §2.3 placement under `.claude/`; §2.4's three tests in the guard comment; §3.4's two numbers. The records table has a row for each of project-recording §1's 12 records a CBC Run keeps.
- **`temp/README.md` against the exchange:** §3.1 and §4.

## Met in passing

- Our side, one gap: the exchange's §4 step 2 gives an edit three endings at a Delivery Take, taken, declined, unanswered; §6.5's third verdict, held, has none there. Neither the manual nor delivered-copies says what a held edit becomes when the copy lands whole.
- Our side, two manuals: commit-plan §2.1 says `COMMIT-PLAN.md` is "not a record" and sits outside project-recording, and the shipped commit-messages Agent Skill line 105 says "None is a project record". But project-recording §1 lists it as record 9, and both records tables carry its row.
- One home: the container's glossary sends Living Text to one-home's *Not a second home* (`container.md` line 52), which does not define it; AGS-1's fix gives it the line.
- Wiring: DECISION-40 turned "CBC docs/…" into "the Concept Deliverer's docs/conventions/…" in shipped files; one remains, split across lines 12-13 of `delivery/container/.claude/rules/one-home.md`: "(CBC" / "docs/conventions/facts-in-sync/ §1, One home; The CBC Run's seat)". Facts-in-sync §3.1 still says a shipped reference "leads with CBC".
- From the delegated readers, each one line: method-internal mismatches on *Answered at close* lines, the Structural Wall Check's "reads the code", the CBC Framing Reconciliation's scope, and READINESS-1; `slice-record.md` 58-62 retells the workflow's stage order (one home); `spring-boot-walkthrough.md` 186's short `bootstrap.sql` path (stale); `postgres-setup-walkthrough.md` 194-195's read-only identity at the CBC Bootstrap; `verify-database-model.sql` not checking role-split's PUBLIC claim; cbc-bootstrap never naming System Readiness's sign-off. Details are in `AGS-method.md` and `AGS-stack.md`.

## Not read

None, within the assignment. The hygiene files (`.editorconfig`, `.gitattributes`, `.gitignore`), the Pure Seed and `delivery/README.md` carry no Foundation Line and are neither Record Stubs nor in part 1, so they were not read for this Finding Kind. The playbook was read for its Plan Step Form only, beside project-recording.
