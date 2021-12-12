from app.db.crud import create_course_lesson
from app.db.crud import get_course_lessons_by_id
from app.db.psql import get_session
from app.db.psql_models import CourseLessonLink
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/course_lesson",
    tags=["Course Lesson Link"],
    responses={404: {"description": "Course Lesson link not found"}}
)


@router.get("/{course_id}")
async def read_specific_course_lesson(course_id: int,
                                      db: Session = Depends(get_session)):
    db_course_lesson = get_course_lessons_by_id(db=db, course_id=course_id)
    if db_course_lesson:
        return db_course_lesson
    raise HTTPException(status_code=404, detail="course lesson not found")


@router.post("/")
async def write_course_lesson(course_lesson: CourseLessonLink,
                              db: Session = Depends(get_session)):
    db_course_lesson = create_course_lesson(db=db, course_lesson=course_lesson)
    if db_course_lesson:
        return db_course_lesson
    raise HTTPException(status_code=422,
                        detail="Course Lesson link could not be created")
