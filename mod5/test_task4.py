# -------------------------------------
# Задача 4. Перенаправление вывода (тестирование)
import unittest
import os
from task4 import Redirect

class TestTask4Redirect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Примеры текста для потоков вывода и ошибок
        cls.stdout_sample_text = 'Sample stdout text'
        cls.stderr_sample_text = 'Sample stderr text'

        # Файлы для перенаправления потоков вывода и ошибок
        cls.stdout_filename = 'stdout.txt'
        cls.stderr_filename = 'stderr.txt'

    @classmethod
    def tearDownClass(cls):

        try:
            os.remove(cls.stdout_filename)
            os.remove(cls.stderr_filename)
        except FileNotFoundError:
            pass


    def test_stdout_to_file(self):

        with open(self.stdout_filename, 'w') as file:
            with Redirect(stdout = file):
                print(self.stdout_sample_text)

        with open(self.stdout_filename, 'r') as file:
            stdout_text = file.read()

        self.assertTrue(self.stdout_sample_text in stdout_text)


    def test_stderr_to_file(self):

        with open(self.stderr_filename, 'w') as file:
            with Redirect(stderr = file):
                raise Exception(self.stderr_sample_text)

        with open(self.stderr_filename, 'r') as file:
            stderr_text = file.read()

        self.assertTrue(self.stderr_sample_text in stderr_text)


    def test_stdout_stderr_to_file(self):

        with open(self.stdout_filename, 'w') as stdout_file, open(self.stderr_filename, 'w') as stderr_file:

            with Redirect(stdout = stdout_file, stderr = stderr_file):
                print(self.stdout_sample_text)
                raise Exception(self.stderr_sample_text)

        with open(self.stdout_filename, 'r') as stdout_file, open(self.stderr_filename, 'r') as stderr_file:

            stdout_text = stdout_file.read()
            stderr_text = stderr_file.read()

        self.assertTrue(self.stdout_sample_text in stdout_text)
        self.assertTrue(self.stderr_sample_text in stderr_text)


    def test_no_stdout_stderr_to_file(self):

        with open(self.stdout_filename, 'w') as stdout_file, open(self.stderr_filename, 'w') as stderr_file:

            with Redirect():

                print(self.stdout_sample_text)         
                raise Exception(self.stderr_sample_text)


        with open(self.stdout_filename, 'r') as stdout_file, open(self.stderr_filename, 'r') as stderr_file:

            stdout_text = stdout_file.read()
            stderr_text = stderr_file.read()

        self.assertFalse(self.stdout_sample_text in stdout_text)
        self.assertFalse(self.stderr_sample_text in stderr_text)

if __name__ == '__main__':
    unittest.main()
