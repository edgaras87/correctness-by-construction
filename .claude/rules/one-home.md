---
foundation: the facts-in-sync convention
---

# One home per fact

**Governs:** where a fact is written in records, manuals, Agent Skills,
Agent Rules, comments and config. Where it lives, never how it reads.

<!-- No paths: line, so this loads at the start of every session.
     Ours is derived from docs/conventions/facts-in-sync/ (§1, One home;
     §2, Point and derive; §3.1, What a Fact Reference is; §3.4, A decision
     citation; The Concept Deliverer's seat). The container's is derived from §1 and its CBC
     Run's seat (§1, One home; The CBC Run's seat). That manual's
     *The seats* says how the two Convention Seats differ. -->

## The rules

1. **Give each fact one home.** The records table in `CLAUDE.md`
   says which record owns which kind of fact. A convention's subject
   lives in its manual (`docs/conventions/facts-in-sync/` §2, *Point and derive*).
2. **Elsewhere, link; retell only where the reader acts on it
   there.** A retelling carries a Fact Reference to its source: its
   path, section and title, in parentheses. "After CBC Run Birth, only the
   copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial,
   the Glossary Names and the concept (`docs/conventions/exchange/` §3.2, *What goes*)."
   Without the Fact Reference it is a second home
   (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. `ARCHITECTURE.md` does this (`ARCHITECTURE.md` §1.2, *The conventions*):
   a phrase for each convention, and the manual for the rest.
4. **Change a fact at its home.** The links don't change, unless
   the home itself moves, or its section is renamed, renumbered or
   retitled. Then every Fact Reference to it is grepped and fixed in
   the same commit (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*).
   Each retelling whose Fact Reference names it is re-read, with its
   paragraph (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
5. **Make every copy a follower:** one is the owner, the other
   follows it and is checked against it. A retelling with a Fact
   Reference is one. Two copies that cannot be avoided are another:
   the worked example sits in the cbc-framing and cbc-slice Agent Skills, and
   the two must stay identical.
6. **Ask each new or changed line at the commit** whether it relies
   on a fact written elsewhere, and whether it says where. Nothing
   else finds a missing Fact Reference
   (`docs/conventions/facts-in-sync/`, *The Concept Deliverer's seat*).
7. **Cite a decision where its reader needs it.** A manual or a
   record cites it inside the sentence; an Agent Skill, an Agent Rule,
   an Approach on Trial or an Output Shape cites it once, in its
   *Decisions* footer, never in a sentence. Cite our own as
   `ADR-nnnn`; the footer is stripped from every copy we deliver
   (`docs/conventions/facts-in-sync/` §3.4, *A decision citation*).

## Not a second home

History: the devlog, closed ADRs, commit bodies, the entries of
`.claude/decisions.md`, `CHANGELOG.md`'s released entries and the parts of
`TODO-CONVERSATION-MEMORY.md`. They record what was true then. They
are never updated, so they cannot drift. Each file's header comment
is Living Text. A fact stated only in history gets a home in Living Text
before anything retells it (`docs/conventions/facts-in-sync/` §1.6,
*History is not a first home*).

---

## Decisions

- ADR-0053 — the one-home Agent Rule loads in every session, here as in
  every CBC Run
- ADR-0059 — a retelling may stand where the reader acts on it,
  with a Fact Reference to its source; ours now, a CBC Run's when its
  case is designed
- ADR-0065 — one home is the facts-in-sync manual's, with the Fact Reference
- ADR-0070 — how a Fact Reference is written; each new line asked
  at the commit
- ADR-0078 — rule 7: a decision is cited where its reader needs it
- ADR-0079 — *Not a second home*: a released CHANGELOG entry is
  history
