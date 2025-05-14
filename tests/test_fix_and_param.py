"""
Script: test_processor.py
"""

import pytest


def process_value(processor, value):
    """
    Применяет процессор к значению.
    
    Parameters
    ----------
    processor : dict
        Словарь с параметрами процессора.
    value : any
        Значение для обработки.
    
    Returns
    -------
    any
        Обработанное значение.
    """
    processor_name = {
        "Multiplier": lambda x: x * 2,
        "Adder": lambda x: x + 1,
    }

    if processor["name"] in processor_name:
        return processor_name[processor["name"]](value)
    else:
        raise ValueError(f"Unknown processor: {processor['name']}")

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