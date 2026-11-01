# Repo hygiene

**The three files every repo carries from its first commit:
`.gitignore`, `.gitattributes` and `.editorconfig`.**

## What it is for

So that a repo never commits what it should not, and never
accumulates line-ending noise, from its first commit. Adopted with
the Container Group (ADR-0038). No failure of the Concept Deliverer's is
recorded before it. Lived since:

- every CBC Run was born with the Hygiene Base;
- CBC Run 3 ignored `CLAUDE.local.md` in its own `.gitignore` before
  the Hygiene Base did (its `aa9b3ec`), and the Hygiene Base carries
  the line now;
- CBC Run 3 appended its stack's ignores at the Plan Step that makes
  the stack true, the Plan Step that first builds the application on its stack (its `5336563`).

## What this is made usable as

- **`delivery/container/.gitignore`,
  `delivery/container/.gitattributes` and
  `delivery/container/.editorconfig` — the Hygiene Base, shipped**, copied
  into a repo at its creation and the CBC Run's own from then on; they
  are never delivered again.
- **`docs/conventions/repo-hygiene/templates/java-spring/` — a
  Stack Overlay, the Concept Deliverer's**, three `.part` files for Maven
  build output, wrapper line-ending exceptions and SQL/conf
  indents. Not shipped.
- **`.gitignore`, `.gitattributes` and `.editorconfig` at this
  repo's root — the Concept Deliverer's own**, the same Hygiene Base.

They carry no rules to read. What
derives from this page is that list. A change here runs the Change Walk on it; a
change forced in one of them is checked back against this page.

## The seats

A CBC Run owns its three files from birth: it edits them when it needs
to, and adds its stack's lines at the Plan Step that makes the stack
true. The Concept Deliverer holds the Hygiene Base's Master Copy and the Stack Overlays, and
applies no Stack Overlay, having no stack. Its own `.gitignore` keeps the
Hygiene Base as shipped, and un-ignores `CLAUDE.local.md` in its "this
repo" section (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*).

## 1. The three files

| File | What it governs | Why it must exist from day zero |
|---|---|---|
| `.gitignore` | What never enters history: derived output, machine-local IDE state, OS junk, secrets | The worst ignores are the ones added *after* the junk is committed |
| `.gitattributes` | The line-ending rule (`* text=auto eol=lf`) and per-file exceptions | Normalization must be in force before the first cross-platform clone, or history accumulates CRLF noise |
| `.editorconfig` | Editor behavior the repo carries itself: charset, EOL, final newline, whitespace, indent | Rules fire only on files you touch, at the moments the file's labels name (`[creating] [typing] [save] [format]`). Untouched files keep their bytes |

`.editorconfig` and `.gitattributes` are a pair: the editor *writes*
LF, git *guarantees* LF. Neither alone is sufficient.

## 2. The template layers

A repo exists before its app does, so the templates split:

- **The Hygiene Base** — stack-agnostic; correct for any repo including a
  records-only one.
- **A Stack Overlay** — snippets appended at the Plan Step that makes the
  stack true, below the marked line each Hygiene Base file carries.

Composition is plain concatenation; all three formats append
cleanly:

```bash
# at the Plan Step that makes the stack true, with the Stack Overlay at hand:
t=<the Stack Overlay's directory>
cat "$t"/gitignore.part      >> .gitignore
cat "$t"/gitattributes.part  >> .gitattributes
cat "$t"/editorconfig.part   >> .editorconfig
```

How a Stack Overlay reaches a CBC Run is open: nothing ships one, and no
Plan Step, Agent Skill or playbook names the append.

*Its story: devlog 2026-09-28; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 3. The hygiene rules

- A CBC Run's files are its own. A fix that would be true of any
  project comes back the way every lesson does. The Concept Deliverer
  reads the CBC Run (`docs/conventions/exchange/` §6, *Up from the CBC
  Run*) and changes the Master Copy here. The next birth starts
  corrected.
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
- **The Plan Step that makes a stack true** — the stack's own Agent Skills,
  `delivery/spring-postgres/`.
- **The records a repo keeps** — `docs/conventions/project-recording/`.

## Where to look

- The Hygiene Base: the three dotfiles at the root of `delivery/container/`.
- The Stack Overlay: `docs/conventions/repo-hygiene/templates/java-spring/`.
