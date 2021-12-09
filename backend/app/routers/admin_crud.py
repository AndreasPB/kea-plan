from app.db.crud import create_attendance
from app.db.crud import create_course
from app.db.crud import create_lecturer
from app.db.crud import create_lesson
from app.db.crud import create_student
from app.db.crud import create_studentclass
from app.db.crud import delete_attendance_by_id
from app.db.crud import delete_course_by_id
from app.db.crud import delete_lecturer_by_id
from app.db.crud import delete_lesson_by_id
from app.db.crud import delete_student_by_id
from app.db.crud import delete_studentclass_by_id
from app.db.crud import get_attendance_by_id
from app.db.crud import get_course_by_id
from app.db.crud import get_lecturer_by_id
from app.db.crud import get_lesson_by_id
from app.db.crud import get_student_by_id
from app.db.crud import get_studentclass_by_id
from app.db.psql import get_session
from app.db.psql_models import Attendance
from app.db.psql_models import Course
from app.db.psql_models import Lecturer
from app.db.psql_models import Lesson
from app.db.psql_models import Student
from app.db.psql_models import StudentClass
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)


# StudentClass
@router.get("/class/{studentclass_id}", response_model=StudentClass)
async def read_specific_studentclass(studentclass_id: int,
                                     db: Session = Depends(get_session)):
    db_studentclass = get_studentclass_by_id(db=db, studentclass_id=studentclass_id)
    if db_studentclass:
        return db_studentclass
    raise HTTPException(status_code=404, detail="student class not found")


@router.post("/class")
async def write_studentclass(studentclass: StudentClass,
                             db: Session = Depends(get_session)):
    db_studentclass = create_studentclass(db=db, studentclass=studentclass)
    if db_studentclass:
        return db_studentclass
    raise HTTPException(status_code=409, detail="request could not be completed")


async def update_studentclass(studentclass_id, db: Session = Depends(get_session)):
    ...


@router.delete("/class/{studentclass_id}")
async def remove_studentclass(studentclass_id: int, db: Session = Depends(get_session)):
    delete_studentclass_by_id(db=db, studentclass_id=studentclass_id)


# Student
@router.get("/student/{student_id}")
async def read_specific_student(student_id: int, db: Session = Depends(get_session)):
    db_student = get_student_by_id(db=db, student_id=student_id)
    if db_student:
        return db_student
    raise HTTPException(status_code=404, detail="Student not found")


@router.post("/student")
async def write_student(student: Student, db: Session = Depends(get_session)):
    db_student = create_student(db=db, student=student)
    if db_student:
        return db_student
    raise HTTPException(status_code=409, detail="request could not be completed")


async def update_student(student_id: int, db: Session = Depends(get_session)):
    ...


@router.delete("/student/{student_id}")
async def remove_student(student_id: int, db: Session = Depends(get_session)):
    delete_student_by_id(db=db, student_id=student_id)


# Course
@router.get("/course/{course_id}")
async def read_specific_course(course_id: int, db: Session = Depends(get_session)):
    db_course = get_course_by_id(db=db, course_id=course_id)
    if db_course:
        return db_course
    raise HTTPException(status_code=404, detail="Course not found")


@router.post("/course")
async def write_course(course: Course, db: Session = Depends(get_session)):
    db_course = create_course(db=db, course=course)
    if db_course:
        return db_course
    raise HTTPException(status_code=409, detail="request could not be completed")


async def update_course(course_id: int, db: Session = Depends(get_session)):
    ...


@router.delete("/course/{course_id}")
async def remove_course(course_id: int, db: Session = Depends(get_session)):
    delete_course_by_id(db=db, course_id=course_id)


# Lecturer
@router.get("/lecturer/{lecturer_id}")
async def read_specific_lecturer(lecturer_id: int, db: Session = Depends(get_session)):
    db_lecturer = get_lecturer_by_id(db=db, lecturer_id=lecturer_id)
    if db_lecturer:
        return db_lecturer
    raise HTTPException(status_code=404, detail="Lecturer not found")


@router.post("/lecturer")
async def write_lecturer(lecturer: Lecturer, db: Session = Depends(get_session)):
    db_lecturer = create_lecturer(db=db, lecturer=lecturer)
    if db_lecturer:
        return db_lecturer
    raise HTTPException(status_code=409, detail="request could not be completed")


async def update_lecturer(lecturer_id: int, db: Session = Depends(get_session)):
    ...


@router.delete("/lecturer/{lecturer_id}")
async def remove_lecturer(lecturer_id: int, db: Session = Depends(get_session)):
    delete_lecturer_by_id(db=db, lecturer_id=lecturer_id)


# Lesson
@router.get("/lesson/{lesson_id}")
async def read_specific_lesson(lesson_id: int, db: Session = Depends(get_session)):
    db_lesson = get_lesson_by_id(db=db, lesson_id=lesson_id)
    if db_lesson:
        return db_lesson
    raise HTTPException(status_code=404, detail="Lesson not found")


@router.post("/lesson")
async def write_lesson(lesson: Lesson, db: Session = Depends(get_session)):
    db_lesson = create_lesson(db=db, lesson=lesson)
    if db_lesson:
        return db_lesson
    raise HTTPException(status_code=409, detail="request could not be completed")


async def update_lesson(lesson_id: int, db: Session = Depends(get_session)):
    ...


@router.delete("/lesson/{lesson_id}")
async def remove_lesson(lesson_id: int, db: Session = Depends(get_session)):
    delete_lesson_by_id(db=db, lesson_id=lesson_id)


# Attendance
@router.get("/attendance/{attendance_id}")
async def read_specific_attendance(attendance_id: int,
                                   db: Session = Depends(get_session)):
    db_attendance = get_attendance_by_id(db=db, attendance_id=attendance_id)
    if db_attendance:
        return db_attendance
    raise HTTPException(status_code=404, detail="Attendance not found")


@router.post("/attendance")
async def write_attendance(attendance: Attendance, db: Session = Depends(get_session)):
    db_attendance = create_attendance(db=db, attendance=attendance)
    if db_attendance:
        return db_attendance
    raise HTTPException(status_code=409, detail="Could not create attendance")


async def update_attendance(attendance_id: int, db: Session = Depends(get_session)):
    ...


@router.delete("/attendance/{attendance_id}")
async def remove_attendance(attendance_id: int, db: Session = Depends(get_session)):
    delete_attendance_by_id(db=db, attendance_id=attendance_id)
