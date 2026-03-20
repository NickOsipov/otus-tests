"""
Script: test_statistics.py
"""

import pytest

from src.statistics import mean_value

@pytest.mark.parametrize("input_data,expected", [
    ([1, 2, 3, 4], 2.5),
    ([0, 0, 0, 0], 0),
    ([5], 5),
    ([], 0)
])
def test_mean_value(input_data, expected):
    """Тестирует функцию среднего значения с разными входными данными."""
    assert mean_value(input_data) == expected
