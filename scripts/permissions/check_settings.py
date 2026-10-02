"""Simulate permission-rule matching against must-allow / must-deny / must-ask commands.

Usage: python scripts/permissions/check_settings.py <settings.json> [Bash|PowerShell] [repo|template]
Prints the mismatch count and exits 1 when there is any; 0 mismatches is the bar.
Does not split compound commands; the real matcher checks each subcommand.
"""
import json, re, sys
p = json.load(open(sys.argv[1]))["permissions"]
TOOL = sys.argv[2] if len(sys.argv) > 2 else "Bash"
PROFILE = sys.argv[3] if len(sys.argv) > 3 else "repo"
def rules(kind):
    out = []
    for r in p.get(kind, []):
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
if PROFILE == "template":
    must = {
     "allow": ["git switch -c feature/x", "git add -A", 'git commit -m "Clean up docs; reset --hard is just words"', "git push origin main",
       "git push -u origin feature/x", "git push origin feature/x-fix", "git merge --ff-only feature/x", "git branch -d feature/x",
       "git push origin --delete feature/x", "git branch --merged main", f"git -C {P} status", f"git -C {P} commit -m x",
       "npm run check", "npm test", "npm ci", "npm install", "backlog task list", "npx backlog.md task list", "git fetch", "git pull",
       "git push origin HEAD:main", "git push origin feature/x:main"],
     "ask": ["git branch -D main", "git branch -d production", "git branch -d -f stage", "git push origin --delete main",
       "git push --delete origin dev", "git push origin :production", "git push origin HEAD:production", "git push origin feature/x:stage",
       'git branch -D "main"', f"git -C {P} branch -D main", "git branch -m main old", "git push --force origin feature/x",
       "git push -f origin x", "git push origin +feature/x", "git push --mirror origin", "git reset --hard HEAD~1", "git clean -fd",
       "git branch -D feature/old", "git branch -f feature/x main", "git switch --discard-changes main", "git switch -f main",
       "git switch -C feature/x", 'git push origin ":main"', "git push origin ':stage'", "git push origin --delete refs/heads/dev",
       "git push origin :refs/heads/production", "git push --prune origin", "git branch -M main old", "git branch -f -m main x",
       "git switch --force main", "git push origin main --delete", 'git push origin --delete "production"',
       "git push --delete origin 'stage'", 'git branch -d "production"', 'git push origin ":refs/heads/dev"',
       "git push origin HEAD:refs/heads/production", 'git push origin "feature/x:dev"', "git branch -M feature/x main",
       "git branch -C feature/x production"],
     "classifier": ["npm install lodash", "npm run dev", f"git -C {P} reflog", "git restore .", "git checkout -- a.ts", "curl https://x",
       "node -e 1", "git rebase main", "git tag v1"],
    }
bad = 0
for want, cs in must.items():
    for c in cs:
        v = verdict(c)
        if v != want: bad += 1; print(f"MISMATCH want={want} got={v}: {c}")
print("checked", sum(map(len, must.values())), "mismatches", bad)
sys.exit(1 if bad else 0)
