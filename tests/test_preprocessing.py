"""
Script: test_preprocessing.py
"""

import unittest
from src.preprocessing import min_max_normalize

class TestMinMaxNormalize(unittest.TestCase):
    
    def test_normalize_positive_values(self):
        data = [1, 2, 3, 4, 5]
        normalized = min_max_normalize(data)
        
        self.assertEqual(min(normalized), 0)
        self.assertEqual(max(normalized), 1)
        self.assertEqual(normalized[1], 0.25)  # (2-1)/(5-1) = 0.25
        self.assertEqual(normalized[2], 0.5)   # (3-1)/(5-1) = 0.5
        
    def test_normalize_negative_values(self):
        data = [-10, -5, 0, 5, 10]
        normalized = min_max_normalize(data)
        
        self.assertEqual(min(normalized), 0)
        self.assertEqual(max(normalized), 1)
        self.assertEqual(normalized[1], 0.25)  # (-5-(-10))/(10-(-10)) = 0.25
        self.assertEqual(normalized[3], 0.75)  # (5-(-10))/(10-(-10)) = 0.75
        
    def test_normalize_same_values(self):
        data = [7, 7, 7, 7]
        normalized = min_max_normalize(data)
        
        self.assertEqual(normalized, [0.5, 0.5, 0.5, 0.5])
        
    def test_normalize_empty_list(self):
        data = []
        normalized = min_max_normalize(data)
        
        self.assertEqual(normalized, [])
        
    def test_normalize_single_value(self):
        data = [42]
        normalized = min_max_normalize(data)
        
        self.assertEqual(normalized, [0.5])  # Особый случай - один элемент

