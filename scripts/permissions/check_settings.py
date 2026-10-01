"""Simulate permission-rule matching against must-allow / must-deny / must-ask commands.

Usage: python scripts/permissions/check_settings.py .claude/settings.json [Bash|PowerShell]
Exits with the mismatch count printed; 0 mismatches is the bar.
"""
import json, re, sys
p = json.load(open(sys.argv[1]))["permissions"]
TOOL = sys.argv[2] if len(sys.argv) > 2 else "Bash"
def rules(kind):
    out = []
    for r in p[kind]:
        m = re.fullmatch(TOOL + r"\((.*)\)", r)
        if m: out.append(re.compile("^" + ".*".join(re.escape(x) for x in m.group(1).split("*")) + "$", re.S))
    return out
D, A, L = rules("deny"), rules("ask"), rules("allow")
def verdict(c):
    if any(r.match(c) for r in D): return "deny"
    if any(r.match(c) for r in A): return "ask"
    if any(r.match(c) for r in L): return "allow"
    return "classifier"
P = "C:/x/clone"
must = {
 "allow": ["git switch -c feature/x", "git push origin feature/task-25-decisions", "git push origin feature/x-fix",
   "git push origin main", "git push -u origin feature/x", "git merge --ff-only feature/x", "git branch -d feature/x",
   "git push origin --delete feature/x", f"git -C {P} status", "git tag v1.0.0", "git branch --merged main",
   "git branch --no-merged main", "git branch --contains main", 'git commit -m "Clean up docs"',
   'git commit -m "Allow push to main via settings"', 'git commit -m "clean up; deny push --delete main and branch -D main via settings; reset --hard"',
   f"git -C {P} commit -m update", "backlog task edit 7 -s Done", "uvx copier copy --trust . .tmp/smoke", "rm -rf .tmp/smoke-express",
   f"git -C {P} branch -d feature/x", f"git -C {P} push origin feature/x", "git reflog", "git cherry-pick abc"],
 "deny": ["git branch -D main", "git branch -d main", "git branch -d -f main", "git branch -f -d main", "git branch --delete --force main",
   "git branch --force --delete main", "git branch -d feature/x main", 'git branch -D "main"', "git push origin --delete main",
   "git push --delete origin main", "git push -d origin main", "git push origin -d main", "git push origin :main", 'git push origin ":main"',
   "git push origin --delete refs/heads/main", "git push origin --delete feature/x main", "git push origin main --delete",
   f"git -C {P} branch -D main", f"git -C {P} branch -d -f main", f"git -C {P} push origin --delete main", "git push --mirror origin",
   "git update-ref -d refs/heads/main", "gh api -X DELETE repos/a/b/git/refs/heads/main", "gh repo delete a/b --yes",
   "git --no-pager branch -D main", "git -c core.x=y branch -D main", "git push origin refs/heads/main --delete", "git branch -m main old"],
 "ask": ["git push --force origin feature/x", "git push -f origin x", "git push origin x -f", "git push origin +feature/x",
   "git push origin v0.1.0", "git push --tags", "git push --follow-tags origin main", "git reset --hard HEAD~1", "git reset -q --hard",
   "git clean -fd", "git branch -D feature/old", "git branch -f feature/x main"],
}
bad = 0
for want, cs in must.items():
    for c in cs:
        v = verdict(c)
        if v != want: bad += 1; print(f"MISMATCH want={want} got={v}: {c}")
print("checked", sum(map(len, must.values())), "mismatches", bad)
sys.exit(1 if bad else 0)
