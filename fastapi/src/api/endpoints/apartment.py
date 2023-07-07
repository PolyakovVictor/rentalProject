from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert, select, update, delete
from schemas import ApartmentCreate, AddressCreate, ApartmentModel, GroupModel
from database import get_async_session
from models import Apartment, Address, Group

router_apartment = APIRouter(
    prefix="/Apartment",
    tags=["Apartment"]
)


@router_apartment.post("/apartments")
async def create_apartment(apartment_data: ApartmentCreate,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        new_apartment = insert(Apartment).values(**apartment_data.dict())
        result = await session.execute(new_apartment)
        await session.commit()
        return {"id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.post("/addresses")
async def create_address(address_data: AddressCreate,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        new_address = insert(Address).values(**address_data.dict())
        result = await session.execute(new_address)
        await session.commit()
        return {"id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# READ
@router_apartment.get("/apartments/{apartment_id}")
async def get_apartment(apartment_id: int,
                        session: AsyncSession = Depends(get_async_session)
                        ):
    try:
        select_apartment = select(Apartment).where(
            Apartment.id == apartment_id)
        result = await session.execute(select_apartment)
        row = result.fetchone()
        if row:
            return row[0]
        else:
            raise HTTPException(status_code=404, detail="Apartment not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.get("/apartments", response_model=List[ApartmentModel])
async def get_all_apartments(session=Depends(get_async_session)):
    try:
        stmt = select(Apartment)
        result = await session.execute(stmt)
        rows = result.scalars().all()
        apartments = [ApartmentModel.from_orm(row) for row in rows]
        return apartments
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.get("/addresses/{address_id}")
async def get_address(address_id: int,
                      session: AsyncSession = Depends(get_async_session)
                      ):
    try:
        select_address = select(Address).where(Address.id == address_id)
        result = await session.execute(select_address)
        row = result.fetchone()
        if row:
            return row[0]
        else:
            raise HTTPException(status_code=404, detail="Address not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.get("/getGroups/{apartment_id}", response_model=List[GroupModel])
async def get_groups_for_apartment(apartment_id: int,
                                   session: AsyncSession = Depends(get_async_session)
                                   ):
    try:
        select_groups = select(Group).where(Group.apartment_id == apartment_id).filter()
        result = await session.execute(select_groups)
        rows = result.scalars().all()
        groups = [GroupModel.from_orm(row) for row in rows]
        return groups
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


# UPDATE
@router_apartment.put("/apartments/{apartment_id}")
async def update_apartment(apartment_id: int,
                           apartment_data: ApartmentCreate,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        update_apartment = update(Apartment).where(
            Apartment.id == apartment_id).values(**apartment_data.dict())
        result = await session.execute(update_apartment)
        await session.commit()
        if result.rowcount:
            return {"message": "Apartment updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Apartment not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.put("/addresses/{address_id}")
async def update_address(address_id: int, address_data: ApartmentCreate,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        update_address = update(Address).where(
            Address.id == address_id
            ).values(**address_data.dict())
        result = await session.execute(update_address)
        await session.commit()
        if result.rowcount:
            return {"message": "Address updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Address not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# DELETE
@router_apartment.delete("/apartments/{apartment_id}")
async def delete_apartment(apartment_id: int,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        delete_apartment = delete(Apartment).where(
            Apartment.id == apartment_id
            )
        result = await session.execute(delete_apartment)
        await session.commit()
        if result.rowcount:
            return {"message": "Apartment deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Apartment not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.delete("/addresses/{address_id}")
async def delete_address(address_id: int,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        delete_address = delete(Address).where(Address.id == address_id)
        result = await session.execute(delete_address)
        await session.commit()
        if result.rowcount:
            return {"message": "Address deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Address not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
