from database import Base
from commons import MixinMarkChanges
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from company import Company


class EntityLegal(Base, MixinMarkChanges):
    __tablename__ = 'entities_legal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # todo: add method and shows

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
