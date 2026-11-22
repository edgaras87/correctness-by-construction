# How the update job's outcomes are shown, compared

<!-- A visual comparison's draft (.claude/skills/visual-comparison/SKILL.md).
     It settles how temp/common-ground/system-repo-change-flow.md §2 shows
     the second of the two jobs, an Update when work resumes.
     Candidate A was chosen, and is worked here. The outcome is
     recorded in the body of the commit that places it in the flow
     file, and this draft goes in that commit. -->

## 1. The defect

The flow file shows the update job only as the second box of *The two jobs*, and the Take in *The Take* (`temp/common-ground/system-repo-change-flow.md` §2). The old five cases drew an Update inside each Look for Lessons, and are gone. Two outcomes have no picture in Now: a Plan Step open, which stops the job, and a Take refused because main moved. The refused Take is drawn only in old picture 2 (`temp/common-ground/system-repo-change-flow-old-pictures.md`), from before the Take's check was settled.

## 2. What the reader must get

1. **U1, the outcomes:** four, and what decides each, in order: is the Version behind; is a Plan Step open; does the Take find main where the Update Note says: *not behind*, *step open*, *taken*, *refused*. Before staging, the job may pause, waiting for the human's word or a clean tree (`temp/common-ground/system-repo-change-simulation.md` §7, step 1, *When one is due*; §7, step 2, *Before staging*; §8, step 1, *Before the Take*).
2. **U2, where it starts:** the human, about to open the System Repo's next Plan Step, names it to update; a Look for Lessons runs first, and the job goes on from where it ended.
3. **U3, what moves main:** the Take's branch, at its gate; an open Plan Step's gate, which comes first.
4. **U4, the refused Take:** main moved after the Update was built against the *settled snapshot*; what follows: the human names the System Repo to update again, and a new Update replaces the waiting one.
5. **U5, what crosses:** nothing crosses without the human's word; an Update is written only into the System Repo's `temp/`.
6. **U6, what is open:** how main can move between staging and the Take is not ruled: postponing a Take is open (`temp/common-ground/system-repo-change-simulation.md` §8, *Open*). No candidate may decide it.

Found while building: every way main can move between staging and the Take is one the simulation leaves open, so the refused Take can be drawn only with its cause marked open (U6).

## 3. The four pictures

The reviewer chose candidate A, a picture per outcome. The other candidates, B to F, and their verdicts are in git at `822b60e5`.

Every picture uses the flow file's key (`temp/common-ground/system-repo-change-flow.md` §2, *Now*). The example: Version 1 in the System Repo, Version 2 the newest; the Look for Lessons ends in case *not moved*.

### *not behind*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1, the newest
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 - the human, about to open the System Repo's       ┊
   next Plan Step, names it to update (§7, step 1)  ┊
 - Look for Lessons (§4 to §6): case not moved,     ┊
   drawn above; the settled snapshot stays c1       ┊
 - Deliver (§7): the Version is 1, the newest:      ┊
   no Update is due; nothing is made                ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    └─ cut ──────┐                            ◀──── the System Repo's next Plan Step opens on Version 1
                                                                 │
                                                              c2 ●  work, on Version 1
```

### *step open*

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
 - the human names the System Repo to update        ┊            ┊
   (§7, step 1)                                     ┊            ┊
 - Look for Lessons (§4 to §6): case not moved;     ┊            ┊
   the open step's work waits for the next one      ┊            ┊
 - Deliver (§7): the Version is 1, the newest is    ┊            ┊
   2: behind                                        ┊            ┊
 - a Plan Step is open: the agent says so, and      ┊            ┊
   makes nothing (§7, step 1)                       ┊            ┊
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

### *taken*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 - the human, about to open the System Repo's       ┊
   next Plan Step, names it to update (§7, step 1)  ┊
 - Look for Lessons (§4 to §6): here case not       ┊
   moved; the settled snapshot stays c1. Any of     ┊
   its three cases leads on the same way: see       ┊
   An Update at the newest Version, below           ┊
 - Deliver (§7): the Version is 1, the newest is    ┊
   2: behind; no Plan Step open (§7, step 1)        ┊
 - Deliver makes the Update: every Copy at          ┊
   Version 2, and an Update Note naming c1          ┊
 - before staging (§7, step 2): when the System     ┊
   Repo's tree is not clean, or no word yet, the    ┊
   agent says what it found, and waits              ┊
 - on the word, Deliver stages the Update in the    ┊
   System Repo's temp/                              ┊
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

### *refused*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account by                        ┌  c0 ●  earlier Plan Steps and Takes           ◀──── history
 earlier Looks for Lessons                    │     │
 settled snapshot                          ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1; the System Kit has since reached Version 2
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 - the human, about to open the System Repo's       ┊
   next Plan Step, names it to update (§7, step 1)  ┊
 - Look for Lessons (§4 to §6): case not moved,     ┊
   drawn above; the settled snapshot stays c1       ┊
 - Deliver (§7): the Version is 1, the newest is    ┊
   2: behind; no Plan Step open (§7, step 1)        ┊
 - Deliver makes the Update, its Update Note        ┊
   naming c1                                        ┊
 - Deliver stages it in the System Repo's temp/     ┊
                                                    ┊                                         ┄┄┄┄┄ the Update waits in temp/, not yet in force
                                                    │
 ── before the Take ────────────────────────────────┼───────────────────────────────────────────────────────────
                                                 c2 ●  a gate closed                          ◀──── main moved past c1 before the Take; how is open: postponing a Take (§8, Open)
                                                    │
 ── the check ──────────────────────────────────────┼───────────────────────────────────────────────────────────
                                                    ┊                                         ┄┄┄┄┄ at the opening, the Take checks, from the Update Note:
                                                    ┊                                               main is c2, not c1: case 2, no Take; the System Repo says so (§8)
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 - the Update stays in temp/, not taken             │
 - the human names the System Repo to update        │
   again (§8, Before the Take)                      │
 - Look for Lessons: main moved; case no Change     │
   or Change read, by what c2 holds                 │
 - Deliver makes a new Update against c2 and the    │
   newest Version; it replaces the waiting one      │
   (§7, step 1)                                     │
```

**An Update at the newest Version.** An Update is always made at the newest Version. When the Look for Lessons ends in *Change read*, Act may raise the Version first: the Update is then made at that Version, and brings the System Repo's own lesson back. If the System Kit moves after it is made, the Update is still taken, and the next brings the rest (`temp/common-ground/system-repo-change-simulation.md` §8, step 1, *A check before delivery*).
