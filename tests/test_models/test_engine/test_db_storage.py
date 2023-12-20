#!/usr/bin/python3
"""Unittest for DBStorage class"""

import unittest
import pep8
import os
import datetime
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City


class TestDBStorage(unittest.TestCase):
    """Test for DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "CA"
        cls.city.save()

    @classmethod
    def teardown(cls):
        """Teardown for the test"""
        del cls.city

    def test_pep8_DBStorage(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_docstring_DBStorage(self):
        """Test for docstring"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def test_init(self):
        """Test for init"""
        self.assertTrue(isinstance(self.city, City))
        self.assertTrue(isinstance(self.city.name, str))
        self.assertTrue(isinstance(self.city.state_id, str))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "__class__"))
        self.assertTrue(hasattr(self.city, "save"))
        self.assertTrue(hasattr(self.city, "to_dict"))
        self.assertTrue(isinstance(self.city.id, str))
        self.assertTrue(isinstance(self.city.created_at, datetime))
        self.assertTrue(isinstance(self.city.updated_at, datetime))
        self.assertTrue(isinstance(self.city.__class__, type))
        # self.assertTrue(isinstance(self.city.save, function))

    def test_all(self):
        """Test for all"""
        storage = DBStorage()
        storage.reload()
        self.assertTrue(isinstance(storage.all(), dict))
        self.assertEqual(len(storage.all()), 0)
        self.assertTrue(isinstance(storage._DBStorage__session, Session))
        self.assertTrue(isinstance(storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(
            storage._DBStorage__sessionmaker, SessionMaker))
        self.assertTrue(isinstance(storage._DBStorage__classes, dict))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["State"], State))
        self.assertTrue(isinstance(storage._DBStorage__classes["City"], City))

    def test_new(self):
        """Test for new"""
        storage = DBStorage()
        storage.reload()
        storage.new(self.city)
        self.assertTrue(len(storage.all()), 1)
        self.assertTrue(isinstance(storage.all(), dict))
        self.assertTrue(isinstance(storage._DBStorage__session, Session))
        self.assertTrue(isinstance(storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(
            storage._DBStorage__sessionmaker, SessionMaker))
        self.assertTrue(isinstance(storage._DBStorage__classes, dict))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["State"], State))
        self.assertTrue(isinstance(storage._DBStorage__classes["City"], City))

    def test_save(self):
        """Test for save"""
        storage = DBStorage()
        storage.reload()
        storage.save()
        self.assertTrue(isinstance(storage._DBStorage__session, Session))
        self.assertTrue(isinstance(storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(storage._DBStorage__classes, dict))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["State"], State))
        self.assertTrue(isinstance(storage._DBStorage__classes["City"], City))

    def test_delete(self):
        """Test for delete"""
        storage = DBStorage()
        storage.reload()
        storage.delete(self.user)
        self.assertTrue(isinstance(storage._DBStorage__session, Session))
        self.assertTrue(isinstance(storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(
            storage._DBStorage__sessionmaker, SessionMaker))
        self.assertTrue(isinstance(storage._DBStorage__classes, dict))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["State"], State))
        self.assertTrue(isinstance(storage._DBStorage__classes["City"], City))
        self.assertTrue(isinstance(storage._DBStorage__classes["User"], User))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["Place"], Place))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["Review"], Review))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["Amenity"], Amenity))

    def test_reload(self):
        """Test for reload"""
        storage = DBStorage()
        storage.reload()
        self.assertTrue(isinstance(storage._DBStorage__session, Session))
        self.assertTrue(isinstance(storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(
            storage._DBStorage__sessionmaker, SessionMaker))
        self.assertTrue(isinstance(storage._DBStorage__classes, dict))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["State"], State))
        self.assertTrue(isinstance(storage._DBStorage__classes["City"], City))
        self.assertTrue(isinstance(storage._DBStorage__classes["User"], User))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["Place"], Place))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["Review"], Review))
        self.assertTrue(isinstance(
            storage._DBStorage__classes["Amenity"], Amenity))
