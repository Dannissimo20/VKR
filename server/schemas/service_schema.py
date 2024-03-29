from pydantic import BaseModel


class ServiceAddRequest(BaseModel):
    name: str
    duration: int
