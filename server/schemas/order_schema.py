from pydantic import BaseModel


class OrderAddRequest(BaseModel):
    worker: str
    lifter: str
    problem_description: str
    recommendation_description: str
