"""
Script: test_normalization.py
"""

import pytest

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


@pytest.mark.parametrize("input_data,expected_min,expected_max", [
    ([1, 2, 3, 4, 5], 0.0, 1.0),              # Положительные числа
    ([-10, 0, 10], 0.0, 1.0),                 # Отрицательные и положительные
    ([100, 200, 300], 0.0, 1.0),              # Большие числа
])
def test_min_max_normalize_bounds(input_data, expected_min, expected_max):
    """Проверяет, что после нормализации мин. значение = 0, макс. = 1."""
    normalized = min_max_normalize(input_data)
    assert normalized[0] == expected_min  # Первое значение (минимальное)
    assert normalized[-1] == expected_max  # Последнее значение (максимальное)


@pytest.mark.parametrize("data,expected", [
    ([7, 7, 7], [0.5, 0.5, 0.5]),           # Одинаковые значения
    ([], []),                               # Пустой список
])
def test_min_max_normalize_special_cases(data, expected):
    """Проверяет особые случаи нормализации."""
    normalized = min_max_normalize(data)
    assert normalized == expected


@pytest.mark.parametrize("data,position,expected", [
    ([0, 5, 10], 1, 0.5),                # Середина диапазона
    ([10, 20, 30, 40], 1, 1/3),          # В первой трети диапазона
    ([0, 10, 20, 30, 40], 2, 0.5),       # Ровно посередине
])
def test_min_max_normalize_values(data, position, expected):
    """Проверяет конкретные значения после нормализации."""
    normalized = min_max_normalize(data)
    assert pytest.approx(normalized[position]) == expected