# app/domain/file/repository.py
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, func

from app.exceptions.exceptions import DatabaseError
from app.common.base_repository import BaseRepository
from app.domain.company.model import Company
from app.domain.company.schema import (
    CompanyCreateSchema,
    CompanyOutSchema
)


class CompanyRepository(BaseRepository[Company, CompanyOutSchema, CompanyCreateSchema]):
    """
    PostgreSQL repository implementation for managing File entities.

    This class provides CRUD operations and database interaction logic for 
    file metadata stored in the vector store system. It extends the generic 
    BaseRepository with types specific to File, including the 
    Pydantic input and output schemas.

    Inherits:
        BaseRepository[Company, CompanyOutSchema, CompanyCreateSchema]
    """

    def __init__(self):
        """
        Initializes the FileRepository by binding the File model
        with its corresponding Pydantic schemas (CompanyOutSchema and CompanyCreateSchema).
        
        This setup allows reuse of the generic BaseRepository for standard
        database operations such as create, read, update, and delete.
        """
        super().__init__(Company, CompanyOutSchema, CompanyCreateSchema)
