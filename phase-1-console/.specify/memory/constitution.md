<!--
Sync Impact Report:
- Version change: N/A -> 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: Global Mandate, Phase 1 Specific Scope, Implementation Rules
- Removed sections: None
- Templates requiring updates: All templates need to be checked for SDD compliance
- Follow-up TODOs: None
-->
# Todo Evolution Constitution

## Core Principles

### I. Global Mandate (SPEC-DRIVEN DEVELOPMENT)
This is a Spec-Driven Development (SDD) project. No code shall be generated without a corresponding specification. The human is the System Architect; the AI Agent is the Implementation Executive. Zero manual coding by the architect is allowed.

### II. Technology Stack
Technology: Python 3.13+ managed by UV. Platform: Strictly a Command Line Interface (CLI). Storage: In-Memory only. No persistent files (JSON/CSV) or databases are allowed in this phase.

### III. Implementation Rules (NON-NEGOTIABLE)
Follow Clean Architecture. Use Type Hinting in Python. The AI Agent must not add features outside the current spec. All execution must be through uv run.

## Additional Constraints

### IV. Code Quality Standards
All code must follow Clean Architecture principles with clear separation of concerns. Type hinting is mandatory in Python for all functions, methods, and class attributes. All code must be executable through uv run commands only.

### V. Storage Limitations
Strictly in-memory storage is enforced for Phase 1. No files (JSON/CSV) or databases are permitted. All data must exist only during runtime and be lost upon program termination.

### VI. Feature Scope Control


No features beyond those specified in the current specification are permitted. The AI Agent must strictly adhere to the defined scope and seek clarification before implementing any additional functionality.

## Development Workflow

### VII. Specification Requirement
Every piece of code must have a corresponding specification before implementation. Specifications must clearly define the scope, requirements, and acceptance criteria before any coding begins.

### VIII. Execution Protocol
All project execution must be performed using uv run. No alternative execution methods are permitted. This ensures consistent dependency management and environment control.

## Governance

All development activities must comply with the Spec-Driven Development mandate. Code without corresponding specifications is prohibited. All team members must adhere to the defined technology stack and implementation rules. Any deviation requires explicit constitutional amendment.

**Version**: 1.0.0 | **Ratified**: 2026-01-09 | **Last Amended**: 2026-01-09
