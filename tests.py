import unittest
import time
import functools
import numpy as np
from functions import _min, _max, _sum, _mult

testarray = np.random.randint(1,1000, size=100)

class MyTests(unittest.TestCase):
    def test_min(self):
        start = time.time()
        self.assertEqual(_min(testarray), min(testarray))
        print('Time for min = ', time.time() - start)
    
    def test_is_min_not_list(self):
        self.assertNotIsInstance(_min(testarray), list)

    def test_max(self):
        start = time.time()
        self.assertEqual(_max(testarray), max(testarray))
        print('Time for max = ', time.time() - start)
    
    def test_sum(self):
        start = time.time()
        self.assertEqual(_sum(testarray), sum(testarray))
        print('Time for max = ', time.time() - start)
    

    def test_mult(self):
        start = time.time()
        self.assertEqual(_mult(testarray), functools.reduce(lambda x, y: x * y, testarray))
        print('Time for mult = ', time.time() - start)

if __name__ == '__main__':
    unittest.main()
    
