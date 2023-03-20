from pydantic import BaseModel, constr


class UserCreate(BaseModel):
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int

# class UserUpdate
# class UserFilter
# class UserShort


class UserDetailed:
    name_first: constr(max_length=50)
    name_middle: constr(max_length=50)
    name_last: constr(max_length=50)

    id_company: int

    class Config:
        orm_mode = True


# при фильтрации все поля опциональны
