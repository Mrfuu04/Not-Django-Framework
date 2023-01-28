from datetime import datetime

from not_django.response import response


def index_view(request):
    context = {
        'current_date': datetime.today().strftime('%Y-%m-%d'),
    }

    return response(request, 'index.html', context=context)


def about_view(request):
    context = {
        'name': 'Sergei',
        'phone_number': '911',
    }

    return response(request, 'about.html', context=context)
