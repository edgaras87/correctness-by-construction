---
foundation: the facts-in-sync convention
---

# One home per fact

**Governs:** where a fact is written in records, comments and
config. Where it lives, never how it reads.

<!-- No paths: line, so this loads at the start of every session:
     a fact can be retold in any line written. The why is in the
     facts-in-sync manual (the Concept Deliverer's
     docs/conventions/facts-in-sync/ §1, One home; The CBC Run's seat). -->

## The rules

1. **Give each fact one home.** The records table in the Entry File
   says which record owns which kind of fact.
2. **Elsewhere, link; retell only where the reader acts on it
   there.** A retelling carries its source's id, as SLICE-4 or
   KILL-12, or else its path, section and title in parentheses.
   "SLICE-4, a retried order makes one order" saves a lookup where
   the reader needs it. Elsewhere, link and don't retell: "The scale
   it is built for: see the System Definition." Without the id or
   the reference, a retelling is a second home.
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. An Invariant Slice Entry does this:
   it links the Invariant Slice Record it sums up.
4. **Change a fact at its home.** The links don't change, unless
   the home itself moves. In the same commit, grep the fact's id or
   path and re-read each line that carries it, with its paragraph.
5. **When two copies are unavoidable,** make one the owner and the
   other its follower, and let a check compare them. Example: the
   version lives in the build file; the CHANGELOG follows it.
6. **Cite a decision where its reader needs it.** A record cites it
   inside the sentence; an Agent Skill, Agent Rule, Approach on Trial
   or Output Shape this project writes cites it once, in its
   *Decisions* footer, never in a sentence, as `ADR-nnnn`. A delivered
   copy has none: its decisions are the Concept Deliverer's.

## Not a second home

History: the devlog, closed ADRs, commit bodies, the entries of
`.claude/decisions.md` and `CHANGELOG.md`'s released entries. They record what was true then. They are
never updated, so they cannot drift. **Living Text** is every text
but history. Each file's header comment is Living Text, the history
files' included. A fact stated only in history gets a home in
Living Text before anything retells it.

---

## Decisions

- ADR-0053 — the one-home Agent Rule loads in every session
- ADR-0065 — one home is facts-in-sync's
- ADR-0070 — a retelling may stand beside its id, re-read when
  its home changes
- ADR-0078 — rule 6: a decision is cited where its reader needs it
- ADR-0079 — *Not a second home*: a released CHANGELOG entry is
  history
