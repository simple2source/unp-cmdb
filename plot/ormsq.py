#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import walk
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, VARCHAR, ForeignKey, Table, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("mysql+pymysql://root:nMtQc1WvHy1Y2p@192.168.1.7/ute?charset=utf8", echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# ------------ one to one -----------


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    gender = Column(CHAR(5))
    name = Column(VARCHAR(45))
    aid = Column(Integer, ForeignKey('ages.id'), unique=True)
    # age = relationship('Age', uselist=False, back_populates='person')


class Age(Base):
    __tablename__ = 'ages'

    id = Column(Integer, primary_key=True)
    num = Column(Integer)
    person = relationship('Person', backref='ages', uselist=False, order_by='Person.id')
    # person = relationship('Person', back_populates='age')


# ------------ one to many ----------

class Usein(Base):
    __tablename__ = 'usein'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    rid = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role', back_populates='user')


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    user = relationship('Usein', back_populates='role')


# --------------- many to one -----------

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    child_id = Column(Integer, ForeignKey('childs.id'))
    # child = relationship('Child', backref='parents')
    child = relationship('Child', back_populates='parent')


class Child(Base):
    __tablename__ = 'childs'

    id = Column(Integer, primary_key=True)
    uname = Column(VARCHAR(45), index=True)
    # parent = relationship('Parent', backref='childs')
    parent = relationship('Parent', back_populates='child')

# --------------- many to many ----------

pentc = Table('pen_to_color', Base.metadata,
              Column('id', Integer, primary_key=True),
              Column('pid', Integer, ForeignKey('pens.id')),
              Column('cid', Integer, ForeignKey('colors.id'))
              )


class Pen(Base):
    __tablename__ = 'pens'

    id = Column(Integer, primary_key=True)
    name = Column(String(55), index=True)
    size = Column(String(7))
    # color = relationship("Color", secondary=pentc, backref="pens")
    color = relationship("Color", secondary=pentc, back_populates="pen")


class Color(Base):
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True)
    style = Column(String(10))
    pen = relationship('Pen', secondary=pentc, back_populates='color')

if __name__ == '__main__':
    # Base.metadata.create_all(engine)

    """one to one"""
    # ag1 = session.query(Age).filter(Age.id == 2).first()
    # ag1 = Age(num=34)
    # session.add(ag1)
    # session.commit()
    # pe1.age = ag1
    # session.commit()

    """one to many"""
    # rl1 = session.query(Role).filter(Role.id == 1).first()
    # print(rl1.user)
    # us1 = Usein(username='wans')
    # rl1.user.append(us1)
    # session.add(us1)
    # session.commit()

    """many to one"""
    # pa1 = Parent(name='big')
    # pa2 = session.query(Parent).filter(Parent.id == 2).first()
    # ch3 = session.query(Child).filter(Child.id == 2).first()
    # print(pa2.child)
    # ch1 = Child(uname='small')
    # ch2 = Child(uname='medium')
    # session.add_all([pa1, ch1, ch2])
    # session.commit()

    """many to many"""

    # add
    # pe2 = Pen(name='yaunzb', size='mde')
    # cl2 = Color(style='black')
    # pe2.color.append(cl2)   # 增加中间表记录
    # session.add(pe2)
    # session.commit()

    # exist 新增中间表记录
    pe1 = session.query(Pen).filter(Pen.id == 2).first()
    cl1 = session.query(Color).filter(Color.id == 3).first()
    cl1.pen.append(pe1)
    session.commit()
    # pe1.color.remove(cl1)  # delete 中间表关联的数据

    # res = session.query(Usein).filter(Usein.id == 1).first()
    # rl = session.query(Role).filter(Role.id == 1).first()
    # u1 = session.query(Usein).filter(Usein.id == 1).first()
    # r1 = session.query(Role).filter(Role.id == 4).first()
    # print('=========', r1.user, type(r1.user))
    # u2 = Usein(username='jsona')
    # r1.user.append(u2)
    # session.add(u1)
    # session.commit()
    # r1.user = u1
    # print(res.role)
    # p1 = Pen(name='gangbi', size='big')
    # c1 = Color(style='blue')
    # p1 = pentc()
    # session.add()
    # session.commit()
