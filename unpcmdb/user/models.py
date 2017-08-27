# -*- coding: utf-8 -*-

from unpcmdb.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(150), nullable=False)

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    def __repr__(self):
        return 'email:{} username:{}'.format(self.email, self.username)
