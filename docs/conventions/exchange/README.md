# The exchange

**Everything that passes between a deliverer and a run, in both
directions, and what each side keeps so it can happen again.**

## What it is for

So that a deliverer and a blind run stay in step: files go down
whole, what the run learned comes back as a reading, and a verdict
returns — each side holding only the half it can run. Not version
control: a pin is one part of it. The failure it answers is lived.
Until 2026-09-26 the receiver's protocol, `convention-lifecycle`,
154 lines, was held by the deliverer, which never once ran it,
while run 3 ran it at every take; the deliverer's half was
`bundle-update.md`, 527 lines; and the rule for editing a copy was
written twice in two repos, six elements the same in different
words (§5.1). Made one convention on 2026-09-26 (CBC ADR-0036); §7
says what it replaced.

## What this is made usable as

The first convention whose artifacts split between the two
arrangements, each side holding only what it runs
(`docs/conventions/agent-arrangement/`, its seats).

- **`delivery/container/.claude/rules/delivered-copies.md` — a
  rule, shipped**, held at `.claude/rules/delivered-copies.md` and
  loading when a copy or a file in `temp/` is touched. §4 and §5.
- **`.claude/skills/exchange-read/SKILL.md` — the deliverer's**,
  opened when the reviewer says to read a run. §6: find the span
  from the run's read-through, read the three things, write the
  reading. Ends where the work begins.
- **`.claude/skills/exchange-deliver/SKILL.md` — the deliverer's**,
  opened when the reviewer says to deliver. §3: the note committed
  last, the staging on the word; the same whether a reading
  preceded it or not. Birth is a delivery into the root plus the
  fills, and `delivery/installs/pure-seed.md` keeps that.
- **`.claude/rules/exchange-reading.md` — the reading's shape, the
  deliverer's**, loading while a reading in `temp/` is written. What
  `exchange-read` writes, and what the work then fills, to one
  form.

No artifact explains anything. What derives from this page is that
list. A change here walks it; a change forced in one of them is
checked back against this page.

*Does the name hold? Every section is about something passing
between two repos. Nothing in it is about versions except one
number. It held, 2026-09-26.*

## The seats

The two seats do different things, and the body is written per
seat. **The deliverer's** is §3, down, and §6, up, written in the
first person because they are its own. **The run's** is §4, the
take, and §5, editing a copy. §1 and §2 are both seats'.

## 1. What cannot change

Five facts. A design that ignores one of them is describing a
different system.

1. **A run is blind.** It holds no address for its deliverer, no
   checkout, no remote. It cannot fetch.
2. **Nothing arrives by itself.** Every delivery is decided on the
   deliverer's side and carried across by hand — the reviewer's, or
   the agent's on the reviewer's word. Never automatic, never
   started by the run.
3. **The run holds copies; the deliverer holds masters.** A copy
   changes only by being copied anew — or by the run editing it,
   which is the next fact.
4. **A run edits a copy when it fails it.** That is where learning
   starts, and it happens in the file, mid-work, not in a note.
5. **Nothing moves upward as files.** The deliverer reads the run.
   A run never pushes.

## 2. What each side keeps

### 2.1 The deliverer

The masters. Nothing per run.

### 2.2 The run

The copies, and one line per note in its own decisions
log carrying two numbers — **the pin**, the deliverer's commit its
copies equal, and **the read-through**, its own commit the
deliverer last read up to. The first comes from the staging's name,
the second from the note. Its edits since the pin need no record
of their own — they are the diff against what was delivered, and
git holds it.

Both numbers are in the run because the run is the only place the
deliverer can look. To deliver, read the run's pin and diff forward
in the deliverer's tree. To read, read the run's read-through and go
forward in the run's. *Intended: today the run records the pin and
nobody records the read-through; the last reading found its start
by matching a
devlog date against the run's log.*

The pin is a commit of the deliverer's. The run stores it and
cannot resolve it, so everything the run needs to check must be
checkable against its own tree.

### 2.3 At the pin, the bytes match

The moment a run takes a delivery,
every copy equals the master exactly, and anyone can check it with
`diff`. Between pins the copy is the master plus the run's edits,
and that difference is the whole of what the deliverer reads. A
take overwrites whole and the bytes match again. Same pin, same
bytes; different bytes means the run has learned something not yet
read.

### 2.4 The records are the one exception

The reason is that they never update. `PLAN`, `TODO` and the
devlog are delivered once as stubs, the entry file once as a
composed file; the run fills them; no later delivery touches
them. Their skeleton froze at birth, so no compare ever runs on
them.

*Rejected 2026-09-25: syncing a skeleton and letting the rest stay
local, for every copy. It would make the compare a judgement where
it is now a `diff` — the miscount problem made permanent; it would
let a run's edit stay in the local part and never reach the next
run, which is the one thing the loop exists to prevent; and the
need it serves already has a home, the run's own records (§5). The
trigger that would reopen it: a run re-applying the same declined
edit after two re-pins. It has not happened.*

### 2.5 One cycle, drawn

Two repos, two numbers, and only a note moves either.

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

Read from the read-through, forward in their tree. Deliver from the
pin, forward in ours. A note without files is a `t` that writes the
read-through and leaves the pin where it was.

## 3. Down

### 3.1 Staging

On the reviewer's word, the delivery and its note are
copied into the run's `temp/` — by the reviewer, or by the agent
when told to. The agent never stages unasked: this repo did once,
into a run mid-step, and it cost that run a commit plan. Whoever
copies, the run's tree is checked quiet first — `git status` there,
nothing in flight — and when it is the agent, it reports what it
found and waits for the word before anything lands. The
staging is named by the commit at which the files and the note are
both final — commit the note last, then name the bundle — so the
pin the run records points at exactly the note it read. *The last
delivery was named one commit before its note was finished.*

### 3.2 What goes

Files, whole. The groups that ship — method,
container, a stack practice if the run is on that stack — and the
concept. Nothing that explains them; the explanation stays home.

### 3.3 Each group is a piece of the run's tree

Inside
`delivery/<group>/`, every path is the path it lands at:
`delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/`. Staging is copying each group the
run takes on top of the last; the result *is* the run's tree, and a
group is left out by not naming its directory. No list of files, no
mapping, nothing to forget. *Until 2026-09-26 `container/` mirrored
and the other two did not — their skills sat flat and were re-homed
by a script line each.* The one named exception is
`concept/`, which stays at this repo's root because the repo is the
concept, and lands at `docs/concept/`; that is the whole of the
mapping, stated here once.

### 3.4 Every shipped file is in exactly one group

The staging checks:
a path claimed by two groups is an error, not a merge. When one
group's words must sit in another group's file — the method's
playbook inside the container's `PLAN.md` — that is a **fill**: the
owning group's file has a marked place, the other group provides
the text, the staging writes it in. Fills are the only step that is
not a copy; they are listed in one place and there are few. *One
exists. One is owed: the container's entry file names the method
skills and `docs/concept/`, so a run taking container without
method would be born with an entry file about files it does not
hold. No such run exists; when one does, those lines become a
fill.*

### 3.5 Every shipped file carries `foundation`

The field — its
name, that every derived file has one, and what it holds for each
kind — is the conventions convention's,
`docs/conventions/conventions/` §2. What is the exchange's: the
line travels with the copy as a live claim, what this file comes
from *now* and not when or from which run, and nothing in a copy
can say otherwise. *Until 2026-09-26 the five method and stack
skills carried this as a comment on line 6, in two different
verbs, nine templates repeated it, and the container's files
carried nothing.*

**One pin** for all of it. Not one per group, not one per
convention. A run that holds two pins for one delivery has been
given a way to be inconsistent.

### 3.6 A copy carries presence and content, never absence

A file
that was delivered before and is not in this staging is still in
the run, and nothing copied can say otherwise. So the note names
every deletion and every rename by path — this is gone, this is
now that. The deliverer finds them with `git diff -M` between the
run's pin and the staging; the run cannot, because it cannot
resolve the pin. A rename in the delivery is a delete and an add,
and the note says both halves.

### 3.7 The note

What changed since the run's pin, stated so the run
can diff the staging against what it holds and find the note wrong.
Why it matters to this run — the part a diff cannot carry. A verdict
on everything the run addressed to us since we last read it.
Nothing that needs our repo to verify: a note that reports facts
about our tree gives the run a hedge it cannot close.

*Three rules about verdicts, each a defect first: a verdict is the
decision and what the run owes now, nothing else; never describe our
own practice, which the run cannot check; never say "accepted" for
something not decided. And four ways a note fails to reach: it was
thin; the thing it names does not exist; the relationship changed
under it; or it carried the right content in a shape the run could
not act on — the last found on 2026-09-20, when a note of reports
was sent back and rewritten as verdicts.*

## 4. The take

The run's agent, from `temp/`, in this order. Nothing in `temp/`
is in force until it is copied into place — a staged skill is a
file, not a skill, and a step that opens meanwhile runs on the held
copy.

1. **Check the note against the staging.** Diff every delivered
   file against what the run holds. The note said N files differ;
   the diff says how many. A mismatch is reported before anything
   moves.
2. **Find your own edits.** The diff of each held copy against the
   pin. Empty: nothing to protect. Not empty: each edit is either
   answered in the note (taken — the new copy carries it; declined
   — it goes, and the need it served goes to the run's records) or
   unanswered, which means it was made after the deliverer last read,
and it
   is re-applied on top.
3. **Place.** The delivered files overwrite the copies whole. A
   receipt branch — the delivery as it arrived, named by the pin —
   is worth cutting when the run expects to edit, because it makes
   step 2's diff exact next time. Optional.
4. **Remove what the note says is gone.** Each path the note names
   as deleted is deleted; each it names as renamed is moved. The
   only step a copy cannot do, and the one that has been missed
   before — a rename once left the old file standing in a run for
   four days.
5. **Register.** One line in the run's decisions log: the date, the
   pin, what came, what was declined and where its need went. Agent
   side only. Then `temp/` is emptied.

## 5. Editing a copy

### 5.1 One rule for every shipped skill and rule

There are not two.
*Finding, checked side by side 2026-09-25: today it is written twice
— once for conventions inside the receiver's protocol, once for the
method skills in a file run 3 wrote itself. Six elements are the
same rule in different words. Run 3's is the superset: it alone
puts the pin and the never-edited concept in one place, states a
priority when edits stack — behind the source is acceptable, behind
this run's own lessons is not — and covers a skill the run has
finished with. The deliverer's alone carried a "provisional" clause that
expired on 09-20, when the first edit went through a re-pin. The
shipped rule is built from theirs.*

A copy may be edited in place when all three hold:

- **Something happened** in this run that the copy did not foresee.
  Never a speculation.
- **The edit asks a question or demands an outcome any run would
  want.** Never this run's own answer. What only this run needs goes
  in its own records, not in the copy.
- **Three records, none of them in the file:** one entry in the
  run's decisions log saying what changed and why; one line in its
  backlog addressed to the deliverer, asking for a verdict since the
  pin; and the diff against the pin, which exists whether anyone
  writes anything.

The backlog lines live under one heading kept for them, *To the
deliverer*. The backlog is the channel — a hand-off is the run's
own open item, waiting on an answer, with a lifecycle git can see:
filed at a step's close, gone with the pin that answers it. `temp/`
is not the channel the other way: it is untracked, emptied at the
take, and a line left there would vanish without a record. One
heading keeps the lines from being swept with a rewrite elsewhere —
which has happened, five items in one commit — and makes the read
one section instead of a search.

Nothing is written into the copy but the edit. No dated line, no
comment saying what changed — a file says how to use it, never its
own history.

### 5.2 A copy the run has finished with

It is edited the same way. One
process for every copy. The one difference is said in the log
entry: a running skill's fix is exercised by the next step here; a
finished skill's fix is first used by the deliverer.

### 5.3 Edits made before a verdict

They stack on the run's side only. Behind the deliverer is
acceptable; behind the run's own lessons is not.

### 5.4 One word for the other side

In the rule and in the backlog line:
*deliverer*. Run 3's text says *source*; `master.md` says
deliverer, and the shipped rule says one thing.

### 5.5 A run does not rename or delete a copy

The delivered path is
the copy's identity for the take: a renamed copy becomes two files
at the next delivery, a deleted one comes back. A copy the run has
no use for is a backlog line — *we do not use this* — and the
deliverer decides.

### 5.6 The concept is never edited

A chapter is not run, so nothing
in it can fail a step. A lesson about the concept is a prose
hand-off in the backlog line, and it reaches the chapter, if it
does, from the deliverer's side.

### 5.7 The records

They are the run's own from birth, not copies (§2.4), and this
section does not apply to them.

## 6. Up

### 6.1 The read

We open the run's repository and read three things
since the read point: its decisions log (every edit and why), its
backlog (every line addressed to us), and the diff of every held
copy against its pin. Nothing else is required; the devlog is
context.

### 6.2 A file the run wrote

It is the run's own until the run offers it. It appears in the
diff against the pin as an addition, and it is read only if a
backlog line points at it — a shape, a rule, a
reference the run thinks any project would want. Then it gets a
verdict like an edit does. That is how a run's rule for editing
copies reached this document.

### 6.3 The reading

The read produces a reading, or extends the one open for that
run — a document in `temp/` listing every edit, every ask and
every finding, one line each, revised as items close and deleted
when the work does. One per run at a time. The reading is the
list; working it is ordinary work here — a commit plan when it
takes more than one commit, an ADR when a decision has rejected
options — and the exchange says nothing about how, only what each
item must end as, and where.

### 6.4 A reading closes two ways

Its work closes — every item taken,
declined or held, the note gone down. Or it is **overtaken**: the
deliverer's tree has moved so far while the reading was open that
its items no longer describe it, though the run's side may still be
true. An overtaken reading is closed the same way — one pass over
its open items saying where each went — and deleted; the next read
starts fresh rather than extending a list written against a tree
that no longer exists. *Found once: a reading paused on 09-24 while
sixty commits changed the ground under it; every open item had been
dissolved or moved by what was done instead.*

### 6.5 Verdicts

Each item leaves the list with one of three:

- **Taken** — a master changes here, committed. The next delivery
  carries it, and the run's edit is absorbed rather than
  overwritten.
- **Declined** — with why, and the why is never "the description
  says otherwise" (`docs/conventions/conventions/` §3.6 owns that
  rule; it is about every description, not only this one). A
  description can be what the run has found wrong. Declined means:
  not general, or not worth the change. The why goes in the note
  and nowhere else; nothing in our tree moves.
- **Held** — with the trigger that would settle it, and a line in
  our own backlog so it is not lost between readings.

An unverifiable promise is worse than any of the three. The note
carries all of them, in the run's order.

### 6.6 Every read ends with a note

Even an empty one. The note names
the run's commit we read through; the run records it beside the pin
(§2). A read that finds nothing addressed to us still sends *read
through `<commit>`, nothing to answer, no files* — one line each
side — so the run always holds the latest read-through, and can see
for itself when a hand-off was seen and not yet answered.

### 6.7 Verdicts travel in the note

There is no other channel. A note
alone, with no files, is still a delivery: the read-through moves,
the pin does not.

## 7. What this replaced, 2026-09-26

| what stood | where | what became of it |
|---|---|---|
| `convention-lifecycle` skill, 154 lines | ours, and shipped | replaced by §4–§5 as the run's half; deleted here |
| `skills-changed-in-place.md`, run 3's own | run 3 | replaced by `delivered-copies.md`, derived from it and shipped; the note names the rename |
| `bundle-update.md`, 527 lines | `delivery/installs/` | replaced by §3 and §6 as our half; the lessons list it never had is what §3–§6 are |
| the harvest section of `delivery/README.md` | ours | folds into §6 |
| the entry-file line "never edited in place" | shipped | contradicts §5; goes |
| `delivery/method/` and `delivery/spring-postgres/` laid out flat | ours | each becomes a piece of the run's tree, §3; two `git mv` per skill |
| the file lists inside `bundle-update.md`'s scripts | ours | gone with the mapping; a group is a directory name |
| the line-6 derivation comments in five skills, and nine template lines | shipped | became the one frontmatter field, `foundation`, `docs/conventions/conventions/` §2 |
| `master.md` §2.5 and §3 | ours | stay; this is their detail |

## Why it arrives this way

The run's half is a rule rather than a skill because its moment is
a path being touched — a copy, or a file in `temp/` — and it loads
when the moment arrives instead of waiting to be opened by name:
the failure the receiver's protocol had since the day it shipped.
The deliverer's two skills open on the reviewer's word, "read" or
"deliver", which is a moment the agent is told rather than one it
must notice. The reading's shape loads by path while a reading is
written.

## What this does not cover

- **Which files each side holds, and which paths are the
  arrangement's** — `docs/conventions/agent-arrangement/`, its
  seats.
- **What `foundation` holds for each kind of file** —
  `docs/conventions/conventions/` §2.
- **How a shape reaches a run** — `docs/conventions/shapes/` §4.
- **How the deliverer works a reading** — ordinary work: a commit
  plan when it takes more than one commit,
  `docs/conventions/commit-plan/`, and an ADR when a decision has
  rejected options, `docs/conventions/project-recording/`.
- **The concept's version** — CBC ADR-0003, and `docs/master.md`
  §1.1.
- **The birth procedure** — `delivery/installs/pure-seed.md`.
