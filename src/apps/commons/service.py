from db.models.users import *
from db.models.company import *
from db.models.arcticles import *
from db.models.entity_legal import *


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
        return model.create().values(

        )

    def get(self, id):
        # get Принимает на вход: ID сущности
        # Что делает: Возвращает модель сущности с переданным ID
        # Возвращает: Инстанс модели
        pass

    def filter(self):
        # list Принимает на вход: Pydantic модель фильтра сущности
        # Что делает: Возвращает список моделей сущностей подходящих под условия фильтрации
        # Возвращает: Список инстансов модели
        pass

    def update(self):
        # update Принимает на вход: ID сущности, Pydantic модель для обновления
        # Что делает: Обновляет сущность с переданным ID данными из Pydantic модели
        # Возвращает: Инстанс модели
        pass

    def delete(self):
        # delete Принимает на вход: ID сущности
        # Что делает: Удаляет (мягко или окончательно) сущность из базы
        # Возвращает: Ничего
        pass

