# the-telescreen Architecture Outline

## General Overview

`the-telescreen` is an event notification app. Its goal is to let users describe information they want monitored on the web, then eventually use a Linux VPS to check relevant sources periodically and notify users when matching events are announced.

Current system flow:

```text
User notification request
        |
        v
Python backend utilities
        |
        v
Developer terminal port
        |
        v
SQLite database: back/data/telescreen.sqlite
        |
        v
Future web monitoring and notification services
```

At this stage, the project contains the first persistence layer and a local developer terminal port. The backend can initialize a local SQLite database, create a `requests` table for user notification requests, inspect basic database intelligence, and create or list test notification requests from the terminal. Monitoring, scraping, notification delivery, authentication, and frontend implementation are still pending.

## Dependencies and External Libraries

- Python standard library
  - Used for the current backend implementation.
  - `argparse` powers the local command-line entry point in `main.py`.
  - `pathlib` handles project-relative database paths.
  - `sqlite3` provides the local relational database without requiring an external database server.
  - Terminal `input()` powers the local interactive developer terminal port.

There are currently no third-party Python dependencies.

## Project Structure

```text
agents/
  AGENTS.md
  architecture/
    AGENTS_ARCHITECTURE.md
    OUTLINE.md
  tasks/
    AGENTS_TASKS.md
    1_2026-04-27_database-initialization.md
    2_2026-04-27_terminal-port.md
back/
  __init__.py
  bridge_back.py
  controllers.py
  data/
    .gitkeep
  database.py
  terminal_port.py
front/
  bridge_front.md
  VIEWS.md
main.py
README.md
```

### `agents/`

Contains instructions and handoff documentation for agents and developers. This area explains how work should be tracked and how architecture documentation must be kept current.

### `back/`

Contains backend Python code. The current backend responsibility is local database initialization, simple request persistence helpers, and the developer terminal port.

### `back/data/`

Holds local backend runtime database files. The SQLite database is created at `back/data/telescreen.sqlite` when `python main.py init-db` is run. Database files are ignored by git; `.gitkeep` exists only so the directory can be tracked.

### `front/`

Placeholder for future frontend code, bridge notes, and view documentation. There is no implemented frontend yet.

### `main.py`

Project command-line entry point. Running `python main.py` opens the developer terminal port. Direct utility commands are still available, including `python main.py init-db`.

## File-by-File Explanation

### `main.py`

High-level summary:

`main.py` exposes local command-line utilities and opens the developer terminal port by default.

More detailed explanation:

It defines an `argparse` parser with direct commands. Running `python main.py` or `python main.py terminal-port` calls `back.terminal_port.run_terminal_port()` and opens an interactive local console. Running `python main.py init-db` calls `back.database.initialize_database`, creates the local SQLite database if needed, creates the `requests` table if needed, and prints the database path. The `init-db` command accepts an optional `--database-path` argument for custom local database locations.

### `back/terminal_port.py`

High-level summary:

Provides the interactive terminal port for local developer testing and project intelligence.

More detailed explanation:

The module defines `TerminalPort`, a small menu-driven console. It can initialize the database, show database intelligence, add a test notification request, list stored notification requests, and exit. The database intelligence currently includes the SQLite path, whether the file exists, file size, table names, and stored request count. This is a local developer tool, not an end-user interface.

### `back/bridge_back.py`

High-level summary:

Placeholder notes for future backend bridge logic.

More detailed explanation:

The file currently contains comments describing a future backend bridge that will coordinate communication between the frontend and backend, including database communication and data transformations. It has no executable behavior yet.

### `back/__init__.py`

High-level summary:

Marks `back` as a Python package.

More detailed explanation:

This allows modules such as `main.py` to import backend code using package-style imports like `from back.database import initialize_database`.

### `back/controllers.py`

High-level summary:

Placeholder for future backend controller logic.

More detailed explanation:

The file currently has no implemented behavior. It is expected to eventually contain application-facing coordination logic between user inputs, database operations, web monitoring, and notifications.

### `back/database.py`

High-level summary:

Owns SQLite database setup and request persistence helpers.

More detailed explanation:

The module defines `DEFAULT_DATABASE_PATH` as `back/data/telescreen.sqlite`. `initialize_database()` creates the database folder and the initial `requests` table. The `requests` table currently contains only the requested notification fields:

- `user_id`
- `request_title`
- `request_summary`
- `information_source_analysis`

`get_connection()` opens SQLite connections and configures rows as dictionary-like objects. `create_request()` inserts a notification request and returns the SQLite row id. `list_requests()` reads stored requests ordered by SQLite `rowid`. `get_database_status()` returns metadata used by the terminal port, including database path, file existence, size, table names, and request count.

The table intentionally does not add extra project tables yet. SQLite's implicit `rowid` is used for simple local identification until the project needs a formal request id strategy.

### `front/VIEWS.md`

High-level summary:

Placeholder documentation for future frontend views.

More detailed explanation:

The file currently states that frontend code will live in the `front` area. No frontend application has been implemented yet.

### `front/bridge_front.md`

High-level summary:

Placeholder for future frontend bridge documentation.

More detailed explanation:

The file currently has no content. It is expected to describe how the frontend communicates with backend bridge logic once that part of the project is implemented.

### `agents/AGENTS.md`

High-level summary:

Entry point for agent and developer instructions.

More detailed explanation:

It tells contributors to read task, architecture, and project documentation before making changes, and to keep documentation aligned with code changes.

### `agents/architecture/AGENTS_ARCHITECTURE.md`

High-level summary:

Defines how architecture documentation must be maintained.

More detailed explanation:

It requires `OUTLINE.md` to stay up to date and reflect the real project state, including dependencies, structure, file responsibilities, and incomplete areas.

### `agents/tasks/AGENTS_TASKS.md`

High-level summary:

Defines the task file template and task handoff rules.

More detailed explanation:

It describes how to name task files, what sections they should include, and how agents should update task progress and handoff notes.

### `agents/tasks/1_2026-04-27_database-initialization.md`

High-level summary:

Task record for the first database initialization work.

More detailed explanation:

It documents the objective, implementation roadmap, validation steps, decisions, and completion status for creating the SQLite database initialization flow and `requests` table.

### `agents/tasks/2_2026-04-27_terminal-port.md`

High-level summary:

Task record for the terminal port feature.

More detailed explanation:

It documents the objective, roadmap, validation, and handoff notes for adding the interactive developer terminal port that appears when running `main.py`.

## Current Limitations and Pending Work

- There is no frontend implementation yet.
- There is no VPS integration yet.
- There is no web monitoring or scraping logic yet.
- There is no notification delivery system yet.
- There is no user authentication model yet.
- There are no automated tests yet.
- The terminal port only provides local database testing and basic database intelligence.
- The database schema is intentionally minimal and only stores notification requests.
