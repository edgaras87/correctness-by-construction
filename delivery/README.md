# Delivery — how its parts land in a CBC Run

A Local Map (ADR-0045): how the parts of `delivery/` relate, and
where each lands in a CBC Run. What each part is, is the map's
(`ARCHITECTURE.md` §2, *The delivery and the CBC Runs*). How a CBC Run is born is `delivery/installs/pure-seed.md`; how it is
updated afterwards, and how what it learns comes back, is the
Exchange Convention, `docs/conventions/exchange/`.

## 1. The groups and the tree

`container/`, `method/` and `spring-postgres/` are each laid out as
the part of the CBC Run's tree they land as: inside `delivery/<group>/`,
every path is the path it lands at. So
`delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/`, and the three copied on top of one
another *are* the CBC Run's tree. No mapping, and nothing to forget. A
group is left out by not naming its directory (ADR-0029, ADR-0036).

An Output Shape travels with the group of the thing it shapes, as a copy
into the CBC Run's `.claude/shapes/`; the rest is the shapes manual's
(`docs/conventions/shapes/` §4, *An Output Shape between repos*).

## 2. Three ways a file lands

- **The CBC Run's own from birth.** The container's Record Stubs, its
  two entry files, its Decisions Log, its hygiene files and its
  `temp/README.md` are copied once and are the CBC Run's from then on.
  They never travel again.
- **Pinned copies.** The container's convention skills, Agent Rules and
  Approach on Trial; the method's and the stack practice's skills,
  Agent Rules and Output Shapes; and the concept, at `docs/concept/`
  (`docs/conventions/exchange/` §3.2, *What goes* and §3.3, *A group's place in the tree*). They land where the container
  claims nothing. The CBC Run may edit one in place, under the
  Exchange Convention's rule (`docs/conventions/exchange/` §5, *Editing a copy*); a newer one
  arrives by copying anew at a new Delivery Pin.
- **Delivery Fills.** Text the Pure Seed writes into a file the container already
  put there, which is the CBC Run's own from that moment. One exists:

| From here | Into the CBC Run |
|---|---|
| `delivery/fills/cbc-run-pure-playbook.md` | its Plan Steps replace everything between the PLAN Record Stub's STEPS markers, and the "Steps from:" line names it at the Delivery Pin (`delivery/installs/pure-seed.md` step 4); the CBC Run holds no copy of the playbook |

A skill's Skill Templates travel with the skill as pinned copies. How
a CBC Run fills a Skill Template, and what it does when it deviates
from one, is the Exchange Convention's (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*).

The method's own artifacts, such as `docs/system/`, which
cbc-framing writes, sit beside the records in the CBC Run, not in place
of them. CbC events are recorded under the container's record rules.

## 3. The one exception

| From here | Into the CBC Run |
|---|---|
| `concept/` | `docs/concept/`, read `docs/concept/00-cbc.md` first |

Here the concept is the repo's subject, so it sits at the root. In a
CBC Run it is a pinned reference beside the CBC Run's own work
(`docs/conventions/exchange/` §3.3, *A group's place in the tree*).

## 4. What the tree does not show

| What | Why |
|---|---|
| `CLAUDE.md` is at `.claude/CLAUDE.md`, not at the root | a CBC Run builds an app, and the root is the app's |
| `.claude/CLAUDE.md` and `README.md` carry bodies composed here, not Record Stubs | they hold two stances a CBC Run can only receive, the pre-framing guard and the pin stance: nothing before the Run Briefing produces them (ADR-0019); each is a whole file, copied, never merged (ADR-0015) |
| `.claude/decisions.md`'s birth entry carries one Delivery Pin and a Read-Through Commit | the Delivery Pin is ours (ADR-0025); the Read-Through Commit is the Exchange Convention's second number (ADR-0036) |

In the two composed entry files, the title line, the records table
and the standing comments are the Record Stubs' own form.

## 5. What a CBC Run does not get

Its own decisions, its own run files and its own versioning, which
are the CBC Run's to make; and the archive's agent definitions, since
the skills carry the method whole (ADR-0006). A CBC Run on another stack
also takes no `spring-postgres/` (`ARCHITECTURE.md` §2.2, *The Stack Group…*).

## 6. When it lands

Everything copies at birth, including the skills for phases that
run much later. Each practice skill's readiness gate refuses to start
before its inputs exist, so an early copy is inert, and one moment
keeps the whole set at one Delivery Pin. The CBC Run's Plan Steps, and which skill
each opens, come from the playbook,
`delivery/fills/cbc-run-pure-playbook.md`. Only infra-serve, re-entry,
arrives unplanned, and its own trigger covers that.
