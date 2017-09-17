#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, request
from unpcmdb.asset.models import ArchetypeAttribute, Archetype, EntityValue, Entity
from unpcmdb.extensions import db
from flask import jsonify

asset = Blueprint('asset', __name__)


@asset.route('/')
def index():
    a = db.session.query(Entity, EntityValue).join(Entity.id == EntityValue.entity_id).all()


@asset.route('/add_archetype', methods=['POST'])
def add_archetype():
    data = request.json
    if not data:
        raise ValueError('request data not allow null')
    archetype = Archetype(archetype_name=data.get('archetype_name'))
    db.session.add(archetype)
    for attribute in json.loads(data.get('att_list')):
        archetype_att = ArchetypeAttribute(**attribute)
        archetype.attribute.append(archetype_att)
        db.session.add(archetype_att)
    db.session.commit()
    return jsonify(ret=0, msg='ok')


@asset.route('/add_entity')
def add_entity():
    data = request.json
    archetype_id = data.get('archetype_id')
    entity_values = json.loads(data.get('entity_values'))
    if not data and archetype_id:
        raise ValueError('request data error')
    entity = Entity(archetype_id=archetype_id)
    db.session.add(entity)
    archetype_att_list = ArchetypeAttribute.query.filter(ArchetypeAttribute.archetype_id == archetype_id).all()
    for archetype_att in archetype_att_list:
        if archetype_att.null == 1:
            for entity_value in entity_values:
                if entity_value['id'] == archetype_att.att_id:
                    break
            else:
                raise ValueError('attr not allow null')
        if archetype_att.unique == 1:
            same_value = []
            for entity_value in entity_values:
                if entity_value['id'] == archetype_att.att_id:
                    same_value.append(entity_value['attr'])
            else:
                if len(same_value) > 1:
                    raise ValueError('attr must unique')

    for entity_value in entity_values:
        entity_v_instance = EntityValue(entity_id=entity.id, archetype_att_id=entity_value['id'],
                                        value=entity_value['attr'])
        db.session.add(entity_v_instance)
    db.session.commit()
    return jsonify(ret=0, msg='ok')


