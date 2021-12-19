from app.db.crud import get_course_lessons
from app.db.psql import engine
from app.db.psql_models import CourseLessonLink
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

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

    with Session(engine) as session:
        db_data = get_course_lessons(session)
        assert db_data == [CourseLessonLink(**course_lesson) for course_lesson in data]
