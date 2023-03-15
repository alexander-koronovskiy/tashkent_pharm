from db.database import Base
from db.models.commons import MixinMarkChanges
from sqlalchemy import Column, Integer, String


class Arcticle(Base, MixinMarkChanges):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)

    type = Column(String(50))
    description = Column(String(255))
