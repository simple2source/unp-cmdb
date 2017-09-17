# -*- coding: utf-8 -*-

from flask import Blueprint, request, render_template, session, redirect, send_from_directory, make_response, send_file
from unpcmdb.utils import login_required
from unpcmdb.user.models import User

user = Blueprint('user', __name__)


@user.route('/')
@login_required
def index():
    name = session['name']
    return render_template("user.html", name=name)


@user.route('/down')
def down():
    name = {'name': 'jack', 'age': 19}
    import json
    from flask import current_app
    print(current_app.root_path)
    resp = make_response(json.dumps(name))
    return send_from_directory(directory=current_app.root_path, filename='requirement.txt')

