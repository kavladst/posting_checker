from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from datetime import datetime

from models.count_records import CountRecords


class AbstractCountRecordsStorage(ABC):

    @abstractmethod
    async def create_count_records(self, phrase_region_id: UUID, count: int,
                                   created_at: datetime) -> CountRecords:
        pass

    @abstractmethod
    async def get_count_records(self, phrase_region_id: UUID,
                                start_date: datetime, end_date: datetime
                                ) -> List[CountRecords]:
        """
        Get all count records from database of the interval.
        :param phrase_region_id: Id of phrase_region.
        :param start_date: Start date of the interval.
        :param end_date: End date of the interval.
        :return: List of counts records.
        """
        pass
