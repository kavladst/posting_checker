from decouple import config

DATABASE_HOST = config('DATABASE_HOST', default='localhost')
DATABASE_PORT = config('DATABASE_PORT', default='5432')
DATABASE_USER = config('DATABASE_USER', default='vlad')
DATABASE_PASSWORD = config('DATABASE_PASSWORD', default='1234')
DATABASE_NAME = config('DATABASE_NAME', default='posts')
DATABASE_SCHEMA = config('DATABASE_SCHEMA', default='posts')

CLASSIFIED_URL = config('CLASSIFIED_URL', default='https://www.avito.ru/')
HTML_FILE_NAME = config('HTML_FILE_NAME', default='tmp_html')
