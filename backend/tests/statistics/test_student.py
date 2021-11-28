import pytest
from app.db.redis import Student
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_db():
    client.post("/statistics/test/student")
    yield
    client.delete("/statistics/test/students")


def test_get_students():
    response = client.get("/statistics/students")
    assert response.status_code == 200

    data = response.json()
    for student in data:
        assert Student(**student)


def test_get_student():
    response = client.get("/statistics/student/1")
    assert response.status_code == 200

    data = response.json()
    assert Student(**data)

    not_found_reponse = client.get("/statistics/student/9001")
    assert not_found_reponse.status_code == 404


# TODO: Doesn't work yet
def test_put_student():
    ...


def test_delete_student():
    response = client.delete("/statistics/student/1")
    assert response.status_code == 200

    print(response.json())


def test_create_test_students():
    response = client.post("/statistics/test/student")
    assert response.status_code == 200
    data = response.json()
    for student in data:
        assert Student(**student)


def test_delete_test_students():
    response = client.delete("/statistics/test/students")
    assert response.status_code == 200
    data = response.json()
    assert data

    response = client.delete("/statistics/test/students")
    assert response.status_code == 500
    data = response.json()
    assert data == {"detail": "No students to delete"}
