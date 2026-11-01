---
paths:
  - ".claude/skills/**"
  - ".claude/rules/**"
  - ".claude/shapes/**"
  - ".claude/approaches-on-trial/**"
  - "docs/concept/**"
  - "temp/**"
foundation: the exchange convention
---

# Delivered copies: pinned, edited in place, re-pinned

<!-- What this CBC Run holds from its Concept Deliverer, and what it may do to
     it. The Concept Deliverer's side of the same exchange is not here; the
     CBC Run never needs it. -->

1. **Every file delivered here is a copy pinned at the Concept Deliverer's
   commit.** The Decisions Log's last delivery entry carries two
   numbers:
   - the **Delivery Pin:** the Concept Deliverer's commit these copies equal, but for
     its *Decisions* footers, taken from the Delivery Staging's name;
   - the **Read-Through Commit:** this CBC Run's own commit the Concept Deliverer last
     read up to, taken from the Delivery Note.

   One Delivery Pin covers everything delivered: the Agent Skills, Agent Rules, Output Shapes
   and Approaches on Trial under `.claude/`, `docs/concept/`, and the
   delivered Glossary Names in `docs/glossary/`. The concept chapters are
   copies too. The records (`PLAN`, `TODO`,
   the devlog, the glossary) were delivered once as Record Stubs, and the Entry File
   and `README.md` were composed once. All of them are this CBC Run's own, not copies, and
   this file does not govern them.

   A copy arrives without the Concept Deliverer's *Decisions* footer:
   the decisions it rests on are the Concept Deliverer's, and this CBC
   Run cannot open them. To go against a copy, quote the line you
   disagree with under *To the deliverer*.

   **A copy is never renamed or deleted here.** Its delivered path
   is its identity for the Delivery Take. A renamed copy becomes two files at
   the next delivery, and a deleted one comes back. A copy this CBC Run
   has no use for gets a CBC Run Ask under *To the deliverer*: *we do not
   use this*. The Concept Deliverer decides.

2. **A copy may be edited in place during a Plan Step when all three
   hold:**
   - something happened in this project that the copy did not
     foresee, never a speculation;
   - the edit asks a question or demands an outcome any project
     would want, never this project's answer, never anything
     project-specific;
   - one entry goes in `.claude/decisions.md` per edit, or per copy
     per Plan Step, saying what changed, which Plan Step found it, and why.

   Nothing is written into the copy but the edit itself. A comment
   in an artifact says how to use it or what a part is, never what
   changed: that is history, and the diff against the Delivery Pin and the
   Decisions Log already hold it.

   A concept chapter is edited only from a mistake lived here:
   Agent Skills are written from the chapters and readers learn the method
   from them, so lived work can show one wrong. A preference for
   other wording is never the reason.

   An Approach on Trial takes one more edit: a dated note of each
   use under its *Uses*, in this project's own terms. It is how the
   use reaches the Concept Deliverer, so the second condition does not hold
   it; the other two do.

3. **What this project needs that no copy should carry goes into
   the project's records,** where that kind of thing already lives:
   a Plan Step Gate item in PLAN, an ADR, an Invariant Slice Record, the Entry File. The
   copy stays general.

4. **At every Plan Step's close, the CBC Run Asks.** One TODO line per edited
   copy: "Concept Deliverer: evaluate this CBC Run's changes to `<copy>` since
   `<Delivery Pin>`". The lines go under one heading kept for the purpose,
   `## To the deliverer`. A rewrite of another section then cannot
   take them. The Concept Deliverer reads one section instead of the whole
   backlog. A copy edited after this CBC Run finished with it (rule 7)
   adds "— untried here: written from this CBC Run's evidence, never
   run", so the Concept Deliverer reads those hunks most carefully.

   The CBC Run Ask is the request. Without it, the Concept Deliverer finds a
   changed file and must guess. The edits describe themselves in the
   diff and the Decisions Log.

   The Concept Deliverer's reply gives each hunk one verdict: taken,
   declined or held. The CBC Run Ask is done at the Delivery Take
   (rule 5).

5. **After the reply, the re-pin: the Delivery Take.** The Concept Deliverer's new
   version arrives as a Delivery Staging in this repo's own `temp/`, a directory
   named for the hash, with the Delivery Note beside it. **Nothing in `temp/`
   is in force until it is copied into place.** A staged Agent Skill is a
   file, not an Agent Skill, and a Plan Step that opens meanwhile runs on the held
   copy.

   In this order, before anything moves:
   1. **Check the Delivery Note against the Delivery Staging.** Diff every delivered
      file against what this CBC Run holds. The Delivery Note says how many
      differ, and the diff says how many. A mismatch is reported
      first.
   2. **Find this CBC Run's own edits.** Diff each held copy against the
      last delivery entry's commit, and read the Delivery Note's verdict on
      each.
   3. **An edit with no verdict was made after the Read-Through Commit the
      Delivery Note names.** The copy lands whole, and that edit is re-applied
      on top. Its Decisions Log entry and its CBC Run Ask stand until a later
      Delivery Note answers the edit. If the edit was made to a path the Delivery Note
      names as gone, there is no copy to land on, and nothing is
      re-applied. The Decisions Log entry and the CBC Run Ask stand, the diff is
      in this CBC Run's history, and the next Delivery Note answers them.
   4. **Copy whole.**
   5. **Remove what the Delivery Note says is gone.** Each path it names as
      deleted is deleted, and each it names as renamed is moved. A
      copy cannot carry an absence, so the Delivery Note carries it and this
      step does it.
   6. **Write one Decisions Log entry** carrying both numbers: the new
      Delivery Pin, and the Read-Through Commit the Delivery Note names. The copy is pristine
      again, and the CBC Run Ask leaves with the Delivery Pin.
   7. **Remove the Delivery Staging,** the directory named for the hash and
      its Delivery Note, and nothing else. `temp/` may hold the project's own
      drafts, which are not the delivery's to clear.

   The Delivery Take's commits follow `.claude/skills/commit-messages/`. When
   there is more than one, the chapters' commit comes first, and the
   entry goes in the last, where every copy equals the Delivery Pin. A
   declined edit is gone with the re-pin, and never edited back in.
   If the project still needs what was declined, that need goes into
   the records under rule 3, and the Decisions Log entry says so.

   **A Delivery Note may arrive alone,** with no files: *read through
   `<commit>`, nothing to answer.* The entry records the
   Read-Through Commit, the Delivery Pin does not move, and nothing else happens.

6. **If a Plan Step opens before the reply,** work continues on the
   edited copy, and edits keep landing under rule 2. They stack on
   this side only. The Concept Deliverer diffs against the Delivery Pin either way,
   and the re-pin still lands whole. Being behind the Concept Deliverer is
   acceptable. Being behind this CBC Run's own lessons is not.

7. **A copy this project has finished with is edited the same way,
   whenever the evidence is here.** It is never kept as a note for a
   later CBC Run, for three reasons:
   - a restarted Plan Step may re-run on it;
   - the Concept Deliverer takes or declines an exact hunk, not a translated
     note;
   - one process serves every copy.

   The one difference: the problem was lived either way, but a
   finished copy's fix is never used by a later Plan Step here. A running
   Agent Skill's fix is exercised by the next Plan Step. A finished Agent Skill's fix
   is first used by the Concept Deliverer. Say so in the Decisions Log entry, and in its
   CBC Run Ask (rule 4).

8. **An Agent Skill Template is copied and filled, never edited in
   place.** At use, copy it to the path its Agent Skill names and fill
   it. The filled file is this project's own, and may drop the
   Agent Skill Template's header. The Agent Skill Template stays a pinned copy: a change to
   it, such as a line every project needs, is an edit to the
   copy under rule 2. Filled values never go back to the Concept Deliverer
   (CBC `docs/conventions/exchange/` §5.8, *Agent Skill Templates*).

   When this project's decided constraints differ from what a
   Agent Skill Template assumes, it is off-template:
   - derive from what the Agent Skill Template implements, which its
     Agent Skill names;
   - record the deviation where the records table puts a decision,
     what was done instead and why (`.claude/CLAUDE.md`, *Records*);
   - expect it to come back as a change to the Agent Skill;
   - never bend a decided constraint to fit an Agent Skill Template.

The Delivery Pin says where a copy came from. The Decisions Log says why it changed. The diff
between the Delivery Pin and the copy is the whole of what this CBC Run changed,
and that is what the Concept Deliverer reads.

---

## Decisions

- ADR-0008 — rule 8: an Agent Skill Template is copied and filled
- ADR-0036 — the Exchange Convention. This Agent Rule is the CBC Run's half of it,
  built from the seven rules CBC Run 3 wrote for its own method
  Agent Skills and widened to every delivered copy; the Delivery Pin and the
  Read-Through Commit; what a copy cannot carry; the check at the Delivery Take
- ADR-0046 — rule 5: the Delivery Take's commits, the chapters first and
  the entry in the last
