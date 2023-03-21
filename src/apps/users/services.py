from apps.commons.service import ServiceBase
from db.models.users import User
from db.models.entity_legal import EntityLegal
from db.models.arcticles import Arcticle


class ServiceUser(ServiceBase):
    MODEL = User


class ServiceArticle(ServiceBase):
    MODEL = Arcticle


class ServiceEntityLegal(ServiceBase):
    MODEL = EntityLegal


class ServicePharmacy(ServiceBase):
    MODEL = Pharmacy
