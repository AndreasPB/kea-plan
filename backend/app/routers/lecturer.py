from app.db.crud import create_lecturer
from app.db.crud import delete_lecturer_by_id
from app.db.crud import get_lecturer_by_id
from app.db.crud import update_lecturer_by_id
from app.db.psql import get_session
from app.db.psql_models import Lecturer
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/lecturer",
    tags=["lecturer"],
    responses={404: {"description": "Lecturer not found"}}
)


@router.get("/{lecturer_id}")
async def read_specific_lecturer(lecturer_id: int, db: Session = Depends(get_session)):
    db_lecturer = get_lecturer_by_id(db=db, lecturer_id=lecturer_id)
    if db_lecturer:
        return db_lecturer
    raise HTTPException(status_code=404, detail="Lecturer not found")


@router.post("/")
async def write_lecturer(lecturer: Lecturer, db: Session = Depends(get_session)):
    db_lecturer = create_lecturer(db=db, lecturer=lecturer)
    if db_lecturer:
        return db_lecturer
    raise HTTPException(status_code=422, detail="request could not be completed")


@router.put("/{lecturer_id}")
async def update_lecturer(lecturer_id: int, db: Session = Depends(get_session)):
    update_lecturer_by_id(db=db, lecturer_id=lecturer_id)


@router.delete("/{lecturer_id}")
async def remove_lecturer(lecturer_id: int, db: Session = Depends(get_session)):
    delete_lecturer_by_id(db=db, lecturer_id=lecturer_id)
