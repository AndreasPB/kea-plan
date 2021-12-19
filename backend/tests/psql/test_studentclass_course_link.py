from app.db.crud import get_studentclass_courses
from app.db.psql import engine
from app.db.psql_models import StudentClassCourseLink
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_student_course_link():
    response = client.get("/studentclass_course/1")
    assert response.status_code == 200


def test_get_student_course_links():
    response = client.get("/studentclass_course")
    assert response.status_code == 200

    data = response.json()
    for studentclass_course in data:
        assert StudentClassCourseLink(**studentclass_course)

    with Session(engine) as session:
        db_data = get_studentclass_courses(session)
        assert db_data == [
            StudentClassCourseLink(**studentclass_course)
            for studentclass_course in data
        ]
