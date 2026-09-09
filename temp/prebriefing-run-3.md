# Pre-briefing prompt — run 3

Fired in its own session on main, before the briefing. Everything
below the line is pasted whole. Three pieces for the retrospective
on top of the branch rule already in: the kit update to af16eb7
(which brings the commit ask rule as the kit's born default), the
operator's local instruction file, and CLAUDE.md under .claude/.

Before the session, deliver the kit the way the seed did — on a
receipt branch, cut from the seed commit that carries the c670fe5
pin, so the branch's one commit against its parent is the kit at
the two pins. The run's worktree must be clean on main first.

```bash
run_dir=~/IdeaProjects/cbc-pure-run-3
handbook_dir=~/PycharmProjects/engineering/engineering-handbook
kit_pin=$(git -C "$handbook_dir" rev-parse --short HEAD)   # af16eb7

git -C "$run_dir" switch -c "kit-$kit_pin" 27db35e
cp -r "$handbook_dir"/starter/kit/. "$run_dir"/
git -C "$run_dir" add -A
git -C "$run_dir" commit -m "chore: seed — kit @ $kit_pin, from c670fe5"
git -C "$run_dir" switch main
```

The copy overwrites the seed's four fills on that branch (the birth
entry's pin and date, the first ADR's date, the devlog heading) with
the kit's placeholders; the prompt tells the agent to read past
them. The ask rule bites from the session after the agent commits
the settings file, not in this one.

---

Before the briefing arrives, three pieces of working arrangement go
in, on trial from Step 1 and evaluated at the retrospective for
folding back to their source. Nothing here names the problem.

1. The starter kit moved since the birth pin. Its state at af16eb7
   is on the branch kit-af16eb7: one commit, cut from the seed
   commit whose subject carries the c670fe5 pin, so that commit
   against its parent is the kit at the two pins — the compare
   your convention-lifecycle §8 asks for. Four lines of that diff
   are the kit's placeholders reappearing where the seed filled
   them (the birth entry's pin and date, the first ADR's date, the
   devlog heading): not changes, read past them. Run the update as
   §8 says — position from the registry, compare-first on every
   copy, the changed stub comments carried into the living records,
   the registry entries. What the kit now ships that it did not — a
   tracked .claude/settings.json holding one permission rule — is
   on trial from Step 1 like the rest, and arrives like the rest.
   Say in the devlog what the branch gave the compare, and where it
   fell short.

2. A file CLAUDE.local.md at the repository root, mine and
   untracked — the hygiene base the update brings already ignores
   it. Its whole content, verbatim:

   # Working with me

   - Every commit is staged first and shown to me as a diff. Commit
     only on my explicit word — never as part of finishing a task.
     This holds for single commits as much as for change sets.
   - One decision at a time: raise it, wait, then act.
   - Never `git push`; I push myself.

   The file is mine: nothing in the records repeats its text, and
   no project file derives from it.

3. CLAUDE.md moves to .claude/CLAUDE.md, content untouched — the
   harness reads either address, and every agent-side file then
   sits under .claude/. Mentions of it by name stay true; none
   names its path. The file in 2 stays at the root: the harness
   reads it there only.

Record each arrival where the records table says a convention's
arrival or an agent-setup change goes, the second as "exists,
ignored, holds the reviewer's pace" so the retrospective can find
it. Extend the TODO Later item that holds the branch rule's trial
to name these three, to fold back to their source at the
retrospective if they hold. Commit per your split, staged and shown
to me first; commit only on my word.
