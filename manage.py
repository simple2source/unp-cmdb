#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask_script import Manager, Shell
from flask import request
from unpcmdb import create_app, ListConverter

basepath = os.path.dirname(os.path.abspath(__file__))
app = create_app(config=os.path.join(basepath, 'config.cfg'))
app.url_map.converters['list'] = ListConverter

manager = Manager(app)


@app.route('/hello/<string:name>')
def hello(name):
    return '<h1>Hello {}!</h1>'.format(name)


@app.route('/hi')
def hi():
    # 查询字符串形式，从url中获取参数
    s = request.args.get('user')
    return '<h1>Hi {}!</h1>'.format(s)


@app.route('/user/<int:uid>')
def user(uid):
    # 指定传入的uid为int类型
    return 'user id {}'.format(uid)


@app.route('/home/<list:subs>')
def home(subs):
    # 使用自定义类型
    htm = ''
    for sub in subs:
        htm += '<h1>{}</h1>'.format(sub)
    return htm


if __name__ == '__main__':
    manager.run()
