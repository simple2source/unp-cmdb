# -*- coding: utf-8 -*-

from flask import Blueprint, request, render_template, session, redirect, url_for
from unpcmdb.utils import login_required
from unpcmdb.user.models import User

user = Blueprint('user', __name__)


@user.route('/')
@login_required
def index():
    name = session['name']
    return render_template("user.html", name=name)

