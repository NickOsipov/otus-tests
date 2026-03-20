"""
Script: test_processor.py
"""

import pytest

from src.processor import process_value

@pytest.fixture
def data_processor():
    return {"name": "Multiplier"}

@pytest.mark.parametrize("value,expected", [
    (2, 4),
    (3, 6),
    (5, 10),
    (0, 0),
    (-1, -2),
])
def test_processor_transform(data_processor, value, expected):
    # Используем фикстуру + параметризацию
    assert process_value(data_processor, value) == expected
