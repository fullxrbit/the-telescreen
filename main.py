"""Command-line entry point for local project utilities."""

from __future__ import annotations

import argparse

from back.database import initialize_database
from back.terminal_port import run_terminal_port


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="the-telescreen local utilities")
    subparsers = parser.add_subparsers(dest="command")

    init_db_parser = subparsers.add_parser(
        "init-db",
        help="Create the local SQLite database and requests table.",
    )
    init_db_parser.add_argument(
        "--database-path",
        default=None,
        help="Optional path for the SQLite database file.",
    )

    subparsers.add_parser(
        "terminal-port",
        help="Open the interactive developer terminal port.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None or args.command == "terminal-port":
        run_terminal_port()
        return

    if args.command == "init-db":
        database_path = initialize_database(args.database_path)
        print(f"Database initialized at {database_path}")


if __name__ == "__main__":
    main()
