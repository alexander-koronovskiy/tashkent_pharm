from apps.commons.manager import ManagerBase as manager_base


class BaseService:

    @property
    def query_basic(self):
        # Содержит базовый SQL-Alchemy запрос отсекающий мягко удаленные объекты.
        # Все запросы для вычитки должны брать за основу этот запрос.
        yield

    async def create_post(self, model, data: dict):
        """
        Принимает на вход: Pydantic модель сущности
        Что делает: Создает в бд новую сущность с данными из переданной модели
        Возвращает: Инстанс модели
        """
        return await manager_base(model).create(data)

    def get(self, key: str, default: Any) -> Any:
        """
        Принимает на вход: ID сущности
        Что делает: Возвращает модель сущности с переданным ID
        Возвращает: Инстанс модели
        """
        pass

    def filter(self):
        """
        list Принимает на вход: Pydantic модель фильтра сущности
        Что делает: Возвращает список моделей сущностей подходящих под условия фильтрации
        Возвращает: Список инстансов модели
        """
        pass

    def update(self, model_id, data: dict):
        """
        update Принимает на вход: ID сущности, Pydantic модель для обновления
        Что делает: Обновляет сущность с переданным ID данными из Pydantic модели
        Возвращает: Инстанс модели
        """
        return await manager_base(model_id).update(data)

    def delete(self, model_id, data: dict):
        """
        delete Принимает на вход: ID сущности
        Что делает: Удаляет (мягко или окончательно) сущность из базы
        Возвращает: Ничего
        """
        return await manager_base(model_id).delete()
