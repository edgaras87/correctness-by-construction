<!-- The exchange's manual: what passes between this repo and a run,
     and why it works the way it does. Never shipped; a run holds the
     rule, not this. Written from what cannot change, with what it
     replaced at the end.

     Same rule as master.md: only what is checkable, and anything
     merely intended marked as intended. -->

# The exchange

**Everything that passes between a deliverer and a run, in both
directions, and what each side keeps so it can happen again.**

Not version control. A pin is one part of it. The rest is how files
go down, how they come back changed, and how a verdict returns.

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

**The deliverer:** the masters. Nothing per run.

**The run:** the copies, and one line per note in its own decisions
log carrying two numbers — **the pin**, the deliverer's commit its
copies equal, and **the read-through**, its own commit the
deliverer last read up to. The first comes from the staging's name,
the second from the note. Its edits since the pin need no record
of their own — they are the diff against what was delivered, and
git holds it.

Both numbers are in the run because the run is the only place the
deliverer can look. To deliver, read the run's pin and diff forward
in our tree. To read, read the run's read-through and go forward in
theirs. *Intended: today the run records the pin and nobody records
the read-through; the last reading found its start by matching a
devlog date against the run's log.*

The pin is a commit of the deliverer's. The run stores it and
cannot resolve it, so everything the run needs to check must be
checkable against its own tree.

**At the pin, the bytes match.** The moment a run takes a delivery,
every copy equals the master exactly, and anyone can check it with
`diff`. Between pins the copy is the master plus the run's edits,
and that difference is the whole of what the deliverer reads. A
take overwrites whole and the bytes match again. Same pin, same
bytes; different bytes means the run has learned something not yet
read.

**The records are the one exception, and the reason is that they
never update.** `PLAN`, `TODO`, the devlog, the entry file are
delivered once as stubs; the run fills them; no later delivery
touches them. Their skeleton froze at birth, so no compare ever
runs on them.

*Rejected 2026-09-25: syncing a skeleton and letting the rest stay
local, for every copy. It would make the compare a judgement where
it is now a `diff` — the miscount problem made permanent; it would
let a run's edit stay in the local part and never reach the next
run, which is the one thing the loop exists to prevent; and the
need it serves already has a home, the run's own records (§5). The
trigger that would reopen it: a run re-applying the same declined
edit after two re-pins. It has not happened.*

**One cycle, drawn.** Two repos, two numbers, and only a note moves
either.

```
   ours   ───X───────────────────────────Y──────────▶
             ▲                             ▲
             │ pin = X                     │ pin = Y
             │                             │
   theirs ───b────e1────e2────r────────────t──────────▶
                               ▲
                               │ read-through = r
                               (named in the note, recorded at t)

   b   born from X. The run writes: pin X, read-through b.
   e   the run edits a copy. Nothing moves; the diff grows.
   r   we read from b to r, write the reading, work it, change
       masters here. Our tree moves; neither number does yet.
   Y   the note is committed here, last. The staging is named Y.
   t   the run takes. It writes: pin Y, read-through r.
```

Read from the read-through, forward in their tree. Deliver from the
pin, forward in ours. A note without files is a `t` that writes the
read-through and leaves the pin where it was.

## 3. Down

**Staging.** On the reviewer's word, the delivery and its note are
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

**What goes.** Files, whole. The groups that ship — method,
container, a stack practice if the run is on that stack — and the
concept. Nothing that explains them; the explanation stays home.

**Each group is a piece of the run's tree.** Inside
`delivery/<group>/`, every path is the path it lands at:
`delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/`. Staging is copying each group the
run takes on top of the last; the result *is* the run's tree, and a
group is left out by not naming its directory. No list of files, no
mapping, nothing to forget. *Intended: today `container/` already
mirrors and the other two do not — their skills sit flat and are
re-homed by a script line each.* The one named exception is
`concept/`, which stays at this repo's root because the repo is the
concept, and lands at `docs/concept/`; that is the whole of the
mapping, stated here once.

**Every shipped file is in exactly one group.** The staging checks:
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

**Every shipped file says what it derives from.** One frontmatter
field, beside `name` and `description`, holding a live claim and
never history: what this file comes from *now*, not when or from
which run. Method skills — the concept and its version. Stack
practice — the concept it was checked against. Container skills —
the convention whose artifact this is, by name; the manual stays
home but the name finds it. Concept chapters — nothing; they are
the top. *Intended: today eight of twelve skills carry this as a
comment on line 6, in two different verbs, and the container's four
carry nothing.* The field is not called `source`; that word already
means the deliverer in a run's text.

**One pin** for all of it. Not one per group, not one per
convention. A run that holds two pins for one delivery has been
given a way to be inconsistent.

**A copy carries presence and content, never absence.** A file
that was delivered before and is not in this staging is still in
the run, and nothing copied can say otherwise. So the note names
every deletion and every rename by path — this is gone, this is
now that. The deliverer finds them with `git diff -M` between the
run's pin and the staging; the run cannot, because it cannot
resolve the pin. A rename in the delivery is a delete and an add,
and the note says both halves.

**The note.** What changed since the run's pin, stated so the run
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
   unanswered, which means it was made after we last read, and it
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

**One rule for every shipped skill and rule.** There are not two.
*Finding, checked side by side 2026-09-25: today it is written twice
— once for conventions inside the receiver's protocol, once for the
method skills in a file run 3 wrote itself. Six elements are the
same rule in different words. Run 3's is the superset: it alone
puts the pin and the never-edited concept in one place, states a
priority when edits stack — behind the source is acceptable, behind
this run's own lessons is not — and covers a skill the run has
finished with. Ours alone carries a "provisional" clause that
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

**A copy the run has finished with is edited the same way.** One
process for every copy. The one difference is said in the log
entry: a running skill's fix is exercised by the next step here; a
finished skill's fix is first used by the deliverer.

**Edits made before a verdict arrives stack on the run's side
only.** Behind the deliverer is acceptable; behind the run's own
lessons is not.

One word for the other side, in the rule and in the backlog line:
*deliverer*. Run 3's text says *source*; `master.md` says
deliverer, and the shipped rule says one thing.

**A run does not rename or delete a copy.** The delivered path is
the copy's identity for the take: a renamed copy becomes two files
at the next delivery, a deleted one comes back. A copy the run has
no use for is a backlog line — *we do not use this* — and the
deliverer decides.

**The concept is never edited.** A chapter is not run, so nothing
in it can fail a step. A lesson about the concept is a prose
hand-off in the backlog line, and it reaches the chapter, if it
does, from our side.

**The records are the run's own from birth.** `PLAN`, `TODO`, the
devlog, the entry file: delivered once as stubs and never again.
They are not copies and this section does not apply to them.

## 6. Up

**The read.** We open the run's repository and read three things
since the read point: its decisions log (every edit and why), its
backlog (every line addressed to us), and the diff of every held
copy against its pin. Nothing else is required; the devlog is
context.

**A file the run wrote is the run's own until the run offers it.**
It appears in the diff against the pin as an addition, and it is
read only if a backlog line points at it — a shape, a rule, a
reference the run thinks any project would want. Then it gets a
verdict like an edit does. That is how a run's rule for editing
copies reached this document.

**The read produces a reading, or extends the one open for that
run** — a document in `temp/` listing every edit, every ask and
every finding, one line each, revised as items close and deleted
when the work does. One per run at a time. The reading is the
list; working it is ordinary work here — a commit plan when it
takes more than one commit, an ADR when a decision has rejected
options — and the exchange says nothing about how, only what each
item must end as, and where.

**Verdicts.** Each item leaves the list with one of three:

- **Taken** — a master changes here, committed. The next delivery
  carries it, and the run's edit is absorbed rather than
  overwritten.
- **Declined** — with why, and the why is never "the description
  says otherwise". A description can be what the run has found
  wrong. Declined means: not general, or not worth the change. The
  why goes in the note and nowhere else; nothing in our tree moves.
- **Held** — with the trigger that would settle it, and a line in
  our own backlog so it is not lost between readings.

An unverifiable promise is worse than any of the three. The note
carries all of them, in the run's order.

**Every read ends with a note, even an empty one.** The note names
the run's commit we read through; the run records it beside the pin
(§2). A read that finds nothing addressed to us still sends *read
through `<commit>`, nothing to answer, no files* — one line each
side — so the run always holds the latest read-through, and can see
for itself when a hand-off was seen and not yet answered.

**Verdicts travel in the note.** There is no other channel. A note
alone, with no files, is still a delivery: the read-through moves,
the pin does not.

---

## What exists today, and what this replaces

| today | where | what happens to it |
|---|---|---|
| `convention-lifecycle` skill, 154 lines | ours, and shipped | replaced by §4–§5 as the run's half; deleted here |
| `skills-changed-in-place.md`, run 3's own | run 3 | replaced by `delivered-copies.md`, derived from it and shipped; the note names the rename |
| `bundle-update.md`, 527 lines | `delivery/installs/` | replaced by §3 and §6 as our half; the lessons list it never had is what §3–§6 are |
| the harvest section of `delivery/README.md` | ours | folds into §6 |
| the entry-file line "never edited in place" | shipped | contradicts §5; goes |
| `delivery/method/` and `delivery/spring-postgres/` laid out flat | ours | each becomes a piece of the run's tree, §3; two `git mv` per skill |
| the file lists inside `bundle-update.md`'s scripts | ours | gone with the mapping; a group is a directory name |
| the line-6 derivation comments in eight skills | shipped | become the one frontmatter field, §3 |
| `master.md` §2.5 and §3 | ours | stay; this is their detail |

## What this is made usable as

**The exchange is a convention**: this document is its manual, which
never ships, and four artifacts are what a repo actually holds. It
replaces `convention-lifecycle`, which was a convention, with one —
and it is the first whose artifacts split between the two
arrangements in `master.md` §4, each side holding only what it does.
This manual is at `docs/conventions/exchange/`. *Intended: the
artifacts' homes are named below and are not yet true.*

- **`delivered-copies.md` — a rule, the run's, shipped** in the
  container at `.claude/rules/`. §4 and §5. A rule rather than a
  skill because its moment is a path being touched: a copy, or a
  file in `temp/`. It loads when the moment arrives instead of
  waiting to be opened by name — the failure the receiver's protocol
  had since the day it shipped.
- **`exchange-read` — a skill, ours**, in this repo's `.claude/skills/`. §6:
  find the span from the run's read-through, read the three things,
  write the reading. Ends where the work begins.
- **`exchange-deliver` — a skill, ours**, beside it. §3: the note committed
  last, the staging on the word; the same whether a reading preceded
  it or not. Birth is a delivery into the root plus the fills, and
  `pure-seed.md` keeps that.
- **The reading's shape — ours**, in `.claude/rules/` with a
  `paths:` line or in `.claude/shapes/`, undecided. What `exchange-read`
  writes, and what the work then fills, to one form.

Between read and deliver is work, not procedure. How this repo
works a reading is arrangement, not exchange, and lives with the
standing rules once it has run twice.

The description stays here, once. No artifact explains anything;
all four point at this.

*Does the name hold? Every section is about something passing
between two repos. Nothing in it is about versions except one
number. It held.*
