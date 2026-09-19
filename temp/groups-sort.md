# The shipped files, sorted

Draft for PLAN Step 9, commit 2 of the groups change-set. Deleted
when ADR-0029 is written from it.

## How it was done

Every file under `starter/`, plus `docs/baselines/` and
`docs/conventions/`, put in one of three candidate groups: the
**container** a run is born into, the **method** (the concept and
what derives from it), and the **stack** (what assumes Spring,
PostgreSQL and podman). A grep over the bundle for stack words —
`spring|postgres|docker|maven|testcontainers|flyway|java|jdbc|`
`compose|psql|podman|boot` — gave a first cut, and then every hit
was read, because the first cut was wrong.

**The grep over-reports badly, and the reason is worth keeping.**
Three words in it are method vocabulary too: *compose* ("compose
the requirements document", "the registry is composed"),
*bootstrap* (the pipeline's third stage, named in all five skills),
and *boot* inside *bootstrap*. cbc-framing scored 5 hits and
cbc-slice 5; on reading, **all ten are false**. A group boundary
drawn from the grep alone would have cut in the wrong place and
looked measured while doing it.

## The sort

### Container — 16 + 8 files

`starter/kit/` (16, this repo's since ADR-0025) is the group with
the cleanest edge: nothing in it mentions a stack, and it is
already copied whole at birth. Beside it and *about* it,
`docs/conventions/` — seven manuals and `docs/conventions.md` —
which never ship. The about-it-beside-it rule the gate asks for is
already how these two sit.

One exception, and it is the one TODO already parked here:
`docs/conventions/repo-hygiene/templates/java-spring/` holds
`gitignore.part`, `gitattributes.part`, `editorconfig.part` —
three **stack** files inside the container's manual directory.

### Method — 9 files, and no more

Stack-free, checked line by line rather than counted:

| File | grep | real |
|---|---|---|
| `cbc-framing/SKILL.md` | 4 | 0 |
| `cbc-framing/references/cbc-framing-workflow.md` | 1 | 0 |
| `cbc-framing/references/the-whole-system-in-plain.md` | 0 | 0 |
| `cbc-framing/references/worked-example.md` | 0 | 0 |
| `cbc-framing/templates/registry.md` | 0 | 0 |
| `cbc-slice/SKILL.md` | 2 | 0 |
| `cbc-slice/references/cbc-slice-workflow.md` | 0 | 0 |
| `cbc-slice/references/system-readiness.md` | 3 | 0 |
| `cbc-slice/references/worked-example.md` | 0 | 0 |

These are exactly the two skills ADR-0005 marked *derives from*
concept v1. The three marked *checked against* are the three with
stack in them. **ADR-0005's split and the group boundary are the
same line**, drawn twice, three weeks apart, without either
noticing the other.

### Stack — 13 files, hard

Unusable without Spring, PostgreSQL or podman, and no pretence
otherwise: `postgres-role-split.md`,
`postgres-setup-walkthrough.md`, `bootstrap.sql`, `compose.yaml`,
`.env.example`, `flyway.conf`, `verify-database-model.sql` (all
infra-establish); `spring-boot-walkthrough.md`,
`spring-harness-reference.md`, `spring-pom-convention.md`,
`application.yaml`, `testcontainers.properties`,
`readme-run-test.md` (all cbc-bootstrap). Plus, already held out
of the bundle, `docs/baselines/spring-slice-reference.md`.

### Refusals — 6 files

The ones that would not sort, which is the part worth having:

- **`infra-establish/SKILL.md`** — the method is stack-neutral and
  its Postgres references are pointed at *conditionally* ("When
  PostgreSQL is the decided datastore, two more references
  apply"). What it does assume is podman-and-compose, as a "lived
  default" it invites the reader to re-decide.
- **`infra-establish/references/establishment-walk.md`** — podman
  commands throughout as the lived walk; Postgres conditional in
  the same way.
- **`cbc-bootstrap/SKILL.md`** — five stages of stack-free
  structure, and three lines that point at the Spring references.
- **`cbc-bootstrap/references/app-structure.md`** — 91 lines of
  stack-free decision surface with one Spring Modulith example.
- **`infra-serve/SKILL.md`** — no Spring, no Postgres; one
  `podman compose ps`, hedged with "or the project's equivalent".
- **`infra-establish/templates/readme-prerequisites.md`** — one
  podman line, and a header that already says a different ground
  writes different lines.

## What the refusals say

**The boundary is inside the three skills, not between them.**
Every `SKILL.md` in the bundle is stack-free or nearly so; the
stack is concentrated in `references/` and `templates/`. So the
group split is not three skills against two. It is: five methods,
and thirteen stack files that three of them point at.

**And the middle is a third thing, not a blur.** Six files assume
*a container ground* — podman, compose — without assuming Spring
or PostgreSQL. A project that is Go and MySQL still wants them; a
project that deploys to someone else's Kubernetes does not. That
is a real seam, and it is not the seam the gate expected.

## Where the gate's arithmetic lands

Step 9's gate cites "six templates all in one group". The disk
says ten templates in three skills:
`infra-establish/templates/` 6, `cbc-bootstrap/templates/` 3,
`cbc-framing/templates/registry.md` 1 — and the tenth is the slice
registry, which is method, not stack. The premise is wrong twice:
not six, and not one group. The gate item is corrected in the
close, not ticked.

## The boundary already exists twice, unnamed

ADR-0021 held the Spring slice reference out of the bundle because
cbc-slice must stay stack-free — that is this boundary, enforced
once by hand for one file. ADR-0005's two pin phrasings are the
same boundary again. Neither calls it a group, so it has to be
re-argued every time a file arrives. Naming it is most of what
Step 9 is for.

## Handed to ADR-0029

1. Three groups or four — does the container-ground middle get its
   own name, or ride with the stack?
2. If the boundary runs inside a skill, does the skill split into
   two directories, or does it stay whole with its references
   marked? The copy-whole-or-not-at-all rule pulls one way and
   the pipeline's own shape pulls the other.
3. The stack group's name: it assumes podman, PostgreSQL, Spring
   Boot and Maven. The gate says name it for the stack, not the
   tier.
4. The three `java-spring/*.part` files: they are stack files in
   the container's manuals. Which group, and does the answer move
   them.
5. `format-comparison` ships or does not — a method-about-the-work
   file, which on the about-it-beside-it rule sits beside a group
   rather than in one, and that may be the whole answer.
