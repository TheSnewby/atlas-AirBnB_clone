#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test for FileStorage class
    """
    def setUp(self):
        """
        SetUp for FileStorage class
        """
        self.storage = FileStorage()
        self.test_model = BaseModel()
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """
        TearDown for FileStorage class
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_objects(self):
        """
        Test for __objects attribute
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all(self):
        """
        Test for all method
        """
        self.assertTrue(isinstance(self.storage.all(), dict))

    def test_new(self):
        """
        Test for new method
        """
        storage = FileStorage()
        storage.new(BaseModel())
        self.assertTrue(isinstance(storage.all(), dict))

    def test_save(self):
        """
        Test for save method
        """
        self.storage.new(self.test_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, "r") as file:
            file_content = json.load(file)
            key = f"BaseModel.{self.test_model.id}"
            self.assertIn(key, file_content)
            self.assertEqual(file_content[key], self.test_model.to_dict())

    def test_reload(self):
        """
        Test for reload method
        """
        self.storage.new(self.test_model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = f"BaseModel.{self.test_model.id}"
        storage_objects = self.storage.all()
        self.assertIn(key, storage_objects)
        self.assertIsInstance(storage_objects[key], BaseModel)

if __name__ == "__main__":
    unittest.main()
