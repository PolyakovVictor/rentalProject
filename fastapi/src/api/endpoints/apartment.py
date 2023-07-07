from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

from schemas import ApartmentCreate, AddressCreate, ApartmentModel, AddressModel, GroupModel
from database import get_async_session
from models import Apartment, Address
from crud import CRUD

router_apartment = APIRouter(
    prefix="/Apartment",
    tags=["Apartment"]
)


@router_apartment.post("/apartments", response_model=ApartmentModel)
async def create_apartment(apartment_data: ApartmentCreate,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        apartment = Apartment(**apartment_data.dict())
        return await CRUD(session).add(apartment)
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router_apartment.post("/addresses")
async def create_address(address_data: AddressCreate,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        address = Address(**address_data.dict())
        return await CRUD(session).add(address)
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# READ
@router_apartment.get("/apartments/{apartment_id}")
async def get_apartment(apartment_id: int,
                        session: AsyncSession = Depends(get_async_session)
                        ):
    try:
        return await CRUD(session).get_by_id(Apartment, apartment_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Apartment not Found")


@router_apartment.get("/apartments", response_model=List[ApartmentModel])
async def get_all_apartments(session: AsyncSession = Depends(get_async_session)):
    try:
        return await CRUD(session).get_all(Apartment)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Apartment not Found")


@router_apartment.get("/filter", response_model=List[ApartmentModel])
async def get_filter_apartments(max_price: str = '30',
                                title: str = 'title',
                                country: str = 'country',
                                city: str = 'city',
                                type: str = 'type',
                                room_count: int = 0,
                                session: AsyncSession = Depends(get_async_session),):
    try:
        return await CRUD(session).get_filter_apartments(Apartment, max_price=max_price, title=title, city=city, country=country, room_count=room_count, type=type)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Apartment not Found")


@router_apartment.get("/addresses", response_model=List[AddressModel])
async def get_all_address(session=Depends(get_async_session)):
    try:
        return await CRUD(session).get_all(Address)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Address not found")


@router_apartment.get("/addresses/{address_id}")
async def get_address(address_id: int,
                      session: AsyncSession = Depends(get_async_session)
                      ):
    try:
        return await CRUD(session).get_by_id(Address, address_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Apartment not Found")


@router_apartment.get("/getGroups/{apartment_id}", response_model=List[GroupModel])
async def get_groups_for_apartment(apartment_id: int,
                                   session: AsyncSession = Depends(get_async_session)
                                   ):
    try:
        result = await CRUD(session).get_groups_by_apartment_id(apartment_id)
        groups = [GroupModel.from_orm(item) for item in result]
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
        apartment = Apartment(apartment_id=apartment_id, **apartment_data().dict())
        await session.add(apartment)
        return await CRUD(session).add(apartment)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Apartment not Found")


@router_apartment.put("/addresses/{address_id}")
async def update_address(address_id: int, address_data: ApartmentCreate,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        address = await CRUD(session).get_by_id(Address, address_id)
        if address:
            address.id = address_data.id
            address.country = address_data.country
            address.city = address_data.city
            address.address = address_data.address
            address.zip_code = address_data.zip_code
            address.apartment_id = address_data.apartment_id
        else:
            raise HTTPException(status_code=404, detail="Address not found")
        return await CRUD(session).add(address)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Address not Found")


# DELETE
@router_apartment.delete("/apartments/{apartment_id}")
async def delete_apartment(apartment_id: int,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        apartment = await CRUD(session).get_by_id(Apartment, apartment_id)
        return await CRUD(session).delete(apartment)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Apartment not Found")


@router_apartment.delete("/addresses/{address_id}")
async def delete_address(address_id: int,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        address = await CRUD(session).get_by_id(Address, address_id)
        return await CRUD(session).delete(address)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Address not Found")
