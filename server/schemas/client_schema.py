from datetime import datetime

from pydantic import BaseModel


class AddSchema(BaseModel):
    name: str
    DoB: datetime


class AddResponse(BaseModel):
    status: int
    message: str
