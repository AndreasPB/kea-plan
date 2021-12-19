from app.db.psql_models import StudentClassCourseLink
from app.main import app
from fastapi.testclient import TestClient

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
