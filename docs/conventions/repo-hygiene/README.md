# Repo hygiene

Three files every repo carries from its first commit, `.gitignore`,
`.gitattributes` and `.editorconfig`, maintained as layered
templates instead of being re-derived per project.

**What ships:** the three base files, in the starter kit and linked
from [`templates/base/`](templates/base/) beside this page, the
links named without the leading dot because git will not follow a
symlinked `.gitignore`. They carry no rules to read; they shape the
repo by existing. The stack
overlays under [`templates/<stack>/`](templates/) stay here and are
appended from a handbook checkout at the step that makes the stack
true.

## The three files

| File | What it governs | Why it must exist from day zero |
|---|---|---|
| `.gitignore` | What never enters history: derived output, machine-local IDE state, OS junk, secrets | The worst ignores are the ones added *after* the junk is committed |
| `.gitattributes` | Line-ending truth (`* text=auto eol=lf`) and per-file exceptions | Normalization must be in force before the first cross-platform clone, or history accumulates CRLF noise |
| `.editorconfig` | Editor behavior the repo carries itself: charset, EOL, final newline, whitespace, indent | "Safe reservations" — rules fire only on files you touch (`[creating] [typing] [save] [format]` labels in the file); untouched files keep their bytes |

`.editorconfig` and `.gitattributes` are a pair: the editor *writes*
LF, git *guarantees* LF. Neither alone is sufficient.

## Layering

A repo following project-recording exists before its app does, so
the templates split:

- **The base** — stack-agnostic; correct for any repo including
  records-only and handbook repos. It is the kit's three dotfiles,
  copied at repo creation.
- **`templates/<stack>/`** — overlay snippets (`*.part` files)
  appended at the step that makes the stack true, the walking
  skeleton in a backend playbook, below the marked line in each
  base file. The overlays live in the handbook, not in the project.
  Currently: `java-spring` (Maven build output, wrapper line-ending
  exceptions, SQL/conf indents).

Composition is plain concatenation; all three formats append cleanly:

```bash
# at the skeleton step, from a handbook checkout:
t="$handbook_dir"/conventions/repo-hygiene/templates/java-spring
cat "$t"/gitignore.part      >> .gitignore
cat "$t"/gitattributes.part  >> .gitattributes
cat "$t"/editorconfig.part   >> .editorconfig
```

## Rules

- Base files ship with the starter kit; appending the stack overlay
  is a gate item of the step that introduces the stack ("hygiene
  overlay applied").
- Overlay content goes below the marker; base content is never
  edited per project. A needed base change is a change to the kit's
  file, with an ADR and a changelog entry in the handbook, and
  reaches it from a project as a friction item, never as a local
  patch: that is how fixes propagate to the next project instead of
  dying in one repo.
- New stack = new `templates/<stack>/` directory with the three
  `.part` files, a changelog entry, and an ADR if any choice was
  non-obvious.
- `.idea/` is ignored wholesale; JetBrains state is machine-local.
  If a team later decides to share run configurations, that
  reversal is a new ADR, not a silent edit.
- Secrets: `.env` is ignored; the committed shape is `.env.example`.

## Maintenance loop

These files follow the playbook pattern: when a project's field use
reveals a missing ignore or a wrong setting, the fix goes to the
handbook's file, base in the kit or overlay here, whichever truly
owns it, with a changelog entry, and every future project starts
corrected.

## Why it is delivered as files

This convention never reaches an agent as text. Its product is
three files that shape the repo by existing: nobody complies with
`.gitignore`, git simply hides what it names. A rule here that
cannot become a line in one of the three files has no delivery at
all (ADR-0008).

## Where to look

- The base: [`templates/base/`](templates/base/), links into
  `starter/kit/`.
- The overlays: [`templates/java-spring/`](templates/java-spring/).
- The step that appends an overlay: the backend playbook in
  [`../../starter/playbooks/`](../../starter/playbooks/).
