from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    email: str | None = None

class JobQuery(BaseModel):
    query:str


class JobsResponse(BaseModel):
    id: str
    job_name: str
