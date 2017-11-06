import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(result, 2) 
    def test_subtract(self):
        result = rpn.calculate('7 1 -')
        self.assertEqual(result, 6)

