import os
from jinja2 import Template

from not_django.application import BASE_DIR


def render(template_name, request, context=None):
    """
    Рендерер страницы.
    :param template_name: Имя шаблона
    :param kwargs: Контекст передаваемый в шаблон
    :return:
    """
    view_module = request['VIEW_MODULE']
    template_path = os.path.join(BASE_DIR, view_module, 'templates', template_name)
    with open(template_path, encoding='utf-8') as f:
        template = Template(f.read())

    return template.render(context)
