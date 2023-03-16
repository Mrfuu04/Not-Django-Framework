from importlib import (
    import_module,
)

from not_django.exceptions import (
    AppNotFound,
)

ROUTES = {}


def path(main_url, app_name):
    """Регистрирует пути под каждое приложение.

    Применение - в приложении в модуле urls.py urls представляет собой словарь, где:
        ключ: относительный путь - /index
        значение: представление - IndexView
    В проекте основной модуль urls.py представляет собой список, где указывается базовый путь под каждое приложение:
        path('/base', 'Имя_приложения') - То есть для IndexView адрес будет следующий - .com/base/index
    """

    try:
        urls = import_module(f'{app_name}.urls').urls
    except ModuleNotFoundError as e:
        raise AppNotFound(e)
    for key in tuple(urls.keys()):
        urls[f'{main_url}{key}'] = urls.pop(key)

    return urls
