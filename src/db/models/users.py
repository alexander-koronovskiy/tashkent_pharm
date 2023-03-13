from database import Base
from commons import MixinMarkChanges

class User(Base, MixinMarkChanges):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    
    name_first =  Column(String(50))
    name_middle =  Column(String(50))
    name_last =  Column(String(50))
    # id_company
