from uuid import UUID
from datetime import datetime
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from services.statistic_service import (
    StatisticService, get_statistic_service
)
from services.phrase_region_service import (
    PhraseRegionService, get_phrase_region_service
)

router = APIRouter()


class Statistic(BaseModel):
    count: int
    timestamp: float


@router.get('/', response_model=list)
async def get_statistic(
        phrase_region_id: UUID,
        start_date: datetime = datetime(1971, 1, 1),
        end_date: datetime = datetime(2030, 1, 1),
        count_records_service: StatisticService = Depends(
            get_statistic_service
        ),
        phrase_region_service: PhraseRegionService = Depends(
            get_phrase_region_service
        )
) -> List[Statistic]:
    """
    Return statistic by id of phrase_region.
    :param phrase_region_id: Id of phrase_region.
    :param start_date: Start date of the interval.
    :param end_date: End date of the interval.
    :param count_records_service:
    :param phrase_region_service:
    :return: List of statistics of the interval.
    """
    phrase_region = await phrase_region_service.get_phrase_region_by_id(
        phrase_region_id
    )
    if not phrase_region:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='phrase_region not found')

    return [
        Statistic(
            count=count_records.count,
            timestamp=count_records.created_at.timestamp(),
        )
        for count_records in await count_records_service.get_statistic(
            phrase_region_id, start_date, end_date
        )
    ]


@router.get('/update', response_model=Statistic)
async def add_new_count_records(
        phrase_region_id: UUID,
        count_records_service: StatisticService = Depends(
            get_statistic_service
        ),
        phrase_region_service: PhraseRegionService = Depends(
            get_phrase_region_service
        )
) -> Statistic:
    """
    Find new statistics for all phrases regions in database.
    :param phrase_region_id: Id of phrase region for search.
    :param count_records_service:
    :param phrase_region_service:
    :return: List of new statistics for phrases regions.
    """
    phrase_region = await phrase_region_service.get_phrase_region_by_id(
        phrase_region_id
    )
    if not phrase_region:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='phrase_region not found')
    count_records = await count_records_service.add_new_statistic(
        phrase_region)
    return Statistic(
        count=count_records.count,
        timestamp=count_records.created_at.timestamp(),
    )
