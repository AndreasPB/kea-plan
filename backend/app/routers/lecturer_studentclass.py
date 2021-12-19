from app.db.crud import create_lecturer_studentclass
from app.db.crud import get_lecturer_classes
from app.db.crud import get_lecturer_studentclass_by_id
from app.db.psql import get_session
from app.db.psql_models import LecturerClassLink
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/lecturer_studentclass",
    tags=["Lecturer StudentClass Link"],
    responses={404: {"description": "Lecturer StudentClass link not found"}},
)


@router.get("/{lecturer_id}")
async def read_specific_lecturer_studentclass(
    lecturer_id: int, db: Session = Depends(get_session)
):
    db_lecturer_studentclass = get_lecturer_studentclass_by_id(
        db=db, lecturer_id=lecturer_id
    )
    if db_lecturer_studentclass:
        return db_lecturer_studentclass
    raise HTTPException(status_code=404, detail="Lecturer StudentClass not found")


@router.get("/")
async def read_all_lecturer_studentclass(db: Session = Depends(get_session)):
    return get_lecturer_classes(db=db)


@router.post("/")
async def write_lecturer_studentclass(
    lecturer_studentclass: LecturerClassLink, db: Session = Depends(get_session)
):
    db_lecturer_studentclass = create_lecturer_studentclass(
        db=db, lecturer_studentclass=lecturer_studentclass
    )
    if db_lecturer_studentclass:
        return db_lecturer_studentclass
    raise HTTPException(
        status_code=422, detail="Lecturer StudentClass link could not be created"
    )
