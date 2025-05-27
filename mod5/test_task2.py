# -------------------------------------
# Задача 2. Удалённое исполнение кода (тестирование)
import unittest
from task2 import app

class TestTask2app(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"]=False
        cls.app = app.test_client()

        cls.base_url = '/run'

    def setUp(self):

        self.base_data = {"code": "print('Hello, World!', end='')",
                          "timeout": 1}

    def test_base_data(self):
        '''Проверка правильного запроса'''
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertEqual(response_text, 'Hello, World!')

    def test_code_error(self):
        '''Проверка запроса с синтаксической ошибкой в коде'''
        self.base_data['code'] = "print('Hello, World!'"
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertTrue('SyntaxError' in response_text)

    def test_timeout_error(self):
        '''Проверка запроса с бесконечным циклом'''
        self.base_data['code'] = "while True: print('Spam')"
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertTrue('Spam' in response_text)
        self.assertTrue('Code execution error: timeout error' in response_text)

    def test_range_timeout(self):
        '''Проверка верификации таймаута'''
        self.base_data['timeout'] = 31
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertTrue('Number must be between 1 and 30.' in response_text)

    def test_no_code(self):
        '''Проверка верификации кода'''
        self.base_data['code'] = ""
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertTrue('This field is required.' in response_text)

    def test_shell_injection1(self):
        '''Проверка защиты от простых инъекций shell-кода'''
        self.base_data['code'] = 'print()"; echo "hacked'
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertTrue('SyntaxError' in response_text)

    def test_shell_injection2(self):
        '''Проверка защиты от запуска дочерних процессов из кода'''
        self.base_data['code'] = "print('Hello, world!'); import subprocess; subprocess.run(['ps'])"
        response = self.app.post(self.base_url, data=self.base_data)
        response_text = response.data.decode()
        self.assertTrue('Resource temporarily unavailable' in response_text)

if __name__ == '__main__':
    unittest.main()
