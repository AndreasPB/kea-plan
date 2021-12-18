import asyncio

from app.db.psql import engine
from app.db.psql_models import SQLModel
from app.db.psql_test_data import setup_psql_test_attendances
from app.db.psql_test_data import setup_psql_test_data
from app.db.psql_test_data import setup_psql_test_links
from app.db.redis import Semester
from app.db.redis import Student
from app.db.redis_test_data import test_semesters
from app.db.redis_test_data import test_students
from app.routers import attendance
from app.routers import course
from app.routers import course_lesson
from app.routers import lecturer
from app.routers import lecturer_studentclass
from app.routers import lesson
from app.routers import login
from app.routers import statistics
from app.routers import student
from app.routers import student_attendance
from app.routers import studentclass
from app.routers import studentclass_course
from app.routers import test_psql
from app.routers import token
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:2000",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(statistics.router)
app.include_router(token.router)
app.include_router(studentclass.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(lecturer.router)
app.include_router(lesson.router)
app.include_router(attendance.router)
app.include_router(course_lesson.router)
app.include_router(student_attendance.router)
app.include_router(studentclass_course.router)
app.include_router(lecturer_studentclass.router)
app.include_router(test_psql.router)


@app.on_event("startup")
async def init_db():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(e)
        print("Will try again in 2 seconds...")
        await asyncio.sleep(3)
        SQLModel.metadata.create_all(engine)
    finally:
        setup_psql_test_data()
        setup_psql_test_attendances()
        setup_psql_test_links()
        print("PostgreSQL database initialized")


# TODO: Replace when done testing
@app.on_event("startup")
async def init_redis():
    try:
        await Student.insert(test_students)
        await Semester.insert(test_semesters)
    except Exception as e:
        print(e)
        print("Will try again in 2 seconds...")
        await asyncio.sleep(2)
        await Student.insert(test_students)
        await Semester.insert(test_semesters)


@app.get("/")
async def read_root():
    return {"message": "Welcome to KEAPlan's Web API - Go to /docs for an API overview"}
