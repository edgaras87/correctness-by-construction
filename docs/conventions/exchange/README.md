---
foundation: the tiers model
---

# The exchange

**Everything that passes between the Concept Deliverer and a CBC Run,
in both directions, and what each side keeps so it can happen again.**

## What it is for

So that the Concept Deliverer and a blind CBC Run stay in step: files go down
whole, what the CBC Run learned comes back as a Run Reading, and a verdict
returns — each side holding only the half it can run. Not version
control: a Delivery Pin is one part of it. The failure it answers is lived.
Until 2026-09-26 the receiver's protocol, `convention-lifecycle`,
154 lines, was held by the Concept Deliverer, which never once ran it,
while CBC Run 3 ran it at every Delivery Take; the Concept Deliverer's half was
`bundle-update.md`, 527 lines; and the rule for editing a copy was
written twice in two repos, six elements the same in different
words (§5.1, *When a copy may be edited*). Made one convention on 2026-09-26; what it replaced
is ADR-0036's.

## What this is made usable as

The first convention whose artifacts split between the two
arrangements, each side holding only what it runs
(`docs/conventions/agent-arrangement/`, *The seats*).

- **`delivery/container/temp/README.md` — shipped at birth**, the
  CBC Run's own from then on: what its `temp/` is for, where a delivery
  arrives and the CBC Run keeps its own scratch (§3.1, *Delivery Staging*; §4, *The Delivery Take*).
- **`delivery/container/.claude/rules/delivered-copies.md` — an
  Agent Rule, shipped**, held at `.claude/rules/delivered-copies.md` and
  loading when a copy or a file in `temp/` is read (§4, *The Delivery Take*; §5, *Editing a copy*).
- **`.claude/skills/exchange-read/SKILL.md` — the Concept Deliverer's**,
  opened when the reviewer says to read a CBC Run (§6, *Up from the CBC Run*): find the span
  from the CBC Run's Read-Through Commit, read the three things, write the
  Run Reading. Ends where the work begins.
- **`.claude/skills/exchange-deliver/SKILL.md` — the Concept Deliverer's**,
  opened when the reviewer says to deliver (§3, *Down to the CBC Run*): the Delivery Note committed
  last, the Delivery Staging on the word; the same whether a Run Reading
  preceded it or not. Birth is a delivery into the root plus the
  fills, and `delivery/installs/pure-seed.md` keeps that.
- **`.claude/rules/exchange-reading.md` — the Run Reading's form, the
  Concept Deliverer's**, loading when a Run Reading in `temp/` is read, not
  while a new one is written (`docs/conventions/agent-arrangement/`
  §5.6, *Rules files*). What `exchange-read` writes, and what
  the work then fills, to one form.
- **`.claude/rules/working-a-reading.md` — how a Run Reading's list is
  worked, the Concept Deliverer's**, practice under this page, loading when
  a Run Reading in `temp/` is read. It works each item to its ending (§6.5, *Verdicts*).

No artifact explains anything. What derives from this page is that
list. A change here walks it; a change forced in one of them is
checked back against this page.

*Its story: devlog 2026-09-25, later.*

## The seats

The two Convention Seats do different things, and the body is written per
Convention Seat. **The CBC Run's** is the Delivery Take and editing a copy (§4, *The Delivery Take*;
§5, *Editing a copy*). **The Concept Deliverer's** is down and up (§3, *Down to the CBC Run*;
§6, *Up from the CBC Run*), written in the first person because they are its own. What
cannot change and what each side keeps are both Convention Seats' (§1, *What
cannot change*; §2, *What each side keeps*).

## 1. What cannot change

The five facts that hold on every flow between a tier and the one
below hold between the Concept Deliverer and a CBC Run
(`docs/models/tiers.md` §3.5, *What holds on every flow*). Here
they mean:

1. **A CBC Run is blind.** No address for its Concept Deliverer, no checkout,
   no remote.
2. **Nothing arrives by itself.** The reviewer carries a delivery
   across, or the agent does on the reviewer's word.
3. **The CBC Run holds copies; the Concept Deliverer holds Master Copies.**
4. **A CBC Run edits a copy when it fails it,** in the file, mid-work,
   not in a note (§5, *Editing a copy*).
5. **Nothing moves upward as files.** The Concept Deliverer reads the CBC Run,
   and a CBC Run never pushes (§6, *Up from the CBC Run*).

## 2. What each side keeps

### 2.1 The Concept Deliverer

The Master Copies. Nothing per CBC Run.

### 2.2 The CBC Run

The copies, and one line per Delivery Note in its own Decisions
Log carrying two numbers — **the Delivery Pin**, the Concept Deliverer's commit its
copies equal, and **the Read-Through Commit**, its own commit the
Concept Deliverer last read up to. The first comes from the Delivery Staging's name,
the second from the Delivery Note. Its edits since the Delivery Pin need no record
of their own — they are the diff against what was delivered, and
git holds it.

Both numbers are in the CBC Run because it is the only place the
Concept Deliverer can look. To deliver, read the CBC Run's Delivery Pin and diff forward
in the Concept Deliverer's tree. To read, read the CBC Run's Read-Through Commit and go
forward in the CBC Run's. *Its story: devlog 2026-10-29, the lessons' own stories: the exchange.*

The Delivery Pin is a commit of the Concept Deliverer's. The CBC Run stores it and
cannot resolve it, so everything the CBC Run needs to check must be
checkable against its own tree.

**One Delivery Pin** for everything delivered, as on every flow
(`docs/models/tiers.md` §3.5, *What holds on every flow*): not one
per group, not one per convention.

### 2.3 The bytes at the Delivery Pin

The moment a CBC Run takes a delivery,
every copy equals the Master Copy exactly, and anyone can check it with
`diff`. Between Delivery Pins the copy is the Master Copy plus the CBC Run's edits,
and that difference is the whole of what the Concept Deliverer reads. A
Delivery Take overwrites whole and the bytes match again. Same Delivery Pin, same
bytes; different bytes means the CBC Run has learned something not yet
read.

### 2.4 The records' exception

The records are the one exception. They never update: `PLAN`, `TODO` and the
devlog are delivered once as Record Stubs, the entry file once as a
composed file; the CBC Run fills them; no later delivery touches
them. Their skeleton froze at birth, so no compare ever runs on
them.

*Its story: devlog 2026-09-25, later.*

Skeleton sync is reopened if a CBC Run re-applies the same declined edit
after two re-pins.

### 2.5 One cycle, drawn

Two repos, two numbers, and only a Delivery Note moves either.

```
   D      ───X───────────────────────────Y──────────▶
             ▲                             ▲
             │ pin = X                     │ pin = Y
             │                             │
   R      ───b────e1────e2────r────────────t──────────▶
                               ▲
                               │ read-through = r
                               (named in the note, recorded at t)

   D   the deliverer's history.  R   the run's.
   b   born from X. The run writes: pin X, read-through b.
   e   the run edits a copy. Nothing moves; the diff grows.
   r   the deliverer reads from b to r, writes the reading, works
       it, changes masters. D moves; neither number does yet.
   Y   the note is committed at the deliverer, last. The staging
       is named Y.
   t   the run takes. It writes: pin Y, read-through r.
```

Read from the Read-Through Commit, forward in their tree. Deliver from the
Delivery Pin, forward in ours. A Delivery Note without files (§6.6, *The Delivery Note after a read*) is a `t` that
writes the Read-Through Commit and leaves the Delivery Pin where it was.

## 3. Down to the CBC Run

### 3.1 Delivery Staging

On the reviewer's word, the delivery and its Delivery Note are
copied into the CBC Run's `temp/` — by the reviewer, or by the agent
when told to. The agent never stages a delivery unasked. Whoever
copies, the CBC Run's tree is checked quiet first — `git status` there,
nothing in flight — and when it is the agent, it reports what it
found and waits for the word before anything lands. The
Delivery Staging is named by the commit at which the files and the Delivery Note are
both final — commit the Delivery Note last, then name the bundle — so the
Delivery Pin the CBC Run records points at exactly the Delivery Note it read. *Its story: devlog 2026-09-25, later; devlog 2026-10-29, the lessons' own stories: the exchange.*

### 3.2 What goes

Files, whole. The groups that ship — the Method Group, the
Container Group, the Stack Group if the CBC Run is on that stack — and the
concept. Nothing that explains them; the explanation stays home.

At birth, every file of each group. After it, only the copies: the
Container Group's skills, Agent Rules and Approaches on Trial; the Method Group's and the Stack Group's
skills, Agent Rules and Output Shapes; the concept. The rest of the Container Group —
its records, the two entry files, the Decisions Log, the hygiene
files — went once and is the CBC Run's (§2.4, *The records' exception*); a later delivery that
carried it would land Record Stubs over what the CBC Run has written.

### 3.3 A group's place in the tree

Inside
`delivery/<group>/`, every path is the path it lands at:
`delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/`. Delivery Staging is copying each group the
CBC Run takes on top of the last; the result *is* the CBC Run's tree, and a
group is left out by not naming its directory. No list of files, no
mapping, nothing to forget. *Its story: devlog 2026-09-26, evening.* The one named exception is
`concept/`, which stays at this repo's root because the repo is the
concept, and lands at `docs/concept/`; that is the whole of the
mapping, stated here once.

### 3.4 One group per file

Every shipped file is in exactly one group, and the Delivery Staging checks it:
a path claimed by two groups is an error, not a merge. A skill
belongs to one group and travels whole, never split across two. The
Method Group holds no stack: nothing that needs Spring, PostgreSQL, Maven
or podman sits under `delivery/method/`, so a CBC Run on another stack
takes the Container Group and the Method Group and leaves the Stack Group
(ADR-0029). When one
group's words must sit in another group's file — the Method Group's
playbook inside the Container Group's `PLAN.md` — that is a **fill**: the
owning group's file has a marked place, the other group provides
the text, the Delivery Staging writes it in. Fills are the only step that is
not a copy; they are listed in one place and there are few. One
exists. One is owed: the Container Group's entry file names the Method Group's
skills and `docs/concept/`, so a CBC Run taking the Container Group without
the Method Group would be born with an entry file about files it does not
hold. When such a CBC Run exists, those lines become a fill.

### 3.5 The Foundation Line in a copy

Every shipped skill, Agent Rule and Output Shape carries a Foundation Line. The field — its name, that each has one,
and what it holds for each kind — is the conventions manual's
(`docs/conventions/conventions/` §1.3, *The Foundation Line*). What is the Exchange Convention's: the
line travels with the copy as a live claim, what this file comes
from *now* and not when or from which CBC Run, and nothing in a copy
can say otherwise. *Its story: devlog 2026-09-26, evening; devlog 2026-10-29, the lessons' own stories: the exchange.*

### 3.6 Absence in a delivery

A copy carries presence and content, never absence. A file
that was delivered before and is not in this Delivery Staging is still in
the CBC Run, and nothing copied can say otherwise. So the Delivery Note names
every deletion and every rename by path — this is gone, this is
now that. The Concept Deliverer finds them with `git diff -M` between the
CBC Run's Delivery Pin and the Delivery Staging; the CBC Run cannot, because it cannot
resolve the Delivery Pin. A rename in the delivery is a delete and an add,
and the Delivery Note says both halves.

### 3.7 The Delivery Note

What changed since the CBC Run's Delivery Pin, stated so the CBC Run
can diff the Delivery Staging against what it holds and find the Delivery Note wrong.
Why it matters to this CBC Run — the part a diff cannot carry. A verdict
on everything the CBC Run addressed to us since we last read it, in the
CBC Run's order: the Delivery Note is the verdicts' only channel. A
verdict says the decision and what the CBC Run owes now, nothing else.
It never describes our own practice, which the CBC Run cannot check. It
never says "accepted" for something not decided.
Nothing that needs our repo to verify: a Delivery Note that reports facts
about our tree gives the CBC Run a hedge it cannot close. Where a claim
cannot avoid it — a thin Delivery Note, which ships no copy; material
outside the delivery; a negative claim, which is about our whole
tree — the Delivery Note says so, in a clause. A Delivery Note fails to reach when it
is thin, when what it names does not exist, when the relationship
changed under it, or when the right content comes in a form the CBC Run
cannot act on.

No ADR number, no path in this repo and no word of this repo's own
vocabulary, in a Delivery Note or in a prompt: the CBC Run cannot see this repo,
and a citation it cannot follow reads as its own. That is told text.
A shipped file carries the Repo Tag instead, `CBC ADR-nnnn`
(`docs/conventions/project-recording/` §3.5, *Numbers across repos*), because a file stays
in the CBC Run and a Delivery Note is read once (ADR-0020).

A Delivery Note that names a third repository gives both names: ours, by
ordinal, and the one it gave itself at its Identity Plan Step. A CBC Run's
records do not say which is which; ours do (`ARCHITECTURE.md` §2.5, *The runs*).

*Its story: devlog 2026-09-20.*

## 4. The Delivery Take

The CBC Run's agent, from `temp/`, in this order. Nothing in `temp/`
is in force until it is copied into place — a staged skill is a
file, not a skill, and a Plan Step that opens meanwhile runs on the held
copy.

1. **Check the Delivery Note against the Delivery Staging.** Diff every delivered
   file against what the CBC Run holds. The Delivery Note said N files differ;
   the diff says how many. A mismatch is reported before anything
   moves.
2. **Find your own edits.** The diff of each held copy against the
   Delivery Pin, which the CBC Run holds as the commit of its last delivery entry
   (§2.2, *The CBC Run*). Empty: nothing to protect. Not empty: each edit is either
   answered in the Delivery Note (taken — the new copy carries it; declined
   — it goes, and the need it served goes to the CBC Run's records) or
   unanswered, which means it was made after the Concept Deliverer last
   read, and it is re-applied on top.
3. **Place.** The delivered files overwrite the copies whole. The
   Delivery Take's commits follow `docs/conventions/commit-messages/`; when
   they are more than one, the chapters' commit comes first, so
   step 5's entry lands in the last (ADR-0046). A receipt
   branch — the delivery as it arrived, named by the Delivery Pin — is worth
   cutting when the CBC Run expects to edit, because it makes step 2's
   diff exact next time. Optional.
4. **Remove what the Delivery Note says is gone.** Each path the Delivery Note names
   as deleted is deleted; each it names as renamed is moved. The
   only step a copy cannot do. *Its story: devlog 2026-09-25, later.*
5. **Register.** One line in the CBC Run's Decisions Log: the date, the
   Delivery Pin, what came, what was declined and where its need went. Agent
   side only, and in the last commit, where every copy equals the
   Delivery Pin. Then the Delivery Staging goes — the directory named for the Delivery Pin and
   its Delivery Note — and nothing else: `temp/` may hold the CBC Run's own
   drafts, which are not the delivery's to clear. *Its story: devlog 2026-10-08.*

## 5. Editing a copy

### 5.1 When a copy may be edited

One rule holds for every delivered copy; there are not two.
*Its story: devlog 2026-09-25, later.*

A copy may be edited in place when all three hold:

- **Something happened** in this CBC Run that the copy did not foresee.
  Never a speculation.
- **The edit asks a question or demands an outcome any CBC Run would
  want.** Never this CBC Run's own answer. What only this CBC Run needs goes
  in its own records, not in the copy.
- **Three records, none of them in the file:** one entry in the
  CBC Run's Decisions Log saying what changed and why; one line in its
  backlog addressed to the Concept Deliverer, asking for a verdict since the
  Delivery Pin; and the diff against the Delivery Pin, which exists whether anyone
  writes anything.

The backlog lines live under one heading kept for them, *To the
deliverer*. The backlog is the channel — a hand-off is the CBC Run's
own open item, waiting on an answer, with a lifecycle git can see:
filed at a Plan Step's close, gone with the Delivery Pin that answers it. `temp/`
is not the channel the other way: it holds drafts, not records,
its files go once they have served, and a line left there would
go with them. One heading keeps the lines from being swept with a
rewrite elsewhere, and makes the read one section instead of a
search. *Its story: devlog 2026-10-29, the lessons' own stories: the exchange.*

Nothing is written into the copy but the edit. No dated line, no
comment saying what changed — a file says how to use it, never its
own history.

One kind of copy takes one more edit: an Approach on Trial gets a
dated note of each use under its *Uses*, in the CBC Run's own terms.
The note is what the Approach on Trial is for, since it carries the use to
the Concept Deliverer's evaluation. It is the CBC Run's own account, so the
second condition does not hold it; the other two do.

### 5.2 A finished copy

A copy the CBC Run has finished with is edited the same way, whenever the evidence is in the CBC Run, and
never kept as a note for a later CBC Run: the Concept Deliverer takes or
declines an exact hunk rather than translating a note, and the CBC Run
that lived the mistake writes the fix. One process for every copy.
The one difference is said in the Decisions Log entry and in the backlog
line: a running skill's fix is exercised by the next Plan Step here; a
finished skill's fix is first used by the Concept Deliverer, so its line
marks it *untried here*, and the Concept Deliverer reads those hunks
hardest. Such an edit is taken when it is sound, and the next CBC Run
is its trial (ADR-0051).
*Its story: ADR-0051.*

### 5.3 Edits made before a verdict

They stack on the CBC Run's side only. Behind the Concept Deliverer is
acceptable; behind the CBC Run's own lessons is not.

### 5.4 One word for the other side

In the rule and in the backlog line:
*the Concept Deliverer*. CBC Run 3's text says *source*; `docs/glossary.md` says
Concept Deliverer, and the shipped Agent Rule says one thing.

### 5.5 Renaming or deleting a copy

A CBC Run does not rename or delete a copy. The delivered path is
the copy's identity for the Delivery Take: a renamed copy becomes two files
at the next delivery, a deleted one comes back. A copy the CBC Run has
no use for is a backlog line — *we do not use this* — and the
Concept Deliverer decides.

### 5.6 Editing a chapter

A chapter is edited as any copy (§5.1, *When a copy may be edited*), and only from a mistake
lived in the CBC Run, never from a preference for other wording. Skills
are written from the chapters and readers learn the method from
them, so lived work can show one wrong; and the Concept Deliverer judges an
exact hunk where a prose line must first be translated. The edit is
the CBC Run's copy's: the concept changes only when the Concept Deliverer takes
it (ADR-0051).
*Its story: ADR-0051.*

### 5.7 The records

They are the CBC Run's own from birth, not copies (§2.4, *The records' exception*), and this
section does not apply to them.

### 5.8 Filling a Skill Template

A Skill Template, a file in a skill's `templates/`, arrives pinned, with the rest of the
skill. At use, the CBC Run copies it to the path the skill names and
fills it. The filled file is the CBC Run's own, as a record is (§5.7,
*The records*), and may drop the Skill Template's header. The Skill
Template stays the pinned copy. A change to it, such as a
line every run needs or a comment that was wrong, is an edit to the
copy under its rule (§5.1, *When a copy may be edited*). The filled
values never come back: they are the CBC Run's decisions.

A CBC Run whose decided constraints differ from what a Skill Template
assumes is off-template. It derives from what the Skill Template
implements, which the skill names. It records the deviation where
its records table puts a decision, what it did instead and why
(`docs/conventions/project-recording/` §13, *The records table*). It expects the
deviation to come back as a change to the skill. It never bends a
decided constraint to fit a Skill Template (ADR-0008).

## 6. Up from the CBC Run

### 6.1 Reading a CBC Run

We open the CBC Run's repository and read three things
since its Read-Through Commit: its Decisions Log (every edit and why), its
backlog (every line addressed to us), and the diff of every held
copy against its Delivery Pin. Those three give every item; the devlog is
context.

One more look gives no item: the CBC Run's tree, the work staged or
changed there but not committed. That work is not yet the CBC Run's
word. But a verdict may rest on it, so the Run Reading names it, and no
verdict is written against what that work undoes.

*Its story: devlog 2026-10-18; devlog 2026-10-29, the lessons' own stories: the exchange.*

### 6.2 A file the CBC Run wrote

It is the CBC Run's own until the CBC Run offers it. It appears in the
diff against the Delivery Pin as an addition, and it is read only if a
backlog line points at it — an Output Shape, an Agent Rule, a
reference the CBC Run thinks any project would want. Then it gets a
verdict like an edit does.

### 6.3 The Run Reading

The read produces a Run Reading, or extends the one open for that
CBC Run — a document in `temp/` listing every edit, every ask and
every finding, one line each, revised as items close and deleted
when the work does. One per CBC Run at a time. The Run Reading is the
list; working it is ordinary work here — a commit plan when it
takes more than one commit, an ADR when a decision has rejected
options. This page says only what each item must end as, and
where; how the list is worked is
`.claude/rules/working-a-reading.md`'s, practice under it.

A Run Reading also asks what the CBC Run teaches the worked example,
`delivery/method/.claude/skills/cbc-framing/references/worked-example.md`,
which its copy in `cbc-slice` follows.

*Its story: devlog 2026-09-30, later still; devlog 2026-10-29, the lessons' own stories: the exchange.*

### 6.4 How a Run Reading closes

A Run Reading closes two ways. Its work closes — every item taken,
declined or held, the Delivery Note gone down. Or it is **overtaken**: the
Concept Deliverer's tree has moved so far while the Run Reading was open that
its items no longer describe it, though the CBC Run's side may still be
true. An overtaken Run Reading is closed the same way — one pass over
its open items saying where each went — and deleted; the next read
starts fresh rather than extending a list written against a tree
that no longer exists. *Its story: devlog 2026-09-26.*

### 6.5 Verdicts

Each item leaves the list with one of three:

- **Taken** — a Master Copy changes here, committed. The next delivery
  carries it, and the CBC Run's edit is absorbed rather than
  overwritten.
- **Declined** — with why, and the why is never "the Canonical Description
  says otherwise" (`docs/conventions/facts-in-sync/` §5, *A disagreement* owns that
  rule; it is about every Canonical Description, not only this one). A
  Canonical Description can be what the CBC Run has found wrong. Declined means:
  not general, or not worth the change. The why goes in the Delivery Note
  and nowhere else; nothing in our tree moves.
- **Held** — with the trigger that would settle it, and a line in
  our own backlog so it is not lost between Run Readings.

An unverifiable promise is worse than any of the three. The
verdicts go down in the Delivery Note (§3.7, *The Delivery Note*).

### 6.6 The Delivery Note after a read

Every read ends with a Delivery Note, even an empty one. The Delivery Note names
the CBC Run's commit we read through; the CBC Run records it beside the Delivery Pin
(§2.2, *The CBC Run*). A read that finds nothing addressed to us still sends *read
through `<commit>`, nothing to answer, no files* — one line each
side — so the CBC Run always holds the latest Read-Through Commit, and can see
for itself when a hand-off was seen and not yet answered. A Delivery Note
alone, with no files, is still a delivery: the Read-Through Commit moves,
the Delivery Pin does not.

## Why it arrives this way

The CBC Run's half is an Agent Rule rather than a skill because its moment is
a copy, or a file in `temp/`, being read, and it loads then instead
of waiting to be opened by name (`docs/models/agent.md` §4.3, *pushed*).
The Concept Deliverer's two skills open on the reviewer's word, "read" or
"deliver", which is a moment the agent is told rather than one it
must notice. The Run Reading's form loads by path when a Run Reading is
read, so it is in view while the list is worked; a Run Reading written
new is written without it (`docs/conventions/agent-arrangement/`
§5.6, *Rules files*).

*Its story: devlog 2026-10-29, the lessons' own stories: six places.*

## What this does not cover

- **Which files each side holds, and which paths are the
  arrangement's** — `docs/conventions/agent-arrangement/`, *The
  seats*.
- **What `foundation` holds for each kind of file** —
  `docs/conventions/conventions/` §1.3, *The Foundation Line*.
- **How an Output Shape reaches a CBC Run** — `docs/conventions/shapes/` §4, *Where a shape lives, between…*.
- **The commits and decisions of working a Run Reading** — a commit
  plan when it takes more than one commit,
  `docs/conventions/commit-plan/`, and an ADR when a decision has
  rejected options, `docs/conventions/project-recording/`.
- **The concept's version** — ADR-0003, and `CHANGELOG.md`'s
  standing comment.
- **The birth procedure** — `delivery/installs/pure-seed.md`.
