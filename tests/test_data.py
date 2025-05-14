"""
Script: test_data.py
"""

import pytest
import os
import tempfile

# Импортируем тестируемые функции
from src.data import load_csv_data, split_data

# Тесты для функции загрузки CSV
def test_load_csv_with_header():
    # Создаем временный CSV файл для тестирования
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write("name,age,score\n")
        tmp.write("Alice,25,95.5\n")
        tmp.write("Bob,30,85\n")
        tmp_path = tmp.name
    
    try:
        # Загружаем данные из созданного файла
        result = load_csv_data(tmp_path, header=True)
        
        # Проверяем заголовок
        assert result["header"] == ["name", "age", "score"]
        
        # Проверяем данные
        assert len(result["data"]) == 2
        assert result["data"][0] == ["Alice", 25, 95.5]
        assert result["data"][1] == ["Bob", 30, 85]
        
    finally:
        # Удаляем временный файл
        os.unlink(tmp_path)

def test_load_csv_without_header():
    # Создаем временный CSV файл без заголовка
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write("Alice,25,95.5\n")
        tmp.write("Bob,30,85\n")
        tmp_path = tmp.name
    
    try:
        # Загружаем данные без заголовка
        result = load_csv_data(tmp_path, header=False)
        
        # Проверяем, что заголовок None
        assert result["header"] is None
        
        # Проверяем данные
        assert len(result["data"]) == 2
        assert result["data"][0] == ["Alice", 25, 95.5]
        assert result["data"][1] == ["Bob", 30, 85]
        
    finally:
        # Удаляем временный файл
        os.unlink(tmp_path)

def test_load_csv_empty_file():
    # Создаем пустой CSV файл
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp_path = tmp.name
    
    try:
        # Загружаем данные из пустого файла
        result = load_csv_data(tmp_path, header=False)
        
        # Проверяем, что данные пусты
        assert result["header"] is None
        assert result["data"] == []
        
    finally:
        # Удаляем временный файл
        os.unlink(tmp_path)

# Тесты для функции разделения данных
def test_split_data_even():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Разделяем данные 80/20
    first, second = split_data(data, split_ratio=0.8)
    
    assert len(first) == 8
    assert len(second) == 2
    assert first == [1, 2, 3, 4, 5, 6, 7, 8]
    assert second == [9, 10]

def test_split_data_odd():
    data = [1, 2, 3, 4, 5]
    
    # Разделяем данные 60/40
    first, second = split_data(data, split_ratio=0.6)
    
    assert len(first) == 3
    assert len(second) == 2
    assert first == [1, 2, 3]
    assert second == [4, 5]

def test_split_data_empty():
    data = []
    
    # Разделяем пустой список
    first, second = split_data(data, split_ratio=0.5)
    
    assert first == []
    assert second == []

def test_split_data_invalid_ratio():
    data = [1, 2, 3, 4, 5]
    
    # Проверяем, что функция вызывает исключение при недопустимом split_ratio
    with pytest.raises(ValueError):
        split_data(data, split_ratio=0)
    
    with pytest.raises(ValueError):
        split_data(data, split_ratio=1)
    
    with pytest.raises(ValueError):
        split_data(data, split_ratio=1.5)
