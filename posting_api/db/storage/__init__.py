from functools import lru_cache

from fastapi import Depends
from databases.core import Database
from sqlalchemy.sql.schema import Table

from db.postgresql import (
    get_database, get_phrase_region_table, get_count_records_table
)
from db.storage.phrase_region.phrase_region_postgresql_storage import (
    PhraseRegionPostgreSQLStorage
)
from db.storage.count_records.count_records_postgresql_storage import (
    CountRecordsPostgreSQLStorage
)


@lru_cache()
def get_phrase_region_storage(
        database: Database = Depends(get_database),
        table: Table = Depends(get_phrase_region_table)
) -> PhraseRegionPostgreSQLStorage:
    return PhraseRegionPostgreSQLStorage(
        database=database, table=table
    )


@lru_cache()
def get_count_records_storage(
        database: Database = Depends(get_database),
        table: Table = Depends(get_count_records_table)
) -> CountRecordsPostgreSQLStorage:
    return CountRecordsPostgreSQLStorage(
        database=database, table=table
    )
