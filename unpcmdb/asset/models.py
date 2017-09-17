#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unpcmdb.extensions import db


class Archetype(db.Model):
    __tablename__ = 'archetype'

    eid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    archetype_name = db.Column(db.String(255))
    attribute = db.relationship('ArchetypeAttribute', back_populates='archetype')


class ArchetypeAttribute(db.Model):
    __tablename__ = 'archetype_attribute'

    att_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    att_name = db.Column(db.String(255), unique=True, nullable=False)
    unique = db.Column(db.Boolean, nullable=False, default=True)
    null = db.Column(db.Boolean, nullable=False, default=True)
    archetype_id = db.Column(db.Integer, db.ForeignKey('archetype.eid'))
    archetype = db.relationship('Archetype', back_populates='attribute')


class Entity(db.Model):
    __tablename__ = 'entity'

    id = db.Column(db.Integer, primary_key=True)
    archetype_id = db.Column(db.Integer, db.ForeignKey('archetype.eid'))


class EntityValue(db.Model):
    __tablename__ = 'entity_value'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    archetype_att_id = db.Column(db.Integer, db.ForeignKey('archetype_attribute.att_id'))

