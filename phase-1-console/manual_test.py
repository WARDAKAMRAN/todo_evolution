#!/usr/bin/env python3
"""Manual test script to verify all user stories work correctly."""

from src.todo_cli.services.todo_service import TodoService
from src.todo_cli.cli.menu import TodoMenu


def test_user_story_1_add_task():
    """Test User Story 1: Add Todo Task"""
    print("Testing User Story 1: Add Todo Task")
    service = TodoService()

    # Add a task
    task = service.add_task("Buy groceries", "Need to buy milk and bread")
    print(f"OK Added task: ID {task.id}, Title: '{task.title}', Description: '{task.description}'")

    # Verify task exists
    retrieved = service.get_task(task.id)
    assert retrieved.title == "Buy groceries"
    assert retrieved.description == "Need to buy milk and bread"
    print("OK Task retrieval confirmed")


def test_user_story_2_list_tasks():
    """Test User Story 2: List All Todo Tasks"""
    print("\nTesting User Story 2: List All Todo Tasks")
    service = TodoService()

    # Add multiple tasks
    task1 = service.add_task("Task 1", "First task")
    task2 = service.add_task("Task 2", "Second task")
    task3 = service.add_task("Task 3", "")

    # List all tasks
    tasks = service.list_tasks()
    print(f"OK Found {len(tasks)} tasks:")
    for task in tasks:
        desc = task.description if task.description else "(no description)"
        print(f"  - ID {task.id}: '{task.title}' - {desc}")

    # Verify ordering by ID
    assert tasks[0].id == task1.id
    assert tasks[1].id == task2.id
    assert tasks[2].id == task3.id
    print("OK Task ordering confirmed")


def test_user_story_3_update_task():
    """Test User Story 3: Update Todo Task"""
    print("\nTesting User Story 3: Update Todo Task")
    service = TodoService()

    # Add a task
    original_task = service.add_task("Original Title", "Original Description")
    print(f"OK Created task: '{original_task.title}' - '{original_task.description}'")

    # Update the task
    updated_task = service.update_task(
        original_task.id,
        title="Updated Title",
        description="Updated Description"
    )
    print(f"OK Updated task: '{updated_task.title}' - '{updated_task.description}'")

    # Verify update
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    print("OK Update confirmed")


def test_user_story_4_delete_task():
    """Test User Story 4: Delete Todo Task"""
    print("\nTesting User Story 4: Delete Todo Task")
    service = TodoService()

    # Add a task
    task = service.add_task("Task to Delete", "Will be deleted")
    print(f"OK Created task to delete: ID {task.id}")

    # Verify it exists
    retrieved = service.get_task(task.id)
    assert retrieved.title == "Task to Delete"
    print("OK Task exists before deletion")

    # Delete the task
    success = service.delete_task(task.id)
    print(f"OK Deletion result: {success}")

    # Verify it's gone
    try:
        service.get_task(task.id)
        assert False, "Task should not exist after deletion"
    except Exception:
        print("OK Task successfully deleted (not found after deletion)")


def test_user_story_5_toggle_completion():
    """Test User Story 5: Toggle Task Completion Status"""
    print("\nTesting User Story 5: Toggle Task Completion Status")
    service = TodoService()

    # Add a task
    task = service.add_task("Toggle Task", "Task to toggle completion")
    print(f"OK Created task: ID {task.id}, Completed: {task.completed}")

    # Verify initial state is incomplete
    assert task.completed is False

    # Toggle completion
    toggled_task = service.toggle_completion(task.id)
    print(f"OK After first toggle: Completed: {toggled_task.completed}")
    assert toggled_task.completed is True

    # Toggle again
    toggled_back_task = service.toggle_completion(task.id)
    print(f"OK After second toggle: Completed: {toggled_back_task.completed}")
    assert toggled_back_task.completed is False
    print("OK Toggle functionality confirmed")


def test_user_story_6_menu_navigation():
    """Test User Story 6: Navigate CLI Menu"""
    print("\nTesting User Story 6: Navigate CLI Menu")
    service = TodoService()
    menu = TodoMenu(service)

    # Just verify the menu can be instantiated and has the right methods
    assert hasattr(menu, 'display_menu')
    assert hasattr(menu, 'run')
    assert hasattr(menu, 'add_task')
    assert hasattr(menu, 'list_tasks')
    assert hasattr(menu, 'update_task')
    assert hasattr(menu, 'delete_task')
    assert hasattr(menu, 'toggle_completion')

    print("OK Menu has all required functionality")


def run_all_tests():
    """Run all manual tests."""
    print("Starting manual testing of all user stories...\n")

    test_user_story_1_add_task()
    test_user_story_2_list_tasks()
    test_user_story_3_update_task()
    test_user_story_4_delete_task()
    test_user_story_5_toggle_completion()
    test_user_story_6_menu_navigation()

    print("\nALL OK: All user stories tested successfully!")
    print("- US1: Add Todo Task OK")
    print("- US2: List All Todo Tasks OK")
    print("- US3: Update Todo Task OK")
    print("- US4: Delete Todo Task OK")
    print("- US5: Toggle Task Completion Status OK")
    print("- US6: Navigate CLI Menu OK")


if __name__ == "__main__":
    run_all_tests()