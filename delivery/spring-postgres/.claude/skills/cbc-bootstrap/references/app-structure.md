<!-- A reference: read and imitated, never copied and filled. -->

# App structure — the choice made at the CBC Bootstrap

How the application's packages are shaped is a **CBC Bootstrap
decision.** It is made and recorded exactly as the stack decision
is: in an ADR, with its why, before the code that lives under it. The
recorded decision governs **all later code, Invariant Slice work
included.** Invariant Slices enter the structure decided here. They
do not decide it again.

This doc carries three things:

- the Stack Default;
- the decision rule;
- the meaning of the named alternatives.

So the choice is made knowingly, can be recalled months later, and
means the same thing to the person and the agent.

**It owns nothing else.** What classes exist is the Invariant Slices'
outcome. What enters the build is `spring-pom-convention.md`'s. This doc owns
only the *shape they land in*.

## The Stack Default

**Package-by-feature, package-private boundaries, structural depth
earned per feature.** One CBC Run used it across nine Invariant
Slices:

```
<base-package>                main
├── <feature-a>/     FeatureAController, FeatureADomainClass
└── <feature-b>/     ...

<base-package>                test
├── adversity/       creates the danger for real: races, bursts of duplicates, killed processes
├── folds/           an Invariant Slice Fold's fact shown by running the system, no attack
├── structure/       reads the code: an Invariant Slice Guarantee held by an absence
├── store/           the store's own refusals, and the migration path
├── door/            the HTTP contract: each answer and its status
├── testsupport/     the Adversity Harness's base classes (harness reference), and its own test
└── <feature-a>/     a unit test that needs the feature's package access
```

- **One package per Responsibility Area,** holding everything that
  Responsibility Area needs. The package list reads as the problem's
  table of contents, not as a list of technical roles.
- **Classes are package-private by default** (`class Foo`, not
  `public class Foo`). Only what another feature really calls becomes
  public. The compiler enforces the boundary: enforcement over
  convention, the same stance as the Database Role Split.
- **Depth is earned per feature, never stamped.** A feature starts
  with as few classes as its Invariant Slice needs. One feature a CBC
  Run built had a controller and a domain class. An internal service
  or persistence split appears inside one feature when that feature's
  own complexity earns it, and nowhere else. Layers inside a feature
  are allowed. A layer template across the whole repo is provisioning
  ahead of need.
- **Tests are placed by the kind of check they are,** never by
  Invariant Slice. An Invariant Slice is the order of building, and
  one test may serve several. A test that mixes kinds goes by its
  main job. The folder answers "show me every race test", or "I
  changed the door: what checks it?". Which test proves which
  Invariant Slice Guarantee is the Invariant Slice Record's. The CBC Bootstrap's
  first tests go in from the start: the CBC Bootstrap Probe in
  `adversity/`, the Migration Path Test in `store/`. These test
  packages were laid out after one CBC Run's Invariant Slices. No CBC
  Run has yet laid them out from its CBC Bootstrap.

This is the shape a CBC Run gets when its ADRs say nothing else.

## The decision rule

- **Decided at the CBC Bootstrap, recorded with its why.** As with
  the stack, the Invariant Slices rarely tell structures apart. So
  the deciding inputs are the CBC Run's own: fluency, audience, and
  a stated intent. *"This CBC Run practices pattern X"* is a
  legitimate deciding input when it is written down.
- **Departing from the Stack Default is off-default,** as departing
  from an Agent Skill Template is. Derive from the chosen pattern's
  own logic, and record the deviation as delivered-copies rule 8 says
  (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is…*).
  What you learn comes back into this doc.
- **The first CBC Run to use an alternative makes it used.** Its
  entry below then stops being a meaning only, and gains a line on
  how it went, when a later delivery brings that back into this doc.

## The named alternatives, none used by a CBC Run yet

Each entry is what the name *means*, in two lines, not an
endorsement. A deeper weighing is a conversation, not this doc.

- **Classic layered** *(no CBC Run has used it)*. Packages by
  technical role (`controller/`, `service/`, `repository/`), and a
  request flows down the layers. The long-standing enterprise
  default: every class is public across layer packages, so the
  boundaries are convention.
- **Hexagonal, onion, clean** *(no CBC Run has used it)*. Domain
  logic in the center with no framework imports, and every external
  thing (DB, HTTP, queues) behind a port interface, with an adapter
  at the edge. It pays when many integrations need swapping or
  faking. It costs interfaces and mapping everywhere.
- **Vertical-slice architecture** *(no CBC Run has used it)*.
  Package-by-feature taken down to each use case: each use case its
  own top-to-bottom package, sharing almost nothing. Of the four, the
  closest to the Stack Default.
- **Modular monolith, Spring Modulith** *(no CBC Run has used it)*.
  The Stack Default plus tooling: an explicit API per module,
  verified boundaries, tests per module. The step to consider when
  features multiply and package-private stops being enough.

## What this doc does not carry

- **Essays of pros and cons.** They can be derived again in
  conversation at the moment of choice, and here they would go stale.
  The two lines above are for recall and shared words only.
- **Application code.** It is the CBC Run's, always. The harness
  reference, `.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`,
  is the only exception that carries code.
