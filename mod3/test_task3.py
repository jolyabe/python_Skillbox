# -------------------------------------
# Задача 3. Учёт финансов
import unittest
from mod2.accounting import app, storage

class TestModule2Task7(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()

        cls.base_url_add = '/add/'
        cls.base_url_calculate = '/calculate/'

    def setUp(self):

        storage.update({2024: {'total': 12500,
                               3: {'total': 3250,
                                    1: 500,
                                    15: 1750,
                                    27: 1000},
                               12: {'total': 9250,
                                    5: 2050,
                                    25: 7200}},
                        2000: {'total': 1000,
                               9: {'total': 1000,
                                    28: 1000}}})

    def tearDown(self):

        storage.clear()

    def test_add_new_record(self):

        self.app.get(self.base_url_add + '20241230/12000')
        self.assertEqual(storage.get(2024).get(12).get(30), 12000)

    def test_add_total(self):

        self.app.get(self.base_url_add + '20241230/12000')
        self.assertEqual(storage.get(2024).get('total'), 24500)
        self.assertEqual(storage.get(2024).get(12).get('total'), 21250)

    def test_add_invalid_date(self):
        with self.assertRaises(ValueError):
            self.app.get(self.base_url_add + '2024_1230/12000')

    def test_calculate_year(self):

        test_year = 2024
        response = self.app.get(f'{self.base_url_calculate}{test_year}')
        response_text = response.data.decode()
        self.assertEqual(int(response_text), storage.get(test_year).get('total'))

    def test_calculate_year_if_empty_storage(self):

        storage.clear()
        test_year = 2024
        response = self.app.get(f'{self.base_url_calculate}{test_year}')
        response_text = response.data.decode()
        self.assertEqual(f'Нет данных за {test_year} год', response_text)

    def test_calculate_year_month(self):

        test_year = 2000
        test_month = 9
        response = self.app.get(f'{self.base_url_calculate}{test_year}/{test_month}')
        response_text = response.data.decode()
        self.assertEqual(int(response_text), storage.get(2000).get(9).get('total'))

    def test_calculate_year_month_if_empty_storage(self):

        storage.clear()
        test_year = 2024
        test_month = 3
        response = self.app.get(f'{self.base_url_calculate}{test_year}/{test_month}')
        response_text = response.data.decode()
        self.assertEqual(f'Нет данных за {test_year} год и {test_month} месяц', response_text)

# python3 -m unittest mod3.test_task3 -v (cd ..)