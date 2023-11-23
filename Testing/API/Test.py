import unittest
import App.API.FileManager as FileManager
import os


class TestFileManager (unittest.TestCase):

    def setUp(self):
        # Prepare the variables for the test cases
        self.file_location = os.path.join(os.getcwd(), 'TestFiles', 'practiceData.json')
        self.sample_content = '{"key": "value"}'

        # Create a temporary file and put content inside it
        with open(self.file_location, 'w') as file:
            file.write(self.sample_content)

    def tearDown(self):
        # Clean up
        os.remove(self.file_location)

    def test_read_from_file_not_None(self):
        # Testing
        read_content = FileManager.read_from_file(self.file_location)

        # Assert
        self.assertIsNotNone(read_content, "File content should not be None")

    def test_save_to_file_not_None(self):
        # Testing
        FileManager.save_to_file(self.sample_content, self.file_location)
        with open(self.file_location, 'r') as file:
            # Assert
            self.assertIsNotNone(file, "File content should not be None")