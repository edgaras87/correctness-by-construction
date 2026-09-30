# Commit plan: one map

## Summary — the state after all commits

This repo has one map of itself, `ARCHITECTURE.md`, built mostly
from `docs/master.md`. The master is gone and every live pointer
into it points into ARCHITECTURE. The master had said of itself
that ARCHITECTURE "describes section 2 a second time". That erratum
closes by there being one map.

What the deliverer's ARCHITECTURE is, and how it differs from a
run's, is written first, as project-recording's fifth seat
difference, with an ADR. A run's ARCHITECTURE maps a built system:
modules, runtime invariants, a `src/` codemap. The deliverer's maps
documents and delivery: what is stated, what ships, how it changes,
the arrangement, what must stay true. It also carries its own words
and the list of what it knows is wrong, and runs longer than §8's
two pages for that reason. The run's seat, §8's text for a run and
the container's stub do not change.

The map says what is, not how it came to be. ARCHITECTURE's history
narration goes. Its seven invariants and the master's "what must
stay true" become one list. The codemap is re-rendered with short
rows and holds this repo's own records too. The two TODO items that
waited on this decision close.

## Commits

**1. `docs(agent): add commit plan for one map`**
This plan.

**2. `docs(adr): ADR-0044 — the deliverer's one map`**
Decision first, since it was settled in conversation. It opens as
Proposed. It records two maps of one repo and the master's own
erratum, and why ARCHITECTURE keeps the name: it is the record
project-recording defines, both seats have it, and a newcomer reads
it second. It also records why the content comes mostly from the
master, which is current and organised, and what the merge keeps
of ARCHITECTURE: its invariants. Rejected: two maps with split
roles, and keeping the master under its own name.

**3. `docs(conventions): the deliverer's ARCHITECTURE`**
project-recording's deliverer seat gains its fifth difference, and
§8 points to it. The seats' intro counts five.

**4. `docs: ARCHITECTURE takes the master's map`**
*Provisional in its cut.* ARCHITECTURE is rewritten from the master:
what is stated, what ships, how it changes, the arrangement, what
must stay true, the words, and what it knows is wrong. The two
invariant lists merge. History narration goes. The master stays for
this one commit, so the merge can be read against it.

**5. `docs: the master's pointers move, the master goes`**
The live pointers into `docs/master.md §N`, about ten across the
exchange, conventions and project-recording manuals and the tiers
model, name ARCHITECTURE's sections. `docs/master.md` is removed.
The sweep searches the unwrapped text for every old section number.

**6. `docs: the codemap re-rendered`**
*Provisional.* By `visual-comparison`, as its TODO item asked:
what a reader must get from the codemap, the candidates rendered
against it, and the one that wins. Its rows stop carrying history,
and this repo's own records join them.

**7. `docs: devlog carries one map`**
The session's entry. ADR-0044 flips to Accepted here. TODO closes
"Decide whether the master becomes ARCHITECTURE" and "Re-render the
ARCHITECTURE codemap". README's Architecture row is checked against
what the file now is.

**8. `docs(agent): close commit plan for one map`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The name is ARCHITECTURE.** It is the record both seats have, and
  the one a newcomer looks for. "Master" was a name for a working
  map, placed loose on purpose.
- **The content comes from the master.** It is the better kept of
  the two. ARCHITECTURE contributes what the master lacks, its
  invariants.
- **A content difference, not a file difference.** Both seats keep
  `ARCHITECTURE.md`. What it maps differs, and that is the seat
  rule.
- **Merge, then remove, in two commits.** Step 4 can be read against
  the master it copies. Step 5 moves the pointers and removes the
  file together, so no pointer is left dangling.
- **The word "master" stays** in the vocabulary, for the canonical
  file every copy comes from. Only the document named for it goes.
