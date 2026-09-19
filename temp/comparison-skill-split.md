# Does the comparison skill split?

Draft. The question: `option-comparison` was widened from form to
any buildable option, but most of its §4 still speaks Mermaid. Keep
one skill with the language fixed, or split the diagram half back
out as `format-comparison`?

Built rather than argued, per the skill's own §2 step 4.

## The measurement first

Six entries in §4. What each would belong to under a split:

| entry | general? | goes where |
|---|---|---|
| the dialect built for the job can fail | lesson general, examples Mermaid | either |
| a requirement no candidate can hold | fully general | general |
| building finds the modelling error | lesson general, example a flowchart | either |
| using a dialect is not fighting it | **mechanics are Mermaid-only** | specific |
| a shape can contain a step the others lack | fully general | general |
| a requirement can be the consequence of the real one | fully general | general |

**One entry is specific. Three are general. Two are general
lessons wearing diagram clothes.**

---

## A. One skill, headlines generalised

`.claude/skills/option-comparison/SKILL.md` — §4 only, the two
changed headlines in bold.

> - **The option built for the job can be the one that fails.**
>   Mermaid `block-beta` is meant for stacked blocks and lost both
>   the arrow labels and the vertical order. `sequenceDiagram` is
>   meant for handoffs between actors and had to draw a read-only
>   reading as an arrow into the other repo — asserting the
>   opposite of the rule the procedure existed to keep. A candidate
>   that states the opposite of the truth is worse than none
>   (ADR-0027, ADR-0028).
>
> - **A requirement no candidate can hold is evidence about the
>   requirement.** *(unchanged)*
>
> - **Building is what finds the modelling error.** *(unchanged)*
>
> - **Using a form is not fighting it.** Ordinary syntax is
>   ordinary. In Mermaid the fight looks like invisible links,
>   spacer nodes and nodes declared out of meaning order; whatever
>   the form, a candidate that needs them has lost (ADR-0027
>   decision 2).
>
> - **A shape can contain a step the others lack.** *(unchanged)*
>
> - **A requirement can be the consequence of the real one.**
>   *(unchanged)*

Files: 1. Diagram content: still present, as evidence under general
headlines.

---

## B. Split — general skill plus a diagram skill

### B1. `.claude/skills/option-comparison/SKILL.md`

§1–3 unchanged. §4 keeps four entries: the requirement-no-candidate
-can-hold one, building-finds-the-modelling-error, and the two from
ADR-0030. §5 loses its Mermaid clause. One line added:

> For diagrams, read `format-comparison` beside this — the method
> is this one; that file is what dialects have cost us.

### B2. `.claude/skills/format-comparison/SKILL.md`

> ---
> name: format-comparison
> description: What rendering a diagram has caught, for use with
>   option-comparison when the options are diagram dialects.
> ---
>
> # Format Comparison — diagrams
>
> **The method is `option-comparison`. This is its diagram
> appendix.** Read both; this one alone will not settle anything.
>
> ## What rendering a dialect has caught
>
> - **The dialect built for the job can be the one that fails.**
>   `block-beta`, `sequenceDiagram`, as above.
> - **Using a dialect is not fighting it.** Invisible links,
>   spacer nodes, nodes out of meaning order.
>
> ## Scope
>
> This repo's Mermaid trial is provisional and does not travel
> (ADR-0027 decision 3); a run decides its own forms.

Files: 2. **And B2 is not a skill.** It has no trigger of its own —
its own text has to say "read the other one first" — and no method,
only two notes. A skill that cannot be used alone is a reference
file wearing a skill's frontmatter.

---

## C. One skill with a reference file — what B exposed

Building B is what produced this. If the diagram material is an
appendix, say so with the shape the repo already uses for an
appendix: the bundle's skills keep theirs in `references/`.

### C1. `.claude/skills/option-comparison/SKILL.md`

As A, plus one line in §4:

> Dialect-specific findings live in
> `references/diagrams.md` — read it when the options are diagram
> dialects.

### C2. `.claude/skills/option-comparison/references/diagrams.md`

The two Mermaid entries and the Mermaid-trial scope clause. No
frontmatter, no trigger, no pretence of standing alone.

Files: 2, one of them a reference. Diagram content: separated,
without inventing a second skill.

---

## Against the requirements

The question's requirements, written before these were built:

1. A reader with a non-diagram option question must not bounce off
   it as "the diagram skill".
2. A reader with a diagram question must still reach the dialect
   findings.
3. It must not cost a file that carries almost nothing.
4. The split must be reversible cheaply if the balance changes.

| | A | B | C |
|---|---|---|---|
| 1. not "the diagram skill" | pass | pass | pass |
| 2. diagram findings reachable | pass | pass, via a pointer | pass, via a pointer |
| 3. no near-empty file | **pass** | **fail** — two entries | partial: a reference may be thin, a skill may not |
| 4. reversible | pass | costly — a skill others may cite | pass |

## Where this lands

**A wins today on the count**, and C wins the moment the diagram
material grows. The number that decides between them is how many
§4 entries apply to one kind only: **one, today.**

So: take A now, and let C be what the split trigger produces —
`references/diagrams.md`, not a second skill. B is rejected outright
and the reason is worth keeping: *a skill that cannot be used alone
is a reference file wearing a skill's frontmatter.*

Trigger for C: three or more §4 entries that apply to one kind of
option only.
