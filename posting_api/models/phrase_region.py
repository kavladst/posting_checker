from uuid import uuid4
from datetime import datetime

import sqlalchemy
from sqlalchemy import MetaData, Table
from sqlalchemy.dialects.postgresql import UUID as UUID_SQLAlchemy

from models.base import AbstractBaseEntity
from core import config


class PhraseRegion(AbstractBaseEntity):
    phrase: str
    region: str
    updated_at: datetime

    @staticmethod
    def create_table_with_metadata(metadata: MetaData) -> Table:
        return sqlalchemy.Table(
            'phrase_region',
            metadata,
            sqlalchemy.Column('id', UUID_SQLAlchemy, primary_key=True,
                              default=uuid4, nullable=False),
            sqlalchemy.Column('phrase', sqlalchemy.Text, nullable=False),
            sqlalchemy.Column('region', sqlalchemy.Text, nullable=False),
            sqlalchemy.Column('updated_at', sqlalchemy.TIMESTAMP,
                              nullable=False),
            sqlalchemy.UniqueConstraint('phrase', 'region'),
            schema=config.DATABASE_SCHEMA
        )
