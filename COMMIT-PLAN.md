# Commit plan: the handbook filtered out of live text

## Summary — the state after all commits

No live file of this repo tells the handbook's story. What a run
receives cites only decisions it can be handed — `CBC ADR-nnnn` —
and the six handbook decisions the two shipped skills rested on are
adopted as ours in one ADR, with each one's claim stated so the
adoption is readable without the handbook. Where the bytes came
from is a fact recorded once, in that ADR, with every coordinate a
re-sync would need: the take, the last aligned state, and where
each set landed here. Nothing in live text repeats those hashes,
keeps a diff command current, or promises a re-verify. The manuals
say their why in this repo's voice, as text this repo owns since
ADR-0025 rather than as a copy narrating another repo's history.
README's scope says what is true: the conventions shipped here are
ours to hold, changed by what runs live. TODO's handbook-filter
item is closed, and the citation rule in the conventions index
knows one tag, ours.

What stays, and is named rather than filtered: the two models'
bodies. Their evidence is the handbook's own history, taken
verbatim under ADR-0026 decision 4 and edited only when something
lived here contradicts them. Naming where evidence came from is
attribution, not the handbook's voice. The records — ADRs, devlog,
TODO, CHANGELOG, the registry, PLAN's closed gates — are history and
are not touched.

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

**6. `docs(conventions): the manuals' and models' provenance becomes history`**
`docs/conventions/README.md`'s "Where these files came from"
section goes; its one standing rule — a manual and its artifact
move in the same commit — moves up under the container's rules.
Both models' header comments say "this repo's (ADR-0026); where it
came from, ADR-0038" and nothing else about it. ARCHITECTURE's
models and conventions codemap rows follow.

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
cites CBC only. TODO's item is ticked. The sweep: `HANDBOOK` in
live text is zero, and `handbook` survives only where the summary
says it does, counted in the commit body.

**11. `docs(agent): close commit plan for the handbook filter`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **One ADR, not six.** Six adoptions in one record, each a
  numbered line with its claim. The TODO asked for one; six would
  spend six numbers on decisions taken elsewhere and read as if we
  had weighed the options ourselves.
- **The models' bodies stay as taken.** The TODO counted
  `agent.md`'s 24 mentions among the text to rewrite; ADR-0026
  decision 4 says the bodies change only when something lived here
  contradicts them, and nothing has. Their evidence is the
  handbook's history and says so. Headers go, bodies stay, and the
  open item on whether `docs/models/` still matches reality keeps
  the rest. If the reviewer reads the TODO as overriding ADR-0026,
  step 6 widens and the ADR is amended in step 10.
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
