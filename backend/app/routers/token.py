import random

from app.config import get_settings
from fastapi import APIRouter


router = APIRouter(
    prefix="/token",
    tags=["token"],
)


@router.get("/generate")
async def generate_token():
    return "".join(
        random.choice(get_settings().token_chars)
        for _ in range(get_settings().token_size)
    )
