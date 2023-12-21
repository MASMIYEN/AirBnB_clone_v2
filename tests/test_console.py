import unittest
from unittest.mock import Mock, patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from io import StringIO

# Mock storage to avoid side effects
storage = Mock()

# Redirect stdout to capture print statements
class TestConsole(unittest.TestCase):

    def setUp(self):
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    # Test cases for do_create method
    def test_do_create_no_args(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** class name missing **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("create")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_create_with_args(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "User.name: 'John Doe'"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("create User name=\"John Doe\"")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_create_with_underscore(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "User.name: 'John Doe'"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("create User name=\"John_Doe\"")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_create_nonexistent_class(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** class doesn't exist **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("create NonExistentClass")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    # Test cases for do_show method
    def test_do_show_existing_object(self):
        # Arrange
        cmd = HBNBCommand()
        storage.__objects = {"User.1234": "User object (1234)"}
        expected_output = "User object (1234)"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("show User 1234")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_show_no_id(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** instance id missing **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("show User")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_show_nonexistent_class(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** class doesn't exist **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("show NonExistentClass 1234")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    # Test cases for do_destroy method
    def test_do_destroy_existing_object(self):
        # Arrange
        cmd = HBNBCommand()
        storage.__objects = {"User.1234": "User object (1234)"}

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("destroy User 1234")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertEqual(output, "")

    def test_do_destroy_no_id(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** instance id missing **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("destroy User")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_destroy_nonexistent_class(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** class doesn't exist **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("destroy NonExistentClass 1234")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    # Test cases for do_all method
    def test_do_all_no_class(self):
        # Arrange
        cmd = HBNBCommand()
        storage.all.return_value = {
            "User.1234": "User object (1234)",
            "Place.5678": "Place object (5678)"
        }
        expected_output = "['User object (1234)', 'Place object (5678)']"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("all")

        # Assert
        output = self.mock_stdout.getvalue().strip()
        self.assertIn(expected_output, output)

    def test_do_all_specific_class(self):
        # Arrange
        cmd = HBNBCommand()
        storage.all.return_value = {
            "User.1234": "User object (1234)"
        }
        expected_output = "['User object (1234)']"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("all User")

        # Assert
        output = self.mock_stdout.getvalue().strip()
        self.assertIn(expected_output, output)

    def test_do_all_nonexistent_class(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** class doesn't exist **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("all NonExistentClass")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    # Test cases for do_update method
    def test_do_update_existing_object(self):
        # Arrange
        cmd = HBNBCommand()
        storage.all.return_value = {"User.1234": BaseModel()}

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("update User 1234 name \"John Doe\"")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertEqual(output, "")

    def test_do_update_no_attribute(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** attribute name missing **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("update User 1234")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_update_no_id(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** instance id missing **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("update User")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

    def test_do_update_nonexistent_class(self):
        # Arrange
        cmd = HBNBCommand()
        expected_output = "** class doesn't exist **\n"

        # Act
        with patch('sys.stdout', self.mock_stdout):
            cmd.onecmd("update NonExistentClass 1234 name \"John Doe\"")

        # Assert
        output = self.mock_stdout.getvalue()
        self.assertIn(expected_output, output)

if __name__ == '__main__':
    unittest.main()
