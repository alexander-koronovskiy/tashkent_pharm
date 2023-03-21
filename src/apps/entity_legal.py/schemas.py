from pydantic import BaseModel, constr


class UserCreate(BaseModel):
   pass


class UserUpdate(BaseModel):
    pass


class UserFilter(BaseModel):
    pass


class UserShort(BaseModel):
    pass


class UserDetailed(BaseModel):
    pass

    class Config:
        orm_mode = True


# при фильтрации все поля опциональны

