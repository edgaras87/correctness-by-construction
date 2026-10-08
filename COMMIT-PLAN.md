# Commit plan: the devlog splits by month

## Summary — the state after all commits

The devlog is one file per month — `devlog/2026-08.md`,
`2026-09.md`, `2026-10.md` — each newest entry on top, every entry
moved whole and unedited. The rules its header carried live once, in
`devlog/README.md`, beside the months, as `temp/README.md` sits
beside its drafts. A session opens the current month, a few hundred
lines, not 5,500. Pointers by date — "devlog 2026-09-19", fifty of
them — find their entry as before: the date names the file. The
entry file's records table names the folder's current month.

## Commits

**1. `docs(agent): add commit plan for devlog split`**
This plan.

**2. `docs: the devlog splits by month`**
`devlog/devlog.md` cut at each entry's dated heading into three
month files, 18, 69 and 10 entries, nothing in an entry touched;
`devlog/README.md` holds the header's rules, the split rule now
said as done — a new month opens its own file. Checked as no line
lost: the three months' entries, joined, equal the old file below
its header.

**3. `chore(agent): the entry file names the month`**
`CLAUDE.md`'s records table: `devlog/devlog.md` becomes
`devlog/<YYYY-MM>.md`, the current month's file. Its own commit, as
an agent file.

**4. `docs: records carry the devlog split`**
TODO's item closes. The devlog's entry, in `2026-10.md`. ARCHITECTURE
§6's line for `devlog/` says one file per month.

**5. `docs(agent): close commit plan for devlog split`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The rules go to `devlog/README.md`, not into each month.** A
  header copied into three files is three places to drift; one at
  the top of the newest month moves every month. The folder's
  README is where `temp/` already keeps its own.
- **`devlog/devlog.md` goes**, rather than staying as the current
  month: one name per month is the convention's form
  (`docs/conventions/project-recording/` §4.3), and a file named
  for no month would need a rule for when it rolls over.
- **Step 2 and step 3 leave one boundary where the entry file names
  a file that is gone.** Agent files commit apart from everything
  else, so one of the two has to land first; the split goes first,
  as the thing the pointer points at.
- **Nothing else moves.** Pointers by date stay; the container's
  devlog stub is the run's, and a newborn's single file stays until
  its own grows long; history (ADRs, baselines) keeps the old path.
