from pydantic import BaseModel, constr
from apps.commons.schemas import MixinMarkChanges


class ArcticleCreate(BaseModel, MixinMarkChanges):
    type: constr(max_length=50)
    description: constr(max_length=50)


class ArcticleUpdate(BaseModel, MixinMarkChanges):
    type: constr(max_length=50)
    description: constr(max_length=50)


class ArcticleFilter(BaseModel, MixinMarkChanges):
    type: constr(max_length=50)
    description: constr(max_length=50)


class ArcticleShort(BaseModel, MixinMarkChanges):
    type: constr(max_length=50)
    description: constr(max_length=50)


class ArcticleDetailed(BaseModel, MixinMarkChanges):
    type: constr(max_length=50)
    description: constr(max_length=50)

    class Config:
        orm_mode: True


# при фильтрации все поля опциональны

