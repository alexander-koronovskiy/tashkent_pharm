from db.models.users import *
from db.models.company import *
from db.models.arcticles import *
from db.models.entity_legal import *
from sqlalchemy import insert

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BaseService:

    @property
    def query_basic(self):
        # Содержит базовый SQL-Alchemy запрос отсекающий мягко удаленные объекты.
        # Все запросы для вычитки должны брать за основу этот запрос.
        yield

    def create(self, model):
        # create Принимает на вход: Pydantic модель сущности
        # Что делает: Создает в бд новую сущность с данными из переданной модели
        # Возвращает: Инстанс модели
        pass

    def get(self, key: str, default: Any) -> Any:
        # element attributes
        if key in {'Id', 'Status'}:
            return self._obj.attrib.get(key, default)

    def filter(self):
        # list Принимает на вход: Pydantic модель фильтра сущности
        # Что делает: Возвращает список моделей сущностей подходящих под условия фильтрации
        # Возвращает: Список инстансов модели
        pass

    def update(self, model_id):
        # update Принимает на вход: ID сущности, Pydantic модель для обновления
        # Что делает: Обновляет сущность с переданным ID данными из Pydantic модели
        # Возвращает: Инстанс модели
        pass

    def delete(self):
        # delete Принимает на вход: ID сущности
        # Что делает: Удаляет (мягко или окончательно) сущность из базы
        # Возвращает: Ничего
        pass
