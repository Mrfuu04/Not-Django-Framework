from importlib import import_module

from not_django.exceptions import AppNotFound


def path(main_url, app_name):
    try:
        urls = import_module(f'{app_name}.urls').urls
    except ModuleNotFoundError as e:
        raise AppNotFound(e)
    for key in tuple(urls.keys()):
        urls[f'{main_url}{key}'] = urls.pop(key)

    return urls
