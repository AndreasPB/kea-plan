import asyncio
import random
import string
from typing import Optional

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
from app.routers import statistics
from app.routers import student
from app.routers import student_attendance
from app.routers import studentclass
from app.routers import studentclass_course
from app.routers import test_psql
from app.routers import token
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from pydantic.class_validators import validator
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
        print("Will try again in 4 seconds...")
        await asyncio.sleep(4)
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


users_db = {
    "henrikpoelse@stud.kea.dk": {
        "username": "henrikpoelse6666",
        "full_name": "John Doe",
        "password": "123456",
        "user_type": "student",
        "person_id": 1,
        "class_id": 1,
    },
    "pubae@stud.kea.dk": {
        "username": "pubae1234",
        "full_name": "Bølle Bob",
        "password": "321",
        "user_type": "lecturer",
        "person_id": 4,
        "class_id": 2,
    },
}


# TODO implement email validation https://github.com/JoshData/python-email-validator
class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    user_type: str
    person_id: int
    class_id: int


class UserInDB(User):
    password: str


class UserInput(BaseModel):
    username: Optional[str]
    password: Optional[str]

    @validator("username")
    def validate_username_length(cls, v):
        if len(v) < 6:
            raise HTTPException(
                status_code=400,
                detail="Username invalid format - must be at least 6 characters",
            )
        if len(v) > 45:
            raise HTTPException(
                status_code=400,
                detail="Username invalid format - must be under 30 characters",
            )
        return v

    @validator("password")
    def validate_password_length(cls, v):
        if len(v) < 2:
            raise HTTPException(
                status_code=400,
                detail="Password invalid format - must be at least 5 characters",
            )
        if len(v) > 20:
            raise HTTPException(
                status_code=400,
                detail="Password invalid format - must be under 30 characters",
            )
        return v


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_input = UserInput(username=form_data.username)
    user_dict = users_db.get(user_input.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username")
    user = UserInDB(**user_dict)
    user_input = UserInput(password=form_data.password)
    password = user_input.password
    if not password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {
        "access_token": (
            "".join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(25)
            )
        ),
        "token_type": "bearer",
        "username": user.username,
        "full_name": user.full_name,
        "user_type": user.user_type,
        "person_id": user.person_id,
        "class_id": user.class_id,
    }
