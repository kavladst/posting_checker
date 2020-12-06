from datetime import datetime
from uuid import UUID, uuid4
from typing import List

from databases.core import Database
from sqlalchemy.sql.schema import Table
from sqlalchemy import and_

from db.storage.count_records.abstract import AbstractCountRecordsStorage
from models.count_records import CountRecords


class CountRecordsPostgreSQLStorage(AbstractCountRecordsStorage):

    def __init__(self, database: Database, table: Table):
        self._database = database
        self._table = table

    async def create_count_records(self, phrase_region_id: UUID, count: int,
                                   created_at: datetime) -> CountRecords:
        new_id = uuid4()
        query = self._table.insert().values(
            id=new_id,
            phrase_region_id=phrase_region_id,
            count=count,
            created_at=created_at
        )
        await self._database.execute(query)
        return CountRecords(
            id=new_id,
            phrase_region_id=phrase_region_id,
            count=count,
            created_at=created_at,
        )

    async def get_count_records(self, phrase_region_id: UUID,
                                start_date: datetime, end_date: datetime
                                ) -> List[CountRecords]:
        query = self._table.select().where(
            and_(
                self._table.columns.phrase_region_id == phrase_region_id,
                start_date <= self._table.columns.created_at,
                self._table.columns.created_at <= end_date
            )
        ).order_by(self._table.columns.created_at.asc())
        return [
            CountRecords(
                id=phrase_region_info['id'],
                phrase_region_id=phrase_region_info['phrase_region_id'],
                count=phrase_region_info['count'],
                created_at=phrase_region_info['created_at'],
            )
            for phrase_region_info in map(
                dict, await self._database.fetch_all(query)
            )
        ]
