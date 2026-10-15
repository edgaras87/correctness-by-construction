# Message to run 4, 2026-10-15

<!-- A draft on its way to a run: the reviewer types it into run 4's
     session after pressing Escape. Written by the deliverer from run
     3's RETRO.md, D2 and D6, which run 4 cannot read, so the tag
     table is carried here whole. Deleted once run 4 has taken it and
     the devlog says so; git history keeps it. -->

```text
Stop Step 3 where it stands. Two things are wrong with the run so
far, and both are fixed before Ground goes on. This is the
reviewer's word, so it overrides L-05.

1. The tags. Every tag is written in full words, everywhere: the
   skills, rules, shapes, check script, concept chapters, PLAN,
   docs/run.md, docs/settled.md, and every record from now on.
   L-05 is reversed. You saw both forms and chose the short one
   because most of your tools spoke it. The tools were behind; fix
   the tools.

   Short    Full                     What it is
   F19      FACT-STORE-19            something the world does that
                                     can hurt us; the actor named
   A4, T4   ASSUMPTION-4             something taken as true, not
                                     defended
   W2       NOT-OURS-2               something that exists, which we
                                     neither own nor defend
   V5       SYSTEM-BOUNDARY-5        a boundary question, decided in
                                     or out
   P4       POSSESSION-4             something the system must own
   R3       REFUSED-3                something the system refuses to
                                     own
   kill 15  KILL-15                  one way the promise can break
   fold 1   FOLD-1                   a rule no danger attacks, folded
                                     into the first slice that needs it
   L1..L5   LAYER-1-ENVIRONMENT, LAYER-2-POSSESSION, LAYER-3-OWNER,
            LAYER-4-KILL, LAYER-5-BETWEEN-OWNERS
   SL-4     SLICE-4
   G1       GUARANTEE-1, outside its record SLICE-4 GUARANTEE-1
   E1       EVIDENCE-1, outside its record SLICE-4 EVIDENCE-1
   R5       READINESS-5 (the readiness check, not a refusal)
   V3       MIGRATION-V3 (a database migration)
   C1       CONSTRAINT-STORE-1

   The rules for any tag not in the table: capitals, the kind first,
   then a domain where it helps, then the number. One spelling
   everywhere, never short in one place and long in another. Numbers
   run once through a record. A number local to one record carries
   its owner outside it, owner first.

2. The voice. The intent reads plain. The definition, the registry,
   the decision log and the devlog do not. Examples from them:
   "F5 × P4 → ... nothing dies. Stopped by W5"; "that storm seen
   from inside"; "we die after recording"; decision log entries of
   40 words in one sentence. The writing rule forbids each of these.
   And the glossary says no word was coined, while a reader meets
   fold, fence, rider, flag, possession, verdict, concern,
   chosen-next and saturated with no definition anywhere. A word the
   method coined is still a coined word to the reader.

What must be true before Step 3 goes on:

- Every skill, rule, shape and concept chapter that names a tag uses
  the full-word form. Each is a Method fix, logged, with its line
  under TODO's "To the deliverer". The check script finds slices and
  every tag kind by the full-word form, and its path to
  apply-retrospective is right.
- PLAN's closing items, for every step from now on, include: new
  and changed text is read against .claude/rules/writing.md, and
  every coined word, the method's included, is in the glossary.
- The framing's records (intent, definition, registry, glossary,
  README) are rewritten in full-word tags and the plain voice, each
  by a dated revision entry. What they say does not change: the same
  facts, kills, slices and decisions. A step does this, with its own
  gate and branch, before Ground; its number and name are yours.
- Each kill keeps one worked example with real numbers.
- History keeps its words: the closed steps' gates, the devlog's
  entries, the decision log's entries up to now, the ADRs. From now
  on all of them are written in the new form.
- ADR-0003 on the ground branch is checked against the new tags
  before Step 3 resumes.

Log this message as one decision-log entry, kind Verdict, from the
reviewer. Then go on, on full auto, as before.
```
