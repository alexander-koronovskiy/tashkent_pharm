from database import Base
from commons import MixinMarkChanges, Column, Integer, String, CompanyType, Tinyint

class Company(Base, MixinMarkChanges):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    title =  Column(String(50))
    type =  Column(Tinyint(50))
 