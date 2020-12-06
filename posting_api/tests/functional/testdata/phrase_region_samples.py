from datetime import datetime
from typing import List, Dict, Any

DEFAULT_SORT_FIELD: str = 'id'
DEFAULT_SORT_ORDER: str = 'asc'


def get_expected_phrase_region(phrase_region: Dict[str, Any]
                               ) -> Dict[str, Any]:
    return {
        'id': phrase_region['id'],
        'phrase': phrase_region['phrase'],
        'region': phrase_region['region'],
        'updated_at': phrase_region['updated_at'].timestamp()
    }


def get_expected_list_phrase_region(phrase_regions: List[Dict[str, Any]],
                                    ) -> List[Dict[str, Any]]:
    expected_list_phrase_region = sorted(
        phrase_regions,
        key=lambda x: x[DEFAULT_SORT_FIELD],
        reverse=(DEFAULT_SORT_ORDER == 'desc')
    )
    return [
        get_expected_phrase_region(phrase_region)
        for phrase_region in expected_list_phrase_region
    ]


PHRASE_REGION_DATA_1 = {
    'id': '6c5ecfc2-a051-4d17-8fce-f0c2efb6e593',
    'phrase': 'ботинки',
    'region': 'moskva',
    'updated_at': datetime(2020, 5, 1)
}
PHRASE_REGION_DATA_2 = {
    'id': '7d8b6868-05fb-4035-adeb-64fd2f659df6',
    'phrase': 'диван',
    'region': 'moskva',
    'updated_at': datetime(2019, 1, 1)
}
PHRASE_REGION_DATA_3 = {
    'id': 'ccf33a0a-b0ee-4811-9111-4b5b7ded31c3',
    'phrase': 'ботинки',
    'region': 'tula',
    'updated_at': datetime(2020, 1, 1)
}

PHRASE_REGION_SAMPLES_1 = [
    PHRASE_REGION_DATA_1, PHRASE_REGION_DATA_2, PHRASE_REGION_DATA_3
]
