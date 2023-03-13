from database import Base
from commons import MixinMarkChanges, Column, Integer, String

class Arcticle(Base, MixinMarkChanges):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)

    type =  Column(String(50))
    description =  Column(String(50))
