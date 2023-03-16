from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Executable

from db.database import Base


class ManagerBase:
    def __init__(self, session: AsyncSession):
        self.session = session

    def execute(self, query: Executable):
        return self.session.execute(query)

    async def create(self, instance: Base):
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def update(self, instance: Base, data_update: dict):
        for field in data_update.keys():
            setattr(instance, field, data_update.get(field))
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def delete(self, instance: Base):
        await self.session.delete(instance)
        await self.session.commit()
        return instance
