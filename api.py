import logging

from functools import wraps
from collections import defaultdict
from wsgiref.simple_server import make_server

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def route(path=None, method=None):
    def deco(f):

        f._route_method = method
        f._route_path = path

        @wraps(f)
        def wapper(*args, **kargs):
            return f(*args, **kargs)
        return wapper
    return deco


class Application(object):

    def __init__(self, port):
        self.port = port
        self.path = defaultdict(dict)

    def set_path(self, prefix, func):
        self.path[func._route_method][prefix+func._route_path] = func

    def application(self, environ, start_response):
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        if method in self.path and path in self.path[method]:
            func = self.path[method][path]
            return func(environ, start_response)
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [b'<h1>404 Not Found, path not found</h1>']

    def run(self):
        httpd = make_server('', self.port, self.application)
        _logger.info('Serving HTTP on port %s', self.port)
        httpd.serve_forever()
