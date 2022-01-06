import time

import pytest
from app.db.psql_test_data import setup_psql_test_attendances
from app.db.psql_test_data import setup_psql_test_data
from app.db.psql_test_data import setup_psql_test_links
from app.db.psql_test_data import teardown_psql
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_db():
    client.post("/test/psql")
    time.sleep(3)
    yield
    time.sleep(5)


def test_setup_psql_test_data():
    assert teardown_psql()
    assert setup_psql_test_data()
    assert setup_psql_test_attendances()
    assert setup_psql_test_links()
