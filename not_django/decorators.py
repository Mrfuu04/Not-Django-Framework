from extra import (
    Singleton,
)

from urls import (
    ROUTES,
)


class Router(metaclass=Singleton):
    """
    Класс-декоратор. Используется для привязки урла к контроллеру.
    В качестве url принимает полный путь.

    Для регистрации функционала добавить ROUTES из urls.py в список корневого urls
    """

    def __init__(self, url):
        self.url = url

    def __call__(self, func, *args, **kwargs):
        ROUTES[self.url] = func
