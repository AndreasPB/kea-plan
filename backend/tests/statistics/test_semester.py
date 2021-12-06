import pytest
from app.db.redis_models import Semester
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_db():
    client.post("/statistics/test/semesters")
    yield
    client.delete("/statistics/test/semesters")


def test_get_semesters():
    response = client.get("/statistics/semesters")
    assert response.status_code == 200

    data = response.json()
    for semester in data:
        assert Semester(**semester)


def test_get_semester():
    response = client.get("/statistics/semester/1")
    assert response.status_code == 200

    data = response.json()
    assert Semester(**data)

    not_found_reponse = client.get("/statistics/semester/9001")
    assert not_found_reponse.status_code == 404


def test_create_test_semesters():
    response = client.post("/statistics/test/semesters")
    assert response.status_code == 200
    data = response.json()
    for semester in data:
        assert Semester(**semester)


def test_delete_test_semesters():
    response = client.delete("/statistics/test/semesters")
    assert response.status_code == 200
    data = response.json()
    assert data

    response = client.delete("/statistics/test/semesters")
    assert response.status_code == 500
    data = response.json()
    assert data == {"detail": "No semesters to delete"}
