from typing import List

from pydantic import BaseModel


class LifterAddRequest(BaseModel):
    name: str
    description: str
    purpose: str


class LifterSchema(BaseModel):
    name: str
    description: str
    purpose: str


class LiftersGetAllSchema(BaseModel):
    lifters: List[LifterSchema]
