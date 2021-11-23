from app.db.db import engine
from app.db.models import SQLModel
from app.routers import router
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

SQLModel.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
