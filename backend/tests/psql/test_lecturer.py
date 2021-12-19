from app.db.crud import get_lecturer_by_id
from app.db.crud import get_lecturers
from app.db.psql import engine
from app.db.psql_models import Lecturer
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_lecturer():
    response = client.get("/lecturer/1")
    assert response.status_code == 200

    data = response.json()
    assert Lecturer(**data)

    with Session(engine) as session:
        db_data = get_lecturer_by_id(session, 1)
        assert db_data == Lecturer(**data)


def test_get_lecturers():
    response = client.get("/lecturer")
    assert response.status_code == 200

    data = response.json()
    for lecturer in data:
        assert Lecturer(**lecturer)

    with Session(engine) as session:
        db_data = get_lecturers(session)
        assert db_data == [Lecturer(**lecturer) for lecturer in data]
