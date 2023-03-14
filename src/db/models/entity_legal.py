from database import Base
from commons import MixinMarkChanges
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from company import Company


class EntityLegal(Base, MixinMarkChanges):
    __tablename__ = 'entities_legal'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name_legal = Column(String(50))
    tin = Column(Integer)   # 16 ИНН; 24 (до 32 для рассчетного счета)
    name_bank = Column(String(50))

    account = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))

    country = Column(String(50))
    city = Column(String(50))
    street = Column(String(50))
    unit = Column(String(50))
    apartament = Column(String(50))

    companies = relationship(
        Company,
        secondary = 'entities_legal_to_companies',
        backref = 'entities_legal',
        lazy='subquery', # todo: change that param
        secondaryjoin = 'and_(EntityLegalToCompany.id_company == Company.id, Company.is_deleted = False)'
    )


class EntityLegalToCompany(Base, MixinMarkChanges):
    __tablename__ = 'entities_legal_to_companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_company = Column(Integer, ForeignKey('companies.id'), nullable=False)
    id_entity_legal = Column(Integer, ForeignKey('entities.id'), nullable=False)
