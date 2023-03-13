from database import Base
from commons import MixinMarkChanges

class Company(Base, MixinMarkChanges):
    __tablename__ = ''
    id = Column(Integer, primary_key=True)
 