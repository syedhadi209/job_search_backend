from app.models.users import User
from app.db.get_db import get_database
from bson import ObjectId

async def get_user_by_email(email: str):
    db = await get_database()
    user = await db["users"].find_one({"email": email})
    return user if user else None

async def create_user(user: User):
    db = await get_database()
    result = await db["users"].insert_one(user.model_dump(by_alias=True,exclude=["id"]))

    user.id = result.inserted_id
    return user