"""
Script: test_parametrize.py
"""

import pytest

def mean_value(data):
    """Возвращает среднее значение списка."""
    if not data:
        return 0
    return sum(data) / len(data)

@pytest.mark.parametrize("input_data,expected", [
    ([1, 2, 3, 4], 2.5),
    ([0, 0, 0, 0], 0),
    ([5], 5),
])
def test_mean_value(input_data, expected):
    """Тестирует функцию среднего значения с разными входными данными."""
    assert mean_value(input_data) == expected