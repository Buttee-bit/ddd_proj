import logging
from app.domain.entity.ner.entity import Ner
from app.domain.entity.object.object import ObjectDomain

def test_create_domain_object():
    object_domain = ObjectDomain(main_name='тестовая шняга')
    assert object_domain.main_name == 'тестовая шняга'

def test_add_child_to_domain_object():
    object_domain = ObjectDomain(main_name='ПАПАША')
    children = ObjectDomain(main_name='детишко')
    object_domain.add_child(children=children)
    assert len(object_domain.childrens) == 1

def test_delete_child_domain_object():
    object_domain = ObjectDomain(main_name='ПАПАША')
    children = ObjectDomain(main_name='детишко')
    object_domain.add_child(children=children)
    object_domain.delete_child(children=children)
    assert len(object_domain.childrens) == 0


def test_delete_child_domain_object():
    object_domain = ObjectDomain(main_name='ПАПАША')
    ner = Ner(
        value='ner',
        type='ner',
        props='ner',
        )
    object_domain.add_ner(ner=ner)
    object_domain.delete_ner(ner=ner)
    assert len(object_domain.ners) == 0
