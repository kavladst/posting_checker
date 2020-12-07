from typing import Dict

COUNT_RECORDS = 'count_records'
TOP_RECORDS_NAMES = 'top_records_names'

XPATH: Dict[str, str] = {
    COUNT_RECORDS: '//span[@class="page-title-count-1oJOc"]/text()',
    TOP_RECORDS_NAMES: '//span[starts-with(@class, "title-root-395AQ")]'
                       '/text()',
}
