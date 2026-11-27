# Claude Code's Tool Binding, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Claude Code's Tool Binding, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work).
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/agent-files-in-keeping-knowledge.md and knowledge/problem-domain-ideas/keeping-knowledge/how-an-agent-works-in-keeping-knowledge.md. Every fact of the tool is the Backend Kit's Tool Binding's, knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md: this text points there and holds only what is this repo's own (the layers document, §3.3, The Adapted Case layer).
What stands on it: this repo's agent files: CLAUDE.md, CLAUDE.local.md and .gitignore's "this repo" section.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when an agent file of this repo changes, and when the Backend Kit's Tool Binding does.
Its first source, input and not rules: the agent-arrangement manual, docs/conventions/agent-arrangement/README.md: §2.3, this repo's Entry File; §3.5 and §3.7, this repo's settings and operator's file; §5.3, claudeMdExcludes.
-->

This text says what is this repo's own in how Claude Code works here. What the tool gives each channel, and where each agent file sits for it, are the Backend Kit's Tool Binding's (`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Enforcement Gate | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Hygiene Base | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |
| Tool Binding | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |

## 2. What differs here

- **The Entry File sits at the root,** `CLAUDE.md`, not under `.claude/` (`knowledge/problem-domain-ideas/keeping-knowledge/agent-files-in-keeping-knowledge.md` §3, *The Entry File*). The tool reads it at either address.
- **The operator's file is tracked.** `.gitignore` ignores `CLAUDE.local.md` in its Hygiene Base, and its "this repo" section takes it back with `!CLAUDE.local.md` (ADR-0062).
- **No `.claude/settings.json`.** No rule here needs an Enforcement Gate as repo state, and nothing needs an exclude.
- **`.claude/understanding/` never loads.** The tool loads nothing from a folder of that name.
- **The Backend Kit's Entry File is kept here,** at `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/entry-file/CLAUDE.md`. To the tool it is a `CLAUDE.md` in a subfolder, so it loads when a file in that folder is touched. That folder holds only that file, so it loads only when the file itself is read or edited, when its text is in front of the agent anyway. No `claudeMdExcludes` is set.

**Rules:**

- A fact of the tool goes in the Backend Kit's Tool Binding, never here.
- `claudeMdExcludes` is set for the Backend Kit's Entry File once another file lands in its folder.
