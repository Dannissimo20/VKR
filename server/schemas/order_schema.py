from typing import List

from pydantic import BaseModel

from schemas.parts_schema import PartsForOrder
from schemas.service_schema import ServicesForOrder


class OrderAddRequest(BaseModel):
    worker: str
    lifter: str
    problem_description: str
    recommendation_description: str


class OrderAddWorkerRequest(BaseModel):
    order_id: str
    worker_id: str


class OrderAddPartsRequest(BaseModel):
    order_id: str
    parts: List[PartsForOrder]


class OrderAddServicesRequest(BaseModel):
    order_id: str
    services: List[ServicesForOrder]
