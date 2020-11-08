import unittest
import random
import hash_table

class TestMain(unittest.TestCase):

    def test_hash_table(self):
        # make sure that the hash table is created and
        # contains the correct data given
        result = None
        test_data = [['boulder', 0], ['denver', 20]]
        table = hash_table.Hash_Table(size=2000)
        self.assertIsNotNone(table)
        for data in test_data:
            table.put(data[0], data[1])
        print(table.get(test_data[1][0]))
        self.assertEqual(table.get(test_data[1][0]), [20])
        self.assertEqual(table.get(test_data[0][0]), [0])


if __name__ == '__main__':
    unittest.main()
