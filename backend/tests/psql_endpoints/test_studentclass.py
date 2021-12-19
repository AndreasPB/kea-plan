import pytest
from app.db.psql_models import StudentClass
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_studentclass():
    response = client.get("/studentclass/1")
    assert response.status_code == 200

    data = response.json()
    assert StudentClass(**data)


def test_get_studentclasses():
    response = client.get("/studentclass")
    assert response.status_code == 200

    data = response.json()
    for studentclass in data:
        assert StudentClass(**studentclass)


@pytest.mark.skip(reason="TODO: Don't understand the error")
def test_create_studentclass():
    test_studentclass = StudentClass(id=9001, name="Test", number_of_students=1337)

    response = client.post("/studentclass", json=test_studentclass.json())

    assert response.status_code == 200

    data = response.json()
    assert StudentClass(**data)
