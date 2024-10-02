import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self): # Test case, counts as one test.
        self.assertEqual(add(1,4), 5) #how the function should work (operation, expected output)
        self.assertNotEqual(add(1,2), 5) #this will return OK

    def test_subtract(self):
        self.assertEqual(subtract(5,3), 2)
        self.assertAlmostEqual(subtract(13.3,2.3), 11.)
        self.assertEqual(subtract(1.0,1.0), 0.0000001) #this fails, would OK with AlmostEqual
        self.assertLess(subtract(0,2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(4,4), 16)
        self.assertNotEqual(multiply(2,0), 10)
        self.assertAlmostEqual(multiply(2,5.0), 10.0000001)

    def test_divide(self):
        self.assertEqual(divide(2,0), 0)

if __name__=="__main__":
    unittest.main() #this will look for a test class and execute it