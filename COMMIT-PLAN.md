# Commit plan: round 2's layer 2, a record's form holds its how

## Summary — the state after all commits

The second of layer 2's three commit plans. It applies the
refinement's DECISION-11 (c) to every record: a record's form is
the home of how the record is kept, and project-recording says what
the record is and why (`temp/refinement-2026-10-18.md`, *Round 2*).
It fixes FINDING-144 and works TODO's Now item, "Read each record's
*How* in project-recording against that record's form".

- **Each *How* section,** §2.4, §3.4, §4.4, §5.4, §6.4, §7.4, §8.4
  and §9.4, keeps what the form is for and why its rules are as
  they are, and names where each seat's form lives. The steps and
  the code-block examples leave: the stub is the live example.
- **A how-rule only the manual held** moves into the form, in each
  seat that keeps the record: a gate's items are verifiable facts;
  a closed step becomes one line naming its commit; a devlog entry
  is tagged with its step; "Discovered along the way" is triaged
  into TODO; breaking changes drive the major version; the README's
  decisions row declares the tag. The full list is known only once
  each record is read line by line.
- **The deliverer's seat** says what a step is and why, and where
  its form lives, and no longer retells the step form (FINDING-144).
- **Our ADRs have a form:** `docs/adr/README.md`, its header
  comment holding the template's rules and a `foundation` line, as
  `devlog/README.md` does for the devlog.
- **The README form carries a `foundation` line** in both seats
  (`docs/conventions/conventions/` §1.3).
- **"Shape" no longer names a form:** both TODO forms say "one
  form", and conventions §1.3 says "`TODO.md`'s item form".
  *The words* defines "form" and "shape", each pointing at
  `docs/models/idea-to-output.md` §2.
- TODO's Now item goes, and conversation-memory §20 with it. The
  refinement's file names FINDING-144's commits.

## Commits

**0. `docs(agent): add commit plan for record forms`**
Opens the set.

**1–8. One record at a time, in the manual's order: PLAN, ADR,
devlog, TODO, CHANGELOG, README, ARCHITECTURE, the playbook.**
Each record is up to two commits:

- **a. `fix(delivery): the <record> stub takes its how`**, the
  shipped master first, when a how-rule only the manual held moves
  into it. Skipped when the stub already holds every rule.
- **b. `docs: <record>'s how lives in its form`**: our form takes
  the same rules where our seat keeps them, and the manual's *How*
  section is rewritten to what the form is for, why, and where each
  seat's form lives.

Provisional: each record's split and wording is settled at its
boundary, once its lines are read against both forms. Text the two
seats' forms share is noted for "Decide whether each seat's copy is
written for its seat", not changed. The rest by record:

- **1, PLAN:** also the deliverer's seat (FINDING-144), and §2.4's
  "the playbook's" named by path.
- **2, ADR:** 2b also creates `docs/adr/README.md`. §3.5, the tag,
  stays: what a number means, not how an ADR is written.
- **3, devlog:** `devlog/README.md` points at project-recording
  §5.4 for when a TODO item's story is written; that rule's home
  becomes TODO's form, and the pointer follows it.
- **4, TODO:** both forms say "one form", not "one shape". The
  five rules §5.4 alone holds move in; its two dated italics stay
  as lessons.
- **5, CHANGELOG:** ours versions the concept, so only the run's
  stub may take the major-version rule.
- **6, README:** both forms gain a `foundation` line. The tag row
  is §7.4's and §3.5's; the form takes the row, §3.5 keeps the tag.
- **7, ARCHITECTURE:** §8.4's dated italic stays as a lesson.
- **8, the playbook:** its form is
  `delivery/fills/cbc-run-pure-playbook.md`, ours only. §9.4's
  lifecycle is read for what is how and what is what, at its
  boundary.

**9. `docs: conventions §1.3 says item form`**
One word, the example of a record's form.

**10. `docs: The words define form and shape`**
Two entries in `ARCHITECTURE.md`. A form: how an output is
written, read while it is written, its rules and its layout
together; a record's sits in the record, and a manual's and a
reading's are rules today, whose future is TODO's "Decide whether
our own forms become shapes". A shape: pointing at
`docs/conventions/shapes/`.

**11. `docs: round 2's layer 2 forms are worked`**
The records commit. The refinement's file: FINDING-144 names its
commits. TODO: the Now item goes, each Idea weighed. Conversation-
memory §20 goes with it (`docs/conventions/project-recording/`
§14).

**12. `docs(agent): close commit plan for record forms`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **A, B and C, as taken on 2026-10-26:** *How* keeps the what and
  why and names each seat's form, examples cut; `docs/adr/README.md`
  holds our ADR form; one plan, one record at a time.
- **Placing, not rewording.** Each fact goes to its home; the
  manual's remaining text keeps its words. Rewording it into a
  describing voice is round 3's (conversation-memory §20).
- **No fact reference from a form to the manual's why.** That is
  DECISION-10's question, in "Decide how a fact reference is
  written".
- **A live run keeps the forms it was born with.** Records go once,
  at birth (`docs/conventions/exchange/` §2.4), so the stubs'
  changes reach future runs only. Run 5's forms do not change.
- **No ADR.** DECISION-11 already decided where each fact lives.
