from typing import List

from pydantic import BaseModel

from schemas.car_schema import CarSchema


class ClientSchema(BaseModel):
    fio: str
    dob: str
    phone: str = "71234567890"
    email: str
    cars: List[CarSchema]


class ClientAddRequest(BaseModel):
    fio: str
    phone: str = "71234567890"
    dob: str
    email: str


class ClientGetAllSchema(BaseModel):
    clients: List[ClientSchema]
