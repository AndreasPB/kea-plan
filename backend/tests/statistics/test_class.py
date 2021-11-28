import pytest
from app.db.redis import Class
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_db():
    client.post("/statistics/test/classes")
    yield
    client.delete("/statistics/test/classes")


def test_create_test_classes():
    response = client.post("/statistics/test/classes")
    assert response.status_code == 200
    data = response.json()
    for element in data:
        assert Class(**element)


def test_delete_test_classes():
    response = client.delete("/statistics/test/classes")
    assert response.status_code == 200
    data = response.json()
    assert data

    response = client.delete("/statistics/test/classes")
    assert response.status_code == 500
    data = response.json()
    assert data == {"detail": "No classes to delete"}
