import unittest
import console
import os
import uuid
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestHBNB_prompt(unittest.TestCase):

    def testprompt(self):
        self.assertEqual('(hbnb)', HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestConsole(unittest.TestCase):
    """
    Test cases for the console
    """
    jsfile_test = 'consoletest.json'
    err = {'CLS_MISS': "** class name missing **",
           'CLS_NOEX': "** class doesn't exist **",
           'ID_MISS': "** instance id missing **",
           'ID_NOEX': "** no instance found **",
           'NO_ATTR': "** attribute name missing **",
           'NO_VAL': "** value missing **"}
    cls_list = ['BaseModel',
                'Amenity',
                'City',
                'Place',
                'Review',
                'State',
                'User']

    def tearDown(self):
        """set enviroment when testing is finished"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_help(self):
        """Test for help a command that doesnt exist
        """
        _help = "*** No help on hello\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help hello")
            self.assertEqual(f.getvalue(), _help)

    def test_unknown(self):
        """ Command that does not exist """
        msg = "*** Unknown syntax: asd\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("asd")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    @classmethod
    def setUpClass(cls):
        """Set up for every test
        """
        FileStorage._FileStorage__file_path = TestConsole.jsfile_test

    def test_console_documented(self):
        """Console has some documentation?
        """
        self.assertTrue
        self.assertTrue
        (len(HBNBCommand.__doc__) >= 1)

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
