from datetime import datetime
from pydantic import (
    field_serializer,
)
from app.common.schema import CamelModel


class CompanyCreateSchema(CamelModel):
    """
    Schema for creating a new file record (DB-first).
    You create the DB row with the intended S3 location; OpenAI fields come later.
    """
    name: str
    address: str | None = None


class CompanyUpdateSchema(CamelModel):
    """Schema for updating company information."""
    name: str | None = None
    address: str | None = None


class CompanyOutSchema(CamelModel):
    """
    Schema for returning file information from storage.
    Includes canonical S3 fields, OpenAI fields, and orchestration state.
    Backward-compatible output aliases are provided for clients expecting old names.
    """
    id: int
    name: str
    address: str | None = None
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, created_at: datetime) -> str:
        """
        Serialize the `created_at` field into ISO 8601 string format for API responses.

        Args:
            created_at (datetime): The timestamp of when the file was created.

        Returns:
            str: The ISO 8601 formatted datetime string.
        """
        return created_at.isoformat()
