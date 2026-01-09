"""Main entry point for the Todo CLI application."""

from .services.todo_service import TodoService
from .cli.menu import TodoMenu


def main() -> None:
    """Application entry point."""
    # Initialize the service and menu
    service = TodoService()
    menu = TodoMenu(service)

    # Run the application
    menu.run()


if __name__ == "__main__":
    main()