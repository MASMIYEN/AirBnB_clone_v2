#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                 'db', "only testing db storage")
class test_DBStorage(unittest.TestCase):
    """ Class to test the DBStorage method """

    def test_all(self):
        """ Test the all method """
        storage.reload()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """ Test the new method """
        storage.reload()
        new = BaseModel()
        new.save()
        self.assertIn(new, storage.all().values())

    def test_save(self):
        """ Test the save method """
        storage.reload()
        new = BaseModel()
        new.save()
        storage.save()
        with open("file.json", "r") as f:
            self.assertIn(new.__class__.__name__ + "." + new.id, f.read())

    def test_reload(self):
        """ Test the reload method """
        storage.reload()
        self.assertIsInstance(storage.all(), dict)

    def test_delete(self):
        """ Test the delete method """
        storage.reload()
        new = BaseModel()
        new.save()
        storage.delete(new)
        self.assertNotIn(new, storage.all().values())

    def test_get(self):
        """ Test the get method """
        storage.reload()
        new = BaseModel()
        new.save()
        self.assertEqual(storage.get(new.__class__.__name__, new.id), new)

    def test_count(self):
        """ Test the count method """
        storage.reload()
        new = BaseModel()
        new.save()
        self.assertEqual(storage.count(new.__class__.__name__), 1)
