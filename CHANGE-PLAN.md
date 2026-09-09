# Change-plan: absorb the 2026-09-08 reply and the checkout handoff (handbook @ af16eb7)

## Summary — the state after all commits

The handbook's reply and its checkout-review handoff are absorbed.
This repo holds seven conventions, all @ af16eb7: the four skill
copies and the agent model already moved (6dc8b23, landed before
this plan opened — the pinned-copy half is skill delivery, one
commit by §8 step 5; the rest is what needed a plan); the seventh,
agent-arrangement, is injected by its installed path — the kit
stub's comments replace the entry file's older ones, the
Conventions section goes, since the registry is the project's only
list (their ADR-0034), and the entry file returns to the root: the
handbook's 09-09 reading gives the address a meaning — root for a
repo whose subject is the arrangement, `.claude/` for one that
builds an app — and this repo is the first kind; project-recording and repo-hygiene are
updated by the same path, their changed comment text carried into
the living records project-side. The bundle's fills follow the kit
stub at the new pin, and the handoff's §2 question is answered in
the templates. Run 3's pre-briefing prompt is rewritten around the
kit update it now needs first. The §8 friction from this pass
(handbook citations and exemplars that do not survive a copy; a
requires chain that can name a convention a repo was born without)
queues in TODO for the next handoff, with the run 3 update report
the reply asked for. The three served drafts are deleted from
temp/, logged in the devlog.

## Commits

**0. `chore(agent): update pinned copies to the handbook @ af16eb7`**
Already landed as 6dc8b23. Named here so the set reads whole; its
registry entry's five findings are this plan's work list.

**1. `docs(agent): add change-plan for the af16eb7 absorption`**
This plan.

**2. `chore(agent): inject agent-arrangement @ af16eb7`**
The chain member convention-lifecycle now requires and this repo
never received (born at 4fe8083, before it existed). Installed
delivery through `.claude/CLAUDE.md`: the kit stub's three comments
at af16eb7 replace ours — the records-table comment, the three-tests
guard (rules directory named, the generated-directory example gone)
in place of the SIZE BUDGET comment — and the Conventions section
and its comment leave: the registry is the only list a project keeps
(their ADR-0034). Content lines untouched. The file moves back to
the root, `git mv`, undoing the 09-07 trial: the address now carries
a distinction (their 09-09 reading), this repo is an arrangement
repo, and run 3 — an app repo — keeps its trial of the other
address. The codemap row follows in commit 3. No
`.claude/settings.json`: the commit ask rule is run 3's trial and
the handbook withdrew it for itself; and nothing under starter/
leaks — the bundle's skills sit outside `.claude/skills/` and never
load (this session's skill list is the four kit copies), and no
file named `CLAUDE.md` exists there, so `claudeMdExcludes` has
nothing to exclude. Registry entry names both as rejected, records
the move back with the 09-07 entry superseded, and carries the
comments finding as it applies here: every comment in the entry
file is edit-time text, so the guard governs edits and costs no
session. One commit: `.claude/decisions.md`, `.claude/CLAUDE.md`
→ `CLAUDE.md`.

**3. `docs: carry the stubs' changed comments into the records`**
The installed compare, kit stub against kit stub, f9371e4..af16eb7
for project-recording and 4fe8083..af16eb7 for repo-hygiene, per the
"Shipped conventions" table. Carries, verified at drafting:
README's closing comment (rewritten: a line here is true now, for
someone arriving from outside); TODO's header comment (triage when
closing a step; the inline rule says "anywhere in the work");
devlog's split-file line (`<YYYY-MM>`); CHANGELOG's comment already
says "lands" — nothing; PLAN's retrospective list gains item 6 (the
entry file re-read against its three tests) and its fold-back line
names the playbook the steps came from; `.gitignore` gains the
hygiene base's two changes — the settings comment's "(if any)"
dropped, the operator's-file block added; ARCHITECTURE's codemap
row follows the entry file back to the root. Not carried: PLAN's birth-
shape comments (nothing retrofits into a living plan, the 09-03
reading) and the kit's ADR-0001 context wording — ours is an
accepted record, not a stub. Project-side only.

**4. `chore(agent): register project-recording and repo-hygiene @ af16eb7`**
Two registry entries, the product of the installed update (§8 step
4, the new text). Both name commit 3 as where the carries landed.

**5. `docs(starter): recompose the fills from the kit @ af16eb7`**
`claude-md-template.md`: the guard comment follows the stub (rules
directory line in, generated-directory example out — the handbook's
argument that an example in a convention steers what the agent
reaches for applies to the template verbatim). `pure-seed.md`: the
TEMPLATE-marker lines go (the marker no longer exists; the kit half
runs pure.md by pointer, so the kit's settings file now rides in);
the Step 0 reading text that names the marker stripped is corrected.
Handoff §2, decided below: one row for `docs/system/` in both
templates' records tables — the moment "the promise, the layers, or
the slices are in question", holding the intent, the system
definition, and the slice registry — the way the ADR row covers a
directory. The README template's kit half is unchanged since
c670fe5 (verified) — the row only. Not in this commit: moving the stub to `.claude/` at
install (run 3's trial; folds on its reading, their decision 5).

**6. `docs(temp): rewrite the pre-briefing prompt for run 3`**
Run 3 holds the kit at c670fe5 and took only the branch rule of the
four (its log: PLAN rule, decisions entry, gate item; no settings
file, no local file, CLAUDE.md at root). The prompt now opens with
the kit update — its own convention-lifecycle §8 against the
handbook's HEAD, the receipt branch as the compare if the agent
reaches for it — which brings the settings file and the gitignore
line; item 2 goes (the kit delivers it); items 3 and 4 stay as
trials, the local file staying at root after the move (the harness
reads it there only). Citation trap holds: no hash, path, or
vocabulary of this repo; the handbook's HEAD is named as "the kit's
source, at its current commit" — the run's agent does not read the
source repos, so the update payload is delivered the way the seed
was, by the user. Provisional: the delivery shape of the payload is
decided at this boundary.

**7. `docs: close records for the af16eb7 absorption`**
TODO — the 09-08 handoff item closes (replied, absorbed); a new
handoff item queues the §8 friction (citations and exemplars written
from the handbook's seat, the chain naming a convention a pre-
arrangement repo was born without, and — after it runs — how run
3's update went, which the reply asked for); the gates-experiment
item gains two evidence notes from the checkout handoff (§3 the
delegated mode needed a record and no gate; §1 the eight lessons
all sit in the frozen baseline v2, absent from the live fill by the
experiment's design — nothing to add, the readings decide); the
run 3 pre-briefing note says what changed. Devlog entry with
Resume. CHANGELOG Unreleased: the templates' `docs/system/` row and the
guard comment (Changed). Walked and cleared: ARCHITECTURE (the
codemap row moves in commit 3; no shape change beyond it), PLAN
(no project ADR — see decisions below).

**8. `docs(temp): delete the served drafts`**
The 09-08 handoff, its reply, and the 09-09 handoff, all served:
their substance is in the registry entries, the records, and TODO.
Tracked since 09-07, so a deletion is a commit of its own,
project-side, before the close.

**9. `docs(agent): close change-plan for the af16eb7 absorption`**
Deletes this file; body is the retro, including that commit 0 ran
before the plan opened.

## Decisions taken inside this plan

- **Commit 0 stands outside the plan, named, not hidden.** The
  pinned-copy update is one-commit skill delivery and needed none;
  what it found is what needed the plan. The close body says so
  rather than re-dating the agreement.
- **Agent-arrangement is injected, not deferred.** §8 step 2 makes
  chain currency a requirement, and the same pass checks a newly
  required member; here the member is absent, and the fix is the
  same installed compare the other two conventions get.
- **The Conventions section leaves the entry file.** Their
  ADR-0034: the registry is the one list; the entry file's rows are
  moments, and a convention's presence is not one. Our list was the
  birth stub's; the skills load themselves, so nothing depends on
  it.
- **The entry file returns to the root.** The 09-07 move was a
  trial of the shape; the handbook's 09-09 reading gave the address
  a meaning, and under it this repo — a concept repo, subject the
  arrangement — belongs at the root, an app repo under `.claude/`.
  Run 3 is the app repo and keeps the trial; ours ends with the
  reading that answered it.
- **No settings file, no exclude key.** The ask rule is on trial in
  run 3 and withdrawn at the handbook. The bundle needs no exclude:
  the harness loads skills only from `.claude/skills/` and memory
  only from files named `CLAUDE.md`, and starter/ has neither.
  Both revisited on run 3's reading.
- **Handoff §2: one row.** The method's three artifacts are records
  by the project's own description; the table is the one place that
  says when to open what, and run 3 already planned a row for the
  directory. One row for `docs/system/`, naming the three files,
  as the ADR row covers its directory. Recorded in the commit body
  and CHANGELOG; no ADR, since it applies the kit's stated rule
  rather than deciding method.
- **Citations and exemplars are raised, not repaired.** Pinned
  copies stay verbatim (§8 step 6: friction goes up, never a side
  effect of the landing).
- **No project ADR.** Every decision is arrangement (registry) or
  applies an upstream decision (their ADR-0034, 0035, 0036, and the
  stub changes).
