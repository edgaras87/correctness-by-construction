---
foundation: the facts-in-sync convention
---

# One home per fact

**Governs:** where a fact is written in records, manuals, skills,
rules, comments and config. Where it lives, never how it reads.

<!-- No paths: line, so this loads at the start of every session.
     Ours, derived from docs/conventions/facts-in-sync/ §1, §2, §3.1
     and its deliverer's seat, like the container's from §1 and its
     run's seat; how the two seats differ, that
     manual's *The seats* says. -->

## The rules

1. **Give each fact one home.** The records table in `CLAUDE.md`
   says which record owns which kind of fact. A convention's subject
   lives in its manual (`docs/conventions/facts-in-sync/` §2, *Point and derive*).
2. **Elsewhere, link; retell only where the reader acts on it
   there.** A retelling carries a fact reference to its source: its
   path, section and title, in parentheses. "After birth, only the
   copies go: skills, rules, shapes, approaches on trial and the
   concept (`docs/conventions/exchange/` §3.2, *What goes*)."
   Without the fact reference it is a second home
   (`docs/conventions/facts-in-sync/` §3.1, *What it is*).
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. `ARCHITECTURE.md` §1.2, *The conventions…* does this:
   a phrase for each convention, and the manual for the rest.
4. **Change a fact at its home.** The links don't change, unless
   the home itself moves, or its section is renamed, renumbered or
   retitled. Then every fact reference to it is grepped and fixed in
   the same commit (`docs/conventions/facts-in-sync/` §3.3, *A rename is grepped…*).
   Each retelling whose fact reference names it is re-read, with its
   paragraph (`docs/conventions/facts-in-sync/` §4, *The rule for every description*).
5. **Make every copy a follower:** one is the owner, the other
   follows it and is checked against it. A retelling with a fact reference is one;
   two copies that cannot be avoided are another: the worked example
   sits in `cbc-framing` and in `cbc-slice`, and the two must stay
   identical.
6. **Ask each new or changed line at the commit** whether it relies
   on a fact written elsewhere, and whether it says where. Nothing
   else finds a missing fact reference
   (`docs/conventions/facts-in-sync/`, *The deliverer's seat*).

## Not a second home

History: the devlog, closed ADRs, commit bodies, the entries of
`.claude/decisions.md` and the parts of
`TODO-CONVERSATION-MEMORY.md`. They record what was true then. They
are never updated, so they cannot drift. Each file's header comment
is living text. A fact stated only in history gets a living home
before anything retells it (`docs/conventions/facts-in-sync/` §1,
*One home*).

---

## Decisions

- ADR-0053 — the one-home rule loads in every session, here as in
  every run
- ADR-0059 — a retelling may stand where the reader acts on it,
  with a fact reference to its source; ours now, a run's when its
  case is designed
- ADR-0065 — one home is facts-in-sync's, with the fact reference
- ADR-0070 — how a fact reference is written; each new line asked
  at the commit
