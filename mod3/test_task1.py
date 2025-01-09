import unittest
from freezegun import freeze_time
from previous_tasks.hello_world import app

class TestModule2Task4(unittest.TestCase):

    def setUp(self) -> None:

        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.base_url = '/hello-world/'
        self.username_default = 'username'

    def test_username(self):

        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(self.username_default in response_text)

        username = 'Anton'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

        username = 'AntonAntonAnton'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

        username = 'Anton Anton'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

        username = 'Хорошего дня!'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2024-12-23")
    def test_weekday_monday(self):

        correct_greeting = 'Хорошего понедельника!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

    @freeze_time("2024-12-24")
    def test_weekday_tuesday(self):

        correct_greeting = 'Хорошего вторника!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

    @freeze_time("2024-12-25")
    def test_weekday_wednesday(self):

        correct_greeting = 'Хорошей среды!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

    @freeze_time("2024-12-26")
    def test_weekday_thursday(self):

        correct_greeting = 'Хорошего четверга!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

    @freeze_time("2024-12-27")
    def test_weekday_friday(self):

        correct_greeting = 'Хорошей пятницы!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

    @freeze_time("2024-12-28")
    def test_weekday_saturday(self):

        correct_greeting = 'Хорошей субботы!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

    @freeze_time("2024-12-29")
    def test_weekday_sunday(self):

        correct_greeting = 'Хорошего воскресенья!'
        response = self.app.get(self.base_url + self.username_default)
        response_text = response.data.decode()
        self.assertTrue(correct_greeting in response_text)

# python3 -m unittest test_task1.py -v