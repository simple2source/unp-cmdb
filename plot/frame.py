#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server


def abc():
    return '<h1>abc</h1>'


def xyz():
    return '<h1>xyz</h1>'

router = {'/abc': abc, '/xyz': xyz}


def runserver(env, start_response):
    print(env)  # 服务端和客户端的环境变量，包括客户端访问url的路径以及查询字符串等信息
    print(env['QUERY_STRING'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    url_prefix = env['PATH_INFO']  # 客户端的url后缀
    if url_prefix in router.keys():
        return router[url_prefix]()
    else:
        return '<h1>404 not found</h1>'


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8080, runserver)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    import webbrowser
    webbrowser.open('http://localhost:8080/xyz?abc')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
