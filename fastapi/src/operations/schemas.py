from pydantic import BaseModel


class ApartmentCreate(BaseModel):
    id: int
    user_id: int
    title: str
    price: str
    description: str
    group_id: int


class AddressCreate(BaseModel):
    id: int
    country: str
    city: str
    address: str
    zip_code: str
    apartment_id: int
