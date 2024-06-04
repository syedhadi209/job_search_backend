from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_url: str
    jwt_secret: str
    algorithm: str
    database_name: str

    class Config:
        env_file = ".env"


settings = Settings()