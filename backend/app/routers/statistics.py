from app.db.redis_models import Semester
from app.db.redis_models import Student
from app.db.redis_test_data import test_semesters
from app.db.redis_test_data import test_students
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
    responses={404: {"description": "Statistic(s) not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# Students
@router.post("/student")
async def create_students(students: list[Student]) -> Student:
    return await Student.insert(students)


@router.get("/student/{user_id}")
async def read_student(user_id: int) -> Student:
    if student := await Student.select(ids=user_id):
        return student[0]
    raise HTTPException(status_code=404, detail="Student not found")


@router.get("/students")
async def read_students() -> list[Student]:
    if students := await Student.select():
        return students
    raise HTTPException(status_code=404, detail="Students not found")


@router.put("/student/{user_id}")
async def update_student(user_id: int, student: Student) -> Student:
    await Student.update(_id=user_id, data=student)
    student = await Student.select(ids=user_id)
    return student[0]


@router.delete("/student/{user_id}")
async def delete_student(user_id: int) -> Student:
    student = await Student.select(ids=user_id)
    await student[0].delete()
    return student[0]


# Semesters
@router.get("/semesters")
async def read_semesters() -> list[Semester]:
    if semesters := await Semester.select():
        return semesters
    raise HTTPException(status_code=404, detail="Semesters not found")


@router.get("/semester/{class_id}")
async def read_semester(class_id: int) -> Semester:
    if semester := await Semester.select(ids=class_id):
        return semester[0]
    raise HTTPException(status_code=404, detail="Semester not found")


# For testing
@router.post("/test/student")
async def create_test_students() -> list[Student]:
    await Student.insert(test_students)
    return test_students


@router.delete("/test/students")
async def delete_test_students() -> list[Student]:
    if students := await Student.select():
        for student in students:
            await student.delete()
        return students
    raise HTTPException(status_code=500, detail="No students to delete")


@router.post("/test/semesters")
async def create_test_semesters() -> list[Semester]:
    await Semester.insert(test_semesters)
    return test_semesters


@router.delete("/test/semesters")
async def delete_test_semesters() -> list[Semester]:
    if semesters := await Semester.select():
        for semester in semesters:
            await semester.delete()
        return semesters
    raise HTTPException(status_code=500, detail="No semesters to delete")
