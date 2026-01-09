# Todo Evolution Monorepo

A comprehensive todo application ecosystem built with a monorepo architecture, featuring multiple phases of development evolution.

## Project Overview

The Todo Evolution project is designed as a monorepo containing multiple phases of a todo application's development journey. Each phase represents a distinct iteration with different technologies and architectural approaches.

## Evolution Phase 1: CLI Implementation

**Status**: ✅ Complete

Phase 1 delivers a robust Python console application that manages a list of todos in memory with complete CRUD operations. This phase serves as the foundation for future evolution phases.

### Features
- Add tasks with title and description
- List all tasks with their status
- Update title/description by ID
- Delete tasks by ID
- Toggle completion status by ID
- CLI menu providing these options until the user exits
- Enhanced rich table formatting for task display with color-coded status indicators

### Technical Stack
- Python 3.13+
- UV package manager
- Rich library for enhanced console output
- Tabulate for table formatting
- Clean Architecture principles
- Type hints for all functions
- Comprehensive error handling

### Project Structure
```
todoo/
├── phase-1-console/          # Phase 1: CLI Implementation
│   ├── src/
│   │   └── todo_cli/
│   │       ├── models/       # Data structures
│   │       ├── services/     # Business logic
│   │       ├── cli/          # User interface
│   │       ├── core/         # Shared utilities
│   │       └── main.py
│   ├── tests/               # Unit and integration tests
│   ├── specs/               # Specification documents
│   ├── pyproject.toml       # Project dependencies
│   └── README.md            # Phase 1 documentation
├── .gitignore
└── README.md               # Root monorepo documentation
```

### Testing Coverage
Phase 1 includes **22 comprehensive tests** covering:
- Unit tests for individual components
- Integration tests for service layer
- Model validation tests
- CLI interaction tests

### Architecture
The application follows Clean Architecture principles:
- **Models Layer**: Data structures and validation (`models/`)
- **Services Layer**: Business logic and orchestration (`services/`)
- **CLI Layer**: User interface and input/output handling (`cli/`)
- **Core Layer**: Shared utilities and exceptions (`core/`)

## Setup and Installation

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if not already installed
3. Clone or download this repository
4. Navigate to the project directory
5. Run the following commands:

```bash
# Install dependencies
cd phase-1-console
uv sync

# Run the application
uv run src/todo_cli/main.py
```

## Future Phases

- **Phase 2**: Web interface implementation
- **Phase 3**: Persistent storage solutions
- **Phase 4**: Multi-user support
- **Phase 5**: Advanced features and analytics

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
