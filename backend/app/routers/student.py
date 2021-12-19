from app.db.crud import create_student
from app.db.crud import delete_student_by_id
from app.db.crud import get_student_by_id
from app.db.crud import get_students
from app.db.crud import update_student_by_id
from app.db.psql import get_session
from app.db.psql_models import Student
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/student",
    tags=["student"],
    responses={404: {"description": "Student not found"}}
)


@router.get("/{student_id}")
async def read_specific_student(student_id: int, db: Session = Depends(get_session)):
    db_student = get_student_by_id(db=db, student_id=student_id)
    if db_student:
        return db_student
    raise HTTPException(status_code=404, detail="Student not found")


@router.get("/")
async def read_all_students(db: Session = Depends(get_session)):
    return get_students(db=db)


@router.post("/")
async def write_student(student: Student, db: Session = Depends(get_session)):
    db_student = create_student(db=db, student=student)
    if db_student:
        return db_student
    raise HTTPException(status_code=422, detail="request could not be completed")


@router.put("/{student_id}")
async def update_student(student_id: int, db: Session = Depends(get_session)):
    update_student_by_id(db=db, student_id=student_id)


@router.delete("/{student_id}")
async def remove_student(student_id: int, db: Session = Depends(get_session)):
    delete_student_by_id(db=db, student_id=student_id)
