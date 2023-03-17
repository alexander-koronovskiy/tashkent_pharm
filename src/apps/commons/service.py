from pydantic import BaseModel
from sqlalchemy import select, Select
from typing import Any, Type, List

from apps.commons.manager import ManagerBase
from db.database import Base


class ServiceBase:

    MODEL: Type[Base] = None

    def __init__(self, manager: ManagerBase):
        self.manager = manager

    def select(self, *selects) -> Select[Any]:
        if not selects:
            selects = self.MODEL,
        return select(*selects).where(self.MODEL.is_deleted.is_(False))

    async def create(self, data: BaseModel) -> MODEL:
        instance = self.MODEL(**data.dict(exclude_unset=True))
        return await self.manager.create(instance)

    async def get(self, id_instance: int) -> MODEL:
        query = self.select().where(self.MODEL.id == id_instance)
        result = await self.manager.execute(query)
        return result.scalars().first()

    async def update(self, id_instance: int, data: dict):
        instance = self.get(id_instance)
        return await self.manager.update(instance, data)

    async def list(self, model_filter: BaseModel) -> List[MODEL]:
        query = self.select()
        for attr, value in model_filter.dict(exclude_unset=True).items():
            query = query.where(getattr(self.MODEL, attr) == value)
        result = await self.manager.execute(query)
        return result.scalars().all()

    async def delete_completely(self, id_instance: int) -> MODEL:
        instance = self.get(id_instance)
        return await self.manager.delete(instance)

    async def delete(self, id_instance: int) -> MODEL:
        instance = self.get(id_instance)
        return await self.manager.update(instance, {self.MODEL.is_deleted: True})
