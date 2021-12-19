from app.db.psql_models import Attendance
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_attendance():
    response = client.get("/attendance/1")
    assert response.status_code == 200

    data = response.json()
    assert Attendance(**data)


def test_get_attendances():
    response = client.get("/attendance")
    assert response.status_code == 200

    data = response.json()
    for student in data:
        assert Attendance(**student)
