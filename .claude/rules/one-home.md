<!-- This repo's own Adapted Case for one home: its Instruction Text, an Agent Rule. No paths: line, so it loads in every session. Why it is as it is: .claude/understanding/one-home.md. -->

# One home per fact

**Governs:** where a fact is written in records, manuals, Agent Skills,
Agent Rules, comments and config. Where it lives, never how it reads.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Agent Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Fact Reference | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Living Text | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Output Shape | `docs/conventions/shapes/` §1, *What an Output Shape is* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## The rules

1. **Give each fact one home.** The records table in `CLAUDE.md`
   says which record owns which kind of fact. A text that touches an
   idea points at its home, and does not restate it
   (`knowledge/backbone-ideas/one-home.md` §4, *Pointing at a home*).
2. **Elsewhere, link; retell only where the reader acts on it
   there.** A retelling carries a Fact Reference to its source: its
   path, section and title, in parentheses. "A Problem Domain Idea names
   the Backbone Idea it is adapted from
   (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The Problem Domain layer*)."
   Without the Fact Reference it is a second home
   (`knowledge/backbone-ideas/one-home.md` §3, *A fact and its home*;
   the form: `knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §2, *Writing a Fact Reference*).
3. **Make a summary say it is one.** It names its owner, and nobody
   reads it in the owner's place. `ARCHITECTURE.md` does this (`ARCHITECTURE.md` §1.2, *The conventions*):
   a phrase for each convention, and the manual for the rest.
4. **Change a fact at its home.** The links don't change, unless
   the home itself moves, or its section is renamed, renumbered or
   retitled. Then every Fact Reference to it is grepped and fixed in
   the same commit (`knowledge/backbone-ideas/one-home.md` §5, *When a home moves*).
   Each retelling whose Fact Reference names it is re-read, with its
   paragraph (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §4, *The Change Walk*).
5. **Make every copy a follower:** one is the owner, the other
   follows it and is checked against it. A retelling with a Fact
   Reference is one. Two copies that cannot be avoided are another:
   the worked example sits in the cbc-framing and cbc-slice Agent Skills, and
   the two must stay identical (`docs/conventions/exchange/` §6.3, *The CBC Run Reading*).
6. **Ask each new or changed line at the commit** whether it relies
   on a fact written elsewhere, and whether it says where. Nothing
   else finds a missing Fact Reference
   (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §4, *The Change Walk*).
7. **Cite a decision where its reader needs it.** A manual or a
   record cites it inside the sentence; an Instruction Text or an
   Output Shape cites it once, in its *Decisions* footer, never in a
   sentence. Cite our own as `ADR-nnnn`; the footer is stripped from
   every copy we deliver (`knowledge/backbone-ideas/one-home.md` §6, *Where a decision is cited*).

## Not a second home

History: the devlog, closed ADRs, commit bodies, the entries of
`.claude/decisions.md`, `CHANGELOG.md`'s released entries and the parts of
`TODO-CONVERSATION-MEMORY.md`. They record what was true then. They
are never updated, so they cannot drift. Each file's header comment
is Living Text. A fact stated only in history gets a home in Living Text
before anything retells it (`knowledge/backbone-ideas/one-home.md` §3,
*A fact and its home*).

---

## Decisions

- ADR-0053 — the one-home Agent Rule loads in every session, here as in
  every CBC Run
- ADR-0059 — a retelling may stand where the reader acts on it,
  with a Fact Reference to its source; ours now, a CBC Run's when its
  case is designed
- ADR-0065 — one home and the Fact Reference gathered in one convention, since rewritten into the layers
- ADR-0070 — how a Fact Reference is written; each new line asked
  at the commit
- ADR-0078 — rule 7: a decision is cited where its reader needs it
- ADR-0079 — *Not a second home*: a released CHANGELOG entry is
  history
