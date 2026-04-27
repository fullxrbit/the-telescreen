# Task ID: TASK-002
**Created Date:** 2026-04-27
**Last Modified:** 2026-04-27
**Current Agent:** Codex
**Task Type:** Feature

## Objective & Success

**Primary Objective:** Add a terminal port that appears when opening `main.py` and helps developers test project data and inspect basic intelligence.

**Success Criteria:**
- Running `python main.py` opens an interactive developer console.
- The console can initialize the local database.
- The console can show database status and request counts.
- The console can add and list notification requests for local testing.
- Existing direct database initialization remains available.

**Definition of Done:**
- [x] Terminal port opens from `main.py` by default.
- [x] `terminal-port` command is available explicitly.
- [x] Database intelligence view exists.
- [x] Request creation and listing are available from the terminal.
- [x] Documentation is updated.
- [x] Code compiles.

## Current State Analysis

**What Exists Now:** The project has an interactive terminal port for local developer testing.

**Code Locations:**
- `main.py`: Opens the terminal port by default and still supports `init-db`.
- `back/terminal_port.py`: Contains the interactive menu and developer actions.
- `back/database.py`: Provides database status, request creation, request listing, and initialization helpers.

**Database Schema:** Reuses the existing SQLite `requests` table.

**Configuration:** Uses the default SQLite path `data/telescreen.sqlite`.

**Known Issues:** The terminal port is intentionally local and developer-facing. It is not a production user interface and does not include authentication, validation beyond required text fields, or advanced intelligence gathering yet.

## Implementation Roadmap

### Phase 1: Terminal Entry Point - Make `main.py` useful when opened
**Dependencies:** Existing CLI structure.

**Sub-tasks:**
- **1.1** Make `python main.py` open the terminal port - Completed.
- **1.2** Keep `python main.py init-db` available - Completed.

### Phase 2: Developer Actions - Add practical local testing tools
**Dependencies:** Existing database helpers.

**Sub-tasks:**
- **2.1** Add database initialization action - Completed.
- **2.2** Add database intelligence action - Completed.
- **2.3** Add request creation action - Completed.
- **2.4** Add request listing action - Completed.

### Phase 3: Documentation and Validation - Make the feature discoverable
**Dependencies:** Phase 1 and Phase 2.

**Sub-tasks:**
- **3.1** Update README usage notes - Completed.
- **3.2** Update architecture outline - Completed.
- **3.3** Compile and smoke test the terminal port - Completed.

## Progress Tracking

**Overall Progress:** 3/3 phases completed
**Current Phase:** Complete

**Phase Status:**
- Phase 1: Complete
- Phase 2: Complete
- Phase 3: Complete

**Last Activity:** Added the interactive terminal port and updated related documentation.
**Last Updated:** 2026-04-27

## Technical Context

**Architecture Overview:** `main.py` is now both a direct CLI utility entry point and the default launcher for a local developer console. The terminal port calls backend database helpers directly.

**Key Technologies:** Python standard library: `argparse` and terminal `input()`.

**File Structure:** Terminal logic lives in `back/terminal_port.py` so `main.py` stays small.

**Entry Points:**
- `python main.py`: opens the terminal port.
- `python main.py terminal-port`: opens the terminal port explicitly.
- `python main.py init-db`: initializes the database directly.

**Environment Setup:** Requires Python. No third-party dependencies are needed.

## Validation & Testing

**Automated Tests:** None yet.

**Manual Testing:** Compile with `python -m compileall main.py back` and run `python main.py`, then choose menu actions.

**Test Data:** Developers can create test notification requests from the terminal port.

**Edge Cases:** Unknown menu choices are rejected and required text prompts repeat until a value is provided.

## Deployment & Cleanup

**Deployment Checklist:**
- [x] Keep feature local and dependency-free.
- [x] Preserve existing initialization command.

**Documentation Updates:** Updated `README.md`, `agents/architecture/OUTLINE.md`, `agents/architecture/AGENTS_ARCHITECTURE.md`, and `agents/tasks/AGENTS_TASKS.md`.

**Cleanup Tasks:** None.

**Handoff Notes:** Future intelligence-gathering features can be added as new actions in `back/terminal_port.py`.

## Agent Notes

**Decisions Made:** The terminal port was implemented as a backend module instead of packing all interaction logic into `main.py`.

**Challenges Encountered:** The requested "intelligence" feature is broad, so this first version focuses on concrete local project intelligence: database path, existence, size, tables, and stored request count.

**Alternative Approaches:** A web dashboard was not added because the request specifically points to `main.py` and terminal usage.

**Next Agent Instructions:** Add new terminal actions by extending the `_actions` mapping in `TerminalPort`.
