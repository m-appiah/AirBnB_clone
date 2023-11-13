"""Module for TestHBNBCommand class."""

import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, func, *args):
        func(*args)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.assert_stdout("", mock_stdout, HBNBCommand().onecmd, "quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.assert_stdout("", mock_stdout, HBNBCommand().onecmd, "EOF")

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            obj_dict = storage.all()
            obj_key = "BaseModel." + output
            self.assertIn(obj_key, obj_dict)

            self.assert_stdout(str(
                obj_dict[obj_key]
                ), mock_stdout, HBNBCommand().onecmd, "show BaseModel "
                + output)

    def test_destroy_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            obj_dict = storage.all()
            obj_key = "BaseModel." + output
            self.assertIn(obj_key, obj_dict)

            HBNBCommand().onecmd("destroy BaseModel " + output)
            self.assertNotIn(obj_key, storage.all())

    def test_all_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()

            self.assert_stdout(
                    output, mock_stdout, HBNBCommand().onecmd, "all BaseModel")

    def test_update_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            obj_dict = storage.all()
            obj_key = "BaseModel." + output
            self.assertIn(obj_key, obj_dict)

            HBNBCommand().onecmd(
                    "update BaseModel " + output + " name 'New Name'")
            updated_obj = storage.all()[obj_key]
            self.assertEqual(updated_obj.name, "New Name")


if __name__ == '__main__':
    unittest.main()
