# THIS FILE NOT YET USED ANYWHERE


from sqlalchemy import select
from models import Address


class CRUD:
    def __init__(self, session):
        self.session = session

    async def add(self, model):
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model.__dict__

    async def get_by_id(self, model, id):
        return (await self.session.get(model, id))

    async def get_all(self, model):
        stmt = select(model)
        result = await self.session.execute(stmt)
        objects = result.scalars().all()
        return [obj.__dict__ for obj in objects]

    async def delete(self, model):
        await self.session.delete(model)
        await self.session.commit()

    async def get_filter_apartments(self, model, max_price=None, title=None, city=None, country=None, room_count=None, type=None):
        stmt = select(model).join(Address, model.id == Address.apartment_id)

        if max_price is not None:
            stmt = stmt.where(model.price <= max_price)
        if room_count is not None:
            stmt = stmt.where(model.room_count == room_count)
        if type is not None:
            stmt = stmt.where(model.type.ilike(f'%{type}%'))
        if title is not None:
            stmt = stmt.where(model.title.ilike(f'%{title}%'))
        if city is not None:
            stmt = stmt.where(Address.city.ilike(f'%{city}%'))
        if country is not None:
            stmt = stmt.where(Address.country.ilike(f'%{country}%'))

        result = await self.session.execute(stmt)
        objects = result.scalars().all()
        return [obj.__dict__ for obj in objects]
