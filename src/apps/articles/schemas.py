from pydantic import BaseModel, constr


class ArcticleCreate(BaseModel):
    type = constr(max_length=50)
    description = constr(max_length=50)


class ArcticleUpdate(BaseModel):
    type = constr(max_length=50)
    description = constr(max_length=50)


class ArcticleFilter(BaseModel):
    type = constr(max_length=50)
    description = constr(max_length=50)


class ArcticleShort(BaseModel):
    type = constr(max_length=50)
    description = constr(max_length=50)


class ArcticleDetailed(BaseModel):
    type = constr(max_length=50)
    description = constr(max_length=50)

    class Config:
        orm_mode = True


# при фильтрации все поля опциональны

