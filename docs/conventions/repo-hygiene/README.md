# Repo hygiene

**The three files every repo carries from its first commit:
`.gitignore`, `.gitattributes` and `.editorconfig`.**

## What it is for

So that a repo never commits what it should not, and never
accumulates line-ending noise, from its first commit — the worst
ignore is the one added after the junk is committed. Adopted with
the Container Group (ADR-0038); no failure of the Concept Deliverer's is
recorded before it. Lived since: every CBC Run was born with the base;
CBC Run 3 ignored `CLAUDE.local.md` in its own `.gitignore` before the
base did (its `aa9b3ec`), and the base carries the line now; CBC Run 3
appended its stack's ignores at its skeleton Plan Step (its `5336563`).

## What this is made usable as

- **`delivery/container/.gitignore`,
  `delivery/container/.gitattributes` and
  `delivery/container/.editorconfig` — the base, shipped**, copied
  into a repo at its creation and the CBC Run's own from then on; they
  never travel again.
- **`docs/conventions/repo-hygiene/templates/java-spring/` — a
  Stack Overlay, the Concept Deliverer's**, three `.part` files for Maven
  build output, wrapper line-ending exceptions and SQL/conf
  indents. Not shipped.
- **`.gitignore`, `.gitattributes` and `.editorconfig` at this
  repo's root — the Concept Deliverer's own**, the same base.

They carry no rules to read; they shape the repo by existing. What
derives from this page is that list. A change here walks it; a
change forced in one of them is checked back against this page.

## The seats

A CBC Run owns its three files from birth: it edits them when it needs
to, and adds its stack's lines at the Plan Step that makes the stack
true. The Concept Deliverer holds the base's Master Copy and the Stack Overlays, and
applies no Stack Overlay, having no stack. Its own `.gitignore` keeps the
base as shipped, and un-ignores `CLAUDE.local.md` in its "this
repo" section (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*).

## 1. The three files

| File | What it governs | Why it must exist from day zero |
|---|---|---|
| `.gitignore` | What never enters history: derived output, machine-local IDE state, OS junk, secrets | The worst ignores are the ones added *after* the junk is committed |
| `.gitattributes` | Line-ending truth (`* text=auto eol=lf`) and per-file exceptions | Normalization must be in force before the first cross-platform clone, or history accumulates CRLF noise |
| `.editorconfig` | Editor behavior the repo carries itself: charset, EOL, final newline, whitespace, indent | "Safe reservations" — rules fire only on files you touch (`[creating] [typing] [save] [format]` labels in the file); untouched files keep their bytes |

`.editorconfig` and `.gitattributes` are a pair: the editor *writes*
LF, git *guarantees* LF. Neither alone is sufficient.

## 2. Base and Stack Overlays

A repo exists before its app does, so the templates split:

- **The base** — stack-agnostic; correct for any repo including a
  records-only one.
- **A Stack Overlay** — snippets appended at the Plan Step that makes the
  stack true, below the marked line each base file carries.

Composition is plain concatenation; all three formats append
cleanly:

```bash
# at the skeleton step, with the overlay at hand:
t=<the overlay's directory>
cat "$t"/gitignore.part      >> .gitignore
cat "$t"/gitattributes.part  >> .gitattributes
cat "$t"/editorconfig.part   >> .editorconfig
```

How a Stack Overlay reaches a CBC Run is open: nothing ships one, and no
Plan Step, skill or playbook names the append.

*Its story: devlog 2026-09-28; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 3. The hygiene rules

- A CBC Run's files are its own. A fix that would be true of any
  project comes back the way every lesson does — the Concept Deliverer reads the CBC Run (`docs/conventions/exchange/` §6, *Up from the CBC Run*) and changes the
  Master Copy here, so the next birth starts corrected.
- A new stack is a new directory under `templates/` with the three
  `.part` files, and an ADR if any choice was non-obvious.
- `.idea/` is ignored wholesale; JetBrains state is machine-local.
  If a team later decides to share run configurations, that
  reversal is a new ADR, not a silent edit.
- Secrets: `.env` is ignored; the committed form is
  `.env.example`.

## Why it arrives this way

This convention never reaches an agent as text. Its product is three
files that shape the repo by existing (`docs/models/agent.md` §4.6, *Installed Channel*):
nobody complies with `.gitignore`, git simply hides what it names. A
rule here that cannot become a line in one of the three files has no
delivery at all.

*Its story: devlog 2026-09-28; ADR-0003; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## What this does not cover

- **How a file reaches a CBC Run, and what a CBC Run may do to it** —
  `docs/conventions/exchange/`.
- **The Plan Step that makes a stack true** — the stack's own skills,
  `delivery/spring-postgres/`.
- **The records a repo keeps** — `docs/conventions/project-recording/`.

## Where to look

- The base: the three dotfiles at the root of `delivery/container/`.
- The Stack Overlay: `docs/conventions/repo-hygiene/templates/java-spring/`.
