import os
from not_django.response_codes import RESPONSE_404


def page_not_found_404(request):
    return {'code': RESPONSE_404}, '404 page not found'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Application:

    def __init__(self, urls, fronts=None):
        if fronts is None:
            fronts = []
        self.urls = urls
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        request = {
            'ENVIRON': environ,
            'PATH_INFO': path,
        }
        self._accept_middlewares(request)

        view = self._get_view_by_path(path)
        request['VIEW_MODULE'] = view.__module__.split('.')[0]
        response, body = view(request)

        headers = response.get('headers') if response.get('headers') else [('Content-Type', 'text/html')]
        start_response(response['code'], headers)

        bytes_body = [bytes(body, encoding='utf-8')]

        return bytes_body

    def _get_view_by_path(self, path):
        if path.endswith('/'):
            path = path[0:-1]

        for url in self.urls:
            if path in url:
                view = url[path]
                break
            else:
                view = page_not_found_404

        return view

    def _accept_middlewares(self, request):
        for front in self.fronts:
            front(request)
