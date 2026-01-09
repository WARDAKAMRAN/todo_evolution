# Phase 2: Agentic Web API

This phase implements a web API for the Todo Evolution project using FastAPI and SQLModel with Neon PostgreSQL as the cloud database.

## Overview

Phase 2 builds upon Phase 1's CLI functionality by exposing it through a modern web API with database persistence. The API provides RESTful endpoints for all todo management operations while maintaining the clean architecture principles established in Phase 1.

## Features

- RESTful API endpoints for todo management
- Database persistence with Neon PostgreSQL
- Automatic API documentation via Swagger/OpenAPI
- Type-safe implementation using FastAPI and SQLModel
- Environment-based configuration
- Health check endpoints

## Technical Stack

- **Framework**: FastAPI
- **ORM**: SQLModel
- **Database**: Neon PostgreSQL
- **Runtime**: Python 3.13+
- **Package Manager**: UV

## Setup and Installation

1. Ensure you have Python 3.13+ and UV installed
2. Navigate to this directory: `phase-2-agentic-web`
3. Install dependencies: `uv sync`
4. Set up environment variables in `.env`
5. Run the application: `uv run main.py`

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- Additional todo management endpoints coming soon...

## Architecture

The application follows Clean Architecture principles:
- **Models**: SQLModel classes for data representation
- **Services**: Business logic and database operations
- **API Layer**: FastAPI route handlers
- **Configuration**: Environment-based settings

## Environment Variables

Copy `.env.example` to `.env` and update with your configuration:

```bash
DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
NEON_DB_CONNECTION_STRING=your_neon_connection_string
APP_ENV=development
LOG_LEVEL=info
```

## Development

To run the development server:

```bash
uv run main.py
```

Or with uvicorn directly:

```bash
uv run uvicorn main:app --reload
```

API documentation will be available at `http://localhost:8000/docs`

## Next Steps

- Implement todo entity models with SQLModel
- Create database service layer
- Implement full CRUD API endpoints
- Add request/response validation
- Implement error handling
- Add authentication (future phase)