import requests
from lxml import html

from core.config import CLASSIFIED_URL
from core.consts import COUNT_RECORDS, XPATH


def get_count_records_from_page(query: str, region: str) -> int:
    """
    Parsing HTML and get count records on it.
    :param query: Query for search.
    :param region: Region for search.
    :return: Count records on site.
    """
    response = requests.get(
        f'{CLASSIFIED_URL}{region}',
        params={'q': query},
        headers={'Content-Type': 'text/html'}
    )
    response.raise_for_status()
    tree = html.fromstring(response.text)
    results = tree.xpath(XPATH[COUNT_RECORDS])
    result_string = results[0] if len(results) else '0'
    return int(result_string.replace(' ', ''))
