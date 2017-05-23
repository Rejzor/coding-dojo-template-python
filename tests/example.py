import unittest
from zad1 import suma

class ExampleTest(unittest.TestCase):
    def test_example(self):
    	res = suma(1,2)
    	self.assertEqual(res, 3)

if __name__ == '__main__':
    unittest.main()