from typing import Dict

import jwt
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from config import SECRET_KEY, ALGORITHM
from database.database import SessionLocal
from models.user_model import User
from repository import client_repo, car_repo, lifter_repo, parts_repo, service_repo, order_repo, record_repo, user_repo
from schemas.add_response import AddResponse
from schemas.car_schema import CarAddRequest, CarGetAllSchema
from schemas.client_schema import ClientAddRequest, ClientGetAllSchema
from schemas.lifter_schema import LifterAddRequest, LifterSchema, LiftersGetAllSchema
from schemas.order_schema import OrderAddRequest
from schemas.record_schema import RecordAddRequest
from schemas.service_schema import ServiceAddRequest
from schemas.parts_schema import PartsAddRequest, PartsGetAllSchema, PartsSchema, PartsUpdateCountRequest, \
    PartsUpdatePriceRequest
from schemas.user_schema import UserSchema, CreateUserSchema

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/login',
          response_model=Dict,
          tags=['Пользователи'],
          summary="Авторизация пользователя")
def login(
        payload: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)):
    try:
        user: User = user_repo.get_user(
            session=session, login=payload.username
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    is_validated: bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    return user.generate_token()


@app.post('/signup',
          response_model=UserSchema,
          tags=['Пользователи'],
          summary="Регистрация нового пользователя")
def signup(
    payload: CreateUserSchema,
    session: Session = Depends(get_db)
):
    """Processes request to register user account."""
    payload.password = User.hash_password(payload.password)
    return user_repo.create_user(session, user=payload)


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
async def get_all_clients(db: Session = Depends(get_db),
                          token: str = Depends(oauth2_scheme)):
    if jwt.decode(token, SECRET_KEY, ALGORITHM)['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Not enough permissions")
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
    return lifter_repo.get_by_id(lifter_id, db)


@app.post('/parts/add',
          response_model=AddResponse,
          tags=['Запчасти'],
          summary='Добавление запчасти в базу')
async def add_parts(parts: PartsAddRequest, db: Session = Depends(get_db)):
    res = parts_repo.add(parts, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.get('/parts/get_all',
         response_model=PartsGetAllSchema,
         tags=['Запчасти'],
         summary='Получение всех запчастей')
async def get_all_parts(db: Session = Depends(get_db)):
    parts = parts_repo.get_all(db)
    return PartsGetAllSchema(parts=parts)


@app.get('/parts/get_by_id',
         response_model=PartsSchema,
         tags=['Запчасти'],
         summary='Получение запчасти по имени')
async def get_parts_by_id(parts_id: str, db: Session = Depends(get_db)):
    return parts_repo.get_by_id(parts_id, db)


@app.put('/parts/update_count',
         response_model=AddResponse,
         tags=['Запчасти'],
         summary='Изменение количества запчастей на складе')
async def update_parts_count(req: PartsUpdateCountRequest, db: Session = Depends(get_db)):
    res = parts_repo.update_for_count(req.part_id, req.count, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.put('/parts/update_price',
         response_model=AddResponse,
         tags=['Запчасти'],
         summary='Изменение цены запчастей')
async def update_parts_price(req: PartsUpdatePriceRequest, db: Session = Depends(get_db)):
    res = parts_repo.update_for_price(req.part_id, req.price, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.post('/service/add',
          response_model=AddResponse,
          tags=['Услуги'],
          summary='Добавление услуги в базу')
async def add_service(service: ServiceAddRequest, db: Session = Depends(get_db)):
    res = service_repo.add(service, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.post('/order/add',
          response_model=AddResponse,
          tags=['Заказы'],
          summary='Добавление заказа в базу')
async def add_order(order: OrderAddRequest, db: Session = Depends(get_db)):
    res = order_repo.add(order, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)


@app.post('/record/add',
          response_model=AddResponse,
          tags=['Записи'],
          summary='Добавление записи в базу')
async def add_record(record: RecordAddRequest, db: Session = Depends(get_db)):
    res = record_repo.add(record, db)
    if res == 'ok':
        return AddResponse(status=200, message=res)
    else:
        return AddResponse(status=400, message=res)
