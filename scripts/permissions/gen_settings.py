"""Generate .claude/settings.json for this repo (decision 0027).

Usage: python scripts/permissions/gen_settings.py <out.json>
Agents cannot write .claude/settings.json themselves (protected path); write to a temp file and let the owner copy it.
"""
import json, sys
TOOLS = ["Bash", "PowerShell"]
# "git -C *" covers git -C <path> forms; a bare "git *" prefix would also match words inside commit messages.
GIT = ["git", "git -C *", "git --no-pager", "git -c *"]
MAINS = ["main", '"main"', "'main'"]

allow = ["Bash", "PowerShell", "Read", "Edit", "Write", "Glob", "Grep", "NotebookEdit",
         "WebFetch", "WebSearch", "Agent", "Skill", "Monitor", "Artifact"]
# Narrow rules survive auto mode (blanket Bash/PowerShell/Agent/Monitor rules are dropped there).
subs = ["status", "log", "diff", "show", "rev-parse", "rev-list", "branch", "switch", "checkout",
        "restore", "add", "rm", "mv", "commit", "merge", "merge-base", "push", "pull", "fetch",
        "stash", "worktree", "remote", "tag", "ls-files", "ls-remote", "config --get", "init", "clone",
        "reflog", "blame", "grep", "describe", "for-each-ref", "cat-file", "check-ignore",
        "cherry-pick", "revert"]
cmds = []
for s in subs:
    cmds += [f"git {s}", f"git {s} *"]
cmds += ["git -C *", "backlog *", "npx backlog.md *", "uvx copier *", "pushover *",
         "gh run *", "gh workflow *", "gh repo view *", "gh auth status",
         "npm ci", "npm install", "npm test", "npm run check", "npm run typecheck",
         "npm run lint", "npm run format", "npm run format:check", "npm run test", "npm run build",
         "rm -rf .tmp/*", "mkdir *", "cp *", "mv *"]
for t in TOOLS:
    allow += [f"{t}({c})" for c in cmds]
allow += ["PowerShell(Remove-Item -Recurse -Force .tmp*)"]

deny = []
for t in TOOLS:
    for g in GIT:
        for m in MAINS:
            for tail in ["", " *"]:
                for f in ["-d", "-D", "--delete"]:
                    deny += [f"{t}({g} branch {f}* {m}{tail})", f"{t}({g} branch * {f}* {m}{tail})"]
                deny += [f"{t}({g} push *-d* {m}{tail})", f"{t}({g} push * :{m}{tail})"]
            deny += [f"{t}({g} push * {m} *-d*)"]
        deny += [f"{t}({g} push * refs/heads/main *-d*)", f"{t}({g} branch -m main*)", f"{t}({g} branch -M main*)",
                 f"{t}({g} branch --move main*)", f"{t}({g} branch * -m main*)", f"{t}({g} branch * -M main*)",
                 f"{t}({g} push * \":main\"*)", f"{t}({g} push * ':main'*)",
                 f"{t}({g} push *-d* refs/heads/main*)", f"{t}({g} push * :refs/heads/main*)",
                 f"{t}({g} push *--mirror*)", f"{t}({g} push *--prune*)",
                 f"{t}({g} update-ref -d refs/heads/main*)", f"{t}({g} update-ref --stdin*)"]
    deny += [f"{t}(gh api *refs/heads/main*)", f"{t}(gh api graphql*deleteRef*)", f"{t}(gh repo delete*)"]

ask = []
for t in TOOLS:
    for g in GIT:
        ask += [f"{t}({g} push *--force*)", f"{t}({g} push -f *)", f"{t}({g} push * -f)", f"{t}({g} push * -f *)",
                f"{t}({g} push * +*)", f"{t}({g} push *--tags*)", f"{t}({g} push *--follow-tags*)",
                f"{t}({g} push * refs/tags/*)", f"{t}({g} push * v*)",
                f"{t}({g} reset *--hard*)", f"{t}({g} clean -*)",
                f"{t}({g} branch -D *)", f"{t}({g} branch *--force*)", f"{t}({g} branch -f *)",
                f"{t}({g} branch * -f *)", f"{t}({g} branch * -f)"]

out = {"$schema": "https://json.schemastore.org/claude-code-settings.json",
       "permissions": {"allow": allow, "deny": deny, "ask": ask}}
json.dump(out, open(sys.argv[1], "w", encoding="utf-8", newline="\n"), indent=2)
print({k: len(v) for k, v in out["permissions"].items()})
