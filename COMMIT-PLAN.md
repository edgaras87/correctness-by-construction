# Commit plan: the fact reference rewrite

## Summary — the state after all commits

Every fact reference in living text takes the form ADR-0070 settled
(`docs/conventions/facts-in-sync/` §3.1, *What it is*): a path from
the root, a section and its title, in parentheses. TODO's "Write
down how a fact reference is written, then rewrite each one to it"
is worked, and leaves TODO.

Measured 2026-10-28, at its opening, in living text:

| Layer | Files | Path and section | Same document, (§n) | "Pointer" |
|---|---|---|---|---|
| The manuals | 12 | 119, 22 titled | 78, 7 titled | 13 |
| The models and the concept | 8 | 6, 1 titled | 27, 6 titled | 5 |
| The records | 9 | 110, 7 titled | 19 | 6 |
| Ours | 18 | 63, 20 titled | 12 | 6 |
| What ships | 56 | 14, 2 titled | 3 | 7 |

So 260 references with a path and 126 in the same document gain a
title; the 65 written since 2026-10-27 already carry one. Besides
these:
- references that are part of their sentence move into parentheses,
  and the sentence is reworded so it says its point in words;
- 41 paths inside skills run from the root (FINDING-219);
- 13 shipped rules named in prose take a reference (FINDING-220);
- a derived file's lines take references to its foundation:
  our record headers (FINDING-191), our rules and skills (196);
- shipped retellings of our manuals take a CBC reference and stand
  alone (FINDING-202, 204, 216).

History is not touched: the devlog, closed ADRs, `temp/`,
`docs/baselines/`, the entries of `.claude/decisions.md`, the parts
of `TODO-CONVERSATION-MEMORY.md`, and `CHANGELOG.md`'s released
entries.

## Commits

**0. `docs(agent): add commit plan for ref rewrite`**
Opens the set; the draft in `temp/` goes.

**0b. `docs: facts-in-sync gives a step or rule its form`**
§3.1 gains the case its five cases lack: a numbered step or rule
stays after the title.

**Two passes per layer.** The first adds titles by script, nothing
else. The second is by hand: parentheses and the reworded sentences,
"pointer", and the layer's findings.

### The manuals

**1. `docs: the manuals' references carry titles`**
Scripted.

**2. `docs: the manuals' references read as addresses`**
By hand.

### The models and the concept

**3. `docs: models and concept take the settled form`**
Both passes in one commit: 21 references and 5 uses of "pointer".

### The records

**4. `docs: the records' references carry titles`**
Scripted: `TODO.md`, `ARCHITECTURE.md`, the glossary, `README.md`,
`PLAN.md`, `CHANGELOG.md`'s unreleased entries, `docs/adr/README.md`,
the conventions index.

**5. `docs: the records' references read as addresses`**
By hand, and FINDING-191: each record header's lines about its own
foundation take a reference to the part they use.

### Ours

**6. `chore(agent): our references carry titles`**
Scripted.

**7. `chore(agent): our references read as addresses`**
By hand, and FINDING-196: our rules and skills take references to
the parts of their foundation they use.

**7b. `docs: ADR-0072 one reference per section`**
Inserted: ADR-0070's trigger fired in commit 7. In `writing.md` every
rule comes from one part of its manual, so a reference per line would
repeat one address eight times. The reviewer chose one reference per
section of a derived file where its lines share a part. ADR-0072
changes ADR-0070's decision 7.

**7c. `docs: facts-in-sync says a section may carry it`**
Inserted: facts-in-sync §4 step 2 says so.

### What ships

**8. `fix(delivery): shipped references take the form`**
Both passes: 17 references and 7 uses of "pointer".

**9. `fix(delivery): skill paths run from the root`**
FINDING-219: 41 paths inside skills.

**10. `fix(delivery): shipped lines name their sources`**
FINDING-220, rules named in prose; 202, 204 and 216, retellings of
our manuals, each with a CBC reference and standing alone.

**10b. `chore(agent): approach drafting points at commit-messages`**
Inserted: `approach-drafting.md` is one text in both seats
(ADR-0069), and commit 10 changed the container's copy; ours takes
the same line.

### Records and close

**11. `docs: TODO's fact reference item is worked`**
The item leaves TODO.

**12. `docs(agent): close commit plan for ref rewrite`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit
that changes a description walks what stands on it; a derived file
that then disagrees gets a lettered commit after it.

## Decisions for you to object to

- **Measured again at its opening,** 2026-10-28: the numbers above.
- **A script adds the titles; a person does the rest.** The script
  runs from the scratchpad, never from the repo. For each reference
  it finds the heading the path and number name, and writes its
  title. What it cannot resolve it lists, and that list is worked by
  hand in the same commit. Before and after, it counts headings,
  front matter and code fences in each file, which must not change.
- **A long title is cut** at a word boundary to 30 characters or
  fewer, ending in "…". 32 of 252 numbered titles run longer.
- **A step or a numbered rule stays after its title:**
  (`docs/conventions/facts-in-sync/` §4, *The rule for every
  description*, step 3); (`.claude/rules/delivered-copies.md`, rule
  8, *A skill's template is copied and filled*). Facts-in-sync §3.1
  gains the case first, in 0b.
- **In a comment, a title carries no asterisks:** an HTML comment, a
  YAML or SQL line shows them as written.
- **A run's ids are not touched.** Decision 4 keeps them bare.
- **By layer, two passes each,** so a scripted diff holds titles
  only and reads in one look, and the hand diff holds only what a
  person changed. The small layers take one commit.
- **No `CHANGELOG.md` entry.** The concept's changes are editorial,
  and ride with the next version, as its standing comment says.
