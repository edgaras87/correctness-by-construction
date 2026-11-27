# <working-name>

A backend built by [correctness-by-construction](docs/concept/).
Its design is derived from one Falsifiable Promise, by asking what
must never happen before what it should do. Every invariant is held
by a Structural Wall, and an Evidence Test that creates its
adversity proves the Structural Wall. The problem is not yet chosen. It arrives
with the CBC Run Briefing that opens CBC Framing, and this paragraph
is then derived again from the CBC Framing Intent
([PLAN.md](PLAN.md), Step 1). Until then the repository holds the
method, the plan and the records, and no code.

The method: [docs/concept/](docs/concept/), a pinned copy of the
concept; start with [00-cbc.md](docs/concept/00-cbc.md).

## Project records

| Record | Where | What it answers |
|---|---|---|
| Plan | [PLAN.md](PLAN.md) | Where are we, what's next, what does *done* mean |
| Decisions | [docs/adr/](docs/adr/) — cited from other repos as `<TAG> ADR-nnnn` | Why is it built this way |
| Architecture | [ARCHITECTURE.md](ARCHITECTURE.md) | What is the current shape of the system |
| System | [docs/system/](docs/system/) | What is promised, what must never happen, what the Invariant Slices are |
| Backlog | [TODO.md](TODO.md) | What's known but not done |
| Changelog | [CHANGELOG.md](CHANGELOG.md) | What changed per version (for users) |
| Devlog | [devlog/](devlog/) | Day-to-day work, dead ends, open questions |

<!-- A line here is true now, and meant for someone arriving from
     outside. What changes weekly is PLAN.md's. Why is the ADRs'. How
     it went is the devlog's. A missing section is not an omission. It
     arrives when a Plan Step Gate makes it true, since the README says
     only what is already true. Once the project runs: its prerequisites, the one command
     that builds and runs it from a clean clone, and how to run its
     tests, each when it becomes true.
     Born from the Backend Kit's Record Stub for the README: this repo's
     own from birth, never a Kit Copy. Why its form is as it is:
     records, in CBC backend design, kept in the Maintainer Repo. -->
