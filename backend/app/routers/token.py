import random
import string

from fastapi import APIRouter


router = APIRouter(
    prefix="/token",
    tags=["token"],
)

TOKEN_SIZE = 4
TOKEN_CHARS = string.ascii_uppercase + string.digits


@router.get("/generate")
async def generate_token():
    return "".join(random.choice(TOKEN_CHARS) for _ in range(TOKEN_SIZE))
