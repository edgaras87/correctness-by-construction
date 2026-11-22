# How the Look for Lessons' cases are shown, compared

<!-- A visual comparison's draft (.claude/skills/visual-comparison/SKILL.md).
     It settles how temp/common-ground/system-repo-change-flow.md §2,
     *The Look for Lessons' cases*, shows the three cases. The outcome
     is recorded in the body of the commit that places the winner,
     and this draft goes in that commit. -->

## 1. The defect

The flow file's section draws five cases, A, B, C1, C2 and D2. They pair a Look for Lessons' result with Deliver's check, from when the two were one job. The simulation now has three cases, *not moved*, *no Change* and *Change read*, and Deliver is outside the Look for Lessons (`temp/common-ground/system-repo-change-simulation.md` §1, *How it is worked*; §4, step 1, *Two checks at main*).

## 2. What the reader must get

1. **L1, the cases:** there are three, and the two checks decide which: main moved, then, only if it moved, a Copy changed.
2. **L2, what each case does:** in each, what Read Changes gives, what Judge decides, and what Act does.
3. **L3, the snapshots:** a Look for Lessons compares the *settled snapshot* with the stop, main as it stands when the Look for Lessons begins. Act sets the *settled snapshot* to the stop in every case.
4. **L4, what moved main:** what the System Repo did before the Look for Lessons that puts it in its case: nothing, a Plan Step that changed no Copy, or one that changed a Copy with its Record.
5. **L5, where it ends:** the Look for Lessons ends at Act. Deliver, the Update and the Take are not in it; naming the System Repo to update leads on to them.
6. **L6, nothing written there:** a Look for Lessons writes nothing in the System Repo.

## 3. The candidates

- **A.** Three pictures, one per case.
- **B.** One picture, its now holding all three cases.
- **C.** A table, no picture.
- **D.** Nothing new: the section goes, and the two-jobs chart above it carries the cases.
- **E.** The section as it stands: five pictures, A to D2. Not rebuilt here; it is in the flow file.
- **F.** One picture, its now holding the three cases side by side, one column each; the Maintainer Repo's side widened for them.

Every picture uses the flow file's key (`temp/common-ground/system-repo-change-flow.md` §2, *Now*). The example is the simulation's: depth b, every Change taken into the System Kit.

### Candidate A, three pictures

#### *not moved*

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
 settled snapshot: c1                       ─▶   c1 ●
 named to update: Deliver's check follows
 (§7, step 1)
```

#### *no Change*

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
 settled snapshot: c3                       ─▶   c3 ●
 named to update: Deliver's check follows
 (§7, step 1)
```

#### *Change read*

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
 settled snapshot: c3                       ─▶   c3 ●
 named to update: Deliver's check follows
 (§7, step 1)
```

### Candidate B, one picture

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 ── before ─────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account                           ┌  c0 ●  earlier steps and Takes                ◀──── history
                                              │     │
 settled snapshot: the last stop           ─▶ └  c1 ●  the last gate closed                   ◀──── not moved: main stays here
                                                    │
                                                    ├─ cut ──────┐                            ◀──── no Change, Change read: one of the System Repo's Plan Steps opens
                                                    │            │
                                                    │         c2 ●  work                      ◀──── no Change: no Copy changed
                                                    │            │                                  Change read: a Copy changed, with its Record
                                                    │         c3 ●  the gate closes           ◀──── the gate (§3, step 2)
                                                    │            │
                                                 c3 ● ◀──────────┘                            ◀──── main moves to c3 by fast-forward; not in not moved
                                                    │
 ── now ────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo, for its           ┊
 lessons or to update it (§1)                       ┊
 Read Changes (§4): the stop is main                ┊
   check 1: has main moved past c1?                 ┊
   no: not moved; the stop is c1                    ┊
   yes: the stop is c3. Check 2: c1 against         ┊
   c3: has a Copy changed?                          ┊
     no: no Change; no Reading written              ┊
     yes: Change read. The Reading: one line,       ┊
     the Change with its Record                     ┊
 Judge (§5): not moved, no Change: nothing.         ┊
   Change read: one verdict: a lesson for its       ┊
   Adapted Case, depth b; the proposal holds        ┊
 Act on the verdicts (§6): Change read: the         ┊
   System Kit's Adapted Case gains the lesson;      ┊
   Version 2. The Reading goes. Every case:         ┊
   the settled snapshot set to the stop             ┊
                                                    │
 ── after ──────────────────────────────────────────┼───────────────────────────────────────────────────────────
 settled snapshot: the stop, c1 when not moved,
 c3 otherwise
 named to update: Deliver's check follows
 (§7, step 1)
```

### Candidate F, one picture, three columns in now

```
 Maintainer Repo                                                                                    main      branches                               System Repo
 ───────────────                                                                                    ────      ────────                               ───────────
 ── before ──────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 taken into account                                                                            ┌  c0 ●  earlier steps and Takes                ◀──── history
                                                                                               │     │
 settled snapshot: the last stop                                                            ─▶ └  c1 ●  the last gate closed                   ◀──── not moved: main stays here
                                                                                                     │
                                                                                                     ├─ cut ──────┐                            ◀──── no Change, Change read: one of the System Repo's Plan Steps opens
                                                                                                     │            │
                                                                                                     │         c2 ●  work                      ◀──── no Change: no Copy changed
                                                                                                     │            │                                  Change read: a Copy changed, with its Record
                                                                                                     │         c3 ●  the gate closes           ◀──── the gate (§3, step 2)
                                                                                                     │            │
                                                                                                  c3 ● ◀──────────┘                            ◀──── main moves to c3 by fast-forward; not in not moved
                                                                                                     │
 ── now ─────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 the human names the System Repo, for its lessons or to update it (§1)                               ┊
                                                                                                     ┊
 not moved                       ┆ no Change                       ┆ Change read                     ┊
 ─────────                       ┆ ─────────                       ┆ ───────────                     ┊
 Read Changes (§4): the stop     ┆ Read Changes (§4): the stop     ┆ Read Changes (§4): the stop     ┊
   is main, c1                   ┆   is main, c3                   ┆   is main, c3                   ┊
 check 1: main is c1, the        ┆ check 1: main is c3, past c1:   ┆ check 1: main is c3, past c1:   ┊
   settled snapshot: not moved;  ┆   moved                         ┆   moved                         ┊
   nothing new                   ┆ check 2: c1 against c3: no      ┆ check 2: c1 against c3: a       ┊
 Judge (§5): nothing to judge    ┆   Copy changed; no Reading      ┆   Copy changed. The Reading:    ┊
 Act on the verdicts (§6): the   ┆   written                       ┆   one line, the Change with     ┊
   settled snapshot set to the   ┆ Judge (§5): nothing to judge    ┆   its Record                    ┊
   stop, c1, as it was           ┆ Act on the verdicts (§6): the   ┆ Judge (§5): a lesson for its    ┊
                                 ┆   settled snapshot set to the   ┆   Adapted Case, depth b; the    ┊
                                 ┆   stop, c3                      ┆   proposal holds                ┊
                                 ┆                                 ┆ Act on the verdicts (§6): the   ┊
                                 ┆                                 ┆   System Kit's Adapted Case     ┊
                                 ┆                                 ┆   gains the lesson: Version 2.  ┊
                                 ┆                                 ┆   The Reading goes. The         ┊
                                 ┆                                 ┆   settled snapshot set to the   ┊
                                 ┆                                 ┆   stop, c3                      ┊
                                                                                                     │
 ── after ───────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────
 settled snapshot: the stop, c1 when not moved, c3 otherwise                                         │
 named to update: Deliver's check follows (§7, step 1)                                               │
```

### Candidate C, a table

| Case | Main moved | Copy changed | What moved main | Read Changes gives | Judge | Act on the verdicts |
|---|---|---|---|---|---|---|
| *not moved* | no | — | nothing | the stop, the *settled snapshot* itself | nothing | the *settled snapshot* set to the stop, as it was |
| *no Change* | yes | no | a Plan Step's gate, no Copy changed | the stop; no Reading written | nothing | the *settled snapshot* set to the stop |
| *Change read* | yes | yes | a Plan Step's gate, a Copy changed with its Record | the stop; a Reading, one line per Change | a verdict per line | what each verdict asks; the Reading goes; the *settled snapshot* set to the stop |

The Look for Lessons compares the *settled snapshot* with the stop, and writes nothing in the System Repo. When the human named the System Repo to update, Deliver's check follows (`temp/common-ground/system-repo-change-simulation.md` §7, step 1).

### Candidate D, nothing new

The section goes. The two-jobs chart above it already draws the two checks and the three cases, each with one line on what follows (`temp/common-ground/system-repo-change-flow.md` §2, *The two jobs*).

## 4. Verdicts

Predictions, until the reviewer has rendered each.

| | L1 cases | L2 what each does | L3 snapshots | L4 what moved main | L5 ends at Act | L6 nothing written |
|---|---|---|---|---|---|---|
| A, three pictures | yes, one each | yes | yes, each drawn | yes, each drawn | yes | yes, by the key |
| B, one picture | yes, as branches | yes, but read across branches | yes, but c1 or c3 in one line | yes, but two outcomes on one commit | yes | yes, by the key |
| C, a table | yes | yes | in words only | in words only | yes, in a line | yes, in a line |
| D, nothing new | yes | in part: one line each | no | no | yes | no |
| E, as it stands | no: five cases | no: Deliver in each | yes | yes | no | yes |
| F, three columns | yes, side by side | yes, compared across | yes, but c1 or c3 in words | yes, but two outcomes on one commit | yes | yes, by the key |
