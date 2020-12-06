from uuid import uuid4, UUID
from datetime import datetime
from typing import List, Optional

from databases.core import Database
from sqlalchemy.sql.schema import Table
from sqlalchemy import and_
from asyncpg.exceptions import UniqueViolationError

from db.storage.phrase_region.abstract import AbstractPhraseRegionStorage
from models.phrase_region import PhraseRegion


class PhraseRegionPostgreSQLStorage(AbstractPhraseRegionStorage):

    def __init__(self, database: Database, table: Table):
        self._database = database
        self._table = table

    async def create_phrase_region(self, phrase: str, region: str
                                   ) -> PhraseRegion:
        new_id = uuid4()
        now = datetime.now()
        try:
            await self._database.execute(
                self._table.insert().values(
                    id=new_id, phrase=phrase, region=region, updated_at=now
                )
            )
        except UniqueViolationError:
            query = self._table.select().where(
                and_(
                    self._table.columns.phrase == phrase,
                    self._table.columns.region == region,
                )
            )
            phrase_region_info = dict(await self._database.fetch_one(query))
            return PhraseRegion(
                id=phrase_region_info['id'],
                phrase=phrase_region_info['phrase'],
                region=phrase_region_info['region'],
                updated_at=phrase_region_info['updated_at'],
            )
        return PhraseRegion(
            id=new_id, phrase=phrase, region=region, updated_at=now
        )

    async def get_all_phrase_regions(self) -> List[PhraseRegion]:
        query = self._table.select().order_by(self._table.columns.id.asc())
        return [
            PhraseRegion(
                id=phrase_region_info['id'],
                phrase=phrase_region_info['phrase'],
                region=phrase_region_info['region'],
                updated_at=phrase_region_info['updated_at'],
            )
            for phrase_region_info in map(
                dict, await self._database.fetch_all(query)
            )
        ]

    async def get_phrase_region_by_id(self, phrase_region_id: UUID
                                      ) -> Optional[PhraseRegion]:
        query = self._table.select().where(
            self._table.columns.id == phrase_region_id,
        )
        phrase_region = await self._database.fetch_one(query)
        if not phrase_region:
            return None
        phrase_region_info = dict(phrase_region)
        return PhraseRegion(
            id=phrase_region_info['id'],
            phrase=phrase_region_info['phrase'],
            region=phrase_region_info['region'],
            updated_at=phrase_region_info['updated_at'],
        )

    async def update_phrase_region_date_by_id(self, phrase_region_id: UUID):
        query = self._table.update().where(
            self._table.columns.id == phrase_region_id
        ).values(updated_at=datetime.now())
        await self._database.fetch_one(query)
