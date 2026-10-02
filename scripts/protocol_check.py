"""Check the protocol cards: the YAML header at the top of every file in template/docs/protocols/.

Usage: python scripts/protocol_check.py
Fails when a card is missing or malformed, names an agent, skill or protocol that does not exist, when an agent
profile or shared skill belongs to no card, or when a protocol is not routed from template/AGENTS.md.jinja.
The card format is documented in template/docs/protocols/agents.md "Protocol cards".
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, "template")
PROTOCOLS = os.path.join(T, "docs", "protocols")
AGENTS_DIR = os.path.join(T, ".claude", "agents")
SKILLS_DIR = os.path.join(T, ".claude", "skills")
ROUTER = os.path.join(T, "AGENTS.md.jinja")

COMMON = ["protocol", "kind", "status", "summary", "applies-when"]
PROCESS_ONLY = ["ends-when", "produces"]
LISTS = ["agents", "skills", "related"]
KINDS = {"process", "rule"}
STATUSES = {"draft", "active", "retired"}


def read_card(path):
    """Return the card as a dict, or raise ValueError. Only `key: value` and `key: [a, b]` lines are allowed."""
    lines = open(path, encoding="utf-8").read().splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("no card: the file must start with a --- line")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("card is not closed with a --- line")
    card = {}
    for line in lines[1:end]:
        m = re.fullmatch(r"([a-z-]+): (.+)", line)
        if not m:
            raise ValueError(f"cannot read card line: {line!r}")
        key, value = m.groups()
        if key in card:
            raise ValueError(f"duplicate key: {key}")
        if value.startswith("["):
            if not value.endswith("]"):
                raise ValueError(f"{key}: unclosed list")
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        card[key] = value
    return card


def names(folder, suffix=""):
    out = set()
    for n in os.listdir(folder):
        if suffix and n.endswith(suffix):
            out.add(n[: -len(suffix)])
        elif not suffix and os.path.isfile(os.path.join(folder, n, "SKILL.md")):
            out.add(n)
    return out


agents, skills = names(AGENTS_DIR, ".md"), names(SKILLS_DIR)
router = open(ROUTER, encoding="utf-8").read()
files = sorted(f for f in os.listdir(PROTOCOLS) if f.endswith(".md"))
ids = {f[:-3] for f in files}
problems, claimed = [], {"agents": set(), "skills": set()}

for f in files:
    pid, where = f[:-3], f"template/docs/protocols/{f}"
    try:
        card = read_card(os.path.join(PROTOCOLS, f))
    except ValueError as e:
        problems.append(f"{where}: {e}")
        continue
    kind = card.get("kind")
    required = COMMON + LISTS + (PROCESS_ONLY if kind == "process" else [])
    for key in required:
        if key not in card:
            problems.append(f"{where}: missing {key}")
    for key in card:
        if key not in COMMON + PROCESS_ONLY + LISTS:
            problems.append(f"{where}: unknown key {key}")
        elif key in PROCESS_ONLY and kind != "process":
            problems.append(f"{where}: {key} is for process cards only")
        elif (key in LISTS) != isinstance(card[key], list):
            problems.append(f"{where}: {key} must {'be' if key in LISTS else 'not be'} a list")
    if card.get("protocol") != pid:
        problems.append(f"{where}: protocol must be {pid!r}")
    if kind not in KINDS:
        problems.append(f"{where}: kind must be one of {sorted(KINDS)}")
    if card.get("status") not in STATUSES:
        problems.append(f"{where}: status must be one of {sorted(STATUSES)}")
    for key, known in (("agents", agents), ("skills", skills), ("related", ids - {pid})):
        for name in card.get(key, []) if isinstance(card.get(key), list) else []:
            if name not in known:
                problems.append(f"{where}: {key} names {name!r}, which does not exist")
            elif key in claimed:
                claimed[key].add(name)
    if card.get("status") != "retired" and f"docs/protocols/{f}" not in router:
        problems.append(f"{where}: not routed from template/AGENTS.md.jinja")

for key, known in (("agents", agents), ("skills", skills)):
    for name in sorted(known - claimed[key]):
        problems.append(f"{key[:-1]} {name!r} belongs to no protocol card")

for p in problems:
    print(p)
print(f"{len(files)} protocol cards checked, {len(problems)} problem(s).")
sys.exit(1 if problems else 0)
