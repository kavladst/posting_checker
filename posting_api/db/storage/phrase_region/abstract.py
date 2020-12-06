from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional

from models.phrase_region import PhraseRegion


class AbstractPhraseRegionStorage(ABC):

    @abstractmethod
    async def create_phrase_region(self, phrase: str, region: str
                                   ) -> PhraseRegion:
        """
        Insert new phrase region into database.
        :param phrase: Phrase of new object.
        :param region: Region of new object.
        :return: New phrase region.
        """
        pass

    @abstractmethod
    async def get_all_phrase_regions(self) -> List[PhraseRegion]:
        """
        Get all phrase regions from database.
        :return: List of phrase regions.
        """
        pass

    @abstractmethod
    async def get_phrase_region_by_id(self, phrase_region_id: UUID
                                      ) -> Optional[PhraseRegion]:
        """
        Get phrase region if phrase_region_id exists.
        :param phrase_region_id: Id of phrase region.
        :return: Phrase region or None if phrase_region_id not exists.
        """
        pass

    @abstractmethod
    async def update_phrase_region_date_by_id(self, phrase_region_id: UUID):
        """
        Set updated_at field to datetime.now() for phrase region.
        :param phrase_region_id: Id of phrase region.
        """
        pass
