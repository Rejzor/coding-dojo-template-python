import unittest
class Basket():
	def __init__(self):
		self.count = 0
	def counter(self):
		return self.count
	def addbook(self,id):
		self.count += 1
	def basketvalue(self):
		return 8

class ExampleTest(unittest.TestCase):
    def test_emptybasket(self):
    	basket = Basket()
    def test_emptybasketcount(self):
    	basket = Basket()
    	self.assertEquals(0, basket.counter())
    def test_addbook(self):
    	basket = Basket()
    	basket.addbook(1)
    	self.assertEquals(1, basket.counter())
    	self.assertEquals(8, basket.basketvalue())
if __name__ == '__main__':
    unittest.main()