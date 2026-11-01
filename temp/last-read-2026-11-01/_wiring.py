"""The last read's Wiring sweep. Run from the repo root.

Checks: backticked paths resolve; Fact References land on a heading
with their number and title; ADRs cited exist; Foundation Lines name
what exists; each manual's 'What this is made usable as' names what
stands on it.
"""
import os, re, sys, glob

ROOT = os.getcwd()
LIVING = [l.split("\t")[1].strip() for l in open(sys.argv[1]) if l.strip()]
HISTORY_BY_HEADER = {"TODO-CONVERSATION-MEMORY.md", ".claude/decisions.md"}
SHIP_ROOTS = ["delivery/container", "delivery/method", "delivery/spring-postgres"]

def text(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

def shipped(p):
    return p.startswith("delivery/")

def strip_fences(t):
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), t, flags=re.S)

def resolve(path, src):
    """Return the repo path a reference names, or None."""
    path = path.strip()
    cands = []
    if shipped(src) and not path.startswith("CBC "):
        q = path
        if q.startswith("docs/concept/"):
            cands.append("concept/" + q[len("docs/concept/"):])
        for r in SHIP_ROOTS:
            cands.append(r + "/" + q)
        cands.append(q)  # e.g. delivery/... named from inside delivery
    else:
        q = path[4:] if path.startswith("CBC ") else path
        cands.append(q)
    for c in cands:
        full = os.path.join(ROOT, c)
        if os.path.isdir(full):
            if os.path.exists(os.path.join(full, "README.md")):
                return os.path.join(c, "README.md").replace("//", "/")
            return c
        if os.path.exists(full):
            return c
        if glob.glob(full):
            return c
    return None

HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.M)

def headings(p):
    out = []
    for m in HEAD.finditer(strip_fences(text(p))):
        h = m.group(2)
        n = re.match(r"^(\d+(?:\.\d+)*)\.?\s+(.*)$", h)
        if n:
            out.append((n.group(1), n.group(2).strip()))
        else:
            out.append((None, h.strip()))
    return out

def norm(t):
    t = re.sub(r"[*`]", "", t)
    return re.sub(r"\s+", " ", t).strip().rstrip(".").lower()

findings = []
def report(kind, src, line, msg):
    findings.append((kind, src, line, msg))

PATHLIKE = re.compile(r"`(CBC )?((?:\.?[\w.-]+/)+[\w.<>*-]*|[\w.-]+\.(?:md|sql|yaml|yml|java|xml|properties|conf|json|part|sh))`")

for src in LIVING:
    if not src.endswith((".md", ".part", ".sql", ".yaml", ".yml", ".properties", ".conf")):
        continue
    raw = text(src)
    t = strip_fences(raw) if src.endswith(".md") else raw
    if src in HISTORY_BY_HEADER:
        t = t[: t.find("-->") + 3] if "-->" in t else t[:2000]
    lines = t.split("\n")
    offs = [0]
    for l in lines:
        offs.append(offs[-1] + len(l) + 1)
    def lineof(i):
        lo, hi = 0, len(offs) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if offs[mid + 1] <= i:
                lo = mid + 1
            else:
                hi = mid
        return lo + 1

    # 1. backticked paths
    for m in PATHLIKE.finditer(t):
        p = (m.group(1) or "") + m.group(2)
        if "<" in p or "*" in p or p.startswith(("http", "~", "/")) or "..." in p:
            continue
        if re.search(r"(^|/)(temp|devlog|docs/baselines)/", p) and not p.endswith((".md", "/")):
            pass
        if not resolve(p, src):
            report("path", src, lineof(m.start()), p)

    # 2. Fact References with a number and title
    joined = re.sub(r"\s*\n\s*", " ", t)
    jo = []  # map joined index -> original line, approximately
    for g in re.finditer(r"\(([^()]*§[^()]*)\)", joined):
        body = g.group(1)
        current = src
        for tok in re.finditer(r"`(CBC )?([^`]+)`|§(\d+(?:\.\d+)*),\s*\*([^*]+)\*", body):
            if tok.group(2) is not None:
                r = resolve((tok.group(1) or "") + tok.group(2), src)
                if r and r.endswith(".md"):
                    current = r
                elif r is None and "/" in tok.group(2):
                    current = None
                continue
            num, title = tok.group(3), tok.group(4)
            if current is None:
                continue
            hs = headings(current)
            if not any(n == num and norm(h) == norm(title) for n, h in hs):
                have = [h for n, h in hs if n == num]
                # locate the line in the original
                needle = "§" + num
                ln = next((i + 1 for i, l in enumerate(lines) if needle in l), 0)
                report("fact-ref", src, ln, f"{current} §{num} *{title}* -> heading there: {have or 'none'}")
    # unnumbered: (`path`, *Title*)
    for g in re.finditer(r"\(`(CBC )?([^`]+)`,\s*\*([^*]+)\*", joined):
        r = resolve((g.group(1) or "") + g.group(2), src)
        if not r or not r.endswith(".md"):
            continue
        title = g.group(3)
        if not any(norm(h) == norm(title) for n, h in headings(r)):
            ln = next((i + 1 for i, l in enumerate(lines) if g.group(2) in l), 0)
            report("fact-ref", src, ln, f"{r} *{title}* -> no such heading")

    # 3. ADRs cited (ours: not in shipped bodies, but in shipped footers)
    scope = t
    if shipped(src):
        k = scope.find("\n## Decisions")
        scope = scope[k:] if k >= 0 else ""
    for m in re.finditer(r"(?<!CBC )ADR-(\d{4})", scope):
        n = m.group(1)
        if not glob.glob(os.path.join(ROOT, "docs/adr", n + "-*.md")):
            report("adr", src, lineof(m.start() + (len(t) - len(scope))), "ADR-" + n)

    # 4. Foundation Lines
    for m in re.finditer(r"^\s*foundation:\s*(.+?)\s*(?:-->)?\s*$", raw, re.M):
        v = m.group(1)
        ok = False
        mm = re.fullmatch(r"(?:practice, under )?the ([\w-]+) convention", v)
        if mm:
            ok = os.path.exists(os.path.join(ROOT, "docs/conventions", mm.group(1), "README.md"))
        mm = re.fullmatch(r"the ([\w-]+) model", v)
        if mm:
            ok = os.path.exists(os.path.join(ROOT, "docs/models", mm.group(1) + ".md"))
        if v in ("concept v1", "practice, checked against concept v1"):
            ok = True
        if not ok:
            report("foundation", src, raw[: m.start()].count("\n") + 1, v)

# 5. each manual names what stands on it
stands = {}
for src in LIVING:
    try:
        raw = text(src)
    except Exception:
        continue
    for m in re.finditer(r"^\s*foundation:\s*(?:practice, under )?the ([\w-]+) convention", raw, re.M):
        stands.setdefault(m.group(1), set()).add(src)
for name, files in sorted(stands.items()):
    man = f"docs/conventions/{name}/README.md"
    t = text(man)
    a = t.find("## What this is made usable as")
    b = t.find("\n## ", a + 5)
    sec = re.sub(r"\s+", " ", t[a:b])
    for f in sorted(files):
        if f == man:
            continue
        if f not in sec and f.replace("README.md", "") not in sec:
            report("derives-list", man, 0, f"does not name {f}")

for k, s, l, msg in sorted(findings):
    print(f"{k}\t{s}:{l}\t{msg}")
print(f"# {len(findings)} hits over {len(LIVING)} files", file=sys.stderr)
