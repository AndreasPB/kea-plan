from app.db.crud import create_student_attendance
from app.db.crud import get_student_attendances
from app.db.crud import get_student_attendances_by_id
from app.db.psql import get_session
from app.db.psql_models import StudentAttendanceLink
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/student_attendance",
    tags=["Student Attendance Link"],
    responses={404: {"description": "Student Attendance Link not found"}},
)


@router.get("/{student_id}")
async def read_specific_student_attendance(
    student_id: int, db: Session = Depends(get_session)
):
    db_student_attendance = get_student_attendances_by_id(db=db, student_id=student_id)
    if db_student_attendance:
        return db_student_attendance
    raise HTTPException(status_code=404, detail="student attendance not found")


@router.get("/")
async def read_all_student_attendances(db: Session = Depends(get_session)):
    return get_student_attendances(db=db)


@router.post("/")
async def write_student_attendance(
    student_attendance: StudentAttendanceLink, db: Session = Depends(get_session)
):
    db_student_attendance = create_student_attendance(
        db=db, student_attendance=student_attendance
    )
    if db_student_attendance:
        return db_student_attendance
    raise HTTPException(
        status_code=422, detail="Student Attendance link could not be created"
    )
