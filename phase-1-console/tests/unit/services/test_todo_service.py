"""Unit tests for TodoService."""

import pytest
from todo_cli.services.todo_service import TodoService
from todo_cli.core.exceptions import TaskNotFoundError, EmptyTitleError


def test_add_task_success():
    """Test successful task addition."""
    service = TodoService()

    task = service.add_task("Test Task", "Test Description")

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False

    # Check that the next task will have ID 2
    assert service.next_id == 2


def test_add_task_without_description():
    """Test adding a task without description."""
    service = TodoService()

    task = service.add_task("Test Task")

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.completed is False


def test_add_task_empty_title():
    """Test adding a task with empty title raises exception."""
    service = TodoService()

    with pytest.raises(EmptyTitleError):
        service.add_task("")

    with pytest.raises(EmptyTitleError):
        service.add_task("   ")


def test_get_task_success():
    """Test getting an existing task."""
    service = TodoService()
    added_task = service.add_task("Test Task")

    retrieved_task = service.get_task(added_task.id)

    assert retrieved_task.id == added_task.id
    assert retrieved_task.title == added_task.title
    assert retrieved_task.description == added_task.description
    assert retrieved_task.completed == added_task.completed


def test_get_task_not_found():
    """Test getting a non-existing task raises exception."""
    service = TodoService()

    with pytest.raises(TaskNotFoundError):
        service.get_task(999)


def test_list_tasks_empty():
    """Test listing tasks when none exist."""
    service = TodoService()

    tasks = service.list_tasks()

    assert tasks == []


def test_list_tasks_multiple():
    """Test listing multiple tasks."""
    service = TodoService()

    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2", "Description 2")
    task3 = service.add_task("Task 3")

    tasks = service.list_tasks()

    assert len(tasks) == 3
    assert tasks[0].id == 1
    assert tasks[0].title == "Task 1"
    assert tasks[1].id == 2
    assert tasks[1].title == "Task 2"
    assert tasks[2].id == 3
    assert tasks[2].title == "Task 3"


def test_update_task_title_only():
    """Test updating only the title of a task."""
    service = TodoService()
    original_task = service.add_task("Original Title", "Original Description")

    updated_task = service.update_task(original_task.id, title="Updated Title")

    assert updated_task.id == original_task.id
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Original Description"
    assert updated_task.completed == original_task.completed


def test_update_task_description_only():
    """Test updating only the description of a task."""
    service = TodoService()
    original_task = service.add_task("Original Title", "Original Description")

    updated_task = service.update_task(original_task.id, description="Updated Description")

    assert updated_task.id == original_task.id
    assert updated_task.title == "Original Title"
    assert updated_task.description == "Updated Description"
    assert updated_task.completed == original_task.completed


def test_update_task_both_fields():
    """Test updating both title and description of a task."""
    service = TodoService()
    original_task = service.add_task("Original Title", "Original Description")

    updated_task = service.update_task(
        original_task.id,
        title="Updated Title",
        description="Updated Description"
    )

    assert updated_task.id == original_task.id
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    assert updated_task.completed == original_task.completed


def test_update_task_nonexistent():
    """Test updating a non-existent task raises exception."""
    service = TodoService()

    with pytest.raises(TaskNotFoundError):
        service.update_task(999, title="New Title")


def test_update_task_empty_title():
    """Test updating a task with empty title raises exception."""
    service = TodoService()
    original_task = service.add_task("Original Title")

    with pytest.raises(EmptyTitleError):
        service.update_task(original_task.id, title="")


def test_delete_task_exists():
    """Test deleting an existing task."""
    service = TodoService()
    task = service.add_task("Test Task")

    result = service.delete_task(task.id)

    assert result is True

    # Verify the task no longer exists
    with pytest.raises(TaskNotFoundError):
        service.get_task(task.id)


def test_delete_task_not_exists():
    """Test deleting a non-existent task."""
    service = TodoService()

    result = service.delete_task(999)

    assert result is False


def test_toggle_completion():
    """Test toggling task completion status."""
    service = TodoService()
    task = service.add_task("Test Task")

    # Initially should be False
    assert task.completed is False

    # Toggle should make it True
    toggled_task = service.toggle_completion(task.id)
    assert toggled_task.completed is True

    # Toggle again should make it False
    toggled_task2 = service.toggle_completion(task.id)
    assert toggled_task2.completed is False


def test_toggle_completion_nonexistent():
    """Test toggling completion for non-existent task raises exception."""
    service = TodoService()

    with pytest.raises(TaskNotFoundError):
        service.toggle_completion(999)