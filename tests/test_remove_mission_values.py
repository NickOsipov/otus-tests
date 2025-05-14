"""
Script: test_remove_missing_values.py
"""

import pytest

from src.preprocessing import remove_missing_values

@pytest.mark.parametrize("input_data,expected", [
    ([1, None, 3, None, 5], [1, 3, 5]),                 # Базовый случай
    ([1, 2, 3, 4], [1, 2, 3, 4]),                       # Без пропущенных значений
    ([None, None, None], []),                           # Все значения пропущены
    ([], []),                                           # Пустой список
    ([None, 1, None, 2, None, 3, None], [1, 2, 3]),     # Чередующиеся значения
])
def test_remove_missing_values(input_data, expected):
    result = remove_missing_values(input_data)
    assert result == expected