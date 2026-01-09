# Quickstart Guide: In-Memory Todo CLI

**Feature**: 1-todo-cli | **Date**: 2026-01-09 | **Plan**: [plan.md](plan.md)

## Prerequisites

- Python 3.13 or higher
- UV package manager installed
- Basic command line familiarity

## Setup Instructions

### 1. Environment Setup
```bash
# Clone or create the project directory
cd todoo

# Initialize UV environment
uv init

# Install dependencies (if any are needed beyond standard library)
uv sync
```

### 2. Project Structure
After setup, your project should have the following structure:
```
todoo/
├── src/
│   └── todo_cli/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── todo_task.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── todo_service.py
│       ├── cli/
│       │   ├── __init__.py
│       │   └── menu.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── exceptions.py
│       └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── pyproject.toml
└── uv.lock
```

## Running the Application

### Execute with UV
```bash
# Run the application
uv run src/todo_cli/main.py

# Or if there's a defined script in pyproject.toml
uv run todo-cli
```

## Basic Usage

### Starting the Application
1. Open your terminal/command prompt
2. Navigate to the project directory
3. Run: `uv run src/todo_cli/main.py`

### Main Menu Options
Once the application starts, you'll see the main menu:

```
Todo CLI Application
====================
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. Exit

Enter your choice (1-6):
```

### Common Workflows

#### Adding a Task
1. Select option `1`
2. Enter the task title when prompted
3. Enter the task description (optional)
4. The task will be added with a unique ID

#### Viewing All Tasks
1. Select option `2`
2. All tasks will be displayed with ID, title, description, and completion status

#### Updating a Task
1. Select option `3`
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep current)
4. Enter the new description (or press Enter to keep current)

#### Deleting a Task
1. Select option `4`
2. Enter the task ID you want to delete
3. Confirm the deletion if prompted

#### Toggling Task Completion
1. Select option `5`
2. Enter the task ID you want to toggle
3. The completion status will switch (completed ↔ incomplete)

## Configuration

### pyproject.toml Setup
```toml
[project]
name = "todo-cli"
version = "0.1.0"
description = "In-Memory Todo CLI Application"
requires-python = ">=3.13"

[project.scripts]
todo-cli = "todo_cli.main:main"

[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
    "mypy>=1.0.0"
]
```

## Development Commands

### Running Tests
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_todo_service.py

# Run with coverage
uv run pytest --cov=src/todo_cli
```

### Type Checking
```bash
# Run type checker
uv run mypy src/
```

### Building/Running
```bash
# Run the application directly
uv run src/todo_cli/main.py

# Or using the defined script
uv run todo-cli
```

## Troubleshooting

### Common Issues

#### Python Version Error
- **Problem**: "Python 3.13+ required"
- **Solution**: Install Python 3.13 or higher and ensure it's in your PATH

#### UV Not Found
- **Problem**: "uv command not found"
- **Solution**: Install UV package manager using the official installation method

#### Import Errors
- **Problem**: Module import errors
- **Solution**: Ensure you're running with `uv run` and the project structure is correct

## Next Steps

1. **Customize the CLI**: Modify the menu options or display format to suit your needs
2. **Add Features**: Consider extending with features like task filtering or priority levels
3. **Testing**: Run the full test suite to ensure everything works as expected
4. **Documentation**: Review the full specification and implementation plan for detailed information

## Useful Commands Summary

```bash
# Setup and run
uv sync                 # Install dependencies
uv run todo-cli         # Run the application
uv run src/todo_cli/main.py  # Alternative run method

# Development
uv run pytest           # Run tests
uv run mypy src/        # Type check
uv run pytest --cov=src/todo_cli  # Coverage report
```