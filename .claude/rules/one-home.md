---
foundation: the project-recording convention
---

# One home per fact

**Governs:** where a fact is written in records, manuals, skills,
rules, comments and config. Where it lives, never how it reads.

<!-- No paths: line, so this loads at the start of every session.
     Ours, derived from docs/conventions/project-recording/ §11,
     rule 1, like the container's; ours also allows a tagged
     retelling, and its examples are this repo's. -->

## The rules

1. **Give each fact one home.** The records table in `CLAUDE.md`
   says which record owns which kind of fact. A convention's subject
   lives in its manual (`docs/conventions/conventions/` §3.1).
2. **Elsewhere, link; retell only where the reader acts on it
   there.** A retelling carries its source's path and section as a
   tag: "after birth, only the copies go: skills, rules, shapes,
   approaches on trial and the concept
   (`docs/conventions/exchange/` §3.2)". Without the tag it is a
   second home.
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. `ARCHITECTURE.md` §1.2 does this:
   a phrase for each convention, and the manual for the rest.
4. **Change a fact at its home.** The links don't change, unless
   the home itself moves (`docs/conventions/conventions/` §3.2).
   Each retelling tagged to it is re-read, with its paragraph
   (`docs/conventions/conventions/` §3.5).
5. **Make every copy a follower:** one is the owner, the other
   follows it and is checked against it. A tagged retelling is one;
   two copies that cannot be avoided are another: the worked example
   sits in `cbc-framing` and in `cbc-slice`, and the two must stay
   identical.

## Not a second home

History: the devlog, closed ADRs, commit bodies. They record what
was true then. They are never updated, so they cannot drift.

---

## Decisions

- ADR-0053 — one home per fact is project-recording's, and its rule
  loads in every session, here as in every run
- ADR-0059 — a retelling may stand where the reader acts on it,
  tagged to its source; ours now, a run's when its case is designed
