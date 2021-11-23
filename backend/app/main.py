import asyncio

from app.db.db import engine
from app.db.models import SQLModel
from app.routers import router
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

app.include_router(router)


@app.on_event("startup")
async def init_db():
    await asyncio.sleep(2)
    SQLModel.metadata.create_all(engine)
