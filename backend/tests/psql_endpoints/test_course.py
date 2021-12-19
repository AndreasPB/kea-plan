from app.db.psql_models import Course
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_course():
    response = client.get("/course/1")
    assert response.status_code == 200

    data = response.json()
    assert Course(**data)


def test_get_courses():
    response = client.get("/course")
    assert response.status_code == 200

    data = response.json()
    for course in data:
        assert Course(**course)
