import os
import time

import pytest
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import OperationalError
from src.wms.adapters import orm
from sqlalchemy.orm import sessionmaker, clear_mappers

'''def get_postgres_uri():  #(1)
    host = os.environ.get('DB_HOST', 'localhost')  #(2)
    port = 54321 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'abc123')
    user, db_name = 'allocation', 'allocation'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5005 if host == 'localhost' else 80
    return f"http://{host}:{port}"
'''
metadata = MetaData()


def get_postgres_uri():
    host = 'localhost'
    port = 5432
    user = 'postgres'
    password = 'root'
    db_name = "wms_allocation"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def postgres_db():
    engine = create_engine(get_postgres_uri())
    wait_for_postgres_to_come_up(engine)
    metadata.create_all(engine)
    return engine


def wait_for_postgres_to_come_up(engine):
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return engine.connect()
        except OperationalError:
            time.sleep(0.5)
    pytest.fail('Postgres never came up')

def postgres_session_factory():
    orm.start_mappers()
    yield sessionmaker(bind=postgres_db())
    clear_mappers()
