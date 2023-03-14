from database import Base
from commons import MixinMarkChanges
from sqlalchemy import Column, Integer, String, Text


class Arcticle(Base, MixinMarkChanges):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)

    type =  Column(String(50))
    description = Column(Text(500))
