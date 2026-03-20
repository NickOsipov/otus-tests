"""
Script: test_data.py
"""

import pytest
import os
import tempfile

# Импортируем тестируемые функции
from src.data import load_csv_data

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
        
        # Проверяем, что заголовок пустой список
        assert result["header"] == []
        
        # Проверяем данные
        assert len(result["data"]) == 2
        assert result["data"][0] == ["Alice", 25, 95.5]
        assert result["data"][1] == ["Bob", 30, 85]
        
    finally:
        # Удаляем временный файл
        os.unlink(tmp_path)

@pytest.mark.skip(reason="Функционал еще не реализован")
def test_load_csv_empty_file():
    # Создаем пустой CSV файл
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp_path = tmp.name
    
    try:
        # Загружаем данные из пустого файла
        result = load_csv_data(tmp_path, header=False)
        
        # Проверяем, что данные пусты
        assert result["header"] == []
        assert result["data"] == []
        
    finally:
        # Удаляем временный файл
        os.unlink(tmp_path)

