import os
from inspect import isclass
import multipart

from not_django.response_codes import RESPONSE_404
from not_django.views import View

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Application:

    def __init__(self, urls, fronts=None):
        if fronts is None:
            fronts = []
        self.urls = urls
        self.fronts = fronts

    def __call__(self, environ, start_response):
        request = self._get_default_request(environ)

        self._accept_middlewares(request)

        view = self._get_view_by_path(request['path'])

        if not isinstance(view, dict):
            request['view_module'] = view.__module__.split('.')[0]

            response = self.call_view(view, request)
        else:
            response = view

        headers = self._get_updated_headers(response)

        start_response(response['code'], headers)

        bytes_body = [bytes(response['body'], encoding='utf-8')]

        return bytes_body

    def call_view(self, view, request) -> dict:
        """
        Метод вызывает представление. В случае, если это класс унаследованный от View,
        то вызывает в классе тот метод, который делает пользователь.
        """
        if isclass(view) and issubclass(view, View):
            method = request['method']
            if hasattr(view, method):
                if method == 'post':
                    data, _ = multipart.parse_form_data(request['ENVIRON'])
                    request['post_data'] = data.dict
                response = getattr(view, method)(view, request)

            else:
                response = self.__get_error_response()
        elif not isclass(view):
            response = view(request)
        else:
            response = self.__get_error_response()

        return response

    def page_not_found_404(self):
        response_dict = self.__get_error_response()

        return response_dict

    @staticmethod
    def _get_updated_headers(response: dict) -> list:
        default_headers = {
            'Content-Type': 'text/html',
        }
        response['headers'].update(default_headers)

        return list(response['headers'].items())

    def _get_view_by_path(self, path):
        if path.endswith('/'):
            path = path[0:-1]

        for url in self.urls:
            if path in url:
                view = url[path]
                break
            else:
                view = self.page_not_found_404()

        return view

    def _accept_middlewares(self, request):
        for front in self.fronts:
            front(request)

    @staticmethod
    def _get_default_request(environ):
        request = {
            'ENVIRON': environ,
            'path': environ['PATH_INFO'],
            'method': environ['REQUEST_METHOD'].lower(),
            'content_length': environ['CONTENT_LENGTH'],
            'address': f'{environ["HTTP_HOST"]}{environ["PATH_INFO"]}',
            'input_data': environ['wsgi.input'],
        }

        return request

    @staticmethod
    def __get_error_response():
        response_dict = {
            'body': '404 BAD REQUEST',
            'code': RESPONSE_404,
            'headers': {},
        }

        return response_dict


class LoggingApplication(Application):

    def call_view(self, view, request) -> dict:
        print(f'request method ---> {request["method"]}')
        print(f'request ---> {request}')
        return super().call_view(view, request)
