from database import Base
from commons import MixinMarkChanges
from sqlalchemy import Column, Integer, String, Tinyint

class Company(Base, MixinMarkChanges):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    title =  Column(String(50))
    type =  Column(Tinyint(50))
 