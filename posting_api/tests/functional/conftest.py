from typing import List, Dict, Any

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from tests.functional import settings
from tests.functional.models.database.base import Base
from tests.functional.models.database.phrase_region import PhraseRegion
from tests.functional.models.database.count_records import CountRecords


@pytest.fixture(scope='session')
def setup_database() -> Session:
    engine = create_engine(
        f'postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@'
        f'{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/'
        f'{settings.DATABASE_NAME}'
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    yield session
    session.close()


@pytest.fixture(scope='function')
def setup_phrase_region_data(setup_database: Session,
                             request) -> List[Dict[str, Any]]:
    phrase_region_infos: List[Dict[str, Any]] = getattr(request, 'param', [])
    for phrase_region_info in phrase_region_infos:
        setup_database.add(
            PhraseRegion(
                id=phrase_region_info['id'],
                phrase=phrase_region_info['phrase'],
                region=phrase_region_info['region'],
                updated_at=phrase_region_info['updated_at'],
            )
        )
    setup_database.commit()
    yield phrase_region_infos
    setup_database.execute(
        f'TRUNCATE TABLE '
        f'{settings.DATABASE_SCHEMA}.{PhraseRegion.__tablename__} CASCADE'
    )
    setup_database.commit()


@pytest.fixture(scope='function')
def setup_count_records_data(setup_database: Session,
                             request) -> List[Dict[str, Any]]:
    count_records_infos: List[Dict[str, Any]] = getattr(request, 'param', [])
    for count_records_info in count_records_infos:
        setup_database.add(
            CountRecords(
                id=count_records_info['id'],
                phrase_region_id=count_records_info['phrase_region_id'],
                count=count_records_info['count'],
                created_at=count_records_info['created_at'],
            )
        )
    setup_database.commit()
    yield count_records_infos
    setup_database.execute(
        f'TRUNCATE TABLE '
        f'{settings.DATABASE_SCHEMA}.{CountRecords.__tablename__} CASCADE'
    )
    setup_database.commit()
