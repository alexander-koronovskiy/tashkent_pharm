from database import Base
from commons import MixinMarkChanges

class Arcticle(Base, MixinMarkChanges):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    
