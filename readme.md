# 使用 wsgi 搭建简单 web 框架

```python
from wsgiref.simple_server import maker_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, world!</h1>']


httpd = make_server('', 8081, application)
httpd.serve_forever()
```
