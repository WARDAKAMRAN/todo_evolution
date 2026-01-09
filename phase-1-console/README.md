# Evolution of Todo - Phase 1: CLI

A Python console application that manages a list of todos in memory with core CRUD operations.

## Features

- Add tasks with title and description
- List all tasks with their status
- Update title/description by ID
- Delete tasks by ID
- Toggle completion status by ID
- CLI menu providing these options until the user exits

## Technical Requirements

- Python 3.13+
- UV package manager
- Command Line Interface only
- In-memory storage only (no persistent files)
- Clean Architecture principles
- Type hints for all functions
- Error handling
- All execution via uv run

## Project Structure

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
├── pyproject.toml
└── specs/
    └── 1-todo-cli/
        ├── spec.md
        ├── plan.md
        ├── research.md
        ├── data-model.md
        ├── quickstart.md
        └── contracts/
            └── todo-service-contract.md
```

## Setup and Installation

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if not already installed
3. Clone or download this repository
4. Navigate to the project directory
5. Run the following commands:

```bash
# Install dependencies
uv sync

# Run the application
uv run src/todo_cli/main.py
```

## Usage

The application provides a menu-driven interface:

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

### Available Operations

1. **Add Task**: Create a new todo task with title and description
2. **List Tasks**: Display all tasks with their status
3. **Update Task**: Modify title or description of an existing task by ID
4. **Delete Task**: Remove a task by ID
5. **Toggle Completion**: Switch completion status of a task by ID
6. **Exit**: Quit the application

## Development

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
# Run type checker (install mypy first if needed)
uv run mypy src/
```

### Project Specifications

For detailed specifications and implementation plans, see the `specs/1-todo-cli/` directory:
- `spec.md`: Feature specification
- `plan.md`: Implementation plan
- `research.md`: Technical research
- `data-model.md`: Data model documentation
- `quickstart.md`: Quickstart guide
- `contracts/`: API contracts

## Architecture

The application follows Clean Architecture principles:

- **Models Layer**: Data structures and validation (`models/`)
- **Services Layer**: Business logic and orchestration (`services/`)
- **CLI Layer**: User interface and input/output handling (`cli/`)
- **Core Layer**: Shared utilities and exceptions (`core/`)

## Contributing

1. Create an issue describing the feature or bug
2. Fork the repository
3. Create a feature branch
4. Add tests for your changes
5. Make your changes
6. Ensure all tests pass
7. Submit a pull request

## License

This project is licensed under the MIT License.