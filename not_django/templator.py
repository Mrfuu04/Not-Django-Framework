import os

from jinja2 import (
    FileSystemLoader,
)
from jinja2.environment import (
    Environment,
)

from not_django.application import (
    BASE_DIR,
)


def render(template_name, request, context: dict = None):
    """
    Рендерер страницы.

    Шаблоны ищет в директории приложения в папке templates

    Args:
        template_name: Имя шаблона
        context: Контекст передаваемый в шаблон
    """

    env = Environment()
    view_module = request['view_module']
    template_path = os.path.join(BASE_DIR, view_module, 'templates')

    env.loader = FileSystemLoader(template_path)
    template = env.get_template(template_name)

    return template.render(context)
