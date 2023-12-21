#!/usr/bin/python3
""" document documt """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")

class TestBaseModel(unittest.TestCase):
    """Testbase model"""
    def test_uuid(self):
        """test uuid"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_id_type(self):
        """test id type"""
        model1 = BaseModel()
        self.assertEqual(type(model1.id), str)

    def test_created_at_type(self):
        """test created_at type"""
        model1 = BaseModel()
        self.assertEqual(type(model1.created_at), datetime.datetime)

    def test_updated_at_type(self):
        """test updated_at type"""
        model1 = BaseModel()
        self.assertEqual(type(model1.updated_at), datetime.datetime)

    def test_created_at(self):
        """test created_at"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.created_at, model2.created_at)

    def test_updated_at(self):
        """test updated_at"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.updated_at, model2.updated_at)

    def test_str(self):
        """test str"""
        model1 = BaseModel()
        model1_str = "[BaseModel] ({}) {}".format(model1.id, model1.__dict__)
        self.assertEqual(model1_str, str(model1))

    def test_save(self):
        """test save"""
        model1 = BaseModel()
        model1.save()
        model1_updated_at = model1.updated_at
        model1.save()
        model1_updated_at2 = model1.updated_at
        self.assertNotEqual(model1_updated_at, model1_updated_at2)

    def test_to_dict(self):
        """test to_dict"""
        model1 = BaseModel()
        model1_dict = model1.to_dict()
        self.assertEqual(type(model1_dict), dict)
        self.assertEqual(model1_dict["id"], model1.id)
        self.assertEqual(model1_dict["__class__"], "BaseModel")
        self.assertEqual(model1_dict["created_at"], model1.created_at.isoformat())
        self.assertEqual(model1_dict["updated_at"], model1.updated_at.isoformat())

    def test_to_dict_type(self):
        """test to_dict_type"""
        model1 = BaseModel()
        model1_dict = model1.to_dict()
        self.assertEqual(type(model1_dict["created_at"]), str)
        self.assertEqual(type(model1_dict["updated_at"]), str)

    def test_to_dict_key(self):
        """test to_dict_key"""
        model1 = BaseModel()