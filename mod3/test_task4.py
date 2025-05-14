# -------------------------------------
# Задача 4. Доверяй, но проверяй
import unittest
from freezegun import freeze_time
from mod3.person import Person

class TestPersonClass(unittest.TestCase):

    def setUp(self):

        self.person = Person('Anton Antonov', 2000, 'Yekaterinburg')

    @freeze_time("2024-12-23")
    def test_get_age(self):

        self.assertEqual(self.person.get_age(), 24)

    def test_get_name(self):

        self.assertEqual(self.person.get_name(), 'Anton Antonov')

    def test_set_name(self):

        self.person.set_name('Ivan Ivanov')
        self.assertEqual(self.person.get_name(), 'Ivan Ivanov')

    def test_set_address(self):

        self.person.set_address('Moscow')
        self.assertEqual(self.person.get_address(), 'Moscow')

    def test_get_address(self):

        self.assertEqual(self.person.get_address(), 'Yekaterinburg')

    def test_is_homeless_1(self):

        self.assertFalse(self.person.is_homeless())

    def test_is_homeless_2(self):

        self.person.set_address('')
        self.assertTrue(self.person.is_homeless())

# python3 -m unittest mod3.test_task4 -v (cd..)
