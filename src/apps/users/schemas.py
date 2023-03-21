from pydantic import BaseModel, constr


class UserCreate(BaseModel):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserUpdate(BaseModel):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserFilter(BaseModel):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserShort(BaseModel):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int


class UserDetailed(BaseModel):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int

    class Config:
        orm_mode = True


# при фильтрации все поля опциональны
