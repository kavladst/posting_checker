import os

import requests
from lxml import etree
from urllib.request import urlopen

from core.config import CLASSIFIED_URL, HTML_FILE_NAME


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
    with open(f'{HTML_FILE_NAME}.html', 'w') as f:
        f.write(response.text)
    response = urlopen(f'file://{os.getcwd()}/{HTML_FILE_NAME}.html')
    tree = etree.parse(response, etree.HTMLParser())
    results = tree.xpath('//span[@class="page-title-count-1oJOc"]/text()')
    result_string = results[0] if len(results) else '0'
    return int(result_string.replace(' ', ''))
