from functools import lru_cache
from uuid import UUID
from typing import List, Optional

from fastapi import Depends

from db.storage.phrase_region.abstract import AbstractPhraseRegionStorage
from db.storage import get_phrase_region_storage
from models.phrase_region import PhraseRegion


class PhraseRegionService:

    def __init__(self, storage: AbstractPhraseRegionStorage):
        self._storage = storage

    async def create_phrase_region(self, phrase: str, region: str
                                   ) -> PhraseRegion:
        """
        Insert new phrase region into database.
        :param phrase: Phrase of new object.
        :param region: Region of new object
        :return: New phrase region.
        """
        return await self._storage.create_phrase_region(phrase, region)

    async def get_phrase_regions(self) -> List[PhraseRegion]:
        """
        Returns all phrase_region from database.
        :return: List of phrase regions.
        """
        return await self._storage.get_all_phrase_regions()

    async def get_phrase_region_by_id(self, phrase_region_id: UUID
                                      ) -> Optional[PhraseRegion]:
        """
        Get phrase region if phrase_region_id exists.
        :param phrase_region_id: Id of phrase region.
        :return: Phrase region or None if phrase_region_id not exists.
        """
        return await self._storage.get_phrase_region_by_id(phrase_region_id)


@lru_cache()
def get_phrase_region_service(
        storage: AbstractPhraseRegionStorage = Depends(
            get_phrase_region_storage
        )
) -> PhraseRegionService:
    return PhraseRegionService(storage=storage)
