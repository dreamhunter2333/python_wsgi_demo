from api import route


@route(path='/demo', method='GET')
def demo1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Demo1</h1>']


@route(path='/demo', method='POST')
def demo2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Demo2</h1>']
