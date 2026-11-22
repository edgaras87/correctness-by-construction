# How the update job's outcomes are shown, compared

<!-- A visual comparison's draft (.claude/skills/visual-comparison/SKILL.md).
     It settles how temp/common-ground/system-repo-change-flow.md §2 shows
     the second of the two jobs, an Update when work resumes. The
     outcome is recorded in the body of the commit that places it in
     the flow file, and this draft goes in that commit. -->

## 1. The defect

The flow file shows the update job only as the second box of *The two jobs*, and the Take in *The Take* (`temp/common-ground/system-repo-change-flow.md` §2). The old five cases drew an Update inside each Look for Lessons, and are gone. Two outcomes have no picture in Now: a Plan Step open, which stops the job, and a Take refused because main moved. The refused Take is drawn only in old picture 2 (`temp/common-ground/system-repo-change-flow-old-pictures.md`), from before the Take's check was settled.

## 2. What the reader must get

1. **U1, the outcomes:** five, and what decides each, in order: is the Version behind; is a Plan Step open; is it clear to stage; does the Take find main where the Update Note says. *not behind*, *step open*, *waits for the word*, *taken*, *refused* (`temp/common-ground/system-repo-change-simulation.md` §7, step 1, *When one is due*; §7, step 2, *Before staging*; §8, step 1, *Before the Take*).
2. **U2, where it starts:** the human, about to open the System Repo's next Plan Step, names it to update; a Look for Lessons runs first, and the job goes on from where it ended.
3. **U3, what moves main:** the Take's branch, at its gate; an open Plan Step's gate, which comes first.
4. **U4, the refused Take:** main moved after the Update was built against the *settled snapshot*; what follows: the human names the System Repo to update again, and a new Update replaces the waiting one.
5. **U5, what crosses:** nothing crosses without the human's word; an Update is written only into the System Repo's `temp/`.
6. **U6, what is open:** how main can move between staging and the Take is not ruled: postponing a Take is open (`temp/common-ground/system-repo-change-simulation.md` §8, *Open*). No candidate may decide it.

Found while building: every way main can move between staging and the Take is one the simulation leaves open, so the refused Take can be drawn only with its cause marked open (U6).

## 3. The candidates

- **A.** A picture per outcome: five.
- **B.** Two pictures, *step open* and *refused*; the other three as a list, *taken* pointing at *The Take*.
- **C.** One picture, its now holding every outcome as a branch of the checks.
- **D.** A table, no picture.
- **E.** Nothing new: *The two jobs* and *The Take* as they stand.
- **F.** Old picture 2, for the refused Take. Not rebuilt here; it is in the old pictures file.

Every picture uses the flow file's key (`temp/common-ground/system-repo-change-flow.md` §2, *Now*). The example: Version 1 in the System Repo, Version 2 the newest; the Look for Lessons ends in case *not moved*.

### Candidate A, a picture per outcome

#### *not behind*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1, the newest
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human, about to open the System Repo's next    ┊
 Plan Step, names it to update (§7, step 1)         ┊
 Look for Lessons (§4 to §6): case not moved,       ┊
 drawn above; the settled snapshot stays c1         ┊
 Deliver (§7): the Version is 1, the newest:        ┊
   no Update is due; nothing is made                ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    └─ cut ──────┐                            ◀──── the System Repo's next Plan Step opens on Version 1
                                                                 │
                                                              c2 ●  work, on Version 1
```

#### *step open*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
                                                    ├─ cut ──────┐                            ◀──── one of the System Repo's Plan Steps opens
                                                    │            │
                                                    │         c2 ●  work, on Version 1        ◀──── the step is still open: no gate yet
                                                    │            ┊
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo to update          ┊            ┊
 (§7, step 1)                                       ┊            ┊
 Look for Lessons (§4 to §6): case not moved;       ┊            ┊
 the open step's work waits for the next one        ┊            ┊
 Deliver (§7): the Version is 1, the newest is      ┊            ┊
   2: behind. A Plan Step is open: the agent        ┊            ┊
   says so, and makes nothing (§7, step 1)          ┊            ┊
                                                    │            ┊
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    │            │
                                                    │         c3 ●  the gate closes           ◀──── the step finishes on Version 1 (§8, Before the Take)
                                                    │            │
                                                 c3 ● ◀──────────┘                            ◀──── main moves to c3 by fast-forward
 at the next opening, the human names the           │
 System Repo to update again (§8, Before the        │
 Take)                                              │
```

#### *waits for the word*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human, about to open the System Repo's next    ┊
 Plan Step, names it to update (§7, step 1)         ┊
 Look for Lessons (§4 to §6): case not moved,       ┊
 drawn above; the settled snapshot stays c1         ┊
 Deliver (§7): the Version is 1, the newest is      ┊
   2: behind; no Plan Step open (§7, step 1)        ┊
   makes the Update: every Copy at Version 2,       ┊
   and an Update Note naming c1                     ┊
   before staging (§7, step 2): the System          ┊
   Repo's tree is not clean, or no word yet:        ┊
   the agent says what it found, and waits          ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 on the word: staged in the System Repo's temp/;    │
 the Take follows, as drawn in The Take             │
```

#### *taken*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human, about to open the System Repo's next    ┊
 Plan Step, names it to update (§7, step 1)         ┊
 Look for Lessons (§4 to §6): case not moved,       ┊
 drawn above; the settled snapshot stays c1         ┊
 Deliver (§7): the Version is 1, the newest is      ┊
   2: behind; no Plan Step open (§7, step 1)        ┊
   makes the Update: every Copy at Version 2,       ┊
   and an Update Note naming c1                     ┊
   stages it in the System Repo's temp/             ┊
                                                    ┊                                         ┄┄┄┄┄ the Update waits in temp/, not yet in force
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    ├─ cut ──────┐                            ◀──── the Take (§8), once it checks: main is still c1, the settled snapshot
                                                    │            │
                                                    │         c2 ●  the Update, as it arrived ◀──── the Take's commits, as drawn in The Take
                                                    │            │                            ◀──── c3 to c6, not drawn
                                                    │         c7 ●  the gate closes           ◀──── the Take's gate checks that the Take finished
                                                    │            │
                                                 c7 ● ◀──────────┘                            ◀──── main moves to c7 by fast-forward, at the gate's close
                                                    │
                                                    └─ cut ──────┐                            ◀──── the System Repo's next Plan Step opens on Version 2
                                                                 │
                                                              c8 ●  work, on Version 2
```

#### *refused*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human, about to open the System Repo's next    ┊
 Plan Step, names it to update (§7, step 1)         ┊
 Look for Lessons (§4 to §6): case not moved,       ┊
 drawn above; the settled snapshot stays c1         ┊
 Deliver (§7): the Version is 1, the newest is      ┊
   2: behind; no Plan Step open (§7, step 1)        ┊
   makes the Update, its Update Note naming c1      ┊
   stages it in the System Repo's temp/             ┊
                                                    ┊                                         ┄┄┄┄┄ the Update waits in temp/, not yet in force
                                                    │
                                                    ├─ cut ──────┐                            ◀──── main moves before the Take; how is open: postponing a Take (§8, Open)
                                                    │            │
                                                    │         c2 ●  work, on Version 1
                                                    │            │
                                                    │         c3 ●  the gate closes
                                                    │            │
                                                 c3 ● ◀──────────┘                            ◀──── main moves to c3 by fast-forward
                                                    │
 ── the check ──────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    ┊                                         ┄┄┄┄┄ at the next opening, the Take checks, from the Update Note:
                                                    ┊                                               main is c3, not c1: case 2, no Take; the System Repo says so (§8)
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo to update          │
 again: the Look for Lessons finds main moved;      │
 Deliver makes a new Update against c3, which       │
 replaces the waiting one (§7, step 1)              │
```

### Candidate B, two pictures and a list

Its two pictures are A's *step open* and *refused*, above. Below them, the list:

**What else may happen.**

- *not behind*: no Update is due, and the System Repo's next Plan Step opens on the same Copies;
- *waits for the word*: the Update is made, and staging waits while the System Repo's tree is not clean or no word is given (`temp/common-ground/system-repo-change-simulation.md` §7, step 2);
- *taken*: the Take, as drawn in *The Take*.

### Candidate C, one picture

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human, about to open the System Repo's next    ┊
 Plan Step, names it to update (§7, step 1)         ┊
 Look for Lessons (§4 to §6): case not moved,       ┊
 drawn above; the settled snapshot stays c1         ┊
 Deliver (§7): is the Version behind the newest?    ┊
   no: not behind; nothing is made                  ┊
   yes: is one of the System Repo's Plan Steps      ┊
   open?                                            ┊
     yes: step open; the agent says so, and         ┊
     makes nothing                                  ┊
     no: makes the Update. Clear to stage?          ┊
       no: waits for the word; the agent says       ┊
       what it found (§7, step 2)                   ┊
       yes: stages it in the System Repo's temp/    ┊
                                                    ┊                                         ┄┄┄┄┄ the Update waits in temp/, not yet in force
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    ┊                                         ┄┄┄┄┄ at the opening, the Take checks, from the Update Note (§8):
                                                    ┊                                               main still c1: taken, as drawn in The Take
                                                    ┊                                               anything else: refused; no Take, and the human names the System Repo to update again
 not behind, or after a Take: the System Repo's     │
 next Plan Step opens (§8)                          │
```

### Candidate D, a table

| Outcome | What decides it | What happens | Main |
|---|---|---|---|
| *not behind* | the System Repo's Version is the newest | no Update; the System Repo's next Plan Step opens on the same Copies | stays; the next Plan Step's branch is cut from it |
| *step open* | Version behind; one of the System Repo's Plan Steps is open | the agent says so and makes nothing; the step finishes on the old Copies | moves at the open step's gate |
| *waits for the word* | Update made; the System Repo's tree not clean, or no word yet | the agent says what it found, and waits | stays |
| *taken* | Update staged; the Take finds main at the *settled snapshot* | the Take, as drawn in *The Take* | moves at the Take's gate |
| *refused* | Update staged; main has moved since, how is open | no Take; the human names the System Repo to update again, and a new Update replaces the waiting one | moved before the Take |

### Candidate E, nothing new

*The two jobs* draws the job's checks as a chart, and *The Take* draws the Take (`temp/common-ground/system-repo-change-flow.md` §2).

## 4. Verdicts

Predictions, until the reviewer has rendered each.

| | U1 outcomes | U2 start | U3 what moves main | U4 refused Take | U5 what crosses | U6 open marked |
|---|---|---|---|---|---|---|
| A, five pictures | yes, one each | yes | yes, each drawn | yes, drawn | yes | yes |
| B, two pictures and a list | yes | yes | yes, where main moves; the list where it does not | yes, drawn | yes | yes |
| C, one picture | yes, as branches | yes | in part: no branch drawn for step open or refused | in words | yes | in part |
| D, a table | yes | no | in words | in words | no | yes, in a word |
| E, nothing new | yes, in the chart | yes | in part: the Take only | no: the chart's check has no refused case | yes | no |
| F, old picture 2 | no | no | yes, for its case | yes, from before the check was settled | yes | no: it draws a postponed Take as allowed |
