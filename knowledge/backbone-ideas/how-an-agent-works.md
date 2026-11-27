# How an agent works

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules: the Agent Model, docs/models/agent.md, deleted on 2026-11-27, its last state in git at 703ff7ca: its opening; §2 to §8; §10's two things every Tool Binding must say; §11; §12's claims, their status and the evidence from outside.
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says how a rule written in a repo reaches the agent meant to follow it: the agent's parts, the channels that carry text into it, and what each channel can and cannot guarantee. It names no Problem Domain: each Problem Domain Idea adapted from it says how its own repos meet it.

It names capabilities, never one tool's mechanisms; those are a Tool Binding's (§8). It is a structure to test, not a finished description: each statement about how an agent behaves is a claim, with a status and what would refute it (§10).

## 1. Its Defined Terms

- **Ambient Channel:** text that reaches the agent at session start, before the first task: the Entry File and what it loads.
- **Enforcement Gate:** a check outside the text that turns "should" into "cannot": a hook, CI, a human review.
- **Entry File:** the file the tool loads at session start, before the first task.
- **Installed Channel:** files that work by existing, such as `.gitignore`, and deliver nothing to the context window.
- **Observed Channel:** the results of commands the agent runs: file contents, search hits, test output, diffs.
- **Pulled Channel:** a file the agent reads because it decided to.
- **Pushed Channel:** text put in the agent's context at a moment it did not choose: a task type matches, an event occurs.
- **Told Channel:** what a human says in the session.
- **Tool Binding:** the mechanisms one tool gives the channels and the Enforcement Gate, written by the repo that uses the tool.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The agent's parts

1. **The repo:** the only durable memory. Files, and their history.
2. **The channels:** how text reaches the agent (§3).
3. **The context window:** everything the agent knows now (§4).
4. **The write-back:** what the agent leaves in the repo (§5).
5. **The Enforcement Gate:** enforcement, which sits outside all of it (§6).

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
                         (§5, Write-back)

   Installed Channel  ── files that shape the repo, never entering the window
   Enforcement Gate   ── hooks, CI, review: blocks or allows, outside all of it
```

## 3. The channels

Five channels carry text into the context window. They differ in when they fire and what they guarantee. A rule's reliability is a property of the channel it travels, not of how well the rule is written. A sixth, the Installed Channel, delivers nothing to the window at all.

### 3.1 The Ambient Channel

Entry Files loaded at session start, before the first task.

- **Fires:** always.
- **Guarantees:** the text is present.
- **Does not guarantee:** that it is followed (§10, A1).
- **Costs:** paid every session, on every task, relevant or not. It grows without bound if it is used as a rulebook, a file holding the rules themselves. Each addition dilutes the rest.
- **Fidelity:** space is scarce here, so rules arrive compressed, and compression loses parts (§10, M1). The tool can lose parts too: what it loads is not always the file on disk (§8).
- **Ownership:** the project's text, or one operator's. An operator's own file, loaded only in their checkout:
  - fires and costs like the Entry File;
  - belongs to one person and one checkout;
  - stays out of the repo's history;
  - never has its words enter records.

  Using it again and again for a rule true in any project is the Told Channel's diagnostic (§3.4): the missing convention is worked around, not written.
- **Suits:** orientation and routing, kept short: where to look, what kind of repo this is, what must never happen.

### 3.2 The Pulled Channel

The agent reads a file because it decided to.

- **Fires:** at the agent's initiative.
- **Guarantees:** full fidelity when it fires: the whole rule, not a summary of it.
- **Does not guarantee:** firing at all (§10, P1).
- **Costs:** nothing when not needed.
- **Suits:** depth. Full conventions, reference material, anything long or precise.

### 3.3 The Pushed Channel

Something outside the agent's choosing puts text in context at a particular moment: a task type matches, an event occurs.

- **Fires:** on a condition, not on initiative.
- **Guarantees:** presence at the moment of need, without depending on the agent going to look.
- **Does not guarantee:** that the condition is right. It can fire when it should not, or fail silently (§10, U1).
- **Costs:** machinery. Something defines and maintains the condition.
- **Suits:** rules bound to an action. A commit format at commit time.

### 3.4 The Told Channel

A human says it in the session.

- **Fires:** when the human bothers.
- **Guarantees:** the highest attention of any channel.
- **Costs:** it does not scale, does not persist, and is not reproducible.
- **Suits:** nothing that should be a convention. Repeated use of this channel is a diagnostic: a convention is missing, or one exists in a channel that is not firing.

### 3.5 The Observed Channel

Results of commands the agent runs: file contents, search hits, test output, diffs.

- **Fires:** when the agent runs something.
- **Guarantees:** ground truth about the repo's actual state.
- **Distinct property:** it is the only channel that can contradict the others. A document claims; a diff shows. Noticing that two copies of a rule disagree needs this channel. No instruction stands in for a comparison actually run (§10, O1).

### 3.6 The Installed Channel

Not a channel into the window. The convention arrives as files and works by existing: `.gitignore`, `.editorconfig`, a directory layout, a committed template.

- **Fires:** never. There is nothing to fire.
- **Guarantees:** the outcome, not the behaviour. The agent does not comply with `.gitignore`. It cannot see what git hides.
- **Limits:** only what holds from a project's first commit can be delivered this way.
- **Suits:** anything expressible as repo state rather than as instruction. It is the strongest delivery there is, and the only one no claim touches (§10).
- **Self-enforcing:** the property that makes it strong. A rule is self-enforcing when acting on the file is what puts the rule in front of you. A record whose form sits in its own header is one (`knowledge/backbone-ideas/records.md` §13, *Where a record's rules sit*): the form cannot be skipped without opening the file it governs. No trigger is needed, because the act is the trigger. This is how a text convention can be installed at all. `.gitignore` is self-enforcing by mechanism. A record's header is self-enforcing by placement, and only while the header stays in the file. It covers the act, not the decision to act. A record's format can be delivered this way. Its timing cannot.

## 4. The context window

### 4.1 Finite

The context window is finite. Everything in it competes with everything else.

### 4.2 Undifferentiated within a role

Once text arrives, its channel of origin is not marked. A rule from the Entry File and a rule from a file read mid-task are the same kind of object.

So no file carries authority over another. "The Entry File overrides the convention" has no mechanism to run on: the agent sees two statements, not two ranks. Precedence between files must be settled before text reaches the window, by not writing the rule twice.

### 4.3 Ranked by role above that

The harness marks three things apart: its own wiring, the prompt, and what tools return. An agent weighs them in that order. A rule in the prompt beats the same rule's contrary in a file. A file's rule holds only until the prompt says otherwise (§10, W2). Every file, through the Ambient Channel or the Pulled Channel, sits in the lowest role.

So a rule that rests on a fact of the session cannot live in a file alone. Such a fact is, for example, that a reviewer is present, or that a repo is out of bounds. The file cannot know the session, and the prompt outranks it. The rule goes through the Told Channel, every session, by design (§7).

### 4.4 Order without priority

The window is ordered, not prioritised. Position is not rank.

## 5. Write-back

Only what is written into the repo survives the session. The context window, the reasoning that filled it, and every decision not recorded are gone at its end.

- A record that assumes context from the session that produced it is unreadable later, by the same agent too (§10, S1).
- The next session starts from the repo alone. It is not a continuation. It is a reconstruction.

## 6. The Enforcement Gate

Enforcement is not in the text. A file cannot prevent anything. Only a check outside the text turns "should" into "cannot": a hook, CI, or a human review. A tool's permission prompt is a human review the tool forces.

No channel choice stands in for an Enforcement Gate. For a rule that must never be broken, the Ambient Channel, the Pulled Channel or the Pushed Channel changes the odds; only an Enforcement Gate changes the outcome (§10, G1).

## 7. Choosing a channel

Whoever writes a convention makes this choice once for each of its rules.

| The rule is… | Channel | Because |
|---|---|---|
| expressible as repo state | Installed Channel | outcome, not compliance |
| needed to orient, every session | Ambient Channel | always present; that cost is unavoidable anyway |
| long, precise, occasionally needed | Pulled Channel | fidelity matters more than presence |
| bound to a specific action | Pushed Channel | present at the moment, without initiative |
| one that must never be broken | + Enforcement Gate | §6 |
| resting on a fact of this session | Told Channel, every session | a file cannot know the session, and the prompt outranks it (§4.3) |
| stated by a human repeatedly, and true of any project | none | a convention is missing, or its channel is not firing |

A rule placed in two channels is not twice as reliable. It is one rule with two texts that can disagree (§4.2).

**Rules:**

- Each rule travels one channel, chosen by the table.
- A rule that must never be broken also has an Enforcement Gate.
- A rule resting on a fact of the session is told, every session.

## 8. The Tool Bindings

This document names capabilities. A Tool Binding names the mechanisms one tool gives each of them: which file the Ambient Channel loads, what the Pushed Channel carries, what an Enforcement Gate checks. It changes with the tool's releases, so the repo that uses the tool writes it. This document changes only when an idea does.

**Rules:** every Tool Binding says these two things, learned from what one tool has shown:

- One mechanism may serve a channel and a gate. A hook that injects context is the Pushed Channel; one that blocks is an Enforcement Gate.
- What the tool loads is not always the file on disk. A tool may drop part of a file, a comment for one, before it reaches the window.

## 9. What it leaves out

- **The kind of project.** Being a backend does not change how context loads. What one kind of project needs is its Problem Domain Idea's.
- **The model's capability.** How capable, how current: it changes with each release. These are claims about the shape of the runtime, not its quality.
- **The tool's mechanisms:** a Tool Binding's (§8).

## 10. Claims

The structure above mixes mechanical facts, such as that a session starts empty and a file must be read to be present, with assumptions about behaviour, such as that presence does not mean compliance. The second kind is stated here, each claim attached to the part it constrains, each written so it can be proven wrong.

A claim's status is one of two:

- `evidenced`: observed in a Problem Domain's work, or true by definition, marked `(definitional)`;
- `assumed`: asserted but never observed, assertions already acted on included.

Each Problem Domain Idea lists what its own work showed, under the claim's label. Evidence from outside the work is listed here, under its claim, marked `measured` for a controlled study with numbers, `reported` for a first-hand or bug report. It leaves the status alone: a claim is evidenced only when it was seen in the work.

### 10.1 On the Ambient Channel

**A1. Presence is not compliance.** A rule being in context does not mean it is followed.
- `evidenced`.

**A2. Instructions have a cost per rule.** The longer the Ambient Channel's text, the lower compliance with any single rule in it.
- `assumed` · *Refuted by:* compliance staying flat as the Ambient Channel's text grows.
- `measured` elsewhere: the best models followed about 68% of 500 instructions given at once, and favoured the earlier ones (Jaroslawicz et al., arXiv 2507.11538, 2025). The task was writing with keywords, not working from an Entry File.

### 10.2 On the Pulled Channel

**P1. A pointer is not the file.** An agent can act on a rule's topic without opening the file that states it.
- `assumed` · *Refuted by:* opening a linked file of instructions unprompted, before doing the thing it governs.
- `measured` elsewhere: a skill, a file of instructions the tool loads when a task matches, held the docs an eval needed and was never invoked in 56% of cases (Vercel, 2026-01-27). With no hook, a skill fired on 50–55% of 22 prompts (Spence, 2026-02-08). Both are small, and each has one source.

**P2. Placement decides whether a pointer fires.** A pointer at the moment of need fires more reliably than the same pointer in a reading list at session start.
- `assumed`. This is the claim that decides whether the Entry File is a router, pointing at each rule at its moment, or a rulebook, holding the rules.
- *Refuted by:* both placements performing the same.
- `measured` elsewhere, on a nearby question, not P2 itself: the same Vercel evals passed 100% with an index of the docs in the Entry File, 79% with a skill the prompt named, and 53% with a skill alone. A skill's trigger reaches through the Ambient Channel too, its name and description loaded at session start, so this compares two pointers read then. Both numbers come from one framework, tested by its vendor's own suite. Khatri (arXiv 2607.27250, 2026) found no difference between a guide always loaded and topic files read by choice, in a study too small to see less than 30 percentage points.

### 10.3 On the Pushed Channel

**U1. A trigger fails in both directions.** A condition can fire when it should not: noise, which trains the reader to ignore it. It can fail to fire when it should: silence, which looks the same as having no rule.
- `assumed` · *Refuted by:* a condition reliably exact in practice.

### 10.4 On the Observed Channel

**O1. Divergence is invisible without a comparison.** Nothing causes two disagreeing copies of a rule to be noticed unless something compares them.
- `evidenced` · *Refuted by:* an agent flagging a stale copy unprompted.

### 10.5 On the context window

**W1. Conflict fails silently.** Faced with two conflicting rules, an agent settles on one and proceeds, rather than reporting the ambiguity.
- `assumed` · *Refuted by:* halting to ask which rule wins.
- The precedence half of this is no longer a claim between files: the context window makes it structural (§4.2). The channel of origin is not marked, so a stated precedence has nothing to run on. Between roles it is W2.

**W2. Roles rank.** Text in the harness's own wiring outranks the prompt. The prompt outranks anything a tool returned. So a file's rule loses to a contrary rule in the prompt, and a rule given through the Told Channel exists only in the session it was told in.
- `evidenced` · *Refuted by:* an agent holding a file's rule against a prompt that contradicts it.

### 10.6 On write-back

**S1. A record is only as good as its self-containment.** A record assuming context from the session that wrote it is unreadable later, by the same agent too.
- `assumed` · *Refuted by:* acting correctly on a terse old record without asking.

### 10.7 On summaries

**M1. A hand-written summary is lossy on arrival.** Summarising drops parts of a rule at once, before any drift.
- `evidenced`.

**M2. Derived text cannot drift, only go stale.** A generated summary disagrees with its source only by being out of date, which regenerating it detects. A hand-written one can disagree while both files look current.
- `evidenced` (definitional).

### 10.8 On the Enforcement Gate

**G1. Text does not enforce.** No file prevents a violation; only a check outside the text can.
- `evidenced`.
- `reported` elsewhere: one agent tool's documentation says an instruction in its Entry File or its skills "is a request, not a guarantee", and that guardrails go in hooks (checked 2026-10-24).

### 10.9 The scorecard

| Status | claims |
|---|---|
| evidenced | A1, M1, M2, G1, W2, O1 |
| assumed | A2, P1, P2, U1, W1, S1 |

Six of twelve remain assumed. P2 decides router against rulebook.

The Installed Channel carries no claims. It is the only delivery that does not depend on an agent doing anything.

## 11. Open questions

1. **What one piece of agent work is:** what the agent does, when, where and how. No text holds it yet. It is written when a second text needs it, here or as a Backbone Idea of its own if a second Backbone Idea uses it (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.1, *The Backbone Idea layer*).
