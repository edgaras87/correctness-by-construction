# Shapes

**What a kind of output looks like, in whichever repository makes
it — its form, never its content — written from work that exists,
and held where its place decides its force.**

## What it is for

So that what a kind of output looks like is written down once, from
work that exists, and held where its place decides whether it
binds — instead of each output re-deriving the form, or a template
being filled in. The failure is lived: run 3 made a thing this
repo's vocabulary had no word for, and it was called a template, a
specification, a convention and trial evidence before it got its
own (§2; CBC ADR-0035, 2026-09-23). Made a convention, with this
page as its manual, on 2026-09-27 (CBC ADR-0037): the rule binds,
and this page is why the rule is the shape it is, so that "why is
this a directory and not a rules file?" has an answer that is not
archaeology.

## What this is made usable as

- **`delivery/container/.claude/rules/shapes-lifecycle.md` — the
  rule, shipped**, held at `.claude/rules/shapes-lifecycle.md` and
  loading when a file under `.claude/shapes/` is touched. §1 to §3
  and §5, from the run's seat, with the definition repeated because
  a run cannot open this page.
- **The deliverer's shapes — instances, not copies**: rules under
  `.claude/rules/` with a Governs line,
  `.claude/rules/exchange-reading.md` and
  `.claude/rules/convention-manual.md` today. They hold no copy of
  the shipped rule, which has nothing at the deliverer to load on.
- **`delivery/README.md` — a pointer**: two sentences on placement,
  and §4 for the rest.

What derives from this page is that list. A change here walks it;
a change forced in one of them is checked back against this page.

*Does the name hold? Every section is about a shape — what one is,
where it sits, who moves it, what a difference with one means. It
held, 2026-09-27.*

## The seats

### The run's seat

A run holds the rule, and keeps shapes both ways: exposed under
`.claude/rules/`, loading while the work is written, and unexposed
under `.claude/shapes/`, opened at a gate. It meets a staged shape
at a step's close (§5), and what the gate reads becomes its own
shape. It offers what it arrived at by keeping it and pointing at
it from its backlog.

### The deliverer's seat

The deliverer makes outputs too — a reading is one — but it has no
steps and no gates. So of §3 it runs the exposed case only: a
shape at the deliverer is a rule under `.claude/rules/` with its
own `paths:`, marked as a shape by its Governs line, loading while
the file it governs is written. There is no `.claude/shapes/`
here, nothing is staged to the deliverer, and the rule's §4 — what
a gate does with what arrives in `temp/` — has no moment to fire
on. The reviewer moves a shape, as the rule says, and here that
means only writing one or withdrawing it.

Unexposed stock, when the deliverer holds any, is held apart from
the groups and names its group (§4); today it holds none, and no
directory is made ahead of a first occupant.

## 1. What a shape is

A **shape** says what a kind of output looks like: its form, never
its content. *Project*, below, is the master's word: whichever
repository makes the output — a run, or the deliverer.

The two halves matter equally. *Form* is what recurs — which parts a
record has, what each is for, what a worked example must contain.
*Never content* is what stops a shape check turning into a review of
the work: a shape can say a guarantee needs an example with real
numbers, and cannot say which numbers, or whether the guarantee is
any good.

*Found twice on 2026-09-26. A shape says what an output looks like
while it exists; when the output opens, extends and closes is the
owning convention's, and a shape that restates it is a copy of that
convention, and a copy that repeats is what drifts. The reading's
shape here restated the reading's lifecycle in its first section and
lost the sentences rather than gaining a clause; run 3's
`slice-record.md` opens with a section on how it is used that says
the same thing from its side. The rule now says it in one sentence.*

A shape is written from work that exists. Two ways one is born, and
neither ranks above the other: **it recurred**, so a pair is the
evidence and what they share is the shape; or **it was judged worth
keeping**, so one piece was rebuilt until it read well and someone
decided that should hold beyond here. What is ruled out is a shape
designed in advance from an idea of how work should go — everything
measured against it afterwards would be measuring the guess.

## 2. What a shape is not

The vocabulary already had four near neighbours, and a shape was
called each of them at some point before it got its own word. The
differences are the reason the entry exists.

- **Not a template.** A template's content is holes awaiting
  specifics, and you fill it in. A shape is read *against* finished
  work. Filling a shape in is the failure mode it warns about — the
  material that does not fit gets hidden as a completed form.
- **Not a specification.** A test can verify conformance to a
  specification. Nothing can test that a passage reads well, and a
  difference from a shape is a question rather than a failure.
- **Not a convention.** Deviating from a convention owes an
  explanation. A shape *wants* divergence: that is how it learns,
  and a difference may end with the shape changing rather than the
  output.
- **Not trial evidence.** This is the one that will be got wrong,
  because both are withheld and look alike. Their blindness runs
  opposite ways. Trial evidence is withheld **in order to stay**
  undelivered — a derivation that has seen it measures imitation
  instead of independence, so showing it destroys the measurement.
  A shape is withheld **only until a gate**, after which being in
  front of the next writer is the entire point.

## 3. Exposure, and why the place is the mechanism

A shape is **exposed** or **unexposed**, and the axis is not how
settled it is. Both go on changing. The axis is whether the shape is
in front of whoever does the work.

| | Where | What happens |
|---|---|---|
| **Unexposed** | `.claude/shapes/` | nothing loads it; it is opened at a gate |
| **Exposed** | `.claude/rules/`, with `paths:` | loads on its `paths:` (`docs/conventions/agent-arrangement/` §3.2) |

The directory is not a filing decision. It *is* the force: the same
file binds in one place and merely describes in the other, and
nothing else in the arrangement works that way: a shape is the one
thing here whose force is decided by where it sits rather than
fixed.

Unexposed is chosen while it still matters what the work produces
*without* the shape — most of all for the first output of a kind,
which is the only one nothing has influenced yet. Exposed is chosen
when conformance is what is wanted, and keeping the shape out of
sight would only make the next output re-derive it badly.

**The reviewer moves a shape, in both directions, and no count
does.** Exposing one and withdrawing it again are judgements. A
count can only prompt the question — a shape that has taken nothing
up across several closes has probably stopped teaching, one that
keeps changing probably still is — and the shape's own dated lines
are what the question is asked against. Changing an exposed shape
does not withdraw it; it returns to `.claude/shapes/` only when
someone decides the question is open again.

## 4. Where a shape lives, between repositories

Stated here once; `delivery/README.md` points here. Inside a
project, §3. Between repositories, a shape follows the
group of the thing it shapes — the same rule by which a skill
belongs to exactly one group and travels whole. A slice record's
shape is `method/`; a Spring harness file's is `spring-postgres/`; a
devlog entry's or a commit plan's is `container/`. A run on another
stack receives the first and never the second, and that falls out of
the groups rather than being enforced on top of them.

Only an exposed shape travels that way, as a pinned copy. An
unexposed one is in no birth copy at all — it would spend the only
independence there is — so it is held apart, names its group, and
reaches a project as a delivery staged at a gate.

**A project fetches nothing** (`docs/conventions/exchange/` §1):
what arrives, arrives because a person asked for it and staged it.
So the gate's act is local and always the same: look in `temp/`.
And what it finds does not stay a delivery — after the gate has
read it, the result **becomes that
project's own shape**, whether it came back unchanged, changed by
what the project found, or merged with what was already there. The
staging leaves; the shape stays, with dated lines saying what
arrived, what was taken and what was refused.

**Why kept rather than deleted.** Deleting would only hide what has
already been read. Keeping it makes the next gate cheap and the
reconciliation possible: the deliverer reads the project's version
and its dated lines against what it sent, and decides whether to
take the change or leave its own standing.

**Staleness, honestly.** A kept copy is a snapshot, current only as
of the delivery it came from, and nothing in a project can tell
when the deliverer's has moved on. A fresh delivery is the only
refresh, and asking for one is a person's act on this side, not the
project's.

**A shape is written in two separable layers, and only one of them
travels well.** The skeleton and what it encodes are general by
construction: they say *a worked example with real numbers from this
system*, not which numbers. The illustrations filling the
placeholders are the project's, and are marked as such. A reader
takes the first and leaves the second, and nothing has to be
rewritten at the hand-off to make that possible. This is why the
rule asks a project to mark its illustrations apart.

*Intended: staging a shape for a gate is a third act of the
exchange, beside read and deliver, and not a delivery. It reads only
which step the run stands at; it moves neither the pin nor the
read-through; its note is one line naming the shape and the step;
and what it stages becomes the project's own after the gate reads it,
never a pinned copy — so `delivered-copies.md`, which loads on
`temp/` and says to take what is there whole, must not apply to it.
No unexposed shape exists on either side, so nothing fires wrongly
today. Its skill, and the copies rule's exclusion, are written from
the first staging, not before (CBC ADR-0037 decision 5).*

**Birth and delivery, drawn.** Where a shape of each kind sits at
the deliverer, and the two different moments at which each reaches
a run. Every arrow that crosses is carried by a person.

*This page's pictures illustrate its prose and never carry a fact
alone. Measured 2026-09-27 and found false: five claims lived only
in a chart — who moves a shape, that a project fetches nothing,
that a difference is proposed and never corrected, what a tick
records, and that a delivery becomes the project's own shape. The
prose grew to cover them; read where Mermaid does not render, this
page loses the pictures and no facts.*

```mermaid
flowchart LR
  subgraph HERE["the deliverer"]
    direction TB
    EX["an exposed shape<br/>sits in the group of<br/>the thing it shapes"]
    UN["unexposed stock<br/>held apart, naming its group<br/>(none held yet)"]
  end

  subgraph RUN["a run repo"]
    direction TB
    MADE["what a step made"]
    TMP["temp/<br/>staged, never fetched"]
    SHP[".claude/shapes/<br/>nothing loads it"]
    RUL[".claude/rules/<br/>loads on its paths:"]
  end

  EX -->|"an operator copies it,<br/>at a birth or an update"| RUL
  UN -->|"an operator stages it,<br/>for one step's gate"| TMP
  TMP -->|"the gate opens it"| SHP
  MADE -->|"read against it, at the close"| SHP
  SHP -->|"the reviewer exposes"| RUL
  RUL -->|"the reviewer withdraws"| SHP

  SHP -.->|"read at a harvest: what it kept,<br/>and what its dated lines say"| UN
  RUL -.->|"read at a harvest: the copy<br/>against the pin it was sent at"| EX
```

**The dashed lines back are a reading, and the difference in the
line is the point.** The traffic model — nothing sent upward,
nothing fetched, the deliverer reading a run and never the reverse
— is `docs/conventions/exchange/` §1 and §6. What is this
convention's is where the reading looks for shapes: at
`.claude/shapes/` for what the project kept and what its dated
lines say it refused, when a backlog line of the run's offers it;
and at `.claude/rules/` for the copy against the pin it was sent
at, at every reading. A solid arrow in one direction and a dashed
one in the other is the part of the picture that states the
asymmetry rather than captioning it.

What travels upward is a **finding**, never a proposal: one project
saying what it arrived at — and it travels by being *read*, not by
being sent. A project offers by keeping its shape where its own
records are and pointing at it from its backlog, and the deliverer
reads it at the next reading (`docs/conventions/exchange/` §6).
What must not travel is a status, not a wording — a shape handed
down as a standard is inherited rather than
derived, and the next project's own answer is lost before it is
written. The protection is in how a shape moves, not in how vaguely
it is phrased.

## 5. How a shape is used, and what a difference means

**Use, drawn.** What a gate actually does when a step closes: look in
`temp/`, find which shapes govern what was made, read, and settle
each difference. Two of its endings are easy to misread as gaps in
prose and are plainly endings here — "nothing was staged" is a
complete answer, and "no shape governs this" means nothing is
checked and that is correct.

```mermaid
flowchart TB
  CLOSE["a step closes"] --> TMP{"anything staged<br/>in temp/ for this step?"}
  TMP -->|no| TICK1["tick it, saying so —<br/>'none' is a complete answer"]
  TMP -->|yes| MOVE["read it, then it becomes<br/>this project's own shape"]
  TICK1 --> GOV
  MOVE --> GOV{"does any shape govern<br/>what this step made?"}
  GOV -->|none| NONE["nothing is checked,<br/>and that is correct"]
  GOV -->|one or more| READ["read what the step made<br/>against each"]
  READ --> DIFF{"a difference?"}
  DIFF -->|no| TICK2["tick, naming what it<br/>was checked against"]
  DIFF -->|yes| PROP["propose it as a diff —<br/>never correct it"]
  PROP --> WHO{"the human says<br/>which of three"}
  WHO -->|"the shape was wrong here"| A["the shape changes;<br/>the output stands"]
  WHO -->|"the output drifted"| B["the output is brought<br/>to the shape"]
  WHO -->|"each has something"| C["both move"]
```

A gate reads what a step made against every shape governing it, and
**what it ticks records what it checked against** — including that
nothing was staged and nothing governed, which are answers rather
than omissions. A tick with no note is what would be wrong.

A difference is **proposed as a diff and never corrected**. That is
the whole guard against a shape check becoming a review of the work:
the gate says where two things differ, and a human says what that
means. It ends one of three ways, decided per difference and never
by a policy of preferring one side: **the shape
was wrong here**, so it changes and the output stands; **the output
drifted**, so it is brought to the shape; or **each has something**,
and both move.

Two things follow either way. Outputs closed before the change are
not reopened — each looks like what the shape asked for when it was
written, and the difference between them records when the shape
changed. And an exposed shape that changes stays exposed; a dated
line is not a withdrawal.

**A shape record that never changes is either finished or unread.**

## Why it arrives this way

The first convention with no skill: its artifact is a rule,
because a shape's moment is a path being touched, and a rule loads
on the path. An exposed shape arrives the same way, as a rule with
its own `paths:`. An unexposed one reaches no agent by design —
nothing loads `.claude/shapes/`, and that is its force (§3).

## What this does not cover

- **When an output opens, extends and closes** — the convention
  that owns the output; a shape that restates it is a copy of that
  convention (§1).
- **How a rule loads** — `docs/conventions/agent-arrangement/` §3.2.
- **What passes between repositories, and how** —
  `docs/conventions/exchange/`.
- **The gate items that make a project meet a shape at a step's
  close** — whatever defines the project's steps; for a run born
  from the deliverer, `delivery/fills/cbc-run-pure-playbook.md`.
- **Whether `docs/baselines/` holds anything that is a shape
  rather than trial evidence** — §2 draws the line; the sorting
  against it is its own work, not yet done.
