# Glossary: the shared Names

<!-- The Names the delivered Agent Skills, Agent Rules, Output Shapes
     and Approaches on Trial are written in, shared by this project
     and its Concept Deliverer, each from this project's side: one
     plain sentence, with its owner where it has one. A pinned copy,
     like every delivered file: changed only as
     .claude/rules/delivered-copies.md says. This project's own Names
     are docs/glossary.md's.
     foundation: the writing convention -->

- **Concept Deliverer** — the repository this project was born from
  and is read back by; it delivers copies and reads this project's
  records, and this project never reaches into it.
- **CBC Run** — this project: a repository born from the Concept
  Deliverer to build a real system by correctness by construction.
- **Concept Repo** — any repository that holds one concept and what
  is made from it; the Concept Deliverer is one.
- **Delivery Pin** — the Concept Deliverer's commit every delivered
  copy here equals, but for its *Decisions* footer, kept in the
  Decisions Log's last delivery entry.
- **Master Copy** — the Concept Deliverer's copy of a file delivered
  here; a copy here follows it and is diffed against it.
- **Read-Through Commit** — this project's own commit the Concept
  Deliverer last read up to, named by each Delivery Note.
- **Delivery Note** — the text beside a delivery: what changed since
  the Delivery Pin, why it matters here, and a verdict on every CBC
  Run Ask.
- **Delivery Staging** — a delivery as it arrives in `temp/`: a
  directory named for the Concept Deliverer's commit, the Delivery
  Note beside it, in force only once taken.
- **Delivery Take** — moving a Delivery Staging into place and
  recording the new Delivery Pin, as `.claude/rules/delivered-copies.md`
  says.
- **CBC Run Ask** — one line under TODO's *To the deliverer*, asking the
  Concept Deliverer for a verdict: on an edit to a copy, a file
  offered, or a question.
- **CBC Run Reading** — the Concept Deliverer reading this project
  since it last read it, and the text that records what it found;
  read only, it writes nothing here.
- **CBC Run Briefing** — the text that names the problem this project
  builds, read at CBC Framing and committed unchanged.
- **CBC Run Hand-off** — the text that says how this project works
  on full auto, when it does; it arrives in `temp/` with the CBC Run
  Briefing.
- **Pure Seed** — the Concept Deliverer's procedure that gave this
  project its birth.
- **Entry File** — the file the tool loads at session start, before
  the first task: `CLAUDE.md`.
- **Living Text** — text kept true as things change: every text here
  but history, which records what was true then and is never updated
  (`.claude/rules/one-home.md`, *Not a second home*).
- **Record Stub** — a record as it was born: the shipped file with
  its header comment and headings, this project's own from its first
  entry on.
- **Agent Rule** — a file under `.claude/rules/`, loaded into the
  agent by path or in every session; a numbered line inside one is
  named by its owner and number, "delivered-copies rule 4".
- **Output Shape** — a presumed output, written from outputs that
  exist and read only at a Plan Step Gate, when the Plan Step closes
  (`.claude/rules/shapes-lifecycle.md`). A particular one is named
  by its output: the Enemy Collision Kill Shape.
- **Agent Skill** — a file under `.claude/skills/<name>/`, its
  `SKILL.md` and what it references, read when its moment comes;
  always written with its kind: the commit-plan Agent Skill.
- **Agent Skill Template** — a file under an Agent Skill's `templates/`, copied
  and filled by this project, never edited in place.
- **Hygiene Base** — the hygiene files every repo gets before it has
  a stack, `.gitignore`, `.gitattributes` and `.editorconfig`, down to
  each one's marked line.
- **Stack Overlay** — the stack's part of a hygiene file,
  `.gitignore`, `.gitattributes` or `.editorconfig`, below the
  Hygiene Base's marked line.
- **Approach on Trial** — the written way of doing one kind of work
  that no Agent Skill covers yet, at `.claude/approaches-on-trial/<work>.md`,
  drafted under the approach-drafting Approach on Trial.
- **Work Approach** — how a piece of work is done: an Agent Skill, an Agent
  Rule, or an Approach on Trial.
- **Plan Step** — one piece of `PLAN.md`'s work, with a goal and a
  Plan Step Gate; named by its number, Step 0. The Plan Step Form is
  `PLAN.md`'s own.
- **Plan Step Gate** — a Plan Step's exit criteria: facts that can be
  checked, written when the Plan Step opens; it is done only when
  every one is true.
- **Agent Skill Stage** — one phase of an Agent Skill, numbered from Stage 0 and
  named by its Agent Skill outside it: the cbc-slice Agent Skill's
  Stage 3.
- **Approach on Trial Stage** — one phase of an Approach on Trial,
  numbered, under its own heading
  (`.claude/approaches-on-trial/approach-drafting.md`, *Stages*).
- **Decisions Log** — `.claude/decisions.md`: the agent's own setup
  decisions, the Work Approaches held, and each delivery's Delivery Pin
  and Read-Through Commit.
- **Change Set** — a body of work that needs more than one commit,
  planned and closed under the commit-plan Agent Skill.
- **Idea Model** — a Concept Deliverer's text stating an idea any
  repository can adapt; this project holds none and may meet the
  word in a delivered Agent Skill.
- **Glossary Name** — the name of a thing this project defines: two
  or more words, capitalized, written exactly; what this file lists.
