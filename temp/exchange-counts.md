# Exchange, counted

<!-- A kept file: exchange's texts in this repo, counted 2026-11-03,
     before the rebuild. Set against exchange rebuilt in cbc-concept,
     by the same method (ADR-0081, decision 7). -->

## 1. In this repo

Exchange is 6 texts, 1,341 lines. 42 of the repo's 101 files of
Living Text point at one of them. A change to the manual can touch 22
files outside exchange.

| Text | Lines | Pointers in | Files pointing in | Pointers out | Sideways out | ADRs cited |
|---|---|---|---|---|---|---|
| the manual, `docs/conventions/exchange/README.md` | 606 | 155 (34 from exchange) | 27 | 57 | 21 | 6 |
| the exchange-read Agent Skill | 114 | 18 (8) | 10 | 22 | 6 | 1 |
| the exchange-deliver Agent Skill | 214 | 18 (9) | 7 | 42 | 8 | 1 |
| the exchange-reading Agent Rule | 76 | 4 (3) | 4 | 10 | 1 | 1 |
| the working-a-reading Agent Rule | 137 | 16 (3) | 9 | 25 | 8 | 1 |
| the delivered-copies Agent Rule, shipped | 194 | 59 (5) | 27 | 22 | 8 | 3 |
| **All 6** | **1,341** | **270 (62)** | **42 outside exchange** | **178** | **52** | |

What the columns mean:

- **Pointers in:** mentions of the text in other Living Text, by path
  or by name. In brackets, those from exchange's own texts.
- **Files pointing in:** the files a change to the text can touch.
  Each one is re-read when the text changes.
- **Pointers out:** paths, Agent Skill and Agent Rule names, and
  convention names the text mentions.
- **Sideways out:** the pointers out to another idea's texts: another
  manual, an Idea Model, another Agent Skill or Agent Rule.

The pointers out, by kind:

| Text | Exchange | Other manual | Idea Model | Other Agent Skill or Agent Rule | Concept | Records and places |
|---|---|---|---|---|---|---|
| the manual | 8 | 13 | 4 | 4 | 1 | 27 |
| exchange-read | 11 | 0 | 0 | 6 | 0 | 5 |
| exchange-deliver | 15 | 0 | 0 | 8 | 2 | 17 |
| exchange-reading | 7 | 1 | 0 | 0 | 0 | 2 |
| working-a-reading | 14 | 2 | 0 | 6 | 0 | 3 |
| delivered-copies | 3 | 0 | 0 | 8 | 0 | 11 |

The manual's sections other texts point at, by section number:

| § | 1 | 2.2 | 2.4 | 2.5 | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.7 | 3.8 | 4 | 5 | 5.1 | 5.2 | 5.6 | 5.8 | 6 | 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 | none |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pointers | 6 | 7 | 4 | 1 | 3 | 10 | 6 | 8 | 2 | 4 | 4 | 5 | 2 | 1 | 1 | 1 | 6 | 5 | 5 | 1 | 6 | 1 | 4 | 2 | 15 |

## 2. How it is counted

The same method runs on exchange rebuilt, so the numbers compare.

1. **Exchange's texts:** the files whose Foundation Line names
   `the exchange convention`, the manual itself, and the
   working-a-reading Agent Rule, whose line reads "practice, under the
   exchange convention".
2. **Living Text:** every tracked `.md` file but the history: `devlog/`,
   `docs/adr/`, `temp/`, `CHANGELOG.md`, `TODO-CONVERSATION-MEMORY.md`
   and `.claude/decisions.md`.
3. **A pointer in** is a match, in Living Text, of the text's path or name:
   - the manual: `docs/conventions/exchange/`, or "exchange convention", any case;
   - each Agent Skill or Agent Rule: its file name, `exchange-read`
     never matching `exchange-reading`.
4. **A pointer out** is a match, in the text, of:
   - a path starting `.claude/`, `docs/`, `delivery/`, `concept/`,
     `temp/` or `devlog/`, or a top-level record such as `PLAN.md`;
   - a name followed by "Agent Skill", "Agent Rule" or "Approach on
     Trial";
   - "the <name> convention", for each convention under `docs/conventions/`.

   The manual's mentions of its own path do not count.
5. **A section pointed at** is `docs/conventions/exchange/` followed by
   § and a number, in Living Text.

What the method cannot tell:

- **A path is not always a pointer.** "Records and places" mixes links
  to a record with places named as the subject: `temp/` 11 times in the
  manual, as the CBC Run's folder.
- **A pointer is not always written as one.** A fact borrowed with no
  path or name is not counted.
- **Names change in the rebuild.** The method's patterns are updated
  to the new repo's paths and names, and the update says which.
