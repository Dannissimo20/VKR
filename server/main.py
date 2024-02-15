from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database.database import SessionLocal
from repository import client_repo, car_repo
from schemas.car_schema import CarAddResponse, CarAddRequest
from schemas.client_schema import ClientAddSchema, ClientAddResponse

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
          response_model=ClientAddResponse,
          tags=["Клиенты"],
          summary="Добавление клиента в базу")
async def add_client(client: ClientAddSchema, db: Session = Depends(get_db)):
    res = client_repo.add(db, client)
    if res == 'ok':
        return {'status': 200, 'message': 'ok'}
    if res == 'name error':
        return {'status': 400, 'message': 'check name format'}
    else:
        return {'status': 500, 'message': 'internal server error'}


@app.post('/car/add',
          response_model=CarAddResponse,
          tags=['Автомобили'],
          summary='Добавление автомобиля в базу')
async def add_car(car: CarAddRequest, db: Session = Depends(get_db)):
    res = car_repo.add(db, car)
    if res == 'ok':
        return CarAddResponse(status=200, message=res)
    else:
        return CarAddResponse(status=400, message=res)
