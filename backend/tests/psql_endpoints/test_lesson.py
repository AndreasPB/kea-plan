from app.db.psql_models import Lesson
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_lesson():
    response = client.get("/lesson/1")
    assert response.status_code == 200

    data = response.json()
    assert Lesson(**data)


def test_get_lessons():
    response = client.get("/lesson")
    assert response.status_code == 200

    data = response.json()
    for lesson in data:
        assert Lesson(**lesson)
