import pytest
from sqlalchemy_utils import database_exists, drop_database, create_database


@pytest.fixture(scope='session')
def override_settings():
    from config import settings
    settings.settings.db.database = f'{settings.settings.db.database}_test'
    yield settings.settings
    settings.settings.db.database = settings.settings.db.database.replace('_test', '')


@pytest.fixture(scope='session', autouse=True)
def client(override_settings):
    from fastapi.testclient import TestClient
    from config.db import get_db
    from main import app

    DB_URI = override_settings.db.uri

    def get_test_db():
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from config.db import Base
        from models.task import Task  # noqa
        from models.person import Person  # noqa

        if database_exists(DB_URI):
            drop_database(DB_URI)
        create_database(DB_URI)

        engine = create_engine(DB_URI)
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        return TestingSessionLocal()

    app.dependency_overrides = {
        get_db: get_test_db
    }

    yield TestClient(app)
    if database_exists(DB_URI):
        drop_database(DB_URI)
