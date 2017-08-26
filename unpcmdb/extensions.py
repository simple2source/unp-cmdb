# -*- coding: utf-8 -*-
"""
    extensions
    ~~~~~~~~~~~~~~~~~~

"""
from flask_allows import Allows
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_caching import Cache
from flask_themes2 import Themes
from flask_alembic import Alembic
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_mail import Mail
from flask_limiter.util import get_remote_address
from unpcmdb.exceptions import AuthorizationRequired


# Permissions Manager
allows = Allows(throws=AuthorizationRequired)

# Database
db = SQLAlchemy()


# Login
login_manager = LoginManager()


# Caching
cache = Cache()


# Migrations
alembic = Alembic()

# Themes
themes = Themes()


# CSRF
csrf = CSRFProtect()

# Mail
mail = Mail()

# Rate Limiting
limiter = Limiter(auto_check=False, key_func=get_remote_address)

