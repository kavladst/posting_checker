import logging

import uvicorn
from fastapi import FastAPI

from api.v1 import phrase_region, statistic
from core import config
from db import postgresql

app = FastAPI(
    title='posts_checker',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


@app.on_event('startup')
async def startup():
    (
        postgresql.database,
        postgresql.phrase_region_table,
        postgresql.count_records_table
    ) = postgresql.init_database(
        f'postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@'
        f'{config.DATABASE_HOST}:{config.DATABASE_PORT}/{config.DATABASE_NAME}'
    )
    await postgresql.database.connect()


@app.on_event('shutdown')
async def shutdown():
    await postgresql.database.disconnect()


app.include_router(phrase_region.router, prefix='/v1/phrase_region',
                   tags=['phrase_region'])
app.include_router(statistic.router, prefix='/v1/stat',
                   tags=['stat'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_level=logging.DEBUG,
    )
