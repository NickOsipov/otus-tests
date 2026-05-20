"""
Script: test_fixtures_and_parametrize.py
"""


import pytest
import os
import time
import tempfile

from src.data import load_csv_data

# Фикстура для создания временных файлов разных типов
@pytest.fixture(params=[
    {"content": "name,age\nAlice,25\nBob,30", "has_header": True},
    {"content": "Alice,25\nBob,30", "has_header": False},
    {"content": "", "has_header": False}
], ids=["with_header", "without_header", "empty"])
def csv_file(request):
    """Создает временный CSV файл с разным содержимым."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write(request.param["content"])
        tmp_path = tmp.name
    
    # Возвращаем путь к файлу и информацию о наличии заголовка
    yield {"path": tmp_path, "has_header": request.param["has_header"]}
    
    # Удаляем файл после теста
    os.unlink(tmp_path)

# Тест использует фикстуру csv_file для проверки загрузки различных файлов
def test_load_csv_various_files(csv_file):
    result = load_csv_data(csv_file["path"], header=csv_file["has_header"])
    
    if csv_file["has_header"]:
        assert result["header"] is not None
    else:
        assert result["header"] is None
    
    # Пропускаем проверку данных для пустого файла
    if os.path.getsize(csv_file["path"]) == 0:
        assert result["data"] == []
        return
    
    # Проверяем данные для непустых файлов
    assert len(result["data"]) > 0