#!/usr/bin/env python3
"""Test script to verify the new rich table formatting for task listing."""

from src.todo_cli.services.todo_service import TodoService
from src.todo_cli.cli.menu import TodoMenu


def test_rich_table_formatting():
    """Test that the rich table formatting works correctly."""
    print("Testing rich table formatting for task listing...")

    # Create a service and add some test tasks
    service = TodoService()

    # Add a few tasks with different properties
    task1 = service.add_task("Buy groceries", "Milk, bread, eggs")
    task2 = service.add_task("Clean house", "")  # No description
    task3 = service.add_task("Finish report", "Complete the quarterly report")

    # Add more varied tasks to showcase the formatting
    task4 = service.add_task("Call dentist", "Schedule annual checkup")
    task5 = service.add_task("Review code", "")

    # Toggle completion on some tasks
    service.toggle_completion(task2.id)  # Clean house -> Done
    service.toggle_completion(task5.id)  # Review code -> Done

    # Create a menu and test listing
    menu = TodoMenu(service)
    print("\nDisplaying tasks with enhanced rich table format:")
    menu.list_tasks()

    print("\nTest completed successfully!")


if __name__ == "__main__":
    test_rich_table_formatting()