# Implementation Tasks: In-Memory Todo CLI

**Feature**: 1-todo-cli | **Date**: 2026-01-09 | **Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

## Overview

This document outlines the implementation tasks for the In-Memory Todo CLI application. The tasks are organized in phases, following the user story priorities from the specification and the Clean Architecture approach from the plan.

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites)
- **Phase 3**: User Story 1 - Add Todo Task (P1)
- **Phase 4**: User Story 2 - List All Todo Tasks (P1)
- **Phase 5**: User Story 6 - Navigate CLI Menu (P1)
- **Phase 6**: User Story 3 - Update Todo Task (P2)
- **Phase 7**: User Story 4 - Delete Todo Task (P2)
- **Phase 8**: User Story 5 - Toggle Task Completion Status (P2)
- **Final Phase**: Polish & Cross-Cutting Concerns

## Dependencies

- User Story 1 (Add) must be implemented before User Stories 3, 4, and 5 (which require existing tasks)
- User Story 2 (List) provides visibility for all other operations
- User Story 6 (Menu) provides the interface for all other operations
- Foundational components (models, services, exceptions) support all user stories

## Parallel Execution Opportunities

- Model and service implementations can be developed in parallel with CLI interface
- Individual user story implementations can be tested independently after core foundation exists
- Unit tests can be written in parallel with implementation

## Implementation Strategy

- Build MVP with User Story 1 (Add) and User Story 6 (Menu) first
- Incrementally add other user stories
- Implement error handling throughout
- Focus on clean architecture separation

---

## Phase 1: Setup

**Goal**: Initialize project structure and basic configuration

- [X] T001 Use `uv init` to initialize the project. Verify output with `ls pyproject.toml`.
- [X] T002 Update `pyproject.toml` with project metadata per quickstart guide.
- [X] T003 Create project directory structure per plan.md: `src/todo_cli/{models,services,cli,core}`, `tests/{unit,integration}`, `specs/1-todo-cli`.
- [X] T004 Create all required `__init__.py` files in the package directories.
- [X] T005 Set up basic dependencies in pyproject.toml for testing and type checking.

## Phase 2: Foundational Components

**Goal**: Implement core data models, service contracts, and error handling

- [X] T006 Create `src/todo_cli/models/todo_task.py` with TodoTask data model. **Doc**: Fetch dataclasses docs via Context7 for proper @dataclass usage.
- [X] T007 Create `src/todo_cli/core/exceptions.py` with custom exception hierarchy per data-model.md.
- [X] T008 Create `src/todo_cli/services/todo_service.py` with TodoService class skeleton per contract.
- [X] T009 Implement in-memory repository in TodoService with dictionary storage and ID generation.
- [X] T010 Create basic `src/todo_cli/main.py` with placeholder main function.

## Phase 3: [US1] Add Todo Task (P1)

**Goal**: Enable users to add new todo tasks with title and description

**Independent Test Criteria**: User can start the application, select "Add" option, enter a title and description, and see the task added to their list with a unique ID.

- [X] T011 [P] [US1] Implement `add_task()` method in TodoService with proper validation per contract.
- [X] T012 [P] [US1] Add unit tests for add_task functionality in `tests/unit/services/test_todo_service.py`.
- [X] T013 [P] [US1] Implement input validation for empty titles per spec requirements.
- [X] T014 [P] [US1] Test edge cases: empty title raises ValidationError, valid input creates task with auto-ID.

## Phase 4: [US2] List All Todo Tasks (P1)

**Goal**: Allow users to view all their current todo tasks with completion status

**Independent Test Criteria**: User can start the application, select "List" option, and see all tasks with their ID, title, description, and completion status.

- [X] T015 [P] [US2] Implement `list_tasks()` method in TodoService per contract.
- [X] T016 [P] [US2] Implement `get_task()` method in TodoService per contract.
- [X] T017 [P] [US2] Add unit tests for list_tasks functionality in `tests/unit/services/test_todo_service.py`.
- [X] T018 [P] [US2] Handle empty list case with appropriate response per spec requirements.

## Phase 5: [US6] Navigate CLI Menu (P1)

**Goal**: Provide menu-driven interface for accessing all todo management functions

**Independent Test Criteria**: User can start the application, navigate between different menu options, and exit the application cleanly.

- [X] T019 [P] [US6] Create `src/todo_cli/cli/menu.py` with CLI interface class.
- [X] T020 [P] [US6] Implement menu display functionality with options 1-6 per research.md.
- [X] T021 [P] [US6] Implement input validation for menu selection per spec requirements.
- [X] T022 [P] [US6] Add graceful exit functionality per spec requirements.
- [X] T023 [P] [US6] Integrate TodoService with CLI menu for basic operations.
- [X] T024 [P] [US6] Test CLI menu navigation and exit functionality.

## Phase 6: [US3] Update Todo Task (P2)

**Goal**: Enable users to edit title or description of existing todo tasks

**Independent Test Criteria**: User can start the application, select "Update" option, enter a valid task ID, and modify the title or description of the task.

- [X] T025 [P] [US3] Implement `update_task()` method in TodoService per contract.
- [X] T026 [P] [US3] Add unit tests for update_task functionality in `tests/unit/services/test_todo_service.py`.
- [X] T027 [P] [US3] Implement CLI interface for update operation in menu.py.
- [X] T028 [P] [US3] Handle invalid task ID case with appropriate error message per spec requirements.

## Phase 7: [US4] Delete Todo Task (P2)

**Goal**: Allow users to remove completed or unwanted todo tasks from their list

**Independent Test Criteria**: User can start the application, select "Delete" option, enter a valid task ID, and see the task removed from the list.

- [X] T029 [P] [US4] Implement `delete_task()` method in TodoService per contract.
- [X] T030 [P] [US4] Add unit tests for delete_task functionality in `tests/unit/services/test_todo_service.py`.
- [X] T031 [P] [US4] Implement CLI interface for delete operation in menu.py.
- [X] T032 [P] [US4] Handle invalid task ID case with appropriate error message per spec requirements.

## Phase 8: [US5] Toggle Task Completion Status (P2)

**Goal**: Enable users to mark tasks as completed or incomplete

**Independent Test Criteria**: User can start the application, select "Complete" option, enter a valid task ID, and see the completion status toggled.

- [X] T033 [P] [US5] Implement `toggle_completion()` method in TodoService per contract.
- [X] T034 [P] [US5] Add unit tests for toggle_completion functionality in `tests/unit/services/test_todo_service.py`.
- [X] T035 [P] [US5] Implement CLI interface for toggle operation in menu.py.
- [X] T036 [P] [US5] Handle invalid task ID case with appropriate error message per spec requirements.

## Final Phase: Polish & Cross-Cutting Concerns

**Goal**: Complete the application with comprehensive testing, error handling, and integration

- [X] T037 Implement comprehensive error handling throughout CLI interface per spec requirements.
- [X] T038 Add integration tests in `tests/integration/test_cli_integration.py` for end-to-end workflows.
- [X] T039 Complete main.py with proper imports and application initialization.
- [X] T040 Add type hints to all functions and classes per spec requirements.
- [X] T041 Implement consistent formatting for task display per research.md UX considerations.
- [X] T042 Run full test suite and fix any failures.
- [X] T043 Perform manual testing of all user stories and acceptance scenarios.
- [X] T044 Document any deviations from original plan or spec in implementation notes.

---

## MVP Scope

The MVP includes:
- Phase 1: Setup
- Phase 2: Foundational components
- Phase 3: Add Todo Task (US1)
- Phase 5: Navigate CLI Menu (US6) - with basic add functionality
- Basic error handling and type hints

This provides a working application where users can start the program, add tasks, and exit.