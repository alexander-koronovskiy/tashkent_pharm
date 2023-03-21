from pydantic import BaseModel, constr
from apps.commons.schemas import MixinMarkChanges


class PharmacyCreate(BaseModel, MixinMarkChanges):
    title: constr(max_length=50)
    

class PharmacyUpdate(BaseModel, MixinMarkChanges):
    title: constr(max_length=50)


class PharmacyFilter(BaseModel, MixinMarkChanges):
    title: constr(max_length=50)


class PharmacyShort(BaseModel, MixinMarkChanges):
    title: constr(max_length=50)
    

class PharmacyDetailed(BaseModel, MixinMarkChanges):
    title: constr(max_length=50)

    class Config:
        orm_mode: True
