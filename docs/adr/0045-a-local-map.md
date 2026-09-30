# 0045. A local map

Date: 2026-09-30
Status: Accepted (2026-09-30, at the set's records commit; opened
Proposed under the commit plan for local maps)

## Context

`ARCHITECTURE.md` is this repo's one map (ADR-0044). It says what
each area is, and points into it. Two directories hold a README
that the map points at, and on 2026-09-30 both were read and cut
down to the same kind of content.

- **`docs/conventions/README.md`, the index.** It held a table
  restating each manual's artifacts, and one row had drifted. It
  also held a list of names and paths the folder already shows. Cut
  down, it holds the chain: how the conventions that act in
  sequence during a piece of work hand to each other. Nothing else
  holds that.
- **`delivery/README.md`.** 207 lines, about a third of them
  relations and the rest restatement and history. Cut to 86, it
  holds how the delivery's parts land in a run: groups as pieces of
  the run's tree, three ways a file lands, the one exception, what
  the container holds that its tree does not show. Nothing else
  holds that either.

The reviewer called these small architectures. Both are what the
map should not carry, because it is detail about one area, and both
decayed the same way: by retelling what the map, a manual or the
exchange already says.

A third directory README, `temp/README.md`, holds the rules for
`temp/`. It is not a map.

## Options considered

- **Put the relations into ARCHITECTURE.** Rejected: the map
  becomes a wall, which is the defect §3.2 of the conventions manual
  names, and ADR-0044 kept the map to what each area is.
- **Name the file `MAP.md`, or a nested `ARCHITECTURE.md`.**
  Rejected. A directory's `README.md` is what GitHub and the IDE
  show on arriving at the folder, and a nested ARCHITECTURE would
  compete with the root one. As with `CLAUDE.md`, the name is the
  tool's and the content is ours.
- **A rule for every README.** Rejected: `temp/README.md` is
  another kind, and a rule for all READMEs would govern it wrongly.
- **No rule.** Rejected: two local maps decayed the same way, and
  our shapes rule takes a pair as the evidence.

## Decision

1. **An area whose parts relate in ways the map should not carry
   gets a local map**: its directory's `README.md`, which the map
   points into.
2. **A local map holds relations only** — how the area's parts
   connect, hand work to each other, or land elsewhere. It holds no
   count and no list the map holds, and nothing a part says about
   itself. It points for the rest.
3. **It keeps the name `README.md`.** The name is the tool's; that
   it is a local map is what its first lines say.
4. **Not every README is a local map.** One that holds a folder's
   rules, like `temp/README.md`, is another kind, and this decision
   does not govern it.
5. **The rule is project-recording's, in §8** beside ARCHITECTURE,
   and "local map" joins ARCHITECTURE's words. Both seats hold it. A
   run's ARCHITECTURE stub is unchanged until a run has an area that
   needs one.

## Consequences

- The two local maps are the conventions index and
  `delivery/README.md`. ARCHITECTURE §1.2 and §2.4 point into them.
- "Make the conventions index a full local map" becomes due: all
  nine conventions and how each touches the others. Its trigger was
  this pair.
- A new directory gets a README only when its parts relate in ways
  worth mapping. `concept/`, `docs/adr/` and `docs/models/` have
  none, and need none.
