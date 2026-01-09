# Research: In-Memory Todo CLI

**Feature**: 1-todo-cli | **Date**: 2026-01-09 | **Plan**: [plan.md](plan.md)

## Technology Stack Analysis

### Python 3.13+
- **Rationale**: Latest stable Python version with modern features
- **Benefits**: Improved performance, latest language features, extended standard library
- **Compatibility**: Compatible with UV package manager
- **Requirements**: Minimum version constraint to ensure feature availability

### UV Package Manager
- **Rationale**: Fast Python package installer and resolver
- **Benefits**: Significantly faster than pip, reliable dependency resolution
- **Usage**: `uv run`, `uv add`, `uv sync` for all project operations
- **Integration**: Seamless with modern Python development workflows

## Clean Architecture Implementation Strategy

### Layer Separation
1. **Models Layer**: Data structures and validation
2. **Services Layer**: Business logic and orchestration
3. **CLI Layer**: User interface and input/output handling
4. **Core Layer**: Shared utilities and exceptions

### Benefits
- **Testability**: Each layer can be tested independently
- **Maintainability**: Changes in one layer don't affect others
- **Flexibility**: Easy to swap implementations (e.g., CLI vs API)

## In-Memory Storage Approach

### Design Choice: Dictionary-Based Repository
```python
# Internal representation
_repository: Dict[int, TodoTask] = {}
_next_id: int = 1
```

### Advantages
- **Speed**: O(1) access time for all operations
- **Simplicity**: No complex setup or configuration required
- **Memory Efficiency**: Direct object storage without serialization overhead

### Constraints
- **Session-Only**: Data lost when application terminates
- **Single Session**: No concurrent access concerns
- **Size Limitation**: Dependent on available RAM

## Type Hinting Strategy

### Comprehensive Coverage
- All function parameters and return values
- Class attributes and method signatures
- Generic types for collections (List, Dict, Optional)
- Union types where multiple return types possible

### Tools for Validation
- mypy for static type checking
- IDE integration for real-time feedback
- Runtime validation for user input

## CLI Interface Design

### Menu Options Mapping
```
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. Exit
```

### User Experience Considerations
- Clear prompts with input validation
- Error messages that guide user correction
- Consistent formatting across all operations
- Graceful handling of invalid inputs

## Error Handling Framework

### Exception Hierarchy Design
```python
class TodoCLIError(Exception):
    """Base exception for Todo CLI application"""

class ValidationError(TodoCLIError):
    """Raised for input validation errors"""

class RepositoryError(TodoCLIError):
    """Raised for repository/data access errors"""
```

### Error Recovery Patterns
- Input validation before processing
- Specific error messages for different failure modes
- State preservation during error conditions
- Graceful degradation when possible

## Testing Strategy

### Unit Testing Focus
- Individual service methods
- Model validation logic
- CLI input parsing
- Error condition handling

### Integration Testing Scope
- End-to-end CLI workflows
- Service-repository interactions
- Error propagation through layers

### Test Data Management
- In-memory test repositories
- Parameterized test cases for edge conditions
- Mock objects for isolated testing

## Performance Considerations

### Operation Complexity Targets
- **Add**: O(1) - Direct insertion with auto-ID
- **List**: O(n) - Need to return all items
- **Update/Delete/Toggle**: O(1) - Direct lookup by ID
- **Menu Navigation**: <200ms response time

### Memory Usage Optimization
- Object reuse where possible
- Efficient data structures
- Cleanup of temporary objects

## Security Considerations

### Input Sanitization
- Validate user input lengths
- Escape special characters if needed
- Prevent injection attacks (though minimal risk in CLI)

### Data Privacy
- No persistent storage means no data retention
- Session-only data handling
- No sensitive data processing required

## Dependency Analysis

### Standard Library Usage
- `dataclasses` for model definition
- `typing` for type hints
- `argparse` for command line parsing (if needed)
- Built-in exceptions for error handling

### Potential Third-Party Libraries
- `pytest` for testing framework
- `mypy` for type checking
- `rich` for enhanced CLI display (optional consideration)

## Implementation Phases

### Phase 1: Core Structure
- Define data models with proper type hints
- Implement basic repository pattern
- Create service layer with business logic

### Phase 2: CLI Interface
- Develop menu system
- Implement user input handling
- Add error handling and validation

### Phase 3: Testing and Refinement
- Write comprehensive test suite
- Performance validation
- User experience refinement

## Risk Assessment

### Technical Risks
- **Memory Growth**: Long-running sessions could accumulate memory
  - *Mitigation*: Monitor memory usage, consider periodic cleanup if needed
- **Type Safety**: Complex type hierarchies might cause runtime issues
  - *Mitigation*: Thorough type checking and testing

### Schedule Risks
- **Complexity Underestimation**: Hidden complexity in error handling
  - *Mitigation*: Iterative development with frequent validation

### Quality Risks
- **Edge Case Handling**: Missing validation for unusual inputs
  - *Mitigation*: Comprehensive test coverage with boundary value analysis