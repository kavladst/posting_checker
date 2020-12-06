from http import HTTPStatus
from uuid import uuid4
from datetime import datetime
from typing import List, Dict, Any

import pytest

from tests.functional.testdata import count_records_samples
from tests.functional.testdata.count_records_samples import (
    get_expected_list_statistic
)
from tests.functional.testdata.base_samples import (
    get_expected_not_found_details
)
from tests.functional.utils.api_worker import get_from_api


@pytest.mark.parametrize(
    'setup_phrase_region_data',
    [
        [count_records_samples.PHRASE_REGION_DATA_1],
    ],
    indirect=True
)
@pytest.mark.parametrize(
    'setup_count_records_data',
    [
        count_records_samples.COUNT_RECORDS_SAMPLES_1,
    ],
    indirect=True
)
def test_get_statistic(setup_phrase_region_data: List[Dict[str, Any]],
                       setup_count_records_data: List[Dict[str, Any]]):
    phrase_region = setup_phrase_region_data[0]
    counts_records = setup_count_records_data

    dates = [count_records['created_at'] for count_records in counts_records]
    dates.append(datetime(1971, 1, 1))
    dates.sort()
    for date_i in range(1, len(dates)):
        start_date, end_date = dates[date_i - 1], dates[date_i],
        response = get_from_api(
            'stat/',
            {
                'phrase_region_id': phrase_region['id'],
                'start_date': start_date,
                'end_date': end_date
            }
        )
        assert response == get_expected_list_statistic(
            counts_records, start_date, end_date
        )


def test_not_found_statistic():
    response = get_from_api(
        'stat/',
        {
            'phrase_region_id': uuid4(),
        },
        HTTPStatus.NOT_FOUND
    )
    assert response == get_expected_not_found_details('phrase_region')
