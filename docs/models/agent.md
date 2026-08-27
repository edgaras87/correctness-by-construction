<!-- Vendored copy — engineering-handbook models/agent.md @ 4fe8083
     (copied 2026-08-27, same commit as this repo's kit birth pin).
     Pinned: do not edit here — changes happen in the handbook and
     arrive as a fresh pinned copy. See ADR-0002. -->

# Agent Model

DRAFT (Step 14). Deliberately incomplete — a first structure to test,
not a finished description. Behavioural statements carry a status and a
refutation condition (§12).

A structured description of what an AI agent working inside a
repository *is*: its parts, the channels that carry text into it, and
what each channel can and cannot guarantee.

This is a **model**, not a convention (artifact-kinds: *could you
disagree with it and violate nothing?* — yes). It binds nothing. Its
job is to let conventions be written against something stated, instead
of each author reasoning from a private picture of "the agent".

Layer 1 — vendor-neutral. One tool's mechanisms are a **binding**
(§10), written separately.

---

## 1. Who this is about

An agent working in **a project that follows the handbook's
conventions**, where those conventions arrive as vendored copies at a
pinned version.

That is the case worth getting right: the conventions are written for
it, and it is the case nobody can watch. The handbook maintaining
itself is one instance of it, not the subject.

The practical question the model exists to answer: *given a convention
sitting in a project, how does it reach the agent that is supposed to
follow it?* — §8, §9, and ADR-0012.

## 2. Components

1. **The repo** — the only durable memory. Files, and their history.
2. **The channels** — how text reaches the agent (§4).
3. **The context window** — everything the agent knows now (§5).
4. **The write-back** — what the agent leaves in the repo (§6).
5. **The gate** — enforcement, which sits outside all of it (§7).

## 3. The shape

```
             ┌─────────── the repo ───────────┐
             │                                │
   ambient   │  entry file ──────────┐        │
   pulled    │  any other file ──────┤        │
   pushed    │  hook ────────────────┤        │
             └───────────────────────┼────────┘
                                     ▼
   told     ─────────────────► CONTEXT WINDOW ──► agent acts
   observed ─────────────────►       │                │
                                     │                ▼
                                     │        write-back to repo
                                     │                │
                            session ends ─────────────┘
                                     │
                       next session starts empty (§6)

   installed  ── files that shape the repo, never entering the window
   the gate   ── hooks, CI, review: blocks or allows, outside all of it
```

## 4. The channels

Five carry text into the context window. They differ in **when they
fire** and **what they guarantee** — and a rule's reliability is a
property of the channel it travels, not of how well the rule is
written. A sixth delivers nothing to the window at all.

### ambient

Entry files loaded at session start, before the first task.
- **Fires:** always.
- **Guarantees:** the text is present.
- **Does not guarantee:** that it is followed (§12 A1).
- **Costs:** paid every session, on every task, relevant or not. Grows
  without bound if used as a rulebook; each addition dilutes the rest.
- **Fidelity:** space is scarce here, so rules arrive compressed — and
  compression loses parts (§12 M1).
- **Suits:** orientation and routing. Where to look, what kind of repo
  this is, what must never happen — if it is short.

### pulled

The agent reads a file because it decided to.
- **Fires:** at the agent's initiative.
- **Guarantees:** full fidelity when it fires — the whole rule, not a
  summary of it.
- **Does not guarantee:** firing at all (§12 P1).
- **Costs:** nothing when not needed.
- **Suits:** depth. Full conventions, reference material, anything long
  or precise.

### pushed

Something outside the agent's choosing puts text in context at a
particular moment: a task type matches, an event occurs.
- **Fires:** on a condition, not on initiative.
- **Guarantees:** presence at the moment of need, without depending on
  the agent going to look.
- **Does not guarantee:** that the condition is right — it can fire
  when it should not, or fail silently (§12 U1).
- **Costs:** machinery. Something defines and maintains the condition.
- **Suits:** rules bound to an action. A commit format at commit time.

### told

A human says it in the session.
- **Fires:** when the human bothers.
- **Guarantees:** the highest attention of any channel.
- **Costs:** does not scale, does not persist, is not reproducible.
- **Suits:** nothing that should be a convention. **Repeated use of
  this channel is a diagnostic:** a convention is missing, or one
  exists in a channel that is not firing.

### observed

Results of commands the agent runs: file contents, search hits, test
output, diffs.
- **Fires:** when the agent runs something.
- **Guarantees:** ground truth about the repo's actual state.
- **Distinct property:** **the only channel that can contradict the
  others.** A document claims; a diff shows. Noticing that two copies
  of a rule disagree requires this channel — no instruction substitutes
  for a comparison actually being run (§12 O1).

### installed

Not a channel into the window. The convention arrives as **files** and
works by existing: `.gitignore`, `.editorconfig`, a directory layout, a
committed template.
- **Fires:** never. There is nothing to fire.
- **Guarantees:** the outcome, not the behaviour — the agent does not
  comply with `.gitignore`, it simply cannot see what git hides.
- **Costs:** only what applies at bootstrap can be delivered this way.
- **Suits:** anything expressible as repo state rather than as
  instruction. **This is the strongest delivery available**, and the
  only one immune to every claim in §12.
- **Self-enforcing:** the property that makes it strong. A rule is
  self-enforcing when acting on the artifact is what puts the rule in
  front of you — the rule for filling in `PLAN.md` sits inside
  `PLAN.md`, so it cannot be skipped without opening the file it
  governs. No trigger is needed because the act is the trigger. This
  is how a text convention can be installed at all (ADR-0004,
  ADR-0015): `.gitignore` is self-enforcing by mechanism; a stub with
  its rules in comments is self-enforcing by placement, and only
  while the comments stay in the file. It covers the act, not the
  decision to act: a record's format travels this way, its timing
  cannot (ADR-0018).

## 5. The context window

- **Finite.** Everything in it competes with everything else.
- **Undifferentiated.** Once text arrives, *its channel of origin is
  not marked.* A rule from the entry file and a rule from a file read
  mid-task are the same kind of object.

  Consequence: **no channel carries authority.** "The entry file
  overrides the convention" has no mechanism to run on — the agent sees
  two statements, not two ranks. Precedence must be resolved before
  text reaches the window, by not writing the rule twice.

- **Ordered, not prioritised.** Position is not rank.

## 6. Write-back and persistence

Only what is written into the repo survives the session. The context
window, the reasoning that filled it, and every decision not recorded
evaporate at session end.

Consequences:
- A record that assumes context from the session that produced it is
  unreadable later — including by the same agent (§12 S1).
- The next session starts from the repo alone. It is not a
  continuation; it is a reconstruction.

## 7. The gate

Enforcement is not in the text. A file cannot prevent anything. Only a
check outside the text — a hook, CI, a human review — turns "should"
into "cannot".

**No channel choice substitutes for a gate.** If a rule must never be
violated, ambient/pulled/pushed changes the odds; only a gate changes
the outcome (§12 G1).

## 8. Choosing a channel

The design decision a convention author makes, and until now made
implicitly. Recorded per convention (ADR-0012).

| The rule is… | Channel | Because |
|---|---|---|
| expressible as repo state | **installed** | outcome, not compliance |
| needed to orient, every session | **ambient** | always present; that cost is unavoidable anyway |
| long, precise, occasionally needed | **pulled** | fidelity matters more than presence |
| bound to a specific action | **pushed** | present at the moment, without initiative |
| must never be violated | + **gate** | §7 |
| stated by a human repeatedly | — | a convention is missing, or its channel is not firing |

A rule placed in two channels is not twice as reliable. It is one rule
with two texts that can disagree (§5).

## 9. Where each convention lands

Stated by each convention for itself: `delivery` in the frontmatter
of its `CONVENTION.md`, with the reasoning in a **Delivery** section
below (ADR-0012, ADR-0013). Read it there.

A worked table stood here until every convention carried its own
statement, at which point the two disagreed on two of five rows.
The table had been right when written and had no way to stay so —
one fact, two homes, and this was the one nothing edited.

## 10. Bindings (Layer 2)

Layer 1 names capabilities; a binding names the mechanisms in one tool.
Bindings are separate files, one per tool, so that writing a second one
is the test for tool-shaped assumptions hiding in Layer 1.

Sketch, Claude Code:

| Layer 1 | Claude Code mechanism |
|---|---|
| ambient | memory files — `CLAUDE.md`, `~/.claude/CLAUDE.md`, `@` imports; a skill's `name` and `description` |
| pulled | `Read`, `Grep`, `Glob`; a skill's body, once the agent invokes it |
| pushed | context-injecting hooks, slash commands, subagents |
| told | the prompt |
| observed | tool results |
| installed | files in the repo; the starter kit that puts them there |
| gate | blocking hooks (`PreToolUse`), CI |

Hooks appear twice: some inject context (pushed), others block (gate).
One mechanism, two roles — a binding has to say which.

Skills appear twice as well, and neither time under pushed. Claude
Code loads a skill's `name` and `description` at session start and
its body only when the agent invokes it: an ambient trigger over a
pulled body. The agent still decides, and pushed promises it does
not (§4). A skill is the closest this tool gets to pushed; a hook
closes the remainder (ADR-0015).

## 11. Out of scope

- **Project type.** Backend-ness does not change how context loads.
  Type-specific guidance is a playbook.
- **Model capability.** How capable, how current — changes per release.
  These are claims about the shape of the runtime, not its quality.
- **Tool mechanisms.** §10.

## 12. Claims

The structure above mixes mechanical facts (a session starts empty; a
file must be read to be present) with behavioural assumptions (presence
does not mean compliance). The second kind is stated here, each
attached to the component it constrains, each written so it can be
proven wrong.

`evidenced` = observed. `assumed` = asserted but never observed —
including assertions this repo has already acted on.

### On ambient

**A1 — Presence is not compliance.** A rule being in context does not
mean it is followed.
- `evidenced` — the commit-subject limit (≤50 chars) has been ambient
  in `AGENTS.md` since Step 6 and pulled in `commit-messages` since
  Step 5. 15 of the first 20 commits in this repo exceed it. Present,
  correct, unfollowed.
- **Open question it raises:** unenforced, or mis-set —
  `docs(handbook):` consumes 15 of the 50 characters before the verb.

**A2 — Instructions have a per-rule cost.** The longer the ambient set,
the lower compliance with any single rule in it.
- `assumed` · *Refuted by:* compliance staying flat as ambient grows.

### On pulled

**P1 — A pointer is not the file.** An agent can act on a rule's topic
without opening the file that states it.
- `assumed` · *Refuted by:* opening a linked `CONVENTION.md` unprompted,
  before doing the thing it governs.

**P2 — Placement decides whether a pointer fires.** A pointer at the
moment of need fires more reliably than the same pointer in a reading
list at session start.
- `assumed` — **this is the claim that decides router vs rulebook.**
- *Refuted by:* both placements performing the same.

### On pushed

**U1 — A trigger fails in both directions.** A condition can fire when
it should not (noise, which trains the reader to ignore it) and fail to
fire when it should (silence, indistinguishable from having no rule).
- `assumed` · *Refuted by:* a condition reliably exact in practice.

### On observed

**O1 — Divergence is invisible without a comparison.** Nothing causes
two disagreeing copies of a rule to be noticed unless something
compares them.
- `partially evidenced` — the three-place hygiene update (devlog k) was
  caught by hand, as ADR-0008 predicted. Not yet observed: a *missed*
  divergence.
- *Refuted by:* an agent flagging a stale copy unprompted.

### On the context window

**W1 — Conflict fails silently.** Faced with two conflicting rules, an
agent resolves one and proceeds rather than reporting the ambiguity.
- `assumed` · *Refuted by:* halting to ask which rule wins.
- The *precedence* half of this is no longer a claim: §5 makes it
  structural — channel of origin is not marked, so a stated precedence
  has nothing to run on.

### On persistence

**S1 — A record is only as good as its self-containment.** A record
assuming context from the session that wrote it is unreadable later,
including by the same agent.
- `assumed` · *Refuted by:* acting correctly on a terse old record
  without asking.

### On summaries

**M1 — A hand-written summary is lossy on arrival.** Summarising drops
parts of a rule immediately, before any drift.
- `evidenced` — `commit-messages/CONVENTION.md:11` states "≤50 chars,
  imperative, **no period**". `AGENTS.md` renders it as "imperative
  subject ≤50 chars, body explains why, footers link ADRs/issues". "No
  period" was gone on arrival.

**M2 — Derived text cannot drift, only go stale.** A generated summary
disagrees with its source only by being out of date, which
regeneration detects. A hand-written one can disagree while both files
look current.
- `evidenced` (definitional)

### On the gate

**G1 — Text does not enforce.** No file prevents a violation; only a
check outside the text can.
- `evidenced` — same measurement as A1. The rule existed in two
  channels for the whole life of the repo, no gate existed, and it was
  broken 15 times.

### Scorecard

| Status | Claims |
|---|---|
| evidenced | A1, M1, M2, G1 |
| partially evidenced | O1 |
| assumed | A2, P1, P2, U1, W1, S1 |

Six of eleven remain assumed. **P2** decides router versus rulebook;
the field test (Step 9) is what resolves it.

Note that **installed** carries no claims. It is the only delivery that
does not depend on an agent doing anything.
