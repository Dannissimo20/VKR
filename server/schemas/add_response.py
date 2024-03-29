from pydantic import BaseModel


class AddResponse(BaseModel):
    status: int
    message: str
