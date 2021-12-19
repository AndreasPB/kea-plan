from app.db.crud import get_student_by_id
from app.db.crud import get_students
from app.db.psql import engine
from app.db.psql_models import Student
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_student():
    response = client.get("/student/1")
    assert response.status_code == 200

    data = response.json()
    assert Student(**data)

    with Session(engine) as session:
        db_data = get_student_by_id(session, 1)
        assert db_data == Student(**data)


def test_get_students():
    response = client.get("/student")
    assert response.status_code == 200

    data = response.json()
    for student in data:
        assert Student(**student)

    with Session(engine) as session:
        db_data = get_students(session)
        assert db_data == [Student(**student) for student in data]
