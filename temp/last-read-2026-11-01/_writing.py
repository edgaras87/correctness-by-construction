"""The last read's Writing sweep: numbered titles, lowercase Names,
bold Names away from their home. Run from the repo root."""
import os, re, sys

LIVING = sorted({l.split("\t")[1].strip() for l in open(sys.argv[1]) if l.strip()})
MD = [p for p in LIVING if p.endswith(".md")]
HIST = {"TODO-CONVERSATION-MEMORY.md", ".claude/decisions.md"}
GLOSS = ["docs/glossary.md", "delivery/container/docs/glossary.md",
         "delivery/container/docs/glossary/container.md",
         "delivery/method/docs/glossary/method.md",
         "delivery/spring-postgres/docs/glossary/stack.md"]

def body(p):
    t = open(p, encoding="utf-8").read()
    if p in HIST:
        k = t.find("-->")
        t = t[: k + 3] if k >= 0 else ""
    # blank out code fences and inline code, keep line numbers
    t = re.sub(r"```.*?```", lambda m: re.sub(r"[^\n]", " ", m.group(0)), t, flags=re.S)
    t = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), t)
    return t

out = []

# 1. numbered titles
for p in MD:
    for i, l in enumerate(body(p).split("\n"), 1):
        m = re.match(r"^#{1,6}\s+(\d+(?:\.\d+)*)\.?\s+(.*\S)\s*$", l)
        if not m:
            continue
        title = m.group(2)
        why = []
        if len(title) > 30:
            why.append(f"{len(title)} chars")
        if re.search(r"\s[—–-]\s|:", title):
            why.append("dash or colon")
        if "(" in title:
            why.append("parenthesis")
        if "," in title:
            why.append("comma: a gloss or a list?")
        if why:
            out.append(("title", p, i, f"{title}  [{'; '.join(why)}]"))

# 2. Names from the glossaries, with the file each entry points at
names = {}
for g in GLOSS:
    t = open(g, encoding="utf-8").read()
    for m in re.finditer(r"^- \*\*([^*]+)\*\*(.*?)(?=^- \*\*|^#|\Z)", t, re.M | re.S):
        name = m.group(1).strip()
        if len(name.split()) < 2 or not name[0].isupper():
            continue
        homes = re.findall(r"`((?:CBC )?[\w./-]+/[\w./-]*)`", m.group(2))
        names.setdefault(name, {"gloss": set(), "homes": set()})
        names[name]["gloss"].add(g)
        names[name]["homes"].update(h.replace("CBC ", "") for h in homes)

for p in MD:
    if p in GLOSS:
        continue
    t = body(p)
    lines = t.split("\n")
    for name, info in names.items():
        # lowercase spelling of a Name, as words
        low = name.lower()
        for m in re.finditer(r"(?<![\w-])" + re.escape(low) + r"(?![\w-])", t):
            if t[m.start(): m.end()] == low:
                ln = t[: m.start()].count("\n") + 1
                out.append(("lowercase", p, ln, f"'{low}' for {name}"))
        # bold Name: a list item's bold lead is form, not a mark
        for m in re.finditer(r"\*\*" + re.escape(name) + r"[^*]{0,3}\*\*", t):
            ln = t[: m.start()].count("\n") + 1
            line = lines[ln - 1]
            if re.match(r"^\s*(?:[-*]|\d+\.)\s+\*\*", line) and line.lstrip("-*0123456789. ").startswith("**" + name):
                continue
            hs = [h.replace("docs/concept/", "concept/").rstrip("/") for h in info["homes"] if h]
            at_home = any(p == h or p.endswith("/" + h) or p.startswith(h + "/") or ("/" + h + "/") in p for h in hs)
            out.append(("bold", p, ln, f"**{name}** {'at a home its entry names' if at_home else 'away from the home its entry names: ' + (', '.join(sorted(info['homes'])) or 'none named')}"))

for k, p, i, msg in sorted(out):
    print(f"{k}\t{p}:{i}\t{msg}")
print(f"# {len(out)} hits; {len(names)} Names", file=sys.stderr)
