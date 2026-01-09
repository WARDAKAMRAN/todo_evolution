"""Integration tests for the CLI application."""

from unittest.mock import patch, MagicMock
from todo_cli.services.todo_service import TodoService
from todo_cli.cli.menu import TodoMenu


def test_add_and_list_tasks():
    """Test adding tasks and then listing them."""
    service = TodoService()
    menu = TodoMenu(service)

    # Add a few tasks
    service.add_task("Task 1", "Description 1")
    service.add_task("Task 2", "Description 2")

    # Get the list of tasks
    tasks = service.list_tasks()

    # Verify we have 2 tasks
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_update_task_flow():
    """Test the flow of adding, updating, and verifying a task."""
    service = TodoService()
    menu = TodoMenu(service)

    # Add a task
    original_task = service.add_task("Original Title", "Original Description")

    # Update the task
    updated_task = service.update_task(
        original_task.id,
        title="Updated Title",
        description="Updated Description"
    )

    # Verify the task was updated
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"


def test_delete_task_flow():
    """Test the flow of adding and then deleting a task."""
    service = TodoService()
    menu = TodoMenu(service)

    # Add a task
    task = service.add_task("Task to Delete", "Description")

    # Verify it exists
    retrieved_task = service.get_task(task.id)
    assert retrieved_task.title == "Task to Delete"

    # Delete the task
    result = service.delete_task(task.id)
    assert result is True

    # Verify it no longer exists
    from todo_cli.core.exceptions import TaskNotFoundError
    try:
        service.get_task(task.id)
        assert False, "Expected TaskNotFoundError"
    except TaskNotFoundError:
        pass  # Expected


def test_toggle_completion_flow():
    """Test the flow of toggling task completion."""
    service = TodoService()
    menu = TodoMenu(service)

    # Add a task
    task = service.add_task("Test Task", "Description")

    # Initially should be False
    assert task.completed is False

    # Toggle to True
    updated_task = service.toggle_completion(task.id)
    assert updated_task.completed is True

    # Toggle back to False
    updated_task2 = service.toggle_completion(task.id)
    assert updated_task2.completed is False