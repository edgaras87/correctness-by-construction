# Change-plan: the moment-of-need set — README direction moves into the skills

## Summary — the state after all commits

The direction the handbook's README stub no longer carries
(Prerequisites, Run, Test — deleted upstream under "container stays,
direction goes") has its method-tier home: infra-establish's walk ends
by projecting the README's Prerequisites section when the ground
stands, and cbc-bootstrap's close projects Run and Test when the
harness is real. Each skill carries the section skeleton as a template
fragment in its own `templates/` (ADR-0008 machinery, nothing new),
extracted from checkout-system's lived README — the same discipline as
the seven existing templates. One lived fact shapes the split: the
JDK line in checkout-system's Prerequisites is stack, not ground, so
the environment lines land at establish and the stack line at
bootstrap — each line arrives when its fact becomes true. ADR-0013
records the decision. The bundle-side work is then whole (the playbook
half landed 2026-09-02, ADR-0011), which fires two queued triggers:
the handbook handoff (four items) and the re-birth.

## Commits

**1. `docs(agent): add change-plan for moment-of-need set`**
This plan, committed after agreement, before the work.

**2. `docs(adr): propose README direction at moment of need`**
ADR-0013, Status: Proposed. Decision-first — the split was settled in
the 2026-08-31 discussion and the handbook exchange (their
ADR-0025/0026: the *when* is convention-tier, theirs; the *what* is
method-tier, ours); the material commits apply it. Options rejected:
leave it to the newborn's derivation (ADR-0012 covers birth-time
arrangement; these sections' moments are mid-run, past any session
that read the scenario), gate items in the cbc-run playbook (the
adopted projection rule says gate items where relevant, no mandatory
doc step per gate — and the playbook already points at the skills,
which is where the work is walked). Scope boundary stated in the ADR:
CLAUDE.md has parallel mid-run moments (the stack fact at bootstrap,
the ground-up rule at establish), deliberately left out — its stub
teaches its own fills, and whether the newborn catches those moments
unprompted is the ADR-0012 derivation experiment's data, not ours to
pre-empt.

**3. `docs(starter): infra-establish projects README Prerequisites`**
The skill gains its moment: `templates/readme-prerequisites.md`
(extracted from checkout-system's lived Prerequisites — environment
lines only, the stack line is not this skill's fact), the walk's
step 7 gains the projection direction, SKILL.md's records-and-outputs
list names it. Dated header lines per ADR-0007 in each edited file.
One logical change — reverting it removes both the fragment and every
pointer to it.

**4. `docs(starter): cbc-bootstrap projects README Run and Test`**
Same shape: `templates/readme-run-test.md` (lived Run and Test
sections plus the stack Prerequisites line whose fact is born here),
Stage 5's exit records name the README projection explicitly, dated
header line.

**5. `docs: close records for the moment-of-need set`**
The records walk, planned at drafting: TODO's Next item closes; the
two Now items' triggers (handoff, re-birth) now read as fired; a new
TODO watch item — at the re-birth's phase closes, watch whether the
newborn updates its own CLAUDE.md at the two parallel moments (stack
at bootstrap, ground-up rule at establish); a costly miss is evidence
for a harvested skill line, decided at trial close beside the snippet
comparison; PLAN's decision index gains ADR-0013; devlog entry with
Resume line; ADR-0013 flips Accepted. Walked and cleared deliberately: CHANGELOG
(mental layer unchanged — no concept version moves), ARCHITECTURE
("two skills carry copy-and-fill template masters" stays true as
written), starter/README.md (its Templates paragraph already
describes copy-and-fill generically; verify at the boundary, edit
only if the fragment shape contradicts it).

**6. `docs(agent): close change-plan for moment-of-need set`**
Deletes this file; body is the retro.

## Decisions taken inside this plan

- **Extraction over authorship.** Both fragments come from
  checkout-system's lived README (read-only), not written from
  theory — the bundle's rule since ADR-0012 closed the last
  theory-only artifact, and ADR-0008's own extraction discipline.
- **The Prerequisites split** (environment at establish, stack at
  bootstrap) is derived from the lived file's own content, not
  invented: at ground time no JDK fact exists to project.
- **The playbook is untouched.** cbc-run's Ground and Skeleton steps
  already route to these skills; adding README gate items would be
  the mandatory-doc-step-per-gate pattern the adopted rule refuses.
  A reviewer could object that the gate is where projection was
  adopted upstream (their ADR-0025) — answer: at run scope the
  skill's own exit test is the gate that fires, and the playbook
  middles change by harvest (ADR-0011), which this is not.
- **CLAUDE.md gains nothing, deliberately** (user consulted at
  planning). Its parallel moments are real but un-orphaned — the
  stub's own comments carry the fill rules — and pre-empting them
  would contaminate the ADR-0012 derivation experiment. A watch item
  rides the records commit; evidence decides at trial close.
- **infra-serve gains nothing.** A later service that changes the
  ground's prerequisites grows the operator manual, and the
  projection follows it — noted as an ADR consequence, harvested
  into a step only if a run shows it missed.
- **Wording discipline** (handbook return item 9): where either edit
  restates the stub rule, only the adopted form appears — container
  stays, direction goes.
