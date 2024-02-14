from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database.database import SessionLocal
from repository import client_repo
from schemas.client_schema import AddSchema, AddResponse

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/client/add",
          response_model=AddResponse,
          tags=["Клиенты"],
          summary="Добавление клиента в базу")
async def add_client(client: AddSchema, db: Session = Depends(get_db)):
    res = client_repo.add(db, client)
    if res == 'ok':
        return {'status': 200, 'message': 'ok'}
    if res == 'name error':
        return {'status': 400, 'message': 'check name format'}
    else:
        return {'status': 500, 'message': 'internal server error'}
