import requests
from lxml import html
from lxml.html import HtmlElement
from typing import List

from core.config import CLASSIFIED_URL
from core.consts import XPATH, COUNT_RECORDS, TOP_RECORDS_NAMES


def _get_html_element_by_request(query: str, region: str) -> HtmlElement:
    response = requests.get(
        f'{CLASSIFIED_URL}{region}',
        params={'q': query},
        headers={'Content-Type': 'text/html'}
    )
    response.raise_for_status()
    return html.fromstring(response.text)


def get_count_records_from_page(query: str, region: str) -> int:
    """
    Parsing HTML and get count records on it.
    :param query: Query for search.
    :param region: Region for search.
    :return: Count records on site.
    """
    tree = _get_html_element_by_request(query, region)
    elements = tree.xpath(XPATH[COUNT_RECORDS])
    count_string = elements[0] if len(elements) else '0'
    return int(count_string.replace(' ', ''))


def get_top_records_names_from_page(query: str, region: str) -> List[str]:
    """
    Parsing HTML and get 5 or less record's names on it.
    :param query: Query for search.
    :param region: Region for search.
    :return: List or record's names on site.
    """
    tree = _get_html_element_by_request(query, region)
    elements = tree.xpath(XPATH[TOP_RECORDS_NAMES])
    return [str(element) for element in elements[0:5]]
