from db.database import Base
from db.models.commons import MixinMarkChanges
from sqlalchemy import Column, Integer, String, ForeignKey
from db.models.company import Company


class User(Base, MixinMarkChanges):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name_first = Column(String(50))
    name_middle = Column(String(50))
    name_last = Column(String(50))

    id_company = Column(Integer, ForeignKey('companies.id'), nullable=False)
