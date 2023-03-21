from apps.commons.service import ServiceBase
from db.models.company import Company


class ServicePharmacy(ServiceBase):
    MODEL = Company

    # переопределить метод create -> созд компании тип проставить
    # переопределить select -> выбирал только аптеки
