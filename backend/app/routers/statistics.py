from app.db.redis_models import Semester
from app.db.redis_models import Student
from app.db.redis_test_data import test_semesters
from app.db.redis_test_data import test_students
from fastapi import APIRouter
from fastapi import HTTPException


router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
    responses={404: {"description": "Statistic(s) not found"}},
)


@router.post("/student")
async def create_students(students: list[Student]) -> Student:
    return await Student.insert(students)


@router.get("/student/{id}")
async def read_student(id: int) -> Student:
    if student := await Student.select(ids=id):
        return student[0]
    raise HTTPException(status_code=404, detail="Student not found")


@router.get("/students")
async def read_students() -> list[Student]:
    if students := await Student.select():
        return students
    raise HTTPException(status_code=404, detail="Students not found")


@router.put("/student/{id}")
async def update_student(id: int, student: Student) -> Student:
    await Student.update(_id=id, data=student)
    student = await Student.select(ids=id)
    return student[0]


@router.delete("/student/{id}")
async def delete_student(id: int) -> Student:
    student = await Student.select(ids=id)
    await student[0].delete()
    return student[0]


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
