"""
Script: test_module_scope.py
"""

import pytest

@pytest.fixture(scope="module")
def large_dataset():
    """Создает большой набор данных один раз для всех тестов в модуле."""
    print("Preparing large dataset...") # Демонстрация, что код выполняется один раз
    data = [i for i in range(1000)]
    return data

def test_dataset_sum(large_dataset):
    assert sum(large_dataset) == 499500

def test_dataset_first_elem(large_dataset):
    assert large_dataset[0] == 0