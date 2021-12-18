from app.db.crud import create_attendance
from app.db.crud import delete_attendance_by_id
from app.db.crud import get_attendance_by_id
from app.db.crud import get_attendances
from app.db.crud import update_attendance_by_id
from app.db.psql import get_session
from app.db.psql_models import Attendance
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/attendance",
    tags=["attendance"],
    responses={404: {"description": "Attendance not found"}},
)


@router.get("/{attendance_id}")
async def read_specific_attendance(
    attendance_id: int, db: Session = Depends(get_session)
):
    db_attendance = get_attendance_by_id(db=db, attendance_id=attendance_id)
    if db_attendance:
        return db_attendance
    raise HTTPException(status_code=404, detail="Attendance not found")


@router.get("/")
async def read_all_attendances(db: Session = Depends(get_session)):
    return get_attendances(db=db)


@router.post("/")
async def write_attendance(attendance: Attendance, db: Session = Depends(get_session)):
    db_attendance = create_attendance(db=db, attendance=attendance)
    if db_attendance:
        return db_attendance
    raise HTTPException(status_code=422, detail="Could not create attendance")


@router.put("/{attendance_id}")
async def update_attendance(attendance_id: int, db: Session = Depends(get_session)):
    update_attendance_by_id(db=db, attendance_id=attendance_id)


@router.delete("/{attendance_id}")
async def remove_attendance(attendance_id: int, db: Session = Depends(get_session)):
    delete_attendance_by_id(db=db, attendance_id=attendance_id)
