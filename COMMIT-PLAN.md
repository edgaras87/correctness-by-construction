# Commit plan: give Change one home

## Summary — the state after all commits

Each fact of Change is written once, in the simulation,
`temp/common-ground/system-repo-change-simulation.md`, until the
change flow is done. The simulation's header and §1 say so: a part's
rules are its steps' *Chosen* and *Adapted Case* fields, and they move
out together at the Change idea's third step (`TODO.md`, the item
"Define the Change idea").

The problem file's §2.1 keeps its two headings, *What passes between
the repos* and *A System Repo's change*, each a short pointer: to the
layers document's §3.1 for the movements between the repos, and to
the simulation for the six parts, their rules and the cases. What it
said that the simulation lacked has moved into the simulation first.
The layers document's §3.2 keeps only its own columns, where each part
sits in the picture and which arrows each depth travels, and points at
the simulation for the rest.

The change flow then edits one file for every fact of Change.

## Commits

**1. `docs(agent): add commit plan for Change's home`**
This plan, agreed.

**2. `docs: PLAN ticks the opening of Change's home`**
The three opening items are true: the branch was cut at `385a684`,
the gate came before the work, the Work Approach is known.

**3. `docs: temp's simulation holds the facts of Change`**
The simulation's header, its opening paragraph and §1's second move
stop saying the rules live in the problem file. They say the
simulation holds the facts of Change until the change flow is done,
and where they go then. Ticks own item 1.

**4. `docs: temp's simulation takes what it cited`**
Before the problem file's block goes, the simulation takes what it
relied on there and does not yet say itself. With commit 3, it
repoints the simulation's 16 Fact References to the problem file's
§2.1, inside the simulation or at the layers document, all but the
one to *Narrowing, never shrinking*. What moves:
- the four questions themselves, into §5 (cited from *Judging a
  change read back*);
- the fixed order when work resumes, that a Copy keeps its Change,
  and that the instructions for taking an Update are taken first
  (cited from *An update*, in §3, §4, §5, §7 and §8);
- the Attention Note's rule, already in §3, its Fact Reference
  dropped;
- the other sources of the Common Ground Problem, into §2 (cited from
  *A System Repo's change*);
- from *A lesson for the idea above*, what fits §6 and is missing
  there: the lesson's first wording kept beside its rewording; each
  survey answer is "holds as it is", "must change" or "conflicts",
  and a conflict is input, never a veto.

**5. `docs: temp's problem points at the simulation`**
The problem file's rules, *Change* to *Take*, and the paragraphs on
the six parts and the cases, become a pointer to the simulation. The
commit body places each line taken out: already in the simulation,
moved in commit 4, kept elsewhere, or dropped as superseded. Fact
References to the cut sections are fixed in the same commit. Ticks
own items 2 and 3.

**6. `docs: temp's movements live in the layers doc`**
The problem file's table of three movements becomes a pointer to the
layers document's §3.1, which holds them, and more. Ticks own item 5.

**7. `docs: temp's layers §3.2 keeps its own columns`**
The layers document's §3.2 drops the columns and paragraph the
simulation holds: who does each part, each depth's highest layer, and
"how deep is how high". It keeps where each part sits in the picture
and the arrows each depth travels, and points at the simulation for
the rest. §3.3's Fact Reference for questions 3 and 4 moves to the
simulation. Ticks own item 4.

**8. `docs: TODO notes what Change's home found`** (provisional)
The findings this plan names below, written into TODO. Its wording
waits for what commits 4 to 7 find.

**9. `docs: PLAN ticks the close of Change's home`**
The rename sweep over Living Text, unwrapped (own item 6), then the
close items, each with its date and how it was checked.

**10. `docs(agent): close commit plan for Change's home`**
Deletes this file; the body records what diverged.

After the plan: main takes the branch by fast-forward, on the
reviewer's word, and one commit on main closes the Plan Step with its
devlog entry, as the Plan Step Form says.

## Decisions taken inside this plan

- **No rules section in the simulation.** The rules are the steps'
  *Chosen* and *Adapted Case* fields, as §1 already says they are read
  together. A rules section would be a second copy of them inside the
  same file. The rules are written out as rules once, at the move.
- **The movements live in the layers document's §3.1.** Its header
  names "how knowledge travels between the repos" as what that
  document adds, and its §3.1 holds every arrow, the problem file's
  three among them.
- **The two headings stay in the problem file,** as pointers. The
  frozen `between-repos-simulation.md` names *What passes between the
  repos* in its header, as where its findings go. Its body's quotes of
  *An update* are left as they are: it is frozen, and is read again
  when it resumes.
- **Where the problem file and the simulation disagree, the simulation
  stands,** being newer and judged by the layers model. One found: the
  problem file runs the survey "at the human's choice when the lesson
  is new"; the simulation's §6 asks every text, every time (`dd56eab`).
  The condition is dropped as superseded, and the commit body says so.
- ***Narrowing, never shrinking* stays in the problem file's §2.1,** under
  its own heading. It is a rule of the arrow *adapt*, not of Change,
  and the general document's §3.2 cites it. Found: it answers the
  general document's open question 3, *Where a skipped part is
  marked*, while that document lists it open. Commit 8 notes this.
- **The TODO item "Sweep the drafts for words that read as walking
  commits"** waits on "the problem file's rules are rewritten from the
  simulation", which will not happen now. Commit 8 rewrites its
  trigger: the facts of Change moved to their final home, when the
  sweep reads the final text.
- **Each commit fixes the Fact References it breaks;** commit 9's
  sweep only confirms. A miss it finds is an inserted commit, `8b`.
