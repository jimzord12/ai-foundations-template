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
        # Claude Code matches PowerShell rules case-insensitively.
        if m: out.append(re.compile("^" + ".*".join(re.escape(x) for x in m.group(1).split("*")) + "$", re.S | (re.I if TOOL == "PowerShell" else 0)))
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
   f"git -C {P} branch -d feature/x", f"git -C {P} push origin feature/x", "git reflog", "git cherry-pick abc",
   # Formerly asked; allowed since decision 0042 (this repo asks nothing).
   "git push --force origin feature/x", "git push -f origin x", "git push origin x -f", "git push origin +feature/x",
   "git push origin v0.1.0", "git push --tags", "git push --follow-tags origin main", "git reset --hard HEAD~1", "git reset -q --hard",
   "git clean -fd", "git branch -f feature/x main"],
 "deny": ["git branch -D main", "git branch -d main", "git branch -d -f main", "git branch -f -d main", "git branch --delete --force main",
   "git branch --force --delete main", "git branch -d feature/x main", 'git branch -D "main"', "git push origin --delete main",
   "git push --delete origin main", "git push -d origin main", "git push origin -d main", "git push origin :main", 'git push origin ":main"',
   "git push origin --delete refs/heads/main", "git push origin --delete feature/x main", "git push origin main --delete",
   f"git -C {P} branch -D main", f"git -C {P} branch -d -f main", f"git -C {P} push origin --delete main", "git push --mirror origin",
   "git update-ref -d refs/heads/main", "gh api -X DELETE repos/a/b/git/refs/heads/main", "gh repo delete a/b --yes",
   "git --no-pager branch -D main", "git -c core.x=y branch -D main", "git push origin refs/heads/main --delete", "git branch -m main old"],
 "ask": [],
}
if PROFILE == "template":
    must = {
     "allow": ["git switch -c feature/x", "git add -A", 'git commit -m "Clean up docs; reset --hard is just words"', "git push origin main",
       "git push -u origin feature/x", "git push origin feature/x-fix", "git merge --ff-only feature/x", "git branch -d feature/x",
       "git push origin --delete feature/x", "git branch --merged main", f"git -C {P} status", f"git -C {P} commit -m x",
       "npm run check", "npm test", "npm ci", "npm install", "backlog task list", "npx backlog.md task list", "git fetch", "git pull",
       "git push origin HEAD:main", "git push origin feature/x:main", "git branch -d feature/x", "git switch -c feature/y",
       "git worktree add -b lab/LAB-1-x .claude/worktrees/LAB-1-x abc1234", "git worktree list", "git worktree remove .claude/worktrees/LAB-1-x",
       "git worktree prune", f"git -C {P} worktree list", "git tag lab-closed/LAB-1-x lab/LAB-1-x", "git tag", "git tag --list 'lab-*'",
       "git push origin lab-closed/LAB-1-x", f"git -C {P} tag v1", 'git tag -a lab-closed/x lab/x -m "evidence"',
       "git tag -l --format=%(refname)", "git worktree add -b lab/LAB-2-y .claude/worktrees/LAB-2-y main",
       "git worktree add -b lab/LAB-3-variant-b .claude/worktrees/LAB-3-variant-b main", "git worktree add -b x ../x-b main",
       "git worktree add -b lab/LAB-4-plan-B .claude/worktrees/LAB-4-plan-B 1a2b3c4",
       "git worktree add .claude/worktrees/LAB-5-x -b lab/LAB-5-x main"],
     "ask": ["git branch -D main", "git branch -d production", "git branch -d -f stage", "git push origin --delete main",
       "git push --delete origin dev", "git push origin :production", "git push origin HEAD:production", "git push origin feature/x:stage",
       'git branch -D "main"', f"git -C {P} branch -D main", "git branch -m main old", "git push --force origin feature/x",
       "git push -f origin x", "git push origin +feature/x", "git push --mirror origin", "git reset --hard HEAD~1", "git clean -fd",
       "git branch -f feature/x main", "git switch --discard-changes main", "git switch -f main", 'git push origin ":main"', "git push origin ':stage'", "git push origin --delete refs/heads/dev",
       "git push origin :refs/heads/production", "git push --prune origin", "git branch -M main old", "git branch -f -m main x",
       "git switch --force main", "git push origin main --delete", 'git push origin --delete "production"',
       "git push --delete origin 'stage'", 'git branch -d "production"', 'git push origin ":refs/heads/dev"',
       "git push origin HEAD:refs/heads/production", 'git push origin "feature/x:dev"', "git branch -M feature/x main",
       "git branch -C feature/x production", "git push origin 'HEAD:production'", "git push origin dev", "git push -u origin stage",
       "git switch -C main", "git switch -C production origin/production", "git switch --force-create stage", "git push origin --delete 'refs/heads/main'", "git push origin ':refs/heads/dev'",
       'git push origin "+main"', "git push origin '+feature/x'",
       "git worktree remove --force .claude/worktrees/x", "git worktree remove -f .claude/worktrees/x", "git worktree remove .claude/worktrees/x --force",
       "git worktree remove .claude/worktrees/x -f", f"git -C {P} worktree remove --force x", "git tag -d lab-closed/x", "git tag --delete x",
       "git tag -f lab-closed/x lab/x", "git tag --force x", f"git -C {P} tag -d x",
       "git tag x -d", "git tag lab-closed/x --delete", "git tag -a -f v1 -m m", "git tag -fa v1", "git tag v1 HEAD -f",
       "git tag -a v1 --force", "git tag -s -f v1", "git worktree remove -ff x", f"git -C {P} tag x -d",
       "git worktree add -B main ../x HEAD~1", "git worktree add -B production ../p HEAD", "git worktree add -f -B main ../x HEAD",
       'git worktree add -B "dev" ../x HEAD', f"git -C {P} worktree add -B stage ../x HEAD"],
     "classifier": ["npm install lodash", "npm run dev", f"git -C {P} reflog", "git restore .", "git checkout -- a.ts", "curl https://x",
       "node -e 1", "git rebase main", "git stash"],
    }
    if TOOL == "Bash":
        must["ask"] += ["git branch -D feature/old", "git switch -C feature/x", "git worktree add -B feature/x ../x HEAD~1"]
if PROFILE == "repo":
    must["allow"] += ["git branch -D feature/old"]  # decision 0042: nothing asks in this repo
bad = 0
if PROFILE == "repo" and p.get("ask"):  # decision 0042: this repo asks nothing
    bad += 1; print(f"MISMATCH: the repo profile must have no ask rules, found {len(p['ask'])}")
for want, cs in must.items():
    for c in cs:
        v = verdict(c)
        if v != want: bad += 1; print(f"MISMATCH want={want} got={v}: {c}")
print("checked", sum(map(len, must.values())), "mismatches", bad)
sys.exit(1 if bad else 0)
