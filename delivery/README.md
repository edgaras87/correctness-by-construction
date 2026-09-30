# Delivery — how its parts land in a run

A local map (ADR-0045): how the parts of `delivery/` relate, and
where each lands in a run. What each part is, is `ARCHITECTURE.md`
§2. How a run is born is `delivery/installs/pure-seed.md`; how it is
updated afterwards, and how what it learns comes back, is the
exchange, `docs/conventions/exchange/`.

## 1. The groups are pieces of the run's tree

`container/`, `method/` and `spring-postgres/` are each laid out as
the part of the run's tree they land as: inside `delivery/<group>/`,
every path is the path it lands at. So
`delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/`, and the three copied on top of one
another *are* the run's tree. No mapping, and nothing to forget. A
group is left out by not naming its directory (ADR-0029, ADR-0036).

A shape travels with the group of the thing it shapes (ADR-0035).
Only an exposed one travels, as a pinned copy into the run's
`.claude/rules/`. What happens to unexposed ones is
`docs/conventions/shapes/` §4.

## 2. Three ways a file lands

- **The run's own from birth.** The container's record stubs, its
  two entry files and its hygiene files are copied once and are the
  run's from then on. They never travel again.
- **Pinned copies.** The convention skills and rules in the
  container, and every skill in `method/` and `spring-postgres/`,
  land where the container claims nothing. The run never edits them
  in place; a newer one arrives by copying anew at a new pin.
- **Fills.** Text the seed writes into a file the container already
  put there, which is the run's own from that moment. One exists:

| From here | Into the run |
|---|---|
| `delivery/fills/cbc-run-pure-playbook.md` | its steps replace everything between the PLAN stub's STEPS markers, and the "Steps from:" line names it at the pin (`pure-seed.md` step 4); the run holds no copy of the playbook |

A skill's `templates/` travels with the skill as a pinned copy. At
use, the run copies a template to the path its walkthrough names and
fills it, and the filled file is the run's own (ADR-0008). A change
to a template's shape comes back like any other change to a skill.

The method's own artifacts, such as `docs/system/`, which
cbc-framing writes, sit beside the records in the run, not in place
of them. CbC events are recorded under the container's record rules.

## 3. The one exception

| From here | Into the run |
|---|---|
| `concept/` | `docs/concept/`, read `00-cbc.md` first |

Here the concept is the repo's subject, so it sits at the root. In a
run it is a pinned reference beside the run's own work.

## 4. What the container holds that its tree does not show

| What | Why |
|---|---|
| `CLAUDE.md` is at `.claude/CLAUDE.md`, not at the root | a run builds an app, and the root is the app's |
| `.claude/CLAUDE.md` and `README.md` carry bodies composed here, not stubs | runs did not derive the pre-framing guard or the pin stance unaided (ADR-0019); each is a whole file, copied, never merged (ADR-0015) |
| `.claude/decisions.md`'s birth entry carries one pin and a read-through | the pin is ours (ADR-0025); the read-through is the exchange's second number (ADR-0036) |

In the two composed entry files, the title line, the records table
and the standing comments are the stubs' own shape. The rest is this
repo's, taken from what the runs derived.

## 5. What a run does not get

Its own decisions, its own run files and its own versioning, which
are the run's to make; and the archive's agent definitions, since
the skills carry the method whole (ADR-0006). A run on another stack
also takes no `spring-postgres/` (ARCHITECTURE §2.2).

## 6. When it lands

Everything copies at birth, including the skills for phases that
run much later. Each practice skill's readiness gate refuses to start
before its inputs exist, so an early copy is inert, and one moment
keeps the whole set at one pin. The run's plan steps come from the
playbook, whose middles are the pipeline, cbc-framing to
infra-establish to cbc-bootstrap to cbc-slice. Each step's gate is
derived when the step opens. Only infra-serve, re-entry, arrives
unplanned, and its own trigger covers that.
