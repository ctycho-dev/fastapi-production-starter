# FastAPI Async SQLAlchemy Template

Production-ready FastAPI template with async SQLAlchemy, comprehensive testing, and clean architecture.

## Features

- ✅ **Async SQLAlchemy** with proper session management
- ✅ **Clean Architecture** (Repository → Service → Router pattern)
- ✅ **Stateless Services** with explicit DB session passing
- ✅ **Comprehensive Testing** with pytest-asyncio
- ✅ **NullPool Testing Strategy** for async session isolation
- ✅ **Global Exception Handling** with structured logging
- ✅ **JWT Authentication** with HTTP-only cookies
- ✅ **Rate Limiting** middleware
- ✅ **CamelCase JSON** serialization
- ✅ **Foreign Key Testing Patterns** with fixture dependencies

## Lessons Learned

This template solves common FastAPI + SQLAlchemy async issues:
- Fixed "another operation is in progress" errors with NullPool
- Proper fixture dependency chains for foreign keys
- Stateless service pattern prevents session reuse bugs
- Exception-driven flow (no boolean returns)

## Tech Stack

- FastAPI
- SQLAlchemy 2.0 (async)
- PostgreSQL / SQLite (testing)
- pytest + pytest-asyncio
- Pydantic v2
