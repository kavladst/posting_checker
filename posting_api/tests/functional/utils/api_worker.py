import requests
import json
from typing import Optional

from tests.functional.settings import API_URL


def get_from_api(route: str, params: Optional[dict] = None,
                 expected_status_code: int = 200) -> dict:
    if params is None:
        params = {}
    response = requests.get(f'{API_URL}v1/{route}', params=params)
    assert response.status_code == expected_status_code
    return response.json()


def post_to_api(route: str, data: Optional[dict] = None) -> dict:
    if data is None:
        data = {}
    response = requests.post(f'{API_URL}v1/{route}', data=json.dumps(data))
    assert response.status_code == 200
    return response.json()
