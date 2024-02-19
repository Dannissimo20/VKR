from typing import List

from pydantic import BaseModel

from schemas.client_schema import ClientSchema


class CarSchema(BaseModel):
    vin: str
    marka: str
    model: str
    color: str
    license_plate: str
    body: str
    yob: int
    engine: str = 'volume/horsepower/fuel_type'
    drive: str = 'front/rear/all'
    transmission: str = 'auto/manual'


class CarAddRequest(CarSchema):
    client: str


class CarGetSchema(CarSchema):
    client: ClientSchema


class CarGetAllSchema(BaseModel):
    cars: List[CarGetSchema]


class CarAddResponse(BaseModel):
    status: int
    message: str
