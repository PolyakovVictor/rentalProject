from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert, select, update, delete

from schemas import GroupUserCreate
from database import get_async_session
from models import Group, GroupUser

router_group = APIRouter(
    prefix="/Group",
    tags=["Group"]
)

@router_group.post("/groups")
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


@router_group.post("/groupUsers")
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


# READ
@router_group.get("/groups/{group_id}")
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


@router_group.get("/groupUsers")
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


# UPDATE
@router_group.put("/groups/{group_id}")
async def update_group(group_id: int,
                       group_data: dict,
                       session: AsyncSession = Depends(get_async_session)
                       ):
    try:
        update_group = update(Group).where(
            Group.id == group_id).values(**group_data)
        result = await session.execute(update_group)
        await session.commit()
        if result.rowcount:
            return {"message": "Group updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Group not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router_group.put("/groupUsers/{group_id}/{user_id}")
async def update_group_user(group_id: int,
                            user_id: int,
                            group_user_data: dict,
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        update_group_user = update(GroupUser).where(
            GroupUser.group_id == group_id,
            GroupUser.user_id == user_id
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


# DELETE
@router_group.delete("/groups/{group_id}")
async def delete_group(group_id: int,
                       session: AsyncSession = Depends(get_async_session)
                       ):
    try:
        delete_group = delete(Group).where(Group.id == group_id)
        result = await session.execute(delete_group)
        await session.commit()
        if result.rowcount:
            return {"message": "Group deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Group not found")
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router_group.delete("/groupUsers/{group_id}/{user_id}")
async def delete_group_user(group_id: int,
                            user_id: int,
                            session: AsyncSession = Depends(get_async_session)
                            ):
    try:
        delete_group_user = delete(GroupUser).where(
            GroupUser.group_id == group_id,
            GroupUser.user_id == user_id
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
