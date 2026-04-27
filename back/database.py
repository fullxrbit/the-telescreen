"""SQLite database initialization and request storage helpers."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATABASE_PATH = PROJECT_ROOT / "data" / "telescreen.sqlite"


REQUESTS_SCHEMA = """
CREATE TABLE IF NOT EXISTS requests (
    user_id TEXT NOT NULL,
    request_title TEXT NOT NULL,
    request_summary TEXT NOT NULL,
    information_source_analysis TEXT NOT NULL
);
"""


def get_database_path(database_path: str | Path | None = None) -> Path:
    """Return the configured database path, falling back to the local data file."""
    if database_path is None:
        return DEFAULT_DATABASE_PATH

    return Path(database_path)


def get_connection(database_path: str | Path | None = None) -> sqlite3.Connection:
    """Open a SQLite connection and configure rows as dictionary-like objects."""
    resolved_path = get_database_path(database_path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(resolved_path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(database_path: str | Path | None = None) -> Path:
    """Create the local database and the initial requests table."""
    resolved_path = get_database_path(database_path)

    with get_connection(resolved_path) as connection:
        connection.execute(REQUESTS_SCHEMA)

    return resolved_path


def create_request(
    *,
    user_id: str,
    request_title: str,
    request_summary: str,
    information_source_analysis: str,
    database_path: str | Path | None = None,
) -> int:
    """Store a notification request and return its SQLite row id."""
    with get_connection(database_path) as connection:
        cursor = connection.execute(
            """
            INSERT INTO requests (
                user_id,
                request_title,
                request_summary,
                information_source_analysis
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                request_title,
                request_summary,
                information_source_analysis,
            ),
        )

    return int(cursor.lastrowid)


def list_requests(database_path: str | Path | None = None) -> list[dict[str, Any]]:
    """Return all stored notification requests."""
    with get_connection(database_path) as connection:
        rows = connection.execute(
            """
            SELECT
                rowid,
                user_id,
                request_title,
                request_summary,
                information_source_analysis
            FROM requests
            ORDER BY rowid
            """
        ).fetchall()

    return [dict(row) for row in rows]


def get_database_status(database_path: str | Path | None = None) -> dict[str, Any]:
    """Return local database metadata useful for developer inspection."""
    resolved_path = get_database_path(database_path)
    exists = resolved_path.exists()
    status: dict[str, Any] = {
        "path": str(resolved_path),
        "exists": exists,
        "size_bytes": resolved_path.stat().st_size if exists else 0,
        "tables": [],
        "request_count": 0,
    }

    if not exists:
        return status

    with get_connection(resolved_path) as connection:
        table_rows = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            ORDER BY name
            """
        ).fetchall()
        status["tables"] = [row["name"] for row in table_rows]

        if "requests" in status["tables"]:
            request_count = connection.execute(
                "SELECT COUNT(*) AS request_count FROM requests"
            ).fetchone()
            status["request_count"] = int(request_count["request_count"])

    return status
