# How I work with Claude, in this repo

- Before any commit: stage it, show me the diff, and stop. Commit
  only when I say so, one commit at a time. Never push unless I ask.
- In a Change Set, stop once its plan is written, for my word on it.
  Then stage each planned commit, show me the diff, and stop, as for
  any commit. No commit runs without my word.
- A TODO line we decide while talking: stage it at once and show
  me. In a Change Set it is an inserted commit.
- At the end of a session, before the devlog entry: list each
  correction or rule said only in our chat, and ask me where each
  goes: your memory, this file, a TODO item, or nowhere. Then check
  your memory against the list of note names and dates the newest
  devlog "Memory checked" line holds: a name not in the list is new,
  one in the list but gone is deleted, a different date is changed,
  the same name and date is unchanged and left out. For each new,
  changed or deleted note, ask whether it stays, moves into this
  file or the repo, or goes. Show both as tables: rule, where it
  came from, now in, suggestion; and note, new, changed or deleted,
  what it says now, what you changed, suggestion. Then write the
  session's "Memory checked" line: the time, and every note's name
  and date. With no such line yet, every note counts as new. On
  trial; it moves to the session-end item in TODO when that item is
  decided.
