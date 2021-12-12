from app.db.crud import create_studentclass_course
from app.db.crud import get_studentclass_course_by_id
from app.db.psql import get_session
from app.db.psql_models import StudentClassCourseLink
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/studentclass_course",
    tags=["StudentClass Course Link"],
    responses={404: {"description": "StudentClass Course link not found"}},
)


@router.get("/{studentclass_id}")
async def read_specific_studentclass_course(
    studentclass_id: int, db: Session = Depends(get_session)
):
    db_studentclass_course = get_studentclass_course_by_id(
        db=db, studentclass_id=studentclass_id
    )
    if db_studentclass_course:
        return db_studentclass_course
    raise HTTPException(status_code=404, detail="studentclass course not found")


@router.post("/")
async def write_studentclass_course(
    studentclass_course: StudentClassCourseLink, db: Session = Depends(get_session)
):
    db_studentclass_course = create_studentclass_course(
        db=db, studentclass_course=studentclass_course
    )
    if db_studentclass_course:
        return db_studentclass_course
    raise HTTPException(
        status_code=404, detail="StudentClass Course link could not be created"
    )
