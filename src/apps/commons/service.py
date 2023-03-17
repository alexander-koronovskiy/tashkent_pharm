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

    async def get(self, model_id: str) -> MODEL:
        instance = self.select().where(self.MODEL.id == model_id)
        return await self.manager.execute(instance)

    async def list(self, model_filter: pydantic) -> List[MODEL]:
        model_list = []
        for condition in model_filter:
            instance = self.select().where(condition)
            model_list = await asyncio.gather(self.manager.execute(instance))
        return model_list

    async def update(self, model_id: str, data: dict):
        instance = self.get(model_id)
        return await self.manager.update(instance, data)

    async def delete_completely(self, model_id: str):
        instance = self.get(model_id)
        return await self.manager.delete(instance)

    async def delete(self, model_id: str):
        # instance = self.update(model_id)
        # return await self.manager.delete(instance)
        pass
