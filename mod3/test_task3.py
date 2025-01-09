import unittest
from previous_tasks.accounting import app, storage

class TestModule2Task4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()

        cls.base_url_add = '/add/'
        cls.base_url_calculate = '/calculate/'

    def setUp(self):

        storage.update({2024: {'total': 13500,
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
        self.assertEqual(storage.get(2024).get('total'), 25500)
        self.assertEqual(storage.get(2024).get(12).get('total'), 21250)

    def test_add_invalid_date(self):
        with self.assertRaises(ValueError):
            self.app.get(self.base_url_add + '2024_1230/12000')

    def test_calculate_year(self):

        self.app.get(self.base_url_calculate + '2024')
        self.assertEqual(storage.get(2024).get('total'), 13500)

    def test_calculate_year_if_empty_storage(self):

        storage.clear()
        response = self.app.get(self.base_url_calculate + '2024')
        response_text = response.data.decode()
        self.assertEqual('Нет данных за 2024 год.', response_text)

    def test_calculate_year_month(self):

        self.app.get(self.base_url_calculate + '2000/9')
        self.assertEqual(storage.get(2000).get(9).get('total'), 1000)

    def test_calculate_year_month_if_empty_storage(self):

        storage.clear()
        response = self.app.get(self.base_url_calculate + '2024/3')
        response_text = response.data.decode()
        self.assertEqual('Нет данных за 2024 год и 3 месяц.', response_text)
