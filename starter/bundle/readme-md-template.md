<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Composed 2026-09-06, user's design: a reusable
     README for a possible semi-pure install — one that ships
     filled entry files (this and claude-md-template.md) while
     the rest of the birth stays pure (the TODO item holds the
     idea; no such install exists yet).
     — the kit half: engineering-handbook starter/kit/README.md
       @ c670fe5 — the records table and both its comments,
       verbatim. The kit's fill-comment (the purpose paragraph
       replaces it) is consumed here at composition, per its own
       rule; the title placeholder is renamed to the CLAUDE
       template's <working-name> slot, one name filled once by
       the seed. At each kit re-pin, re-verify this half against
       their README stub at the new pin.
     — the fills: harvested from run-1's own derivation
       (cbc-pure-run README @ c3ffda8, grown unaided from the
       kit stub), a run's words taken consciously — the trade
       the semi-pure shape makes on purpose. One correction
       made and reverted: the run's "a backend" was read as a
       pre-framing presumption and neutralized to "a system",
       then restored 2026-09-06 after the run-2 reading — the
       word is the skills' own (their description lines say
       backend, and their bodies are backend-born), so it names
       the toolkit, not the problem; the CLAUDE template says
       the same. Revisit at the first non-backend run (TODO
       Later). The
       temporary paragraph survives harvest because it is true
       for every newborn at delivery time and names its own end
       (Step 1) — the entry-file retirement rule's shape.
     Use: parked, undelivered — no install delivers this file;
     it waits beside claude-md-template.md for the semi-pure
     install if one is designed, and run 2's README derivation
     is a comparison object against this harvest in the
     meantime.
     Authoring: every edit to the body below answers to the
     copy's own closing comment, read at authoring time — a
     line here must be true at birth for every project, meant
     for someone arriving from outside; what only one run made
     true stays out. -->

# <working-name>

A correctness-by-construction run: a backend whose design is
derived from one falsifiable promise — asking what must never
happen before what it should do — and whose every invariant is
closed by a test that creates its adversity. The problem is not
yet chosen. It arrives with the framing briefing, and this
paragraph is then re-derived from the framed intent
([PLAN.md](PLAN.md), Step 1). Until then the repository holds
the method, the plan, and the records — no code.

The method: [docs/concept/](docs/concept/), a pinned copy of the
correctness-by-construction concept in five chapters; start with
[00-cbc.md](docs/concept/00-cbc.md).

## Project records

| Record | Where | What it answers |
|---|---|---|
| Plan | [PLAN.md](PLAN.md) | Where are we, what's next, what does *done* mean |
| Decisions | [docs/adr/](docs/adr/) | Why is it built this way |
| Architecture | [ARCHITECTURE.md](ARCHITECTURE.md) | What is the current shape of the system |
| Backlog | [TODO.md](TODO.md) | What's known but not done |
| Changelog | [CHANGELOG.md](CHANGELOG.md) | What changed per version (for users) |
| Devlog | [devlog/](devlog/) | Day-to-day work, dead ends, open questions |

<!-- A line here is true now, and meant for someone arriving from
     outside. What changes weekly is PLAN.md's; why is the ADRs'; how
     it went is the devlog's. A missing section is not an omission: it
     arrives when a step's gate makes it true — projection follows
     truth. -->
