from pydantic import BaseModel, constr, conint


class EntityLegalCreate(BaseModel):
    name_legal: constr(max_length=50)
    tin: conint(gt=16, lt=32)   # 16 ИНН; 24 (до 32 для рассчетного счета)
    name_bank: constr(max_length=50)

    account: constr(max_length=50)
    email: constr(max_length=50)
    phone: constr(max_length=50)

    country: constr(max_length=50)
    city: constr(max_length=50)
    street: constr(max_length=50)
    unit: constr(max_length=50)
    apartment: constr(max_length=50)


class EntityLegalUpdate(BaseModel):
    name_legal: constr(max_length=50)
    tin: conint(gt=16, lt=32)   # 16 ИНН; 24 (до 32 для рассчетного счета)
    name_bank: constr(max_length=50)

    account: constr(max_length=50)
    email: constr(max_length=50)
    phone: constr(max_length=50)

    country: constr(max_length=50)
    city: constr(max_length=50)
    street: constr(max_length=50)
    unit: constr(max_length=50)
    apartment: constr(max_length=50)


class EntityLegalFilter(BaseModel):
    name_legal: constr(max_length=50)
    tin: conint(gt=16, lt=32)   # 16 ИНН; 24 (до 32 для рассчетного счета)
    name_bank: constr(max_length=50)

    account: constr(max_length=50)
    email: constr(max_length=50)
    phone: constr(max_length=50)

    country: constr(max_length=50)
    city: constr(max_length=50)
    street: constr(max_length=50)
    unit: constr(max_length=50)
    apartment: constr(max_length=50)


class EntityLegalShort(BaseModel):
    name_legal: constr(max_length=50)
    tin: conint(gt=16, lt=32)   # 16 ИНН; 24 (до 32 для рассчетного счета)
    name_bank: constr(max_length=50)

    account: constr(max_length=50)
    email: constr(max_length=50)
    phone: constr(max_length=50)

    country: constr(max_length=50)
    city: constr(max_length=50)
    street: constr(max_length=50)
    unit: constr(max_length=50)
    apartment: constr(max_length=50)


class EntityLegalDetailed(BaseModel):
    name_legal: constr(max_length=50)
    tin: conint(gt=16, lt=32)   # 16 ИНН; 24 (до 32 для рассчетного счета)
    name_bank: constr(max_length=50)

    account: constr(max_length=50)
    email: constr(max_length=50)
    phone: constr(max_length=50)

    country: constr(max_length=50)
    city: constr(max_length=50)
    street: constr(max_length=50)
    unit: constr(max_length=50)
    apartment: constr(max_length=50)

    class Config:
        orm_mode: True
