from fastapi import APIRouter
from fastapi import Form

router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post("/")
async def login(username: str = Form(...), password: str = Form(...)):
    users = [
        {"username": "bruger123", "password": "123"},
        {"username": "bruger456", "password": "456"},
        {"username": "bruger789", "password": "789"},
    ]

    for user in users:
        if user["username"] == username and user["password"] == password:
            return {"status": "success", "data": f"Logged in as {username}"}

    return {"status": "unsuccessful", "username": username, "password": "yea, no"}
