from app.db.crud import get_attendance_by_id
from app.db.crud import get_attendances
from app.db.psql import engine
from app.db.psql_models import Attendance
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_attendance():
    response = client.get("/attendance/1")
    assert response.status_code == 200

    data = response.json()
    assert Attendance(**data)

    with Session(engine) as session:
        db_data = get_attendance_by_id(session, 1)
        assert db_data == Attendance(**data)


def test_get_attendances():
    response = client.get("/attendance")
    assert response.status_code == 200

    data = response.json()
    for student in data:
        assert Attendance(**student)

    with Session(engine) as session:
        db_data = get_attendances(session)
        assert db_data == [Attendance(**attendance) for attendance in data]
