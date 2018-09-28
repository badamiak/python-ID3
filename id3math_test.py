import unittest
import id3math

class id3math_test(unittest.TestCase):

    def test_get_entropy1(self):
        collection = [True,True,False,False,False,False]

        result = id3math.get_entropy(collection)

        self.assertAlmostEqual(result, 0.918, places=3)

    def test_get_enthropy2(self):
        collection = [True, True, False]

        result = id3math.get_entropy(collection)

        self.assertAlmostEqual(result, 0.918, places=3)

if __name__ == '__main__':
    unittest.main()
