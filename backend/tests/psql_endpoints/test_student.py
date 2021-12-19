from app.db.psql_models import Student
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_student():
    response = client.get("/student/1")
    assert response.status_code == 200

    data = response.json()
    assert Student(**data)


def test_get_students():
    response = client.get("/student")
    assert response.status_code == 200

    data = response.json()
    for student in data:
        assert Student(**student)
