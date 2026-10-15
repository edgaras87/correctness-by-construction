---
foundation: the project-recording convention
---

# One home per fact

**Governs:** where a fact is written in records, comments and
config. Where it lives, never how it reads.

<!-- No paths: line, so this loads at the start of every session:
     a fact can be retold in any line written. The why is the
     deliverer's project-recording manual, §11, rule 1. -->

## The rules

1. **Give each fact one home.** The records table in the entry file
   says which record owns which kind of fact.
2. **Elsewhere, link; don't retell.** "The scale it is built for:
   see the system definition." Not the scale again.
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. A registry entry does this: it
   links the slice record it sums up.
4. **Change a fact at its home.** The links don't change.
5. **When two copies are unavoidable,** make one the owner and the
   other its follower, and let a check compare them. Example: the
   version lives in the build file; the CHANGELOG follows it.

## Not a second home

History: the devlog, closed ADRs, commit bodies. They record what
was true then. They are never updated, so they cannot drift.

---

## Decisions

- CBC ADR-0053 — one home per fact is project-recording's, and its
  rule loads in every session
