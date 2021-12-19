from app.db.crud import get_lesson_by_id
from app.db.crud import get_lessons
from app.db.psql import engine
from app.db.psql_models import Lesson
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_lesson():
    response = client.get("/lesson/1")
    assert response.status_code == 200

    data = response.json()
    assert Lesson(**data)

    with Session(engine) as session:
        db_data = get_lesson_by_id(session, 1)
        assert db_data == Lesson(**data)


def test_get_lessons():
    response = client.get("/lesson")
    assert response.status_code == 200

    data = response.json()
    for lesson in data:
        assert Lesson(**lesson)

    with Session(engine) as session:
        db_data = get_lessons(session)
        assert db_data == [Lesson(**lesson) for lesson in data]
