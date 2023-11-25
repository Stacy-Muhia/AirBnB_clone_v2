#!/usr/bin/python3
"""Unittest module for the db_storage file"""

import unittest
from models import storage
from models.user import User
from models.place import Place

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up a clean database before each test."""
        storage.reload()

    def test_all_method(self):
        """Test the 'all' method."""

        test_user = User()
        test_user.save()

        test_place = Place()
        test_place.save()

        all_objects = storage.all()

        user_key = 'User.{}'.format(test_user.id)
        self.assertIn(user_key, all_objects)

        place_key = 'Place.{}'.format(test_place.id)
        self.assertIn(place_key, all_objects)

    def test_new_method(self):
        """Test the 'new' method."""

        test_user = User()

        storage.new(test_user)
        storage.save()

        all_objects = storage.all()

        user_key = 'User.{}'.format(test_user.id)
        self.assertIn(user_key, all_objects)

    def test_delete_method(self):
        """Test the 'delete' method."""

        test_user = User()

        storage.new(test_user)
        storage.save()

        storage.delete(test_user)
        storage.save()

        all_objects = storage.all()

        user_key = 'User.{}'.format(test_user.id)
        self.assertNotIn(user_key, all_objects)


if __name__ == '__main__':
    unittest.main()
