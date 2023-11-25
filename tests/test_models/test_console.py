#!/usr/bin/python3
"""Unittest module for the console"""

import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Class that tests the HBNBCommand console"""

    def setUp(self):
        """Function to set up test environment"""
        # Reset storage before each test
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Not FileStorage")
    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            uuid = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().onecmd(f'show BaseModel {uuid}')
                output = mock_stdout.getvalue().strip()
                self.assertIn(uuid, output)

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            uuid = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().onecmd(f'destroy BaseModel {uuid}')
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, '')
                # Verify the object is actually destroyed
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    HBNBCommand().onecmd(f'show BaseModel {uuid}')
                    output_show = mock_stdout.getvalue().strip()
                    self.assertEqual(output_show, '** no instance found **')

    def test_all(self):
        """Test the all command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            uuid = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().onecmd('all')
                output = mock_stdout.getvalue().strip()
                self.assertIn(uuid, output)

    def test_count(self):
        """Test the count command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().onecmd('count BaseModel')
                count = mock_stdout.getvalue().strip()
                self.assertEqual(count, '1')

    def test_update(self):
        """Test the update command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            uuid = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().onecmd
                (f'update BaseModel {uuid} name "new_name"')
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, '')
                # Verify the object is actually updated
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    HBNBCommand().onecmd(f'show BaseModel {uuid}')
                    output_show = mock_stdout.getvalue().strip()
                    self.assertIn('new_name', output_show)

    def test_quit(self):
        """Test the quit command"""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd('quit')

    def test_EOF(self):
        """Test the EOF command"""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd('EOF')

    def test_emptyline(self):
        """Test the emptyline command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '')

    def test_docstrings(self):
        """Test the presence of docstrings"""
        for attr_name in dir(HBNBCommand):
            attr = getattr(HBNBCommand, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                self.assertTrue
                (attr.__doc__, f"Docstring missing for {attr_name}")


if __name__ == '__main__':
    unittest.main()
