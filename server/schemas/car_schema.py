from pydantic import BaseModel


class CarAddRequest(BaseModel):
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
    client: str


class CarAddResponse(BaseModel):
    status: int
    message: str
