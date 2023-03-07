from mapper import (
    BaseModel,
    MapperRegistry,
)

from settings import (
    DB_CONNECTION,
)


class Category(BaseModel):
    """Таблица 'Категория'."""

    def __init__(self, id, title, info):
        self.id = id
        self.title = title
        self.info = info


class CategoryMapper:
    """Маппер категорий.

    Реализация паттерна Data Mapper.
    Слой преобразования данных.
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id):
        statement = "SELECT id, title, info FROM category WHERE id=?"
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Category(*result)
        else:
            raise Exception(f'record with id={id} not found')

    def insert(self, category):
        statement = "INSERT INTO category (title, info) VALUES (?, ?)"
        self.cursor.execute(statement, (category.title, category.info))
        self.connection.commit()

    def update(self, category):
        statement = "UPDATE category SET title=?, info=? WHERE id=?"
        self.cursor.execute(
            statement, (
                category.first_name, category.last_name, category.id_person)
        )
        self.connection.commit()

    def delete(self, category):
        statement = "DELETE FROM category WHERE id=?"
        self.cursor.execute(statement, (category.id,))
        self.connection.commit()


class CategoryMapperRegistry(MapperRegistry):
    MAPPER_OBJ = (Category, CategoryMapper)
    CONNECTION = DB_CONNECTION
