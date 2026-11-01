# AGS-method: Agreement, the CBC Run's side, the method

Reader: Agreement, the CBC Run's side, the method's files. Read at `70404e1`.
Canonical Description: concept v1, `concept/00-cbc.md` to `concept/04-cbc-slice.md`, read whole.
Output Shapes also read beside `docs/conventions/shapes/README.md`.

Three findings. Two of them are already named as ideas in TODO.md's item "Rewrite the method's texts plain" (TODO.md 642, ideas at 653-656 and 659-661). A TODO idea is not a decision, so they are listed. The reviewer may drop them as already held.

## AGS-M1

- **Where:** `delivery/method/.claude/skills/cbc-slice/SKILL.md`, the opening under *Invariant Slice — one invariant made real*, line 11.
- **Quote:** `non-negotiable: **the test that creates the adversity exists and`
- **The other side:** `concept/04-cbc-slice.md` line 22: `Structural Wall stands, the proof exists, and later work is allowed to`. And line 56: `Wall is ever weakened and only the test remains, the System Guarantee`.
- **The rule:** a derived thing agrees with its Canonical Description until a disagreement is decided (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; §5, *A disagreement*).
- **What the text says:** the Agent Skill says the completion test is "single": the adversity-creating test exists and passes. The concept says a closed Invariant Slice needs two things: the Structural Wall stands, and the proof exists. The concept also says a passing test without its Structural Wall is not closed, "whatever the test suite says". So the Agent Skill's one test is the very test the concept says is not enough.
- **Which side is wrong:** the Agent Skill's opening. Its own gates already require the Structural Wall: the Stage 2 Gate, and the Stage 3 Gate, where the Red Run has the Structural Wall absent and the same test goes green with it standing. Only the opening sentence drops it. The concept's line is the stronger claim, and the method's practice keeps it.
- **Stands:** checked. Both lines are in the tree. TODO.md 659-661 names the same gap.
- **Why it was missed:** older than the refinement's rules. The words came with the plain rewrite of cbc-slice and were rewrapped at `06a3915`. It is held as an idea in TODO.md's item "Rewrite the method's texts plain", waiting for its trigger, the refinement's close.
- **Proposed:** fix: "Carry one Invariant Slice, one invariant × its adversity, to demonstrated evidence. The completion test is non-negotiable: **the Structural Wall stands, and the test that creates the adversity had its Red Run and passes.** No evidence, no closed Invariant Slice." Or question: does the reviewer leave this to the TODO item's rewrite?

## AGS-M2

- **Where:** `delivery/method/.claude/shapes/kill.md`, *The shape*, Skeleton, line 74 (and the template at 51-56).
- **Quote:** `- **An Enemy Collision that breaks nothing stays in the list,**`
- **The other side:** `concept/03-cbc-framing.md` line 46: `Possession: what dies? The output names the **Enemy Collision Kill**,`. The method's own glossary agrees with the concept: `delivery/method/docs/glossary/method.md` line 77, "what dies in an Enemy Collision". So do the worked example, line 174, `Enemy Facts a Scope Exclusion covers collide with nothing:`, and the framing workflow, line 304, `Fact collides with nothing.`.
- **The rule:** a derived thing agrees with its Canonical Description until a disagreement is decided (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; §5, *A disagreement*). Where an Output Shape states the method's facts, it states the concept's.
- **What the text says:** in the concept, an Enemy Collision Kill is what dies when an Enemy Fact meets a System Possession. The Output Shape gives a collision where nothing dies its own tag, `KILL-<n>`, and counts it in the list as an Enemy Collision Kill. Its own Governs line, line 8, calls an Enemy Collision Kill "one way the Falsifiable Promise can break". So a `KILL-<n>` with "**nothing dies.**" is a Kill that kills nothing. The worked example and the workflow say the opposite: an Enemy Fact a Scope Exclusion covers collides with nothing and is not listed.
- **Which side is wrong:** not clear; practice may be right. CBC Run 5 carried a kill that breaks nothing (`temp/reading-run-5-2026-10-22.md` 449), and TODO.md 653-656 plans to move the worked example toward the Output Shape. If practice is right, the concept's Name is too narrow, or the tried pair needs a Name of its own that is not a Kill. If the concept is right, the Output Shape's third template and its fifth Skeleton bullet go, and a pair a Scope Exclusion stops is counted somewhere other than the KILL numbers.
- **Stands:** checked: the Output Shape, the concept, the glossary, the worked example and the workflow all hold these lines. Which side is wrong rests on the reader.
- **Why it was missed:** known, and deferred. devlog 2026-10 (2612) records it, found while the kills were written: "the kill shape keeps a collision that breaks nothing as a kill, and the worked example does not". The fix waited for the plain rewrite, because it moves the kill count the Invariant Slices cite. This is not reader H's H5. H5 is about the illustration starting with NOT-OURS-1. This finding is about whether a collision where nothing dies is an Enemy Collision Kill at all.
- **Proposed:** question: is a collision where nothing dies an Enemy Collision Kill (the concept and glossary widen), or a tried Enemy Collision under another tag (the Output Shape changes)? Then the worked example, the workflow's line 303-304 and the registry template's "excluded: NOT-OURS-n" row (`templates/registry.md` 96) follow the answer.

## AGS-M3

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`, *Working one Invariant Slice*, line 85.
- **Quote:** `- **Document:** the Falsifiable Promise, the Invariant Slice Guarantees, the proof,`
- **The other side:** `concept/04-cbc-slice.md` line 47: `what Structural Wall holds it, and how it was shown to survive. The` (after line 46, "**Document.** The claim and its proof, kept readable: what is promised,").
- **The rule:** a derived thing agrees with its Canonical Description until a disagreement is decided (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; §5, *A disagreement*). The page says it is a summary of the concept, and that if the two disagree, one of them is wrong (lines 3-8).
- **What the text says:** the concept's Document phase records three things: what is promised, what Structural Wall holds it, and how it was shown to survive. The page also lists three things, but puts the Invariant Slice Guarantees where the Structural Wall should be, so the Structural Wall is gone. Under the concept's proof standard, the Structural Wall is the thing the proof demonstrates (`concept/04-cbc-slice.md`, *The proof standard*). The Agent Skill (Stage 4) and the Invariant Slice Record Shape both record it.
- **Which side is wrong:** the page. It is the only text in the method that leaves the Structural Wall out of the document.
- **Stands:** resting on the reader. The page is a summary, and a summary may shorten. The reader judges that this is a swap, not a shortening.
- **Why it was missed:** older than the rule. The words came in with the import, `edecd0e` (2026-08-28), as "the promise, the guarantees, the proof". They were reworded at `8316ce0` and `60398b1` without a check against the concept's Document phase.
- **Proposed:** fix: "- **Document:** what is promised, the Structural Wall that holds it, and the proof, readable later."

## Found true, so not listed

- The derivation order. Framing SKILL 57-65, workflow 36-44 and the plain page 53-73 follow `concept/03-cbc-framing.md`'s six moves in its order. The two changes of order match concept 03's *Why this order and not the layers'*.
- The five System Layers, their names and their containment match `concept/01-layered-system.md` in the workflow, the plain page and the glossary. LAYER-5-INTERACTION is empty with a single Responsibility Area, as in concept 01 and 03. "Only if owners exist" (framing SKILL 63, workflow 42) is a drawing label, and workflow 369 states the condition.
- The three CBC Framing Exports, and what each holds (the CBC Framing Intent's purposes refused, the System Definition, the Invariant Slice Registry), agree with concept 03 *What CBC Framing produces*.
- The Invariant Slice's four phases, Specify, Plan, Build and Document, are the cbc-slice Stages 1 to 4. "No mechanisms" at Specify, and the comparison of Structural Walls at Plan, agree with concept 04.
- The ladder of Structural Walls has six rungs in the same order in slice SKILL 116-118, the plain page 96-97 and the glossary 48-51, matching concept 02.
- The Trust Assumption on who writes the store, and "a writer who can remove a Structural Wall cannot be walled against", agree with concept 02 (67-75). These are in framing SKILL 96-98, workflow 201-211, slice SKILL 127-133 and slice workflow 129-135.
- The Standing Guards are three of concept 00's four failure modes. Theory Swamp belongs to framing, not to a closed Invariant Slice. Concept 04's "a later change ... re-opens the question" is kept by the System Guarantee Erosion guard (slice workflow 225-228).
- The System Refusal Test, a second question after the System Possession Test, gives the same outcome as concept 03's "No means it's refused". It adds a question and contradicts nothing.
- The concept's Names in the glossary (13-84) agree with the chapters they cite.
- The four Output Shapes each give two layers, marked apart, and illustrate from the method's worked example: its order service, tags and numbers. Each states form, not content. The Structural Wall Backstop, a part only the work can produce, is also asked for by slice SKILL 180-182, as shapes manual §3 requires.

## Met in passing

- Method-internal: the registry-entry Output Shape (66-67) and the registry template (51-53) list one *Answered at close* line per Adversity Flag or judgment. Slice SKILL 227-230 also asks for what was left provisional and what is handed on.
- Method-internal: `evidence-test.md` 25 says a Structural Wall Check "reads the code". Slice SKILL 194-197, the glossary 225-227 and the Output Shape's own 174-176 say it sends a refusal or reads the store.
- Method-internal: the glossary 162-165 has the CBC Framing Reconciliation account for every CBC Framing Concern. Framing SKILL 238-239 and the template 84-85 say every Enemy Collision Kill.
- Method-internal: READINESS-1 in `system-readiness.md` 12-15 asks only for a `chosen-next` Invariant Slice. Slice SKILL 39-42 also asks for the CBC Framing Reconciliation.
- One home: `slice-record.md` 58-62 retells which Agent Skill Stage adds which part of a Block, which slice workflow 52-57 owns. Shapes manual §1.1 says when an output extends is not an Output Shape's to restate.

## Not read

None. Every assigned file was read whole. The worked example was read once, and `cmp` shows the two copies are byte-identical.
