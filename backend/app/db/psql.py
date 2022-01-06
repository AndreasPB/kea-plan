from app.config import get_settings
from sqlmodel import create_engine
from sqlmodel import Session

SQLMODEL_DATABASE_URL = f"postgresql://{get_settings().psql_user}:"\
        f"{get_settings().psql_pwd}@postgres:5432/KEAPlan"
engine = create_engine(SQLMODEL_DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
