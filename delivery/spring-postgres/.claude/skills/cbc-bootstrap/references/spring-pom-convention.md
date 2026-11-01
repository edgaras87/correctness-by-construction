# Spring pom convention — how the pom is written and kept

Scope: Spring Boot on Maven, the Boot 4 line. It governs the pom's
**shape** only. Which dependencies are chosen is the CBC Bootstrap's
decision. When they enter is the implementer's judgment, under the
rule below.

## The governing rule

**A dependency enters only at the step or Invariant Slice that needs
it: nothing ahead of need.** The pom records what the system has
proven it requires. It is not a list of what might be needed. The
CBC Bootstrap's first set is deliberately small. The Adversity
Harness, the driver and every later library arrive at their own
commits, each with the reason it is needed written in the file.

## Every entry carries its why

The inheriting reader's question is never *what*: the coordinates
say that. It is ***why is this here***.

- **Every runtime dependency carries a comment above it.** It says
  what capability the dependency gives, in the project's own terms:
  what the system does with it, and, where a decision hangs on it,
  which boundary or guarantee it serves. Capability, not where the
  requirement came from.
- **Every test companion carries its own line.** Some companions
  exist only to satisfy another module's auto-configuration. Then the
  comment says so plainly. That comment is the only thing between the
  next reader and a puzzling removal.
- **Every plugin carries a comment** on why it is configured, and
  what its configuration changes. A plugin with default behavior and
  no reason to be there is removed, not commented.
- **Comments state facts and reasons, never instructions to a
  reader.**
- **No dependency whose reason cannot be written honestly.** If the
  comment cannot be written, the dependency is not needed.

## Grouping and order

Group by **the capability served,** never by scope, with a blank
line between groups. Within a group: the runtime dependency first,
and its test companion right after, so the pairing is visible at a
glance. A pom sorted by scope (all compile, then all test) scatters
the dependencies of one capability.

The Boot 4 pairing rule is stated **once,** as a block comment above
the dependency section: runtime starters pair with their `-test`
companions. Where no companion exists, the runtime dependency stands
alone, and the gap is left uncommented: its absence is not a
decision.

## What the file does not carry

- No generated empty metadata: `<url/>`, `<licenses>`, `<developers>`
  and `<scm>` are deleted unless actually populated.
- `<description>` is filled from the project's CBC Framing Intent:
  one line, in the problem's language, not the artifact's name
  restated.
- Versions are the parent's, wherever the parent manages them. An
  explicit version is itself a decision, and carries a comment saying
  why.

## Afterwards

Every Invariant Slice that adds a dependency writes it the same way:
the same grouping, the same written reason.
