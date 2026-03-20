"""
Script: test_normalization.py
"""

from src.preprocessing import min_max_normalize

def test_normalize_positive_values():
    """Test min-max normalization with positive values."""
    data = [1, 2, 3, 4, 5]
    result = min_max_normalize(data)
    
    assert min(result) == 0
    assert max(result) == 1
    assert result[1] == 0.25
    assert result[2] == 0.5

def test_normalize_empty_list():
    """Test min-max normalization with an empty list."""
    assert min_max_normalize([]) == []
