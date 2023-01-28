from wsgiref.simple_server import make_server

from not_django.application import Application
from urls import urls

application = Application(urls)

with make_server('', 8000, application) as httpd:
    print('Server started at 127.0.0.1:8000')
    httpd.serve_forever()
