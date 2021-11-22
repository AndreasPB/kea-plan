from fastapi import APIRouter
from fastapi import Form

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/student/{id}")
async def read_student(id: int) -> dict[list[int, str, str]]:
    # TODO: Repace awful if-logic with Redis lookup for student id

    if id == 1:
        return {
            "data": [
                {"id": 1, "name": "Large systems", "attendance": "91%"},
                {"id": 2, "name": "Small systems", "attendance": "81%"},
                {"id": 3, "name": "Medium systems", "attendance": "71%"},
            ]
        }
    if id == 2:
        return {
            "data": [
                {"id": 1, "name": "Large systems", "attendance": "42%"},
                {"id": 2, "name": "Small systems", "attendance": "22%"},
                {"id": 3, "name": "Medium systems", "attendance": "12%"},
            ]
        }
    if id == 3:
        return {
            "data": [
                {"id": 1, "name": "Large systems", "attendance": "83%"},
                {"id": 2, "name": "Small systems", "attendance": "43%"},
                {"id": 3, "name": "Medium systems", "attendance": "13%"},
            ]
        }


@router.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    users = [
        {"username": "bruger123", "password": "123"},
        {"username": "bruger456", "password": "456"},
        {"username": "bruger789", "password": "789"},
    ]

    for user in users:
        if user["username"] == username and user["password"] == password:
            return {"status": "success",
                    "data": f"Logged in as {username}"}

    return {"status": "unsuccessful", "username": username, "password": "yea, no"}
