"""Check that the copies listed in dogfood.json (in this repo, or inside template/) match their template sources.

Usage: python scripts/dogfood_check.py [--sync]
Drift means a missing, differing or extra file under a mapped copy. A source that does not exist yet passes
(git does not track empty folders). --sync makes each copy match its source; the owner runs it when Claude Code
refuses an agent write under .claude/ (a protected path).
"""
import filecmp, json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNC = "--sync" in sys.argv


def files(base):
    if os.path.isfile(base):
        return {"": base}
    out = {}
    for d, _, names in os.walk(base):
        for n in names:
            full = os.path.join(d, n)
            out[os.path.relpath(full, base).replace(os.sep, "/")] = full
    return out


problems = []
for pair in json.load(open(os.path.join(ROOT, "dogfood.json"), encoding="utf-8"))["pairs"]:
    src, dst = os.path.join(ROOT, pair["source"]), os.path.join(ROOT, pair["copy"])
    if not os.path.exists(src):
        continue
    want, have = files(src), files(dst) if os.path.exists(dst) else {}
    for rel, path in want.items():
        target = dst if rel == "" else os.path.join(dst, rel)
        if rel not in have:
            problems.append(f"missing: {pair['copy']}/{rel}".rstrip("/"))
        elif not filecmp.cmp(path, have[rel], shallow=False):
            problems.append(f"differs: {pair['copy']}/{rel}".rstrip("/"))
        else:
            continue
        if SYNC:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copyfile(path, target)
    for rel in set(have) - set(want):
        problems.append(f"extra: {pair['copy']}/{rel}")
        if SYNC:
            os.remove(have[rel])

for p in problems:
    print(("fixed " if SYNC else "") + p)
print(f"{len(problems)} problem(s)" + (" fixed" if SYNC else ""))
sys.exit(1 if problems and not SYNC else 0)
