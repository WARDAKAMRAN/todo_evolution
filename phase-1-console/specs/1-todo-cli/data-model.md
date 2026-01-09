# Data Model: In-Memory Todo CLI

**Feature**: 1-todo-cli | **Date**: 2026-01-09 | **Plan**: [plan.md](plan.md)

## Entity: TodoTask

### Attributes
- **id**: `int` - Unique identifier for the task (auto-generated)
- **title**: `str` - Title of the todo task (required, non-empty)
- **description**: `str` - Detailed description of the task (optional, can be empty string)
- **completed**: `bool` - Completion status of the task (default: False)

### Class Definition
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoTask:
    id: int
    title: str
    description: str = ""
    completed: bool = False
```

### Validation Rules
- `id` must be a positive integer
- `title` must be a non-empty string (length > 0)
- `completed` must be a boolean value
- `description` can be any string (including empty string)

## Service Layer Data Contracts

### Input/Output Models

#### AddTaskRequest
- **title**: `str` - Title for the new task
- **description**: `str` - Description for the new task (optional)

#### UpdateTaskRequest
- **id**: `int` - ID of the task to update
- **title**: `Optional[str]` - New title (if provided)
- **description**: `Optional[str]` - New description (if provided)

#### DeleteTaskRequest
- **id**: `int` - ID of the task to delete

#### ToggleTaskRequest
- **id**: `int` - ID of the task to toggle

#### ListTasksResponse
- **tasks**: `List[TodoTask]` - List of all tasks in the system

### Error Models
- **TaskNotFoundError**: Raised when an operation is requested on a non-existent task ID
- **InvalidTaskError**: Raised when task data is invalid (e.g., empty title)

## CLI Input Models

### Menu Selection
- **option**: `int` - User-selected menu option (1-6)

### Task Input
- **title**: `str` - User-entered task title
- **description**: `str` - User-entered task description (optional)
- **task_id**: `int` - User-entered task ID for operations

## In-Memory Storage Model

### TodoRepository
- **Internal storage**: `Dict[int, TodoTask]` - In-memory dictionary mapping task IDs to TodoTask objects
- **ID generation**: Sequential integer starting from 1, auto-incrementing
- **Thread safety**: Not required for single-user CLI application

## Data Flow

1. **Input**: CLI receives user input and validates it
2. **Service**: Service layer processes requests and updates the in-memory repository
3. **Storage**: Repository maintains the current state of all tasks
4. **Output**: Service layer returns data to CLI for display to user

## Error Handling

### Validation Errors
- Empty title during task creation
- Invalid task ID during update/delete/complete operations
- Invalid menu selection

### Exception Hierarchy
```
TodoCLIError (base)
├── ValidationError
│   ├── EmptyTitleError
│   └── InvalidTaskIdError
└── RepositoryError
    └── TaskNotFoundError
```