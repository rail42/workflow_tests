import unittest
import rng

class TestRng(unittest.TestCase):
    
    def test_rng(self):
        result = rng.randomFromRange(324, 1000)
        self.assertNotEqual(-1)
        self.assertTrue(324 <= result <= 1000)
