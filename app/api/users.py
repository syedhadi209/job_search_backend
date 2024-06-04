from fastapi import APIRouter, Depends, HTTPException, status,Response
from app.services.user_service import get_user_by_email,create_user
from app.services.jobs_service import fuzzy_search
from app.schemas.users import UserCreate,UserResponse,JobQuery
from app.utils.security import hash_password,verify_password
from app.models.users import User
from app.utils.security import create_access_token,get_current_user
from typing import Annotated
import csv
from app.db.get_db import get_database

UserRouter = APIRouter()

@UserRouter.post("/auth/signup")
async def signup(user: UserCreate):
    db_user = await get_user_by_email(user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    user_obj = User(
        email=user.email,
        hashed_password=hashed_password
    )

    new_user = await create_user(user_obj)
    return UserResponse(id=str(new_user.id), email=new_user.email)

@UserRouter.post("/auth/login")
async def login(user_data: UserCreate):
    user = await get_user_by_email(user_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(user_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token_data = {"sub": str(user["_id"]), "email": user['email']}
    response = {
        "accessToken":create_access_token(token_data),
        "user":UserResponse(id=str(user["_id"]), email=user['email'])
    }
    return response

@UserRouter.get("/current-session")
async def get_current_session(current_user: Annotated[User,Depends(get_current_user)]):
    return UserResponse(id=str(current_user["_id"]), email=current_user['email'])


@UserRouter.get("/seed-data")
async def seed_data_to_db():
    db = await get_database()

    with open("app\data\jobs_data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)

        documents = [{"job_name": row[1]} for row in csv_reader]

        if documents:
            await db['jobs'].insert_many(documents)

    return {"message": "Data seeded successfully"}


@UserRouter.post("/jobs-listings")
async def get_jobs_listings(query: JobQuery):
    results = await fuzzy_search(query.query)
    return results