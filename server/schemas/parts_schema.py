from pydantic import BaseModel


class PartsAddRequest(BaseModel):
    name: str
    description: str
    price: float
    count: int
    unit: str
