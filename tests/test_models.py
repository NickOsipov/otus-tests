"""
Script: test_models.py
"""

import pytest

from src.models import MeanPredictor

@pytest.mark.parametrize("X,y,expected_mean", [
    ([1, 2, 3], [10, 20, 30], 20.0),                # Базовый случай
    ([1, 2, 3], [5, 5, 5], 5.0),                    # Одинаковые значения
    ([1, 2, 3], [0, 100], 50.0),                    # Разные размеры X и y
    ([1], [42], 42.0),                              # Один элемент
])
def test_mean_predictor_fit(X, y, expected_mean):
    """Проверяет, что модель правильно вычисляет среднее значение."""
    model = MeanPredictor()
    model.fit(X, y)
    
    assert model.mean == expected_mean
    assert model.is_fitted == True

@pytest.mark.parametrize("fit_X,fit_y,pred_X,expected_pred", [
    ([1, 2], [10, 20], [3, 4, 5], [15.0, 15.0, 15.0]),     # Базовый случай
    ([1], [42], [1, 2, 3, 4], [42.0, 42.0, 42.0, 42.0]),   # Одно обучающее значение
])
def test_mean_predictor_predict(fit_X, fit_y, pred_X, expected_pred):
    """Проверяет, что модель корректно предсказывает средние значения."""
    model = MeanPredictor()
    model.fit(fit_X, fit_y)
    
    predictions = model.predict(pred_X)
    
    assert predictions == expected_pred
    assert len(predictions) == len(pred_X)

@pytest.mark.parametrize("error_case", ["no_fit", "empty_y"])
def test_mean_predictor_errors(error_case):
    """Проверяет, что модель корректно обрабатывает ошибки."""
    model = MeanPredictor()
    
    if error_case == "no_fit":
        # Тест на предсказание без обучения
        with pytest.raises(ValueError, match="не обучена"):
            model.predict([1, 2, 3])
    elif error_case == "empty_y":
        # Тест на обучение с пустым y
        with pytest.raises(ValueError, match="не может быть пустым"):
            model.fit([1, 2, 3], [])