from uuid import uuid4, UUID
from datetime import datetime

import sqlalchemy
from sqlalchemy import MetaData, Table
from sqlalchemy.dialects.postgresql import UUID as UUID_SQLAlchemy

from models.base import AbstractBaseEntity
from core import config


class CountRecords(AbstractBaseEntity):
    phrase_region_id: UUID
    count: int
    created_at: datetime

    @staticmethod
    def create_table_with_metadata(metadata: MetaData) -> Table:
        return sqlalchemy.Table(
            'count_records',
            metadata,
            sqlalchemy.Column('id', UUID_SQLAlchemy,
                              primary_key=True, default=uuid4,
                              nullable=False),
            sqlalchemy.Column('phrase_region_id', UUID_SQLAlchemy,
                              index=True,
                              nullable=False),
            sqlalchemy.Column('count', sqlalchemy.Integer,
                              nullable=False),
            sqlalchemy.Column('created_at', sqlalchemy.TIMESTAMP,
                              nullable=False),
            schema=config.DATABASE_SCHEMA
        )
