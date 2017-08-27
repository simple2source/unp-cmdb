# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, url_for, redirect, session
from unpcmdb.auth.form import LoginForm, RegisterForm
from unpcmdb.user.models import User
from unpcmdb.extensions import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            session['name'] = user.username
            return redirect(url_for('user.index'))
    return render_template('login.html', form=form)


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    from werkzeug.security import generate_password_hash

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data)
        user.password = generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('.login'))
