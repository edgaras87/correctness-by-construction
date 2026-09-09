# Reply from the handbook — 2026-09-08

<!-- Staging copy, tracked in temp/ while it is absorbed; deleted
     once it has served, with the handoff it answers. Substance is on
     record in the handbook: ADR-0035, ADR-0036, PLAN Step 26,
     devlog (ap), and CHANGELOG under Unreleased. -->

To the concepts tier, answering the 2026-09-08 handoff. Everything
below is on record in the handbook from `f3f6448` on; the kit pin is
the handbook's HEAD at the moment you read, since the kit's stub
changed once more after that hash (below). Two things first: the earlier asks (ADR-0031 through 0034,
which you read at `c670fe5`) are absorbed on our side and nothing
further is owed on them; and a test we ran for your §3 found
something that touches your own entry file, at the end.

## On §1: yes to all three, one frame corrected

**The pace.** Taken, and moved rather than copied. It is now the
first rule of thumb in commit-messages — stage, show the reviewer
the diff, commit only on their word, one commit at a time, no push
without the same word — and change-plans §6 keeps its why and
points at it. Same reasoning that put the `agent` scope in
commit-messages: the discipline binds at the commit, so its text
lives where the commit moment fires (ADR-0019 decision 3,
ADR-0035 decision 3).

**The gate.** Taken as you proposed, and it is the first gate in the
system. The model's §7 names the tool's permission prompt among the
gate kinds; §10's binding lists permission rules in the gate row. We
verified the holes so they are on record rather than discovered: the
rule matches by prefix, so `git -C … commit` and a commit inside a
script pass it; a permission mode that bypasses prompts skips it;
and the prompt shows the command, not the diff. So the sentence
carries "show the diff" and the gate carries "stop", and run 3
should watch which of the two fails first and in which direction
(claim U1).

**Ownership.** Taken as a note in §4, but not as a form of told.
`CLAUDE.local.md` fires at session start, is paid every session, and
is present without being obeyed — every property of ambient. What
differs is the owner, so §4's ambient entry now says whose a text
is, and that an operator's file never enters records. One thing we
added beside it, as an agent-arrangement §4 anti-pattern: that file
is exactly where a rule the human keeps repeating gets parked
instead of becoming a convention, which makes the saying persistent
and the §8 diagnosis invisible. Also corrected in passing: the
harness does not ignore the file on its own; its init flow adds the
line to `.gitignore`. The hygiene base now owns that line.

## On §2: yours stands; ours waits

Your move is a permitted shape. Agent-arrangement §2's Where now
says root or under `.claude/`, read as one file, and that a project
may take the second so every agent-side path sits in one directory.
The handbook did not take it for itself, on the test below: the
move gains nothing mechanical, nothing recorded forbids it, and
tidiness alone did not earn a change set. ADR-0035 decision 5 names
run 3's retrospective as the next reading.

## On §3: wait

Same reason. The kit's stub stays at root and the pure seed keeps
delivering it there. Your run 3 trial is the evidence; its Step 1
reading and the retrospective decide.

## On §4: the settings file yes, the local file's shape no

**`.claude/settings.json`** ships in the kit at the new pin, tracked,
with the one `ask` rule and nothing else. Its why is in ADR-0035 and
agent-arrangement §3; the birth entry's "see the handbook's ADRs"
covers a born project. The kit's file does not carry the exclude
mentioned below; a born project has nothing to exclude.

**`CLAUDE.local.md`**: the gitignore line is taken into the hygiene
base. The shipped shape with the pace as its content is not, for
three reasons on record in ADR-0035 option 5: it would be a third
text for one rule; the operator's file would carry the project's
rule, which your own ownership point argues against; and it is the
parking place described above. Trial it in your checkout as planned
and bring the reading. If the gate plus the sentence hold, the local
copy is dead weight; if they do not, it is a told band-aid, and that
is the evidence we want.

## The finding: comments in the entry file are not ambient

We ran your §3 as a test before deciding it: two scratch clones of
the handbook, the kit stub at each address, a fresh session told to
read one file under the kit and report its context. The stub loaded
at both addresses, which is why §3 waits. But in both runs the agent
could quote the stub's records table and denied seeing any of its
comment text. The loader confirms it: a memory file containing
`<!--` is parsed and every HTML-comment block is dropped before the
text enters context, on every installed version we have (2.1.260
through 2.1.263). ADR-0036 records it, with what it undid on our
side: the kit's TEMPLATE marker never reached an agent and is gone
with its `sed` line; ADR-0032's line-count argument was never paid;
the entry file's guard comments are read at edit time, which is the
moment they govern.

What it means for you:

- Every comment in your `.claude/CLAUDE.md`, including the template
  under it, is invisible at session start. Your entry file's ambient
  cost is its non-comment lines only, and any rule you put in a
  comment there reaches the agent only when it opens the file.
- If your tree keeps a template `CLAUDE.md` anywhere — your
  `starter/` directory is the place to check — it loads as nested
  memory when work touches that directory, without its warning. The
  fix is one settings key, `claudeMdExcludes`, a list of globs
  matched against the absolute path, so the pattern needs a leading
  `**/`. The handbook's own settings file carries it for
  `starter/kit/**`.
- Check the version in your run's harness before relying on either
  fact. The model's §10 states the versions observed.

## After the reply was written, same day

Two more things, both from checking `.claude/rules/` — a directory
the harness reads that the model did not know. A rules file without
frontmatter is the entry file by another name; one with a `paths:`
list loads only when the agent touches a file under those paths,
the tool deciding — pushed with no hook, keyed on a place and never
an action. Model §10 has it; agent-arrangement §2 and §3 name it as
a fourth home for a rule with a moment, and the kit stub's guard
comment names it too, since the model never reaches a project. And
the guard's passing example — a generated directory — is gone from
the stub and the convention: a rules file now delivers that fact at
its moment, so it no longer passes the third test. Nothing replaces
it; the maintainer's reason is that an example in a convention
steers what the agent reaches for. If your template under
`.claude/CLAUDE.md` carries the same example, the same argument
applies.

Also withdrawn, in the handbook only: the commit `ask` rule. Run
under it for eleven commits, it asked for a word the reviewer had
already given in chat, twice on the path where the prompt is
declined to read the staged diff first. The kit keeps it as the born
default; your run 3 reading decides whether a born project sees the
same. ADR-0035 carries the note.

## The next day, 2026-09-09: §2 and §3 read together

The maintainer's reading of your move: the address can carry a
distinction the tree states nowhere else. A repo whose subject is
the arrangement — this one, yours — keeps the entry file at the
root. A repo that builds an app puts it under `.claude/`, so the
tracked root is the project's truth and one directory holds
everything the agent owns; ADR-0019's commit split becomes `.claude`
plus `CHANGE-PLAN.md`. ADR-0020 already draws that line for the
decisions log; this extends it to the address.

Nothing in the handbook has to change for the bundle to do it.
Agent-arrangement §2 permits either address, so a bundle install
that moves the stub into `.claude/` is inside the convention as
written — and it is exactly the evidence ADR-0035 decision 5 waits
for: run 3 lives under `.claude/`, the retrospective says what the
clean root bought, and the kit's stub moves on that reading or
stays. Three things to hold while trialing it:

- Until the kit moves, the address says "installed by the bundle",
  not "an app repo": a project born from the pure seed still has
  the stub at root. Fine for a trial; if the shape proves out, the
  end state is the kit shipping the stub under `.claude/` and the
  bundle's step going away.
- A move at install time is one install step. The last one — the
  `sed` line — went because it protected no one. This one names
  what the clean root bought at the retrospective, or goes the
  same way.
- The operator's file does not follow. The harness installed here
  today (2.1.266) reads `CLAUDE.local.md` at the project root and
  ancestor directories only; the second address exists for the
  checked-in entry file alone. An app repo's working tree keeps
  that one file at root, untracked and ignored. The tracked root is
  clean; the working tree is not quite. §10 takes the line once the
  move is a shape in use.

§3's answer stands: the kit's stub stays at root until the reading.

## What moved since your pins

From `f3f6448` to HEAD, against your registry: commit-messages and
change-plans (the pace, today), agent-arrangement (§2 Where and size
rule, §3's two files, §4's anti-pattern — today, on top of the
09-04 changes), repo-hygiene's base (one line, today), the agent
model (§4, §7, §10, today), and the kit (settings file added, marker
gone, hygiene line, the skill copies of the two conventions, the
stub's guard comment). Your §8 compare handles the rest.

**Run 3, specifically.** It holds the kit at c670fe5, before all of
today. Its first §8 update, across the settings file, the marker's
removal, the hygiene line, the two skill copies and the stub's guard
line, will be the first update anywhere to carry an entry-file
comment — the test agent-arrangement's Delivery has waited for. We
are rewriting §8's installed paragraph from your 09-03 run now, so
that update reads the refined text. Its receipt branch is a compare
mechanism §8 does not have; if the update uses it, say how it went.

Nothing here blocks run 3.
