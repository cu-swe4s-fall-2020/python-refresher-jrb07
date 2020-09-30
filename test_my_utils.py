
import my_utils as mu
import unittest
import random

class TestMain(unittest.TestCase):

    def test_get_column(self):
        test_results = None
        test_results = mu.get_column('covid-19-data/us-counties.csv', 1, 'Boulder', 4)
        self.assertIsNotNone(test_results)

    def test_get_column_error_mode(self):
        with self.assertRaises(SystemExit) as cm:
            mu.get_column('covid-19-data/us-counties.cs', 1, 'Boulder', 4)
        self.assertEqual(cm.exception.code, 1)

    def test_get_daily_count(self):
        test_results = None
        test_results = mu.get_daily_count(mu.get_column('covid-19-data/us-counties.csv', 1, 'Boulder', 4))
        self.assertIs(test_results[19], 18)

    def test_get_daily_count_error_mode(self):
        with self.assertRaises(SystemExit) as cm:
            mu.get_daily_count(mu.get_column('covid-19-data/us-counties.cs', 1, 'Boulder', 4))
        self.assertEqual(cm.exception.code, 1)

    def test_get_running_average(self):
        test_results = None
        test_results = mu.running_average([1, 2, 1, 2])
        self.assertAlmostEqual(test_results[0], 1.5)

    def test_get_running_average_error_mode(self):
        with self.assertRaises(SystemExit) as cm:
            mu.running_average(None)
        self.assertEqual(cm.exception.code, 2)

if __name__ == "__main__":
    unittest.main()