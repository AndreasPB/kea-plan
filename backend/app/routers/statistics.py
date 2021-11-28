from app.db.redis import Class
from app.db.redis import Student
from app.db.redis_test_data import test_classes
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


@router.post("/test/classes")
async def create_test_classes() -> list[Class]:
    await Class.insert(test_classes)
    return test_classes


@router.delete("/test/classes")
async def delete_test_classes() -> list[Class]:
    if classes := await Class.select():
        for class_ in classes:
            await class_.delete()
        return classes
    raise HTTPException(status_code=500, detail="No classes to delete")
