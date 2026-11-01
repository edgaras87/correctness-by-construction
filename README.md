# correctness-by-construction

One canonical home for a single concept: **correctness by
construction**, the design principle that correctness is built into
the structure of a thing rather than tested in afterwards.

- **What it holds:** the plain-words statement of the concept, with
  its rationale, open questions, and the log of what changed it and
  why. And what is made usable from it: Agent Skills with their Agent
  Skill Templates and checklists, and Output Shapes, each pinned to
  the concept version it derives from.
- **The Container Group:** it also holds the files a CBC Run is born
  into, as its own (ADR-0024, ADR-0025; where they came from is
  ADR-0038's record). So a CBC Run has one upstream and one Delivery
  Pin.
- **The Concept Deliverer:** this repo is the Concept Deliverer. Each
  CBC Run is born from what it ships, in a repo of its own pinned to a concept version, and is read
  back from here.
- **Documents only:** nothing is built here, no application, no
  service, no CBC Run.
- **Its tier:** a Concept Repo, the concepts tier of the workspace,
  with the tier above empty (`docs/models/tiers.md` §2.1, *The empty
  top tier*; §2.2, *Concept Repos*).
- **What comes back:** a CBC Run's surprises return as changes to what
  we hold: the concept, the Idea Models, the conventions, and the
  Master Copies made from them.
- **Why it exists:** so its author's understanding improves in a
  recorded way instead of living in a head and scattered notes.

## Success criteria

- The concept statement here is the single canonical version;
  the archive copy is demoted to a historical snapshot.
- The Record Harvest loop has run end-to-end at least once: a real CBC Run's
  surprise recorded as a concept change with provenance, and the
  affected Agent Skill re-derived.
- At least one new CBC Run is born from what this repo made usable,
  copied from it, not from the archive.
- Months-scale: the concept doc is actually consulted and updated
  after CBC Runs.

## Out of scope

- Running projects or experiments here — that is the CBC Runs', as
  the opening says (the Run Repo tier).
- A general method or working arrangement — the conventions
  shipped here are this repo's, held for CBC Runs and changed by
  what the CBC Runs live through (ADR-0025, ADR-0031). A second repo
  that needs them copies parts, and anything general waits on three
  repos (ADR-0038; `docs/models/tiers.md` §2.1, *The empty top tier*).
- Garden machinery — none until the Concept Garden rule triggers: a second
  Concept Repo, a rule written twice (`docs/models/tiers.md` §2.2, *Concept Repos*).
- Moving a CBC Run into a Concept Repo of its own — same trigger,
  not now.
- Everything in the archive repo, `system-design-method`, beyond the
  concept chapters taken from it (`CHANGELOG.md`, *[v1]*).

## Project records

| Record | Where | What it answers |
|---|---|---|
| Plan | [PLAN.md](PLAN.md) | The Plan Step being worked, and what *done* means for it |
| Decisions | [docs/adr/](docs/adr/) — cited from other repos as `CBC ADR-nnnn` | Why is it built this way |
| Architecture | [ARCHITECTURE.md](ARCHITECTURE.md) | What is here, what ships, and what must stay true |
| Backlog | [TODO.md](TODO.md) | What's next, and what's known but not done |
| Backlog's talk | [TODO-CONVERSATION-MEMORY.md](TODO-CONVERSATION-MEMORY.md) | The talk that shaped each TODO item, on trial |
| Changelog | [CHANGELOG.md](CHANGELOG.md) | What changed per concept version, for those who pin one |
| Devlog | [devlog/](devlog/) | What happened, the dead ends, where to resume |

A summary. Every record in both Convention Seats, the CBC Run's and this repo's,
and where each is explained, is project-recording's list of the
records (`docs/conventions/project-recording/` §1, *The records at a glance*).

<!-- A line here is true now, and meant for someone arriving from
     outside. What changes weekly is TODO.md's; why is the ADRs'; how
     it went is the devlog's. A missing section is not an omission. It
     arrives when a Plan Step Gate makes it true, since the README says
     only what is already true.
     Why the form is as it is: (docs/conventions/project-recording/
     §7.4, How a README is written).
     foundation: the project-recording convention -->
