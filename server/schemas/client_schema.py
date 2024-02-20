from datetime import datetime
from typing import List

from pydantic import BaseModel


class ClientSchema(BaseModel):
    name: str
    dob: datetime


class ClientAddSchema(BaseModel):
    name: str
    dob: str = "1970-01-01"


class ClientAddResponse(BaseModel):
    status: int
    message: str


