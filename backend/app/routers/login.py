# import random
# import string
# from typing import Optional
#
# from fastapi import APIRouter
# from fastapi import Depends
# from fastapi import HTTPException
# from fastapi import status
# from fastapi.security import OAuth2PasswordBearer
# from fastapi.security import OAuth2PasswordRequestForm
# from pydantic import BaseModel
#
# router = APIRouter(
#     prefix="/login",
#     tags=["login"],
# )
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
# users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "password": "123",
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "password": "321",
#     },
# }
#
#
# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
#
#
# class UserInDB(User):
#     password: str
#
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
# async def get_current_user(token: str = Depends()):
#     user = token
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user
#
#
# @router.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail=
#         "Incorrect username or password")
#     password = form_data.password
#     if not password == user.password:
#         raise HTTPException(status_code=400, detail=
#         "Incorrect username or password")
#
#     return {
#         "access_token": (
#             "".join(
#                 random.choice(string.ascii_uppercase + string.digits)
#                 for _ in range(25)
#             )
#         ),
#         "token_type": "bearer",
#     }
#
#
# @router.get("/users/me")
# async def read_users_me(token: str = Depends(oauth2_scheme)):
#     return {"the_token": token}
