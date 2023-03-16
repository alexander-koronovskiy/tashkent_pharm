from apps.commons.manager import ManagerBase as manager_base

import pydantic
from typing import Any


class BaseService:

    def __init__(self, model: pydantic.BaseModel):
        self.model = model

    @property
    def query_basic(self):
        # Содержит базовый SQL-Alchemy запрос отсекающий мягко удаленные объекты.
        # Все запросы для вычитки должны брать за основу этот запрос.
        pass

    async def create(self, query: dict):
        """
        Принимает на вход: Pydantic модель сущности
        Что делает: Создает в бд новую сущность с данными из переданной модели
        Возвращает: Инстанс модели
        """
        return manager_base.create(self.model)

    def get(self, key: str, default: Any) -> Any:
        """
        Принимает на вход: ID сущности
        Что делает: Возвращает модель сущности с переданным ID
        Возвращает: Инстанс модели
        """
        # return manager_base.create(self.model.id)
        pass

    def filter(self, filter: Any):
        """
        list Принимает на вход: Pydantic модель фильтра сущности
        Что делает: Возвращает список моделей сущностей подходящих под условия фильтрации
        Возвращает: Список инстансов модели
        """
        pass

    def update(self, data: dict):
        """
        update Принимает на вход: ID сущности, Pydantic модель для обновления
        Что делает: Обновляет сущность с переданным ID данными из Pydantic модели
        Возвращает: Инстанс модели
        """
        return manager_base.update(self.model, data)

    def delete(self):
        """
        delete Принимает на вход: ID сущности
        Что делает: Удаляет (мягко или окончательно) сущность из базы
        Возвращает: Ничего
        """
        return manager_base.delete(self.model.id)
