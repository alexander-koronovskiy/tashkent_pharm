from pydantic import BaseModel, constr
from apps.commons.schemas import MixinMarkChanges


class UserCreate(BaseModel, MixinMarkChanges):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserUpdate(BaseModel, MixinMarkChanges):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserFilter(BaseModel, MixinMarkChanges):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserShort(BaseModel, MixinMarkChanges):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserDetailed(BaseModel, MixinMarkChanges):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int

    class Config:
        orm_mode: True


# при фильтрации все поля опциональны
