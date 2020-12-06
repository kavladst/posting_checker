from uuid import uuid4

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID as UUID_SQLAlchemy

from tests.functional.models.database.base import Base


class CountRecords(Base):
    __tablename__ = 'count_records'

    id = sqlalchemy.Column('id', UUID_SQLAlchemy,
                           primary_key=True, default=uuid4,
                           nullable=False)
    phrase_region_id = sqlalchemy.Column('phrase_region_id', UUID_SQLAlchemy,
                                         index=True,
                                         nullable=False)
    count = sqlalchemy.Column('count', sqlalchemy.Integer,
                              nullable=False)
    created_at = sqlalchemy.Column('created_at', sqlalchemy.TIMESTAMP,
                                   nullable=False)
