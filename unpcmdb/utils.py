from flask import session, redirect, url_for
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get('name', 0) == 0:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return wrapper
