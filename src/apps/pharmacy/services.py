from apps.commons.service import ServiceBase
from apps.pharmacy.schemas import PharmacyCreate, PharmacyFilter
from db.models.company import Company


class ServicePharmacy(ServiceBase):
    MODEL = Company

    # переопределить метод create -> созд компании тип проставить
    async def create(self, data: PharmacyCreate) -> Company:
        return await self.create(data)

    # переопределить select -> выбирал только аптеки
    async def select(self, data: PharmacyFilter) -> Company:
        return await self.create(data)
