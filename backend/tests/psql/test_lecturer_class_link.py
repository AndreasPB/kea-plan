from app.db.crud import get_lecturer_classes
from app.db.psql import engine
from app.db.psql_models import LecturerClassLink
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_lecturer_class_link():
    response = client.get("/lecturer_studentclass/1")
    assert response.status_code == 200


def test_get_lecturer_class_links():
    response = client.get("/lecturer_studentclass")
    assert response.status_code == 200

    data = response.json()
    for lecturer_class in data:
        assert LecturerClassLink(**lecturer_class)

    with Session(engine) as session:
        db_data = get_lecturer_classes(session)
        assert db_data == [
            LecturerClassLink(**lecturer_class) for lecturer_class in data
        ]
