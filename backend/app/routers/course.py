from app.db.crud import create_course
from app.db.crud import delete_course_by_id
from app.db.crud import get_course_by_id
from app.db.crud import update_course_by_id
from app.db.psql import get_session
from app.db.psql_models import Course
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/course",
    tags=["course"],
    responses={404: {"description": "Course not found"}}
)


@router.get("/{course_id}")
async def read_specific_course(course_id: int, db: Session = Depends(get_session)):
    db_course = get_course_by_id(db=db, course_id=course_id)
    if db_course:
        return db_course
    raise HTTPException(status_code=404, detail="Course not found")


@router.post("/")
async def write_course(course: Course, db: Session = Depends(get_session)):
    db_course = create_course(db=db, course=course)
    if db_course:
        return db_course
    raise HTTPException(status_code=422, detail="request could not be completed")


@router.put("/{course_id}")
async def update_course(course_id: int, db: Session = Depends(get_session)):
    update_course_by_id(db=db, course_id=course_id)


@router.delete("/{course_id}")
async def remove_course(course_id: int, db: Session = Depends(get_session)):
    delete_course_by_id(db=db, course_id=course_id)
