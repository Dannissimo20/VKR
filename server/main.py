from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated

from database.database import SessionLocal
from repository import client_repo, car_repo, lifter_repo
from schemas.add_response import AddResponse
from schemas.car_schema import CarAddRequest, CarGetAllSchema
from schemas.client_schema import ClientAddRequest, ClientGetAllSchema
from schemas.lifter_schema import LifterAddRequest, LifterSchema, LiftersGetAllSchema

from jwt import get_current_active_user, User, Token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, \
    create_access_token

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


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.login}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.post("/client/add",
          response_model=AddResponse,
          tags=["Клиенты"],
          summary="Добавление клиента в базу")
async def add_client(client: ClientAddRequest, db: Session = Depends(get_db)):
    res = client_repo.add(db, client)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.get('/client/get_all',
         response_model=ClientGetAllSchema,
         tags=['Клиенты'],
         summary='Получение всех клиентов')
async def get_all_clients(current_user: Annotated[User, Depends(get_current_active_user)],
                          db: Session = Depends(get_db)):
    if current_user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": "Bearer"},
        )
    clients = client_repo.get_all(db)
    return ClientGetAllSchema(clients=clients)


@app.get('/car/get_all',
         response_model=CarGetAllSchema,
         tags=['Автомобили'],
         summary='Получение всех автомобилей')
async def get_all_cars(db: Session = Depends(get_db)):
    cars = car_repo.get_all(db)
    return CarGetAllSchema(cars=cars)


@app.get('/car/get_all_for_client',
         response_model=CarGetAllSchema,
         tags=['Автомобили'],
         summary="Получение всех автомобилей для одного клиента")
async def get_all_cars(client_id: str, db: Session = Depends(get_db)):
    cars = car_repo.get_all_for_client(db, client_id)
    return CarGetAllSchema(cars=cars)


@app.post('/car/add',
          response_model=AddResponse,
          tags=['Автомобили'],
          summary='Добавление автомобиля в базу')
async def add_car(car: CarAddRequest, db: Session = Depends(get_db)):
    res = car_repo.add(db, car)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.post('/lifter/add',
          response_model=AddResponse,
          tags=['Подъемники'],
          summary='Добавление подъемника в базу')
async def add_lifter(lifter: LifterAddRequest, db: Session = Depends(get_db)):
    res = lifter_repo.add(lifter, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.get('/lifter/get_all',
         response_model=LiftersGetAllSchema,
         tags=['Подъемники'],
         summary='Получение всех подъемников')
async def get_all_lifters(db: Session = Depends(get_db)):
    lifters = lifter_repo.get_all(db)
    return LiftersGetAllSchema(lifters=lifters)


@app.get('/lifter/get_by_id',
         response_model=LifterSchema,
         tags=['Подъемники'],
         summary='Получение подъемника по имени')
async def get_lifter_by_id(lifter_id: str, db: Session = Depends(get_db)):
    lifter_repo.get_by_id(lifter_id, db)
