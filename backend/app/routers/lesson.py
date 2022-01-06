from app.db.crud import create_lesson
from app.db.crud import delete_lesson_by_id
from app.db.crud import get_lesson_by_id
from app.db.crud import get_lesson_by_token
from app.db.crud import get_lessons
from app.db.crud import update_lesson_by_id
from app.db.psql import get_session
from app.db.psql_models import Lesson
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session

router = APIRouter(
    prefix="/lesson",
    tags=["lesson"],
    responses={404: {"description": "Lesson not found"}}
)


@router.get("/{lesson_id}")
async def read_specific_lesson(lesson_id: int, db: Session = Depends(get_session)):
    db_lesson = get_lesson_by_id(db=db, lesson_id=lesson_id)
    if db_lesson:
        return db_lesson
    raise HTTPException(status_code=404, detail="Lesson not found")


@router.get("/token/{token}")
async def read_lesson_from_token(token: str, db: Session = Depends(get_session)):
    if db_token := get_lesson_by_token(db=db, token=token):
        return db_token
    raise HTTPException(status_code=404, detail="Token not found")


@router.get("/")
async def read_all_lessons(db: Session = Depends(get_session)):
    return get_lessons(db=db)


@router.post("/")
async def write_lesson(lesson: Lesson, db: Session = Depends(get_session)):
    db_lesson = create_lesson(db=db, lesson=lesson)
    if db_lesson:
        return db_lesson
    raise HTTPException(status_code=422, detail="request could not be completed")


@router.put("/{lesson_id}")
async def update_lesson(lesson_id: int, db: Session = Depends(get_session)):
    update_lesson_by_id(db=db, lesson_id=lesson_id)


@router.delete("/{lesson_id}")
async def remove_lesson(lesson_id: int, db: Session = Depends(get_session)):
    delete_lesson_by_id(db=db, lesson_id=lesson_id)
