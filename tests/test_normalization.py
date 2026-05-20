"""
Script: test_normalization.py
Description: Тесты для функции min_max_normalize из модуля preprocessing.py
"""

from src.preprocessing import min_max_normalize


def test_normalize_positive_values():
    data = [1, 2, 3, 4, 5]
    normalized = min_max_normalize(data)
    
    assert min(normalized) == 0
    assert max(normalized) == 1
    assert normalized[1] == 0.25
    assert normalized[2] == 0.5

def test_normalize_empty_list():
    assert min_max_normalize([]) == []
