from enum import StrEnum


class AppMode(StrEnum):
    """Runtime mode of the application."""
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class UserRole(StrEnum):
    """User role and permissions in the system."""
    ADMIN = "admin"
    USER = "user"


class RAGType(StrEnum):

    CLASSIC = "classic"
