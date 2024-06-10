import unittest
import rng

class TestRng(unittest.TestCase):
    
    def test_rng(self):
        rng.max_number = 345
        rng.min_number = 5
        self.assertTrue(998 <= rng.rnd_number <= 1000)
