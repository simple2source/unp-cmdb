# -*- coding: utf-8 -*-

__version__ = '1.0'  # noqa
from unpcmdb.app import create_app
from werkzeug.routing import BaseConverter


class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value) for value in values)
