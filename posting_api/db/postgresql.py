from typing import Tuple, Optional

import databases
import sqlalchemy
from databases.core import Database
from sqlalchemy.sql.schema import Table
from sqlalchemy import MetaData

from models.phrase_region import PhraseRegion
from models.count_records import CountRecords

database: Optional[Database] = None
phrase_region_table: Optional[Table] = None
count_records_table: Optional[Table] = None


async def get_database() -> Database:
    return database


async def get_phrase_region_table() -> Table:
    return phrase_region_table


async def get_count_records_table() -> Table:
    return count_records_table


def init_database(url: str) -> Tuple[Database, Table, Table]:
    """
    Create PostgreSQL connection.
    :param url: URL for PostgreSQL connection.
    :return: Tuple of database and tables (phrase_region, count_records).
    """
    database_result: Database = databases.Database(url)
    metadata: MetaData = sqlalchemy.MetaData()

    phrase_region = PhraseRegion.create_table_with_metadata(metadata)
    count_records = CountRecords.create_table_with_metadata(metadata)

    engine = sqlalchemy.create_engine(url)
    metadata.create_all(engine)
    return database_result, phrase_region, count_records
