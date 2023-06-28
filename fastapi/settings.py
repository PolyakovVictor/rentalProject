# from functools import lru_cache

# from pydantic import BaseSettings, PostgresDsn
# from dotenv import load_dotenv
# load_dotenv()


# class Settings(BaseSettings):
#     db_url: PostgresDsn
#     jwt_secret_key: str

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"


# @lru_cache
# def get_settings() -> Settings:
#     return Settings()
