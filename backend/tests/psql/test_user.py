from app.db.crud import get_user_by_id
from app.db.psql import engine
from app.db.psql_models import User
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session

client = TestClient(app)


def test_get_user():
    with Session(engine) as session:
        db_data = get_user_by_id(session, 1)
        assert db_data == User()


def test_get_users():
    pass
