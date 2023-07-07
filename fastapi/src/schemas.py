from pydantic import BaseModel


class ApartmentCreate(BaseModel):
    user_id: int
    title: str
    price: str
    description: str
    type: str
    room_count: int
    group_id: int

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
    group_id: int

    class Config(BaseModel):
        orm_mode = True


class AddressModel(BaseModel):
    id: int
    country: str
    city: str
    address: str
    zip_code: str
    apartment_id: int

    class Config(BaseModel):
        orm_mode = True
