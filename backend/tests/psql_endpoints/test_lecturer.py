from app.db.psql_models import Lecturer
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_lecturer():
    response = client.get("/lecturer/1")
    assert response.status_code == 200

    data = response.json()
    assert Lecturer(**data)


def test_get_lecturers():
    response = client.get("/lecturer")
    assert response.status_code == 200

    data = response.json()
    for lecturer in data:
        assert Lecturer(**lecturer)
