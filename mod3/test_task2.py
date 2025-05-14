# -------------------------------------
# Задача 2. Дешифратор
import unittest
from mod2.decrypt import decrypt

class TestModule2Task3(unittest.TestCase):

    def test_one_dot(self):

        one_dot = {'абра-кадабра.': 'абра-кадабра',
                   '.': ''}

        for code, decode in one_dot.items():
            with self.subTest(code = code):
                result = decrypt(code)
                self.assertEqual(decode, result)

    def test_two_dots(self):

        two_dots = {'абраа..-кадабра': 'абра-кадабра',
                    'абра--..кадабра': 'абра-кадабра'}

        for code, decode in two_dots.items():
            with self.subTest(code = code):
                result = decrypt(code)
                self.assertEqual(decode, result)

    def test_multiple_dots(self):

        multiple_dots = {'абраа..-.кадабра': 'абра-кадабра',
                         'абрау...-кадабра': 'абра-кадабра',
                         'абра........': '',
                         'абр......а.': 'а',
                         '1..2.3': '23',
                         '1.......................': ''}

        for code, decode in multiple_dots.items():
            with self.subTest(code = code):
                result = decrypt(code)
                self.assertEqual(decode, result)

# python3 -m unittest mod3.test_task2 -v (cd ..)