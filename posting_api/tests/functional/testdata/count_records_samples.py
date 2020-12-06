from datetime import datetime
from typing import List, Dict, Any

from tests.functional.testdata.phrase_region_samples import (
    PHRASE_REGION_DATA_1
)

DEFAULT_SORT_FIELD: str = 'created_at'
DEFAULT_SORT_ORDER: str = 'asc'


def get_expected_statistic(count_records: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'count': count_records['count'],
        'timestamp': count_records['created_at'].timestamp(),
    }


def get_expected_list_statistic(counts_records: List[Dict[str, Any]],
                                start_date: datetime, end_date: datetime
                                ) -> List[Dict[str, Any]]:
    expected_list_count_records = sorted(
        counts_records,
        key=lambda x: x[DEFAULT_SORT_FIELD],
        reverse=(DEFAULT_SORT_ORDER == 'desc')
    )
    return [
        get_expected_statistic(count_records)
        for count_records in expected_list_count_records
        if start_date <= count_records['created_at'] <= end_date
    ]


COUNT_RECORDS_DATA_1 = {
    'id': '08cd0a62-0341-435f-90b0-08b5fb51fb5c',
    'phrase_region_id': PHRASE_REGION_DATA_1['id'],
    'count': 1234,
    'created_at': datetime(2010, 5, 1)
}
COUNT_RECORDS_DATA_2 = {
    'id': '7cc7c6a9-0d71-4a89-879f-b18e3d841553',
    'phrase_region_id': PHRASE_REGION_DATA_1['id'],
    'count': 4321,
    'created_at': datetime(2015, 5, 1)
}
COUNT_RECORDS_DATA_3 = {
    'id': '58b03530-e146-40e1-8ce7-a7ac7d2f0122',
    'phrase_region_id': PHRASE_REGION_DATA_1['id'],
    'count': 5678,
    'created_at': datetime(2020, 5, 1)
}

COUNT_RECORDS_SAMPLES_1 = [
    COUNT_RECORDS_DATA_1, COUNT_RECORDS_DATA_2, COUNT_RECORDS_DATA_3
]
