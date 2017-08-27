# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, HiddenField,
                     SubmitField, SelectField)
from wtforms.validators import (DataRequired, InputRequired, Email, EqualTo,
                                regexp, ValidationError, Required)
from unpcmdb.user.models import User


class LoginForm(FlaskForm):
    """登录表单"""
    username = StringField(u'用户名', validators=[DataRequired(message=u'请输入用户名')])
    password = PasswordField(u'密码', validators=[DataRequired(message=u'请输入密码')])
    remember_me = BooleanField(u'是否记住用户名')
    submit = SubmitField(u"登录")


class RegisterForm(FlaskForm):
    """注册表单"""
    username = StringField(u"用户名", validators=[
        DataRequired(message=u"用户名是必填项")])

    email = StringField(u"电子邮件", validators=[
        DataRequired(message=u"电子邮件是必填项"),
        Email(message=u"错误的邮件格式.")])

    password = PasswordField(u'密码', validators=[
        InputRequired(),
        EqualTo('confirm_password', message=u'密码必须匹配.')])

    confirm_password = PasswordField(u'验证密码')

    submit = SubmitField(u"注册")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')