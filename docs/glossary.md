# Glossary

<!-- What each word of ours means, each defined once, in plain words
     (docs/conventions/writing/ §2, rule 6 and rule 9). Two kinds of
     entry. A word with one sense here: the word in bold, then what
     it means. It owns the bare word, so that word is not used in its
     plain sense here. A word with more than one meaning here: the word in
     bold, a line saying that bare it is plain English, then each
     sense of ours beneath it with the subject it carries at every
     use, written exactly as the entry writes it (rule 6). The entry
     is a contents page: one line per sense in use, ours and others'
     alike, each with the address of the home that defines it; the
     home defines, the entry points. A word of another part of
     speech is another word. A thing with a word of its own is not a
     sense. A new sense gets its
     line before its first use; a word of the first kind that needs
     a second sense, ours or the plain one, becomes an entry of the
     second kind, and its bare uses take their subject in the same
     change. Where a manual or a model owns the thing a word names,
     the entry points at it with a fact reference and does not
     restate it. A word is coined only when plain English cannot say
     it; an entry goes when its word does. Entries sit in groups by
     what they name; a new word goes in its group, after the words
     it uses.
     foundation: the writing convention -->

Used across both repos, each defined here once — or, where a
manual owns the thing a word names, pointed at there.

## The repositories

- **deliverer** — the repository holding the master of every file a
  project receives. Here, this repo.
- **run** — bare, plain English, read as any word is: the verb,
  "a script runs", is another word. Our sense carries its subject:
  - **cbc run** — a separate repository that builds a real system
    with what this repo gave it, blind to its deliverer
    (`docs/models/tiers.md` §2.3, *Runs*). Named by its number: cbc
    run 6.
- **newborn** — a run at its birth, from its seed until its agent
  finishes the birth. It holds what the seed put there, one pin
  included, and no earlier state.
- **project** — whichever repository is doing the work under a
  convention or making an output: a run, or this one.
- **seats** — the sides a convention has, this repo's and a run's
  (`docs/conventions/conventions/` §2.4, *The seats*).

## Between them

- **master** — the deliverer's copy of a file; a run holds copies
  of it (`docs/conventions/exchange/` §1, *What cannot change*, fact 3).
- **read-through**, **pin** — the two numbers a run records for a
  delivery: its own commit the deliverer last read up to, and the
  deliverer's commit its copies equal. The exchange's
  (`docs/conventions/exchange/` §2.2, *The run*).
- **delivery** — files copied whole into a run with a note, or a
  note alone. At birth, and after (`docs/conventions/exchange/`
  §3.2, *What goes*, §6.6, *Every read ends with a note*).
- **note** — the text beside a delivery: what changed since the
  run's pin, and a verdict on everything the run asked
  (`docs/conventions/exchange/` §3.7, *The note*).
- **staging** — copying the delivery and its note into a run's
  `temp/`, by the reviewer or by the agent when told to
  (`docs/conventions/exchange/` §3.1, *Staging*). The run does nothing until it
  has happened. The verb names its object, "stage a delivery", since
  git's verb is the same word.
- **take** — bare, plain English, read as any word is: the verb,
  "take the diff", is another word. Our sense carries its subject:
  - **a cbc run's take** — the cbc run's act: moving delivered files
    from `temp/` into place and recording the pin
    (`docs/conventions/exchange/` §4, *The take*).
- **harvest** — us reading a run's repository and changing our
  masters from what it learned (`docs/models/tiers.md` §3.3, *Up is harvest, through records*).

## Kinds of text

- **description** — how we understand a thing today, written down:
  the concept, a model, a manual. It may be wrong or
  incomplete and is canonical regardless; what derives from it
  applies it and does not explain. One rule for all of them
  (`docs/conventions/facts-in-sync/` §4, *The rule for every description*); they differ at the edges
  (ADR-0039).
- **model** — bare, plain English, read as any word is. Each sense
  in use carries its subject:
  - **idea model** — the top description of a chain of texts: an
    idea any repo can adapt, its rules varying by repo, like an
    interface. A repo adapts it in a manual
    (`docs/models/idea-to-output.md` §2, *The kinds*, and §5, *A
    model and a concept*). A particular one is named by its name: the
    agent model, the tiers model, the idea-to-output model.
  - others': the adversity model, the method's
    (`delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md`);
    the world model, the concept's (`concept/01-layered-system.md`);
    the data model and the role model, the stack's
    (`delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md`);
    the Claude model a delegation names, "Opus 5.5".
- **canonical** — of a description or a copy: the one that counts,
  from which every other is derived or copied. Says reference,
  never correctness — a canonical description is today's
  understanding and changes only for a reason recorded. In plain
  engineering words, a source of truth, where the truth is ours
  today; that phrase is a gloss on this word, not a second term. If
  it reads as settled where the stance is today, *standing* is the
  runner-up, recorded here rather than decided.
- **convention** — a way of working written down once, as two texts
  kept apart: its manual, and the artifacts a project acts on
  (`docs/models/idea-to-output.md` §6, *A convention*).
- **manual** — a convention's description, at
  `docs/conventions/<name>/README.md` (`docs/conventions/conventions/`
  §2, *The manual*).
- **made usable** — what a stated body becomes in the delivery:
  the concept as the method, the conventions as the container.
- **approach** — how a piece of work is done. A skill or a rule is
  an approach proven and placed; an approach on trial is not yet
  proven (`docs/models/idea-to-output.md` §2, *The kinds*).
- **approach on trial** — the written approach to one kind of work,
  not yet proven, at `.claude/approaches-on-trial/<work>.md`. It is
  drafted during its first use, used again, and in the end placed
  into conventions or dropped:
  `.claude/approaches-on-trial/approach-evaluation.md`.
- **form** — bare, plain English, read as any word is; nothing of
  ours. Our sense carries its subject, "output" for the kind and the
  owner for a particular one:
  - **output form** — how an output is written, read while it is
    written: rules for the writing and the output's layout, together.
    An approach (`docs/models/idea-to-output.md` §2, *The kinds*). A
    particular one is named by its owner: a record's form sits in the
    record itself, its header comment, `PLAN.md`'s step form, a
    record stub's headings. A manual's and a reading's are agent
    rules today; whether they become output shapes is TODO's "Decide
    whether our own forms become shapes".
- **shape** — bare, plain English, read as any word is; nothing of
  ours. Our sense carries its subject, "output" for the kind and the
  output's name for a particular one:
  - **output shape** — a presumed output, written from outputs that
    exist, and read only at the gate to check what was made
    (`docs/models/idea-to-output.md` §2, *The kinds*;
    `docs/conventions/shapes/`). A particular one is named by its
    output: the kill shape, the slice-record shape, the reading's
    shape. Not an output form, which is read while writing.
- **local map** — a directory's `README.md` that says how the parts
  of that area relate (`docs/conventions/project-recording/` §8.6, *Local maps*).
- **log** — bare, plain English, read as any word is: git log, the
  verb, a probe's log in the stack. Devlog and CHANGELOG are names of
  records, not this word. Our sense carries its subject:
  - **decisions log** — a cbc run's `.claude/decisions.md`, where its
    agent records the decisions about its own setup
    (`docs/conventions/agent-arrangement/` §3.4, *`decisions.md`*).
- **rule** — bare, plain English, read as any word is; nothing of
  ours. Each sense of ours carries its subject
  (`docs/conventions/writing/` §2, rule 9):
  - **agent rule** — a file under `.claude/rules/`, loaded into the
    agent by path or in every session
    (`docs/conventions/agent-arrangement/` §3.2, *`rules/`*).
  - a numbered line inside one carries its owner: "one-home rule 3",
    "writing rule 6".
  - the kinds in use: a local rule, the entry file's
    (`docs/conventions/agent-arrangement/` §2.4, *How*); a paths rule,
    an agent rule loaded by path (`docs/conventions/agent-arrangement/`
    §3.2, *`rules/`*); a permission rule and a deny rule, Claude
    Code's settings (`docs/conventions/agent-arrangement/` §3.5,
    *`settings.json`*).
- **template** — bare, plain English, read as any word is; nothing
  of ours. Our sense carries its subject:
  - **a skill's template** — a file under a skill's `templates/`,
    copied and filled by the project, never edited in place
    (`docs/conventions/exchange/` §5.8, *A skill's template is filled…*).
    A particular one is named by its file: the registry template,
    the glossary template.
- **stub** — bare, plain English, read as any word is; nothing of
  ours. Our sense carries its subject:
  - **record stub** — a record as it is born: the shipped file with
    its header comment and headings, which a project fills from its
    first entry on. The container holds one per record, each named
    by it: the plan stub, the decisions-log stub
    (`docs/conventions/project-recording/`, *What this is made usable as*).
- **overlay** — bare, plain English, read as any word is; nothing
  of ours. Our sense carries its subject:
  - **stack overlay** — the stack's part of the hygiene files,
    appended below the base's marked line: repo-hygiene's `.part`
    files for one stack (`docs/conventions/repo-hygiene/` §2, *Layering*).

## How texts tie

- **fact reference** — what a line carries when it relies on a fact
  written elsewhere: the address of the fact's home, its path,
  section and title, in parentheses
  (`docs/conventions/facts-in-sync/` §3.1, *What it is*).
- **tag** — bare, plain English, read as any word is: git's tag, a
  container image's tag. Each sense in use carries its subject:
  - **repo tag** — the letters a repo's decisions carry when cited
    from another repo, CBC for this one
    (`docs/conventions/project-recording/` §3.5, *A number is local to one repo*).
  - the framing's tags, KILL-3, FACT-CALLER-5: the method's, each
    tag kind defined in a cbc run's own glossary.
- **link** — a relation from a lower text to the upper one it
  relies on: stands on, points, governs, written from
  (`docs/models/idea-to-output.md` §3.1, *The four links*). Wider than a fact
  reference, which is what one kind of link, points, writes down.
- **foundation** — the line by which a file names the one thing the
  whole of it stands on: its description, or the practice it was
  written under. A skill, a rule, a shape, a record's form and a
  manual standing on a model carry one; a line that uses a part of a
  document carries a fact reference to that part instead
  (`docs/conventions/conventions/` §1.3, *The `foundation` line*;
  `docs/conventions/facts-in-sync/` §4, *The rule for every description*). Not *source*: that
  was a run's word for the deliverer, and is not ours.
- **walk** — what a change to a description sets off: the greps for
  its path and its name, and the re-read of each line they find
  (`docs/conventions/facts-in-sync/` §4, *The rule for every description*, step 3).

## The work

- **step** — bare, plain English, read as any word is: a numbered
  step inside a text is named by its owner, "the walk's step 3",
  "working-a-reading's step 4"; a casual phase stays bare. Our sense
  carries its subject:
  - **plan step** — one piece of PLAN's work, a cbc run's or ours. What
    makes work a plan step here is our `PLAN.md`'s step form
    (ADR-0057). Named by its number in its plan: Step 0.
- **stage** — bare, plain English, read as any word is: git's
  staged, and the verb, are other words. Each sense in use carries
  its subject:
  - **skill stage** — one phase of a skill, numbered from Stage 0,
    and named by its skill outside it: `cbc-slice`'s Stage 3,
    `cbc-framing`'s Stage 2. A plan step's Now line names the skill
    stage it is in. How a skill names them is the conventions
    manual's (`docs/conventions/conventions/` §1.4, *Stages*).
  - **approach stage** — one phase of an approach on trial, numbered
    the same way (`.claude/approaches-on-trial/approach-drafting.md`,
    *Stages*).
  - the exchange's staging has its own entry.
- **conversation-memory** — the talk that shaped a TODO item,
  kept beside it in `TODO-CONVERSATION-MEMORY.md`: what was asked,
  the options weighed, what was said for and against. It decides
  nothing; it is read when the item is worked
  (`docs/conventions/project-recording/` §14, *Conversation-memory…*).
