from app.db.crud import create_studentclass
from app.db.crud import delete_studentclass_by_id
from app.db.crud import get_studentclass_by_id
from app.db.crud import update_studentclass_by_id
from app.db.psql import get_session
from app.db.psql_models import StudentClass
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/studentclass",
    tags=["studentclass"],
    responses={404: {"description": "StudentClass not found"}}
)


@router.get("/{studentclass_id}", response_model=StudentClass)
async def read_specific_studentclass(studentclass_id: int,
                                     db: Session = Depends(get_session)):
    db_studentclass = get_studentclass_by_id(db=db, studentclass_id=studentclass_id)
    if db_studentclass:
        return db_studentclass
    raise HTTPException(status_code=404, detail="student class not found")


@router.post("/")
async def write_studentclass(studentclass: StudentClass,
                             db: Session = Depends(get_session)):
    db_studentclass = create_studentclass(db=db, studentclass=studentclass)
    if db_studentclass:
        return db_studentclass
    raise HTTPException(status_code=422, detail="request could not be completed")


@router.put("/{studentclass_id}")
async def update_studentclass(studentclass_id, db: Session = Depends(get_session)):
    update_studentclass_by_id(db=db, studentclass_id=studentclass_id)


@router.delete("/{studentclass_id}")
async def remove_studentclass(studentclass_id: int, db: Session = Depends(get_session)):
    delete_studentclass_by_id(db=db, studentclass_id=studentclass_id)
