from datetime import datetime
from typing import List

from pydantic import BaseModel

from schemas.car_schema import CarSchema


class ClientSchema(BaseModel):
    fio: str
    phone: str = "71234567890"
    cars: List[CarSchema]


class ClientAddRequest(BaseModel):
    fio: str
    phone: str = "71234567890"


class ClientGetAllSchema(BaseModel):
    clients: List[ClientSchema]
