from uuid import uuid4

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID as UUID_SQLAlchemy

from tests.functional.models.database.base import Base


class PhraseRegion(Base):
    __tablename__ = 'phrase_region'

    id = sqlalchemy.Column('id', UUID_SQLAlchemy, primary_key=True,
                           default=uuid4, nullable=False)
    phrase = sqlalchemy.Column('phrase', sqlalchemy.Text, nullable=False)
    region = sqlalchemy.Column('region', sqlalchemy.Text, nullable=False)
    updated_at = sqlalchemy.Column('updated_at', sqlalchemy.TIMESTAMP,
                                   nullable=False)
