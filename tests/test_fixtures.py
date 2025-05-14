import pytest

@pytest.fixture
def sample_data():
    """Создает тестовый набор данных."""
    return [1, 2, 3, 4, 5]

def test_data_sum(sample_data):
    assert sum(sample_data) == 15

def test_data_length(sample_data):
    assert len(sample_data) == 5