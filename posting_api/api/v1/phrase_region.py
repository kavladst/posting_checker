from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from services.phrase_region_service import (
    PhraseRegionService, get_phrase_region_service
)

router = APIRouter()


class PhraseRegionIn(BaseModel):
    phrase: str
    region: str


class PhraseRegion(BaseModel):
    id: UUID
    phrase: str
    region: str
    updated_at: float


@router.post('/add', response_model=PhraseRegion)
async def create_region_phrase(
        phrase_region: PhraseRegionIn,
        phrase_region_service: PhraseRegionService = Depends(
            get_phrase_region_service
        )
) -> PhraseRegion:
    """
    Insert new phrase region into database.
    :param phrase_region: Information about phase region.
    :param phrase_region_service:
    :return: New phrase region.
    """
    phrase_region_response = await phrase_region_service.create_phrase_region(
        phrase=phrase_region.phrase,
        region=phrase_region.region,
    )
    return PhraseRegion(
        id=phrase_region_response.id,
        phrase=phrase_region_response.phrase,
        region=phrase_region_response.region,
        updated_at=phrase_region_response.updated_at.timestamp()
    )


@router.get('/', response_model=list)
async def get_all_region_phrases(
        phrase_region_service: PhraseRegionService = Depends(
            get_phrase_region_service
        )
) -> List[PhraseRegion]:
    """
    Returns all phrase_region from database.
    :param phrase_region_service:
    :return: List of phrase_region.
    """
    return [
        PhraseRegion(
            id=phrase_region.id,
            phrase=phrase_region.phrase,
            region=phrase_region.region,
            updated_at=phrase_region.updated_at.timestamp()
        )
        for phrase_region in await phrase_region_service.get_phrase_regions()
    ]
