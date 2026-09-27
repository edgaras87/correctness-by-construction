# Commit plan: the handbook filtered out of live text

## Summary — the state after all commits

No live file of this repo tells the handbook's story. What a run
receives cites only decisions it can be handed — `CBC ADR-nnnn` —
and the six handbook decisions the two shipped skills rested on are
adopted as ours in one ADR, with each one's claim stated so the
adoption is readable without the handbook. The same ADR says the
handbook is history: where the bytes came from is a fact recorded
once, and no re-sync is planned, protected or prepared for. The
coordinates ADR-0025 and ADR-0026 kept as protection, the delta
list kept as a re-sync aid, and the two reopen triggers — a second
repo wanting the kit, the handbook revived — are superseded by the
reviewer's rule: a second repo copies parts of this one, a third
does the same, and only after three is anything handbook-like
considered. Nothing in live text repeats those hashes, keeps a
diff command current, promises a re-verify, or names the handbook
as a tier above this repo. The manuals
say their why in this repo's voice, as text this repo owns since
ADR-0025 rather than as a copy narrating another repo's history.
README's scope says what is true: the conventions shipped here are
ours to hold, changed by what runs live. TODO's handbook-filter
item is closed, and the citation rule in the conventions index
knows one tag, ours.

The tiers model says what is true: two tiers today, concepts and
runs, the top row empty until three repos say otherwise. ADR-0026
decision 4 let a model's body change only when something lived
here contradicted it; the reviewer's rule is that contradiction.
The agent model keeps its evidence, which is the handbook's own
history and says so — attribution, not the handbook's voice — and
its subject sentence names the conventions a project was born
with rather than "the handbook's". The records — ADRs, devlog,
TODO, CHANGELOG, the registry, PLAN's closed gates — are history
and are not touched, except the three TODO items that waited on
the handbook being opened again, triaged at the records commit.

## Commits

**1. `docs(agent): add commit plan for the handbook filter`**
This file.

**2. `docs(adr): ADR-0038 — the handbook's decisions become ours`**
Opens Proposed. Adopts, by number and title with the claim each
one made, the six handbook decisions the shipped skills cite
(their 0005, 0010, 0019, 0025, 0027, 0035), so a run's skill can
cite one decision of ours and a maintainer here can read why.
Records the provenance coordinates once — `ba7eaa4` taken,
`8adb46f` last aligned, `dc3b7db` / `9a1637d` / `df9d5ed` where the
container, the manuals and the models landed, `c670fe5` for the
default playbook — and says these are the ADR's now, amending where
ADR-0025 decision 2 and ADR-0026 decision 2 put them. Retires the
`HANDBOOK` tag from shipped text; the tag rule ADR-0020 adopted is
unchanged, since a run still cites us. Decision-first: the shape
was settled in the TODO item and this conversation.

**2a. `docs(adr): ADR-0038 says the handbook is history`**
Revision at step 5's boundary, the ADR still Proposed. Retitled.
Decision 2 no longer keeps coordinates *for* a re-sync: the
hashes stay as the fact of where the bytes came from, the paths at
landing go with the diff guidance, and the decision supersedes
ADR-0025 decisions 2, 4 and 7 and ADR-0026 decisions 2 and 5,
stating the reviewer's rule of three in their place. Decision 5
changes: the tiers model's body is edited, the agent model's
subject sentence too. Consequences rewritten: the cost is no
longer "a re-sync diff grows", it is that a fourth repo, if one
comes, starts from what this repo holds then and not from a fork
point. The set's other decisions are unchanged.

**3. `refactor(container): shipped files cite CBC, not the handbook`**
The two shipped skills' Decisions footers cite `CBC ADR-0038`; the
decisions-log stub's header line and its birth entry's "began as
the engineering-handbook starter kit" go; the container's `PLAN.md`
placeholder loses "handbook or", and the seed's `sed` that matches
that placeholder changes in the same commit, or birth breaks. The
conventions index's two citation lines — the artifact rule's
"each as `HANDBOOK ADR-nnnn`" and the container rule's two-tag
clause — say `CBC ADR-nnnn` only. A manual and its artifacts move
together (the index's own rule).

**4. `chore(agent): our copies of the two skills follow`**
`.claude/skills/commit-plan` and `commit-messages` take the same
footers, with a registry entry. Agent-scoped, so it cannot share
step 3's commit.

**5. `docs(delivery): the container's provenance becomes history`**
`delivery/README.md`'s container half keeps what the container is
and loses the provenance passage, the kit-pin line, the landed-at
anchor and its diff command, and the closing "they are the
handbook's rules, passed on unedited", which ADR-0025 made false;
the seed's "no `handbook_dir`" paragraph says one pin without
naming what it is not; `playbooks/default.md`'s header says whose
it is now; the playbook fill's "refresh against a new kit pin"
clause, an obligation ADR-0025 removed, goes; ARCHITECTURE's
container section, its diagram's origin node and the delivery
codemap row follow. Coordinates that leave point at ADR-0038.
Widened at its boundary: the delta table, "what differs from what
we took", was a re-sync reading aid (ADR-0025 decision 4) and now
has no reader. Its rows are true facts about the container — the
entry file's address, the composed bodies, one pin, the exchange
in place of `convention-lifecycle`, `visual-comparison` ours — so
the table stays as a description of the container's own shape, in
this repo's terms, and the sentence calling it a reading aid goes.
ARCHITECTURE's taken-material invariant, which names the three
live sections as where the coordinates are held, goes with them:
a fact in an ADR is not an invariant anything enforces.

**6. `docs(conventions): the manuals' and models' provenance becomes history`**
`docs/conventions/README.md`'s "Where these files came from"
section goes, and so does "no compare runs on a schedule", which
told a re-sync where to start; the one standing rule — a manual
and its artifact move in the same commit — moves up under the
container's rules. Both models' header comments say "this repo's
(ADR-0026); where it came from, ADR-0038" and nothing else about
it. The tiers model's body: §1's shape and §2's first tier say the
top row is empty — no repo owns method above this one, and the
rule of three says when that is reconsidered; the upward channels
in §3 and §4 that named the handbook name the tier above, which
today is nobody. The agent model's §2 subject sentence names the
conventions a project was born with. ARCHITECTURE's models and
conventions codemap rows follow.

**7. `docs(conventions): agent-arrangement says its why in our voice`**
Twenty-six mentions, the most of any manual. Each inline
`HANDBOOK ADR-nnnn` becomes the reason in prose where the manual
does not already give it, is dropped where it does, or becomes
`ADR-0038` where the decision is one adopted there.

**8. `docs(conventions): project-recording says its why in our voice`**
Fifteen mentions, the same treatment. The tag example
`HANDBOOK ADR-0014` becomes a run's tag citing ours, which is the
case that exists.

**9. `docs(conventions): repo-hygiene, commit-plan and commit-messages in our voice`**
Sixteen mentions across the three. repo-hygiene's overlay
procedure stops reading from a handbook checkout and names this
repo's `templates/` directory; commit-messages' "the handbook's
answer was `docs(handbook)`" paragraph keeps the rejected option
without the narrative.

**10. `docs: README's scope, the records, and ADR-0038 accepted`**
README's intro and out-of-scope bullet say the container and the
conventions are this repo's, with authoring bounded by ADR-0025's
trigger rather than by the handbook owning method. ADR-0038 flips
Accepted; ADR-0025 and ADR-0026 gain a Status line naming the
amendment. CHANGELOG: what a run receives at its next delivery
cites CBC only. TODO: the filter item is ticked; the note held
for the handbook's ADR-0038 and the handbook's invitation are
dropped, since the repo they wait on is not opened; the overlay
marker suggestion loses "handbook" from its name and keeps its
trigger, a second method bundle. The sweep: `HANDBOOK` in
live text is zero, and `handbook` survives only where the summary
says it does, counted in the commit body.

**11. `docs(agent): close commit plan for the handbook filter`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **One ADR, not six.** Six adoptions in one record, each a
  numbered line with its claim. The TODO asked for one; six would
  spend six numbers on decisions taken elsewhere and read as if we
  had weighed the options ourselves.
- **The models' bodies: the tiers model changes, the agent model's
  evidence stays** (revised at step 5's boundary; the plan first
  said both stay). ADR-0026 decision 4 lets a body change when
  something lived here contradicts it. The reviewer's rule — no
  handbook until three repos exist — contradicts the tiers model's
  first tier directly, so it is edited. The agent model's mentions
  are the source of its evidence, which nothing contradicts; they
  stay.
- **The delta table is described, not deleted** (revised at the
  same boundary). Deleting it would lose five facts about the
  container that are true whatever they are compared against;
  keeping it as a comparison would keep a reader who does not
  exist. The comparison ends; the facts stay where a reader of the
  delivery looks for them.
- **ADR-0038 is revised rather than a second ADR written.** It is
  Proposed and a living document until the flip; the re-sync
  premise was its own, so it is the record that changes.
- **`temp/README.md`'s dated episode stays.** Its purpose line is
  rewritten in step 5 with the seed; the 2026-09 note about the
  handbook mistaking our run's name is a recorded event, not live
  guidance.
- **The manuals lose citations rather than gaining a table.** A
  manual is the why; a `HANDBOOK` number pointed past the manual at
  a record the reader cannot open. Writing the reason in is the
  rewrite; a mapping table of our numbers to theirs lives in
  ADR-0038 alone, for whoever holds a handbook checkout.
- **Order is decision-first throughout.** Nothing here waits on a
  shape only seeable in the material: the mentions were read in
  full before this plan, and the three kinds of work were named in
  the TODO on 2026-09-26.
