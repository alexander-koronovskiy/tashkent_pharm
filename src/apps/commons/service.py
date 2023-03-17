from sqlalchemy import select, Select
import pydantic
from typing import Any, Type, List

from apps.commons.manager import ManagerBase
from db.database import Base
import asyncio


class ServiceBase:

    MODEL: Type[Base] = None

    def __init__(self, manager: ManagerBase):
        self.manager = manager

    def select(self, *selects) -> Select[Any]:
        if not selects:
            selects = self.MODEL,
        return select(*selects).where(self.MODEL.is_deleted.is_(False))

    async def create(self, data: pydantic.BaseModel) -> MODEL:
        instance = self.MODEL(data.dict(exclude_unset=True))
        return await self.manager.create(instance)

    async def get(self, id_instance: int) -> MODEL:
        instance = self.select().where(self.MODEL.id == id_instance)
        return await self.manager.execute(instance)

    async def update(self, id_instance: int, data: dict):
        instance = self.get(id_instance)
        return await self.manager.update(instance, data)

    async def list(self, model_filter: pydantic) -> List[MODEL]:
        instances = self.select().where(model_filter)
        return await self.manager.execute(instances)


    async def delete_completely(self, instance: ) -> MODEL:
        instance = self.get(instance)
        return await self.manager.delete(instance)

    async def delete(self, id_instance: int) -> MODEL:
        instance = self.get(id_instance)
        return await self.manager.update(instance, {self.MODEL.is_deleted: True})
