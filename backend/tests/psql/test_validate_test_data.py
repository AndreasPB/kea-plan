import time

import pytest
from app.db.psql_test_data import setup_psql_test_attendances
from app.db.psql_test_data import setup_psql_test_data
from app.db.psql_test_data import setup_psql_test_links
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_db():
    client.post("/test/psql")
    time.sleep(1)
    yield
    time.sleep(1)


def test_setup_psql_test_data():
    # assert teardown_psql()
    assert setup_psql_test_data()
    time.sleep(1)
    assert setup_psql_test_attendances()
    time.sleep(1)
    assert setup_psql_test_links()
