from sqlalchemy import BinaryExpression, select, Select
import pydantic
from typing import Any, Type, Union, Tuple

from apps.commons.manager import ManagerBase
from db.database import Base


class ServiceBase:

    MODEL: Type[Base] = None

    def __init__(self, manager: ManagerBase):
        self.manager = manager

    def select(self, *selects) -> Select[Any]:
        # Содержит базовый SQL-Alchemy запрос отсекающий мягко удаленные объекты.
        # Все запросы для вычитки должны брать за основу этот запрос.
        if not selects:
            selects = self.MODEL,
        return select(*selects).where(self.MODEL.is_deleted.is_(False))

    async def create(self, data: pydantic.BaseModel) -> MODEL:
        """
        Принимает на вход: Pydantic модель сущности
        Что делает: Создает в бд новую сущность с данными из переданной модели
        Возвращает: Инстанс модели
        """
        # u1 = U# (name="pkrabs", fullname="Pearl Krabs")
        instance = self.MODEL(data.dict(exclude_unset=True))
        return await self.manager.create(instance)

    def get(self, key: str, default: Any) -> Any:
        """
        Принимает на вход: ID сущности
        Что делает: Возвращает модель сущности с переданным ID
        Возвращает: Инстанс модели
        """
        # return manager_base.create(self.model.id)
        pass

    def list(self, filter: Any):
        """
        list Принимает на вход: Pydantic модель фильтра сущности
        Что делает: Возвращает список моделей сущностей подходящих под условия фильтрации
        Возвращает: Список инстансов модели
        """
        # self.select().where()...
        # pydantics model with filters
        pass

    def update(self, data: dict):
        """
        update Принимает на вход: ID сущности, Pydantic модель для обновления
        Что делает: Обновляет сущность с переданным ID данными из Pydantic модели
        Возвращает: Инстанс модели
        """
        # instance = self.MODEL(data.dict(exclude_unset=True))
        # return await self.manager.update(instance)
        pass

    def delete(self):
        """
        delete Принимает на вход: ID сущности
        Что делает: Удаляет (мягко или окончательно) сущность из базы
        Возвращает: Ничего
        """
        # return manager_base.delete(self.model.id)
        pass
