# correctness-by-construction

One canonical home for a single concept: **correctness by
construction** — the design principle that correctness is built into
the structure of a thing rather than tested in afterwards. The repo
holds the plain-words statement of the concept (with its rationale,
open questions, and the log of what changed it and why) and what is
Made Usable from it — agent skills, checklists, templates —
each pinned to the concept version it derives from. It also holds
the Container Group a CBC Run is born into — its own (ADR-0024,
ADR-0025; where it came from is ADR-0038's record) — so a CBC Run has
one upstream and one Delivery Pin. It is the Concept Deliverer: each CBC Run is born from
what this repo ships, and is read back from here. Documents only:
nothing is built here, no application, no service, no CBC Run.
It is a Concept Repo, the concepts tier of the workspace
(Concept Repos → Run Repos, the tier above empty; see `docs/models/tiers.md` §2.1, *The empty top tier*, §2.2, *Concepts*):
CBC Runs happen in other repos pinned to
a concept version, and their surprises come back here as changes to
what we hold: the concept, the Idea Models, the conventions, and the
masters made from them.
It exists so its author's understanding improves in a
recorded way instead of living in a head and scattered notes.

## Success criteria

- The concept statement here is the single canonical version;
  the archive copy is demoted to a historical snapshot.
- The Record Harvest loop has run end-to-end at least once: a real CBC Run's
  surprise recorded as a concept change with provenance, and the
  affected skill re-derived.
- At least one new CBC Run is born from what this repo Made Usable,
  copied from it, not from the archive.
- Months-scale: the concept doc is actually consulted and updated
  after CBC Runs.

## Out of scope

- Running projects or experiments here — CBC Runs happen in their own
  repos, pinned to a concept version (the Run Repo tier).
- A general method or working arrangement — the conventions
  shipped here are this repo's, held for CBC Runs and changed by
  what runs live (ADR-0025, ADR-0031). A second repo that needs
  them copies parts, and anything general waits on three
  (ADR-0038; `docs/models/tiers.md` §2.1, *The empty top tier*).
- Garden machinery — none until the Concept Garden rule triggers: a second
  Concept Repo, a rule written twice (`docs/models/tiers.md` §2.2, *Concept Repos*).
- Graduating an execution to its own concept repo — same trigger,
  not now.
- Everything in the archive repo outside the two directories named
  in the birth briefing.

## Project records

| Record | Where | What it answers |
|---|---|---|
| Plan | [PLAN.md](PLAN.md) | The Plan Step being worked, and what *done* means for it |
| Decisions | [docs/adr/](docs/adr/) — cited from other repos as `CBC ADR-nnnn` | Why is it built this way |
| Architecture | [ARCHITECTURE.md](ARCHITECTURE.md) | The map: what is here, what ships, and what must stay true |
| Backlog | [TODO.md](TODO.md) | What's next, and what's known but not done |
| Backlog's talk | [TODO-CONVERSATION-MEMORY.md](TODO-CONVERSATION-MEMORY.md) | The talk that shaped each TODO item, on trial |
| Changelog | [CHANGELOG.md](CHANGELOG.md) | What changed per concept version, for those who pin one |
| Devlog | [devlog/](devlog/) | What happened, the dead ends, where to resume |

A summary. Every record in both Convention Seats, the CBC Run's and this repo's,
and where each is explained, is the records map:
[project-recording §1](docs/conventions/project-recording/README.md).

<!-- A line here is true now, and meant for someone arriving from
     outside. What changes weekly is TODO.md's; why is the ADRs'; how
     it went is the devlog's. A missing section is not an omission: it
     arrives when a Plan Step's gate makes it true — projection follows
     truth.
     Why the form is as it is: (docs/conventions/project-recording/
     §7.4, How a README is written).
     foundation: the project-recording convention -->
