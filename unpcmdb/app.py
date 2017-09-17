# -*- coding: utf-8 -*-

import os
import jinja2
from flask import Flask, render_template
from flask._compat import string_types
from unpcmdb.extensions import (db, login_manager, cache, allows, limiter, csrf,
                                alembic, themes, mail, bootstrap)
from unpcmdb.user.views import user
from unpcmdb.user.models import User
from unpcmdb.auth.viwes import auth
from unpcmdb.asset.viwes import asset


def create_app(config=None):
    """
    工厂方法创建配置app实例
    :param config: 配置是文件或者config 对象
    :return:
    """
    app = Flask('unp')
    # 指定jinjia2 template目录位置
    tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app.jinja_loader = jinja2.FileSystemLoader(tmpl_dir)
    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
    configure_errorhandlers(app)
    return app


def configure_app(app, config):
    """配置项目"""
    app.config.from_object('unpcmdb.configs.default.DefaultConfig')

    if isinstance(config, string_types) and \
            os.path.exists(os.path.abspath(config)):
        config = os.path.abspath(config)
        app.config.from_pyfile(config)
    else:
        app.config.from_object(config)
    app.config['CONFIG_PATH'] = config

    # 增加环境变量中配置
    app.config.from_envvar("UNP_SETTING", silent=True)


def configure_blueprints(app):
    """配置蓝图注册到app实例"""
    app.register_blueprint(user, url_prefix=app.config["USER_URL_PREFIX"])
    app.register_blueprint(auth, url_prefix=app.config['AUTH_URL_PREFIX'])
    app.register_blueprint(asset, url_prefix=app.config['ASSET_URL_PREFIX'])


def configure_extensions(app):
    """Configures the extensions."""

    # Flask-WTF CSRF
    # csrf.init_app(app)

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Alembic
    alembic.init_app(app, command_name="db")

    # Flask-Mail
    mail.init_app(app)

    # Flask-Cache
    cache.init_app(app)

    # Flask-Themes
    themes.init_themes(app, app_identifier="unpcmdb")

    # Flask-Limiter
    limiter.init_app(app)

    # Flask-Bootstrap
    bootstrap.init_app(app)

    # Flask-Login
    login_manager.login_view = app.config["LOGIN_VIEW"]
    login_manager.refresh_view = app.config["REAUTH_VIEW"]
    login_manager.login_message_category = app.config["LOGIN_MESSAGE_CATEGORY"]
    login_manager.needs_refresh_message_category = \
        app.config["REFRESH_MESSAGE_CATEGORY"]
    # login_manager.anonymous_user = Guest
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """Loads the user. Required by the `login` extension."""

        user_instance = User.query.filter_by(id=user_id).first()
        if user_instance:
            return user_instance
        else:
            return None
    #
    #
    # # Flask-Allows
    # allows.init_app(app)
    # allows.identity_loader(lambda: current_user)


def configure_errorhandlers(app):
    """Configures the error handlers."""

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/page_not_found.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500
