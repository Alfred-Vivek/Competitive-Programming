import unittest

def find_repeat(numbers_list):
    n = len(numbers_list)-1
    x = n*(n+1)/2
    y = 0
    for i in numbers_list:  y += i
    return y - x

# Test Cases

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)