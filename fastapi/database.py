# import asyncio
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# from settings import get_settings

# Base = declarative_base()
# engine = create_async_engine(
#     get_settings().db_url,
#     echo=True
#     )
# async_session_maker = sessionmaker(engine,
#                                    class_=AsyncSession,
#                                    expire_on_commit=False)


# async def get_async_session() -> AsyncSession:
#     session = async_session_maker()
#     return session
