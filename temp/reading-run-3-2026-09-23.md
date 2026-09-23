<!-- A reading: what one pass over run 3 found, and the work it
     implies. Written 2026-09-23, before any of the work.

     This one stays here. temp/'s rule about our vocabulary binds
     what leaves for a run; nothing in this file is going to one,
     so it cites our ADRs and paths freely. What goes to run 3 is
     the note at item W9, written separately.

     It is a scaffold, not a record. The list below is revised as
     items land — settling one can reword or delete others — and
     the file is deleted when the work closes. History keeps it.
     Findings go to TODO, decisions to ADRs, the session to the
     devlog; this file is where they wait until they have a home.

     Its list is not a commit plan. These are things that must be
     done or considered; several will open a commit plan of their
     own, and those are named per item. -->

# Reading: run 3, through `9869798`

## Where we read to

**Run 3 (`never-oversold`, `~/IdeaProjects/cbc-pure-run-3`) read
through `9869798`, 2026-09-23 01:14.** Previous reading stopped at
`adc90f6`, 2026-09-20 14:48 — 45 commits.

That previous point had to be excavated today: our devlog entry of
2026-09-20 named the delivery, and the commit was found by matching
its date against the run's log. This line exists so the next reading
does not repeat that. Where it lives permanently is D7.

## What the run did

**Step 6 — SL-2 closed** (`correction-never-undercuts`). It added
no production code: SL-1's wall and ADR-0011's value-shaped door
already covered it, so the slice is evidence plus two structural
guards. 29 tests to 39. Version 0.2, two of four invariants
evidence-closed. SL-3 is next.

**A writing pass, on its own branch, 19 commits.** It began as "the
records are hard to read" and ended with two artifacts nobody had
asked for: `.claude/shapes/slice-record.md` and
`.claude/rules/shapes-lifecycle.md`. The mechanism it arrived at is
the part that travels: a shape sits where nothing loads it, or
where a `paths:` line loads it while the matching artifact is
written, and **the directory decides whether it is in front of the
writer.**

**Three in-place edits of copies pinned at `4c3ac99`**, the second
firing of the machinery ADR-0034 was written for. Two to
`cbc-slice`, one to `artifact-kinds`. Their reasons are in the
run's decisions log at 2026-09-21 and 2026-09-22.

**Four hand-offs**, one of which asks this repo for a role it does
not have.

## Findings

**F1 — our entry file names a file that no longer exists.**
`CLAUDE.md:25` says `CHANGE-PLAN.md`; the convention renamed it to
`COMMIT-PLAN.md` on 2026-09-19, and `delivery/container/.claude/CLAUDE.md:50`
has it right. Wrong for four days in the one file loaded in full on
every task. **Fourth instance of the class** run 3 has now caught us
on three times — and our own `bundle-update.md:133` uses this exact
rename as the worked example when telling a run to sweep for it.

**F2 — possibly more of the same noun in shipped files.**
`delivery/fills/cbc-run-pure-playbook.md:26`,
`delivery/installs/pure-seed.md:18, 32, 334`. Most read as
historical narration inside comments; `pure-seed.md:334` reads as
live prose. One grep pass decides, not a decision.

**F3 — run 3's last commit deleted five TODO items, and two have
no survivor.** The commit message describes a rewrite of `Now` and
says nothing about deletions; the `## Next (upcoming steps)` header
went, and its children went with it. Checked each:

- the branch-trial gate item — correctly deleted, it became PLAN's
  step-form default gate item
- SL-3's expired-hold mechanism and the `Location` deviation —
  survive in SL-1 §7, the lift condition weaker for it
- **Release: fail fast on a missing secret** — the decision
  survives in their devlog and in `cbc-bootstrap`; the lived
  reproduction is gone (boot at ~2.5s, 500/503 on first request,
  the lazy pool, and the two candidate fixes with what each costs
  the store-free context test)
- **Release: README names each refusal but not what it costs** —
  gone entirely. Filed 2026-09-20, deleted 2026-09-23. Their
  CHANGELOG already states such a cost plainly for SL-2 while
  README line 36 does not, so the inconsistency is live and no
  longer written down.

Theirs to decide, ours to tell. It matters to us for a second
reason: their TODO is the channel our hand-offs ride on, and a
section-header rewrite that takes its children could take one of
those just as easily. All four hand-offs are intact; the failure
mode is now demonstrated.

**F4 — the inbound direction has no procedure.** Outbound is
`delivery/installs/bundle-update.md`: seven numbered steps, shell
commands, an owner per step, four sections each dated to the firing
that taught it. Inbound is six paragraphs inside
`delivery/README.md`, a document whose job is to describe what a
run copies at birth. Same number of lived firings behind each —
three deliveries against three harvests. The verdict rules, which
are the inbound loop's output, are specified in the outbound
manual.

**F5 — the evidence we said we were watching for did not arrive.**
The held `infra-establish` hand-off watches for a second run
reaching the contract's facility gap, and reads SL-2 leaning on
that paragraph as evidence the first slice needed it. SL-2 does not
mention the facility at all. The item stays held; what changes is
that it has now been checked rather than left looking unexamined.

## What the run taught us that we had not thought of

**A tripwire never discharges a kill.** Our skill demanded a red
for every guarantee and said nothing about a test that cannot be
reddened — so such a test was either mislabelled as evidence or
deleted. The run hit it, and the red run is what told the two
apart, not a reading.

**Force can come from placement rather than wording.** Our
conventions get all of theirs from wording, and rely on a person
remembering to read. Worth keeping whatever we decide about shapes.

**One draft per unsettled shape, never per pile of queued work.**
Their `decide-first` draft covered three queued items; two had no
shape question, so the count was sayable for both and the draft was
covering work rather than settling anything.

## Decisions

Preliminary order. D1 gates three of the others, which is why it is
first and why the commit count for this whole reading is not
sayable until it settles.

- **D1 — do we become the collector?** Run 3 asks this repo to hold
  unexposed shapes from every project, stage them into a run's
  `temp/` with a note when that run reaches a gate ("I hold none" is
  a real delivery), and reconcile afterwards. Today our exchange
  fires when we initiate; this makes it fire on the receiver's
  calendar. It rides with a shipping rule — exposed shapes ship,
  unexposed ones never do — which constrains us immediately and
  could be taken on its own. **Gates D2, D3, and part of D4.**
  Standing recommendation: hold the role with a named trigger (a
  second run reaching a gate with a shape of its own), take the
  shipping rule now. A collector with one contributor is a folder,
  and writing the protocol from one project is what killed ADR-0021.
- **D2 — `cbc-slice` Stage 4 and the `artifact-kinds` shape entry:
  take or decline.** One decision, not two: the shape check is dead
  text for a project with no notion of a shape. Depends on D1.
- **D3 — does `shapes-lifecycle` become a convention?** It would be
  the container's first `.claude/rules/` artifact and the first
  shipped rule presuming a collector. Depends on D1.
- **D4 — does `agent-arrangement` §3 learn about `.claude/shapes/`?**
  A directory whose defining property is that nothing loads it.
  Separable; can be taken without D1.
- **D5 — `cbc-slice` Stage 3, the tripwire rule: take or decline.**
  Rests on nothing. Recommend taking it whole.
- **D6 — do the step form and default gate items fold into
  `cbc-run-pure-playbook`?** Ours. Their branch-per-step trial is
  still open beside it.
- **D7 — the inbound harvest manual: peer to `bundle-update.md` or
  a section of it, and where does it sit?** Recommend a peer.
  `installs/` may be the wrong parent — both files there put files
  into a run, and a harvest puts nothing anywhere.
- **D8 — the standing rule: a branch and a reading for work needing
  more than one commit plan.** On trial, in PLAN above the steps
  with its decision in `.claude/decisions.md`, which is how run 3
  introduced its own branch rule.

## The work

Preliminary order. Items marked **plan** are expected to need a
commit plan of their own; the rest are a commit or two.

- **W1 — fix `CLAUDE.md:25`.** Needs no decision. One commit.
- **W2 — grep pass for the remaining stale noun** (F2). May fold
  into W1 or may not, depending on what it finds.
- **W3 — the standing rule into PLAN and the decisions log.**
  Needs D8.
- **W4 — a `decide-first` draft on the collector**, which settles
  D1. One unsettled shape, not the pile below it.
- **W5 — take the tripwire rule into the master** (D5). **plan** —
  the skill, its workflow reference, and the records.
- **W6 — whatever D1 settles**: D2, D3, D4. **plan**, size unknown
  until D1.
- **W7 — write the inbound harvest manual** (D7), from the running
  of W4–W6 rather than from memory of the last three harvests.
  **plan**.
- **W8 — record the checked-through mark** at `9869798`. Lands
  wherever D7 puts it, so it follows W7.
- **W9 — one delivery to run 3**: verdicts on all four hand-offs,
  the three edits answered, and F3 told as a finding with the five
  lines quoted so they can restore what they want. Last, and one
  delivery rather than two — nothing over there is waiting on us.
  **plan**.
- **W10 — records catch up**: the ADRs each decision earns, the
  devlog, TODO.

## Notes

- Ten work items, at least four of them wanting a commit plan. By
  D8's test this is branch work.
- W9 is deliberately last. A delivery costs the receiver a take,
  and run 3 has three branches of its own queued before SL-3.
- Nothing here is staged into run 3's `temp/` yet. Its tree is
  clean as of `9869798`, so the 2026-09-20 mistake — staging while
  its agent was mid-work — is not in play, but the staging is the
  operator's step either way.
- This file is itself on trial. If it turns out to be TODO's "Now"
  written earlier, one firing will show it and we drop it.

## Why this file has this shape

Written down because it lives nowhere else. The shape was settled
in conversation on 2026-09-23, and W7 will be written from this
file rather than from that conversation.

**The branch is `reading-run-3-2026-09-23`**, cut from main at
`93b7f1a`. Named for the artifact, because the artifact is what
decided the branch exists. Recorded here because this repo has made
no merge commit in its history — every branch is fast-forwarded, so
nothing in main will say a branch existed or what it was called.

**The list is not a commit plan, and could not be.** That
convention rules it out twice over: it plans the commits and not
the change, so what is being changed is settled *before* it opens —
and half the list here is not settled. And it forbids status, where
this list must carry it, because settling one item reshapes or
deletes others.

**The kind is `plan`, by `artifact-kinds`' own test.** *Does it lie
if not kept current?* Yes. Narrowed from "one per project" to one
per undertaking, which that convention permits — contexts may
specialise, not contradict. Its top half is findings, which
describes; a hybrid, named by its dominant force.

**The reading comes before the branch, not after.** The branch test
is whether the work needs more than one commit plan, and only the
list can answer that. So the reading is written first, on main, and
the branch is cut from what it counts.

### What was rejected

- **TODO's "Now" section as the home.** It is the nearest fit and
  the real competitor: an ordered worklist for what is being done
  now, where the last two harvests went. Rejected because TODO
  accretes — completed entries stay as history, which is its job —
  and this list is edited down as it is worked. A record whose
  value is that nothing leaves it cannot hold a list whose value is
  that things do.
- **A branch per step, run 3's standing rule.** Rejected because
  their steps are gated: the gate closes, then the branch
  fast-forwards, so the branch is the unit the gate certifies. A
  reading has no gate. Taking their rule because we happened to be
  reading their repo is the wrong way for a convention to arrive.
- **A `.claude/rules/` file with a `paths:` list.** Rejected on
  mechanism: a rules file loads when a matching path is touched,
  and a reading begins with no file open. The trigger could never
  fire.
- **Making it a convention now.** Rejected as generalising from one
  firing — the thing that withdrew ADR-0021, and what run 3's own
  `shapes-lifecycle` §1 rules out. It goes in as a standing rule on
  trial (D8) and earns promotion or dies.

### What is deliberately not being done yet

The manual, an `installs/` file, or a convention. That is D7 and
W7, and it should be written from two firings. Noting the reasoning
is not promoting it.
