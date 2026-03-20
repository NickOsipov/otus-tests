"""
Script: test_data.py
"""

import unittest
from src.preprocessing import min_max_normalize

class TestMinMaxNormalize(unittest.TestCase):
    
    def test_normalize_positive_values(self):
        data = [1, 2, 3, 4, 5]
        result = min_max_normalize(data)
        # result = [0.0, 0.25, 0.5, 0.75, 1.0]
        
        self.assertEqual(min(result), 0)
        self.assertEqual(max(result), 1)
        self.assertEqual(result[1], 0.25)  # (2-1)/(5-1) = 0.25
        self.assertEqual(result[2], 0.5)   # (3-1)/(5-1) = 0.5
        
    def test_normalize_negative_values(self):
        data = [-10, -5, 0, 5, 10]
        result = min_max_normalize(data)
        
        self.assertEqual(min(result), 0)
        self.assertEqual(max(result), 1)
        self.assertEqual(result[1], 0.25)  # (-5-(-10))/(10-(-10)) = 0.25
        self.assertEqual(result[3], 0.75)  # (5-(-10))/(10-(-10)) = 0.75
        
    def test_normalize_same_values(self):
        data = [7, 7, 7, 7]
        result = min_max_normalize(data)
        
        self.assertEqual(result, [0.5, 0.5, 0.5, 0.5])
        
    def test_normalize_empty_list(self):
        data = []
        result = min_max_normalize(data)
        
        self.assertEqual(result, [])
        
    def test_normalize_single_value(self):
        data = [42]
        result = min_max_normalize(data)
        
        self.assertEqual(result, [0.5])  # Особый случай - один элемент
