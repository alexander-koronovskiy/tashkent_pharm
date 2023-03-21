from pydantic import BaseModel, constr


class PharmacyCreate(BaseModel):
    title: constr(max_length=50)
    

class PharmacyUpdate(BaseModel):
    title: constr(max_length=50)


class PharmacyFilter(BaseModel):
    title: constr(max_length=50)


class PharmacyShort(BaseModel):
    title: constr(max_length=50)
    

class PharmacyDetailed(BaseModel):
    title: constr(max_length=50)

    class Config:
        orm_mode: True
