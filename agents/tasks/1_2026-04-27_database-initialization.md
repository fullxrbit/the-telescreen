# Task ID: TASK-001
**Created Date:** 2026-04-27
**Last Modified:** 2026-04-27
**Current Agent:** Codex
**Task Type:** Setup

## Objective & Success

**Primary Objective:** Initialize a working local database for storing user notification requests.

**Success Criteria:**
- The project can create a local database.
- The database contains a `requests` table.
- The `requests` table can store `user_id`, `request_title`, `request_summary`, and `information_source_analysis`.
- Basic documentation explains how to initialize the database and where request data is stored.

**Definition of Done:**
- [x] Database initialization code exists.
- [x] `requests` table schema exists.
- [x] Local initialization command exists.
- [x] Documentation is updated.
- [x] Initialization is verified locally.

## Current State Analysis

**What Exists Now:** The project now has a minimal SQLite-backed persistence layer.

**Code Locations:**
- `main.py`: CLI entry point with the `init-db` command.
- `back/database.py`: SQLite connection, schema initialization, and request helper functions.
- `back/__init__.py`: Marks the backend as a Python package.
- `back/data/.gitkeep`: Keeps the runtime backend data directory in git while database files remain ignored.

**Database Schema:** SQLite database at `back/data/telescreen.sqlite` with one table:

```sql
CREATE TABLE IF NOT EXISTS requests (
    user_id TEXT NOT NULL,
    request_title TEXT NOT NULL,
    request_summary TEXT NOT NULL,
    information_source_analysis TEXT NOT NULL
);
```

**Configuration:** Uses the default database path `back/data/telescreen.sqlite`. A custom path can be passed with `python main.py init-db --database-path <path>`.

**Known Issues:** There are no automated tests yet. The schema is intentionally minimal and does not include authentication, request status, scheduling, or notification delivery metadata.

## Implementation Roadmap

### Phase 1: Choose Persistence Approach - Select a local database
**Dependencies:** Current project structure and architecture docs.

**Sub-tasks:**
- **1.1** Review existing backend structure - Completed.
- **1.2** Choose SQLite for local development - Completed.

### Phase 2: Implement Initialization - Create the first schema
**Dependencies:** Phase 1.

**Sub-tasks:**
- **2.1** Add `back/database.py` - Completed.
- **2.2** Add `requests` table schema - Completed.
- **2.3** Add local CLI command - Completed.

### Phase 3: Document and Validate - Make the change usable by the next agent
**Dependencies:** Phase 2.

**Sub-tasks:**
- **3.1** Update README setup instructions - Completed.
- **3.2** Update architecture documentation - Completed.
- **3.3** Run local initialization and inspect schema - Completed.

## Progress Tracking

**Overall Progress:** 3/3 phases completed
**Current Phase:** Complete

**Phase Status:**
- Phase 1: Complete
- Phase 2: Complete
- Phase 3: Complete

**Last Activity:** Added SQLite initialization flow, request persistence helpers, and related documentation.
**Last Updated:** 2026-04-27

## Technical Context

**Architecture Overview:** The backend currently exposes local Python utilities. SQLite stores notification request data in a local file. Future controllers can call `back.database.create_request()` and `back.database.list_requests()`.

**Key Technologies:** Python standard library: `sqlite3`, `argparse`, and `pathlib`.

**File Structure:** Runtime database files are stored under `back/data/`. Backend persistence code is stored under `back/`.

**Entry Points:** Run `python main.py init-db` from the project root.

**Environment Setup:** Requires Python. No third-party dependencies are needed for this task.

## Validation & Testing

**Automated Tests:** None yet.

**Manual Testing:** Run `python main.py init-db`, then inspect the SQLite schema to confirm the `requests` table exists with the required columns.

**Test Data:** No seed data is required.

**Edge Cases:** Running initialization multiple times should be safe because the schema uses `CREATE TABLE IF NOT EXISTS`.

## Deployment & Cleanup

**Deployment Checklist:**
- [x] Keep generated database files out of git.
- [x] Keep the data directory available with `.gitkeep`.

**Documentation Updates:** Updated `README.md`, `agents/architecture/AGENTS_ARCHITECTURE.md`, `agents/architecture/OUTLINE.md`, and `agents/tasks/AGENTS_TASKS.md`.

**Cleanup Tasks:** None.

**Handoff Notes:** The next backend task can build on `back/database.py` instead of creating a second persistence path.

## Agent Notes

**Decisions Made:** SQLite was selected because the current project has no third-party dependencies, no running backend framework yet, and needs a simple local database that can be initialized immediately.

**Challenges Encountered:** The project started with empty backend files, so the database layer was introduced as a small module instead of being wired into a non-existent framework.

**Alternative Approaches:** A server database such as PostgreSQL was not introduced because it would add setup complexity before the architecture needs it.

**Next Agent Instructions:** Read `agents/architecture/OUTLINE.md` before extending storage. If new tables, dependencies, or flows are added, update `OUTLINE.md` in the same task.
