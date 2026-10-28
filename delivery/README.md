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

A shape travels with the group of the thing it shapes, as a copy
into the run's `.claude/shapes/`; the rest is
`docs/conventions/shapes/` §4.

## 2. Three ways a file lands

- **The run's own from birth.** The container's record stubs, its
  two entry files, its decisions log, its hygiene files and its
  `temp/README.md` are copied once and are the run's from then on.
  They never travel again.
- **Pinned copies.** The container's convention skills, rules and
  approach on trial; the method's and the stack practice's skills,
  rules and shapes; and the concept, at `docs/concept/`
  (`docs/conventions/exchange/` §3.2 and §3.3). They land where the container
  claims nothing. The run may edit one in place, under the
  exchange's rule (`docs/conventions/exchange/` §5); a newer one
  arrives by copying anew at a new pin.
- **Fills.** Text the seed writes into a file the container already
  put there, which is the run's own from that moment. One exists:

| From here | Into the run |
|---|---|
| `delivery/fills/cbc-run-pure-playbook.md` | its steps replace everything between the PLAN stub's STEPS markers, and the "Steps from:" line names it at the pin (`delivery/installs/pure-seed.md` step 4); the run holds no copy of the playbook |

A skill's `templates/` travels with the skill as a pinned copy. How
a run fills a skill's template, and what it does when it deviates
from one, is the exchange's (`docs/conventions/exchange/` §5.8, *A
skill's template is filled, not edited*).

The method's own artifacts, such as `docs/system/`, which
cbc-framing writes, sit beside the records in the run, not in place
of them. CbC events are recorded under the container's record rules.

## 3. The one exception

| From here | Into the run |
|---|---|
| `concept/` | `docs/concept/`, read `docs/concept/00-cbc.md` first |

Here the concept is the repo's subject, so it sits at the root. In a
run it is a pinned reference beside the run's own work
(`docs/conventions/exchange/` §3.3).

## 4. What the container holds that its tree does not show

| What | Why |
|---|---|
| `CLAUDE.md` is at `.claude/CLAUDE.md`, not at the root | a run builds an app, and the root is the app's |
| `.claude/CLAUDE.md` and `README.md` carry bodies composed here, not stubs | they hold two stances a run can only receive, the pre-framing guard and the pin stance: nothing before the briefing produces them (ADR-0019); each is a whole file, copied, never merged (ADR-0015) |
| `.claude/decisions.md`'s birth entry carries one pin and a read-through | the pin is ours (ADR-0025); the read-through is the exchange's second number (ADR-0036) |

In the two composed entry files, the title line, the records table
and the standing comments are the stubs' own shape.

## 5. What a run does not get

Its own decisions, its own run files and its own versioning, which
are the run's to make; and the archive's agent definitions, since
the skills carry the method whole (ADR-0006). A run on another stack
also takes no `spring-postgres/` (`ARCHITECTURE.md` §2.2).

## 6. When it lands

Everything copies at birth, including the skills for phases that
run much later. Each practice skill's readiness gate refuses to start
before its inputs exist, so an early copy is inert, and one moment
keeps the whole set at one pin. The run's plan steps, and which skill
each opens, come from the playbook,
`delivery/fills/cbc-run-pure-playbook.md`. Only infra-serve, re-entry,
arrives unplanned, and its own trigger covers that.
