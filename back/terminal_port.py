"""Interactive terminal portal for local developer testing."""

from __future__ import annotations

from collections.abc import Callable

from back.database import (
    create_request,
    get_database_status,
    initialize_database,
    list_requests,
)


MenuAction = Callable[[], None]


class TerminalPort:
    """Small terminal interface for inspecting and testing local project data."""

    def __init__(self) -> None:
        self._actions: dict[str, tuple[str, MenuAction]] = {
            "1": ("Initialize database", self.initialize_database),
            "2": ("Show database intelligence", self.show_database_intelligence),
            "3": ("Add test notification request", self.add_test_request),
            "4": ("List notification requests", self.list_notification_requests),
            "5": ("Exit", self.exit_port),
        }
        self._running = True

    def run(self) -> None:
        print("the-telescreen terminal port")
        print("Developer testing and project intelligence console.")

        while self._running:
            self.show_menu()
            choice = input("Select an option: ").strip()
            action = self._actions.get(choice)

            if action is None:
                print("Unknown option. Choose a listed number.")
                continue

            print()
            action[1]()
            print()

    def show_menu(self) -> None:
        print("Available actions:")
        for key, (label, _) in self._actions.items():
            print(f"  {key}. {label}")

    def initialize_database(self) -> None:
        database_path = initialize_database()
        print(f"Database initialized at {database_path}")

    def show_database_intelligence(self) -> None:
        status = get_database_status()
        print("Database intelligence:")
        print(f"  Path: {status['path']}")
        print(f"  Exists: {status['exists']}")
        print(f"  Size: {status['size_bytes']} bytes")
        print(f"  Tables: {', '.join(status['tables']) if status['tables'] else 'none'}")
        print(f"  Stored requests: {status['request_count']}")

    def add_test_request(self) -> None:
        print("Create a test notification request.")
        user_id = self.prompt_required("User id")
        request_title = self.prompt_required("Request title")
        request_summary = self.prompt_required("Request summary")
        information_source_analysis = self.prompt_required(
            "Information source analysis"
        )

        row_id = create_request(
            user_id=user_id,
            request_title=request_title,
            request_summary=request_summary,
            information_source_analysis=information_source_analysis,
        )
        print(f"Stored request with row id {row_id}")

    def list_notification_requests(self) -> None:
        requests = list_requests()

        if not requests:
            print("No notification requests stored yet.")
            return

        for request in requests:
            print(f"[{request['rowid']}] {request['request_title']}")
            print(f"  User: {request['user_id']}")
            print(f"  Summary: {request['request_summary']}")
            print(f"  Source analysis: {request['information_source_analysis']}")

    def exit_port(self) -> None:
        self._running = False
        print("Terminal port closed.")

    @staticmethod
    def prompt_required(label: str) -> str:
        while True:
            value = input(f"{label}: ").strip()
            if value:
                return value

            print(f"{label} is required.")


def run_terminal_port() -> None:
    """Open the interactive terminal port."""
    TerminalPort().run()
