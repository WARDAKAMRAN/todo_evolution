"""Custom exception hierarchy for the Todo CLI application."""

from typing import Optional


class TodoCLIError(Exception):
    """Base exception for Todo CLI application."""

    pass


class ValidationError(TodoCLIError):
    """Raised for input validation errors."""

    pass


class EmptyTitleError(ValidationError):
    """Raised when a task title is empty or contains only whitespace."""

    def __init__(self, message: str = "Task title cannot be empty or contain only whitespace"):
        super().__init__(message)


class InvalidTaskIdError(ValidationError):
    """Raised when a task ID is invalid (e.g., negative or zero)."""

    def __init__(self, task_id: int, message: Optional[str] = None):
        if message is None:
            message = f"Invalid task ID: {task_id}. Task ID must be a positive integer."
        super().__init__(message)
        self.task_id = task_id


class RepositoryError(TodoCLIError):
    """Base exception for repository-related errors."""

    pass


class TaskNotFoundError(RepositoryError):
    """Raised when an operation is requested on a non-existent task ID."""

    def __init__(self, task_id: int, message: Optional[str] = None):
        if message is None:
            message = f"Task with ID {task_id} not found."
        super().__init__(message)
        self.task_id = task_id