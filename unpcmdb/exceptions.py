# -*- coding: utf-8 -*-

"""
    exceptions
    ~~~~~~~~~~~~~~~~~~
"""
from werkzeug.exceptions import HTTPException, Forbidden


class UnpcmdbError(HTTPException):
    """Root exception"""
    description = "An internal error has occured"


class AuthorizationRequired(UnpcmdbError, Forbidden):
    description = u"没有权限访问"


class AuthenticationError(UnpcmdbError):
    description = u"用户名或者密码错误"
