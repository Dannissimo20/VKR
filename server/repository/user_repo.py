from sqlalchemy.orm import Session

from models.user_model import User
from schemas.user_schema import CreateUserSchema, UserSchema


def create_user(session: Session, user: CreateUserSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
    # return UserSchema(
    #     id=str(db_user.id),
    #     login=db_user.login,
    #     role=db_user.role,
    #     fio=db_user.fio
    # )


def get_user(session: Session, login: str):
    return session.query(User).filter(User.login == login).one()
