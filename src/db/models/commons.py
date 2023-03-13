from sqlalchemy import Column, DateTime, Boolean, String, Integer
from sqlalchemy.sql import func


class MixinMarkChanges:
    created_at = Column(DateTime, server_default=func.now())
    updaded_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    created_by = Column(Integer)
    updated_by = Column(Integer)
    is_deleted = Column(Boolean, default=False)


class CompanyType(String):
    pass
