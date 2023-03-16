from not_django.response_codes import (
    RESPONSE_200,
)
from not_django.templator import (
    render,
)


def response(request, html: str, context={}, code=RESPONSE_200, headers={}):
    """Основная функция, которая формирует ответ"""

    body = render(html, request, context=context)
    response_dict = {
        'body': body,
        'code': code,
        'headers': headers,
    }

    return response_dict
