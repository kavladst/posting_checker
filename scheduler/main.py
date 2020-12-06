import time
import logging
from datetime import datetime, timedelta

import backoff
import requests

from core import config

logger = logging.getLogger(__name__)


def _is_time_interval_over(phrase_region_timestamp: float) -> bool:
    delta = (
        datetime.now() -
        datetime.fromtimestamp(phrase_region_timestamp)
    )
    if delta > timedelta(minutes=config.INTERVAL_UPDATE_MINUTES):
        return True
    return False


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException,
                      max_time=config.API_TIMEOUT_SECONDS)
def run_scheduler():
    while True:
        response = requests.get(
            f'{config.API_URL}v1/phrase_region/'
        )
        response.raise_for_status()
        phrase_regions = response.json()
        new_statistics_count = 0
        for phrase_region in phrase_regions:
            if _is_time_interval_over(phrase_region['updated_at']):
                response = requests.get(
                    f'{config.API_URL}v1/stat/update',
                    params={'phrase_region_id': phrase_region['id']}
                )
                response.raise_for_status()
                new_statistics_count += 1
        logger.info('Add %d new statistics.'.format(new_statistics_count))
        time.sleep(config.INTERVAL_SCHEDULE_MINUTES * 60)


if __name__ == '__main__':
    run_scheduler()
