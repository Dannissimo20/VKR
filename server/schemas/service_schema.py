from pydantic import BaseModel


class ServiceAddRequest(BaseModel):
    name: str
    duration: int


class ServicesForOrder(BaseModel):
    service_id: str
