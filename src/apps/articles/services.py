from apps.commons.service import ServiceBase
from db.models.users import User
from db.models.entity_legal import EntityLegal
from db.models.arcticles import Arcticle
from db.models.company import Company


class ServiceArticle(ServiceBase):
    MODEL = Arcticle
