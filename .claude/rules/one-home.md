---
foundation: the project-recording convention
---

# One home per fact

**Governs:** where a fact is written in records, manuals, skills,
rules, comments and config. Where it lives, never how it reads.

<!-- No paths: line, so this loads at the start of every session.
     Ours, derived from docs/conventions/project-recording/ §11,
     rule 1, like the container's; its examples are this repo's. -->

## The rules

1. **Give each fact one home.** The records table in `CLAUDE.md`
   says which record owns which kind of fact. A convention's subject
   lives in its manual (`docs/conventions/conventions/` §3.1).
2. **Elsewhere, link; don't retell.** "The pin and the read-through:
   `delivered-copies.md`, rule 1." Not the rule again.
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. `ARCHITECTURE.md` §1.2 does this:
   a phrase for each convention, and the manual for the rest.
4. **Change a fact at its home.** The links don't change.
5. **When two copies are unavoidable,** make one the owner and the
   other its follower, and let a check compare them. Example: the
   worked example sits in `cbc-framing` and in `cbc-slice`, and the
   two must stay identical.

## Not a second home

History: the devlog, closed ADRs, commit bodies. They record what
was true then. They are never updated, so they cannot drift.

---

## Decisions

- ADR-0053 — one home per fact is project-recording's, and its rule
  loads in every session, here as in every run
