from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from rental.models import Group, Apartment, Address, GroupUser
from rental.schemas import ApartmentCreate, AddressCreate, GroupUserCreate

routerGroup = APIRouter(
    prefix="/Group",
    tags=["Group"]
)

routerApartment = APIRouter(
    prefix="/Apartment",
    tags=["Apartment"]
)


@routerGroup.post("/groups")
async def create_group(group_data: dict,
                       session: AsyncSession = Depends(get_async_session)
                       ):
    try:
        new_group = insert(Group).values(**group_data)
        result = await session.execute(new_group)
        await session.commit()
        return {"id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerGroup.post("/groupUsers")
async def create_group_user(group_user_data: GroupUserCreate,
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        new_group_user = insert(GroupUser).values(**group_user_data.dict())
        result = await session.execute(new_group_user)
        await session.commit()
        return {"id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerApartment.post("/apartments")
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


@routerApartment.post("/addresses")
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
@routerGroup.get("/groups/{group_id}")
async def get_group(group_id: int,
                    session: AsyncSession = Depends(get_async_session)
                    ):
    try:
        select_group = select(Group).where(Group.id == group_id)
        result = await session.execute(select_group)
        row = result.fetchone()
        if row:
            return row[0]
        else:
            raise HTTPException(status_code=404, detail="Group not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@routerGroup.get("/groupUsers")
async def get_all_group_user(
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        select_group_user = select(GroupUser)
        result = await session.execute(select_group_user)
        row = result.fetchone()
        if row:
            return row[0]
        else:
            raise HTTPException(status_code=404, detail="GroupUser not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@routerApartment.get("/apartments/{apartment_id}")
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


@routerApartment.get("/apartments")
async def get_all_apartment(
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        select_apartment = select(Apartment)
        result = await session.execute(select_apartment)
        row = result.fetchone()
        if row:
            return row[0]
        else:
            raise HTTPException(status_code=404, detail="Apartment not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@routerApartment.get("/addresses/{address_id}")
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


# UPDATE
@routerGroup.put("/groups/{group_id}")
async def update_group(group_id: int,
                       group_data: dict,
                       session: AsyncSession = Depends(get_async_session)
                       ):
    try:
        update_group = update(Group).where(
            Group.c.id == group_id).values(**group_data)
        result = await session.execute(update_group)
        await session.commit()
        if result.rowcount:
            return {"message": "Group updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Group not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerGroup.put("/groupUsers/{group_id}/{user_id}")
async def update_group_user(group_id: int,
                            user_id: int,
                            group_user_data: dict,
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        update_group_user = update(GroupUser).where(
            GroupUser.c.group_id == group_id,
            GroupUser.c.user_id == user_id
        ).values(**group_user_data)
        result = await session.execute(update_group_user)
        await session.commit()
        if result.rowcount:
            return {"message": "GroupUser updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="GroupUser not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerApartment.put("/apartments/{apartment_id}")
async def update_apartment(apartment_id: int,
                           apartment_data: ApartmentCreate,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        update_apartment = update(Apartment).where(
            Apartment.c.id == apartment_id).values(**apartment_data.dict())
        result = await session.execute(update_apartment)
        await session.commit()
        if result.rowcount:
            return {"message": "Apartment updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Apartment not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerApartment.put("/addresses/{address_id}")
async def update_address(address_id: int, address_data: ApartmentCreate,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        update_address = update(Address).where(
            Address.c.id == address_id
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
@routerGroup.delete("/groups/{group_id}")
async def delete_group(group_id: int,
                       session: AsyncSession = Depends(get_async_session)
                       ):
    try:
        delete_group = delete(Group).where(Group.c.id == group_id)
        result = await session.execute(delete_group)
        await session.commit()
        if result.rowcount:
            return {"message": "Group deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Group not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerGroup.delete("/groupUsers/{group_id}/{user_id}")
async def delete_group_user(group_id: int,
                            user_id: int,
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        delete_group_user = delete(GroupUser).where(
            GroupUser.c.group_id == group_id,
            GroupUser.c.user_id == user_id
        )
        result = await session.execute(delete_group_user)
        await session.commit()
        if result.rowcount:
            return {"message": "GroupUser deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="GroupUser not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@routerApartment.delete("/apartments/{apartment_id}")
async def delete_apartment(apartment_id: int,
                           session: AsyncSession = Depends(get_async_session)
                           ):
    try:
        delete_apartment = delete(Apartment).where(
            Apartment.c.id == apartment_id
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


@routerApartment.delete("/addresses/{address_id}")
async def delete_address(address_id: int,
                         session: AsyncSession = Depends(get_async_session)
                         ):
    try:
        delete_address = delete(Address).where(Address.c.id == address_id)
        result = await session.execute(delete_address)
        await session.commit()
        if result.rowcount:
            return {"message": "Address deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Address not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
