from datetime import datetime

from not_django.response import response
from not_django.views import View


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


class IndexView(View):

    def get(self, request):
        form_url = request["path"]

        return response(
            request,
            'form.html',
            context={'form_url': form_url}
        )

    def post(self, request):
        print(f"post_data = {request['post_data']}")

        return response(request, 'form.html')
