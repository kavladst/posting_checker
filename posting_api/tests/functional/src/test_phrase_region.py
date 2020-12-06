from datetime import datetime
from typing import List, Dict, Any

import pytest

from tests.functional.testdata import phrase_region_samples
from tests.functional.testdata.phrase_region_samples import (
    get_expected_list_phrase_region
)
from tests.functional.utils.api_worker import get_from_api, post_to_api


@pytest.mark.parametrize(
    'setup_phrase_region_data',
    [
        phrase_region_samples.PHRASE_REGION_SAMPLES_1,
    ],
    indirect=True
)
def test_get_phrase_regions(setup_phrase_region_data: List[Dict[str, Any]]):
    phrase_regions = setup_phrase_region_data
    response = get_from_api('phrase_region/')
    assert response == get_expected_list_phrase_region(phrase_regions)


@pytest.mark.parametrize(
    'setup_phrase_region_data',
    [
        phrase_region_samples.PHRASE_REGION_SAMPLES_1[1:],
    ],
    indirect=True
)
def test_add_phrase_region(setup_phrase_region_data: List[Dict[str, Any]]):
    phrase_regions = setup_phrase_region_data
    new_phrase_region = phrase_region_samples.PHRASE_REGION_SAMPLES_1[0]
    new_phrase_region = post_to_api(
        'phrase_region/add',
        {
            'phrase': new_phrase_region['phrase'],
            'region': new_phrase_region['region'],
        }
    )
    new_phrase_region['updated_at'] = datetime.fromtimestamp(
        new_phrase_region['updated_at']
    )
    phrase_regions += [new_phrase_region]
    response = get_from_api('phrase_region/')
    assert response == get_expected_list_phrase_region(phrase_regions)


def test_add_same_phrase_regions(setup_phrase_region_data: List[Dict[str, Any]]
                                 ):
    new_phrase_region = phrase_region_samples.PHRASE_REGION_SAMPLES_1[0]
    new_phrase_region_1 = post_to_api(
        'phrase_region/add',
        {
            'phrase': new_phrase_region['phrase'],
            'region': new_phrase_region['region'],
        }
    )
    new_phrase_region_2 = post_to_api(
        'phrase_region/add',
        {
            'phrase': new_phrase_region['phrase'],
            'region': new_phrase_region['region'],
        }
    )
    assert new_phrase_region_1 == new_phrase_region_2
