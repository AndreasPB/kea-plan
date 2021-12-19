from app.db.crud import get_course_by_id
from app.db.crud import get_courses
from app.db.psql import engine
from app.db.psql_models import Course
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_course():
    response = client.get("/course/1")
    assert response.status_code == 200

    data = response.json()
    assert Course(**data)

    with Session(engine) as session:
        db_data = get_course_by_id(session, 1)
        assert db_data == Course(**data)


def test_get_courses():
    response = client.get("/course")
    assert response.status_code == 200

    data = response.json()
    for course in data:
        assert Course(**course)

    with Session(engine) as session:
        db_data = get_courses(session)
        assert db_data == [Course(**course) for course in data]
