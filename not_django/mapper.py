import threading


class MapperRegistryMeta(type):
    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        if new_cls.__name__ != 'MapperRegistry':
            __class__.REGISTRY[new_cls.__name__] = {
                'table': new_cls.MAPPER_OBJ[0],
                'table_mapper': new_cls.MAPPER_OBJ[1],
                'connection': new_cls.CONNECTION,
            }

        return new_cls


class MapperRegistry(metaclass=MapperRegistryMeta):
    """Регистрация мапперов.

    Все регистраторы мапперов в приложениях должны наследоваться от этого класса.
    В MAPPER_OBJ в виде tuple определяются объект модели и его маппер
        пример:  MAPPER_OBJ = (User, UserMapper)

    В CONNECTION коннект с базой (обычно значение DB_CONNECTION из settings.py)
    """

    __slots__ = ['MAPPER_OBJ', 'CONNECTION']

    def get_mapper(self, obj):
        for val in __class__.REGISTRY.values():
            if isinstance(obj, val['table']):
                return val['table_mapper'](val['connection'])


class BaseModel:
    """Базовая модель для всех моделей таблиц."""

    def mark_new(self):
        UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        UnitOfWork.get_current().register_removed(self)


class UnitOfWork:
    """Применение паттерна UnitOfWork.

    Содержит список охватываемых бизнес-транзакцией объектов, координирует запись изменений в базе
    данных и разрешает проблемы параллелизма.
    """

    current = threading.local()

    def __init__(self):
        self.mapper_registry = MapperRegistry()
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []

    def register_new(self, obj):
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        self.dirty_objects.append(obj)

    def register_removed(self, obj):
        self.removed_objects.append(obj)

    def commit(self):
        self.insert_new()
        self.update_dirty()
        self.delete_removed()

    def insert_new(self):
        for obj in self.new_objects:
            self.mapper_registry.get_mapper(obj).insert(obj)

    def update_dirty(self):
        for obj in self.dirty_objects:
            self.mapper_registry.get_mapper(obj).update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            self.mapper_registry.get_mapper(obj).delete(obj)

    @staticmethod
    def new_current():
        __class__.set_current(UnitOfWork())

    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work

    @classmethod
    def get_current(cls):
        return cls.current.unit_of_work
