import asyncio

from app.db.models import SQLModel
from app.db.redis import Class
from app.db.redis import Student
from app.db.redis_test_data import test_classes
from app.db.redis_test_data import test_students
from app.db.sql import engine
from app.routers import login
from app.routers import statistics
from app.routers import token
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(statistics.router)
app.include_router(token.router)


@app.on_event("startup")
async def init_db():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(e)
        print("Will try again in 2 seconds...")
        await asyncio.sleep(2)
        SQLModel.metadata.create_all(engine)


# TODO: Replace when done testing
@app.on_event("startup")
async def init_redis():
    try:
        await Student.insert(test_students)
        await Class.insert(test_classes)
    except Exception as e:
        print(e)
        print("Will try again in 2 seconds...")
        await asyncio.sleep(2)
        await Student.insert(test_students)
        await Class.insert(test_classes)


@app.get("/")
async def read_root():
    return {"message": "Welcome to KEAPlan's Web API - Go to /docs for an API overview"}
