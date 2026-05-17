# MEMORY.md

> Operational memory.
> Strict scope: inter-session state only.
> This file is NOT governance. This is NOT a journal.
> Decisions go to DECISIONS.<slug>.md or to an ADR.
> Rules go to AGENTS.md/AGENTS.override.md or _constitution.md.

---

## Rules for this file

- **Read at the start of session** before any action.
- **Update at the end of session** or when state changes.
- **Delete an entry** as soon as it is no longer true.
- **Do not let it grow**: if a section exceeds 10 lines, it is a signal that the information belongs elsewhere.

---

## Active Feature

```
Slug    : <!-- No slug -->
Branch : <!-- No branch -->
Worktree: <!-- No worktree -->
Current task : <!-- No current task -->
Started on : <!-- No date -->
```

---

## Gate Status

| Gate | Status | Note |
|-------|--------|------|
| `$triage` | <!-- No status info --> | <!-- No Note --> |
| `$planner` | <!-- No status info --> | <!-- No Note --> |
| `$preflight` | <!-- No status info --> | <!-- No Note --> |
| `$architect` | <!-- No status info --> | <!-- No Note --> |
| `$security` | <!-- No status info --> | <!-- No Note --> |
| `$adr` | <!-- No status info --> | <!-- No Note --> |
| `$coder` | <!-- No status info --> | <!-- No Note --> |
| `$qa` | <!-- No status info --> | <!-- No Note --> |
| `$review` | <!-- No status info --> | <!-- No Note --> |
| `$doc` | <!-- No status info --> | <!-- No Note --> |
| `$release` | <!-- No status info --> | <!-- No Note --> |

---

## Active Blockers

```
<!-- No blockers currently -->
```

---

## Repository Gotchas

```
<!-- No gotchas currently -->
```

---

## Resumption Context

```
Last session : <!-- No session history --> 
Stopped on      : <!-- No stop -->
Next action  : <!-- no action -->
```

---

## Cleanup

This file must be **emptied or archived** when:
- The feature is merged → delete or archive
- A new feature slug starts → reset Active Feature and Gate Status sections
- A gotcha is fixed in the repository → delete the GOTCHA entry

**This file must never become a history log.**
