from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import group, groupUser, apartment, address
from operations.schemas import ApartmentCreate, AddressCreate

router = APIRouter(
    prefix="/rental",
    tags=["Rental"]
)


@router.get("/get-apartaments")
async def get_apartaments(apartment_title: str,
                          session: AsyncSession = Depends(get_async_session)):
    query = select(apartment).where(apartment.c.title == apartment_title)
    result = await session.execute(query)
    result = result.fetchall()
    return result[0]


@router.post("/add-apartament")
async def add_apartament(new_apartment: ApartmentCreate,
                         session: AsyncSession = Depends(get_async_session)):
    stmt = insert(apartment).values(**new_apartment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/delete-apartament")
async def delete_apartament(apartment_id: int,
                            session: AsyncSession = Depends(get_async_session)):
    query = select(apartment).where(apartment.c.id == apartment_id)
    result = await session.execute(query)
    result = result.fetchall()
    return result


@router.post("/add-address")
async def add_address(new_address: AddressCreate,
                      session: AsyncSession = Depends(get_async_session)):
    stmt = insert(address).values(**new_address.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add-group")
async def add_group(new_group: int,
                    session: AsyncSession = Depends(get_async_session)):
    stmt = insert(group).values(id=new_group)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
