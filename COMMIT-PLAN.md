# Commit plan: the eval's group 2, the method against itself

## Summary — the state after all commits

The method's skills agree with each other, and say nothing a run
cannot resolve.

- **Readiness asks per slice.** `system-readiness.md` R4 asks for the
  adversity class this slice names, as `cbc-slice` Stage 0 and
  `cbc-bootstrap` already say (F12).
- **Framing hands off to what comes next.** Its close says the ground
  and the bootstrap sit between framing and the first slice, without
  naming another group's skills; its workflow's slice is one
  invariant × one adversity (F13, F14).
- **Framing's census gate passes what its workflow allows** — the
  labelled trust-assumptions and runtime-ground blocks beside the
  facts (F19).
- **A caller's key is not a leaked mechanism.** `cbc-slice`'s gate
  drops "key", as its workflow's gate already does (F18, D4).
- **The worked example shows what framing now requires**: the
  audience as who the claim is sold to, what done demonstrably means,
  the runtime ground, the fence list, the not-probed ledger — in both
  byte-identical copies. The framing workflow's header carries the
  guard: when a step's required output changes, the example changes
  in the same commit (F15, D5).
- **`infra-establish` promises only what happens**: `compose.yaml`
  stays the ground's, and the exit is the walk's (F16, F20).
- **No shipped skill names a run.** Names, ordinals and retold stories
  go; "lived twice" and its kind stay (F7, D3).
- **The playbook's Release step** stops claiming framing decided its
  operations items (F17).

Nothing here is delivered. Run 3 opens SL-3 on the copies it holds;
these ship after SL-3 closes, at a step boundary.

## Commits

**1. `docs(agent): add commit plan for the eval's group 2`**
This plan.

**2. `fix(delivery): readiness asks for this slice's adversity`**
`cbc-slice/references/system-readiness.md` R4: its title and body ask
for the class the slice names, and its preamble stops saying "before
the first slice", since Stage 0 runs at every slice.

**3. `fix(delivery): framing hands off to the ground`**
`cbc-framing` SKILL.md's close: the ground, then the bootstrap, then
slicing. Its workflow's step 6 says one invariant × one adversity,
and its *Hands off to* names what follows the registry.

**4. `fix(delivery): the census gate passes its two blocks`**
`cbc-framing` SKILL.md step 2's gate: never what you trust, outside
the labelled trust-assumptions and runtime-ground blocks the workflow
allows beside the facts.

**5. `fix(delivery): a caller's key is not a mechanism`**
`cbc-slice` SKILL.md Stage 1's gate drops "key".

**6. `fix(delivery): the worked example shows framing as it is`**
Both `references/worked-example.md` copies, byte-identical: the
audience, and a line or two each for what done demonstrably means,
the runtime ground, the fence list, the not-probed ledger. The
framing workflow's header takes the guard.

**7. `fix(delivery): infra-establish promises what happens`**
`infra-establish` SKILL.md: the compose sentence loses "becomes the
whole system's declaration"; "the guide's own" becomes the walk's.

**8. `fix(delivery): shipped skills name no run`**
Every line F7 names, and the three it found beside them: run names,
ordinals and stories go, each line keeping the rule it carried and
its evidence strength.

**9. `fix(delivery): Release checks its operations items`**
`delivery/fills/cbc-run-pure-playbook.md`'s Release step: monitoring,
alerts, deploy and rollback are checked there, each unless the run
recorded an exclusion — not "decided at framing".

**10. `docs: records carry the eval's group 2`**
The eval marks F7 and F12 to F20 fixed with their commits. CHANGELOG
gains a Fixed line under Unreleased. The devlog waits for the
session's end.

**11. `docs(agent): close commit plan for the eval's group 2`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **One commit per finding, two where one change is.** F13 and F14
  share a commit because both are the framing's hand-off; F16 and
  F20 because both are `infra-establish`'s promises about itself.
  F7 is one commit across many files: one change, the same rule
  applied everywhere.
- **The method names no stack skill.** `cbc-framing` ships in the
  method group and `infra-establish` in the stack's, so framing's
  hand-off says "the ground" and "the bootstrap", not skill names.
- **No change to the concept.** Every finding is an execution
  disagreeing with another execution or with the concept; the
  concept stays v1.
- **One seat only.** Every file here is under `delivery/`; we hold
  none of these skills ourselves, so no commit splits by seat.
- **The deduplication TODO stays open.** D5 changes both copies the
  same way; whether they become one file is that item's question.
