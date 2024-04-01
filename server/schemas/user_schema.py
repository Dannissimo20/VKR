from pydantic import BaseModel, UUID4


class UserBaseSchema(BaseModel):
    login: str
    fio: str
    role: str


class CreateUserSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: UUID4


class UserLoginSchema(BaseModel):
    login: str
    password: str
