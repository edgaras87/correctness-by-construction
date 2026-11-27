<!-- This repo's own Adapted Case for the check at the commit: its Instruction Text, an Agent Rule. No paths: line, so it loads in every session. Why it is as it is: .claude/understanding/foundation-check.md. -->

# The Foundation Check

**Governs:** the moment before a commit is staged, when the commit
changes a file that stands on a foundation, or a foundation itself,
or moves a section. Which side is right, never how either reads.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Canonical Description | `docs/models/idea-to-output.md` §2, *The kinds* |
| Change Walk | `knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Fact Reference | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Foundation Check | `.claude/understanding/foundation-check.md` §1, *Its Defined Terms* |
| Foundation Line | `docs/conventions/conventions/` §1.3, *The Foundation Line* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Living Text | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Record Stub | `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §1, *Its Defined Terms* |

## The check

1. **Look at the staged paths first.** Only these are checked
   (`docs/conventions/conventions/` §1.3, *The Foundation Line*, for
   the first two):
   - files with a Foundation Line: `.claude/skills/`,
     `.claude/rules/`, `.claude/` under `delivery/`, and a manual
     that names the model under `docs/models/` it stands on;
   - records whose header comment carries a Foundation Line, ours
     and the Backend Kit's Record Stubs alike,
     and the shipped files whose header comment carries one: the
     delivered glossaries under `delivery/*/docs/glossary/` and
     the playbook's form for a Plan Step;
   - Canonical Descriptions: `docs/models/`, `docs/conventions/*/README.md`,
     `concept/` (`knowledge/backbone-ideas/one-home.md` §7, *What stands on a text*).

   If none is staged, the check is done.
2. **A file with a Foundation Line changed:** open what the line
   names beside the change. For a convention, its manual,
   `docs/conventions/<name>/README.md`. For a model,
   `docs/models/<name>.md`. For `concept v1`, the chapters under
   `concept/`. Read the parts the change touches. A file names one
   `foundation`; a second is a Fact Reference to a part
   (`knowledge/backbone-ideas/one-home.md` §7, *What stands on a text*).
3. **A Canonical Description changed:** run the Change Walk on what derives from it
   (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §4, *The Change Walk*).
4. **List every disagreement before deciding any.** For each, show
   the reviewer what the foundation says, what the change says, and
   which side the agent thinks is wrong, and why. The reviewer
   decides each (`knowledge/backbone-ideas/one-home.md` §8, *A disagreement*).
5. **The commit body names each ending,** one of four:
   - **the change is wrong:** it is brought back to the foundation;
   - **the foundation is wrong:** it changes;
   - **both change;**
   - **they agree:** one line names the foundation read.

   A change on the other side goes in the same commit, or in the
   next when one side is an agent file and the other is not
   (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*).
6. **A foundation that changes is a Canonical Description changed.** Step 3
   runs on it again, and what it finds goes through steps 4 and 5.
   The check ends when a Change Walk finds nothing new. When the changes
   need more than one commit, they are a commit plan.

## A moved section

When the commit renames a file, renumbers or retitles a section, in
any file, or moves a fact to a new home, grep all Living Text for
each old path, number and title, and fix what points at them in
this commit (`knowledge/backbone-ideas/one-home.md` §5, *When a home moves*).
When the commit replaces a word across files, re-read each changed
sentence for what it now claims.

## What this does not cover

- **What a Canonical Description and what stands on it are** —
  `knowledge/backbone-ideas/one-home.md` §7, *What stands on a text*.
- **How a Backend Repo's Copy Change is taken** —
  `.claude/rules/working-a-reading.md`, step 4.
- **How a Backend Repo changes a Kit Copy it holds** —
  `delivery/container/.claude/rules/delivered-copies.md`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-17 — the check at the commit,
  loaded in every session; why not a Paths Rule, a `CLAUDE.md`
  line, or a hook now
- ADR-0065 — the check came from the facts-in-sync convention, since rewritten into the layers
