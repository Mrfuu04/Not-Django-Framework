from not_django.templator import render
from not_django.response_codes import RESPONSE_200


def response(request, html, context={}, code=RESPONSE_200, headers={}):
    body = render(html, request, context=context)
    response_dict = {
        'body': body,
        'code': code,
        'headers': headers,
    }

    return response_dict
