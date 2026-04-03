# DevOps in Production

> Build, verify, commit, deliver.

## Responsibilities

- Build verification after each implementation step
- Test execution
- Git commit workflow
- Delivery pipeline

## Build Verification

After every implementation step:
- Run the build
- Verify compilation / no errors
- Run existing tests (if test suite exists)

## Commit Workflow

```bash
git add <changed-files>    # Only specific files, NOT git add .
git commit -m "<type>(<scope>): <description>

<what and why>"
```

### Commit Rules

- Directly to main (no feature branches for plans, unless explicitly desired)
- Meaningful messages (what AND why)
- Only stage changed files — never `git add .`
- Build must be successful before committing

### Commit Convention for Plans

```
ctx(NNN): <short description>     ← Context phase
exp(NNN): <short description>     ← Exploration phase
prd(NNN): <short description>     ← Production phase
```

## AI Behavior

### MUST
- Verify build after each implementation step
- Wait for explicit commit request from the human
- Stage specific files (not `git add .`)
- Write meaningful commit messages

### MUST NOT
- Commit without being asked
- Push without being asked
- Force-push
- Skip git hooks (`--no-verify`)
- Commit code that does not compile

## Multi-Agent: Branch and Merge Workflow

When multiple agents work in parallel on separate branches, production delivery follows a branch-based workflow:

### Branch Strategy

- Each agent works on its own feature branch (e.g., `feature/auth`, `feature/dashboard`)
- Commits go to the feature branch, not to main
- The commit convention includes the branch context: `prd(NNN): <description>`

### Pull Request as Merge Gate

After G3 is passed, the agent's work is delivered via pull request:

1. Agent pushes its feature branch
2. Agent creates a PR against main
3. **Human reviews** the PR — this is the merge decision point
4. Human resolves merge conflicts (especially in shared artifacts: CLAUDE.md, Architecture docs, ADRs)
5. Human merges after verification

### Post-Merge Responsibilities

After merge, the human (or a designated agent on main) ensures:
- CLAUDE.md reflects the merged changes
- No contradictory ADRs exist
- Shared architecture docs are consistent
- No regressions from combined changes

## Checklist

- [ ] Build is successful
- [ ] Tests pass (if applicable)
- [ ] Commit uses specific file staging
- [ ] Commit message is meaningful
- [ ] Human authorized the commit
- [ ] Feature branch is up to date with main before PR (multi-agent scenarios)
- [ ] PR created for human review (multi-agent scenarios)
