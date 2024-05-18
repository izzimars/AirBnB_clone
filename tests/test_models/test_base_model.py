#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def setUp(self):
        self.varone = BaseModel()
        self.vartwo = BaseModel()

    def test_instanciation_with_variables(self):
        with self.assertRaises(TypeError):
            BaseModel(4)
        with self.assertRaises(TypeError):
            BaseModel("Temi")
        with self.assertRaises(TypeError):
            BaseModel([])

    def test_class_id_not_none(self):
        self.assertIsNotNone(self.varone.id)
        self.assertIsNotNone(self.vartwo.id)

    def test_class_is_string(self):
        self.assertIs(str, type(self.varone.id))
        self.assertIs(str, type(self.vartwo.id))

    def test_class_id_not_equal(self):
        self.assertNotEqual(self.varone.id, self.vartwo.id)

    def test_created_at(self):
        self.assertIsNotNone(self.varone.created_at)
        self.assertIsNotNone(self.vartwo.created_at)

    def test_updated_at(self):
        self.assertIsNotNone(self.varone.updated_at)
        self.assertIsNotNone(self.vartwo.updated_at)

    def test_str_method(self):
        obj = self.varone
        expected_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        b1 = self.varone.updated_at
        self.varone.save()
        self.assertNotEqual(b1, self.varone.updated_at)
        self.assertTrue(datetime.datetime.now() >= self.varone.updated_at)

    def test_to_dict(self):
        b1 = self.varone.to_dict()
        self.assertTrue("id" in b1)
        self.assertTrue("created_at" in b1)
        self.assertTrue("updated_at" in b1)
        self.assertTrue("__class__" in b1)
        temp = bool(datetime.datetime.fromisoformat(b1["created_at"]))
        self.assertTrue(temp)
        temp = bool(datetime.datetime.fromisoformat(b1["updated_at"]))
        self.assertTrue(temp)
        self.assertTrue(b1["__class__"] == "BaseModel")


if __name__ == "__main__":
    unittest.main()
