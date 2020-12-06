from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

from tests.functional.settings import DATABASE_SCHEMA

Base = declarative_base(metadata=MetaData(schema=DATABASE_SCHEMA))
