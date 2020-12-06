from decouple import config

API_URL = config('API_URL', default='http://0.0.0.0:8000/')
API_TIMEOUT_SECONDS = config('API_TIMEOUT_SECONDS', default=5, cast=int)

INTERVAL_UPDATE_MINUTES = config('INTERVAL_MINUTES', default=60, cast=int)

INTERVAL_SCHEDULE_MINUTES = config('INTERVAL_SCHEDULE', default=5, cast=int)
