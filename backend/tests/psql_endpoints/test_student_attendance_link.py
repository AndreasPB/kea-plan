from app.db.psql_models import StudentAttendanceLink
from app.main import app
from fastapi.testclient import TestClient

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
