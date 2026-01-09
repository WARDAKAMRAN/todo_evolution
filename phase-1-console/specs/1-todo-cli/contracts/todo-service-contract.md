# Todo Service Contract

**Feature**: 1-todo-cli | **Date**: 2026-01-09 | **Service**: TodoService

## Overview

This contract defines the public API for the TodoService, which handles all business logic for managing todo tasks in the In-Memory Todo CLI application.

## Service Interface

### TodoService Class

#### Methods

##### `add_task(title: str, description: str = "") -> TodoTask`
- **Purpose**: Creates a new todo task with the given title and description
- **Inputs**:
  - `title`: String containing the task title (required, non-empty)
  - `description`: String containing the task description (optional, defaults to empty string)
- **Output**: TodoTask object with assigned ID and initial completion status (False)
- **Exceptions**:
  - `ValidationError` if title is empty
- **Side Effects**: Increments internal ID counter, adds task to repository
- **Time Complexity**: O(1)

##### `get_task(task_id: int) -> TodoTask`
- **Purpose**: Retrieves a specific task by its ID
- **Inputs**:
  - `task_id`: Integer representing the unique ID of the task
- **Output**: TodoTask object matching the ID
- **Exceptions**:
  - `TaskNotFoundError` if no task exists with the given ID
- **Time Complexity**: O(1)

##### `list_tasks() -> List[TodoTask]`
- **Purpose**: Returns all tasks in the repository
- **Inputs**: None
- **Output**: List of all TodoTask objects, sorted by ID
- **Exceptions**: None
- **Time Complexity**: O(n) where n is the number of tasks

##### `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> TodoTask`
- **Purpose**: Updates the title and/or description of an existing task
- **Inputs**:
  - `task_id`: Integer representing the ID of the task to update
  - `title`: Optional string for new title (if provided)
  - `description`: Optional string for new description (if provided)
- **Output**: Updated TodoTask object
- **Exceptions**:
  - `TaskNotFoundError` if no task exists with the given ID
  - `ValidationError` if title is provided but empty
- **Side Effects**: Modifies existing task in repository
- **Time Complexity**: O(1)

##### `delete_task(task_id: int) -> bool`
- **Purpose**: Removes a task from the repository
- **Inputs**:
  - `task_id`: Integer representing the ID of the task to delete
- **Output**: Boolean indicating success (True) or failure (False if task didn't exist)
- **Exceptions**: None (non-existent task returns False)
- **Side Effects**: Removes task from repository
- **Time Complexity**: O(1)

##### `toggle_completion(task_id: int) -> TodoTask`
- **Purpose**: Toggles the completion status of a task
- **Inputs**:
  - `task_id`: Integer representing the ID of the task to toggle
- **Output**: Updated TodoTask object with toggled completion status
- **Exceptions**:
  - `TaskNotFoundError` if no task exists with the given ID
- **Side Effects**: Changes completion status of existing task
- **Time Complexity**: O(1)

## Data Models

### TodoTask
```python
@dataclass
class TodoTask:
    id: int          # Unique identifier (positive integer)
    title: str       # Task title (non-empty string)
    description: str # Task description (can be empty string)
    completed: bool  # Completion status (boolean)
```

## Error Types

### Base Exceptions
```python
class TodoCLIError(Exception):
    """Base exception for Todo CLI application"""

class ValidationError(TodoCLIError):
    """Raised for input validation errors"""

class TaskNotFoundError(ValidationError):
    """Raised when an operation is requested on a non-existent task ID"""
```

## State Management

### Repository Contract
- All operations maintain consistency of the in-memory repository
- IDs are guaranteed to be unique and sequential starting from 1
- No persistence outside of the application lifecycle
- Thread safety is not guaranteed (single-user application)

## Performance Guarantees

- All individual operations complete in under 200ms
- Memory usage scales linearly with number of tasks
- No resource leaks during normal operation

## Testing Contract

### Required Test Coverage
- All methods must have unit tests covering normal operation
- All exception cases must be tested
- Boundary conditions must be validated (empty inputs, invalid IDs)
- Integration tests must verify service-repository interactions