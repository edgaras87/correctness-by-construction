# Commit plan: pure-seed says what is true now

## Summary — the state after all commits

`delivery/installs/pure-seed.md` is the birth procedure of record
until the next birth, when `exchange-birth` replaces it (TODO). Until
then it says only what is true of the repo as it stands:

- Step 5's check shows which files differ and always resets the
  index, so no birth starts from a staged index.
- Nothing in it points at what is gone: step 2's audit of a
  `delivery/README.md` section, a delta list and a re-verify duty;
  the container's provenance in that README; a "first-session
  comment".
- The prompt names one pin, as its own first sentence does.
- The reader's checklist at the end agrees with the checks above
  it: the entry files arrive composed, and there is one birth entry.
- Its script comment cites bare, as ADR-0020 says of the seed.
- No revision history. Each passage keeps its one-line why and
  points to the ADR that holds the rest.

Its structure is not touched; that is `exchange-birth`'s to decide.

## Commits

**1. `docs(agent): add commit plan for pure-seed`**
This plan.

**2. `fix(installs): step 5's check resets on a miss`**
`git add -A && git diff --cached --quiet birth-seed && git reset -q`
prints nothing either way, and on a mismatch it skips the reset and
leaves every file staged (tested in a scratch repo). It becomes
`git add -A && git diff --cached --stat birth-seed; git reset -q`,
and its prose and the checklist item that cites it say "lists
nothing".

**3. `docs(installs): pure-seed drops what is gone`**
- Step 2's audit goes. The section, the delta list and the duty it
  checks are gone (the local-maps set, ADR-0025, `starter/`), and a
  container that is ours has nothing outside it to drift from.
- "Provenance in `delivery/README.md`" goes.
- "The kit's first-session comment" goes from the list of what
  rides in with the steps.
- The prompt's "the pins name" becomes one pin.
- The reader's checklist loses "its own CLAUDE.md" and "the
  bundle's birth entry reconstructed".
- Step 4's comment cites ADR-0036 and ADR-0029 bare.

**4. `docs(installs): pure-seed's history goes`**
The 75-line header comment goes. Its nine revisions are ADR-0016,
0018, 0019 and 0024 and the devlog, and two of its claims are false
now. In the body, the semi-pure switch, the "candidate variant" and
run 1's story each become their one-line why and a pointer.

**5. `docs: devlog carries pure-seed`**
The session's entry. The TODO item `exchange-birth` gains a line
saying pure-seed was brought up to date on 2026-09-30, so the skill
is written from true text.

**6. `docs(agent): close commit plan for pure-seed`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Fix, do not restructure.** `pure-seed.md` goes at the next
  birth; its shape is for `exchange-birth` to decide, and only what
  is wrong in it is changed now.
- **The broken check is a commit of its own**, a fix, apart from
  the text that is only out of date.
- **Step 2's audit goes rather than being repointed.** There is no
  text about the container left that could drift from it.
