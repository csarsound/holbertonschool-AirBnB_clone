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
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

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

    def test_quit(self):
        """Test for help quit command
        """
        _help = 'Quit method to exit form cmd '
        _help += 'program (Usage: quit)\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), _help)

    def test_EOF(self):
        """Test for help EOF command
        """
        _help = 'EOF method to exit cmd program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), _help)

    def test_all(self):
        """Test for help all command
        """
        _help = "[Usage: all <class name>]or [Usage: all] or "\
                "[Usage: <class name>.all()]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue(), _help)

    def test_count(self):
        """Test for help count command
        """
        _help = "[Usage: <class name>.count()]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue(), _help)

    def test_create(self):
        """Test for help create command
        """
        _help = "[Usage: create <class name>]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), _help)

    def test_destroy(self):
        """Test for help EOF command
        """
        _help = "[Usage: destroy <class name> <id>] or "\
                "[Usage: <class name>.destroy(<id>)]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue(), _help)

    def test_show(self):
        """Test for help show command
        """
        _help = "[Usage: show <class name> <id>] or "\
                "[Usage: <class name>.show(<id>)]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), _help)

    def test_update(self):
        """Test for help update command
        """
        _help = "[Usage: update <class name> <id> <attribute name> "\
                '"<attribute value>"] or [Usage: <class name>.update(<id>,'\
                "<attribute name>, <attribute value>)]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue(), _help)

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

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

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

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "User.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd("create State"))
                    self.assertLess(0, len(output.getvalue().strip()))
                    testKey = "State.{}".format(output.getvalue().strip())
                    self.assertIn(testKey, storage.all().keys())
                    with patch("sys.stdout", new=StringIO()) as output:
                        self.assertFalse(HBNBCommand().onecmd("create City"))
                        self.assertLess(0, len(output.getvalue().strip()))
                        testKey = "City.{}".format(output.getvalue().strip())
                        self.assertIn(testKey, storage.all().keys())
                        with patch("sys.stdout", new=StringIO()) as output:self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                        self.assertLess(0, len(output.getvalue().strip()))
                        testKey = "Amenity.{}".format(output.getvalue().strip())
                        self.assertIn(testKey, storage.all().keys())
                        with patch("sys.stdout", new=StringIO()) as output:
                            self.assertFalse(HBNBCommand().onecmd("create Place"))
                            self.assertLess(0, len(output.getvalue().strip()))
                            testKey = "Place.{}".format(output.getvalue().strip())
                            self.assertIn(testKey, storage.all().keys())
                            with patch("sys.stdout", new=StringIO()) as output:
                                self.assertFalse(HBNBCommand().onecmd("create Review"))
                                self.assertLess(0, len(output.getvalue().strip()))
                                testKey = "Review.{}".format(output.getvalue().strip())
                                self.assertIn(testKey, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
