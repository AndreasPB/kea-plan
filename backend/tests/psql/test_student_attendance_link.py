from app.db.crud import get_student_attendances
from app.db.psql import engine
from app.db.psql_models import StudentAttendanceLink
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_student_attendance_link():
    response = client.get("/student_attendance/1")
    assert response.status_code == 200


def test_get_student_attendance_links():
    response = client.get("/student_attendance")
    assert response.status_code == 200

    data = response.json()
    for student_attendance in data:
        assert StudentAttendanceLink(**student_attendance)

    with Session(engine) as session:
        db_data = get_student_attendances(session)
        assert db_data == [
            StudentAttendanceLink(**student_attendance) for student_attendance in data
        ]
