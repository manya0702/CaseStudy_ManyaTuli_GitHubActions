import unittest
from simple_interest import calculate_simple_interest

class TestSimpleInterest(unittest.TestCase):

    def test_calculate_simple_interest(self):
        # Test case 1: principal = 1000, rate = 5, time = 2
        self.assertEqual(calculate_simple_interest(1000, 5, 2), 100.0)

        # Test case 2: principal = 1500, rate = 4.5, time = 3
        self.assertEqual(calculate_simple_interest(1500, 4.5, 3), 202.5)

        # Test case 3: principal = 2000, rate = 3, time = 1
        self.assertEqual(calculate_simple_interest(2000, 3, 1), 60.0)

        # Test case 4: principal = 0, rate = 5, time = 2
        self.assertEqual(calculate_simple_interest(0, 5, 2), 0.0)

        # Test case 5: principal = 1000, rate = 0, time = 2
        self.assertEqual(calculate_simple_interest(1000, 0, 2), 0.0)

if __name__ == '__main__':
    unittest.main()
