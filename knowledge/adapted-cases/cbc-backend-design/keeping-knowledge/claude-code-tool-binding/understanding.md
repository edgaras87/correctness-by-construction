# Claude Code's Tool Binding

<!--
What it is: one of the Backend Kit's files, the Adapted Understanding Text of its Adapted Case for Claude Code's Tool Binding: the mechanisms Claude Code gives each channel and the Enforcement Gate, and where each agent file sits for it.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/agent-files-in-cbc-backend-design.md and knowledge/problem-domain-ideas/cbc-backend-design/how-an-agent-works-in-cbc-backend-design.md, kept in the Maintainer Repo. What every Tool Binding must say is how an agent works's, §8.
What stands on it: the Backend Kit's Instruction Texts whose place or form rests on the tool: the Entry File, the Decisions Log's Record Stub, each Agent Rule's paths: list. The Maintainer Repo's own Tool Binding points here for every fact of the tool, and holds only what is its own (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.3, The Adapted Case layer).
Its first source, input and not rules: the agent-arrangement manual, docs/conventions/agent-arrangement/README.md, deleted on 2026-11-27, its last state in git at bd6941d6: §5; from §2.3, §2.6 and §3, each agent file's path, the tool's bound on the Entry File, and the settings' format.
It never loads; it is read when an Instruction Text that rests on it changes, and when the tool's release is checked again. Each fact names the release it was checked against, and is changed here alone.
-->

This text says what Claude Code, the tool this repo is worked with, gives each channel and the Enforcement Gate, and where each agent file sits for it. Each Defined Term here is defined in the Backend Kit's Defined Terms.

The facts were checked against Claude Code 2.1.310 on 2026-10-24, by its documentation, by what could be seen in the Maintainer Repo, and by bug reports; first against 2.1.284 on 2026-09-29. A fact checked against another release says so.

## 1. Channels to mechanisms

| Channel | Claude Code mechanism |
|---|---|
| Ambient Channel | memory files: `CLAUDE.md`, at the root or under `.claude/`; `~/.claude/CLAUDE.md`; `@` imports; `AGENTS.md`, read when no `CLAUDE.md` is found; each Agent Rule without a `paths:` list; `CLAUDE.local.md`, the operator's file; the first 200 lines of auto memory's `MEMORY.md`; each Agent Skill's `name` and `description` |
| Pulled Channel | `Read`, `Grep`, `Glob`; an Agent Skill's body, once the agent invokes it |
| Pushed Channel | hooks that add context, slash commands, subagents; each Paths Rule, and a `CLAUDE.md` in a subfolder, loaded when the agent reads, writes or edits a matching file, or reads one from the shell with a command such as `cat`; never on a script's edit (§6) |
| Told Channel | the prompt |
| Observed Channel | tool results |
| Installed Channel | files in the repo |
| Enforcement Gate | hooks that block, such as `PreToolUse`; CI; permission rules in `settings.json`: `ask` stops at a prompt, `deny` refuses (§4) |

## 2. Where each agent file sits

| Agent file | Path |
|---|---|
| The Entry File | `CLAUDE.md`, at the root or under `.claude/`. The tool reads it at either address as one file. This repo's sits under `.claude/`. |
| Agent Skills | `.claude/skills/<name>/SKILL.md`, one folder each |
| Agent Rules | `.claude/rules/<name>.md`. A Paths Rule has a `paths:` list in its frontmatter. |
| Ways of working not yet proven | `.claude/approaches-on-trial/`, one file each |
| Output Shapes | `.claude/shapes/` |
| The Decisions Log | `.claude/decisions.md` |
| The repo's settings | `.claude/settings.json`, tracked |
| One machine's settings | `.claude/settings.local.json`, ignored |
| The operator's file | `CLAUDE.local.md`, beside the Entry File, ignored |

The tool's documentation keeps the Entry File under 200 lines. A screen is the bound here (agent files, kept in the Maintainer Repo, *The Entry File's size*).

`settings.json` is JSON, which holds no comment. So the why of each setting sits in the Decisions Log, and a setting added later is merged into the file, never written into it as text.

## 3. Hooks

Hooks serve two roles. A hook that adds context is the Pushed Channel. A hook that blocks is an Enforcement Gate. One mechanism, two roles: each hook says which it is.

## 4. Permission rules

A permission rule is an Enforcement Gate only in a mode that honours it. `deny` refuses in every mode. `ask` still prompts in auto mode, and in the mode that bypasses permissions. The mode that never asks turns it into a refusal. What no rule matches, auto mode lets a classifier decide in the background. The Enforcement Gate is the tool's, not the repo's.

A rule reaches only what the tool can name. A `Read` deny covers the file tools, and the shell commands the tool knows as file commands, such as `cat`, `head` and `sed`. It does not cover `grep -r` across a tree, or a script that opens files itself. The documentation sends that to the sandbox.

## 5. What the tool drops

The tool loads a memory file without its HTML comments. It drops every block-level `<!-- … -->` comment before the text reaches the context window, and keeps one inside a code block. So a comment in the Entry File never goes through the Ambient Channel: it reaches the agent only when the file is opened with a tool, which for the Entry File is when it is edited. Seen on 2.1.260 to 2.1.263, documented since, and seen again on 2.1.284.

The same loader honours `claudeMdExcludes` in `settings.json`, globs matched against the absolute path. That is how a `CLAUDE.md` kept in a repo as a template stays out of its sessions.

## 6. Paths Rules

A Paths Rule loads when the agent reads, writes or edits a file under one of its paths, or reads one from the shell with a command such as `cat` or `head`. The tool decides that, not the agent. That is the Pushed Channel with no hook to write. A `CLAUDE.md` in a subfolder loads the same way. An Agent Rule with no `paths:` list loads in every session, through the Ambient Channel, like the Entry File.

Three limits:

- **It arrives after the first draft.** A new file's content is written in the call that loads the rule. So a record written from scratch gets the rule no earlier than a comment in its Record Stub would have given it.
- **A script's edit loads nothing,** and nor does listing the folder.
- **Its condition is a place, never an action.** So it does not replace an Agent Skill.

What is documented and what is seen have differed. On 2.1.284 the Maintainer Repo saw the `Read` tool alone load a rule. On 2.1.310 a read by `sed` loaded one, as the documentation now says. Bug reports, checked 2026-10-24, show `paths:` failing silently in some formats and surfaces (Claude Code issues #17204, #33581, #87217). So an Agent Rule that must arrive does not rest on its path alone.

## 7. Agent Skills

Claude Code loads an Agent Skill's `name` and `description` at session start, and its body only when the agent invokes it: a trigger in the Ambient Channel over a body in the Pulled Channel. The agent still decides whether to invoke it, so an Agent Skill is not the Pushed Channel. It is still the closest this tool gets to the Pushed Channel for a rule about an action. A hook closes the rest.

The tool ignores a frontmatter field it does not know, without an error, in an Agent Skill as in an Agent Rule. An Agent Skill may also carry a `paths:` list. What that does has not been checked.

## 8. Compaction and subagents

- **Compaction** restores the root `CLAUDE.md`, the Agent Rules without `paths:`, and auto memory, from disk. A Paths Rule and a subfolder's `CLAUDE.md` come back only when a matching file is touched again. An invoked Agent Skill's body comes back cut to 5,000 tokens.
- **A subagent** loads the `CLAUDE.md` files, the Agent Rules and `CLAUDE.local.md`, but not auto memory, and no Agent Skill's body unless its definition names the Agent Skill. The built-in Explore and Plan agents skip `CLAUDE.md`. A fork inherits the whole conversation.

So what a delegated task must know goes in its prompt, the Told Channel. An Explore or Plan agent gets none of the Agent Rules loaded every session, only the Paths Rules whose paths match the files it touches.

## 9. Open

- **What a `paths:` list does to an Agent Skill:** not checked. Its trigger: an Agent Skill that needs one.
