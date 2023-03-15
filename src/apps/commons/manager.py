from sqlalchemy.ext.asyncio import AsyncSession


class ManagesBase:
    def __init__(self, session: AsyncSession):
        self.session = session

    def execute(self, query):
        return self.session.execute(query)

    async def create(self, instance):
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def update(self, instance, data_update: dict):
        for field in data_update.keys():
            setattr(instance, field, data_update.get(field))
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def delete(self, instance):
        self.session.delete(instance)
        await self.session.commit()
        return instance
