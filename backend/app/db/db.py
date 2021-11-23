from sqlmodel import create_engine
from sqlmodel import Session

SQLMODEL_DATABASE_URL = "postgresql://postgres:postgres@database:5432/KEAPlan"
engine = create_engine(SQLMODEL_DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
