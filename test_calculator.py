import unittest
from calculator import add,subtract,multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,4), 5)
        self.assertNotEqual(add(-1,1),5)
        self.assertAlmostEqual(add(11.0, 2.3), 13.3)

    def test_subtract(self):
        self.assertEqual(subtract(1,2), -1)
        self.assertLess(subtract(0,2), -1)
        self.assertNotEqual(subtract(1.0,1.0), 0.00000001)

    def test_multiply(self):
        self.assertEqual(multiply(2,5),10)
        self.assertNotEqual(multiply(2,0),10)
        self.assertAlmostEqual(multiply(2,5.0),10.00000001)

    def test_divide(self):
        self.assertEqual(divide(2,1),2)
        with self.assertRaises(ValueError):
            divide(10,0)



if __name__=="__main__":
    unittest.main()