# Commit plan: the conventions manual

## Summary — the state after all commits

A ninth convention, `conventions`: what a convention is here, its
two parts kept apart, how an artifact is written, how a manual is
written, the rules the container holds about them, and how one is
added. Its manual is born from the four rule sections the index
accreted — the opening definition, *A skill file*, *Writing an
artifact*, *The container's rules*, *Adding a convention* — and the
index returns to what ADR-0032 scoped it to: the table and the
chain, relations only. Every manual answers the seats question in
one sentence or a section. The shape of a manual is a rule of ours
under `.claude/rules/`, loading on the manuals' paths, born from
the pair that recurred in the exchange and shapes manuals. The
convention ships nothing: `foundation` is already in every shipped
file, and the run's own descriptions earn their rule later.

The shared core — one description, everything derived points back,
a change walks the list, a forced change is checked back, a
disagreement is decided with practice as the evidence — is stated
once, in the master document's section 3, which stops calling
itself "not a rule yet". Both kinds of description point at it; the
edges that differ stay where they are. The words are decided: a
description is any body of writing things derive from, a manual is
a convention's, `foundation` is the derived side's claim, and the
split carries meaning — versioning, shipping, the kind of
derivative, seats, and what each asserts. Four TODO items close.

## Commits

**1. `docs(agent): add commit plan for the conventions manual`**
This file.

**2. `docs(adr): ADR-0039 — conventions are a convention`**
Opens Proposed. Decides: the manual, named `conventions`, from
what the index held, and the index back to relations; the seats
rule; the shape of a manual as a rule here, its artifact; the
words, with the five differences that make the split meaningful;
the master's section 3 as the rule for every description, and the
trigger for a descriptions manual of its own — that section
outgrowing the page, the master's own rule for itself. Records
what was checked before writing: the last three conventions got a
registry entry and a table row, and none got a CHANGELOG line or a
PLAN step, so the index's *Adding a convention* stated two steps
nobody took. Decision-first: settled in conversation on
2026-09-27 and 28.

**3. `docs: the master's section 3 is the rule for every description`**
The five steps stated as the rule, the "not a rule yet" paragraph
gone, its trigger recorded as fired. *The words* gains what the
ADR decided. Section 1.2 says nine. This comes before the manual
because the manual points at it.

**4. `docs(conventions): the conventions manual, and the index returns to relations`**
`docs/conventions/conventions/README.md` written from the index's
four rule sections and ADR-0031's claim about what a convention
asserts, in the manual shape: header, opening, what ships (nothing
— what a repo holds is the shape rule and the `foundation` line),
the seats (this repo writes manuals; a run holds artifacts), *what
this is made usable as*. *Adding a convention* is rewritten from
what the last three did. The index keeps the table, with a ninth
row, and the chain; every rule leaves it. Provisional in one
respect: which sentences of the index are relations and stay is
seen only in the cutting.

**5. `docs(conventions): six manuals say their seats`**
One sentence each — project-recording, commit-messages,
repo-hygiene, commit-plan, agent-arrangement, visual-comparison —
placed where the shape says, after *what ships*. Material-first:
the sentence is written from each manual, and if one turns out to
need a section, the boundary says so.

**6. `chore(agent): the shape of a manual, as a rule here`**
`.claude/rules/convention-manual.md`, a Governs line and
`paths: docs/conventions/*/README.md`, stating the sections a
manual has: the header on what derives from it and how a
disagreement ends; the opening statement; what ships; the seats;
lessons as dated italics; what it is made usable as. Registry entry
"Convention held: conventions". Agent-scoped, alone.

**7. `docs: records, and ADR-0039 accepted`**
ARCHITECTURE's conventions row says nine; the master's 2.3 count
stands (nothing entered the container). TODO: the descriptions
convention item closes into the ADR, the seats item into step 5,
the words item into the ADR, the maintenance rule into step 3.
ADR-0039 flips.

**8. `docs(agent): close commit plan for the conventions manual`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Named `conventions`, so the path reads
  `docs/conventions/conventions/`.** The manual is about
  conventions whole — the artifact, the manual, the container's
  rules, adding one — not manuals alone, so `manuals` would name a
  part. The doubled word is the cost.
- **No descriptions convention.** Two kinds of description is two
  instances, and ADR-0038's rule of three binds here too. The
  shared core is one section of the master, and the master already
  says what happens when a section outgrows it.
- **The shape rule is written now, not held.** The shapes manual
  says a shape is born when a pair recurs; the exchange and shapes
  manuals share six sections and both were written from nothing
  telling the writer to. That is the pair. It is ours, exposed,
  ships nowhere.
- **Nothing ships, so no CHANGELOG entry** — and *Adding a
  convention* stops asking for one. The CHANGELOG is the
  concept-version log (ADR-0003); the last three conventions wrote
  no line in it and were right not to.
- **The index is cut, not rewritten.** What leaves it goes to the
  manual with its wording; a sentence that is a relation stays. The
  test is ADR-0032's: does it restate a rule that lives in a manual
  or a skill.
