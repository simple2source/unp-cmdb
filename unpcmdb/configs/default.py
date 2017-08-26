# -*- coding: utf-8 -*-
"""
    configs.default
    ~~~~~~~~~~~~~~~~~~~~~~~
"""
import os
import sys
import datetime


class DefaultConfig(object):

    # Get the app root path
    #            <_basedir>
    basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(
                           os.path.dirname(__file__)))))

    # Python version
    py_version = '{0.major}{0.minor}'.format(sys.version_info)

    # Flask Settings
    # ------------------------------
    # There is a whole bunch of more settings available here:
    # http://flask.pocoo.org/docs/0.11/config/#builtin-configuration-values
    DEBUG = False
    TESTING = False

    SEND_LOGS = False

    # The filename for the info and error logs. The logfiles are stored at
    # flaskbb/logs
    INFO_LOG = "info.log"
    ERROR_LOG = "error.log"

    # Database
    # ------------------------------
    # For PostgresSQL:
    #SQLALCHEMY_DATABASE_URI = "postgresql://flaskbb@localhost:5432/flaskbb"
    # For SQLite:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/' + \
                              'flaskbb.sqlite'

    # This option will be removed as soon as Flask-SQLAlchemy removes it.
    # At the moment it is just used to suppress the super annoying warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ECHO = False

    # Security
    # ------------------------------
    # This is the secret key that is used for session signing.
    # You can generate a secure key with os.urandom(24)
    SECRET_KEY = 'x97)\x87\x90\x983\xf6\x88\xbe\x14x\xf8\xd0\x96D>\x19\x89/\x846q\xf0\x8c'

    # You can generate the WTF_CSRF_SECRET_KEY the same way as you have
    # generated the SECRET_KEY. If no WTF_CSRF_SECRET_KEY is provided, it will
    # use the SECRET_KEY.
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "reallyhardtoguess"

    # Full-Text-Search
    # ------------------------------
    # This will use the "whoosh_index" directory to store the search indexes
    WHOOSHEE_DIR = os.path.join(basedir, "whoosh_index", py_version)
    # How long should whooshee try to acquire write lock? (defaults to 2)
    WHOOSHEE_WRITER_TIMEOUT = 2
    # Minimum number of characters for the search (defaults to 3)
    WHOOSHEE_MIN_STRING_LEN = 3

    # Auth
    # ------------------------------
    LOGIN_VIEW = "auth.login"
    REAUTH_VIEW = "auth.reauth"
    LOGIN_MESSAGE_CATEGORY = "info"
    REFRESH_MESSAGE_CATEGORY = "info"

    # The name of the cookie to store the “remember me” information in.
    REMEMBER_COOKIE_NAME = "remember_token"
    # The amount of time before the cookie expires, as a datetime.timedelta object.
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=365)
    # If the “Remember Me” cookie should cross domains,
    # set the domain value here (i.e. .example.com would allow the cookie
    # to be used on all subdomains of example.com).
    REMEMBER_COOKIE_DOMAIN = None
    # Limits the “Remember Me” cookie to a certain path.
    REMEMBER_COOKIE_PATH = "/"
    # Restricts the “Remember Me” cookie’s scope to secure channels (typically HTTPS).
    REMEMBER_COOKIE_SECURE = None
    # Prevents the “Remember Me” cookie from being accessed by client-side scripts.
    REMEMBER_COOKIE_HTTPONLY = False

    # Rate Limiting via Flask-Limiter
    # -------------------------------
    # A full list with configuration values is available at the flask-limiter
    # docs, but you actually just need those settings below.
    # You can disabled the Rate Limiter here as well - it will overwrite
    # the setting from the admin panel!
    # RATELIMIT_ENABLED = True
    # You can choose from:
    #   memory:// (default)
    #   redis://host:port
    #   memcached://host:port
    # Using the redis storage requires the installation of the redis package,
    # which will be installed if you enable REDIS_ENABLE while memcached
    # relies on the pymemcache package.
    #RATELIMIT_STORAGE_URL = "redis://localhost:6379"

    # Caching
    # ------------------------------
    # For all available caching types, have a look at the Flask-Cache docs
    # https://pythonhosted.org/Flask-Caching/#configuring-flask-caching
    CACHE_TYPE = "simple"
    # For redis:
    #CACHE_TYPE = "redis"
    CACHE_DEFAULT_TIMEOUT = 60

    # Redis
    # ------------------------------ #
    # If redis is enabled, it can be used for:
    #   - Sending non blocking emails via Celery (Task Queue)
    #   - Caching
    #   - Rate Limiting
    REDIS_ENABLED = False
    REDIS_URL = "redis://localhost:6379"  # or with a password: "redis://:password@localhost:6379"
    REDIS_DATABASE = 0

    # Plugin Folder
    PLUGINS_FOLDER = os.path.join(basedir, "flaskbb", "plugins")
