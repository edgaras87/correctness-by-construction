<!-- The redesign of the conventions, opened 2026-10-19 on
     redesign-2026-10-19. Data only: how this file is made is
     docs/conventions/conventions-redesign/ §2. It grows a part at
     each stage, and goes at the close. -->

# Conventions redesign, 2026-10-19

## The targets (§2.1)

Designs discussed with the reviewer on 2026-10-19. Each is
possible, not promised: an iteration moves toward one, or shows it
wrong.

| Target | What it would change | Why it might help |
|---|---|---|
| TARGET-A | each manual states its main subject first | the conventions convention opens with "a rule the work may break only with a reason", and its core idea, a thing described once with rules and skills made from it, sits in §3.5 |
| TARGET-B | a manual names its sub-ideas; a sub-idea can grow into a manual of its own, which the first references | parts with rules of their own exist unnamed: one home in project-recording §11, the foundation check in conventions §3.5 |
| TARGET-C | a picture of how a manual's sub-ideas relate | how the parts and the conventions relate is seen nowhere (PAIN-11) |
| TARGET-D | every link named, each with what keeps it up: derives, points, part of, reasons from, requires, governs | governs, reasons from and requires have no upkeep today (PAIN-8) |
| TARGET-E | what a thing is, apart from what we do about it: a model that binds nothing beside the manual that binds | the agent model and agent-arrangement already work this way; on 2026-10-19 "what a concept is" and "how one is written" were mixed |
| TARGET-F | a manual is called a concept, and its rules and skills the convention | one word for one idea (PAIN-5); "concept" already names the CbC concept and the tiers model's concepts tier |

## The target sketch (§2.1)

A manual as all six targets would make it. Possible, not promised,
and read again after each verdict.

```
# <name>
main subject                          ← TARGET-A
sub-ideas, each in its own section;   ← TARGET-B
  one grows into a manual when …
picture of how they relate            ← TARGET-C
links, each with what keeps it up     ← TARGET-D
the model it reasons from             ← TARGET-E
seats; why it arrives this way;
  what it does not cover
```

Its name, a concept or a manual, waits for TARGET-F.

## The pains, as tests (§2.1)

Listed and confirmed by the reviewer on 2026-10-19. Each is a way
the conventions make upkeep hard, with its case. Sources: the
refinement's session of 2026-10-18 and 2026-10-19, and TODO's items
about how a convention is built. *Answered* means a fix already
landed; the redesign still checks that it fits.

| Pain | What makes upkeep hard | Its case | Now |
|---|---|---|---|
| PAIN-1 | a moved section breaks the pointers to it | the refinement's manual renumbered three times on 2026-10-18; a TODO pointer stood stale for five commits, fixed at `999fdce` | answered: the grep at the commit, `7061c89`, `d1fb072` |
| PAIN-2 | a seat retells another home | project-recording's deliverer seat retells `PLAN.md`'s step form, found 2026-10-19 | open |
| PAIN-3 | a record is not linked to the manual its form comes from | `PLAN.md`'s step form and project-recording: a change on either side reached neither, 2026-10-19 | rule answered, `c06943d`, `242d248`; the lines wait for the refinement's Wiring |
| PAIN-4 | one case's data sits in a manual | the refinement's eight kinds in its manual's §1, 2026-10-18, moved to its file at `7ee14e2` | open: no rule says it |
| PAIN-5 | a word means two things, or has no one definition | "step": PLAN's, a list's, `commit-plan`'s "small steps"; "stage": a skill's and the refinement manual's; "group": a delivery's, and the refinement's until `97f4adc`; "areas" never defined, `2f7dcea`; the writing manual sends coined words to a glossary, our rule to `ARCHITECTURE.md`'s *The words* | open |
| PAIN-6 | one fact is told in several places | how the seats differ, in five places (devlog 2026-10-17, W8); what TODO's Now holds, three ways (2026-10-19) | open |
| PAIN-7 | the why and the how are split the wrong way between a manual and what derives from it | `PLAN.md`'s step form explains why ("a gate written at the close describes what happened"); project-recording's seat says how, 2026-10-19 | open |
| PAIN-8 | a rule that governs other text has no upkeep when it changes | the writing rule's older text waits for a refinement (TODO, 2026-10-17); this redesign; the local map item: "governs (none …)" | open |
| PAIN-9 | commits cited by hash cannot be regrouped | the refinement's commits were not regrouped before main took them, `5c79a11` | open: TODO, due here |
| PAIN-10 | nothing puts how a skill or rule is written in front of its writer | conventions §2 says it, and a manual has `convention-manual.md`; a skill or rule has no such rule (TODO, 2026-10-17) | open |
| PAIN-11 | how the conventions relate is seen nowhere | about thirty pointers across the manuals' *What this does not cover*, seen together nowhere (TODO, 2026-09-30) | open |
| PAIN-12 | our own forms load while written, where a run's shapes are read at the gate | the reading's and the manual's forms are rules; they kept that place before this repo had steps, and it has since ADR-0057 (TODO, 2026-10-17) | open |

Not listed, each a question about how a convention is built but no
pain yet, since no case of harm is recorded:

- folding the agent model into agent-arrangement: neither had
  drifted on 2026-09-30;
- a convention for the playbook: one playbook exists;
- the form rule loads only when a manual is opened with the Read
  tool, and this session edited manuals by script: no form break
  was found.

Not searched yet: the findings of earlier readings and of the eval
of 2026-09-30, in git.

## The iterations (§2.2)

A rolling list, in the reviewer's order of 2026-10-19. The first is
firm; the rest are provisional, and change after each verdict.

1. **A main subject in the conventions convention.** Toward
   TARGET-A. *Firm.*
2. **The conventions convention's sub-ideas named,** and whether
   other conventions belong as its sub-ideas, or the other way
   round. Toward TARGET-B. *Provisional.*
3. **A picture of how its sub-ideas relate.** Toward TARGET-C.
   *Provisional.*
4. **What is still missing** for maintenance, readability and
   future-proofing, the pains as prompts. Toward TARGET-D and
   TARGET-E. *Provisional.*
5. **The same on project-recording** (§2.4). *Provisional.*
6. **The pattern,** if one held, written in the conventions
   convention with its rule (§2.5). *Provisional.*
7. **The other manuals** (§2.4). *Provisional.*
8. **The words** (§2.6). Toward TARGET-F. *Provisional.*

## The verdicts (§2.3)

None yet.
