from sqlalchemy import select

# THIS FILE NOT YET USED ANYWHERE


class CRUD:
    def __init__(self, get_async_session):
        self.get_async_session = get_async_session

    async def create(self, obj):
        async with self.get_async_session() as session:
            session.add(obj)
            await session.commit()

    async def get_by_id(self, model, id):
        async with self.get_async_session() as session:
            query = select(model).filter(model.id == id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def update(self, obj):
        async with self.get_async_session() as session:
            session.add(obj)
            await session.commit()

    async def delete(self, obj):
        async with self.get_async_session() as session:
            session.delete(obj)
            await session.commit()
