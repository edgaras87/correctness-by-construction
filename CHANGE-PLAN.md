# Change-plan: the update procedure shows its shape

## Summary — the state after all commits

`starter/installs/bundle-update.md` opens with a Mermaid flowchart
of its seven steps, its prose unchanged beneath it. The picture
carries what the prose could not show at a glance: the order, the
three actors, the boundary between two repos, and the one record
each side writes.

`.claude/skills/format-comparison/SKILL.md` states the method that
produced it, so the third format question does not re-derive it:
write what the artifact must carry, render candidates against it,
judge per requirement, let the render decide. It carries the two
warnings the two runs have accumulated.

ADR-0028 records both — why that shape and not the other three,
what the comparison cost the spec it was judged against, and that
ADR-0027 decision 5's trigger fired and was answered rather than
parked.

## The kind and the home, which are two questions

**Kind, by artifact-kinds' axes:** *executes* (a step sequence with
gates) and *template* (copied into a fresh `temp/` draft each time)
point at **playbook**, and its test — *do you copy it to use it?* —
is yes. Not a convention: "do they owe an explanation if they
ignore it" is thin here.

**Home, by agent-arrangement §2**, which is a different question
and was answered wrong first. A rule with a moment goes where the
moment is, and §2 names a skill as one of those places. This has a
sharp moment — a format is in question — so it is neither
entry-file content nor `playbooks/` content. It becomes
`.claude/skills/format-comparison/SKILL.md`.

`playbooks/` was the first answer, and the reason it failed is
worth keeping: that directory has no channel. Nothing routes an
agent to it; it is read only when a project playbook is copied into
a PLAN at Framing. A method filed where no moment sends anyone goes
stale unread.

**A tension to note rather than resolve:** a native skill now sits
beside four pinned convention copies, and what distinguishes it is
absence — no pin header, no manual, no registry entry. Weak, but
real. Worth marking positively if a second native skill arrives.

## Commits

**1. `docs(temp): the shape is compared, four candidates`**
The draft: what the shape must carry, four candidates, a pass/fail
per requirement, and the two findings that only building them
produced. Lands first because the ADR reads as a verdict on
evidence — even though the draft is deleted at step 5 and the ADR
must stand without it.

**2. `docs(adr): the procedure gets a picture, the method a playbook`**
ADR-0028. Decision-first, following ADR-0027's own order: settled
in conversation, confirmed by a render, recorded before implemented.

**3. `docs(starter): the update procedure shows its shape`**
Diagram C into `bundle-update.md`, above step 1. The prose is not
touched.

**4. `docs(agent): spec, then render`**
`.claude/skills/format-comparison/SKILL.md`. Lands after the
instance, not before: a playbook is distilled from what held, which
is why `default.md` carries a "Last updated from project" line.
Agent scope, not project — it changes what the agent is arranged
with, and the agent/project commit split has held since Step 0.

**5. `docs(temp): the comparison is spent`**
Delete the draft. It has served; git history keeps it.

**6. `docs: the records catch up`**
TODO gains the `playbooks/default.md` finding below; the devlog
gains the session — step 7's verdict home and restructure, and
this comparison.

## Decisions taken inside this plan

- **The prose stays whole.** The tempting move after adding a
  picture is to thin the text under it. Refused: the reasoning in
  these steps is load-bearing at execution time, which is the
  finding that rejected the manual-and-rule split.

- **Requirement 5 is struck, not failed.** No candidate could carry
  the conditionals, which is evidence about the requirement. A
  branch is decidable only with its reason attached. Recorded in
  the ADR so the next comparison inherits a corrected spec.

- **The trial now spans two files.** Both never ship, so no run
  inherits a renderer. What changes is that ADR-0027 decision 2's
  revert, if it fires, is now two reverts.

- **It does not ship, and the trigger is named** — the first run
  that actually faces a format question, seen through the harvest
  loop. Two reasons stand: the kit delta is at its ceiling, and a
  method *about* the work is Step 9's question. A third died when
  the home moved — a skill has an obvious slot where a playbook
  file had none — and ADR-0028 records that rather than deleting
  it.

- **ADR-0027 decision 5 is answered, not parked** (the user's call,
  against my recommendation to wait for a third instance). The
  trigger fired as written and the method becomes a playbook. My
  objection stands in the ADR rather than being dropped: two uses
  by one author in one week is thin evidence, and the playbook's
  own warnings list is the place that will show it — a playbook
  whose warnings never grow was distilled too early.

## Discovered along the way

- **`playbooks/default.md` still carries the dead ADR-0002 rule**
  — "Pinned: do not edit here — changes happen in the handbook and
  arrive as a fresh pinned copy". ADR-0026 hunted exactly this
  sentence and missed this file; nothing in this repo tracks the
  handbook, so the rule cannot fire. Not fixed in this set — it is
  ADR-0026's subject, not this one's. To TODO at commit 6.

- **And the grep that found it had to be written twice.** The
  first search missed it, because the sentence wraps across lines
  and the file stores it as "do not edit\n     here". Third
  instance of one lesson: a search for one spelling of a thing
  that exists in several. The `§8` hunt that missed `§7`, the
  renumbering described without reading its range, and now a
  phrase broken by a line wrap.
