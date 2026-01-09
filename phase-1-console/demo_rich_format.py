#!/usr/bin/env python3
"""Demo script to showcase the rich table formatting for task listing."""

from src.todo_cli.services.todo_service import TodoService
from src.todo_cli.cli.menu import TodoMenu


def demo_rich_formatting():
    """Demonstrate the rich table formatting."""
    print("Rich Table Formatting Demo")
    print("=" * 30)

    # Create a service and add some test tasks
    service = TodoService()

    # Add a variety of tasks to showcase the formatting
    service.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    service.add_task("Clean house", "Living room and kitchen")
    service.add_task("Finish report", "Complete the quarterly report for stakeholders")
    service.add_task("Call dentist", "Schedule annual checkup appointment")
    service.add_task("Review code", "Go through PRs and provide feedback")
    service.add_task("Plan vacation", "Research destinations and book flights")

    # Toggle completion on some tasks to show different statuses
    service.toggle_completion(2)  # Clean house
    service.toggle_completion(5)  # Review code

    # Create a menu and display tasks
    menu = TodoMenu(service)
    print("\nTasks displayed with rich formatting:")
    menu.list_tasks()

    print("\nNotice the improved table formatting with:")
    print("- Color-coded status indicators (green for Done, red for Todo)")
    print("- Enhanced table borders and headers")
    print("- Better spacing and alignment")
    print("- Rich text formatting")


if __name__ == "__main__":
    demo_rich_formatting()