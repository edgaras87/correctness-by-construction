# Commit plan: the facts-in-sync convention

## Summary — the state after all commits

How a text relies on another, and how the two are kept in
agreement, is one convention: `docs/conventions/facts-in-sync/`.
It is round 2's rule fix (`temp/refinement-2026-10-18.md`,
*Round 2*), landed before round 2 reads.

- ADR-0065 records the convention, its name and scope, and the
  options weighed.
- The manual stands on the idea-to-output model, whose §3 names
  the links, and holds:
  - **one home:** each fact has one home; elsewhere a text links
    to it, and a copy is a follower (from project-recording §11,
    rule 1);
  - **point and derive:** the two relations (from conventions
    §3.1);
  - **the fact reference:** what a line carries when it relies on
    a fact written elsewhere, its two readers, the agent and the
    walk; written today as a path and a section (from conventions
    §3.2);
  - **the rule for every description:** the list, the
    `foundation` line, the walk, named there (from conventions
    §3.5); and a description states what is true today, its history
    kept in the ADRs, the devlog and commit bodies;
  - **a disagreement:** raised and decided, either side free to be
    wrong (from conventions §3.6).
- The conventions manual keeps §2, §3.3, §3.4, §3.7 and §4, its
  numbers unchanged, with one line saying where the rest went.
  project-recording §11 keeps its pipeline, and its rule 1 points
  at the new manual.
- `one-home.md`, ours and the shipped one, and
  `foundation-check.md` stand on the facts-in-sync convention.
- `ARCHITECTURE.md` counts twelve manuals; *The words* defines the
  fact reference and the walk.
- The staying-in-step item closes. The fact-reference item stays,
  narrowed to writing a reference with its title.

## Commits

**0. `docs(agent): add commit plan for facts-in-sync`**
Opens the set.

**1. `docs: ADR-0065 the facts-in-sync convention`**
Proposed.

**2. `docs: facts-in-sync takes what keeps facts in sync`**
The new manual, in the form, and in the same commit the text it
takes leaves its old homes: conventions §3.1, §3.2, §3.5 and §3.6,
and project-recording §11's rule 1, each replaced by a pointer.
Every living reference to those sections moves to the new manual's,
and "tag" becomes "fact reference" in the docs. One move: no
commit holds the rules in two homes.

**2b. `docs: facts-in-sync trims its list, names the walk`**
The reviewer's questions on commit 2. In the new manual:
- *What this is made usable as* names each rule's path, seat,
  moment and the sections it makes usable, and no longer retells
  the rules' content;
- §4 step 3 names the walk: the greps and the re-read of each line
  they find;
- §3 drops "'Tag' is no longer used for it", and §4 says a
  description states what is true today, how it came to be being
  history's;
- §3's sweep reference points at the commit-plan convention's
  manual, `docs/conventions/commit-plan/` §2, not the container's
  skill;
- §3 says a fact reference names the home of the fact its line
  relies on: a fact has one home, so a reference has one target,
  at whatever level of the chain it lives.

**3. `chore(agent): our rules stand on facts-in-sync`**
`one-home.md` and `foundation-check.md`: their `foundation`, their
references, "tag" renamed. `convention-manual.md`'s references to
§3.1 and §3.2. Agent files, next after 2.

**4. `fix(delivery): the shipped one-home stands on facts-in-sync`**
The container's `one-home.md`: its `foundation`. The container's
decisions-log stub lists facts-in-sync among those a run
holds (conventions §4, step 3).

**5. `docs: ARCHITECTURE names facts-in-sync`**
§1.2's count and what the manuals cover; §2.3's line on which
convention owns `one-home.md`; the codemap's count; *The words*:
the fact reference, the walk, and the foundation entry's pointer.

**6. `docs: round 2's rule check ends`**
The records commit. ADR-0065 Accepted. TODO: the staying-in-step
item goes; the fact-reference item is rewritten true for today,
its remaining question the title in the written form. The
refinement file's rule check says how each doubt ended.
`TODO-CONVERSATION-MEMORY.md` §13 stays with its item.

**7. `docs(agent): close commit plan for facts-in-sync`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **The name: `facts-in-sync`.** Plain words, a subject as the
  other names have, and the words already chosen: one home per
  fact, the fact reference. Weighed: `links`, `traceability`,
  `anchors`, `lineage`, `in-sync` and `staying-in-step`, whose
  "step" is PLAN's word.
- **Scope: only what round 2's doubted rules need.** The staying-in-
  step item's other Ideas, conventions §1 to the model, *The
  words*' "model" entry, the hand-off chain's rename and a
  `requires` grep in the walk, stay in TODO, moved to the
  fact-reference item or an item of their own at commit 6.
- **The fact reference's written form stays `path §n` for now.**
  Adding the title would rewrite about 200 references, a change of
  its own; round 2 does not need it.
- **The conventions manual keeps its numbers.** §3.3, §3.4 and §3.7
  stay, so their references hold; a line under §3 names where §3.1,
  §3.2, §3.5 and §3.6 went.
- **`one-home.md` keeps its name.** The rule is one home; the
  convention is wider.
