# Repo hygiene

**Three files every repo carries from its first commit,
`.gitignore`, `.gitattributes` and `.editorconfig`, maintained as
layered templates instead of being re-derived per project.**

## What it is for

So that a repo never commits what it should not, and never
accumulates line-ending noise, from its first commit — the worst
ignore is the one added after the junk is committed. Adopted with
the container (CBC ADR-0038); no failure of the deliverer's is
recorded before it. Lived since: every run was born with the base;
run 3 ignored `CLAUDE.local.md` in its own `.gitignore` before the
base did (its `aa9b3ec`), and the base carries the line now; run 3
appended its stack's ignores at its skeleton step (its `5336563`).

## What this is made usable as

- **The three dotfiles at the root of `delivery/container/` — the
  base, shipped**, copied into a repo at its creation and the run's
  own from then on; they never travel again.
- **`docs/conventions/repo-hygiene/templates/java-spring/` — a
  stack overlay, the deliverer's**, three `.part` files for Maven
  build output, wrapper line-ending exceptions and SQL/conf
  indents. Not shipped.
- **The deliverer's own three dotfiles**, the same base.

They carry no rules to read; they shape the repo by existing. What
derives from this page is that list. A change here walks it; a
change forced in one of them is checked back against this page.

## The seats

A run owns its three files from birth: it edits them when it needs
to, and adds its stack's lines at the step that makes the stack
true. The deliverer holds the base's master and the overlays, and
applies no overlay, having no stack.

## 1. The three files

| File | What it governs | Why it must exist from day zero |
|---|---|---|
| `.gitignore` | What never enters history: derived output, machine-local IDE state, OS junk, secrets | The worst ignores are the ones added *after* the junk is committed |
| `.gitattributes` | Line-ending truth (`* text=auto eol=lf`) and per-file exceptions | Normalization must be in force before the first cross-platform clone, or history accumulates CRLF noise |
| `.editorconfig` | Editor behavior the repo carries itself: charset, EOL, final newline, whitespace, indent | "Safe reservations" — rules fire only on files you touch (`[creating] [typing] [save] [format]` labels in the file); untouched files keep their bytes |

`.editorconfig` and `.gitattributes` are a pair: the editor *writes*
LF, git *guarantees* LF. Neither alone is sufficient.

## 2. Layering

A repo exists before its app does, so the templates split:

- **The base** — stack-agnostic; correct for any repo including a
  records-only one.
- **An overlay** — snippets appended at the step that makes the
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

*Found 2026-09-28: nothing ships an overlay, and a run is blind to
the deliverer and cannot fetch one. Run 3 wrote its stack's lines
itself at its skeleton step; the overlay here and the run's are two
sources for one thing, and no step, skill or playbook names the
append. How an overlay reaches a run is open.*

## 3. Rules

- Overlay content goes below the marker; base content above it is
  the base.
- A run's files are its own. A fix that would be true of any
  project comes back the way every lesson does — the deliverer
  reads the run, `docs/conventions/exchange/` §6 — and changes the
  master here, so the next birth starts corrected.
- A new stack is a new directory under `templates/` with the three
  `.part` files, and an ADR if any choice was non-obvious.
- `.idea/` is ignored wholesale; JetBrains state is machine-local.
  If a team later decides to share run configurations, that
  reversal is a new ADR, not a silent edit.
- Secrets: `.env` is ignored; the committed shape is
  `.env.example`.

## 4. Why it is delivered as files

This convention never reaches an agent as text. Its product is
three files that shape the repo by existing: nobody complies with
`.gitignore`, git simply hides what it names. A rule here that
cannot become a line in one of the three files has no delivery at
all.

*Until 2026-09-28 this page asked for a changelog entry with every
base or overlay change, and none was ever written: the CHANGELOG is
the concept's version log (CBC ADR-0003).*

## What this does not cover

- **How a file reaches a run, and what a run may do to it** —
  `docs/conventions/exchange/`.
- **The step that makes a stack true** — the stack's own skills,
  `delivery/spring-postgres/`.
- **The records a repo keeps** — `docs/conventions/project-recording/`.

## Where to look

- The base: the three dotfiles at the root of `delivery/container/`.
- The overlay: `docs/conventions/repo-hygiene/templates/java-spring/`.
