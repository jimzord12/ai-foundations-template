"""Generate Claude Code permission settings.

Profiles:
  repo      .claude/settings.json for this repo (decision 0027): everything allowed, deleting main denied.
  template  template/.claude/settings.json for generated projects (decisions 0021, 0024, 0029, 0031):
            a narrow allowlist, and the AGENTS.md ask-first list as ask rules.

Usage: python scripts/permissions/gen_settings.py <out.json> [repo|template]
Agents cannot write .claude/settings.json themselves (protected path); write to a temp file and let the owner copy it.
"""
import json, sys
PROFILE = sys.argv[2] if len(sys.argv) > 2 else "repo"
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

if PROFILE == "template":
    # Owner answer 5 (0021) amended by 0024: read-only tools, package scripts, backlog, git add/commit/push and
    # the branch commands; nothing broader. No blanket entries (auto mode drops them) and no bare "git -C *".
    allow = ["Read", "Glob", "Grep"]
    tsubs = ["status", "log", "diff", "show", "add", "commit", "push", "switch", "branch", "merge", "fetch", "pull"]
    tcmds = []
    for s_ in tsubs:
        tcmds += [f"git {s_}", f"git {s_} *", f"git -C * {s_}", f"git -C * {s_} *"]
    tcmds += ["npm ci", "npm install", "npm test", "npm run check", "npm run typecheck", "npm run lint",
              "npm run format", "npm run format:check", "npm run test", "npm run build",
              "backlog *", "npx backlog.md *"]
    for t in TOOLS:
        allow += [f"{t}({c})" for c in tcmds]
    # The ask-first list of template AGENTS.md "Git and safety"; nothing is denied outright.
    CORES = ["main", "production", "stage", "dev"]
    deny = []
    ask = []
    for t in TOOLS:
        for g in ["git", "git -C *"]:
            for core in CORES:
                names = [core, f'"{core}"', f"'{core}'"]
                for m in names:
                    for tail in ["", " *"]:
                        for f in ["-d", "-D", "--delete"]:
                            ask += [f"{t}({g} branch {f}* {m}{tail})", f"{t}({g} branch * {f}* {m}{tail})"]
                for m in names + [f"refs/heads/{core}", f'"refs/heads/{core}"']:
                    for tail in ["", " *"]:
                        ask += [f"{t}({g} push *-d* {m}{tail})", f"{t}({g} push * :{m}{tail})"]
                    ask += [f"{t}({g} push * {m} *-d*)"]
                ask += [f"{t}({g} push * refs/heads/{core} *-d*)", f"{t}({g} push *-d* refs/heads/{core}*)",
                        f"{t}({g} push * :refs/heads/{core}*)", f"{t}({g} push * \":{core}\"*)", f"{t}({g} push * ':{core}'*)",
                        f"{t}({g} branch -m {core}*)", f"{t}({g} branch -M {core}*)", f"{t}({g} branch --move {core}*)",
                        f"{t}({g} branch * -m {core}*)", f"{t}({g} branch * -M {core}*)",
                        f"{t}({g} push * \":refs/heads/{core}\"*)"]
                for f in ["-m", "-M", "-c", "-C", "--move", "--copy"]:
                    ask += [f"{t}({g} branch {f} * {core})"]
            for core in CORES[1:]:
                ask += [f"{t}({g} push * *:{core})", f"{t}({g} push * *:{core} *)", f"{t}({g} push * HEAD:{core}*)",
                        f"{t}({g} push * *:refs/heads/{core}*)", f"{t}({g} push * \"*:{core}\"*)"]
            ask += [f"{t}({g} push *--force*)", f"{t}({g} push -f *)", f"{t}({g} push * -f)", f"{t}({g} push * -f *)",
                    f"{t}({g} push * +*)", f"{t}({g} push *--mirror*)", f"{t}({g} push *--prune*)",
                    f"{t}({g} reset *--hard*)", f"{t}({g} clean -*)",
                    f"{t}({g} branch -D *)", f"{t}({g} branch *--force*)", f"{t}({g} branch -f *)",
                    f"{t}({g} branch * -f *)", f"{t}({g} branch * -f)",
                    f"{t}({g} switch *--discard-changes*)", f"{t}({g} switch -f*)", f"{t}({g} switch --force*)",
                    f"{t}({g} switch -C *)"]

out = {"$schema": "https://json.schemastore.org/claude-code-settings.json",
       "permissions": {"allow": allow, "deny": deny, "ask": ask}}
json.dump(out, open(sys.argv[1], "w", encoding="utf-8", newline="\n"), indent=2)
print({k: len(v) for k, v in out["permissions"].items()})
