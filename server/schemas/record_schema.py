from pydantic import BaseModel


class RecordAddRequest(BaseModel):
    confirmation: int = 0
    date: str
    client_fio: str
    client_phone: str
