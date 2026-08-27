---
name: change-plans
description: How work larger than one commit is planned, reviewed at each boundary, and closed. Use before starting a change set that needs more than one commit.
delivery: pushed
requires: commit-messages, artifact-kinds
---

# Change-Plans Convention

How a body of work that needs more than one commit is planned before it
starts, reviewed as it lands, and closed. The unit is one **change
set** — the scope between a single commit (`commit-messages`) and a
whole project (`project-recording`).

<!-- The artifact is a change-plan: agreed up front, committed, revised
     only when reality diverges, deleted at the close. Its content
     survives as the commit messages it produced; the file itself is
     recoverable from history. See ADR-0010. -->

---

## 1. When a change-plan is needed

Write one when the work is **worth splitting into more than one
commit**. A single-commit change gets none — the plan costs two extra
commits, and that only pays for itself across a sequence.

Reach for one especially when the change set is large enough that you
would otherwise discover halfway through that the split was wrong, or
when someone other than the author is reviewing as it lands.

## 2. The artifact

One file, `CHANGE-PLAN.md`, at the repo root. One at a time — a second
concurrent change set means the first should have been finished or
abandoned.

Root placement is deliberate: an in-flight change set is then visible
from a clean clone, so "is work half-landed, and where did it stop?"
is answerable without reading the working tree.

```markdown
# Change-plan: <what this change set does>

## Summary — the state after all commits
<Prose. The end state, not the steps. What the repo looks like once
this is done, and what it gives us that it did not have before.>

## Commits

**1. `<type>(<scope>): <subject>`**
<What this commit does, or what it gives us, or both — whatever tells
the reader why this step exists as its own step.>

**2. `<type>(<scope>): <subject>`**
<…>

## Decisions taken inside this plan
<Judgment calls made while planning that a reviewer should see and
could reasonably object to. Optional, but usually the most useful
section.>
```

Commit subjects follow `commit-messages`. The per-step note is not the
commit body — it is why this step is a step. The body gets written at
commit time.

**Status is not tracked in the file.** No checkboxes, no `[x]`. Git
history is the status: the commits that exist are the steps done.
Tracking status here would couple every work commit to a plan edit,
breaking atomicity, and would reintroduce the staleness that makes a
neglected `PLAN.md` lie.

## 3. How steps are split

**By change, not by artifact.** One step is one coherent thing the repo
needs, whatever number of files that touches. One file may appear in as
many steps as it has distinct changes to make.

The test is **revert**: undo a single step, and the repo must land in a
coherent state.

- A convention document and the README row listing it are *one* step —
  reverting the document alone would leave the table pointing at a
  missing file.
- Adding a plan, revising it on divergence, and deleting it at the
  close are *three* steps on the same file — three different needs.

This is the `commit-messages` rule "one logical change per commit"
applied ahead of time instead of at commit time. The failure mode it
prevents is grouping by file type — "all the doc files," "all the
record files" — which produces commits that look tidy and revert
incoherently.

## 4. Lifecycle

| Step | Commit | Contents |
|---|---|---|
| Open | `docs(agent): add change-plan for <X>` | the approved plan |
| Work | the steps themselves | as planned; stop at each boundary |
| Diverge | `docs(agent): revise change-plan — <what changed>` | only when reality diverged; body says why |
| Close | `docs(agent): close change-plan for <X>` | deletes the file; **body records what diverged** |

The plan is committed **after** it is agreed, before any of the work.
That timestamps the agreement, so the series can be read against its
own plan afterwards.

The closing commit's body is the change set's retrospective: what
diverged from plan, and why. It is the cheapest retro that exists and
it is greppable. If nothing diverged, say so — that is information
too. An abandoned change set closes the same way, with the reason.

## 5. Divergence

When a step turns out to need something other than what was planned:

1. Stop before committing it.
2. Re-evaluate the **remaining** steps — a changed step often
   invalidates later ones, and the whole point of the plan is that the
   tail is no longer trustworthy on its own.
3. Revise `CHANGE-PLAN.md` and commit the revision on its own, with a
   body explaining what forced it.
4. Continue.

The revision commit is what makes a divergence first-class: a diff
between the commits it separates, rather than an invisible mental
adjustment nobody can reconstruct later.

## 6. Review protocol

Work stops at every commit boundary. The reviewer inspects the actual
diff before it lands, and may ask for an explanation of any part of it
before agreeing to continue.

This matters most when an agent is doing the committing: the boundary
is the only place where a misunderstanding is cheap to catch. Without
it, a wrong assumption in step 2 propagates silently through every
later step, and the review becomes an archaeology exercise.

## 7. Anti-patterns

- **Grouping steps by file type.** Tidy-looking, reverts incoherently.
  See §3.
- **Checkboxes in the plan.** Status belongs to git history; a plan
  that tracks it will go stale and start lying.
- **Writing the plan after the work.** Then it is a summary, not an
  agreement — nothing was reviewable, and divergence is unrecorded.
- **Plans for single commits.** Ceremony that outweighs the change.
- **Keeping the file after the close.** It becomes a stale duplicate of
  facts that now live in the commit messages. Delete it; history keeps
  it.
- **Silent divergence.** Quietly doing something other than the plan
  and fixing the plan afterwards, or not at all.

## 8. Relation to other records

**Not a `PLAN.md`.** A change-plan is the artifact-kinds `plan` kind
specialized to change-set scope (permitted by artifact-kinds §3:
contexts may specialize, not contradict). The two differ absolutely in
lifetime — `PLAN.md` is durable and carries live status; a change-plan
is ephemeral and carries none — which is a distinction the artifact-
kinds axes do not currently express.

**Not a record.** It is a scaffold. Everything durable in it survives
as commit messages; nothing about it is meant to be read a year later
except through `git log`. That is why it is not part of
`project-recording`, whose records are all append-or-evolve (ADR-0010).

**Feeds the devlog.** A divergence worth remembering beyond the change
set — a dead end, a wrong assumption about the codebase — gets promoted
to a devlog entry. The closing commit body is per-change-set; the
devlog is per-project.

## 9. Origin

The practice is the kernel and git mailing-list **patch series** —
one logical change per patch, ordered so each applies on the last,
reviewed patch by patch rather than as a lump — carried into a repo
where work is committed directly instead of mailed. What is added here
is the plan agreed *before* the series is written, and its disposal
afterwards.

See ADR-0010 for why this is a separate convention, and for the
options rejected.

---

## Delivery

`pushed` — it fires when work turns out to need more than one commit.

That trigger is weaker than it looks. Recognising that a change set is
large is a judgment, and a convention firing on judgment misses exactly
when the judgment fails. Nothing catches the miss, which is why "the
plan written after the work" is an anti-pattern here (§7) rather than
a lapse.

**What this constrains.** It has to be usable at the moment it fires —
mid-task, before anything is committed — so a cross-reference is a cost
paid then, not while studying the document. And any rule here that
delegates to another convention belongs in `requires` (ADR-0017).
