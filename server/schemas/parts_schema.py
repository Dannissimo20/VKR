from typing import List

from pydantic import BaseModel


class PartsAddRequest(BaseModel):
    name: str
    description: str
    price: float
    count: int
    unit: str


class PartsSchema(BaseModel):
    id: str
    name: str
    description: str
    price: float
    count: int
    unit: str


class PartsGetAllSchema(BaseModel):
    parts: List[PartsSchema]


class PartsUpdateCountRequest(BaseModel):
    part_id: str
    count: int


class PartsUpdatePriceRequest(BaseModel):
    part_id: str
    price: float
