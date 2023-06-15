from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import get_settings


engine = create_engine(
    get_settings().db_url,
    echo=True
    )

Base = declarative_base()
