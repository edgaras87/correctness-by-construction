# The move: split first, choose a pattern after

<!-- A draft: how this repo moves from today's design to small texts
     with one job each, whichever pattern is chosen after. The reviewer's
     order, why it holds for every pattern, and what it needs besides.
     The patterns: temp/model-example/other-patterns.md. The layering:
     temp/model-example/layers.md. -->

## 1. Split first

Every pattern works on small texts with one job each. So the split
comes first, whatever pattern follows:

| Pattern | Needs the split |
|---|---|
| Sockets | Yes: a socket belongs to one idea, and an idea covering 4 cases has muddled needs |
| Single-sourcing | Yes, most: small typed pieces are where it starts |
| Versions and pinning | Yes: one case cannot be versioned without the other 3 |
| A public part and a private part | Yes: the line is drawn per idea |
| Checks written by the user | Yes: one check per place relying on one case |
| Copy and own | Less: it works on large texts too |
| A pattern language | No: it is near today's design |

## 2. The order

1. **Split each Work Approach by case.** One Work Approach for each case.
2. **Split each convention by seat.** One text for each seat.
3. **Give each case its own section** inside a text. Cheaper than a
   file, and it shows whether the cut is in the right place before it
   becomes one.
4. **Lift the ideas out,** into texts bound to no project.

Then measure, and only then decide whether a pattern is worth adding.
The split alone may give most of the gain.

## 3. Rules from the first split

1. **No new sideways pointer.** Split alone, a manual's pointers spread
   over the new texts, and some are copied into several: the split can
   add pointers. Where a split text relies on another manual's fact,
   the need is written in its own words instead. This holds under every
   pattern.
2. **Each fact keeps one home at every commit.** A part moves, never
   copies. The old text points at the new one for what moved, until the
   old text is empty and goes.
3. **The shape to land in:** the three templates of
   `temp/model-example/layers.md`. They fit every pattern.

## 4. Before the first move

**The repo's own rules push back.** A split manual breaks three of
them:

- the manual's form asks for *The seats* and nine sections
  (`.claude/rules/convention-manual.md`);
- the Foundation Check checks every Agent Skill and Agent Rule against
  its manual (`.claude/rules/foundation-check.md`);
- a pointer carries a section number (`docs/conventions/facts-in-sync/`
  §3.1, *What a Fact Reference is*).

Decide which are paused for a moved idea, and what holds in their
place. Otherwise each commit of the move is flagged by the repo's own
checks.

## 5. While moving

- **Lived lessons keep a place.** A manual holds *Its story* lines, ADR
  citations, and lessons from real CBC Runs. Each split says where they
  go: the why into the idea, in its own words; the history stays in the
  ADRs and the devlog.
- **Deliveries wait.** CBC Runs hold copies. An idea ships only when
  its move is done.
- **Split only what holds more than one case or seat.** commit-messages,
  visual-comparison and repo-hygiene are single ideas already.
- **Count each step:** lines, pointers in and out, the texts a change
  touches, before and after. Without the counts, "less complex" stays a
  feeling.

## 6. One idea, then decide

The whole move is large: 12 manuals, 3 Idea Models, and about 20 Agent
Skills and Agent Rules with their shipped copies. Move one idea end to
end, exchange first, count it, and decide then whether to go on.
