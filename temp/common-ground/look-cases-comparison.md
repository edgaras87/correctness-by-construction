# How the Look for Lessons' cases are shown, compared

<!-- A visual comparison's draft (.claude/skills/visual-comparison/SKILL.md).
     It settles how temp/common-ground/system-repo-change-flow.md §2,
     *The Look for Lessons' cases*, shows the three cases. Candidate A
     was chosen, and its after is worked here. The outcome is recorded
     in the body of the commit that places it in the flow file, and
     this draft goes in that commit. -->

## 1. The defect

The flow file's section draws five cases, A, B, C1, C2 and D2. They pair a Look for Lessons' result with Deliver's check, from when the two were one job. The simulation now has three cases, *not moved*, *no Change* and *Change read*, and Deliver is outside the Look for Lessons (`temp/common-ground/system-repo-change-simulation.md` §1, *How it is worked*; §4, step 1, *Two checks at main*).

## 2. What the reader must get

1. **L1, the cases:** there are three, and the two checks decide which: main moved, then, only if it moved, a Copy changed.
2. **L2, what each case does:** in each, what Read Changes gives, what Judge decides, and what Act does.
3. **L3, the snapshots:** a Look for Lessons compares the *settled snapshot* with the stop, main as it stands when the Look for Lessons begins. Act sets the *settled snapshot* to the stop in every case.
4. **L4, what moved main:** what the System Repo did before the Look for Lessons that puts it in its case: nothing, a Plan Step that changed no Copy, or one that changed a Copy with its Record.
5. **L5, where it ends:** the Look for Lessons ends at Act. Deliver, the Update and the Take are not in it; naming the System Repo to update leads on to them.
6. **L6, nothing written there:** a Look for Lessons writes nothing in the System Repo.

## 3. The three pictures

The reviewer chose candidate A, three pictures, one per case. The other candidates, B to F, and their verdicts are in git at `67853479`.

Every picture uses the flow file's key (`temp/common-ground/system-repo-change-flow.md` §2, *Now*). The example is the simulation's: depth b, every Change taken into the System Kit.

### *not moved*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account                           ┌  c0 ●  earlier steps and Takes                ◀──── history
                                              │     │
 settled snapshot: the last stop           ─▶ └  c1 ●  the last gate closed                   ◀──── no Plan Step has closed since
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo, for its           ┊
 lessons or to update it (§1)                       ┊
 Read Changes (§4): the stop is main, c1            ┊
   check 1: main is c1, the settled snapshot:       ┊
   not moved, nothing new                           ┊
 Judge (§5): nothing to judge                       ┊
 Act on the verdicts (§6): the settled              ┊
   snapshot set to the stop, c1, as it was          ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 settled snapshot: c1                       ─▶   c1 ●                                         ◀──── the System Repo may go on with a Plan Step already open; its next opens once it is named to update
 what may follow, by why the human named it:
 - for its lessons: nothing follows
 - to update it: Deliver's check comes next,
   then the System Repo's next Plan Step opens,
   with or without an Update (§7, step 1)
```

### *no Change*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account                           ┌  c0 ●  earlier steps and Takes                ◀──── history
                                              │     │
 settled snapshot: the last stop           ─▶ └  c1 ●  the last gate closed
                                                    │
                                                    ├─ cut ──────┐                            ◀──── one of the System Repo's Plan Steps opens
                                                    │            │
                                                    │         c2 ●  work, no Copy changed
                                                    │            │
                                                    │         c3 ●  the gate closes           ◀──── the gate (§3, step 2): no Change to decide
                                                    │            │
                                                 c3 ● ◀──────────┘                            ◀──── main moves to c3 by fast-forward
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo, for its           ┊
 lessons or to update it (§1)                       ┊
 Read Changes (§4): the stop is main, c3            ┊
   check 1: main is c3, past c1: moved              ┊
   check 2: c1 against c3: no Copy changed:         ┊
   no Change; no Reading written                    ┊
 Judge (§5): nothing to judge                       ┊
 Act on the verdicts (§6): the settled              ┊
   snapshot set to the stop, c3                     ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 settled snapshot: c3                       ─▶   c3 ●                                         ◀──── the System Repo may go on with a Plan Step already open; its next opens once it is named to update
 what may follow, by why the human named it:
 - for its lessons: nothing follows
 - to update it: Deliver's check comes next,
   then the System Repo's next Plan Step opens,
   with or without an Update (§7, step 1)
```

### *Change read*

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account                           ┌  c0 ●  earlier steps and Takes                ◀──── history
                                              │     │
 settled snapshot: the last stop           ─▶ └  c1 ●  the last gate closed                   ◀──── the Copies at Version 1, the newest
                                                    │
                                                    ├─ cut ──────┐                            ◀──── one of the System Repo's Plan Steps opens
                                                    │            │
                                                    │         c2 ●  a Copy changed            ◀──── a Change, with its Record; its proposal: any repo would meet it
                                                    │            │
                                                    │         c3 ●  the gate closes           ◀──── the gate (§3, step 2): the Change kept
                                                    │            │
                                                 c3 ● ◀──────────┘                            ◀──── main moves to c3 by fast-forward
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo, for its           ┊
 lessons or to update it (§1)                       ┊
 Read Changes (§4): the stop is main, c3            ┊
   check 1: main is c3, past c1: moved              ┊
   check 2: c1 against c3: a Copy changed:          ┊
   Change read. The Reading: one line, the          ┊
   Change with its Record                           ┊
 Judge (§5): one verdict: a lesson for its          ┊
   Adapted Case, depth b; the proposal holds        ┊
 Act on the verdicts (§6): the System Kit's         ┊
   Adapted Case gains the lesson, reworded:         ┊
   the System Kit reaches Version 2. The            ┊
   Reading goes. The settled snapshot set to        ┊
   the stop, c3                                     ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 settled snapshot: c3                       ─▶   c3 ●                                         ◀──── the System Repo may go on with a Plan Step already open; its next opens once it is named to update
 what may follow, by why the human named it:
 - for its lessons: nothing follows
 - to update it: Deliver's check comes next,
   then the System Repo's next Plan Step opens,
   with or without an Update (§7, step 1)
```
