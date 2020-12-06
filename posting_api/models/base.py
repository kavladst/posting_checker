from abc import abstractmethod, ABC
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.sql.schema import Table
from sqlalchemy import MetaData


class AbstractBaseEntity(BaseModel, ABC):
    id: UUID

    @staticmethod
    @abstractmethod
    def create_table_with_metadata(metadata: MetaData) -> Table:
        """
        Create table for SQLAlchemy.
        """
        pass
