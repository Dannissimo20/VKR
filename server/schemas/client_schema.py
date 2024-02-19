from datetime import datetime

from pydantic import BaseModel


class ClientAddSchema(BaseModel):
    name: str
    DoB: datetime


class ClientAddResponse(BaseModel):
    status: int
    message: str


class ClientSchema(BaseModel):
    name: str
    DoB: datetime
