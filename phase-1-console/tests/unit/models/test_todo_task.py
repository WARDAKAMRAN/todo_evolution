"""Unit tests for TodoTask model."""

from todo_cli.models.todo_task import TodoTask


def test_create_valid_todo_task():
    """Test creating a valid TodoTask."""
    task = TodoTask(id=1, title="Test Task", description="Test Description", completed=False)

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False


def test_todo_task_defaults():
    """Test TodoTask default values."""
    task = TodoTask(id=1, title="Test Task")

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.completed is False