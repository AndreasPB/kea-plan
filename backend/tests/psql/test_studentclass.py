import pytest
from app.db.crud import get_studentclass_by_id
from app.db.crud import get_studentclasses
from app.db.psql import engine
from app.db.psql_models import StudentClass
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_studentclass():
    response = client.get("/studentclass/1")
    assert response.status_code == 200

    data = response.json()
    assert StudentClass(**data)

    with Session(engine) as session:
        db_data = get_studentclass_by_id(session, 1)
        assert db_data == StudentClass(**data)


def test_get_studentclasses():
    response = client.get("/studentclass")
    assert response.status_code == 200

    data = response.json()
    for studentclass in data:
        assert StudentClass(**studentclass)


@pytest.mark.skip(reason="TODO: Don't understand the error")
def test_create_studentclass():
    test_studentclass = StudentClass(id=9001, name="Test", number_of_students=1337)

    response = client.post("/studentclass", json=test_studentclass.json())

    assert response.status_code == 200

    data = response.json()
    assert StudentClass(**data)

    with Session(engine) as session:
        db_data = get_studentclasses(session)
        assert db_data == [StudentClass(**studentclass) for studentclass in data]
