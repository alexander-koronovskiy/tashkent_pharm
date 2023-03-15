from db.database import Base
from db.models.commons import MixinMarkChanges
from sqlalchemy import Column, Integer, String, SmallInteger


class Company(Base, MixinMarkChanges):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    title = Column(String(50))
    type = Column(SmallInteger)
 