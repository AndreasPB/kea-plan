import pytest
from app.db.psql_models import LecturerClassLink
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture()
def setup_db():
    client.post("/test/psql")
    yield
    client.delete("/test/psql")


def test_get_lecturer_class_link():
    response = client.get("/lecturer_studentclass/1")
    assert response.status_code == 200


def test_get_lecturer_class_links():
    response = client.get("/lecturer_studentclass")
    assert response.status_code == 200

    data = response.json()
    for lecturer_class in data:
        assert LecturerClassLink(**lecturer_class)
