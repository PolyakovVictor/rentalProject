from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

db_username = os.getenv('username_db')
db_password = os.getenv('password')
db_host = os.getenv('host')
db_name = os.getenv('database')

engine = create_engine(
    f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}",
    echo=True
    )

Base = declarative_base()
