from typing import Optional
from datetime import date

from pydantic import BaseModel, conint


class ApartmentCreate(BaseModel):
    user_id: int
    title: str
    price: str
    description: str
    type: str
    room_count: int

    class Config(BaseModel):
        orm_mode = True


class AddressCreate(BaseModel):
    country: str
    city: str
    address: str
    zip_code: str
    apartment_id: int

    class Config(BaseModel):
        orm_mode = True


class GroupCreate(BaseModel):
    settlers_limit: conint(gt=0)
    title: str
    description: str
    apartment_id: Optional[int] = None
    start_of_lease: Optional[date] = None
    end_of_lease: Optional[date] = None

    class Config:
        orm_mode = True


class GroupUserCreate(BaseModel):
    user_id: int
    group_id: int

    class Config(BaseModel):
        orm_mode = True


class ApartmentModel(BaseModel):
    id: int
    user_id: int
    title: str
    price: str
    description: str
    type: str
    room_count: int

    class Config:
        orm_mode = True


class GroupModel(BaseModel):
    id: int
    apartment_id: int
    start_of_lease: date
    end_of_lease: date
    settlers_limit: int
    description: str
    title: str

    class Config:
        orm_mode = True
