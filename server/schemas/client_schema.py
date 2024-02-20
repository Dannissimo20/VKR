from datetime import datetime
from typing import List

from pydantic import BaseModel

from schemas.car_schema import CarSchema


class ClientSchema(BaseModel):
    name: str
    dob: datetime
    cars: List[CarSchema]


class ClientAddSchema(BaseModel):
    name: str
    dob: str = "1970-01-01"


class ClientAddResponse(BaseModel):
    status: int
    message: str


class ClientGetAllSchema(BaseModel):
    clients: List[ClientSchema]
