import unittest
import linq_to_python as linq

class test_class(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value

class linq_test(unittest.TestCase):

    def test_select(self):
        item1 = test_class(1,5)
        item2 = test_class(2,6)
        
        collection = [item1, item2]

        result = linq.select(collection, lambda x: x.value)

        self.assertTrue(5 in result)
        self.assertTrue(6 in result)
        self.assertFalse(1 in result)
        self.assertFalse(2 in result)

    def test_where(self):
        item1 = test_class(1,5)
        item2 = test_class(2,6)
        
        collection = [item1, item2]

        result = linq.where(collection, lambda x: x.value == 5)

        print (result)
        self.assertTrue(item1 in result)
        self.assertFalse(item2 in result)

    def test_count(self):
        collection = [1,5,2,6,2,3,6]

        self.assertEqual(2, linq.count(collection, lambda x: x == 6))
        self.assertEqual(1, linq.count(collection, lambda x: x == 5))

    def test_to_dictionary(self):
        collection = [1,5,2,6,2,3,6]

        key_selector = lambda x: x
        value_selector = lambda x: linq.count(collection, lambda y: y == x)
        result = linq.to_dict(collection, key_selector, value_selector)

        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 1)
        self.assertEqual(result[5], 1)
        self.assertEqual(result[6], 2)


if __name__ == '__main__':
    unittest.main()