#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask_script import Manager, Shell, prompt_bool
from flask import request, render_template
from unpcmdb.extensions import db
from unpcmdb.user.models import User
from unpcmdb.asset.models import Archetype, ArchetypeAttribute, Entity, EntityValue
from unpcmdb import create_app, ListConverter

basepath = os.path.dirname(os.path.abspath(__file__))
app = create_app(config=os.path.join(basepath, 'config.cfg'))
app.url_map.converters['list'] = ListConverter


def make_shell_context():
    return dict(app=app, db=db, User=User, Archetype=Archetype,
                ArchetypeAttribute=ArchetypeAttribute, Entity=Entity, EntityValue=EntityValue)

manager = Manager(app)


@manager.command
def dropdb():
    # 清空数据
    if prompt_bool('delete all data'):
        db.drop_all()
manager.add_command("sh", Shell(make_context=make_shell_context))


@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/hello/<string:name>')
def hello(name):
    return '<h1>Hello {}!</h1>'.format(name)


@app.route('/hi')
def hi():
    # 查询字符串形式，从url中获取参数
    s = request.args.get('name')
    return '<h1>Hi {}!</h1>'.format(s)


@app.route('/name/<int:uid>')
def u_id(uid):
    # 指定传入的uid为int类型
    return 'user id {}'.format(uid)


@app.route('/t')
def t():
    from flask import redirect, url_for
    print(request.endpoint)
    return redirect(url_for('user.index'))


@app.route('/home/<list:subs>')
def home(subs):
    # 使用自定义类型
    htm = ''
    for sub in subs:
        htm += '<h1>{}</h1>'.format(sub)
    return htm


if __name__ == '__main__':
    manager.run()
