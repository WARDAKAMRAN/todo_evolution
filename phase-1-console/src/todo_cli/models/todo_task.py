"""Data model for a todo task."""

from dataclasses import dataclass


@dataclass
class TodoTask:
    """Represents a single todo task with ID, title, description, and completion status."""

    id: int
    title: str
    description: str = ""
    completed: bool = False