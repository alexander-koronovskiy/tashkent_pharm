from apps.commons.service import ServiceBase
from db.models.users import User


class ServiceUser(ServiceBase):
    MODEL = User

