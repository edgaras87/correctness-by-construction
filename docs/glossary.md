# Glossary

<!-- The list of Glossary Names: every thing this repo defines, named
     in two or more words, owner or kind first, each word capitalized,
     written exactly (docs/conventions/writing/ §2, Why each rule,
     rule 9). A lowercase word is English. One entry per Name: the
     Name in bold, then what it means in plain words, and, where a
     manual or a model owns the thing, a Fact Reference to it; the
     home defines, the entry points. A Name is added in the commit
     that first uses it; an entry goes when its thing does. A word
     whose English meaning is ours has no Name and no entry. A
     convention is named by its path in backticks, with its kind
     word, the exchange manual, or by its Name, the Exchange
     Convention; never by the bare word. Entries sit in
     groups by what they name; a new Name goes in its group, after
     the Names it uses. The concept's, the method's and the stack's
     Names are written once, in the file each group delivers, and
     read there; their groups here point at it. A Name that file
     delivery/container/docs/glossary/container.md also lists is
     shared: its entry there follows this one, from the CBC Run's
     side.
     foundation: the writing convention -->

The Names used in this repo, each pointing at the home that defines
its thing. A CBC Run keeps a glossary of its own, and receives the
delivered files below.

## The repositories

- **Concept Repo** — the Tiers Model's word for any concept's
  repository (`docs/models/tiers.md` §2.2, *Concept Repos*).
- **Run Repo** — the Tiers Model's word for any repository born from
  a Concept Repo to try it (`docs/models/tiers.md` §2.3, *Run Repos*).
- **Concept Garden** — the folder that holds the Concept Repos
  (`docs/models/tiers.md` §2.2, *Concept Repos*).
- **Concept Deliverer** — this repo: the Concept Repo of correctness
  by construction, holding the Master Copy of every file a CBC Run
  receives (`docs/models/tiers.md` §2.2, *Concept Repos*).
- **CBC Run** — a Run Repo of this concept: a separate repository
  that builds a real system with what this repo gave it, blind to
  its Concept Deliverer (`docs/models/tiers.md` §2.3, *Run Repos*). Named by
  its number: CBC Run 6.
- **Newborn CBC Run** — a CBC Run at its birth, from its Pure Seed
  until its agent finishes the CBC Run Birth. It holds what the Pure
  Seed put there, one Delivery Pin included, and no earlier state.
- **Convention Seat** — a side a convention has, this repo's or a
  CBC Run's (`docs/conventions/conventions/` §2.4, *The seats*).

## Between them

- **Master Copy** — the Concept Deliverer's copy of a file; a CBC Run
  holds copies of it (`docs/conventions/exchange/` §1, *What cannot change*, fact 3).
- **Read-Through Commit** — the CBC Run's own commit the Concept
  Deliverer last read up to, one of the two numbers a CBC Run
  records for a delivery (`docs/conventions/exchange/` §2.2, *The CBC Run*).
- **Delivery Pin** — the Concept Deliverer's commit a CBC Run's
  copies equal, but for their *Decisions* footers; the other number
  (`docs/conventions/exchange/` §2.2, *The CBC Run*).
- **Delivery Note** — the text beside a delivery: what changed since
  the CBC Run's Delivery Pin, and a verdict on everything the CBC Run
  asked (`docs/conventions/exchange/` §3.7, *The Delivery Note*).
- **Delivery Staging** — a delivery as it arrives in a CBC Run's
  `temp/`: the files and their Delivery Note, in a directory named for
  our commit (`docs/conventions/exchange/` §3.1, *Delivery Staging*).
  The act is "stage a delivery", by the reviewer or by the agent when
  told to; the verb names its object, since git's verb is the same
  word. The CBC Run does nothing until it has happened.
- **Delivery Take** — the CBC Run's act: moving delivered files from
  `temp/` into place and recording the Delivery Pin
  (`docs/conventions/exchange/` §4, *The Delivery Take*).
- **Receipt Branch** — a branch holding a delivery as it arrived,
  named by its Delivery Pin and never merged: the Pure Seed's
  `birth-seed`, or one a CBC Run cuts at its Delivery Take, so the
  next diff of its edits is exact (`docs/conventions/exchange/` §4,
  *The Delivery Take*, step 3; `delivery/installs/pure-seed.md`).
- **Delivery Fill** — text one group writes at Delivery Staging into
  a marked place in another group's file, the playbook's Plan Steps
  into `PLAN.md`; the only delivery that is not a copy
  (`docs/conventions/exchange/` §3.4, *One group per file*).
- **CBC Run Ask** — a line in a CBC Run's backlog, under *To the
  deliverer*, asking us for a verdict: on an edit to a copy, a file
  it offers, or a question. Every CBC Run Reading lists each
  (`docs/conventions/exchange/` §5.1, *When a copy may be edited*).
- **CBC Run Reading** — the Concept Deliverer reading a CBC Run
  since it last read it, and the text that records what it found
  (`docs/conventions/exchange/` §6.3, *The CBC Run Reading*).
- **Record Harvest** — us reading a CBC Run's records and changing
  our Master Copies from what it learned
  (`docs/models/tiers.md` §3.3, *Upward harvest*).
- **CBC Run Birth** — a CBC Run's first state, made from this repo at one
  Delivery Pin (`docs/models/tiers.md` §3.1, *Downward delivery*).
- **Pure Seed** — the procedure that gives a CBC Run its birth from
  this repo alone: `delivery/installs/pure-seed.md`.
- **CBC Run Briefing** — the text put in a Newborn CBC Run's `temp/`
  before it starts that says what it is to build
  (`.claude/approaches-on-trial/auto-run.md`, *Stages*).
- **CBC Run Hand-off** — the text beside it that says how it is to
  work (`.claude/approaches-on-trial/auto-run.md`, *Stages*).
- **Container Group** — the group of files every CBC Run receives,
  its records and working arrangement: `delivery/container/`
  (`docs/conventions/exchange/` §3.3, *A group's place in the tree*).
- **Method Group** — the group that carries the method, its Agent
  Skills and Output Shapes: `delivery/method/`
  (`docs/conventions/exchange/` §3.3, *A group's place in the tree*).
- **Stack Group** — the group for one stack, swapped with the stack:
  `delivery/spring-postgres/`
  (`docs/conventions/exchange/` §3.3, *A group's place in the tree*).

## Kinds of text

- **Canonical Description** — how we understand a thing today,
  written down: the concept, an Idea Model, a Convention Manual. It
  may be wrong or incomplete. It is the one that counts regardless.
  What derives from it applies it and does not explain. One rule for
  all of them (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*);
  they differ at the edges (ADR-0039). Canonical says reference,
  never correctness: today's understanding, changed only for a
  reason recorded.
- **Idea Model** — the top Canonical Description of a chain of
  texts: an idea any repo can adapt, its rules varying by repo, like
  an interface. A repo adapts it in a Convention Manual
  (`docs/models/idea-to-output.md` §2, *The kinds*, and §5, *An Idea
  Model and a concept*). A particular one is named by its name: the
  Agent Model, the Tiers Model, the Idea-to-Output Model.
- **Convention Manual** — a convention's Canonical Description, at
  `docs/conventions/<name>/README.md` (`docs/conventions/conventions/`
  §2, *The Convention Manual*).
- **Exchange Convention** — the convention at
  `docs/conventions/exchange/`: everything that passes between the
  Concept Deliverer and a CBC Run. The one convention with a Name of
  its own; the others are named by path or with their kind word.
- **Made Usable** — what a body of text becomes in the delivery: the
  concept becomes the method, the conventions become the Container
  Group.
- **Work Approach** — how a piece of work is done. An Agent Skill or an
  Agent Rule is a Work Approach proven and placed; an Approach on
  Trial is not yet proven (`docs/models/idea-to-output.md` §2, *The kinds*).
- **Approach on Trial** — the written Work Approach to one kind of
  work, not yet proven, at `.claude/approaches-on-trial/<work>.md`.
  It is drafted during its first use, used again, and in the end
  placed into conventions or dropped:
  `.claude/approaches-on-trial/approach-evaluation.md`.
- **Output Form** — how an output is written, read while it is
  written: rules for the writing and the output's layout, together.
  A Work Approach (`docs/models/idea-to-output.md` §2, *The kinds*).
  A particular one is named by its owner: a record's form sits in
  the record itself, its header comment, the Plan Step Form, a Record
  Stub's headings. A Convention Manual's and a CBC Run Reading's are
  Agent Rules today; whether they become Output Shapes is TODO's
  "Decide whether our own forms become Output Shapes".
- **Output Shape** — a presumed output, written from outputs that
  exist, and read only at the gate to check what was made
  (`docs/models/idea-to-output.md` §2, *The kinds*;
  `docs/conventions/shapes/`). A particular one is named by its
  output: the Enemy Collision Kill Shape, the Invariant Slice Record Shape. Not an Output
  Form, which is read while writing.
- **Entry File** — the file the tool loads at session start, before
  the first task: `CLAUDE.md` here, and in every CBC Run
  (`docs/models/agent.md` §4.1, *Ambient Channel*).
- **Local Map** — a directory's `README.md` that says how the parts
  of that area relate (`docs/conventions/project-recording/` §8.6, *Local Maps*).
- **Agent Rule** — a file under `.claude/rules/`, loaded into the
  agent by path or in every session
  (`docs/conventions/agent-arrangement/` §3.2, *`.claude/rules/`*). A
  numbered line inside one is named by its owner and number:
  "one-home rule 3", "writing rule 6". The kinds in use: a Local
  Rule, the entry file's (`docs/conventions/agent-arrangement/`
  §2.4, *How the Entry File is written*); a Paths Rule, one loaded by path; and Claude Code's
  permission and deny rules, its own words
  (`docs/conventions/agent-arrangement/` §3.5, *`.claude/settings.json`*).
- **Agent Skill** — a file under `.claude/skills/<name>/`, its
  `SKILL.md` and what it references, read when its moment comes
  (`docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`*). Always written with its
  kind, the commit-plan Agent Skill
  (`docs/conventions/conventions/` §1.5, *Naming a Work Approach*).
- **Agent Skill Template** — a file under an Agent Skill's `templates/`, copied
  and filled by the project, never edited in place
  (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*).
  A particular one is named by its file: `templates/registry.md`.
- **Record Stub** — a record as it is born: the shipped file with its
  header comment and headings, which a project fills from its first
  entry on. The Container Group holds one per record, each named by
  it: the Plan Stub, the Decisions Log Stub
  (`docs/conventions/project-recording/`, *What this is made usable as*).
- **Hygiene Base** — the stack-agnostic hygiene files every repo
  gets, correct for a records-only one; a Stack Overlay is appended
  below each one's marked line (`docs/conventions/repo-hygiene/`
  §2, *The template layers*).
- **Stack Overlay** — the stack's part of the hygiene files, appended
  below the Hygiene Base's marked line: the `.part` files under
  `docs/conventions/repo-hygiene/templates/`, one directory per stack (`docs/conventions/repo-hygiene/` §2, *The template layers*).
- **Decisions Log** — a CBC Run's `.claude/decisions.md`, where its
  agent records the decisions about its own setup; ours is the same
  file here (`docs/conventions/agent-arrangement/` §3.4, *`.claude/decisions.md`*).
- **Repo Tag** — the letters a repo's decisions carry when cited from
  another repo, CBC for this one
  (`docs/conventions/project-recording/` §3.5, *Numbers across repos*).

## How texts tie

- **Glossary Name** — the name of a thing this repo defines: two or
  more words, owner or kind first, each capitalized, written
  exactly; what this file lists
  (`docs/conventions/writing/` §2, *Why each rule*, rule 9).
- **Living Text** — text kept true as things change: every text
  here but history, which records what was true then
  and is never updated (`docs/conventions/facts-in-sync/` §1, *One
  home*).
- **Fact Reference** — what a line carries when it relies on a fact
  written elsewhere: the address of the fact's home, its path,
  section and title, in parentheses
  (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **Chain Link** — a relation from a lower text to the upper one it
  relies on: stands on, points, governs, written from
  (`docs/models/idea-to-output.md` §3.1, *The four Chain Links*). Wider
  than a Fact Reference, which is what one kind of link, points,
  writes down.
- **Foundation Line** — the line by which a file names the one thing
  the whole of it stands on: its Canonical Description, or the
  practice it was written under. A skill, an Agent Rule, an Output
  Shape, a record's form and a Convention Manual standing on an Idea
  Model carry one; a line that uses a part of a document carries a
  Fact Reference to that part instead
  (`docs/conventions/conventions/` §1.3, *The Foundation Line*;
  `docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
  Not *source*: that was a CBC Run's word for the Concept Deliverer, and is not
  ours.
- **Change Walk** — what a change to a Canonical Description sets
  off: the greps for its path and its name, and the re-read of each
  line they find
  (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 3).
- **Foundation Check** — the check before a commit is staged that
  runs the Change Walk and settles each disagreement it finds, our
  Agent Rule `.claude/rules/foundation-check.md`
  (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).

## The work

- **Plan Step** — one piece of `PLAN.md`'s work, a CBC Run's or ours.
  What makes work a Plan Step here is the Plan Step Form in our
  `PLAN.md` (ADR-0057). Named by its number in its plan: Step 0.
- **Agent Skill Stage** — one phase of an Agent Skill, numbered from Stage 0 and
  named by its Agent Skill outside it: `cbc-slice`'s Stage 3,
  `cbc-framing`'s Stage 2. A Plan Step's Now line names the Agent Skill
  Stage it is in. How an Agent Skill names them is the conventions manual's
  (`docs/conventions/conventions/` §1.4, *Agent Skill Stages*).
- **Approach on Trial Stage** — one phase of an Approach on Trial, numbered
  the same way (`.claude/approaches-on-trial/approach-drafting.md`,
  *Stages*).
- **Refinement Layer** — a set of files the refinement fixes together
  (`.claude/approaches-on-trial/refinement.md` §1, *What it reads, and its words*).
- **Refinement Round** — the Finding Kinds whose fixes do the same to
  the text, read together
  (`.claude/approaches-on-trial/refinement.md` §1, *What it reads, and its words*).
- **Finding Kind** — one rule the refinement reads against, and the
  findings it makes
  (`.claude/approaches-on-trial/refinement.md` §1, *What it reads, and its words*).
- **Change Set** — a body of work that needs more than one commit,
  sequenced and closed as a commit plan
  (`docs/conventions/commit-plan/` §1, *What a commit plan is*).
- **Plan Step Gate** — a Plan Step's exit criteria: facts that can be
  checked, written when the Plan Step opens; it is done only when
  every one is true (the Plan Step Form in our `PLAN.md`).
- **Conversation Memory** — the talk that shaped a TODO item, kept
  beside it in `TODO-CONVERSATION-MEMORY.md`: what was asked, the
  options weighed, what was said for and against. It decides
  nothing; it is read when the item is worked
  (`docs/conventions/project-recording/` §14, *Conversation Memory*).

## The Agent Model

- **Ambient Channel** — text that reaches the agent at session start,
  before the first task: the Entry File and what it loads
  (`docs/models/agent.md` §4.1, *Ambient Channel*).
- **Pulled Channel** — a file the agent reads because it decided to
  (`docs/models/agent.md` §4.2, *Pulled Channel*).
- **Pushed Channel** — text put in the agent's context at a moment it
  did not choose: a task type matches, an event occurs
  (`docs/models/agent.md` §4.3, *Pushed Channel*).
- **Told Channel** — what a human says in the session
  (`docs/models/agent.md` §4.4, *Told Channel*); between tiers, what a tier
  above hands a Run Repo as session input (`docs/models/tiers.md`
  §3.2, *The Told Channel*).
- **Observed Channel** — the results of commands the agent runs: file
  contents, search hits, test output
  (`docs/models/agent.md` §4.5, *Observed Channel*).
- **Installed Channel** — files that work by existing, such as
  `.gitignore`, and deliver nothing to the context window
  (`docs/models/agent.md` §4.6, *Installed Channel*).
- **Enforcement Gate** — a check outside the text that turns "should"
  into "cannot": a hook, CI, a human review
  (`docs/models/agent.md` §7, *The Enforcement Gate*).
- **Tool Binding** — the mechanisms one tool gives the channels and
  the Enforcement Gate, written by the repo that uses the tool
  (`docs/models/agent.md` §10, *The Tool Bindings*).

## The concept and the method

Their Names are in `delivery/method/docs/glossary/method.md`.

## The stack

Its Names are in `delivery/spring-postgres/docs/glossary/stack.md`.
