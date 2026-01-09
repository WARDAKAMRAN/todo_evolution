"""Service layer for Todo operations."""

from typing import Dict, List, Optional
from ..models.todo_task import TodoTask
from ..core.exceptions import TaskNotFoundError, EmptyTitleError


class TodoService:
    """Handles all business logic for managing todo tasks."""

    def __init__(self):
        """Initialize the service with an empty repository and ID counter."""
        self._repository: Dict[int, TodoTask] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> TodoTask:
        """
        Creates a new todo task with the given title and description.

        Args:
            title: The task title (required, non-empty)
            description: The task description (optional, defaults to empty string)

        Returns:
            TodoTask object with assigned ID and initial completion status (False)

        Raises:
            EmptyTitleError: If title is empty
        """
        if not title or not title.strip():
            raise EmptyTitleError()

        task = TodoTask(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )

        self._repository[self._next_id] = task
        self._next_id += 1

        return task

    def get_task(self, task_id: int) -> TodoTask:
        """
        Retrieves a specific task by its ID.

        Args:
            task_id: The unique ID of the task

        Returns:
            TodoTask object matching the ID

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._repository:
            raise TaskNotFoundError(task_id)

        return self._repository[task_id]

    def list_tasks(self) -> List[TodoTask]:
        """
        Returns all tasks in the repository.

        Returns:
            List of all TodoTask objects, sorted by ID
        """
        return sorted(self._repository.values(), key=lambda x: x.id)

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> TodoTask:
        """
        Updates the title and/or description of an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (if provided)
            description: New description (if provided)

        Returns:
            Updated TodoTask object

        Raises:
            TaskNotFoundError: If no task exists with the given ID
            EmptyTitleError: If title is provided but empty
        """
        if task_id not in self._repository:
            raise TaskNotFoundError(task_id)

        task = self._repository[task_id]

        if title is not None:
            if not title.strip():
                raise EmptyTitleError()
            task.title = title

        if description is not None:
            task.description = description

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Removes a task from the repository.

        Args:
            task_id: The ID of the task to delete

        Returns:
            Boolean indicating success (True) or failure (False if task didn't exist)
        """
        if task_id not in self._repository:
            return False

        del self._repository[task_id]
        return True

    def toggle_completion(self, task_id: int) -> TodoTask:
        """
        Toggles the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            Updated TodoTask object with toggled completion status

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._repository:
            raise TaskNotFoundError(task_id)

        task = self._repository[task_id]
        task.completed = not task.completed

        return task

    @property
    def next_id(self) -> int:
        """Get the next available ID."""
        return self._next_id