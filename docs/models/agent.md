# Agent Model

A structured description of what an AI agent working inside a
repository *is*: its parts, the channels that carry text into it, and
what each channel can and cannot guarantee.

Deliberately incomplete: a structure to test, not a finished
description. Behavioural statements carry a status and a refutation
condition (§12, *Claims*).

This is an Idea Model: the top Canonical Description of its chain. It binds
what stands on it. When the two disagree, either side may be
the wrong one (`docs/models/idea-to-output.md` §3.3, *Settling a disagreement*). Its job is to
let conventions be written against something stated, instead of
each author reasoning from a private picture of "the agent".

Vendor-neutral: this Idea Model names capabilities, its Layer 1. The
mechanisms one tool gives them are a Tool Binding, its Layer 2
(§10, *The Tool Bindings*).

---

## 1. Who this is about

An agent working in **a project that follows the conventions it was
born with**: a Run Repo, pinned to the copies it took. How the repos relate is the Tiers Model's
(`docs/models/tiers.md` §2.3, *Run Repos*).

That is the case worth getting right: the conventions are written for
it, and it is the case nobody can watch. An agent in the repo that
delivers them meets the same channels all the same.

The practical question the Idea Model exists to answer: *given a convention
sitting in a project, how does it reach the agent that is supposed to follow it?* (§8, *Choosing a channel*; §9, *Where each
convention lands*).

## 2. The agent's components

1. **The repo** — the only durable memory. Files, and their history.
2. **The channels** — how text reaches the agent (§4, *The channels*).
3. **The context window** — everything the agent knows now (§5, *The context window*).
4. **The write-back** — what the agent leaves in the repo (§6, *Write-back and persistence*).
5. **The Enforcement Gate** — enforcement, which sits outside all of it (§7, *The Enforcement Gate*).

## 3. A drawing of the components

```
                     ┌─────────── the repo ───────────┐
                     │                                │
   Ambient Channel   │  Entry File ──────────┐        │
   Pulled Channel    │  any other file ──────┤        │
   Pushed Channel    │  hook ────────────────┤        │
                     └───────────────────────┼────────┘
                                             ▼
   Told Channel     ─────────────────► CONTEXT WINDOW ──► agent acts
   Observed Channel ─────────────────►       │                │
                                             │                ▼
                                             │        write-back to repo
                                             │                │
                                    session ends ─────────────┘
                                             │
                         next session starts empty
                         (§6, Write-back and persistence)

   Installed Channel  ── files that shape the repo, never entering the window
   Enforcement Gate   ── hooks, CI, review: blocks or allows, outside all of it
```

## 4. The channels

Five carry text into the context window. They differ in **when they
fire** and **what they guarantee**. A rule's reliability is a
property of the channel it travels, not of how well the rule is
written. A sixth delivers nothing to the window at all.

### 4.1 Ambient Channel

Entry Files loaded at session start, before the first task.
- **Fires:** always.
- **Guarantees:** the text is present.
- **Does not guarantee:** that it is followed (§12, *Claims* A1).
- **Costs:** paid every session, on every task, relevant or not. It
  grows without bound if used as a rulebook, a file holding the rules
  themselves. Each addition dilutes the rest.
- **Fidelity:** space is scarce here, so rules arrive compressed. And
  compression loses parts (§12, *Claims* M1). The Tool Binding can lose parts too:
  what the tool loads is not always the file on disk (§10, *The Tool Bindings*).
- **Ownership:** the project's text, or one operator's. An operator's
  own file, loaded only in their checkout:
  - fires and costs like the Entry File;
  - belongs to one person and one checkout;
  - stays out of the repo's history;
  - never has its words enter records.

  Using it again and again for a rule true in any project is the Told
  Channel's diagnostic (§4.4, *Told Channel*): the missing convention
  is worked around, not written.
- **Suits:** orientation and routing, kept short: where to look, what
  kind of repo this is, what must never happen.

### 4.2 Pulled Channel

The agent reads a file because it decided to.
- **Fires:** at the agent's initiative.
- **Guarantees:** full fidelity when it fires — the whole rule, not a
  summary of it.
- **Does not guarantee:** firing at all (§12, *Claims* P1).
- **Costs:** nothing when not needed.
- **Suits:** depth. Full conventions, reference material, anything long
  or precise.

### 4.3 Pushed Channel

Something outside the agent's choosing puts text in context at a
particular moment: a task type matches, an event occurs.
- **Fires:** on a condition, not on initiative.
- **Guarantees:** presence at the moment of need, without depending on
  the agent going to look.
- **Does not guarantee:** that the condition is right — it can fire
  when it should not, or fail silently (§12, *Claims* U1).
- **Costs:** machinery. Something defines and maintains the condition.
- **Suits:** rules bound to an action. A commit format at commit time.

### 4.4 Told Channel

A human says it in the session.
- **Fires:** when the human bothers.
- **Guarantees:** the highest attention of any channel.
- **Costs:** does not scale, does not persist, is not reproducible.
- **Suits:** nothing that should be a convention. **Repeated use of
  this channel is a diagnostic:** a convention is missing, or one
  exists in a channel that is not firing.

### 4.5 Observed Channel

Results of commands the agent runs: file contents, search hits, test
output, diffs.
- **Fires:** when the agent runs something.
- **Guarantees:** ground truth about the repo's actual state.
- **Distinct property:** **the only channel that can contradict the
  others.** A document claims; a diff shows. Noticing that two copies
  of a rule disagree requires this channel. No instruction substitutes
  for a comparison actually being run (§12, *Claims* O1).

### 4.6 Installed Channel

Not a channel into the window. The convention arrives as **files** and
works by existing: `.gitignore`, `.editorconfig`, a directory layout, a
committed template.
- **Fires:** never. There is nothing to fire.
- **Guarantees:** the outcome, not the behaviour. The agent does not
  comply with `.gitignore`. It cannot see what git hides.
- **Limits:** only what holds from a project's first commit can be
  delivered this way.
- **Suits:** anything expressible as repo state rather than as
  instruction. **This is the strongest delivery available**, and the only one immune to every claim (§12, *Claims*).
- **Self-enforcing:** the property that makes it strong. A rule is
  self-enforcing when acting on the file is what puts the rule in
  front of you. Here, for example, the rule for filling in `PLAN.md`
  sits inside `PLAN.md`, so it cannot be skipped without opening the
  file it governs. No trigger is needed because the act is the trigger. This is
  how a text convention can be installed at all. `.gitignore` is
  self-enforcing by mechanism. A Record Stub with its rules in
  comments is self-enforcing by placement, and only while the comments
  stay in the file. It covers the act, not the decision to act. A
  record's format can be delivered this way. Its timing cannot.

## 5. The context window

- **Finite.** Everything in it competes with everything else.
- **Undifferentiated within a role.** Once text arrives, *its channel
  of origin is not marked.* A rule from the Entry File and a rule from
  a file read mid-task are the same kind of object.

  Consequence: **no file carries authority over another.** "The Entry
  File overrides the convention" has no mechanism to run on — the
  agent sees two statements, not two ranks. Precedence between files
  must be resolved before text reaches the window, by not writing the
  rule twice.

- **Ranked by role above that.** The harness marks three things
  apart: its own wiring, the prompt, and what tools return. An agent
  weighs them in that order. A rule in the prompt beats the same
  rule's contrary in a file. A file's rule holds only until the prompt
  says otherwise (§12, *Claims* W2). Every file, through the Ambient
  Channel or the Pulled Channel, sits in the lowest role. So a rule
  that rests on a fact of the session cannot live in a file alone.
  Such a fact is, for example, that a reviewer is present, or a repo
  is out of bounds. The file cannot know the session, and the prompt
  outranks it.
  It goes through the Told Channel, every session, by design (§8, *Choosing a channel*).

- **Ordered, not prioritised.** Position is not rank.

## 6. Write-back and persistence

Only what is written into the repo survives the session: the context
window, the reasoning that filled it, and every decision not recorded
are gone at its end.

Consequences:
- A record that assumes context from the session that produced it is
  unreadable later — including by the same agent (§12, *Claims* S1).
- The next session starts from the repo alone. It is not a
  continuation; it is a reconstruction.

## 7. The Enforcement Gate

Enforcement is not in the text. A file cannot prevent anything. Only a
check outside the text turns "should" into "cannot": a hook, CI, or a
human review. The tool's permission prompt is a human review the tool
forces.

**No channel choice substitutes for an Enforcement Gate.** If a rule
must never be violated, the Ambient Channel, the Pulled Channel or the
Pushed Channel changes the odds; only an Enforcement Gate changes the outcome (§12, *Claims* G1).

## 8. Choosing a channel

The design decision a convention author makes, once for each
convention.

| The rule is… | Channel | Because |
|---|---|---|
| expressible as repo state | Installed Channel | outcome, not compliance |
| needed to orient, every session | Ambient Channel | always present; that cost is unavoidable anyway |
| long, precise, occasionally needed | Pulled Channel | fidelity matters more than presence |
| bound to a specific action | Pushed Channel | present at the moment, without initiative |
| must never be violated | + Enforcement Gate | §7, *The Enforcement Gate* |
| resting on a fact of this session | Told Channel, every session | a file cannot know the session, and the prompt outranks it (§5, *The context window*) |
| stated by a human repeatedly, and true of any project | — | a convention is missing, or its channel is not firing |

A rule placed in two channels is not twice as reliable. It is one rule
with two texts that can disagree (§5, *The context window*).

## 9. Where each convention lands

Each convention's Work Approaches show where it lands: an Agent Skill
for a rule bound to a moment, an Agent Rule for a rule bound to a
path or to every task, an Output Form for a rule carried in the files
a project is born with. The choice
rests on the table in §8 (§8, *Choosing a channel*). No field in a file
names a channel.

No table here: a list of each convention's channel would be a second
home for facts this Idea Model does not own.

## 10. The Tool Bindings

Tool Bindings are Layer 2. Layer 1 names capabilities. A Tool
Binding names the mechanisms one tool gives each of them: which file the Ambient Channel loads, what the
Pushed Channel carries, what an Enforcement Gate checks. It changes
with the tool's releases. So the repo that uses the tool writes it,
beside its arrangement. This Idea Model changes only when an idea
does. Two things every Tool Binding has to say, from what one tool
has shown:

- **One mechanism may serve two channels.** A hook that injects
  context is the Pushed Channel; one that blocks is an Enforcement
  Gate.
- **What the tool loads is not always the file on disk.** A tool may
  drop part of a file, a comment for one, before it reaches the
  window.

## 11. What the model leaves out

- **Project type.** Being a backend does not change how context loads.
  Type-specific guidance is a playbook.
- **Model capability.** How capable, how current — changes per release.
  These are claims about the shape of the runtime, not its quality.
- **Tool mechanisms.** (§10, *The Tool Bindings*)

## 12. Claims

The structure above mixes mechanical facts (a session starts empty; a
file must be read to be present) with behavioural assumptions (presence
does not mean compliance). The second kind is stated here, each
attached to the component it constrains, each written so it can be
proven wrong.

`evidenced` = observed. `assumed` = asserted but never observed —
including assertions already acted on. Each piece of evidence says
where it was seen: this repo's history, a CBC Run's, or the
handbook's. The handbook is the repo that held the working
arrangement before this one, now history (ADR-0038).

Evidence from outside is listed under its claim too, marked
`measured` for a controlled study with numbers, `reported` for a
first-hand or bug report. It leaves the status alone: a claim is
evidenced only when it was seen in this work.

### 12.1 Claims on the Ambient Channel

**A1 — Presence is not compliance.** A rule being in context does not
mean it is followed.
- `evidenced` — the commit-subject limit (≤50 chars) was in the
  handbook's Entry File, its Ambient Channel, from its Step 6, and in
  its commit-messages Agent Skill, its Pulled Channel, from its Step 5.
  15 of the handbook's first 20 commits exceed it. Present, correct,
  unfollowed.
- `evidenced` here too — 125 of this repo's 233 commits from
  2026-09-20 to 09-29 run over 50 characters, though the
  commit-messages Agent Skill is opened at every commit here. Seven of
  the eight revisions of commit plans of 2026-09-29 ran over too, the
  longest at 67. CBC Run 3's subjects crossed 50 at every Plan Step we
  read, at 52 to 56 (this repo's devlog, 2026-09-10 to 09-14).
- **Open question it raises:** is the limit only unenforced, or set
  wrong?
  `docs(handbook):` consumes 15 of the 50 characters before the verb.
  Here, for example, the commit-plan Agent Skill's own revision form,
  `docs(agent): revise commit plan — `, consumes 34 before saying
  what changed.

**A2 — Instructions have a per-rule cost.** The longer the Ambient
Channel's text, the lower compliance with any single rule in it.
- `assumed` · *Refuted by:* compliance staying flat as the Ambient
  Channel's text grows.
- `measured` elsewhere — the best models followed about 68% of 500
  instructions given at once, and favoured the earlier ones
  (Jaroslawicz et al., arXiv 2507.11538, 2025). The task was writing
  with keywords, not working from an Entry File.

### 12.2 Claims on the Pulled Channel

**P1 — A pointer is not the file.** An agent can act on a rule's topic
without opening the file that states it.
- `assumed` · *Refuted by:* opening a linked Agent Skill unprompted,
  before doing the thing it governs.
- `measured` elsewhere — an Agent Skill holding the docs an eval needed was
  never invoked in 56% of cases (Vercel, 2026-01-27). With no hook,
  an Agent Skill fired on 50–55% of 22 prompts (Spence, 2026-02-08). Both
  are small, and each has one source.

**P2 — Placement decides whether a pointer fires.** A pointer at the
moment of need fires more reliably than the same pointer in a reading
list at session start.
- `assumed` — **this is the claim that decides whether the Entry File
  is a router, pointing at each rule at its moment, or a rulebook,
  holding the rules.**
- *Refuted by:* both placements performing the same. The test that
  can run: a CBC Run Reading of a CBC Run that holds one rule both ways, pointed
  at from an Agent Skill at its moment and from the Entry File alone.
- `measured` elsewhere, on a nearby question, not P2 itself: the
  same Vercel evals passed 100% with an index of the docs in the
  Entry File, 79% with an Agent Skill the prompt named, and 53% with
  an Agent Skill alone. An Agent Skill's trigger reaches through the
  Ambient Channel too, its name and description loaded at session
  start, so this compares two pointers read then. Both numbers come
  from one framework, tested by its vendor's own suite. Khatri (arXiv 2607.27250, 2026) found no
  difference between a guide always loaded and topic files read by
  choice, in a study too small to see less than 30 percentage
  points.

### 12.3 Claims on the Pushed Channel

**U1 — A trigger fails in both directions.** A condition can fire when
it should not (noise, which trains the reader to ignore it) and fail to
fire when it should (silence, indistinguishable from having no rule).
- `assumed` · *Refuted by:* a condition reliably exact in practice.

### 12.4 Claims on the Observed Channel

**O1 — Divergence is invisible without a comparison.** Nothing causes
two disagreeing copies of a rule to be noticed unless something
compares them.
- `evidenced` — here, three divergences were missed until a
  comparison was run for another reason:
  - ADR-0024 decision 4 said `fills/` retires, and it still held one
    file, added 2026-09-18; found on 2026-09-29 while PLAN's Step 8
    was being shrunk.
  - PLAN's decision index went stale twice, found each time while
    something else was being written.
  - The project-recording manual said the Concept Deliverer kept its
    records "under the same stubs" after ADR-0041 had split its PLAN
    from the Record Stub; found at the reviewer's question.

  Earlier, a hygiene change the handbook needed in three places was
  caught by hand (the handbook's devlog, entry k).
- *Refuted by:* an agent flagging a stale copy unprompted.

### 12.5 Claims on the context window

**W1 — Conflict fails silently.** Faced with two conflicting rules, an
agent resolves one and proceeds rather than reporting the ambiguity.
- `assumed` · *Refuted by:* halting to ask which rule wins.
- The *precedence* half of this is no longer a claim between files:
  the context window makes it structural (§5, *The context window*).
  Channel of origin is not marked, so a stated precedence has nothing
  to run on. Between roles it is W2.

**W2 — Roles rank.** Text in the harness's own wiring outranks the
prompt. The prompt outranks anything a tool returned. So a file's rule
loses to a contrary rule in the prompt, and a rule given through the
Told Channel exists only in the session it was told to.
- `evidenced` · three CBC Runs of the Pure Seed, reported 2026-09-10:
  - a stop the change-plans Agent Skill of the time asked for,
    skipped on an instruction the prompt never gave;
  - a checkout opened because the prompt's "stay inside this
    repository" had not fired yet, while the CBC Run's own procedure
    named a checkout on disk. *Refuted by:* an agent holding a file's rule against a prompt
  that contradicts it.

### 12.6 Claims on persistence

**S1 — A record is only as good as its self-containment.** A record
assuming context from the session that wrote it is unreadable later,
including by the same agent.
- `assumed` · *Refuted by:* acting correctly on a terse old record
  without asking.

### 12.7 Claims on summaries

**M1 — A hand-written summary is lossy on arrival.** Summarising drops
parts of a rule immediately, before any drift.
- `evidenced` — the commit-messages manual states "≤50 chars, imperative, **no
  period**". The handbook's Entry File of the time rendered it as
  "imperative subject ≤50 chars, body explains why, footers link
  ADRs/issues". "No period" was gone on arrival.

**M2 — Derived text cannot drift, only go stale.** A generated summary
disagrees with its source only by being out of date, which
regeneration detects. A hand-written one can disagree while both files
look current.
- `evidenced` (definitional)

### 12.8 Claims on the Enforcement Gate

**G1 — Text does not enforce.** No file prevents a violation; only a
check outside the text can.
- `evidenced` — same measurement as A1. The rule existed in two
  channels for the whole life of the handbook. No Enforcement Gate
  existed. It was broken 15 times. Here too: nothing gates a subject's
  length, and A1's count is 125 of 233.
- The tool's documentation says the same: an instruction in
  `CLAUDE.md` or an Agent Skill "is a request, not a guarantee", and
  guardrails go in hooks (checked 2026-10-24).

### 12.9 The claims' scorecard

| Status | Claims |
|---|---|
| evidenced | A1, M1, M2, G1, W2, O1 |
| assumed | A2, P1, P2, U1, W1, S1 |

Six of twelve remain assumed. **P2** decides router versus rulebook,
and a CBC Run Reading is what can resolve it.

The Installed Channel carries no claims. It is the only delivery that
does not depend on an agent doing anything.
