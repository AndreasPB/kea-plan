from app.db.psql_models import CourseLessonLink
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_course_lesson_link():
    response = client.get("/course_lesson/1")
    assert response.status_code == 200


def test_get_course_lesson_links():
    response = client.get("/course_lesson")
    assert response.status_code == 200

    data = response.json()
    for course_lesson_link in data:
        assert CourseLessonLink(**course_lesson_link)
