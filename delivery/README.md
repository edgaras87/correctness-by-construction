# Delivery — how its parts land in a CBC Run

A Local Map (ADR-0045): how the parts of `delivery/` relate, and
where each lands in a CBC Run. What each part is, is
`ARCHITECTURE.md`'s (`ARCHITECTURE.md` §2, *The delivery and the CBC Runs*). How a CBC
Run is born is `delivery/installs/pure-seed.md`. How it is updated
afterwards, and how what it learns comes back, is the Exchange
Convention, `docs/conventions/exchange/`.

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

The method's own files, such as `docs/system/`, which the
cbc-framing Agent Skill writes, sit beside the records in the CBC Run,
not in place of them. Events of the method are recorded where the
container's records table and each Record Stub's header comment say.

## 2. Three ways a file lands

### 2.1 Own from birth

The container's Record Stubs, its two composed files, the Entry File
and `README.md`, its Decisions Log and its `temp/README.md`, and the
Hygiene Base, are copied once and are the CBC Run's from then on.
They are never delivered again
(`docs/conventions/exchange/` §2.4, *The records' exception*).

### 2.2 Pinned copies

- the Container Group's convention Agent Skills, Agent Rules and
  Approach on Trial;
- the Method Group's and the Stack Group's Agent Skills, Agent
  Rules and Output Shapes;
- each group's delivered Glossary Names, in `docs/glossary/`;
- the concept (§3, *The one exception*).

(`docs/conventions/exchange/` §3.2, *What goes* and §3.3, *A group's place in the tree*). They land where the container
claims nothing. The CBC Run may edit one in place, under the
Exchange Convention's rule (`docs/conventions/exchange/` §5, *Editing a copy*). A newer one
arrives by copying anew at a new Delivery Pin.

An Agent Skill's Agent Skill Templates are delivered with the Agent Skill as pinned copies. How
a CBC Run fills an Agent Skill Template, and what it does when it deviates
from one, is the Exchange Convention's (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*).

### 2.3 Delivery Fills

Text the Pure Seed writes into a file the container already put
there, which is the CBC Run's own from that moment. One exists:

| From here | Into the CBC Run |
|---|---|
| `delivery/fills/cbc-run-pure-playbook.md` | its Plan Steps replace everything between the PLAN Record Stub's STEPS markers. The "Steps from:" line names it at the Delivery Pin (`delivery/installs/pure-seed.md` step 4). The CBC Run holds no copy of the playbook. |

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
| `.claude/CLAUDE.md` and `README.md` carry bodies composed here, not Record Stubs | they hold two stances a CBC Run can only receive: the paragraph that forbids method work before CBC Framing, and the line that says the concept is a pinned copy. Nothing before the CBC Run Briefing produces them (ADR-0019). Each is a whole file, copied, never merged (ADR-0015). |
| `.claude/decisions.md`'s birth entry carries one Delivery Pin and a Read-Through Commit | the Delivery Pin is ours (ADR-0025); the Read-Through Commit is the Exchange Convention's second number (ADR-0036) |

In the two composed files, the title line, the records table
and the header comments are the Record Stubs' own form.

## 5. What a CBC Run does not get

Its own decisions, its own `temp/RUN-n.md` files that brief the next CBC Run, and its own versioning: they
are the CBC Run's to make. Nor the agent definitions of the archive
repo the concept came from, since the Agent Skills carry the method
whole (ADR-0006). A CBC Run on another stack
also takes no `spring-postgres/` (`docs/conventions/exchange/` §3.4, *One group per file*).

## 6. When it lands

Everything copies at birth, including the Agent Skills for phases
that run much later. The Stage 0 of the cbc-slice Agent Skill and of the Stack Group's three Agent Skills refuses to start
before its inputs exist, so an early copy is inert. And one moment
keeps the whole set at one Delivery Pin. The CBC Run's Plan Steps,
and which Agent Skill each opens, come from the playbook,
`delivery/fills/cbc-run-pure-playbook.md`. Only the infra-serve Agent Skill, for an Infrastructure Service Re-entry,
arrives unplanned, and its own trigger covers that.
