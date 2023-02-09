import os
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from not_django.application import BASE_DIR


def render(template_name, request, context: dict = None):
    """
    Рендерер страницы.
    :param template_name: Имя шаблона
    :param context: Контекст передаваемый в шаблон
    :return:
    """
    env = Environment()
    view_module = request['view_module']
    template_path = os.path.join(BASE_DIR, view_module, 'templates')

    env.loader = FileSystemLoader(template_path)
    template = env.get_template(template_name)

    return template.render(context)
