# -------------------------------------
# Задача 3. Заглушка исключений (тестирование)
import unittest
from task3 import BlockErrors

class TestTask3BlockErrors(unittest.TestCase):

    def test_ZeroDivisionError_exception(self):

        with self.assertRaises(ZeroDivisionError):

            errors = {TypeError}
            with BlockErrors(errors):
                a = 1 / 0

    def test_ZeroDivisionError_ignore(self):

        errors = {ZeroDivisionError}
        try:
            with BlockErrors(errors):
                a = 1 / 0
        except ZeroDivisionError:
            self.fail()

    def test_TypeError_exception(self):

        with self.assertRaises(TypeError):

            errors = {ZeroDivisionError}
            with BlockErrors(errors):
                a = 1 / '0'

    def test_TypeError_ignore(self):

        errors = {TypeError}
        try:
            with BlockErrors(errors):
                a = 1 / '0'
        except TypeError:
            self.fail()

    def test_Exception_ignore(self):

        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
        except Exception:
            self.fail()

    def test_noBlockErrors(self):

        with self.assertRaises(TypeError):
            err_types = {}
            with BlockErrors(err_types):
                a = 1 / '0'

    def test_nested_BlockErrors_ignore(self):

        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):

                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
        except (ZeroDivisionError, TypeError):
            self.fail()

if __name__ == '__main__':
    unittest.main()
