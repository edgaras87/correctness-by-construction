# Today's design: its problems, and the way out

<!-- A draft: three problems the reviewer named in how this repo is
     built today, checked against the repo's own counts on 2026-11-02;
     how the new layering answers them; and how the repo would move to
     it, idea by idea. The layering: temp/model-example/layers.md. -->

## 1. The problems, checked

**1. The Idea Models point at each other, and hold too much.** True,
and small.

- Each of the 3 Idea Models points at both others.
- `docs/models/agent.md`, 459 lines, 12 sections and 19 parts, holds
  several ideas: what an agent is, its channels, the warning channel
  between repos, what survives a session, choosing a channel.
- With 3 models the mesh is small. The weight is in the manuals.

**2. A convention holds both seats, and several processes.** True,
and the largest problem.

- All 12 manuals hold both seats: the manual's form asks for *The
  seats* (`.claude/rules/convention-manual.md`). 5 split them into a
  section each.
- The 3 largest manuals are 2,115 of the manuals' 4,284 lines, and
  each holds several subjects:
  - exchange, 606 lines: 4 processes, delivering down, the take,
    editing a copy, reading up, for 2 seats; 6 texts derive from it,
    and it points at 7 other manuals;
  - project-recording, 905 lines: 14 sections, each record an idea of
    its own;
  - agent-arrangement, 604 lines: 4 subjects.
- The small manuals are single ideas already: commit-messages,
  visual-comparison and repo-hygiene, 113 to 136 lines each.

**3. A Work Approach should cover one case.** Partly done, and done by
copying.

- Split by case once: the exchange-read Agent Skill, 114 lines, and
  the exchange-deliver Agent Skill, 214.
- Split by seat by copying: five Agent Skills and Agent Rules exist
  twice, ours and the shipped one, each derived from the manual on its
  own. About 1,400 lines:

  | | Ours | Shipped |
  |---|---|---|
  | commit-plan | 206 | 206 |
  | commit-messages | 140 | 140 |
  | visual-comparison | 157 | 158 |
  | writing | 140 | 129 |
  | one-home | 78 | 60 |

  The shared part is paid twice, since no layer holds it once.

## 2. Not four conventions

Splitting a convention into one text per seat and per process, two
seats with reading and writing, gives four texts that each copy the
shared part: reading and writing must agree on one format. Four
copies drift, the problem one home per fact exists to stop.

With the new layering the split holds:

| What | Where | How many |
|---|---|---|
| What all cases share | the idea | 1 |
| What differs by seat | a project text for each seat | 2 |
| Each process | a Work Approach for each seat and process | up to 4 |

## 3. What the new layering improves

**Maintenance.**

- Today: a change to the exchange manual is checked against 8 cases in
  one text, then 6 texts that derive from it, then 7 manuals it
  points at. A change to commit-plan is made twice.
- New: a change to how one seat reads touches one Work Approach. A
  change to what both share touches one idea, two project texts, and
  the Work Approaches that rely on the changed part. The five pairs
  become one idea each, with what differs per seat.

**Readability.**

- Today: a manual's reader reads every seat and process in it. The
  agent's Agent Skill sends it to the manual for the why.
- New: each text holds one case. The agent reads one Work Approach,
  the size of the exchange-read Agent Skill, not the manual behind it.

**Future-proofing.**

- Today: a third seat, such as a second concept repo, grows *The
  seats* in all 12 manuals.
- New: a third seat adds project texts and Work Approaches; no idea
  changes. A new process adds one Work Approach.

**Complexity.**

- Inside each text: much lower. One case, links only up.
- Across texts: higher. More files, and the wiring becomes the busy
  part. Exchange might become 2 or 3 ideas, 2 project texts and about
  6 Work Approaches.
- It moves, it does not vanish: from inside the texts to the wiring.
  It is better only while the wiring is easy to see, which is why the
  idea map is read from the project texts, never written by hand.

## 4. Moving there, idea by idea

The reviewer's way, from the bottom up:

1. **Start at a Work Approach.** If it covers more than one case, split
   it, one Work Approach per case.
2. **Go up a layer.** Write the project text the split Work Approaches
   stand on. Move what it holds out of the old convention: the old
   text then points at the new one for it, or drops it.
3. **What the old convention still holds is more work.** Look at what
   is left, and repeat from step 1 with its Work Approaches.
4. **When the old convention holds nothing,** it goes. Write the idea
   the new project texts share.
5. **Repeat with the next idea.**

**Why bottom up is right.** The Work Approach is what the agent
actually uses, so its cases are lived, not guessed. Each step is small
and can be checked before the next.

**What to add:**

- **The new grows around the old until the old is gone.** In shared
  code this is called a strangler fig. At every commit each fact has
  one home: moved, never copied. The old convention points at the new
  text for each moved part.
- **Write the idea by taking things out.** Lifted last, from this
  repo's project texts, an idea comes out shaped by this repo. Check
  it: an idea names no project. What a second project would answer
  differently goes back down to the project text.
- **Hold the deliveries.** CBC Runs hold copies. Ship an idea only
  when its move is done, not halfway.
- **Count each step:** lines, pointers in and out, texts a change
  touches. If the counts do not fall, stop and look why before going
  on.

**First:** exchange. It is the worst case, 4 processes for 2 seats
with 6 texts derived from it, and its Agent Skills are split by case
already. If the layering holds there, it holds anywhere.
