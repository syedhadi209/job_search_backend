from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId
from pydantic import Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, field):
        field.update(type="string")
        return schema

class Jobs(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    job_name: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
