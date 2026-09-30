# Commit plan: local maps

## Summary — the state after all commits

`delivery/README.md` is a local map: how the parts of `delivery/`
relate and land in a run, and nothing else. It holds the groups as
pieces of the run's tree, the one exception (`concept/` to
`docs/concept/`), where fills land, which copies are pinned and
which become the run's own, what the container holds that its tree
does not show, and pointers to when each moves. Its history and its
restatements of ARCHITECTURE §2, the exchange and project-recording
are gone, each one checked against its home first. Its one lived
lesson, "ask what the run teaches the worked example", lives in the
exchange's §6.3, the reading.

With the conventions index, that is two local maps, the pair. The
rule is written from them: an ADR; "local map" in ARCHITECTURE's
words; and project-recording §8 saying when an area gets one and
what it holds. Relations only, no counts, nothing a part says about
itself, and pointed into by the map. The TODO item waiting on this
reading closes, and the full local map of all nine conventions
becomes due.

## Commits

**1. `docs(agent): add commit plan for local maps`**
This plan.

**2. `docs(conventions): the worked example, at the read`**
The lesson lives only in `delivery/README.md`, which step 3
trims. It moves first, to the exchange's §6.3, the reading, as a
dated lesson, so no commit removes it before it has a home.

**3. `docs: delivery/README becomes a local map`**
*Provisional in its cut.* Material first: the file is rewritten to
its relations. Each passage that goes is checked against where it
lives:
- The groups, and what another stack gets: ARCHITECTURE §2 and
  §2.2. The file said the second of these three times.
- Birth and update: ARCHITECTURE §2.4 and §2.5, and the exchange.
- Harvest: the exchange's §6 and ARCHITECTURE §2.5.
- The citation rule: project-recording §3.5.
- Templates: ARCHITECTURE §2.2.
- The contract and the renames: ADR-0024, ADR-0029 and the devlog.

The provenance header names `installs/cbc.md`, which no longer
exists, and goes. So do "v5" and "kit facts". The title stops
saying "at birth".

**4. `docs(adr): ADR-0045 — a local map`**
The rule, written from the pair, opens as Proposed. An area whose
parts relate in ways the map should not carry gets a `README.md`
that is a local map: relations only, no counts, nothing a part says
about itself, pointed into by the map. The file keeps the name
`README.md`, because the name is the tool's and the content is
ours. Not every README is one: `temp/README.md` holds rules.

**5. `docs(conventions): a local map, in §8`**
project-recording §8, which holds ARCHITECTURE, gains the local map
as a part of its own. It is numbered by form, so every part of §8
is numbered. ARCHITECTURE's words gain "local map", and its §1.2
and §2.4 name the two it points into. The container's ARCHITECTURE
stub does not change, since no run has an area that needs one yet.

**6. `docs: devlog carries local maps`**
The session's entry. ADR-0045 flips to Accepted. TODO closes
"Read `delivery/README.md` against ARCHITECTURE §2". "Make the
conventions index a full local map" moves to Next, due, to be built
to the rule in a set of its own.

**7. `docs(agent): close commit plan for local maps`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Material first, the rule after.** The rule is written from two
  real local maps, not from the idea of one, which is the pair our
  shapes rule asks for.
- **The lesson moves before the file shrinks**, so no commit loses
  it.
- **The rule is in §8, for both seats.** A run's own areas may need
  a local map too. Its ARCHITECTURE stub waits for one that does.
- **The full local map of the conventions is not in this set.** It
  needs `visual-comparison`, and it gets its own.
