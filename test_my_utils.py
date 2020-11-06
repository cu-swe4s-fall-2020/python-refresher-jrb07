
import my_utils as mu
import numpy as np
import unittest
import random


class TestMain(unittest.TestCase):

    def test_get_column(self):
        test_results = None
        test_results = mu.get_column('covid-19-data/us-counties.csv',
                                     1, 'Boulder', 4, 0)
        self.assertIsNotNone(test_results)

    def test_get_columns_dates_cases(self):
        test_results = None
        test_results = mu.get_columns('covid-19-data/us-counties.csv',
                                      1, 'Boulder', ['cases', 'date'], 0)
        self.assertEqual(test_results[0][5], '11')
        self.assertEqual(test_results[1][25], '2020-04-08')

    def test_get_column_error_mode(self):
        with self.assertRaises(SystemExit) as cm:
            mu.get_column('covid-19-data/us-counties.cs', 1, 'Boulder', 4, 0)
        self.assertEqual(cm.exception.code, 1)

    def test_date_skipping(self):
        mu.get_column('test_date_missing.csv', 1, 'Boulder', 4, 0)

    def test_no_date_column(self):
        mu.get_column('test_date_missing.csv', 1, 'Boulder', 4, None)

    def test_out_of_order_date(self):
        with self.assertRaises(SystemExit) as cm:
            mu.get_column('test_date_disorder.csv', 1, 'Boulder', 4, 0)
        self.assertEqual(cm.exception.code, 6)

    def test_get_daily_count(self):
        self.assertIs(mu.get_daily_count(
            mu.get_column('covid-19-data/us-counties.csv',
                          1, 'Boulder', 4, 0))[4], 3)

    def test_get_daily_count_error_mode(self):
        with self.assertRaises(SystemExit) as cm:
            mu.get_daily_count(mu.get_column('covid-19-data/us-counties.cs',
                                             1, 'Boulder', 4, 0))
        self.assertEqual(cm.exception.code, 1)

    def test_get_running_average(self):
        test_results = None
        test_results = mu.running_average([1, 2, 1, 2])
        self.assertAlmostEqual(test_results[0], 1.5)

    def test_get_running_average_error_mode(self):
        with self.assertRaises(SystemExit) as cm:
            mu.running_average(None)
        self.assertEqual(cm.exception.code, 3)

    def test_get_running_average_random_mode(self):
        for i in range(10):
            arr = []
            for j in range(100):
                x = random.randint(0, 10000)
                arr.append(x)
            for k in range(100):
                window = random.randint(1, 100)
                test_data, _ = mu.running_average(arr, window)
                for m in range(int(100/window)-1):
                    expected_result = np.mean(arr[m:m + window])
                    self.assertEqual(test_data[m], expected_result)


if __name__ == '__main__':
    unittest.main()
