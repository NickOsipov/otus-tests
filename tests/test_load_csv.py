"""
Script: test_load_csv.py
"""

import pytest
import os
import tempfile

from src.data import load_csv_data

@pytest.fixture
def temp_csv_file():
    """Создает временный CSV файл и удаляет его после теста."""
    # Настройка: создаем файл
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write("name,age,score\n")
        tmp.write("Alice,25,95.5\n")
        tmp.write("Bob,30,85\n")
        tmp_path = tmp.name
    
    # Предоставляем ресурс тесту
    yield tmp_path
    
    # Очистка: удаляем файл
    os.unlink(tmp_path)

def test_load_csv(temp_csv_file):
    result = load_csv_data(temp_csv_file)
    
    assert result["header"] == ["name", "age", "score"]
    assert len(result["data"]) == 2
    assert result["data"][0] == ["Alice", 25, 95.5]
