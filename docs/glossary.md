# Glossary

<!-- What each coined word means, each defined once, in plain words
     (docs/conventions/writing/ §2, rule 6). One entry per word: the
     word in bold, then what it means. Where a manual or a model owns
     the thing a word names, the entry points at it with a fact
     reference and does not restate it. A word is coined only when
     plain English cannot say it; an entry goes when its word does.
     foundation: the writing convention -->

Used across both repos, each defined here once — or, where a
manual owns the thing a word names, pointed at there.

- **deliverer** — the repository holding the master of every file a
  project receives. Here, this repo.
- **run** — a separate repository that builds a real system with
  what it was given. Blind to its deliverer.
- **newborn** — a run at its birth, from its seed until its agent
  finishes the birth. It holds what the seed put there, one pin
  included, and no earlier state.
- **project** — whichever repository is doing the work under a
  convention or making an output: a run, or this one.
- **delivery** — files copied whole into a run with a note, or a
  note alone. At birth, and after (`docs/conventions/exchange/`
  §3.2, §6.6).
- **staging** — copying the delivery and its note into a run's
  `temp/`, by the reviewer or by the agent when told to
  (`docs/conventions/exchange/` §3.1). The run does nothing until it
  has happened.
- **take** — the run's act: moving delivered files from `temp/`
  into place and recording the pin (`docs/conventions/exchange/`
  §4).
- **read-through**, **pin** — the two numbers a run records for a
  delivery: its own commit the deliverer last read up to, and the
  deliverer's commit its copies equal. The exchange's,
  `docs/conventions/exchange/` §2.2.
- **note** — the text beside a delivery: what changed since the
  run's pin, and a verdict on everything the run asked
  (`docs/conventions/exchange/` §3.7).
- **harvest** — us reading a run's repository and changing our
  masters from what it learned. No files move.
- **master** — the one copy of a file that is edited. Every other
  copy changes only by being copied anew.
- **made usable** — what a stated body becomes in the delivery:
  the concept as the method, the conventions as the container.
- **description** — how we understand a thing today, written down:
  the concept, a model, a manual. It may be wrong or
  incomplete and is canonical regardless; what derives from it
  applies it and does not explain. One rule for all of them,
  `docs/conventions/facts-in-sync/` §4; they differ at the edges
  (ADR-0039).
- **model** — the top description of a chain of texts: an idea any
  repo can adapt, its rules varying by repo, like an interface. A
  repo adapts it in a manual (`docs/models/idea-to-output.md` §2
  and §5).
- **canonical** — of a description or a copy: the one that counts,
  from which every other is derived or copied. Says reference,
  never correctness — a canonical description is today's
  understanding and changes only for a reason recorded. In plain
  engineering words, a source of truth, where the truth is ours
  today; that phrase is a gloss on this word, not a second term. If
  it reads as settled where the stance is today, *standing* is the
  runner-up, recorded here rather than decided.
- **local map** — a directory's `README.md` that says how the parts
  of that area relate, which `ARCHITECTURE.md` points into. Relations only;
  not every README is one (ADR-0045).
- **convention** — a way of working written down once, as two texts
  kept apart: its manual, and the artifacts a project acts on
  (`docs/models/idea-to-output.md` §6).
- **manual** — a convention's description, at
  `docs/conventions/<name>/README.md`. Never shipped.
- **approach** — how a piece of work is done. A skill or a rule is
  an approach proven and placed; an approach on trial is not yet
  proven (`docs/models/idea-to-output.md` §2).
- **approach on trial** — the written approach to one kind of work,
  not yet proven, at `.claude/approaches-on-trial/<work>.md`. It is
  drafted during its first use, used again, and in the end placed
  into conventions or dropped:
  `.claude/approaches-on-trial/approach-evaluation.md`.
- **form** — how an output is written, read while it is written:
  rules for the writing and the output's layout, together. An
  approach (`docs/models/idea-to-output.md` §2). A record's form
  sits in the record itself: its header comment, `PLAN.md`'s step
  form, a stub's headings. A manual's and a reading's are agent
  rules today; whether they become shapes is TODO's "Decide whether
  our own forms become shapes".
- **shape** — a presumed output, written from outputs that exist,
  and read only at the gate to check what was made
  (`docs/models/idea-to-output.md` §2; `docs/conventions/shapes/`).
  Not a form, which is read while writing.
- **seats** — the sides a convention has, this repo's and a run's.
  A manual says whether the two use it the same way.
- **foundation** — the line by which a file names the one thing the
  whole of it stands on: its description, or the practice it was
  written under. A skill, a rule, a shape, a record's form and a
  manual standing on a model carry one; a line that uses a part of a
  document carries a fact reference to that part instead
  (`docs/conventions/conventions/` §1.3;
  `docs/conventions/facts-in-sync/` §4). Not *source*: that
  was a run's word for the deliverer, and is not ours.
- **link** — a relation from a lower text to the upper one it
  relies on: stands on, points, governs, written from, requires
  (`docs/models/idea-to-output.md` §3.1). Wider than a fact
  reference, which is what one kind of link, points, writes down.
- **fact reference** — what a line carries when it relies on a fact
  written elsewhere: the address of the fact's home, today a path
  and a section (`docs/conventions/facts-in-sync/` §3.1).
- **walk** — what a change to a description sets off: the greps for
  its path and its name, and the re-read of each line they find
  (`docs/conventions/facts-in-sync/` §4, step 3).
- **step** — one piece of PLAN's work, a run's or ours. What makes
  work a step here is our `PLAN.md`'s step form (ADR-0057).
- **conversation-memory** — the talk that shaped a TODO item,
  kept beside it in `TODO-CONVERSATION-MEMORY.md`: what was asked,
  the options weighed, what was said for and against. It decides
  nothing; it is read when the item is worked
  (`docs/conventions/project-recording/` §14).
- **stage** — one phase of a skill, numbered from Stage 0:
  `cbc-slice`'s Stage 3, `cbc-framing`'s Stage 2. A step's Now line
  names the stage it is in. How a skill names them:
  `docs/conventions/conventions/` §1.4.
