from functools import lru_cache
from uuid import UUID
from datetime import datetime
from typing import List

from fastapi import Depends

from db.storage.count_records.abstract import AbstractCountRecordsStorage
from db.storage import get_count_records_storage
from models.count_records import CountRecords
from models.phrase_region import PhraseRegion
from utils.html_parser import get_count_records_from_page


class StatisticService:

    def __init__(self, storage: AbstractCountRecordsStorage):
        self._storage = storage

    async def get_statistic(self, phrase_region_id: UUID,
                            start_date: datetime, end_date: datetime
                            ) -> List[CountRecords]:
        """
        Return count records phrase_region's by id and interval.
        :param phrase_region_id: Id of phrase_region.
        :param start_date: Start date of the interval.
        :param end_date: End date of the interval.
        :return: List of count records in the interval.
        """
        return await self._storage.get_count_records(
            phrase_region_id, start_date, end_date
        )

    async def add_new_statistic(self, phrase_region: PhraseRegion
                                ) -> CountRecords:
        """
        Insert new count records for input phrases region.
        :param phrase_region: Phrase_region for search.
        :return: New count records for phrases region.
        """
        count_records = get_count_records_from_page(
            phrase_region.phrase, phrase_region.region
        )
        current_date = datetime.now()
        return await self._storage.create_count_records(
            phrase_region.id, count_records, current_date
        )


@lru_cache()
def get_statistic_service(
        storage: AbstractCountRecordsStorage = Depends(
            get_count_records_storage
        )
) -> StatisticService:
    return StatisticService(storage=storage)
